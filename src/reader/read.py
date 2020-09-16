import json


class FlashCard:
    # pw = polish word
    # ps = polish sentence
    # ew = english word
    # es = english sentence
    def __init__(self,pw,ps,ew,es):
        self.pw = pw
        self.ps = ps
        self.ew = ew
        self.es = es

    def __str__(self):
        return f'{self.pw, self.ps, self.ew, self.es}'


def readFile(path):
    with open(path,"r",encoding="utf-8") as file:
        data = json.load(file)
    return data

def read(path):
    result = list()
    data = readFile(path=path)
    for i in data:
        pw = i['polish_word']
        ps = i['polish_sentence']
        ew = i['english_word']
        es = i['english_sentence']
        fc = FlashCard(pw,ps,ew,es)
        result.append(fc)
    return result
