# 实验室设备管理系统

CityU Zhu Lab 实验室设备管理与查询网站，基于 Astro + Tailwind CSS 构建的静态站点。

**在线访问**：https://programmlearner.github.io/zhu-lab-equipment/

---

## 功能

- 卡片式设备展示，附图片、状态标签、类别标签
- 按类型（测量仪器 / 电源设备 / 开关控制 / 计算平台 / 网络设备 / 工具 / 耗材）和状态（可用 / 使用中 / 维修中）多维度筛选
- 关键字搜索（名称、品牌、型号、标签）
- 设备详情页：技术参数表、使用指南、注意事项、PDF 说明书下载
- 响应式设计，支持手机和桌面端
- 静态部署，零运行时成本

---

## 当前设备清单（41 件）

| 类别 | 设备 |
|------|------|
| 测量仪器 | Rohde & Schwarz RTM3004、Tektronix TDS 3032C / TDS 2022C、Fluke 79 III、Micsig DP1500A / CP2100、CHINT DTSU666、UGREEN 网络测线仪 |
| 电源设备 | RIGOL DP832、Danfoss VLT FC302、MWEL NDR-75-24 |
| 开关控制 | Schneider WHT35 / LC1D32 / RXM 24VDC、DELIXI DEP2-025、R.STAR MB04K |
| 计算平台 | Raspberry Pi 5 4GB、TI LAUNCHXL-F28379D、TI BOOSTXL-3PHGANINV、SEL Contactor Control Board |
| 网络设备 | TP-Link LS1008G |
| 工具 | 自动剥线钳、棘轮压接钳、剥线钳、RJ45 压接钳、螺丝刀套装 |
| 耗材 | 薄膜电容、铝电解电容 ×3、陶瓷电容 MLCC、肖特基二极管 BAT54S、铁芯电感 ×2、DC-DC 模块 JRA4812、冷压端子套装、导线套装、水晶头、膨胀螺丝等 |

---

## 如何添加新设备

### 1. 准备图片

将设备图片（JPG，建议 ≤ 500KB）放入 `public/images/`，命名规则：`品牌-型号.jpg`（小写、连字符）。

### 2. 创建设备文件

在 `content/equipment/` 下新建 `品牌-型号.md`：

```yaml
---
name: "设备中文名"
category: "测量仪器"        # 测量仪器 / 电源设备 / 开关控制 / 计算平台 / 网络设备 / 工具 / 耗材
tags: ["标签1", "标签2"]
brand: "品牌"
model: "型号"
location: "实验室 A"        # 可选
status: "可用"              # 可用 / 使用中 / 维修中
image: "/images/品牌-型号.jpg"
manual_pdf: "/manuals/类别/文件名.pdf"    # 可选
datasheet_pdf: "/manuals/类别/文件名.pdf" # 可选
specs:
  参数名: "参数值"
---

## 简介
...

## 快速使用
1. ...

## 注意事项
- ...
```

### 3. 推送部署

```bash
git add .
git commit -m "add: 设备名称"
git push
```

推送后 GitHub Actions 自动重新构建，约 1 分钟生效。

---

## 本地开发

```bash
npm install
npm run dev      # 本地预览 http://localhost:4321
npm run build    # 构建静态文件到 dist/
```

**环境要求**：Node.js ≥ 22.12、npm ≥ 9

---

## 技术栈

| 项目 | 选型 |
|------|------|
| 框架 | [Astro 6](https://astro.build) |
| 样式 | [Tailwind CSS 4](https://tailwindcss.com) + [@tailwindcss/typography](https://tailwindcss.com/docs/typography-plugin) |
| 数据 | Markdown + YAML frontmatter（Content Collections） |
| 部署 | GitHub Pages（GitHub Actions 自动部署） |
