---
name: "单板计算机"
category: "计算平台"
tags: ["树莓派", "SBC", "Linux", "Python"]
brand: "Raspberry Pi"
model: "Pi 5 4GB"
status: "可用"
image: "/images/raspberry-pi5-4gb.jpg"
datasheet_pdf: "/manuals/计算平台/raspberry-pi5-datasheet.pdf"
specs:
  处理器: "Broadcom BCM2712, 4核 Cortex-A76 @ 2.4GHz"
  内存: "4GB LPDDR4X"
  存储接口: "microSD + M.2 HAT (可选)"
  接口: "2×USB 3.0, 2×USB 2.0, 2×HDMI, GPIO 40-pin, GbE"
  操作系统: "Raspberry Pi OS (Linux)"
---

## 简介
Raspberry Pi 5 是实验室数据采集和自动化控制主机，运行 Python 脚本，通过 GPIO 连接控制板，通过 RS485 读取电能表数据。

## 快速使用
1. 插入 microSD 卡（已烧录系统），接显示器/键鼠上电。
2. SSH 连接：`ssh pi@<IP地址>`（局域网内）。
3. 通过 USB-RS485 读取 Modbus 数据。

## 注意事项
- 使用官方 27W USB-C 电源，劣质电源会导致欠压降频。
- 不要直接断电，正确关机命令 `sudo shutdown -h now`。
