---
name: "拓竹 3D 打印机 P1S Combo"
category: "制造设备"
tags: ["3D打印", "FDM", "多色打印", "AMS 2 Pro"]
brand: "Bambu Lab 拓竹"
model: "P1S Combo (含 AMS 2 Pro)"
status: "可用"
image: "/images/bambu-p1s-combo.jpg"
manual_pdf: "/manuals/制造设备/bambu-p1s-combo-quickstart.pdf"
datasheet_pdf: "/manuals/制造设备/bambu-ams-2-pro-quickstart.pdf"
specs:
  打印技术: "FDM 熔融沉积"
  打印尺寸: "256 × 256 × 256 mm"
  最高速度: "500 mm/s"
  最大加速度: "20000 mm/s²"
  喷嘴温度: "最高 300°C（硬化钢喷嘴）"
  热床温度: "最高 100°C（纹理 PEI 板）"
  腔体: "全封闭 + 活性炭过滤"
  耗材直径: "1.75 mm"
  AMS 容量: "AMS 2 Pro × 1，4 槽多色"
  AMS 干燥功能: "主动烘干，最高 55°C"
  支持材料: "PLA / PETG / ABS / ASA / PC / PA / PA-CF / TPU (主进料)"
  切片软件: "Bambu Studio / Orca Slicer"
  联网: "Wi-Fi 2.4GHz + 以太网"
  电源: "100-240 V AC"
---

## 简介
Bambu Lab P1S 是一款封闭腔体 CoreXY 桌面级 FDM 3D 打印机，配合附赠的 **AMS 2 Pro** 实现 4 色多材料打印和主动烘干。适合实验室快速制作夹具、外壳、示教模型、PCB 固定件等原型件。

## 主要用途
- 实验夹具、示波器/电源外壳、测试治具打印
- 电路板 / 元器件 3D 模型展示（教学）
- 多色标识件（例如不同类别的实验室标签）
- 吸湿耗材（PA、PVA）的主动烘干保存

## 快速使用
1. **拆运输件**：底部 3 颗橙色螺丝 + 打印头泡沫块 + 所有蓝/橙色胶带必须全部拆除。
2. **首次联网**：屏幕 → 设置 → WLAN（仅 2.4GHz） → 连入实验室 Wi-Fi。
3. **升级固件**：屏幕 → 设置 → 通用 → 固件升级 → 升到最新版（**必须在接 AMS 前完成**）。
4. **首次自检**：自动调平 + 振动补偿 + 噪音校准（约 15 分钟，不要中断）。
5. **连接 AMS 2 Pro**：
   - 缓冲器卡进背板凹槽，用 M3 × 21.5 螺丝固定（H2.0 内六角）
   - 4-pin 数据线接打印机背面 AMS 接口
   - AMS 2 Pro 接**独立电源适配器**（不共用打印机电源）
   - PTFE 管从 AMS 出料口 → buffer → 打印头
6. **AMS 固件升级**：屏幕 → 设置 → 通用 → 固件升级 → 选 AMS 升级。
7. **装料**：AMS 2 Pro 顶盖掀起 → 料盘卡入槽位 → 料头剪 45° → 推入进料口直到齿轮咬住 → RFID 自动识别（原厂料）。
8. **切片打印**：电脑安装 Bambu Studio → 导入 STL → 选择 P1S + AMS → 切片 → Wi-Fi 发送到打印机。

## 注意事项
- **不要直接打 TPU 软料到 AMS**：TPU 只能用后侧外部料架进料，AMS 的切料刀和 buffer 会卡软料。
- **AMS 烘干 PLA 不要超过 45°C、不要长时间开**：PLA 会变软粘连在料盘上。
- **PA / PA-CF 必须烘干后打印**：开封 2 小时即开始吸湿，直接打会爆米花。
- **打印中不要开腔门**：P1S 是封闭腔体，开门会导致 ABS/ASA/PC 翘边。
- **喷嘴更换**：实验室常备 0.4mm 硬化钢喷嘴，打碳纤料（PA-CF、PLA-CF）时必须用硬化钢。
- **切片时 AMS 料槽对应顺序**：Studio 里的 1/2/3/4 对应 AMS 从左到右的物理槽位。

## 附带手册
- `bambu-p1s-combo-quickstart.pdf` — P1S Combo 整体开箱与装配（英文官方）
- `bambu-ams-2-pro-quickstart.pdf` — AMS 2 Pro 专项说明（英文官方）
- 中文版 P1S 快速入门（`/manuals/制造设备/bambu-p1s-quickstart-cn.pdf`）
- 更多：[官方 Wiki](https://wiki.bambulab.com/zh/p1/manual)
