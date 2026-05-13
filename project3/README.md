# Project 3：石头剪刀布手势识别 (Rock-Paper-Scissors Detection)

基于 YOLO11n 的石头剪刀布手势目标检测项目。

## 项目概述

使用 Ultralytics YOLO11n 模型训练一个手势识别检测器，能够实时识别摄像头画面中的剪刀（Scissors）、石头（Rock）、布（Paper）三种手势。

## 数据集

数据集来自 Roboflow 上的 [rock-paper-scissors-sxsw](https://universe.roboflow.com/roboflow-58fyf/rock-paper-scissors-sxsw) v11 版（YOLOv8n-100epochs），共 **15,874 张图片**，由 SXSW 2023《World's Largest Game of Rock, Paper, Scissors》挑战赛贡献者制作。

### 数据预处理
- 自动旋转（EXIF 方向修正）
- 缩放到 640×640（拉伸填充）

### 数据增强（每张原图生成 7 个版本）
- 50% 概率水平翻转
- 随机旋转 -12° ~ +12°
- 随机剪切 -2° ~ +2°
- 亮度调整 -25% ~ +25%
- 曝光调整 -25% ~ +25%
- 随机高斯模糊 0 ~ 1.5 像素
- 1% 像素的椒盐噪声

### 类别
- Paper（布）
- Rock（石头）
- Scissors（剪刀）

## 环境要求

- Python 3.12+
- PyTorch 2.7+
- CUDA 兼容 GPU（训练用，推理可选）
- ultralytics
- opencv-python
- roboflow（下载数据集用）

## 文件结构

```
project3/
├── README.md                    # 本文件
├── console.md                   # 控制台运行日志
├── download_data.py             # 从 Roboflow 下载数据集
├── train.py                     # 训练模型
├── evaluate.py                  # 在验证集上评估
├── test.py                      # 在测试集上评估
├── predict.py                   # 单张图片推理
├── detect.py                    # 实时摄像头检测
├── yolo11n.pt                   # YOLO11n 预训练权重
├── yolo26n.pt                   # YOLO26n 预训练权重
├── rock-paper-scissors-11/      # 数据集目录
│   ├── data.yaml                # 数据集配置文件
│   ├── train/                   # 训练集（图片 + 标签）
│   ├── valid/                   # 验证集
│   └── test/                    # 测试集
└── runs/
    └── detect/
        ├── train/               # 训练输出（权重、指标曲线、训练图片）
        ├── val/                 # 验证集评估输出
        └── val-2/               # 测试集评估输出
```

## 使用说明

### 1. 下载数据集

```bash
python download_data.py
```

需要有效的 Roboflow API Key（已内置在脚本中）。

### 2. 训练模型

```bash
python train.py
```

训练参数：
- 模型：`yolo11n.pt`
- 输入尺寸：640×640
- Epochs：50
- Batch size：16
- Workers：8
- 优化器：AdamW
- 设备：CUDA

训练耗时约 **3.07 小时**（50 epochs，RTX 5060 Laptop GPU）。

### 3. 评估模型

```bash
# 验证集评估
python evaluate.py

# 测试集评估
python test.py
```

**验证集结果：**
| Class     | Images | Instances | P     | R     | mAP50 | mAP50-95 |
|-----------|--------|-----------|-------|-------|-------|----------|
| all       | 588    | 406       | 0.942 | 0.891 | 0.940 | 0.697    |
| Paper     | 134    | 141       | 0.934 | 0.894 | 0.936 | 0.690    |
| Rock      | 125    | 147       | 0.949 | 0.898 | 0.943 | 0.689    |
| Scissors  | 114    | 118       | 0.944 | 0.881 | 0.940 | 0.714    |

**测试集结果：**
| Class     | Images | Instances | P     | R     | mAP50 | mAP50-95 |
|-----------|--------|-----------|-------|-------|-------|----------|
| all       | 320    | 210       | 0.898 | 0.920 | 0.934 | 0.693    |
| Paper     | 72     | 72        | 0.868 | 0.861 | 0.904 | 0.630    |
| Rock      | 63     | 72        | 0.938 | 0.944 | 0.951 | 0.715    |
| Scissors  | 64     | 66        | 0.887 | 0.953 | 0.947 | 0.734    |

### 4. 单张图片预测

```bash
python predict.py
```

默认读取 `my_hand.jpg`，识别结果保存到 `runs/detect/` 目录。

### 5. 实时摄像头检测

```bash
python detect.py
```

- 调用系统摄像头实时检测
- 窗口显示 FPS
- 按 `Q` 键退出

## 训练日志

详见 `console.md`。

## 训练环境

- GPU: NVIDIA GeForce RTX 5060 Laptop GPU (8GB VRAM)
- CUDA: 11.8
- PyTorch: 2.7.1
- Ultralytics: 8.4.48
- Python: 3.12.13
