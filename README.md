# fornowAI

一个纯静态的站点入口页：把作者 **fornow** 的几个小游戏与工具聚在同一页，点开即玩。
线上：<<https://fornow330.github.io/>>

## 页面里收录的站点

| 站点 | 简介 | 地址 |
|---|---|---|
| 文字传奇 | 单文件 HTML 文字放置传奇，凡界→仙界→大世界，170 级渡雷劫、1000 级破碎虚空 | <https://fornow330.github.io/legendword/> |
| 三连收纳 | 三消收纳小游戏 | <https://fornow330.github.io/tidy-up/> |
| 二合甜品小店 | 合成经营类甜品店小游戏 | <https://fornow330.github.io/tycoon/> |
| 怪潮幸存者 | 割草塔防，无限波次、异变叠加、周目挑战 | <https://fornow330.github.io/cutting/> |
| 工具箱 | 小羽工具箱，常用小工具合集 | <https://fornow330.github.io/xiaoyutool/> |

## 这个页面是什么

根目录 `index.html` 就是入口页本体，单文件、无框架、无构建，样式与逻辑全部内联：

- 深色界面 + 站点卡片，卡片点击直接打开对应站点
- 底部支持按仓库名搜索 GitHub：输入 `owner/repo` 精确查，输入关键词全站搜（按星数排序），有主页就直接打开主页；贴完整网址也能直接开
- 页面在 App 内打开时，卡片改发 `fornowai://open?u=…&repo=…&path=…`，由 App 截获后走 CDN 竞速

## 配套 App：fornowAI

Android WebView 外壳，启动时先竞速拉取本页（jsDelivr 各节点 + ghfast / gh-proxy / ghproxy），拿到即渲染；点站点时同样多线路竞速，先到先用，全部失败回源站。全屏沉浸、无顶栏，返回键回入口页。

因此**新增站点只改本页 `SITES` 数组并推送即可，App 无需重新打包**。

## 目录结构

```
index.html            入口页（本页面对应的页面）
fornowai/index.html   App 拉取的入口页副本（与根页面内容一致）
legendword/           文字传奇：game.html、分片 c02…、README.md、CREDITS.md、LICENSE
tidy-up/              三连收纳
tycoon/               二合甜品小店
vitrine/              其他页面资源
.github/workflows/    文字传奇本体同步工作流
```

各站点的说明文档与许可证放在各自目录下：`legendword/README.md`（玩法与系统说明）、`legendword/CREDITS.md`（第三方说明）、`legendword/LICENSE`（GPL-3.0）。

## 新增一个站点

1. 在 `index.html` 与 `fornowai/index.html` 的 `SITES` 里加一条：`name`、`desc`、`url`，GitHub 站点再补 `repo` 与 `path`（用于 CDN 加速）。
2. 推送到 `main` 分支，Pages 自动更新。
3. App 下次启动即生效。

## 许可

本仓库按目录分别授权：根页面与说明为 MIT；`legendword/` 为 GPL-3.0（全文见 `legendword/LICENSE`）；`vitrine/` 为 MIT（见 `vitrine/LICENSE`）；`tidy-up/`、`tycoon/` 与工作流配置按根 MIT 授权。完整对照表见根目录 `LICENSE`。

## 说明

页面本身不依赖任何第三方库、字体或图片；字体走系统字体栈，图标用 CSS 绘制。第三方 CDN 仅在 App 内用于内容竞速，页面直开不受影响。
