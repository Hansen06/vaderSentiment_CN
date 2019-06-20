import os
from inspect import getsourcefile
from io import open

lexicon_file=r"G:\3. 20170901-至今-情感分析\情感 Research\code\vaderSentiment\vaderSentiment\vader_lexicon2.txt"

_this_module_file_path_ = os.path.abspath(getsourcefile(lambda: 0))
lexicon_full_filepath = os.path.join(os.path.dirname(_this_module_file_path_), lexicon_file)
with open(lexicon_full_filepath, encoding='utf-8') as f:
    lexicon_full_filepath = f.readlines()


lex_dict = {}
for line in lexicon_full_filepath:
    (word, measure) = line.strip().split('\t')[0:2]
    print(line.strip().split('\t')[0:2])
    lex_dict[word] = float(measure)
