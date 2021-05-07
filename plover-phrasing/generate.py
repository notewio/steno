# note: in verb.txt, verb "have", "do", "need" negative forms have been deleted 

enders = {

    "6": "have",

    "6G": "forget",

    "68": "feel",

    "7": "want",
    "79": "want to",

    "7B": "know",
    "7B9": "know that",

    "7BD": "need",

    "7B8G": "imagine",

    "8": "like",

    "R": "be",

    "R78": "remember",
    "R789": "remember that",

    "RBG": "care",
    "RBG9": "care about",

    "R7BD": "understand",

    "B8": "believe",
    
    "BG": "think",

    "G": "go",

    "G9": "get",

    "S": "say",

    "D": "do",
    
}

from pprint import pprint

verb_tenses = {}
import os
path = os.path.join(os.path.dirname(__file__), "verb.txt")
data = open(path).readlines()
for i in range(len(data)):
    a = data[i].strip().split(",")
    verb_tenses[a[0]] = a

for key, value in enders.items():
    s = value.split()
    tenses = verb_tenses[s[0]]
    enders[key] = {}
    for t in range(len(tenses)):
        tense = tenses[t]
        if tense:            
            if len(s) > 1:
                tense = ' '.join((tense, *s[1:]))
            enders[key][t] = tense

enders[""] = [""]*24

pprint(enders, compact=True, width=750)
