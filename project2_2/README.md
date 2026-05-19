# Project 2-2：学生数字行为与学习表现分析

基于真实学生数字行为数据的探索性分析与回归预测项目。分析学习时间、屏幕时间、睡眠、运动、出勤等因素与学业表现（CGPA）之间的关系。

## 项目结构

```
project2_2/
├── README.md                          # 本文件
├── DownloadCSV.py                     # kagglehub 下载数据集
├── main.py                            # 主程序：清洗 → 可视化 → 建模 → 评估
├── data/
│   └── student_digital_behavior.csv   # 原始数据集
├── outputs/
│   ├── cleaned_student_digital_behavior.csv  # 清洗后数据
│   ├── descriptive_statistics.csv           # 描述性统计
│   ├── model_results.csv                    # 模型评估对比
│   └── feature_importance.csv               # 随机森林特征重要性
└── figures/
    ├── fig1_screen_time_distribution.png    # 屏幕时间分布（直方图 + KDE）
    ├── fig2_screen_time_vs_cgpa.png         # 屏幕时间 vs CGPA 散点图
    ├── fig3_study_hours_vs_cgpa.png         # 学习时间 vs CGPA 散点图
    ├── fig4_sleep_hours_vs_cgpa.png         # 睡眠时间 vs CGPA 散点图
    ├── fig5_correlation_heatmap.png         # 数值特征相关性热力图
    └── fig6_feature_importance.png          # Top 10 特征重要性柱状图
```

## 数据集

来自 Kaggle 的 **[Student Lifestyle and Academic Performance Dataset](https://www.kaggle.com/datasets/rafi003/student-lifestyle-and-academic-performance-dataset)**。

**原始字段**（共 12 列）：

| 字段 | 说明 | 类型 |
|------|------|------|
| Age | 年龄 | 数值 |
| Branch | 专业分支 | 分类 |
| Study_Hours_per_Day | 每日学习时间（小时） | 数值 |
| Sleep_Hours | 每日睡眠时间（小时） | 数值 |
| Screen_Time_Hours | 每日屏幕时间（小时） | 数值 |
| Gym_Hours_per_Week | 每周运动时间（小时） | 数值 |
| Diet_Type | 饮食类型 | 分类 |
| Attendance_Percentage | 出勤率（%） | 数值 |
| Stress_Level_1_to_10 | 压力水平（1~10） | 数值 |
| Residence | 住宿类型 | 分类 |
| Internal_Marks | 内部成绩 | 数值 |
| **CGPA** | **绩点（目标变量）** | 数值 |

## 数据清洗

主程序自动执行以下清洗步骤：

1. **字段筛选** — 仅保留建模所需字段（排除 `Internal_Marks` 以避免数据泄漏）
2. **去重** — 删除重复行
3. **缺失值处理** — 数值字段用中位数填充，分类字段用众数填充
4. **异常值过滤** — 对年龄、学习时间、睡眠时间等字段设置合理范围

## 探索性分析（EDA）

主程序自动生成 6 张可视化图表：

| 图表 | 内容 |
|------|------|
| fig1 | 屏幕时间分布（直方图 + KDE 曲线） |
| fig2 | 屏幕时间 vs CGPA 散点图 |
| fig3 | 学习时间 vs CGPA 散点图 |
| fig4 | 睡眠时间 vs CGPA 散点图 |
| fig5 | 数值特征相关性热力图 |
| fig6 | Top 10 特征重要性（随机森林） |

## 建模与评估

### 模型对比

同时训练两种回归模型进行对比：

| 模型 | 说明 |
|------|------|
| Linear Regression | 线性回归（基线模型） |
| Random Forest | 随机森林回归（100 棵决策树） |

### 特征编码

分类变量（`Branch`、`Diet_Type`、`Residence`）使用独热编码（One-Hot Encoding，`drop_first=True`）转为数值。

### 训练/测试划分

80% 训练集 / 20% 测试集，`random_state=42`。

## 运行方式

### 1. 下载数据集（可选）

```bash
cd project2_2
python DownloadCSV.py
```

需要安装 `kagglehub` 并配置 Kaggle API 密钥。数据集也可手动从 [Kaggle](https://www.kaggle.com/datasets/rafi003/student-lifestyle-and-academic-performance-dataset) 下载并放入 `data/` 目录。

### 2. 运行完整分析

```bash
python main.py
```

输出：
- 控制台打印数据概览、清洗前后样本量、描述性统计、模型评估结果、特征重要性
- `outputs/` — CSV 结果文件
- `figures/` — 可视化图表

## 环境要求

```bash
pip install pandas matplotlib seaborn scikit-learn
```

- Python 3.8+
- pandas
- matplotlib
- seaborn
- scikit-learn
- kagglehub（仅下载数据集时需要）
