import re
import string
import unicodedata


def load_data(file_name):
    '''
        To read the raw data from the source file.
        Do not read larger than memory files.
    '''
    file = open(file_name, mode='rt', encoding='utf-8')
    data = file.read()
    file.close()
    return data


def get_sentence_list(raw_text):
    '''
        Assume every new line is a sentence. Which is a stupid assumption. 
        But works in my case.
    '''
    return raw_text.strip().split('\n')


def get_sentence_size_range(sentences):

    token_sizes = [len(sentence.split()) for sentence in sentences]
    return min(token_sizes), max(token_sizes)


def clean_sentences(sentences):

    cleaned_sentences = []

    regex_template = re.compile(f'[^{re.escape(string.printable)}]')
    lookup_table = str.maketrans('', '', string.punctuation)

    for sentence in sentences:
        
        # These functions are very specific. So better look at the documentations.
        sentence = unicodedata.normalize('NFD', sentence).encode('ascii', 'ignore')

        # Converting back to unicode
        sentence = sentence.decode("UTF-8")

        # Get tokens
        sentence = sentence.split()

        # Lowercasing the tokens
        sentence = [token.lower() for token in sentence]

        # Remove all punctuations from tokens
        sentence = [token.translate(lookup_table) for token in sentence]

        # Replace all the non printable characters from tokens
        sentence = [regex_template.sub('', token) for token in sentence]

        # Remove tokens which contain non alphabetical characters
        sentence = [token for token in sentence if token.isalpha()]

        cleaned_sentences.append(sentence)

    return cleaned_sentences
