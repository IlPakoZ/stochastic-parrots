from slm import *
from glob import glob


context_length = 3

def get_model(context_length):
    #tokenizer = WhitespaceTokenizer()
    #tokenizer = CharacterTokenizer()
    #tokenizer = SpaceTokenizer()
    tokenizer = Gpt2Tokenizer()

    embedder = NullEmbedder()
    predictor = FrequencyTablePredictor(context_length)

    model = LanguageModel(
        tokenizer=tokenizer,
        embedder=embedder,
        predictor=predictor
    )

    return model

# Usage starts here


model = get_model(context_length)
end_token = model.tokenizer("\2")[0]
print(end_token)

for file in glob("./r9k/res/*"):
    text = open(file)
    text = text.read()
    tokens = model.tokenizer(text)
    model.train(tokens)


initial_context = tokens[:context_length]
generated_tokens = model.generate(initial_context)


generated_text = model.tokenizer.decode(generated_tokens)
print(generated_text)


