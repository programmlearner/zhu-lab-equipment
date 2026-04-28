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

## 调研档案
RTScale 安装包、Simulink/HDL 工程示例、Danfoss 模型与联调资料归档于项目内部 Nutstore：`Physical Platform/CityU_HK/05_RT_Simulator/Simulink_HDL/` 与 `Software/`（实验室成员内部可访问，不公开）。控制器选型阶段曾对比 Plexim B-Box / RT-box、YXSPACE 等候选方案，资料在 `04_RT_Controller/`。

## 案例演示视频归档
基于 RTScale 的 RCP / HIL / LLC 实时仿真案例演示视频（来自 https://www.insrealm.com/spzx_08271717_191）归档于本机 `C:\Users\Xiangyu.Cityus\Documents\InsRealm-Demos\`（含 4 个 MP4 + 4 张海报封面 + README.md）。

## 厂家信息（InsRealm · 杭州瞬迦科技有限公司）

- **官网**：https://www.insrealm.com/
- **官方案例演示**：https://www.insrealm.com/spzx_08271717_191
- **电话**：400-066-1130
- **Email**：service@insrealm.com
- **地址**：浙江省杭州市萧山区宁围街道建设三路 733 号信息港五期 9 号楼 9106

### 产品线（同厂家其它型号，便于未来扩展时参考）

| 类别 | 型号 | 定位 |
|------|------|------|
| 软件平台 | **Insrealm**（基于 Simulink） | 上位实时仿真工具链 |
| 软件平台 | **InScope** | 实时参数标定与采集 |
| 硬件平台 | **RTPi** | 性价比入门仿真器 |
| 硬件平台 | **RTScale**（实验室在用） | 均衡型中端仿真器（FPGA 亚微秒级） |
| 硬件平台 | **RTCenter** | 高端性能仿真器 |
| 解决方案 | 电机电控 / 高校科研教学 | 行业方案 |

### 资源中心

- **成功案例**：https://www.insrealm.com/cgal_v
- **案例演示**：https://www.insrealm.com/spzx_08271717_191（4 段官方 demo 视频，本仓库 RTScale 词条上方"案例演示视频归档"已离线保存）
- **使用教程**：https://www.insrealm.com/sygjj
