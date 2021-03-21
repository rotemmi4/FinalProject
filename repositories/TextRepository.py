import random

from model.concrete import TextConcrete


def insert_text(name, content):
    return TextConcrete.insert_text(name, content)

def update_text(id, name, content):
    return TextConcrete.update_text(id, name, content)

def delete_text(id):
    return TextConcrete.delete_text(id)

def get_text_by_id(id):
    return TextConcrete.get_text_by_id(id)

def get_texts():
    return TextConcrete.get_texts()

def get_random_text():
    texts=TextConcrete.get_texts()
    randomTexts = []
    res = []
    for i in range(16):
        found = False
        while(found==False):
            num=random.randint(1, len(texts))
            if(num not in randomTexts):
                randomTexts.append(num)
                found = True
    for j in range(len(texts)):
        if(texts[j]["id"] in randomTexts):
            res.append(texts[j])
    print(res)
    return res

        #print(texts[i]["id"])


