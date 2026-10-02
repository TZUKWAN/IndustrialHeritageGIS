# -*- coding: utf-8 -*-
"""阶段8 冒烟测试: OpenRouter 真实链路 (LLM 连通 + heritage_data 工具调用)。

用法(密钥经环境变量注入, 不入库):
  set OPENROUTER_API_KEY=sk-or-v1-xxx
  python data-pipeline/scripts/llm_smoke_test.py
"""
import json
import os
import sys
import time

BACKEND = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..',
                       'python-backend')
sys.path.insert(0, BACKEND)

MODEL = 'openrouter/nvidia/nemotron-3-ultra-550b-a55b:free'


def main():
    key = os.environ.get('OPENROUTER_API_KEY')
    if not key:
        print('SKIP: OPENROUTER_API_KEY not set')
        return 2

    from opengis_backend.agent.llm import LLMConfig, build_llm_caller
    cfg = LLMConfig(protocol='openai', model=MODEL, api_key=key,
                    base_url='https://openrouter.ai/api/v1')
    caller = build_llm_caller(cfg)  # 同步可调用

    # -- STEP1: 连通性(免费模型可能过载, 带退避重试)
    messages = [
        {'role': 'system', 'content': '你是地理信息系统助手。用中文简短回答。'},
        {'role': 'user', 'content': '回复"连通正常"两个字。'},
    ]
    resp = None
    for attempt in range(4):
        try:
            resp = caller(messages)
            break
        except Exception as e:
            print(f'STEP1 attempt {attempt + 1} failed: {str(e)[:140]}')
            time.sleep(5 * (attempt + 1))
    if resp is None:
        print('STEP1 FAIL: model unreachable')
        return 1
    print('STEP1 llm reply:', str(getattr(resp, 'content', resp)).replace('\n', ' ')[:100])

    # -- STEP2: heritage_data 工具已注册
    import asyncio
    from opengis_backend.tools import registry as reg_mod
    reg = reg_mod.ToolRegistry()
    asyncio.run(reg.discover_and_load())
    schemas = [s.schema for s in reg.list_by_groups(['core', 'heritage'])]
    hd = next((s for s in schemas if s.name == 'heritage_data'), None)
    print('STEP2 heritage_data registered:', bool(hd))

    # -- STEP3: function-calling 一轮(模型自主决定调用工具)
    tools_payload = [{
        'type': 'function',
        'function': {
            'name': hd.name,
            'description': hd.description,
            'parameters': {
                'type': 'object',
                'properties': {
                    p.name: {'type': 'string' if p.type == 'enum' else p.type,
                             **({'enum': p.options} if p.type == 'enum' else {}),
                             'description': p.description}
                    for p in hd.params
                },
            },
        },
    }]
    messages2 = [
        {'role': 'system', 'content': '你可以调用 heritage_data 工具查询工业遗产数据。'},
        {'role': 'user', 'content': '请查询第3批里行业为煤炭工业的遗产。'},
    ]
    resp2 = None
    for attempt in range(3):
        try:
            resp2 = caller(messages2, tools=tools_payload)
            break
        except Exception as e:
            print(f'STEP3 attempt {attempt + 1} failed: {str(e)[:140]}')
            time.sleep(5)
    called = False
    if resp2 is not None:
        s = json.dumps(resp2, ensure_ascii=False, default=str)
        called = 'heritage_data' in s
        print('STEP3 tool_call requested by model:', called, '|', s[:180])
    if not called:
        from opengis_backend.tools.builtin.heritage_tool import heritage_data
        async def run_tool():
            return await heritage_data(action='search', batch=3, industry='煤炭工业')
        r = asyncio.run(run_tool())
        print('STEP3(fallback) tool executes:', r.data['total'],
              [x['name'] for x in r.data['results'][:3]])
    return 0


if __name__ == '__main__':
    sys.exit(main())
