# 随包字体与许可

用户指定、最新确认稿和既有母版优先；下表只用于没有既定字体的首稿。

| 用途 | 默认字体与字重 | 随包文件 | 官方许可证 |
| --- | --- | --- | --- |
| 中文标题、正文 | Noto Sans SC；正文 400，标题 700／900 | [完整可变 WOFF2](../assets/fonts/NotoSansSC-VF.woff2)，100–900 | [OFL](../assets/fonts/NotoSansSC-OFL.txt) |
| 英文说明、数字、标签 | Space Grotesk；500／700 | [可变 TTF](../assets/fonts/SpaceGrotesk-VF.ttf)，300–700 | [OFL](../assets/fonts/SpaceGrotesk-OFL.txt) |
| 英文大标题 | Anton Regular；400 | [TTF](../assets/fonts/Anton-Regular.ttf) | [OFL](../assets/fonts/Anton-OFL.txt) |

## 使用方式

- Figma／Canva：先核对当前平台实际可用的字体及字重。随包文件不会自动安装到平台，也不代表有上传字体的权限或工具。平台已有该字体时直接使用；缺失时报告，并按现有工具支持的方式安装／上传或采用用户确认的替代字体。
- HTML：可引用 [fonts.css](../assets/fonts/fonts.css)，直接加载随包字体。
- 需要桌面可安装 TTF 时，在技能目录运行 `python3 scripts/prepare_fonts.py --output-dir <技能目录以外的字体文件夹>`。脚本将 Noto Sans SC 从 WOFF2 恢复为 TTF，并复制其余 TTF 与许可证；需要 Python 的 `fonttools[woff]`，不会自行安装依赖。

Noto Sans SC 官方 TTF 大于 10 MB，因此随包采用 WOFF2。该文件保留全部 31,036 个字形、30,890 个 Unicode 映射和 100–900 字重轴，未做字符子集化。恢复后的 TTF 会大于 10 MB，请不要再放回用于平台提交的 skill 文件夹。

## 来源与许可

三款字体均取自 Google Fonts 官方仓库，附各自原始 SIL Open Font License 1.1 及版权声明。它们是公开许可证文件，不是个人购买凭证。字体按各自 OFL 分发，不能用 skill 的其他许可替代。

官方来源、固定版本、文件校验值和格式转换记录见 [sources.json](../assets/fonts/sources.json)。随包内容不包含个人授权账号、下载登录信息或购买订单。
