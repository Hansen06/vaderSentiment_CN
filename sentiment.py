import pynlpir

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
# from vaderSentiment import SentimentIntensityAnalyzer

f_w = open(r'E:\F盘\合并-20181030\label_pre.dat', 'w', encoding='utf-8')

analyzer = SentimentIntensityAnalyzer()
with open(r'E:\F盘\合并-20181030\final-泰国沉船评论文本-提取长度大于20小于60-去重-人工筛选-繁简转换-分词-1.dat', 'r', encoding='utf-8') as f:
    for sentence in f.readlines():
        vs = analyzer.polarity_scores(sentence.strip())

        # positive : compound  score >= 0.05
        # neutral  : (compound score > -0.05) and (compound score < 0.05)
        # negative : compound  score <= -0.05

        score = float(vs['compound'])
        print("{:-<65} {}".format(sentence, str(vs['compound'])))
        if score > -0.05:
            f_w.write('1' + '\n')
        elif score <= -0.05:
            f_w.write('0' + '\n')

print('completed!')