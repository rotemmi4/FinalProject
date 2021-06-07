#!/usr/bin/env python
# coding: utf-8

# In[2]:
# import algorithems.summarizer


from summarizer import Summarizer

sample_doc = '''

Prince Philip on Sunday condemned the ``senseless'' killing of 10 Royal Marines musicians in an IRA bombing, and Britain's defense secretary said he warned all military bases of the risk of similar attacks.  Clergyman urged relatives and friends of dead and maimed musicians to forgive the bombers. ``Only forgiveness breaks the tie between the hater and the hated,'' the Rev. George Lings told mourners.  The prince, husband of Queen Elizabeth II and captain general of the Royal Marines, visited injured men in the hospital and toured the severely damaged Royal Marines School of Music in Deal, southeast Britain.  ``It will not help the IRA win anything,'' said Philip, who wore a Royal Marines tie. ``It is senseless. One simply wonders what sort of mentality can even contemplate such meaningless acts. It is appalling.''  He paid tribute to the 12 injured men, five of whom were critically wounded.  The prince was accompanied by Viscountess Mountbatten, daughter of Lord Mountbatten, who was killed by an IRA bomb on his boat in 1979. Mountbatten was India's last viceroy and a cousin of the queen.  British military installations are a frequent target of the Irish Republican Army in its campaign to end British rule in Northern Ireland and unite the predominantly Protestant province with the Roman Catholic Republic of Ireland.  Defense Secretary Tom King said Sunday he has issued an alert to all military installations to prevent other attacks. He would not give details.  ``The perpetrators of the latest outrage are at large and there is a risk of other attacks,'' King said. ``That is why we are taking a number of other steps.''  King defended the use of private security firms hired to guard the Deal school and 29 other ``low-risk'' military installations in Britain. Local residents and grieving relatives have said security was lax and should be turned back to the marines. King said the private firms will remain.  ``It is important to remember that what we need in these cases are eyes and ears and observation,'' King said on British Broadcasting Corp. radio.  ``Private security guards can be a very useful additional assistance. They also help to reduce the amount of time soldiers have to spend on what is not the most enjoyable part of their activity.''  At church services throughout the small port, clergymen urged mourners to pray for and forgive the bombers.  The Rev. Charles Howard, a Royal Navy chaplain, asked the 300-member congregation inside the barracks, ``if you can find room in your hearts ... pray for the men who perpetrated this terrible act, that God will soften their hearts and turn them from their violent and evil ways.''  Many cried as Howard read aloud the names of the 10 servicemen killed during a coffee break between band practices. It was the worst IRA attack on the British mainland since July 1982.  At nearby St. George's Church, formerly the Royal Marines' church, Lings said, ``no one says forgiveness is easy; no one says the terrorist deserves forgiveness.  ``But ... forgive them, they not what they do.''



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