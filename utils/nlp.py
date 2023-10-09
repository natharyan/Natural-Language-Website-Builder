import nltk
from nltk.tokenize import RegexpTokenizer
from nltk import pos_tag
import sys
sys.path.append('utils/')
from sections import sections
from keymap import subsections_dict

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


def nlp(key):
    print('nlp')
    text = key

    #tokenize with single quotes
    def tokenize_with_phrase(text,phrase):
        tokenizer = RegexpTokenizer(phrase)
        tokens = tokenizer.tokenize(text)
        tagged_tokens = pos_tag(tokens)
        for i,(token,_) in enumerate(tagged_tokens):
            if token[0].startswith("'") and token[0].endswith("'"):
                tagged_tokens[i] = (token,'SingleQuoteCmd')
        return tagged_tokens
    phrase = r"'[^']*'|\S+"
    tokens = tokenize_with_phrase(text,phrase)
    print(tokens)

    # NN tag tokens
    nn_tokens = list(filter(lambda token: (token[1] in ['NN',"SingleQuoteCmd"]) and token[0]!='content', tokens))
    print(nn_tokens)

    # NN token values
    nn_tokens_token = list(map(lambda token: token[0],nn_tokens))
    print(nn_tokens_token)

    def rich_content(text,filter):
        for i,candidate in enumerate(text):
            if candidate in filter and i+1<len(text):
                content = text[i+1]
        return content
    
    # get usable keys
    richContent_dict = {}
    for i in subsections_dict:
        # true if any items from subsections_dict[i] exist in nn_tokens
        if any(item in subsections_dict[i] for item in nn_tokens_token):
            richContent_dict[i] = rich_content(nn_tokens_token,subsections_dict[i])
    return richContent_dict