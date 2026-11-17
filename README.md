# fornowAI

纯静态的站点入口页：把 fornow 的小游戏与工具聚在一页，点开即玩，单文件、无框架、无构建。

- 在线：<https://fornow330.github.io/>
- 作者：fornow
- 许可：按目录分别授权，见文末

## 页面收录的站点

| 站点 | 一句话 | 地址 |
|---|---|---|
| 文字传奇 | 文字放置传奇，凡界→仙界→大世界 | <https://fornow330.github.io/legendword/> |
| 三连收纳 | 三消收纳小游戏，100 关 + 周目 | <https://fornow330.github.io/tidy-up/> |
| 二合甜品小店 | 合成经营类甜品店小游戏 | <https://fornow330.github.io/tycoon/> |
| 怪潮幸存者 | 割草塔防，无限波次、异变叠加 | <https://fornow330.github.io/cutting/> |
| 工具箱 | 小羽工具箱，常用小工具合集 | <https://fornow330.github.io/xiaoyutool/> |
| 进入主站 | 站长主页与全部作品 | <https://fornow.cc> |

## 页面本身

根目录 `index.html` 即入口页，样式与逻辑全部内联：

- 深色界面 + 站点卡片，点卡片直接打开对应站点
- 底部按仓库名搜 GitHub：`owner/repo` 精确查，关键词全站搜（按星数排序），有主页就开主页；也能贴完整网址
- 在 App 内打开时卡片改发 `fornowai://open?u=…&repo=…&path=…`，由 App 截获后走 CDN 竞速

配套 App（fornowAI）启动时先多线路竞速拉取本页，点站点同样竞速，全失败回源站。因此**新增站点只改本页 `SITES` 数组并推送，App 不用重新打包**。

## 目录

```
index.html            入口页本体
legendword/           文字传奇：game.html、加载器与资源、README.md、CREDITS.md、LICENSE
tidy-up/              三连收纳
tycoon/               二合甜品小店
vitrine/              其他页面资源
.github/workflows/    文字传奇本体同步工作流
```

## 许可

根页面与说明为 MIT；`legendword/` 为 GPL-3.0（全文见 `legendword/LICENSE`）；`vitrine/` 为 MIT（见 `vitrine/LICENSE`）；`tidy-up/`、`tycoon/` 与工作流配置按根 MIT 授权。完整对照表见根目录 `LICENSE`。
