import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import spearmanr

# 生成示例数据
np.random.seed(0)
data = pd.DataFrame({
    'Feature1': np.random.randn(100),
    'Feature2': np.random.randn(100),
    'Feature3': np.random.randn(100),
    'Feature4': np.random.randn(100),
    'Feature5': np.random.randn(100),
    'Feature6': np.random.randn(100)
})

# 计算Spearman相关性系数矩阵
corr_matrix, p_values = spearmanr(data)

# 设置绘图风格
sns.set(style='white')

# 创建绘图
fig, ax = plt.subplots(figsize=(10, 8))

# 绘制下三角矩阵中的相关性系数，并根据相关性大小调整颜色深浅
for i in range(corr_matrix.shape[0]):
    for j in range(i + 1):
        correlation = corr_matrix[i, j]
        color = plt.cm.coolwarm((correlation + 1) / 2)  # 将相关性系数映射到颜色
        ax.text(j + 0.5, corr_matrix.shape[0] - i - 1 + 0.5, f"{correlation:.2f}",
                ha='center', va='center', color='black', fontsize=10,
                bbox=dict(facecolor=color, edgecolor='none', boxstyle='round,pad=0.3'))

# 绘制上三角矩阵中的圆形和显著性标记
for i in range(corr_matrix.shape[0]):
    for j in range(i + 1, corr_matrix.shape[1]):
        corr = corr_matrix[i, j]
        size = abs(corr) * 1000  # 圆的大小比例
        color = 'red' if corr > 0 else 'blue'
        ax.scatter(j + 0.5, corr_matrix.shape[0] - i - 1 + 0.5, s=size, color=color, alpha=0.5)
        
        # 显著性标记
        significance_level = p_values[i, j]
        if significance_level < 0.001:
            ax.text(j + 0.5, corr_matrix.shape[0] - i - 1 + 0.5, '***', ha='center', va='center', color='black')
        elif significance_level < 0.01:
            ax.text(j + 0.5, corr_matrix.shape[0] - i - 1 + 0.5, '**', ha='center', va='center', color='black')
        elif significance_level < 0.05:
            ax.text(j + 0.5, corr_matrix.shape[0] - i - 1 + 0.5, '*', ha='center', va='center', color='black')

# 设置轴标签和标题
ax.set_xticks(np.arange(corr_matrix.shape[1]) + 0.5)
ax.set_yticks(np.arange(corr_matrix.shape[0]) + 0.5)
ax.set_xticklabels(data.columns, rotation=45, ha='right')
ax.set_yticklabels(data.columns[::-1])
ax.set_title('Spearman Correlation Heatmap with Significance Levels')

# 添加color bar
norm = plt.Normalize(vmin=-1, vmax=1)
sm = plt.cm.ScalarMappable(cmap="coolwarm", norm=norm)
sm.set_array([])
fig.colorbar(sm, ax=ax)

# 调整网格线
ax.set_xticks(np.arange(corr_matrix.shape[1]), minor=True)
ax.set_yticks(np.arange(corr_matrix.shape[0]), minor=True)
ax.grid(which='minor', color='black', linestyle='-', linewidth=1)
ax.tick_params(which='minor', size=0)
ax.grid(False)  # 去掉默认的主要网格线

plt.show()
