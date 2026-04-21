---
name: "Simulink HDL Coder"
category: "软件工具"
tags: ["软件", "FPGA", "HDL", "代码生成", "Simulink"]
brand: "MathWorks"
model: "HDL Coder (R2023b)"
status: "可用"
image: "/images/placeholder.svg"
manual_pdf: "/manuals/软件工具/hdlcoder-guide.pdf"
datasheet_pdf: "/manuals/软件工具/fpga-engine-guide.pdf"
specs:
  类型: "Simulink → VHDL/Verilog 代码生成工具箱"
  目标FPGA: "Xilinx（通过 RTScale FPGA Engine）"
  配套工具: "Vivado, RTScale FPGA Engine"
  许可证: "随 MATLAB 校园授权包含"
---

## 简介
Simulink HDL Coder 将 Simulink 控制模型自动转换为 VHDL 或 Verilog 代码，配合 InsRealm RTScale 的 FPGA Engine 部署到 FPGA，实现亚微秒级实时控制仿真。

## 工作流程
1. 在 Simulink 中设计控制子系统（需使用 HDL Coder 支持的模块）
2. 运行 HDL Coder 生成 VHDL/Verilog 代码（输出到 `hdlsrc/` 目录）
3. 将生成的代码导入 RTScale FPGA Engine 工程
4. 通过 Vivado 综合/实现，下载到 FPGA

## 注意事项（常见报错）
- 浮点运算需替换为定点（使用 `fixdt` 数据类型）
- 不支持：可变维度信号、部分 Stateflow 状态机
- 具体报错解决方案参见本词条的「用户手册」PDF（`HDLCoder使用方法.pdf`）
- RTScale 特有的配置步骤参见「Datasheet」PDF（`FPGA Engine使用流程.pdf`）
