---
name: "实时缩比仿真平台"
category: "仿真平台"
tags: ["实时仿真", "RTScale", "HIL", "FPGA", "功率电子"]
brand: "InsRealm 盈斯锐"
model: "RTScale"
status: "可用"
image: "/images/rtscale.jpg"
manual_pdf: "/manuals/仿真平台/rtscale-manual.pdf"
datasheet_pdf: "/manuals/仿真平台/rtscale-danfoss-guide.pdf"
specs:
  仿真核心: "FPGA（Xilinx/AMD）"
  仿真步长: "亚微秒级（< 1μs）"
  软件接口: "Simulink HDL Coder / RT-LAB eFPGASIM"
  用途: "三相逆变器RCP、变频器控制HIL"
  配套设备: "Danfoss VLT FC302 变频器"
---

## 简介
InsRealm RTScale 是基于 FPGA 的超高速实时仿真平台，仿真步长可达亚微秒级，适合对开关频率要求高的功率电子系统（GaN/SiC 变换器）的 HIL 测试。通过 Simulink HDL Coder 将控制算法转换为 VHDL/Verilog 代码部署到 FPGA。

## 与 OP4200 的分工
| 特性 | OP4200 (CPU核) | RTScale (FPGA核) |
|------|---------------|----------------|
| 仿真步长 | 20μs~100μs | < 1μs |
| 适用场景 | 系统级 HIL | 开关级 HIL |
| 编程方式 | Simulink 直接 | HDL Coder 转换 |

## Danfoss 变频器联调流程
参见 `RTScale-Danfoss(5.5kW)用户指导三通道.pdf`（可从说明书按钮下载）。

## 快速使用
1. 在 Simulink 中完成控制器设计（GFM/GFL 算法）
2. 使用 HDL Coder 将控制子系统转换为 HDL 代码
3. 通过 RTScale 工具链部署到 FPGA
4. 通过杜邦线转接板连接实物逆变器

## 注意事项
- HDL Coder 对 Simulink 模块支持有限制，不支持的模块需手动替换
- 具体报错解决方案参见 `HDLCoder报错解决.pdf`（软件工具词条）
