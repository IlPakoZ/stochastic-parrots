from pprint import pprint
from collections import defaultdict
from simple_lm import *
import re
import random
import os
from transformers import AutoTokenizer
import platform

tokenizer = AutoTokenizer.from_pretrained("gpt2")

OS = platform.platform()
context_length = 4
dir = "r9k/res/"


def load_dataset():
    freq_table = defaultdict(list)

    for filename in os.listdir(dir):
        if not os.path.isfile(dir+filename):
            continue
        
        f = open(dir+filename, "r", encoding="utf-8")
        body = f.read()
        body = "\n".join(s.strip() for s in body.split('\n'))
        tokens = tokenizer(body)["input_ids"]
        freq_table = get_next_token_table(tokens, context_length, freq_table)
    return freq_table

freq_table = load_dataset()
initial_context = ["How", "are", "you?"]

# Filter comments of length < context_length

to_del = [] 
for k in freq_table.keys():    
    if k[:4] == (27, 23893, 29, 198):
        for i in range(4, len(k)):
            if k[i:i+4] == (27, 23893, 29, 198):
                to_del.append(k)

for k in to_del:
    del freq_table[k]
    print(f"Deleted {k}!")


if "Linux" in OS or "macOS" in OS:
    os.system("clear")
elif "Windows" in OS:
   os.system("cls")

# ------- FOR DEMO -------
possible_starts = []

for k,v in freq_table.items():
    if k[:4] == (27, 23893, 29, 198):
        possible_starts.append(k)
    
# -----------------------

random.seed(1933)
while(True):
    initial_context = list(random.choice(possible_starts))
    generator = generate_tokens(freq_table, initial_context[-context_length:])
    tokens = list(generator)[4:-3]
    text = tokenizer.decode(tokens)
    print(text)
    a = input()
    
    if a == "q":
        break
    