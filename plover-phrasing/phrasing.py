LONGEST_KEY = 2


# copied from the output of generate.py
enders = \
{'': ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
 '6': {0: 'have', 3: 'has', 5: 'having', 10: 'had', 11: 'had'},
 '68': {0: 'feel', 3: 'feels', 5: 'feeling', 10: 'felt', 11: 'felt'},
 '6G': {0: 'forget', 3: 'forgets', 5: 'forgetting', 10: 'forgot', 11: 'forgotten'},
 '7': {0: 'want', 3: 'wants', 5: 'wanting', 10: 'wanted', 11: 'wanted'},
 '79': {0: 'want to', 3: 'wants to', 5: 'wanting to', 10: 'wanted to', 11: 'wanted to'},
 '7B': {0: 'know', 3: 'knows', 5: 'knowing', 10: 'knew', 11: 'known'},
 '7B8G': {0: 'imagine', 3: 'imagines', 5: 'imagining', 10: 'imagined', 11: 'imagined'},
 '7B9': {0: 'know that', 3: 'knows that', 5: 'knowing that', 10: 'knew that', 11: 'known that'},
 '7BD': {0: 'need', 3: 'needs', 5: 'needing', 10: 'needed', 11: 'needed'},
 '8': {0: 'like', 3: 'likes', 5: 'liking', 10: 'liked', 11: 'liked'},
 'B8': {0: 'believe', 3: 'believes', 5: 'believing', 10: 'believed', 11: 'believed'},
 'BG': {0: 'think', 3: 'thinks', 5: 'thinking', 10: 'thought', 11: 'thought'},
 'D': {0: 'do', 3: 'does', 5: 'doing', 10: 'did', 11: 'done'},
 'G': {0: 'go', 3: 'goes', 5: 'going', 10: 'went', 11: 'gone'},
 'G9': {0: 'get', 3: 'gets', 5: 'getting', 10: 'got', 11: 'gotten'},
 'R': {0: 'be', 1: 'am', 2: 'are', 3: 'is', 4: 'are', 5: 'being', 6: 'was', 7: 'were', 8: 'was', 9: 'were', 10: 'were', 11: 'been', 13: 'am not', 14: "aren't", 15: "isn't", 16: "aren't", 18: "wasn't", 19: "weren't", 20: "wasn't", 21: "weren't", 22: "weren't"},
 'R78': {0: 'remember', 3: 'remembers', 5: 'remembering', 10: 'remembered', 11: 'remembered'},
 'R789': {0: 'remember that', 3: 'remembers that', 5: 'remembering that', 10: 'remembered that', 11: 'remembered that'},
 'R7BD': {0: 'understand', 3: 'understands', 5: 'understanding', 10: 'understood', 11: 'understood'},
 'RBG': {0: 'care', 3: 'cares', 5: 'caring', 10: 'cared', 11: 'cared'},
 'RBG9': {0: 'care about', 3: 'cares about', 5: 'caring about', 10: 'cared about', 11: 'cared about'},
 'S': {0: 'say', 3: 'says', 5: 'saying', 10: 'said', 11: 'said'}}


starters = {
    "#R": "I", "R": "I",
    "4R": "you",
    "3R": "he", "34R": "she", "24R": "it",
    "2R": "we",
    "23R": "they",
    "234R": "",

    "#WR": "what I", "WR": "what I",
    "W4R": "what you",
    "3WR": "what he", "3W4R": "what she", "2W4R": "what it",
    "2WR": "what we",
    "23WR": "what they",
}
persons = {
    "I": 1,
    "you": 2,
    "he": 3, "she": 3, "it": 3,
    "we": 4, "they": 4,
    "": 0
}


aux = {
    #   "0": "don't",   # these get handled separately - conjugation
    #   "E": "<past>",      "0E": "didn't",
    #  "5U": "",           "50U": "",
        "5": "can",         "50": "can't",
       "5E": "could",      "50E": "couldn't",
      "5EU": "should",    "50EU": "shouldn't",
        "U": "will",        "0U": "won't",
       "EU": "would",      "0EU": "wouldn't",
}


retros = ("-R8", "*R8", "#KR-GS")


def conj(v, offset):
    try:
        conjugated = v[offset]
    except KeyError:
        try:
            if   offset < 6   : conjugated = v[0]    # present
            elif offset < 12  : conjugated = v[10]   # past
            elif offset < 18  : conjugated = v[12]   # negative
            else              : conjugated = v[22]   # negative past
        except KeyError:
            return ""
    return conjugated


def lookup(key):
    assert len(key) <= LONGEST_KEY

    if len(key) > 1:
        if key[1] not in retros:
            raise KeyError

    stroke = key[0]

    # split the stroke into its three parts
    start = ""
    middle = ""
    end = ""
    current = 0
    valid = False
    for character in stroke:
        if not valid and (character == "#" or character.isdigit()): valid = True
        if character in "50*EU-":
            current = 1
            middle += character
        elif character not in "50*EU-" and current >= 1:
            current = 2
            end += character
        else:
            start += character

    if not valid: raise KeyError

    start = starters[start]
    person = persons[start.split()[-1]]

    final = [start]

    v = ""
    if middle == "0":           # don't/doesn't/aren't
        v = conj(enders[end], 12 + person)
        if not v:
            if person == 3: final.append("doesn't")
            else:           final.append("don't")
            final.append(enders[end][0])
        else:
            final.append(v)
    elif middle == "E":         # am/was
        final.append(conj(enders[end], 5 + person))
    elif middle == "0E":        # didn't/weren't
        v = conj(enders[end], 17 + person)
        if not v:
            final.append("didn't")
            final.append(enders[end][0])
        else:
            final.append(v)
    elif middle == "5U":        # are being/is being
        if start.endswith("I"):        final[0] += "'m"
        elif start.endswith("you"):    final[0] += "'re"
        elif start.endswith("he"):     final[0] += "'s"
        elif start.endswith("she"):    final[0] += "'s"
        elif start.endswith("it"):     final[0] += "'s"
        elif start.endswith("we"):     final[0] += "'re"
        elif start.endswith("they"):   final[0] += "'re"
        final.append(enders[end][5])
    elif middle == "50U":
        if start == "I": final[0] = "I'm not"
        else:
            final.append(conj(enders["R"], 12 + person))
        final.append(enders[end][5])
    elif middle == "-":         # am/is
        final.append(conj(enders[end], person))
    else:                       # aux + inf
        final.append(aux[middle])
        final.append(enders[end][0])


    # retro strokes
    if len(key) > 1:
        retro = key[1]
        if retro == "-R8":          # I don't really know
            final.insert(-1, "really")
        elif retro == "*R8":        # I really don't know
            final.insert(1, "really")
        elif retro == "#KR-GS":     # I don't know/I do not know
            f = " ".join(list(filter(None, final))).strip()
            f = f.replace("won't", "will not")
            f = f.replace("n't", " not")
            return f

    return " ".join(list(filter(None, final))).strip()
