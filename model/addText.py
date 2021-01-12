import os
import sqlite3
from model import TextConcrete


def addtext(folderName):
    for file in os.listdir(folderName):
        fname= folderName+"/"+file
        f = open(fname, "r")
        text= f.read()
        TextConcrete.insert_text("name", text)



### addtext("C:/Users/meital/Desktop/פרוייקט/DUC/DUC_2002/texts/d061j")