# -*- coding: utf-8 -*-
"""
项目名称：基于学生数字行为数据的学习表现影响因素分析与预测
文件名称：main.py

数据文件位置：
data/student_digital_behavior.csv

说明：
本代码使用你当前 CSV 的真实字段名：
Age, Branch, Study_Hours_per_Day, Sleep_Hours, Screen_Time_Hours,
Gym_Hours_per_Week, Diet_Type, Attendance_Percentage, Stress_Level_1_to_10,
Residence, Internal_Marks, CGPA

本项目以 CGPA 作为学习表现指标，分析学习时间、睡眠时间、屏幕时间、
出勤率、压力水平等因素与学习表现之间的关系。
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# ======================
# 1. 基本设置
# ======================

DATA_PATH = "data/student_digital_behavior.csv"
FIGURE_DIR = "figures"
OUTPUT_DIR = "outputs"

os.makedirs(FIGURE_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

RANDOM_STATE = 42

# 因变量：学习表现
TARGET = "CGPA"

# 自变量：用于预测 CGPA 的因素
# 注意：Internal_Marks 也是学习表现类指标，容易造成结果过于直接，所以这里不放进模型。
FEATURES = [
    "Age",
    "Branch",
    "Study_Hours_per_Day",
    "Sleep_Hours",
    "Screen_Time_Hours",
    "Gym_Hours_per_Week",
    "Diet_Type",
    "Attendance_Percentage",
    "Stress_Level_1_to_10",
    "Residence"
]


# ======================
# 2. 读取数据
# ======================

df = pd.read_csv(DATA_PATH)

print("数据读取成功")
print("数据规模：", df.shape)
print("\n字段名：")
print(df.columns.tolist())
print("\n前5行数据：")
print(df.head())


# ======================
# 3. 检查字段
# ======================

needed_cols = FEATURES + [TARGET]
missing_cols = [col for col in needed_cols if col not in df.columns]

if missing_cols:
    raise ValueError("以下字段在 CSV 中不存在，请检查字段名：" + str(missing_cols))


# ======================
# 4. 数据清洗
# ======================

before_rows = len(df)

# 只保留本项目需要的字段
df = df[needed_cols].copy()

# 删除重复行
df = df.drop_duplicates()

# 数值字段和分类字段分开处理
numeric_cols = [
    "Age",
    "Study_Hours_per_Day",
    "Sleep_Hours",
    "Screen_Time_Hours",
    "Gym_Hours_per_Week",
    "Attendance_Percentage",
    "Stress_Level_1_to_10",
    "CGPA"
]

category_cols = [
    "Branch",
    "Diet_Type",
    "Residence"
]

# 数值字段转成数值类型，并用中位数填充缺失值
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(df[col].median())

# 分类字段用众数填充缺失值
for col in category_cols:
    df[col] = df[col].fillna(df[col].mode()[0])

# 删除明显不合理的异常值
df = df[(df["Age"] >= 15) & (df["Age"] <= 35)]
df = df[(df["Study_Hours_per_Day"] >= 0) & (df["Study_Hours_per_Day"] <= 24)]
df = df[(df["Sleep_Hours"] >= 0) & (df["Sleep_Hours"] <= 24)]
df = df[(df["Screen_Time_Hours"] >= 0) & (df["Screen_Time_Hours"] <= 24)]
df = df[(df["Gym_Hours_per_Week"] >= 0) & (df["Gym_Hours_per_Week"] <= 40)]
df = df[(df["Attendance_Percentage"] >= 0) & (df["Attendance_Percentage"] <= 100)]
df = df[(df["Stress_Level_1_to_10"] >= 1) & (df["Stress_Level_1_to_10"] <= 10)]
df = df[(df["CGPA"] >= 0) & (df["CGPA"] <= 10)]

after_rows = len(df)

print("\n数据清洗完成")
print("清洗前样本量：", before_rows)
print("清洗后样本量：", after_rows)

cleaned_path = os.path.join(OUTPUT_DIR, "cleaned_student_digital_behavior.csv")
df.to_csv(cleaned_path, index=False, encoding="utf-8-sig")
print("清洗后数据已保存：", cleaned_path)


# ======================
# 5. 描述性统计
# ======================

print("\n描述性统计：")
print(df[numeric_cols].describe())

stats_path = os.path.join(OUTPUT_DIR, "descriptive_statistics.csv")
df[numeric_cols].describe().to_csv(stats_path, encoding="utf-8-sig")


# ======================
# 6. 数据可视化
# ======================

# 图1：屏幕时间分布
plt.figure(figsize=(7, 5))
sns.histplot(df["Screen_Time_Hours"], bins=20, kde=True)
plt.title("Distribution of Screen Time")
plt.xlabel("Screen Time Hours")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(FIGURE_DIR, "fig1_screen_time_distribution.png"), dpi=300)
plt.close()

# 图2：屏幕时间与 CGPA
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="Screen_Time_Hours", y="CGPA")
plt.title("Screen Time vs CGPA")
plt.xlabel("Screen Time Hours")
plt.ylabel("CGPA")
plt.tight_layout()
plt.savefig(os.path.join(FIGURE_DIR, "fig2_screen_time_vs_cgpa.png"), dpi=300)
plt.close()

# 图3：学习时间与 CGPA
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="Study_Hours_per_Day", y="CGPA")
plt.title("Study Hours vs CGPA")
plt.xlabel("Study Hours per Day")
plt.ylabel("CGPA")
plt.tight_layout()
plt.savefig(os.path.join(FIGURE_DIR, "fig3_study_hours_vs_cgpa.png"), dpi=300)
plt.close()

# 图4：睡眠时间与 CGPA
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df, x="Sleep_Hours", y="CGPA")
plt.title("Sleep Hours vs CGPA")
plt.xlabel("Sleep Hours")
plt.ylabel("CGPA")
plt.tight_layout()
plt.savefig(os.path.join(FIGURE_DIR, "fig4_sleep_hours_vs_cgpa.png"), dpi=300)
plt.close()

# 图5：相关性热力图
plt.figure(figsize=(9, 7))
corr = df[numeric_cols].corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.savefig(os.path.join(FIGURE_DIR, "fig5_correlation_heatmap.png"), dpi=300)
plt.close()


# ======================
# 7. 建立预测模型
# ======================

X = df[FEATURES]
y = df[TARGET]

# 将 Branch、Diet_Type、Residence 这类文字变量转成 0/1 变量
X = pd.get_dummies(X, drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=RANDOM_STATE
)

models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(
        n_estimators=100,
        random_state=RANDOM_STATE
    )
}

results = []

for model_name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results.append([model_name, mae, mse, r2])

results_df = pd.DataFrame(results, columns=["Model", "MAE", "MSE", "R2"])

print("\n模型评价结果：")
print(results_df)

result_path = os.path.join(OUTPUT_DIR, "model_results.csv")
results_df.to_csv(result_path, index=False, encoding="utf-8-sig")


# ======================
# 8. 特征重要性分析
# ======================

rf_model = models["Random Forest"]

importance_df = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_
}).sort_values(by="Importance", ascending=False)

print("\n随机森林特征重要性：")
print(importance_df)

importance_path = os.path.join(OUTPUT_DIR, "feature_importance.csv")
importance_df.to_csv(importance_path, index=False, encoding="utf-8-sig")

plt.figure(figsize=(9, 6))
sns.barplot(data=importance_df.head(10), x="Importance", y="Feature")
plt.title("Top 10 Feature Importance")
plt.xlabel("Importance")
plt.ylabel("Feature")
plt.tight_layout()
plt.savefig(os.path.join(FIGURE_DIR, "fig6_feature_importance.png"), dpi=300)
plt.close()


# ======================
# 9. 运行结束
# ======================

print("\n运行完成")
print("图表已保存到 figures 文件夹")
print("清洗后数据、描述性统计、模型结果和特征重要性已保存到 outputs 文件夹")
print("注意：本项目只能说明变量之间的相关关系，不能直接证明因果关系。")
