#!/usr/bin/env python
# coding: utf-8

# In[2]:
# import algorithems.summarizer


from summarizer import Summarizer

sample_doc = '''

West German Chancellor Helmut Kohl declared on his return from Moscow on Sunday  that "the way is now free" for German reunification.    His meeting with Soviet President Mikhail S. Gorbachev convinced him, he told  West German radio, that the two German states should "enter into negotiations  as quickly as possible" after the March 18 East German election. 
   Kohl will meet with East German Prime Minister Hans Modrow on Tuesday and  Wednesday in Bonn to discuss immediate steps in economic cooperation, including  monetary union, to prevent the collapse of the faltering East German economy.    "Political and economic union go hand in hand," Kohl said.    He said that immediate steps must be taken on the economic front to "stop the  hemorrhage of East Germans to the Federal Republic and keep them in their  heimat," or home, in East Germany.   
 Kohl said that his talks with Gorbachev -- who told him that reunification is a  matter for the Germans themselves to decide -- could lead to an "economic  breakthrough" in East Germany, which in turn could provide a "push forward" for  all of Europe.    Asked how soon the two Germanys could merge, Kohl declared that the March  election has to come first, and "then I think it will all go very quickly."    The chancellor said that almost all of the political parties and opposition  groups in East Germany now support reunification. And after the election, he  said, "they will want to put their programs into practice quickly."  
  Gorbachev inquired about plans by West German politicians to campaign in East  Germany, Kohl said, adding that the Soviet leader did not appear to be upset  about such political activity.    West Germany's Social Democratic Party is expected to campaign heavily in East  Germany in support of a fledging branch of the party that has taken a  surprisingly strong lead in public opinion polls.    Major members of the party, including former Chancellor Willy Brandt, are  scheduled to appear at rallies on behalf of the East German Social Democrats. 
   With the surge of the East German Social Democrats, political analysts are  pointing to the strange role they could play in the ultimate political fate of  Kohl.    Ever since reunification became a blazing issue, Kohl's standing in West German  opinion polls has risen, and if the national elections, now scheduled for  December, were held today, he would have a good chance of leading his Christian  Democratic Union to victory.    But if the two Germanys are fused before the West Germany election in December,  the growing number of Social Democratic voters in what today is East Germany  who would presumably be allowed to vote in December -- could easily tip the  balance away from the Christian Democrats, pushing Kohl out of the government  leadership.   

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