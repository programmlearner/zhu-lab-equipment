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

## 背板端口说明

实验室在用机身丝印 **RTScale / RTS35181170**。背板端口从左到右如下：

![RTScale 背板端口](/images/rtscale-back.jpg)

```
  ┌──────────────────────────┬─────────┬─────────┬─────────┐
  │   1    2    3    4       │  ETH1   │  ETH2   │  HOST   │
  │ ▓▓▓ ▓▓▓ ▓▓▓ ▓▓▓          │ ┃┃┃┃┃   │ ┃┃┃┃┃   │ ┃┃┃┃┃   │
  │      SFP+ ×4             │  RJ45   │  RJ45   │  RJ45   │
  └──────────────────────────┴─────────┴─────────┴─────────┘
```

| 端口 | 物理形态 | 在本平台的角色 | 备注 |
|------|---------|-------------|------|
| **SFP+ 1~4** | 4 路 SFP+ 笼（10 Gbps，光模块或 DAC 铜缆均可插） | **FPGA 高速 I/O 扩展通道**：连接 InsRealm 信号转接板 / I/O 扩展箱，把 FPGA 内部的 PWM 输出、ADC 回传、编码器、SPI 等信号通过光纤引出到外部硬件（如 Danfoss IGBT 驱动板、LCL 电流采样、DC bus 电压采样） | 光纤天然 **galvanic isolation**——切断 IGBT 开关共模噪声从功率侧反灌 FPGA；端到端延迟 <1 µs，足以承载亚微秒仿真步长 |
| **ETH1, ETH2** | 2 个标准 RJ45 千兆口 | **辅助网络通讯**：可用于 EtherCAT 现场总线（接伺服/外部 RT 设备）、UDP/TCP 数据流（喂 InScope 远程参数采集），或留作管理 / 调试备用 | 双口允许"业务+管理"物理隔离；也可菊花链做环网冗余 |
| **HOST** | 专用 RJ45 千兆口 | **上位 PC 通讯专用口**：Simulink/HDL Coder 工程编译后的 bitstream 通过这条口下发到 FPGA；InScope 实时监控/参数标定也走这条 | InsRealm 私有协议，与 ETH1/2 的开放协议物理分离；**首次联机这是必接的口** |

**接线方向（典型 PHIL 配置）**：

```
                                       ┌──────────────────┐
   PC（Simulink+HDL Coder+InScope）───▶│ HOST (RJ45)       │
                                       │                   │
                  ┌────────────────────│ SFP+ 1 (Tx/Rx)    │  → InsRealm 信号转接板
                  │ 光纤              │                   │     │
                  │                    │ SFP+ 2 (Tx/Rx)    │  → │  · PWM 输出到 Danfoss IGBT 驱动
                  │ 光纤              │                   │     │  · ADC 回传：LCL 电流、DC bus 电压
                  │                    │ SFP+ 3, 4 备用    │     │  · 故障/急停握手
                  │                    │                   │
   EtherCAT 现场设备（可选）─────────│ ETH1 / ETH2       │
                                       └──────────────────┘
                                            RTScale RTS35181170
```

**实操要点**：

- **SFP+ 模块需匹配**：光纤距离短（同机柜）用 OM3 多模 + 850 nm SFP+ 模块；超过 30 m 用 OM4 或单模。短跳直接用 SFP+ DAC 铜缆（1~3 m）成本最低
- **ETH 不能替代 SFP+**：PWM 等高速 I/O 必须走 SFP+ 通道（FPGA 直连 + 隔离），ETH 不参与实时仿真回路
- **HOST 与 ETH 不能互换**：HOST 走私有协议，连错口 InsRealm 软件搜不到设备
- **接地**：RTScale 机壳必须 PE 母排单点接地（与 Danfoss、ITECH 同点），避免和功率系统形成地环路

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
