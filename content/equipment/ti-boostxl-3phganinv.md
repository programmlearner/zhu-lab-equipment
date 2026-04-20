---
name: "三相GaN逆变器BoosterPack"
category: "计算平台"
tags: ["GaN", "逆变器", "BoosterPack", "功率电子"]
brand: "Texas Instruments"
model: "BOOSTXL-3PHGANINV"
status: "可用"
image: "/images/ti-boostxl-3phganinv.jpg"
specs:
  拓扑: "三相半桥逆变器"
  开关器件: "GaN FET"
  配合使用: "LAUNCHXL-F28379D"
  接口: "BoosterPack 标准接口"
---

## 简介
TI BOOSTXL-3PHGANINV 三相 GaN 逆变器 BoosterPack，插接在 F28379D LaunchPad 上，用于验证三相 GaN 功率电子控制算法。

## 快速使用
1. 将 BoosterPack 对准引脚插入 LaunchPad。
2. 配合 C2000Ware MotorControl SDK 示例使用。

## 注意事项
- 先检查 GaN 管有无短路，再上电。
- 实验台高压接通前确认控制代码已正确下载。
