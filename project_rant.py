from slm import *
from glob import glob
import os
import platform
from slm_sparse import *

context_length = 3
OS = platform.platform()

def get_model(context_length):
    #tokenizer = WhitespaceTokenizer()
    #tokenizer = CharacterTokenizer()
    #tokenizer = SpaceTokenizer()
    tokenizer = Gpt2Tokenizer()
    embedder = Gpt2Embedder()

    predictor = EmbeddingTablePredictor(embedder, context_length)
    #predictor = FrequencyTablePredictor(context_length, len(tokenizer.tokenizer))

    model = LanguageModel(
        tokenizer=tokenizer,
        predictor=predictor
    )

    return model

def generate(model, initial_context, end_token):
    #initial_context = tokens[:context_length]
    generator = model.generate(initial_context)
    next(generator)
    generated = []
    for token in generator:
        if token == end_token:
            print(model.tokenizer.decode(generated[len(initial_context)-1:]).strip())

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
    for file in glob("./r9k/res/7296*"):
        text = open(file)
        text = text.read()
        tokens = model.tokenizer(text)
        model.train(tokens)