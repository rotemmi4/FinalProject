#!/usr/bin/env python
# coding: utf-8

# In[2]:
# import algorithems.summarizer


from summarizer import Summarizer

sample_doc = '''
With the winds of Hurricane Gilbert clocked at 175 miles per hour, U.S. weather officials called Gilbert the most intense hurricane ever recorded in the Western Hemisphere.  Mark Zimmer, a meterologist at the National Hurricane Center, reported an Air Force reconnaissance plane measured the barometric pressure at Gilbert's center at 26.13 inches at 5:52 p.m. EDT on Tuesday. 
Gilbert was barreling toward Mexico's Yucatan Peninsula.  ``That's the lowest pressure ever measured in the Western Hemisphere,'' Zimmer said. The previous record low pressure of 26.35 inches was set by the 1935 Labor Day hurricane that struck the Florida Keys with winds above 150 mph, killing 408 people, he said.  With tropical storm force winds extending 250 miles north and 200 miles south of the hurricane's center, Gilbert also was one of the largest. But because the circumference of a hurricane changes so often during its course, no records are kept on their overall size, said center meterologist Jesse Moore.  Hurricane Debby, which barely crossed the 74 mph threshold to hurricane strength before striking Mexico last month, was probably about half that size, Moore said.  
Gilbert is one of only three Category 5 storms in the hemisphere since weather officials began keeping detailed records. The others were the 1935 Labor Day hurricane and Hurricane Camille, which bulldozed the Mississippi Coast with 172 mph winds and a 28-foot wave in 1969, leaving $1.4 billion in damage and 256 dead.  A 1900 hurricane is responsible for the worst natural disaster in U.S. history, however. That storm hit Galveston, Texas, Sept. 8 and killed more than 6,000 people.  Category 5 storms have winds greater than 155 mph, barometric pressure of less than 27.17 inches and a storm surge higher than 18 feet.  The storm surge _ a great dome of water that follows the eye of the hurricane across coastlines, bulldozing everything in its path _ accounts for nine out of 10 hurricane fatalities. 
 Camille's storm surge was 25 feet high, but the hurricane center was forecasting a surge of only 8-12 feet for Gilbert, Zimmer said.  The damage from these worst-case hurricanes is catastrophic _ shrubs and trees blown down, all street signs gone, roofs and windows blown away and shattered, and mobile homes destroyed.  ``Moisture and heat are what drives the hurricane,'' Zimmer said. ``The engine itself is this tall chimney of warm, moist air in the center. If the atmospheric conditions in general allow this warm chimney to build to very high levels, 10-12 miles high, then you can have a severe hurricane.''  Category 4 storms cause extreme damage with winds from 131 to 155 mph, surge of 13-18 feet and pressure of 27.17 to 27.90. The weakest hurricanes, Category 1, cause minimal damage with winds of 74 to 95 mph, 4-5 foot surge and pressure at 28.94 or more.
'''
#model = Summarizer()
#result = model(sample_doc, min_length=1,max_length=10000000,ratio=0.1)
# features=model.features
# centroids=model.centroids
# args=model.args
#model.df=df
#print(model.df)

def Bert_alg(text):
    ans=[]
    model=Summarizer()
    result = model(sample_doc, min_length=1,max_length=10000000,ratio=0.1)
    for index, row in model.df.iterrows():
        dic = {
            "sentenceNum": row['Id'],
            "content": row['Sent'],
            "weight": row['Weight'],
        }
        ans.append(dic)
    return ans

print(Bert_alg(sample_doc))