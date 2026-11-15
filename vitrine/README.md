# Vitrine

Photograph, track & value your collection.

Vitrine 是一个纯前端的单文件收藏管理应用：拍照录入手办、球鞋、黑胶、乐高、卡牌等藏品，记录入手价与估值，看组合曲线，导出 CSV 与投保 PDF。

**在线试用：** https://fornow330.github.io/vitrine/

## 特点

- **单文件**：整个应用就是一个 `index.html`，CSS 与 JS 全部内联，无外部依赖、无构建步骤、无网络请求；下载下来双击就能用。
- **数据在本地**：藏品、照片、估值全部存在浏览器 IndexedDB 里，不上传任何服务器。照片在本地用 canvas 压缩（长边 2048 / 质量 0.7，缩略图 400 / 0.6）。
- **四语界面**：English / 简体中文 / Deutsch / Français，首次打开按浏览器语言自动选择，也可在设置里手动切换。
- **货币显示换算**：数据库内一律以美元分保存，展示层按当前语言换算成 USD / CNY / EUR（固定参考汇率，基准 2026-11，非实时行情）。
- **可安装 PWA**：iOS / Android 浏览器「添加到主屏幕」后全屏运行，离线可用。
- **导出**：全量 CSV（含币种列，按当前显示币种换算）、投保用的藏品清单 PDF（走打印样式表）。
- **引导**：首次打开且库为空时，自动加入一件示例藏品与一条估值，并给出去留提示。

## 使用

直接用浏览器打开 `index.html`，或访问 GitHub Pages 上的在线版。

必需三项：名称、分类、照片。7 个预置分类：手办、球鞋、黑胶、乐高、卡牌、艺术微喷、其他。

## 技术

- 原生 HTML / CSS / JS，无框架、无打包器
- IndexedDB（`items` / `photos` / `valuations` 三个 object store）
- hash 路由（`#/collection`、`#/stats`、`#/lists`、`#/settings`）
- 自写 zip 打包器（CRC32 + 本地文件头 / 中央目录 / EOCD，UTF-8 文件名标志 0x0800），不依赖 JSZip
- 曲线计算 `itemSeries` / `portfolioSeries` / `quarterlySeries` 与统计 `computeStats`

## 明确不做

云同步、后台自动备份、家庭共享、从备份恢复、去水印、抓取商品页、鉴定与估值建议、社区、爬取行情、内置品牌 logo 库。

## License

MIT，见 [LICENSE](LICENSE)。
