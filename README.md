# 传奇文字

单文件 HTML 文字传奇游戏：凡界（封顶 170）→ 雷劫飞升 → 仙界 → 破界门 → 大世界（11 个「XX域」，200~1000 级）+ 灵器 / 专属灵器系统。

- 在线玩：https://fornow330.github.io/legendword/
- 仓库结构：`legendword/index.html` 为加载器，`legendword/c00 ~ c12` 为游戏本体（gzip + base64 分片）。
- 加载顺序：fastly.jsdelivr.net → ghproxy.net → gh-proxy.com → 仓库原地址（GitHub Pages）→ 云端在线版，逐级回退；CDN 与 raw 均按提交号钉版。
- 主页 `index.html` 已指向 https://fornow.cc。

## 灵器系统

- 六部位：武器 / 甲 / 头巾 / 项链 / 腰带 / 鞋子。
- 品质：凡 / 灵 / 仙 / 神，上中下品；词条数按品质 3~12 条。
- 词条池 12 种，均入战斗数值；锁定词条后重铸不会改变该条，价格随锁条数上浮。
- 专属灵器：历练 / BOSS 低概率掉落，1000 级内可成长，品质自动提升；重铸仅升不降，消耗为普通灵器 10 倍。
