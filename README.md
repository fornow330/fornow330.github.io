# 传奇文字

单文件 HTML 文字传奇游戏：凡界（封顶 170）→ 雷劫飞升 → 仙界 → 破界门 → 大世界（11 个「XX域」，200~1000 级）+ 灵器 / 专属灵器系统。

- 在线玩：https://fornow330.github.io/legendword/
- 仓库结构：`legendword/index.html` 为加载器，`legendword/c00 ~ c11` 为游戏本体（gzip + base64 分片）。
- 加载顺序：fastly.jsdelivr.net → ghproxy.net → gh-proxy.com → 仓库原地址（GitHub Pages）→ 云端在线版，逐级回退；CDN 与 raw 均按提交号钉版，避免缓存与新旧分片错配。
- 主页 `index.html` 已指向 https://fornow.cc。
