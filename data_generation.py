import numpy as np
import pandas as pd

# 算例数据（根据实验算例数目要求随机生成算例，修改n即可）
n = 20
# 设置随机种子以便结果可重现
np.random.seed(42)
# 直接生成(0, 10]之间的均匀分布，排除0
job_size = np.random.uniform(low=1e-10, high=10.0, size=n)
# 使用astype进行内存优化
job_size = np.round(job_size, 3).astype(np.float32)
job_size = np.sort(job_size)  # 从小到大SPT排序
S = 10

# 将生成的数据转换为DataFrame，方便保存为CSV并添加列名
df = pd.DataFrame({
    'job_id': range(1, n+1),  # 添加作业编号（1到20）
    'job_size': job_size      # 作业大小数据
})

# 保存为CSV文件
# index=False 表示不保存行索引，header=True 保留列名
df.to_csv('job_size_data.csv', index=False, header=True)

# 打印生成的数据，方便查看
print("生成的作业大小数据（SPT排序后）：")
print(df)
print("\n数据已保存到 job_size_data.csv 文件中")