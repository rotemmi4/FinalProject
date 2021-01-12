import re
import random
def getWeights(text,type):
    response = [{
        "sentences": [
            {"sentenceNum": 1,
             "content": "",
             "weight": 0},
        ],
        "name": ""
    }]
    sentences = re.split(r' [\.\?!][\'"\)\]] *', text)
    for stuff in sentences:
        print(stuff)
        if type=='random':
            weight= random.random()
            print(weight)


    return response

getWeights("hello? it's me",'random')