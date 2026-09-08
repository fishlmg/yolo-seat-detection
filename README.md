# YOLO 座位检测：训练与边缘部署

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-blue.svg)](https://www.python.org/)
[![Ultralytics](https://img.shields.io/badge/Ultralytics-YOLOv8%2Fv11%2Fv12-00ffff.svg)](https://github.com/ultralytics/ultralytics)

使用 Ultralytics YOLO 系列（v8 / v11 / v12 / YOLO-World）训练**图书馆座位占用检测模型**，并完成从云 GPU 训练到树莓派/摄像头端推理部署、结果上报的完整链路。

> 本仓库与 [library-seat-system](https://github.com/fishlmg/library-seat-system) 配套：这里负责"检测"，那里负责"服务与展示"。

## ✨ 特性

- 覆盖 YOLOv8 / YOLOv11 / YOLOv12 / YOLOv8-World 多个版本实践
- 完整训练流程：数据集配置（`detection.yaml`）→ 云 GPU 训练 → 评估曲线
- 边缘部署：摄像头实时检测、视频文件检测
- 结果上报：检测到的 occupied / available 数量定时上报服务器
- 模型转换：PyTorch `.pt` → ONNX，适配低算力设备

## 🗂 项目结构

```
.
├── detection.yaml                # 训练数据集路径与类别配置
├── command.txt                   # 云 GPU 训练命令记录（已脱敏）
├── show.txt                      # 训练日志（mAP 等指标）
├── Arial.ttf                     # YOLO 绘图字体（离线环境备用）
│
├── YOLOv8-world/
│   ├── test.py                   # YOLOv8-World 开放词汇（open-vocabulary）检测
│   └── test/                     # 测试图片
│
├── yolov11/
│   ├── code/
│   │   ├── camera.py             # 摄像头实时座位检测
│   │   └── test.py
│   └── command.txt               # v11 训练命令
│
├── test/24_11_14/
│   ├── camera.py                 # 摄像头检测
│   ├── video.py                  # 视频文件检测
│   └── url.py                    # 检测结果上报（地址/密码走环境变量）
│
├── yolov8/ yolo12/               # 各版本预训练权重目录（权重不入库）
├── data/                         # 训练数据集（不入库）
└── result/                       # 训练输出（权重/曲线图，不入库）
```

## 🚀 快速开始

```bash
pip install -r requirements.txt
```

**1. 训练（云 GPU）**

```bash
# 命令参考 command.txt
yolo detect train data=detection.yaml model=yolo11n.pt epochs=100 imgsz=640
```

**2. 摄像头推理**

```bash
python yolov11/code/camera.py
```

**3. YOLOv8-World 开放词汇检测**（无需训练，直接文本提示）

```bash
python YOLOv8-world/test.py
```

**4. 检测结果上报**

```bash
export SEAT_SERVER_HOST=your_server_domain_or_ip
export SEAT_SERVER_PASSWORD=your_password
python test/24_11_14/url.py
```

## 📊 训练记录

`show.txt` 记录了一次完整训练：278 epochs（EarlyStopping，patience=100），最佳模型出现在 epoch 178，mAP50 达到 0.916。

## 📦 依赖

ultralytics、OpenCV、requests —— 详见 [requirements.txt](requirements.txt)

## 🔒 安全说明

服务器地址与上报密码通过环境变量（`SEAT_SERVER_HOST` / `SEAT_SERVER_PASSWORD`）注入，代码中无硬编码。

## 📝 说明

预训练权重、自训练权重（`*.pt`）、数据集（`data/`）与训练结果（`result/`）体积较大，已通过 `.gitignore` 排除，仅保留在本地。

## 📄 许可证

[MIT License](LICENSE)
