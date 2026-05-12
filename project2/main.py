from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split


# =========================
# 1. 创建输出目录
# =========================
Path("images").mkdir(exist_ok=True)


# =========================
# 2. 加载加州房价数据集
# =========================
print("正在加载 California Housing 数据集...")
housing = fetch_california_housing(as_frame=True)

# 特征数据
X = housing.data

# 目标值（房价中位数，单位：10万美元）
y = housing.target

# 合并为一个 DataFrame，便于查看
df = pd.concat([X, y.rename("MedHouseVal")], axis=1)

print("\n数据集前 5 行：")
print(df.head())

print("\n数据集形状：", df.shape)
print("特征数量：", X.shape[1])
print("样本数量：", X.shape[0])


# =========================
# 3. 划分训练集和测试集
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\n训练集大小：", X_train.shape)
print("测试集大小：", X_test.shape)


# =========================
# 4. 创建并训练随机森林回归模型
# =========================
print("\n开始训练 Random Forest 模型...")

model = RandomForestRegressor(
    n_estimators=200,
    max_depth=20,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

print("模型训练完成。")


# =========================
# 5. 模型预测
# =========================
y_pred = model.predict(X_test)


# =========================
# 6. 模型评估
# =========================
mse = mean_squared_error(y_test, y_pred)
rmse = mse ** 0.5
r2 = r2_score(y_test, y_pred)

print("\n模型评估结果：")
print(f"MSE  = {mse:.4f}")
print(f"RMSE = {rmse:.4f}")
print(f"R²   = {r2:.4f}")


# =========================
# 7. 特征重要性可视化
# =========================
feature_importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=True)

plt.figure(figsize=(8, 5))
feature_importance.plot(kind="barh")
plt.title("Feature Importance")
plt.xlabel("Importance")
plt.tight_layout()
plt.savefig("images/feature_importance.png")
plt.close()

print("已生成 images/feature_importance.png")


# =========================
# 8. 真实值 vs 预测值散点图
# =========================
plt.figure(figsize=(6, 6))
plt.scatter(y_test, y_pred, alpha=0.5)

min_val = min(y_test.min(), y_pred.min())
max_val = max(y_test.max(), y_pred.max())
plt.plot([min_val, max_val], [min_val, max_val], "r--")

plt.xlabel("Actual House Value")
plt.ylabel("Predicted House Value")
plt.title("Actual vs Predicted")
plt.tight_layout()
plt.savefig("images/prediction_scatter.png")
plt.close()

print("已生成 images/prediction_scatter.png")


# =========================
# 9. 保存模型
# =========================
joblib.dump(model, "model.pkl")
print("模型已保存到 model.pkl")


# =========================
# 10. 保存预测结果
# =========================
results = pd.DataFrame({
    "Actual": y_test.values,
    "Predicted": y_pred
})

results.to_csv("prediction_results.csv", index=False)
print("预测结果已保存到 prediction_results.csv")


# =========================
# 11. 项目完成
# =========================
print("\n项目运行完成。")
print("生成文件：")
print(" - model.pkl")
print(" - prediction_results.csv")
print(" - images/feature_importance.png")
print(" - images/prediction_scatter.png")