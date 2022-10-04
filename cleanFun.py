import nltk
import re

import pkg_resources
from nltk.tokenize import TweetTokenizer
from nltk.corpus import words
from symspellpy import SymSpell

nltk.download("stopwords")
nltk.download('omw-1.4')
nltk.download('wordnet')
nltk.download('words')
corrected_words = words.words()
took = TweetTokenizer()
stopwords = nltk.corpus.stopwords.words('english')
wn = nltk.WordNetLemmatizer()


def lower_converter(lines):  # questa funzione converte le lettere maiuscole in minuscole
    return lines.lower()


def break_remover(lines):  # questa funzione rimuove gli invii
    lines = re.sub("<br>", " ", lines)
    return lines


def punt_remover(lines):  # questa funzione rimuove la punteggiatura dal dataset
    lines = re.sub("[^A-Za-z ]", " ", lines)
    return lines


def href_remover(lines):  # questa funzione rimuove i link
    lines = re.sub("href*\w+", " ", lines)
    return lines


def http_remover(lines):  # questa funzione rimuove i link
    lines = re.sub("http*\w+", " ", lines)
    return lines


def spaces_remover(lines):  # questa funzione rimuove spazi consecutivi > 1 dal dataset
    lines = re.sub("\s+", " ", lines)
    return lines


def reduce_lengthening(text):
    pattern = re.compile(r"(.)\1{2,}")
    return pattern.sub(r"\1\1", text)


def correct_words(text):
    line = took.tokenize(text)
    for i in range(len(line)):
        # print("accorciando", line[i])
        line[i] = reduce_lengthening(line[i])
        # print("accorciata", line[i])

    return " ".join(line)


def word_correction(text):
    line = took.tokenize(text)
    for i in range(len(line)):
        # print("correggendo", line[i])
        sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
        dictionary_path = pkg_resources.resource_filename(
            "symspellpy", "frequency_dictionary_en_82_765.txt"
        )
        sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)
        suggestions = sym_spell.lookup_compound(line[i], max_edit_distance=2, ignore_non_words=True)
        line[i] = suggestions[0].term  # Prendiamo la prima/e che troviamo tra quelle con distanza minima
        # print("corretta", line[i])
    print(line)
    return " ".join(line)


def stopwords_remover(x):  # funzione per la rimozione delle stopwords
    x = took.tokenize(x)
    post = [i for i in x if i not in stopwords]
    return " ".join(post)


def lemmatizer(x):  # funzione per la lemmatizzazione delle parole
    x = took.tokenize(x)
    w = [wn.lemmatize(i) for i in x]

    return " ".join(w)

