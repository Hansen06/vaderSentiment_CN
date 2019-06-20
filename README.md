# vaderSentiment_CN
基于情感词典进行情感分析，目前中文能达到80%

根据项目 https://github.com/cjhutto/vaderSentiment 进行中文版开发

本项目只进行正负两类的判别，<br>
根据原项目的规则：<br>
>positive sentiment: compound score >= 0.05<br>
neutral sentiment: (compound score > -0.05) and (compound score < 0.05)<br>
negative sentiment: compound score <= -0.05<br>

本项目使用以下规则进行判别：<br>
>positive sentiment: compound score > -0.05<br>
negative sentiment: compound score <= -0.05<br>
  
本项目没有做对应的中文情感词典，而是将中文调用google翻译，翻译成英文进行判定，没想到效果还是不错的。<br>
实验数据集采用谭松波老师的酒店评论数据集。
