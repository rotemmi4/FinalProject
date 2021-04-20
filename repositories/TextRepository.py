import random

from model.concrete import TextConcrete

colorDictionary = ["204,204,204","179,179,179","244,78,59","211,49,21","159,5,0","154,146,0","226,115,0","196,81,0","252,220,0","252,196,0","251,158,0","219,223,0","176,18,0","128,137,0","164,221,0","104,188,0","104,204,204","22,165,165","12,121,125","115,216,225","0,156,224","0,98,177","174,161,255","123,100,255","253,161,255","250,40,255","171,20,158"]

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
            num=random.randint(1, len(texts))
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
        if (visualization[j] == "Gradual Highlight" or visualization[j] == "Highlight"):
            num = random.randint(0, len(colorDictionary)-1)
            dic["propertyName"] = "color"
            dic["propertyValue"] = colorDictionary[num]
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


