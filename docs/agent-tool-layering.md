# Agent Tool Layering

OpenGIS separates executable tools into coarse tool packs.  The global tool
registry may still load every built-in tool for manual UI/RPC use, but
autonomous agent loops should see only packs that are appropriate for the
current profile.

## Current Runtime Rule

- `layout` is manual UI only. Layout composer functions stay registered for the
  frontend/RPC surface, but they are not exposed to autonomous agent loops.
- `report` is skill-led. Report generation and academic-writing workflows are
  represented by the built-in `report` skill, not by always-on function schemas.
- `manual_ui` tools are not exposed to agents. Currently this includes
  `set_basemap`, because basemap style is user/UI state.

The central classification lives in
`python-backend/opengis_backend/agent/execution/tool_packs.py`.

Normal chat turns no longer expose the whole agent profile schema.  They start
with a small default pack set:

- `skill`
- `file`
- `code`
- `map`

The runtime then adds domain packs from the current turn objective, pending
intent, and recent failures.  For example:

- layer zoom/query: default packs only.
- categorized/graduated styling: add `style`.
- TIFF/raster work: add `raster` and often `style`.
- 3D/extrusion/camera: add `map_3d`.
- resident/dynamic workers: add `worker`.
- operation repair/run: add `operation`.
- OSM requests: add `osm`.

If the model appears to confuse tool visibility with platform capability, the
runner retries internally with the full agent tool surface once.  The user
should not see "this tool is unavailable" when the platform supports the
capability.

## Pack Classes

- `skill`: load instruction/resource bundles and update user preferences.
- `file`: workspace file read/write/edit/search operations.
- `code`: Python execution and reusable scripts.
- `system`: shell execution.
- `map`: map layer and view primitives.
- `style`: vector layer styling, labels, filters, ordering, legends.
- `raster`: raster loading, inspection, and style updates.
- `map_3d`: 3D camera/view/extrusion controls.
- `operation`: reusable geoprocessing operations.
- `worker`: resident worker lifecycle and dynamic map streams.
- `workflow`: workflow creation/execution surfaces.
- `subagent`: child-agent orchestration.
- `datasource`, `osm`, `qgis`, `web`: external/data connectors.
- `layout`: manual layout composer.
- `report`: report and academic-writing workflows.
- `debug`: agent observability.

## Candidate Removals

These are not deleted yet; they are candidates for future cleanup after usage
telemetry confirms they are not needed.

- `qgis_call`: keep only if the QGIS bridge is actively supported. Otherwise it
  adds schema and failure paths for a backend that is often disconnected.
- `copy_file`, `move_file`, `delete_file`, `create_directory`: keep if agents
  need file management. Otherwise prefer `write_file` / `edit_file` plus user
  approval for destructive operations.
- `webfetch`, `websearch`: keep only for profiles that can use network access.
  In offline desktop mode they are high-confusion tools.
- `debug_agent_context`: keep for development profiles, hide from ordinary user
  profiles once the context debugger UI is mature.

## Token Impact

Measured locally on the `gis-build` profile:

- full filtered profile schema: about `15.1k` estimated tokens.
- simple map zoom/query packs: about `4.7k` estimated tokens.
- vector styling packs: about `7.2k` estimated tokens.
- raster/style packs: about `8.3k` estimated tokens.
- worker packs: about `6.7k` estimated tokens.

This shifts simple map turns from "full GIS platform" requests toward focused
provider calls without removing any registered manual/RPC tools.

## Next Architecture Step

The current implementation is a stable deterministic pack router.  The next
larger upgrade is learned pack expansion:

1. Log user request, selected packs, actually used tools, failures, token usage,
   and final success.
2. Resolve the requested capability domain from the turn objective and active
   workspace state.
3. Compare deterministic routing with the actually used successful packs.
4. If a missing-pack condition is detected, expand internally and retry without
   telling the user the platform lacks the capability.
5. After enough successful runs, replace or augment the deterministic router
   with an optional local classifier.

This keeps agent capability stable while avoiding an 80-tool schema on every
request.
