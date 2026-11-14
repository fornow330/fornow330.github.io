# 传奇文字

单文件 HTML 文字传奇游戏：凡界（封顶 170）→ 雷劫飞升 → 仙界 → 破界门 → 大世界（11 个「XX域」，200~1000 级）+ 灵器 / 专属灵器系统。

- 在线玩：https://fornow330.github.io/legendword/
- 仓库结构：`legendword/index.html` 为加载器，`legendword/c00 ~ c11` 为游戏本体（gzip + base64 分片，共 48476 字符），加载器拼接、解压后整页渲染；分片与源文件字节一致。
- 兜底：加载器失败时自动切云端在线版。
- 主页 `index.html` 已指向 https://fornow.cc。
