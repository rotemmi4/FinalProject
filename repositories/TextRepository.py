import random

from model.concrete import TextConcrete


colorDictionaryHighlight = ["Yellow","Green"]
colorDictionaryGradualHighlight = ["Yellow","Green","Orange"]
sizeDictionaryGradualHighlight = ['3','4','5','6','7','8']

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
    texts=get_all_id_texts()
    randomTexts = []
    res = []
    for i in range(0,numOfText):
        found = False
        while(found==False):
            num=random.randint(1, max(texts))
            if((num not in randomTexts) and (num in texts)):
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
        if( visualization[j] == "Summary Only" or visualization[j] == "Highlight" or visualization[j] == "Increased Font"  ):
            dic["threshold"] = float("{:.2f}".format(random.uniform(0.01, 1.0)))
        else:
            dic["threshold"] = 0.5
        if (visualization[j] == "Highlight"):
            num = random.randint(0, len(colorDictionaryHighlight)-1)
            dic["propertyName"] = "color"
            dic["propertyValue"] = "1"+","+colorDictionaryHighlight[num]
            dic["propertyType"] = "str"
        elif (visualization[j] == "Gradual Highlight"):
            numColor = random.randint(0, len(colorDictionaryGradualHighlight)-1)
            numSize = random.randint(0, len(sizeDictionaryGradualHighlight)-1)
            dic["propertyName"] = "color"
            dic["propertyValue"] = sizeDictionaryGradualHighlight[numSize]+","+colorDictionaryGradualHighlight[numColor]
            dic["propertyType"] = "str"
        elif (visualization[j] == "Gradual Font" or visualization[j] == "Increased Font"):
            dic["propertyName"] = "font"
            dic["propertyValue"] = "18"
            dic["propertyType"] = "int"
        else:
            dic["propertyName"] = "none"
            dic["propertyValue"] = "none"
            dic["propertyType"] = "none"

        res.append(dic)

    return res

def get_all_id_texts():
    ans =[]
    texts=TextConcrete.get_all_id_texts()
    for text in texts:
        ans.append(text["id"])
    return ans


# def get_visualization_id(type):
#         if type == "Without Visualization":
#             return 0
#         elif type == "Gradual Highlight" :
#             return 1
#         elif type == "Highlight" :
#             return 2
#         elif type == "Increased Font" :
#             return 3
#         elif type == "Gradual Font" :
#             return 4
#         else :
#             return 5

