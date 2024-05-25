from slm import *
from glob import glob
import os
import platform
from slm_nn import *

OS = platform.platform()

def get_model(context_length):
    #tokenizer = WhitespaceTokenizer()
    #tokenizer = CharacterTokenizer()
    #tokenizer = SpaceTokenizer()
    #tokenizer = Gpt2Tokenizer()

    #base_predictor = FrequencyTablePredictor(context_length, bail_to_random=True)
    #embedder = Gpt2Embedder()
    #predictor = EmbeddingTablePredictor(embedder, context_length, predictor=base_predictor)
    
    model = NnLanguageModel("jampekka/4chan_r9k")

    return model

def generate(model, initial_context, end_token):
    #initial_context = tokens[:context_length]
    print(initial_context)
    generator = model.generate(initial_context)
    #next(generator)
    generated = []
    for token in generator:
        if len(generated) > 80:
            if token == model.tokenizer("\n")[0] or token == model.tokenizer(".")[0]:
                generated.append(token)
                return generated 
        if token == end_token:
            #print(model.tokenizer.decode(generated[len(initial_context)-1:]).strip())

            if model.tokenizer.decode(generated[len(initial_context)-1:]).strip():
                return generated
        generated.append(token)
    return generated

"""
def generate(model, initial_context, end_token):
    #initial_context = tokens[:context_length]
    generator = model.generate(initial_context)

    yield next(generator)

    for token in generator:
        if token == end_token:
            
            return
        yield token
"""

def get_possible_starts(freq_table, end_token):
    # ------- FOR DEMO -------
    possible_starts = []

    for k,v in freq_table.items():
        if k[0] == end_token:
            possible_starts.append(k)
        
    # -----------------------
    return possible_starts

def get_initial_context(possible_starts):
    return list(random.choice(possible_starts))

def clear_console():
    if "Linux" in OS or "macOS" in OS:
        os.system("clear")
    elif "Windows" in OS:
        os.system("cls")

def train_model(model):
    for file in glob("./out/res/*"):
        #print(file)

        text = open(file, encoding="utf-8", errors="ignore")
        txt = text.read()
        text.close()
        tokens = model.tokenizer(txt)
        model.train(tokens)
            