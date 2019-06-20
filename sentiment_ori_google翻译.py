import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from googletrans import Translator
import time

f_w = open(r'G:\3. 20170901-至今-情感分析\毕设论文\paper\情感\词典标注-ori\pre_label-ori_5.txt', 'a+', encoding='utf-8')
f_s = open(r'G:\3. 20170901-至今-情感分析\毕设论文\paper\情感\词典标注-ori\pre_label-score-google_5.txt', 'a+', encoding='utf-8')

analyzer = SentimentIntensityAnalyzer()
translator = Translator(service_urls=['translate.google.cn'])
with open(r'G:\3. 20170901-至今-情感分析\毕设论文\paper\情感\词典标注-ori\final-泰国沉船评论文本-提取长度大于20小于60-去重-人工筛选-繁简转换.dat', 'r', encoding='utf-8') as f:
    for sentence in f.readlines()[9770:]:

        time.sleep(3)
        translation = translator.translate(sentence, src='zh-cn', dest='en').text
        vs = analyzer.polarity_scores(translation)
        print("- {: <69}\t {} ".format(sentence, str(vs['compound'])))

        f_s.write("{}\t {} {} \n ".format(sentence, str(vs['compound']), str(vs)))
        score = float(vs['compound'])
        if score > -0.05:
            f_w.write('1' + '\n')
        elif score <= -0.05:
            f_w.write('0' + '\n')

f_w.close()
f_s.close()
print('completed!')