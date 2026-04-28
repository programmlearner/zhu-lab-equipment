---
name: "实时仿真器"
category: "仿真平台"
tags: ["实时仿真", "OPAL-RT", "HIL", "RT-LAB"]
brand: "OPAL-RT"
model: "OP4200"
status: "可用"
image: "/images/opalrt-op4200.jpg"
manual_pdf: "/manuals/仿真平台/opalrt-op4200-quickstart.pdf"
specs:
  处理器: "Intel Core i7（多核）"
  实时操作系统: "QNX / RedHat Linux"
  I/O接口: "4个可插拔I/O子板插槽"
  通信: "100Mbps Ethernet (SFP), PCIe"
  软件: "RT-LAB 11+, eMEGASIM, eFPGASIM"
  仿真步长: "最小约 20μs（CPU核）"
---

## 简介
OPAL-RT OP4200 是一款基于 Intel 多核处理器的实时仿真硬件平台，配合 RT-LAB 软件使用，可将 MATLAB/Simulink 模型直接编译为实时代码运行在目标机上，用于电力电子系统的 HIL（硬件在环）和 RCP（快速控制原型）测试。

## 软件生态
- **RT-LAB**：核心仿真软件，基于 MATLAB/Simulink，将模型分解为 SM_（Master）、SS_（Slave）、SC_（Console）子系统
- **eMEGASIM**：电磁暂态仿真（高精度电路求解）
- **eFPGASIM**：FPGA 加速仿真（超高速开关仿真）
- **ARTEMiS**：提升精度的求解器工具箱

## 快速使用（RT-LAB 8步流程）
1. 打开 Simulink 模型，划分 SM_/SS_/SC_ 子系统
2. 在每个子系统中插入 OpComm 块
3. 在 RT-LAB 中编译（自动代码生成）
4. 分配节点（将 SM_ 分配到 OP4200）
5. 选择同步模式（Software Sync / Hardware Sync）
6. 加载模型到目标机
7. 执行实时仿真，实时调整参数
8. Reset 停止仿真

## 注意事项
- 仿真步长受模型复杂度影响，功率电子模型通常设 50~100μs
- OP4200 目标机 IP 地址需与主机在同一网段
- 详细使用流程参见 `RT-LAB_OP101_入门指南.txt`（实验室文件服务器）

## 调研档案
快速入门指南、Danfoss 联调资料、3 相逆变 RCP FYP 工程归档于项目内部 Nutstore：`Physical Platform/CityU_HK/05_RT_Simulator/`（实验室成员内部可访问，不公开）。
