import json
import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


f_w = open(r'G:\3. 20170901-至今-情感分析\情感 Research\code\酒店\pre_label-ori.txt', 'w', encoding='utf-8')
f_s = open(r'G:\3. 20170901-至今-情感分析\情感 Research\code\酒店\pre_label-score.txt', 'w', encoding='utf-8')

analyzer = SentimentIntensityAnalyzer()
with open(r'G:\3. 20170901-至今-情感分析\情感 Research\code\酒店\ChnSentiCorp.txt', 'r', encoding='utf-8') as f:
    for sentence in f.readlines():
        to_lang = "en"
        from_lang = "zh"
        api_url = "http://mymemory.translated.net/api/get?q={}&langpair={}|{}".format(sentence, from_lang, to_lang)
        hdrs = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
            'Accept-Encoding': 'none',
            'Accept-Language': 'en-US,en;q=0.8',
            'Connection': 'keep-alive'}
        response = requests.get(api_url, headers=hdrs)
        response_json = json.loads(response.text)
        translation = response_json["responseData"]["translatedText"]
        vs = analyzer.polarity_scores(translation)
        print("- {: <69}\t {} ".format(sentence, str(vs['compound'])))

        f_s.write("{}\t {} {} ".format(sentence, str(vs['compound']), str(vs)) + "\n")
        score = float(vs['compound'])
        if score > -0.05:
            f_w.write('1' + '\n')
        elif score <= -0.05:
            f_w.write('0' + '\n')

f_w.close()
f_s.close()
print('completed!')