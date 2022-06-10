import json
from snownlp import SnowNLP
with open("data/东航坠机.csv", "r", encoding="utf-8") as f:
    data = f.readlines()
    sentimentList = []
    for i in data:
        s=SnowNLP(i)
        print(s.sentences)
        sentimentList.append(s.sentiments)
with open("data/emtion.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(sentimentList))


with open("data/emtion.json", "r", encoding="utf-8") as f:
    data = json.loads(f.read())
    postive = 0
    negative = 0
    neutral = 0
    for i in data:
        if i > 0.5:
            postive += 1
        elif i < 0.5:
            negative += 1
        else:
            neutral += 1
            
    emtion_list = [postive, negative, neutral]
            
import matplotlib.pyplot as plt
import seaborn as sns
# 标题
plt.title("情感分析")
# 设置字体解决中文乱码
plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
labels = ['积极的', '消极的', '中性']
colors = sns.color_palette('bright')
plt.pie(emtion_list, labels=labels,colors = colors, autopct = '%0.0f%%')
plt.savefig('data/emtion.png')

   