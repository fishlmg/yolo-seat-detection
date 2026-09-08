# YOLO 目标检测：座位检测训练与部署

使用 Ultralytics YOLO（v8 / v11 / v12 / World）训练座位占用检测模型，并在摄像头/树莓派端部署推理、上报结果。

## 文件结构

```
├── detection.yaml            # 训练数据集配置
├── command.txt               # 云 GPU 训练命令记录（已脱敏）
├── show.txt                  # 训练日志
├── YOLOv8-world/
│   └── test.py               # YOLOv8-World 开放词汇检测测试
├── yolov8/ yolov11/ yolo12/  # 各版本预训练权重（不入库）
├── yolov11/code/
│   ├── camera.py             # 摄像头实时检测
│   └── test.py
├── test/24_11_14/
│   ├── camera.py / video.py  # 摄像头/视频检测
│   └── url.py                # 检测结果上报服务器（地址/密码走环境变量）
├── data/                     # 数据集（不入库）
└── result/                   # 训练输出（不入库）
```

## 快速开始

```bash
pip install -r requirements.txt

# 训练（云 GPU 命令见 command.txt）
yolo detect train data=detection.yaml model=yolo11n.pt epochs=100 imgsz=640

# 摄像头推理
python yolov11/code/camera.py

# 结果上报（需配置环境变量）
export SEAT_SERVER_HOST=your_server_domain_or_ip
export SEAT_SERVER_PASSWORD=your_password
python test/24_11_14/url.py
```

## 说明

- 预训练权重、自训练权重（`*.pt`）、数据集（`data/`）与训练结果（`result/`、`train4/`）不包含在仓库中，`.gitignore` 已排除，本地保留
- 服务器地址与上报密码通过环境变量配置，代码中无硬编码
