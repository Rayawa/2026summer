import sys
import platform
import numpy as np
import pandas as pd
import matplotlib
import seaborn as sns
import sklearn

print("\n[Python 环境]")
print(f"Python 可执行文件: {sys.executable}")
print(f"Python 版本: {sys.version.split()[0]}")
print(f"操作系统: {platform.system()} {platform.release()}")
print(f"处理器架构: {platform.machine()}")

print("\n[基础科学计算库]")
print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"Matplotlib: {matplotlib.__version__}")
print(f"Seaborn: {sns.__version__}")
print(f"scikit-learn: {sklearn.__version__}")

print("\n[功能测试]")
a = np.array([1, 2, 3, 4, 5])
print(f"NumPy 平均值测试: {a.mean()}")

df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
print(f"Pandas DataFrame 测试: {df.shape}")

print("\n[PyTorch 检测]")
try:
    import torch
    print(f"PyTorch_Version: {torch.__version__}")
    print(f"CUDA: {torch.cuda.is_available()}")
    print(f"MPS: {torch.backends.mps.is_available()}")

    x = torch.tensor([1.0, 2.0, 3.0])
    print(f"PyTorch 张量均值测试: {x.mean().item()}")

except ImportError:
    print("PyTorch: 未安装")

print("\n" + "=" * 30)
print("环境检查完成！")
print("=" * 30)