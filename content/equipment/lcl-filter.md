---
name: "LCL 滤波器"
category: "仿真平台"
tags: ["LCL", "滤波器", "并网", "自制PCB", "功率电子"]
brand: "CityU Zhu Lab 自制"
model: "LCLFilter v1.0 (Altium PCB)"
status: "可用"
image: "/images/lcl-filter.jpg"
specs:
  拓扑: "三相 LCL 滤波器"
  逆变器侧电感 L1: "2 mH（手绕铁芯环形）"
  滤波电容 Cf: "4.7 μF / 400V（薄膜电容）"
  电网侧电感 L2: "约 80 μH（手绕铁芯环形）"
  额定电压: "三相 400V"
  额定电流: "约 10A（5.5kW 平台）"
  PCB设计软件: "Altium Designer"
  设计文件路径: "05_RT_Simulator/3-Phase-Inverter-RCP-FYP-main/Design Files/LCLFilter_Final/"
---

## 简介

LCL 滤波器是并网逆变器与电网之间的无源接口，用于衰减逆变器开关谐波，使并网电流满足 IEEE 1547 / GB/T 14549 谐波标准。本滤波器为实验室 FYP 项目定制设计的三相 PCB，配合 Danfoss VLT FC302 逆变器使用。**实物已于 2026-04-29 到货登记。**

---

## 实物照片（2026-04-29 到货）

![LCL 滤波器整体外观](/images/lcl-filter.jpg)

![LCL 滤波器视角 2](/images/lcl-filter-2.jpg)

![LCL 滤波器视角 3](/images/lcl-filter-3.jpg)

![LCL 滤波器视角 4](/images/lcl-filter-4.jpg)

![LCL 滤波器视角 5](/images/lcl-filter-5.jpg)

---

## 电路拓扑图

```
  逆变器侧 (Danfoss 输出)          电网侧 (IT-7900EP)
                                   
  A ──[L1a: 2mH]──┬──[L2a: 80μH]── A'
                  │
                 [Cf: 4.7μF]
                  │
  B ──[L1b: 2mH]──┼──[L2b: 80μH]── B'
                  │
                 [Cf: 4.7μF]
                  │
  C ──[L1c: 2mH]──┴──[L2c: 80μH]── C'
                  │
                 [Cf: 4.7μF]
                  │
                 GND
```

**各元件作用：**

| 元件 | 参数 | 作用 |
|------|------|------|
| L1（逆变器侧电感） | 2 mH | 限制开关纹波电流，保护逆变器 |
| Cf（滤波电容） | 4.7 μF / 400V | 提供谐波电流旁路，与 L2 形成谐振陷波 |
| L2（电网侧电感） | ~80 μH | 阻挡高频谐波进入电网，与 Cf 形成截止频率 |

---

## 谐振频率

LCL 谐振频率：

```
f_res = (1/2π) × √[(L1 + L2) / (L1 × L2 × Cf)]
      ≈ (1/2π) × √[(2mH + 80μH) / (2mH × 80μH × 4.7μF)]
      ≈ 约 1.8 kHz
```

> ⚠️ 控制带宽应低于谐振频率的 1/3（约 600 Hz），否则控制器会激励谐振导致不稳定。

---

## 元件对应实验室库存

| LCL 元件 | 对应实验室耗材词条 |
|----------|-----------------|
| L1 (2mH) | 铁芯环形电感 2mH (`inductor-toroid-2mh`) |
| L2 (80μH) | 铁芯环形电感 ~80μH (`inductor-toroid-80uh`) |
| Cf (4.7μF) | 薄膜电容 4.7μF 400V (`cap-film-4u7-400v`) |

---

## 注意事项

- 上电前检查所有电感绕组绝缘，环形电感匝间绝缘靠漆包线，注意引脚焊点处不要破损
- 滤波电容额定 400V，三相 380V 系统峰值约 537V，**必须使用 400V 以上薄膜电容**，不可使用铝电解电容（交流纹波过大）
- PCB 设计文件（Altium Designer `.SchDoc` / `.PcbDoc`）存放于坚果云实验室文件服务器
