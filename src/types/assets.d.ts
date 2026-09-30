/**
 * 静态资源模块声明 (Vite)
 *  - *.geojson 以 JSON 模块导入
 *  - *.png?inline 导出 base64 data URL
 *  - *.png 默认导出 URL
 */
declare module '*.geojson' {
  const value: unknown
  export default value
}

declare module '*.png?inline' {
  const value: string
  export default value
}

declare module '*.png' {
  const value: string
  export default value
}
