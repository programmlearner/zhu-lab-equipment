---
name: "RT-LAB 实时仿真软件"
category: "软件工具"
tags: ["软件", "实时仿真", "OPAL-RT", "Simulink接口"]
brand: "OPAL-RT"
model: "RT-LAB 11+"
status: "可用"
image: "/images/opalrt-op4200.jpg"
specs:
  类型: "实时仿真软件"
  运行平台: "Windows 10/11 主机 + OP4200 目标机"
  Simulink版本: "R2020b 及以上"
  许可证: "实验室已购（绑定 OP4200 硬件）"
  工具箱: "eMEGASIM, eFPGASIM, ARTEMiS, ePHASORSIM"
---

## 简介
RT-LAB 是 OPAL-RT 的核心实时仿真软件，以 MATLAB/Simulink 为前端，将模型自动转换为实时可执行代码并部署到 OP4200 目标机。许可证与 OP4200 硬件绑定。

## 子系统命名规范
- `SM_xxx`：Master 子系统（核心计算 + I/O，必须有且仅有一个）
- `SS_xxx`：Slave 子系统（分布式计算，可选多个）
- `SC_xxx`：Console 子系统（UI 面板、示波器，运行在主机）
- **OpComm 块**：每个子系统必须插入，处理子系统间通信

## 在线培训
- 平台：https://training-opalrt.talentlms.com/index
- 账号：yue.zhu@cityu.edu.hk（实验室账号，请联系 Supervisor 获取密码）
- 建议先完成 OP101 基础课程

## 注意事项
- RT-LAB 版本需与 OP4200 固件版本匹配，升级前请确认兼容性。
- 实验结束后需执行 Reset 步骤，防止目标机残留进程影响下次仿真。
