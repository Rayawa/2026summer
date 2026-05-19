# Project 2-1：加州房价预测（Random Forest）

基于 scikit-learn 的回归预测项目，使用 **加州房价数据集** 训练随机森林回归模型，根据房屋特征预测街区房价中位数。

## 项目结构

```
project2_1/
├── README.md                # 本文件
├── main.py                  # 主程序：训练 + 预测 + 评估 + 可视化
├── model.pkl                # 训练好的 RandomForest 模型（joblib 序列化）
├── prediction_results.csv   # 测试集真实值与预测值对比
└── images/
    ├── feature_importance.png    # 特征重要性柱状图
    └── prediction_scatter.png    # 真实值 vs 预测值散点图
```

## 数据集

**California Housing Dataset**（scikit-learn 内置）

- 样本量：20,640 条街区数据
- 特征数：8 个
- 目标变量：`MedHouseVal`（房价中位数，单位：10 万美元）

| 特征 | 说明 | 类型 |
|------|------|------|
| MedInc | 街区收入中位数 | 连续值 |
| HouseAge | 房屋年龄中位数 | 连续值 |
| AveRooms | 平均房间数 | 连续值 |
| AveBedrms | 平均卧室数 | 连续值 |
| Population | 街区人口 | 连续值 |
| AveOccup | 平均居住人数 | 连续值 |
| Latitude | 纬度 | 连续值 |
| Longitude | 经度 | 连续值 |

## 模型

**算法**：RandomForestRegressor（随机森林回归）

**超参数**：
- `n_estimators=200` — 200 棵决策树
- `max_depth=20` — 限制最大深度，防止过拟合
- `random_state=42` — 结果可复现
- `n_jobs=-1` — 使用全部 CPU 核心并行训练

### 评估结果

| 指标 | 值 |
|------|------|
| MSE | 0.2552 |
| RMSE | 0.5052 |
| R² | 0.8053 |

R² = 0.8053，模型解释了约 80.5% 的房价方差，表现良好。

### 特征重要性 Top 5

1. **MedInc**（收入中位数）— 最强预测因子
2. **AveOccup**（平均居住人数）
3. **Latitude**（纬度）
4. **Longitude**（经度）
5. **HouseAge**（房屋年龄）

收入水平和地理位置是房价的核心影响因素。

## 运行方式

```bash
cd project2_1
python main.py
```

输出：
- 控制台打印数据集信息、训练进度、评估指标
- `model.pkl` — 训练好的模型
- `prediction_results.csv` — 预测结果
- `images/feature_importance.png` — 特征重要性图
- `images/prediction_scatter.png` — 预测散点图

## 环境要求

```bash
pip install scikit-learn pandas matplotlib joblib
```

- Python 3.8+
- scikit-learn
- pandas
- matplotlib
- joblib
