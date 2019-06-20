import pynlpir

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# note: depending on how you installed (e.g., using source code download versus pip install), you may need to import like this:
# from vaderSentiment import SentimentIntensityAnalyzer

f_w = open(r'G:\3. 20170901-至今-情感分析\情感 Research\code\微博\pre_label.txt', 'w', encoding='utf-8')

analyzer = SentimentIntensityAnalyzer()
with open(r'G:\3. 20170901-至今-情感分析\情感 Research\code\微博\weibo-seg1.txt', 'r', encoding='utf-8') as f:
    for sentence in f.readlines():
        vs = analyzer.polarity_scores(sentence.strip())

        # positive : compound  score >= 0.05
        # neutral  : (compound score > -0.05) and (compound score < 0.05)
        # negative : compound  score <= -0.05

        score = float(vs['compound'])
        print("{} \t {}".format(sentence, str(vs['compound'])))
        if score > -0.05:
            f_w.write('1' + '\n')
        elif score <= -0.05:
            f_w.write('0' + '\n')

print('completed!')