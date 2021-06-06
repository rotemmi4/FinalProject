# # In[1]:
#
#
# from functools import lru_cache
# import pandas as pd
# import nltk
# from nltk.stem.porter import *
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords
# from nltk.tokenize import sent_tokenize
# import glob
# from itertools import combinations
# import networkx as nx
# import os
#
# from sklearn.preprocessing import MinMaxScaler
# stop_words_set = set(stopwords.words("english"))
# nltk.download('punkt')
# nltk.download('stopwords')
#
#
# # for path in path_list:
# #     name=path.split('\\')[1].split('.txt')[0]
# #     text_file=open(path, 'r').read()
# #     textrank(text_file, name)
#
#
# stemmer = PorterStemmer()
# path_files= 'algorithems/texts/'
#
# path_list=glob.glob(f'{path_files}*.txt')
#
#
# new_path = f"{path_files}Summarize"
# try:
#     os.mkdir(new_path)
# except OSError:
#     pass
#
# def skip_word(w):
#     if len(w) < 2 or w in stop_words_set:
#         return True
#     return False
#
# @lru_cache(maxsize=None)
# def word_stemming(w):
#     return stemmer.stem(w)
#
# def similarity(s1, s2):
#     if not len(s1) or not len(s2):
#         return 0.0
#     return len(s1.intersection(s2))/(1.0 * (len(s1) + len(s2)))
#
# # I suggest to use Jaccard index instead of this
# def jaccard_index(s1, s2):
#
#     # If both sets are empty, jaccard index is defined to be 1
#     index = 1.0
#     if s1 and s2:
#         intersection=len(s1.intersection(s2))
#         union=len(s1.union(s2))
#         index=float(intersection/union)
#     return index
#
# def sorensen_index(s1, s2):
#     index = 1.0
#     if s1 or s2:
#         index=2*len(s1.intersection(s2))/((len(s1) + len(s2)))
#     return index
#
#
# def textrank(text,name, func='else'):
#     sentences = sent_tokenize(text) #Splitting into sentences
#     r=len(sentences) # number of sentences
#     words_in_sentence = [set(word_stemming(word) for word in word_tokenize(sentence.lower()) if not skip_word(word) )
#          for sentence in sentences]
#     pairs = combinations(range(len(sentences)), 2)
#     if func=='jaccard':
#         scores = [(i, j, jaccard_index(words_in_sentence[i], words_in_sentence[j])) for i, j in pairs]
#     elif func=='sorensen':
#         scores = [(i, j, sorensen_index(words_in_sentence[i], words_in_sentence[j])) for i, j in pairs]
#     else:
#         scores = [(i, j, similarity(words_in_sentence[i], words_in_sentence[j])) for i, j in pairs]
#     g = nx.Graph()
#     g.add_weighted_edges_from(scores)
#     pr = nx.pagerank(g)
#     result=sorted(((id,pr[id],sen) for id,sen in enumerate(sentences)),key=lambda x: x[0],reverse=False)
#
#
#     result=pd.DataFrame(result)
#
#     scaler = MinMaxScaler(feature_range=(0, 1))
#
#
#
#     # result['ff'] = scaler.fit_transform(result['Weight'])
#
#     result.columns=['Index','Weight','Sentence']
#     result['d'] = scaler.fit_transform(result['Weight'].values.reshape(-1, 1))
#     result=result[['Index','Sentence','d']]
#     result_df = result
#     result.to_csv(new_path+'/'+name+'.csv',index=False)
#
#
#
#     ans=[]
#
#     for ind in result_df.index:
#
#         dic = {
#             "sentenceNum": int(result_df['Index'][ind]),
#             "content":result_df['Sentence'][ind],
#             "weight": str(result_df['d'][ind])
#         }
#         ans.append(dic)
#
#     # print(ans)
#     return ans
#
#
#
# def textRank_algorithm(text_file):
#     # name="CSV"
#     # for path in path_list:
#         # name = path.split('\\')[1].split('.txt')[0]
#         # text_file = open(path, 'r').read()
#     arr=[]
#     for sen in textrank(text_file['content'], text_file['name']):
#         arr.append(sen)
#     # arr = textrank(text_file['content'], text_file['name'])
#     response = {
#         "sentences": arr,
#         "name":  text_file['name']
#     }
#     # print(response,type(response))
#
#     return response
#
#
#
# # In[ ]: