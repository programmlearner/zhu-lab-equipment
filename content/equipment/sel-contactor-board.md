---
name: "接触器控制板"
category: "计算平台"
tags: ["自制", "Raspberry Pi", "控制板", "HAT"]
brand: "Smart Energy Lab"
model: "Contactor Control Board"
status: "可用"
image: "/images/sel-contactor-board.jpg"
specs:
  基础平台: "Raspberry Pi 5"
  功能: "驱动接触器线圈 (24VDC)"
  接口: "GPIO 40-pin, 绿色端子排"
  设计: "CityU Zhu Lab 自制"
---

## 简介
实验室自制 Raspberry Pi HAT，通过 GPIO 输出信号驱动 Schneider RXM 继电器和 LC1D 接触器线圈，实现实验台拓扑切换自动化控制。

## 快速使用
1. 叠放在 Raspberry Pi 5 上。
2. 运行控制脚本，通过 GPIO 高/低电平控制继电器线圈。

## 注意事项
- 控制板供电来自 24V 开关电源，与树莓派 5V 隔离。
- 接线前参考端子排旁边的标签（A/B/C/D 分组）。
