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

def get_random_text(numOfText):
    texts=TextConcrete.get_texts()
    randomTexts = []
    res = []
    for i in range(1,numOfText):
        found = False
        while(found==False):
            num=random.randint(1, len(texts))
            if(num not in randomTexts):
                randomTexts.append(num)
                found = True
    for j in randomTexts:
        res.append(TextConcrete.get_text_by_id(j)[0])
    # for j in range(len(texts)):
    #     if(texts[j]["id"] in randomTexts):
    #         res.append(texts[j])
    return res

def get_random_visualization(numOfVisualizations):
    randomVisualizations = []
    res =[]
    for i in range(numOfVisualizations):
        found = False
        while (found == False):
            num = random.randint(0, 5)
            if (randomVisualizations.count(num)<2):
                randomVisualizations.append(num)
                found = True
    for visu in randomVisualizations:
        if visu == 0:
            res.append("Without Visualization")
        elif visu == 1 :
            res.append("Gradual Highlight")
        elif visu == 2 :
            res.append("Highlight")
        elif visu == 3 :
            res.append("Increased Font")
        elif visu == 4 :
            res.append("Gradual Font")
        else :
            res.append("Summary Only")
    return res

def get_random_text_and_visualizations(numberOfRandom):
    res =[]
    texts = get_random_text(numberOfRandom)
    visualization = get_random_visualization(numberOfRandom)
    for j in range(len(texts)):
        dic={}
        dic["id"]=texts[j]["id"]
        dic["name"]=texts[j]["name"]
        dic["visualization"]=visualization[j]
        res.append(dic)

    return res




