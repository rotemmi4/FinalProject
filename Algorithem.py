import re
import random
from nltk import tokenize

def getWeights(text,type):
    arr = []
    i=0
    name = text["name"]
    sentences = re.split(r' [\.\?!][\'"\)\]] *', text["content"])
    for stuff in sentences:
        if type=='random':
            weight= "%.2f" % random.random()
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
    return response
