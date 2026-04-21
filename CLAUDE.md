# CLAUDE.md — 实验室设备管理网站

## 项目概述
CityU Zhu Lab 实验室设备管理静态网站，基于 Astro 6 + Tailwind CSS。
- **在线地址**：https://programmlearner.github.io/zhu-lab-equipment/
- **仓库**：https://github.com/programmlearner/zhu-lab-equipment
- **部署**：`git push` → GitHub Actions 自动构建 → GitHub Pages

---

## 目录结构（关键路径）

```
content/equipment/     ← 每台设备一个 .md（日常只改这里）
public/images/         ← 设备 JPEG 图片（命名：品牌-型号.jpg，小写连字符）
public/manuals/        ← 说明书文件，按类别子目录存放
  ├── 测量仪器/
  ├── 电源设备/
  ├── 仿真平台/
  ├── 软件工具/
  └── 计算平台/
src/content.config.ts  ← Content Collection schema
src/pages/index.astro  ← 首页（筛选栏 statuses 数组在此）
src/components/DeviceCard.astro
src/pages/equipment/[slug].astro
```

---

## 查阅设备手册的优先级

**当需要查询设备参数、使用方法或技术细节时，优先使用 `.md` 格式文档，而非 `.pdf`。**

原因：`.md` 文档对 AI 解析更友好，内容直接可读，检索效率更高。

| 设备 | 优先查阅（.md） | 备用（.pdf） |
|------|----------------|-------------|
| Danfoss VLT FC302 | `public/manuals/电源设备/danfoss-fc302-manual.md` | `danfoss-fc302-manual.pdf` |
| Danfoss FC302 Datasheet | `public/manuals/电源设备/danfoss-fc302-datasheet.md` | `danfoss-fc302-datasheet.pdf` |

未来新增的 `.md` 手册均存放在 `public/manuals/<类别>/` 目录下，命名规则：`<品牌-型号>-manual.md` 或 `<品牌-型号>-datasheet.md`。

---

## 添加新设备的标准流程

### 1. 准备图片
```bash
# 转换 HEIC（iPhone 照片）→ JPEG
PYTHON="/c/Users/Xiangyu.Cityus/AppData/Local/Programs/Python/Python312/python.exe"
"$PYTHON" convert_heic.py
```
注意：**不能直接用 `python` 命令**，必须用完整路径（Windows Store Python 存根在 Git Bash 下无效）。

压缩规范（运行 `compress_images.py`）：
- 最大宽度：1200px
- JPEG quality：82
- 旋转修正：使用 `img.rotate(angle, expand=True)`（Pillow 不自动处理 EXIF 方向）

### 2. 创建设备 .md 文件

路径：`content/equipment/<品牌-型号>.md`

```yaml
---
name: "设备中文名"
category: "测量仪器"      # 见下方枚举
tags: ["标签1", "标签2"]
brand: "品牌"
model: "型号"
location: "实验室 A"      # 可选
status: "可用"            # 见下方枚举
image: "/images/品牌-型号.jpg"
manual_pdf: "/manuals/<类别>/文件名.pdf"    # 可选
datasheet_pdf: "/manuals/<类别>/文件名.pdf" # 可选
specs:
  参数名: "参数值"         # z.record(string, string)，值必须是字符串
---

## 简介
...

## 快速使用
1. ...

## 注意事项
- ...
```

### 3. 部署
```bash
git add .
git commit -m "add: 设备名称"
git push   # Actions 自动部署，约 1 分钟生效
```

---

## 枚举值（不可随意修改，否则 schema 报错）

**status**（`src/content.config.ts` 定义）：
- `可用` — 绿色
- `使用中` — 黄色
- `维修中` — 红色
- `待到货` — 紫色

**category**（自由字符串，但保持一致）：
- `测量仪器` / `电源设备` / `开关控制` / `计算平台`
- `网络设备` / `工具` / `耗材`
- `仿真平台` / `软件工具`

---

## 环境要求

| 工具 | 版本 |
|------|------|
| Node.js | ≥ 22.12.0（Astro 6 强制要求） |
| npm | ≥ 9 |
| Python | 3.12（路径见上） |
| Pillow | 已安装（`pillow-heif` 也已安装） |

```bash
npm run dev    # 本地预览 http://localhost:4321
npm run build  # 构建到 dist/（验证无报错）
```

---

## 已知约定

- `astro.config.mjs` 中 `base: '/zhu-lab-equipment'`，所有路径需用 `import.meta.env.BASE_URL` 前缀，不要硬编码 `/`
- `specs` 字段所有值必须是**字符串**（`z.record(z.string(), z.string())`），数字要加引号
- 图片 `onerror` 回退用 `{backtick}${base}/images/placeholder.svg{backtick}` 动态路径
- `src/content.config.ts` 用了 Astro 5+ 的 `glob` loader，不是旧版 `type: 'content'`
