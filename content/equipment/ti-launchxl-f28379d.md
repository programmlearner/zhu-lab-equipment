---
name: "C2000 DSP 开发板"
category: "计算平台"
tags: ["DSP", "TI", "C2000", "实时控制"]
brand: "Texas Instruments"
model: "LAUNCHXL-F28379D"
status: "可用"
image: "/images/ti-launchxl-f28379d.jpg"
manual_pdf: "/manuals/计算平台/ti-launchxl-f28379d-manual.pdf"
datasheet_pdf: "/manuals/计算平台/ti-f28379d-datasheet.pdf"
specs:
  主芯片: "TMS320F28379D (dual-core C28x, 200MHz)"
  内存: "512KB Flash, 100KB RAM"
  接口: "USB (XDS110 仿真器), BoosterPack 接口"
  工具链: "Code Composer Studio (CCS), MATLAB/Simulink"
---

## 简介
TI LaunchPad F28379D 是双核 C2000 实时控制 DSP 开发板，用于功率电子控制算法开发，支持 MATLAB/Simulink 自动代码生成，与 BOOSTXL-3PHGANINV 配合使用。

## 快速使用
1. 通过 USB 连接电脑，CCS 识别为 XDS110 仿真器。
2. 在 MATLAB/Simulink 中配置目标为 F28379D，生成并下载代码。

## 注意事项
- 不要在上电状态下插拔 BoosterPack，避免损坏 IO。
- 使用 USB 隔离器时注意供电是否足够。
