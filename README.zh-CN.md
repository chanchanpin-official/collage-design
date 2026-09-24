# Collage Design · 拼贴设计

[English](README.md) | 简体中文

在 **Canva 或 Figma** 中制作可编辑的拼贴海报、易拉宝和社媒图片的 Agent Skill。

确定设计目标和平台，提供文案，可选指定配色。Agent 会检索真实图片、制作拼贴主视觉、建立主题色，再在所选平台完成可编辑排版，并根据后续反馈返修。

在 Codex 中运行时，还可使用当前内置的图像生成与编辑能力，制作主视觉、纸张纹理、概念背景或局部修改。调用遵循可用的 `imagegen` skill 和实际工具接口，不限定模型版本；内置路线无需另配 API key。

Skill 指令以中文编写，使用时可按你的语言交流。

## 安装

需要 Node.js 和 npm。安装到 Codex：

```sh
npx skills add chanchanpin-official/collage-design --skill collage-design --agent codex --global
```

该命令通过 npm 运行 [Skills CLI](https://github.com/vercel-labs/skills)，从本 GitHub 仓库安装 skill。无需安装名为 `collage-design` 的独立 npm 包。

去掉 `--global` 可安装到当前项目；去掉 `--agent codex` 可选择其他支持的 Agent，其工具能力和兼容性需在对应环境中确认。

仅查看可安装的 skill：

```sh
npx skills add chanchanpin-official/collage-design --list
```

## 使用条件

- 已连接并授权 **Canva 或 Figma connector**，具备目标设计所需的创建和编辑能力。每次任务只需连接选中的平台。
- 运行环境提供网页和图片搜索能力，搜图独立于设计平台自带图库。
- 运行环境及所选 connector 支持素材处理与上传，图像操作遵循当前工具要求。

安装 skill 只会安装操作指引，不会自动安装 connector、登录账号、授予权限或提供平台付费权益。具体功能及批准要求以当前工具接口为准。

## 视觉参考

内含脱敏易拉宝、海报，以及对应的上游素材和中间图。文字与私有标识已遮盖，不包含未脱敏原稿。

示例展示真实素材选择、黑白／彩色层次、前景主体和素材上下游关系；生成概念图会单独标明。

![易拉宝：素材到成品的关系](skills/collage-design/references/visuals/rollup/flow.png)

![海报：素材到成品的关系](skills/collage-design/references/visuals/poster/flow.png)

可查看 [视觉示例](skills/collage-design/references/visual-examples.md)、[选材与层次判断](skills/collage-design/references/composition-decisions.md) 和 [图片来源索引](skills/collage-design/references/visuals/sources.md)。脱敏图用于学习构图与材料关系，不能作为像素精确的母版；遮盖矩形不属于新设计的内容。

## 使用方式

调用 `$collage-design`，提供目标形式、制作平台和需要展示的文本。按需补充尺寸、意向配色或已有设计。

## 制作流程

1. 确定输出目标：形式、尺寸或发布位置、页数及用途。实体尺寸统一用 cm，屏幕图片使用比例和像素。
2. 选择 Canva 或 Figma，固定本次制作平台并检查 connector；工具故障不会自动触发换平台。
3. 将文案整理为各级标题、正文、行动指引及辅助信息。
4. 使用指定配色，或根据主题与照片建立色板。
5. 用通用主题词检索真实图片，核对来源和使用范围，准备拼贴素材。在 Codex 中可按任务需要使用图像生成或编辑能力，尊重仅实拍、保留原像素等要求，并准确标注生成素材。
6. 在所选平台排版，保留原生可编辑文字，检查预览并确认保存。
7. 交付预览、可编辑链接和已要求的导出文件。后续返修先读取最新设计，保留人工修改。

Canva 通过当前可用的创建或导入工具起稿，再进行精修；Figma 通过上传素材和原生 Frame、文本、图层完成制作。已有确认母版优先沿用；工具无法完成的调整会明确说明，继续在同一平台处理。

## 隐私与任务文件

公开包只包含可复用指引与脱敏视觉参考。真实项目需求、对话、生成提示词、个人偏好、凭据和私有设计链接应保存在私有任务记录中。

将任务简报、素材清单、设计标识、预览、导出及交接文件保存在独立的私有项目目录，不回写到 skill 包。搜索时使用通用主题词，避免公开保密原文；上传素材时使用平台支持的私有上传方式。

## 文件导航

- [Skill 主指引](skills/collage-design/SKILL.md)
- [设计与编辑约定](skills/collage-design/references/preferences.md)
- [Canva 流程](skills/collage-design/references/canva.md)
- [Figma 流程](skills/collage-design/references/figma.md)
- [素材与交接](skills/collage-design/references/assets-and-handoff.md)
- [视觉示例与素材关系](skills/collage-design/references/visual-examples.md)
- [真实素材、黑白／彩色与前景选择](skills/collage-design/references/composition-decisions.md)

## 许可

[MIT](LICENSE) 适用于 skill 的指令和元数据。参考图片另有 [素材说明](skills/collage-design/references/visuals/NOTICE.md)，第三方照片、角色图片及其他素材仍遵循各自的使用条款。
