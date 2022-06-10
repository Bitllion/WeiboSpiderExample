import pandas as pd
import numpy as np
from pandas import DataFrame, Series
from datetime import datetime
from matplotlib import pyplot as plt
# 读入文件
df = pd.read_csv('data\东航坠机.csv')
# 转化为数据框
df = DataFrame(df)

df['publish_time'] = pd.to_datetime(df['publish_time'])
df = df[['publish_time','forward_num']]

#转化天
df['publish_time'] = [datetime.strftime(x,'%Y-%m-%d') for x in df['publish_time']]
# 分组合并
df = df.groupby('publish_time').sum()

# 保存
df.to_csv('data\sum.csv')

#绘图
data = pd.read_csv('data\sum.csv')
plt.rcParams['font.sans-serif'] = 'simhei'
plt.rcParams['axes.unicode_minus']=False
data = np.array(data)
date = []
num = []
for i in range(len(data)):
    date.append(data[i][0])
    num.append(data[i][1])
    
plt.fill_between(date, num ,color="skyblue", alpha=0.4)
for i in range(len(data)):
    plt.text(date[i], num[i], num[i], ha='center', va='bottom')
    
plt.title('东航坠机')

plt.savefig('data\mianji.png')

