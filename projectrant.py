import json
from pprint import pprint
from collections import defaultdict
from simple_lm import *
import re
import random
import pandas as pd
import os

context_length = 3
tokenizer = WhitespaceTokenizer()
dir = "../r9k/res/"

#table = pd.read_csv("outputgreaterthan.csv")
#table.to_json("output.json", orient="index")
#file = open("output.json", "r")
#data = json.load(file)

    

# ------- Preprocessing here ----------

# -------------------------------------
def load_dataset():
    freq_table = defaultdict(list)

    rants = []
    for filename in os.listdir(dir):
        if not os.path.isfile(dir+filename):
            continue
        
        f = open(dir+filename, "r", encoding="utf-8")
        body = f.read()
        body = "\n".join(s.strip() for s in body.split('\n'))
        tokens = tokenizer.tokenize(body)
        freq_table = get_next_token_table(tokens, context_length, freq_table)

    return freq_table
"""
for _, d in data.items():
    body = d['body']

    body = "\n".join(s.strip() for s in body.split('\n'))
    d['tokens'] = tokens = tokenizer.tokenize(body)
    freq_table = get_next_token_table(tokens, context_length, freq_table)
    rants.append(d)
"""
freq_table = load_dataset()


initial_context = ["How", "are", "you?"]
generator = generate_tokens(freq_table, initial_context[-context_length:])
text = tokenizer.untokenize(generator)
print(text)
"""
for i in range(20):
    print("--------- START RANT ---------\n")

    #start = random.choice(bodies)
    initial_context = start['tokens'][:context_length]
    print(initial_context)
    
    #generator = generate_tokens(freq_table, initial_context)
    #text = tokenizer.untokenize(generator)
    #print(text)

    print("\n--------- END ---------\n")
    """
"""

    for t in bodies:
        if text == t["body"]:
            print("Duplicate!")
    """

"""
for k in "Country Year Artist Song".split():
    print(f"{k}: {start[k]}")
print()
"""