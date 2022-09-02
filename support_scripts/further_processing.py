import pickle
from pickle import load, dump
from collections import Counter

def load_cleaned_data(file):
    '''
        To open the pickled object and return
    '''
    return load(open(file, 'rb'))

def save_processed_data(data, file):
    '''
        Saving the data in pickled format.
    '''
    dump(data, open(file, 'wb'))
    print("Data is saved to disk!")
    return

def get_vocabulary(tokenized_sentences):
    '''
        Get the vocabulary of the sentences along with the token frequencies.
    '''
    vocabulary = Counter()
    for sentence in tokenized_sentences:
        vocabulary.update(sentence)
    return vocabulary


def trim_vocabulary(vocabulary, min_occurance=5):
    '''
        To filter out tokens which have less occurances than 
        a given value.
    '''
    trimmed_vocab = [token for token, count in vocabulary.items() if count>=min_occurance]
    return set(trimmed_vocab)

def update_dataset(data, vocab):
    '''
        Will remove the tokens in data which are not available in 
        the vocabulary with "unk" token.
    '''
    updated_data = []

    for sentence in data:
        temp_line = []
        for token in sentence:
            if(token not in vocab):
                temp_line.append('unk')
            else:
                temp_line.append(token)
        updated_data.append(" ".join(temp_line))
    
    return updated_data
