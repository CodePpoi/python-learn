
import seaborn as sns
import matplotlib.pyplot as plt


# 设置背景
sns.set(style="darkgrid", color_codes=True)
# 使用示例数据
iris = sns.load_dataset('iris')
# 加载数据，使用散点图，设置点的颜色和样式
sns.pairplot(iris,
kind = 'scatter', #散点图
diag_kind = 'hist', #直方图
hue = 'species', #按照某一字段进行分类
palette = 'husl', #设置调色板
markers = ['o', 's', 'D'], #设置不同系列的点样式
height = 2 #图标大小
)
print(iris.info)
plt.show()