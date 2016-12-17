import numpy as np
import re

# load a corpus
import requests
target_url = 'http://www.gutenberg.org/cache/epub/1260/pg1260.txt'
text = requests.get(target_url).text


def preprocess(text):
    """
    Given a text, returns a list consisting solely of the word
    tokens contained therein. Feel free to write helper
    functions for removing formatting and punctuation, converting
    word case, creating equivalence classes, etc.

    Parameters
    ----------
    text: string
        A string containing the raw text of your corpus

    Returns
    -------
    cleaned_text: list of strings
        a list of the words in your corpus presented in the same
        order as they appear in text
    """
    a = re.findall("[^\W_]+", text)
    for x in range(len(a)):
        a[x] = a[x].lower()
    return a


def calc_ngram_probs(cleaned_text, n=3):
    """
    Calculates the log probability of each unique n-word sequence
    within a text.

    Parameters
    ----------
    cleaned_text: string
        A list of the words in your corpus presented in the same
        order as they appear in text

    n: int
        The gram-size for your model (i.e., the number of words in
        your n-gram sequences).

    Returns
    -------
    ngram_probs: dict
        A dictionary of key,value pairs where the keys correspond
        to unique n-gram word sequences and the values correspond
        to the log probability of the sequence occurring within
        your corpus
    """

    grams = [cleaned_text[i:i + n] for i in range(len(cleaned_text) - n + 1)]
    len_grams = len(grams)

    count = {}

    for i in range(len(grams)):
        tup = tuple(grams[i])
        if tup not in count:
            count[tup] = 1
        else:
            count[tup] += 1

    for key, value in count.items():
        count[key] = np.log(value / len_grams)

    return count


def generate(ngram_probs, seed):
    """
    Completes a sentence using the probabilities using your ngram model.

    Parameters
    ----------
    ngram_probs: dict
        A dictionary of key,value pairs where keys correspond
        to n-gram word sequences and values correspond to the
        log probability of the sequence occurring within your
        corpus

    seed: list
        A list containing the first n words of a sentence.

    Returns
    -------
    sentence: list
        A list of length >= n+1 word tokens constituting a sentence. The
        n+1st to the last word should be generated using the probabilities
        of your ngram model.
    """
    list_g = []
    for x in range(1, n):
        for key, value in ngram_probs.items():
            if seed[-x:] == list(key[0:x]):
                list_g.append((seed[-x:], key, value))

    if not list_g:
        return seed
    else:
        current_max = list_g[0][2]
        for x in list_g:
            if current_max <= x[2]:
                to_r = x

        to_add = to_r[1][len(to_r[0]):]
        for x in to_add:
            seed.append(x)
        return seed


def log_sentence_prob(ngram_probs, sentence):
    """
    Returns the log probability of a sentence using the probabilites
    of your n-gram model. You may assume that the probability of generating
    the first n-1 words (i.e., the seed words) is 1.

    Parameters
    ----------
    ngram_probs: dict
        A dictionary of key,value pairs where keys correspond
        to n-gram word sequences and values correspond to the
        log probability of the sequence occurring within your
        corpus

    sentence: list
        A list of word tokens constituting a single sentence

    Returns
    -------
    prob: float
        The log probability of generating the words in sentence
        according to your n-gram model.
    """
    prob = 1
    n_len = len(ngram_probs.popitem()[0])
    n_parts_of_s = [sentence[x:x + n_len] for x in range(len(sentence) - n_len + 1)]
    for g in n_parts_of_s:
        if tuple(g) in ngram_probs:
            print(g)
            prob = prob * ngram_probs[tuple(g)]
    return prob






# Test the model for n=3 (tri-grams)

n = 4
seed = ["one", "morning", "she", "told"]

cleaned_text = preprocess(text)
ngram_probs = calc_ngram_probs(cleaned_text, n)
sentence = generate(ngram_probs, seed)
log_prob = log_sentence_prob(ngram_probs, sentence)

print('Sentence: {}'.format(sentence))
print('log P(Sentence): {}'.format(log_prob))