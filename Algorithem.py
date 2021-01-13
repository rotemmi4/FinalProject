import re
import random
from nltk import tokenize

def getWeights(text,type):
    arr = []
    i=0
    name=""
    sentences = re.split(r' [\.\?!][\'"\)\]] *', text)
    for stuff in sentences:
        if i==0:
            name= stuff
        if type=='random':
            weight= random.random()
            dic= {
                "sentenceNum":i,
                "content": stuff,
                "weight":weight
            }
            arr.append(dic)
            i+=1

    response={
        "sentences": arr,
        "name": name
    }
    print(response)
    return response

getWeights("hello. it's me",'random')