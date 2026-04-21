---
name: "MATLAB/Simulink"
category: "软件工具"
tags: ["软件", "仿真", "MATLAB", "Simulink", "代码生成"]
brand: "MathWorks"
model: "MATLAB R2023b"
status: "可用"
image: "/images/placeholder.svg"
specs:
  版本: "R2023b（实验室授权）"
  许可证类型: "校园网授权（CityU）"
  主要工具箱: "Simulink, Control System, Signal Processing, Power Systems"
  代码生成: "Simulink Coder, Embedded Coder, HDL Coder"
  运行平台: "Windows 10/11"
---

## 简介
MATLAB/Simulink 是实验室所有仿真和控制算法开发的核心软件平台。电力电子控制器（GFM/GFL 逆变器、变频器）均在 Simulink 中建模，通过 RT-LAB 或 RTScale 部署到实时平台。

## 实验室已有 Simulink 模型
| 模型 | 控制算法 | 文件位置 |
|------|----------|---------|
| 三相并网逆变器（GFL） | 电流控制 + PLL | `05_RT_Simulator/3-Phase-Inverter-RCP-FYP-main/` |
| 三相并网逆变器（GFM） | 虚拟同步机 | `05_RT_Simulator/3-Phase-Inverter-RCP-FYP-main/` |
| Dual 模式（GFM+GFL） | 双逆变器并联 | `05_RT_Simulator/Simulink_HDL/` |
| Danfoss VLT 变频器模型 | 变速驱动 | `05_RT_Simulator/Danfoss模型以及相关资料/` |

## 校园网激活
CityU 提供校园 MATLAB 许可，访问 https://www.cityu.edu.hk/csc 下载安装包，使用 CityU 邮箱激活。

## 注意事项
- 使用 SimplusGT 工具箱时需先运行 `restoredefaultpath; matlabrc`。
- Simulink 模型保存为 `.slx` 格式，不要另存为 `.mdl`（旧格式）。
