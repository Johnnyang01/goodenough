import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 假设有以下数据
time = np.linspace(0, 100, 500)  # 时间点，0到100之间的500个点
rmsd = np.sin(time / 10) + np.random.normal(0, 0.1, len(time))  # 模拟的RMSD数据

# 创建主图和附图
fig = plt.figure(figsize=(10, 6))
gs = fig.add_gridspec(1, 2, width_ratios=[4, 1], wspace=0.00)

# 主图
ax_main = fig.add_subplot(gs[0])
ax_main.plot(time, rmsd, label='RMSD')
ax_main.set_xlabel('Time (ns)')
ax_main.set_ylabel('RMSD (Å)')
ax_main.legend()
#ax_main.grid(True)

# 附图
ax_side = fig.add_subplot(gs[1], sharey=ax_main)
sns.kdeplot(rmsd, vertical=True, ax=ax_side, color='r', fill=True)
ax_side.set_xlabel('Density')
#ax_side.set_ylabel('')

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 假设有以下数据
time = np.linspace(0, 100, 500)  # 时间点，0到100之间的500个点
rmsd = np.sin(time / 10) + np.random.normal(0, 0.1, len(time))  # 模拟的RMSD数据

# 创建主图和附图
fig, (ax_main, ax_side) = plt.subplots(nrows=1, ncols=2, figsize=(10, 6), 
                                       gridspec_kw={'width_ratios': [4, 1], 'wspace': 0.00})

# 绘制RMSD随时间变化的曲线
ax_main.plot(time, rmsd, label='RMSD')
ax_main.set_xlabel('Time (ns)')
ax_main.set_ylabel('RMSD (Å)')
ax_main.legend(loc='upper left')
ax_main.grid(True)

# 绘制RMSD的分布图
sns.kdeplot(rmsd, vertical=True, ax=ax_side, color='r', fill=True)

# 隐藏分布图的左边轴，使其看起来像主图的右边框轴
ax_side.yaxis.set_visible(False)
ax_side.set_ylabel('')
ax_side.set_xlabel('Density')

# 调整布局
plt.tight_layout()
plt.show()

