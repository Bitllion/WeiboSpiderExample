import pandas as pd

df = pd.read_csv('data\东航坠机.csv')
df.head()


import jieba
import re

# 整理数据
df['content'] = df['content'].astype(str)
description = ''.join(df['content'])

#清洗数据
description = ''.join(re.findall('[\u4e00-\u9fa5]+', description))

# 分词&词频统计个
words = jieba.lcut(description)
wordfreqs = []
for word in set(words):
    freq = words.count(word)
    wordfreqs.append((word, freq))

# 保存结果
data = pd.DataFrame(wordfreqs, columns=['word', 'freq'])
data.to_csv('data\cipin.csv', index=False)

import stylecloud

stopwords = open('data\stopwords.txt', encoding='utf-8').read().split('\n')

stylecloud.gen_stylecloud(file_path='data\cipin.csv',
                          font_path='C:\Windows\Fonts\simhei.ttf',
                          output_name='data\wordcloud.png',
                          size=500,
                          icon_name='fas fa-cannabis',
                          custom_stopwords=stopwords)
