---
name: "电网模拟器"
category: "电源设备"
tags: ["电网模拟器", "交流电源", "可编程", "ITECH"]
brand: "ITECH 艾德克斯"
model: "IT-7900EP"
status: "待到货"
image: "/images/it7900ep.jpg"
manual_pdf: "/manuals/电源设备/it7900ep-manual-en.pdf"
datasheet_pdf: "/manuals/电源设备/it7900ep-manual-cn.pdf"
specs:
  输出功率: "15kVA"
  输出电压: "0~350V (单相), 0~350V L-N (三相)"
  输出频率: "15~1200Hz"
  总谐波失真: "<0.5% (线性负载)"
  接口: "USB, LAN, RS232, RS485, GPIB (可选)"
  功能: "电网异常模拟, 谐波叠加, 电压跌落"
---

## 简介
ITECH IT-7900EP 是一款高性能可编程交流电源，可模拟电网异常（电压跌落、频率偏差、谐波污染等），用于逆变器并网测试和电网扰动响应实验。支持单相/三相输出，带 GPIB/LAN 远程控制接口。

## 主要用途
- 并网逆变器低电压穿越（LVRT/HVRT）测试
- 电网频率偏差下的逆变器响应测试
- 谐波注入测试（模拟非线性电网）
- 功率因数、THD 测量

## 快速使用
1. 选择输出模式（单相 / 三相）并设置输出电压和频率。
2. 通过面板或 IT7900EP 上位机软件（VB 控制程序）设置电网异常参数。
3. 连接 LAN 口可使用 SCPI 命令远程控制。

## 注意事项
- 设备为 15kVA 大功率，接线前确认配电容量。
- 输出端务必安全接地，防止触电。
- 当前状态：**已采购，待到货**。

## 调研档案
选型对比（Chroma 62000/61800、Keysight RP7900 等候选）、招标 RFQ、报价单归档于项目内部 Nutstore：`Physical Platform/CityU_HK/02_Grid_Simulator/`（实验室成员内部可访问，不公开）。
