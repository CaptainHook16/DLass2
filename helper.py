import numpy as np
from itertools import izip

#this file contains helper functions to deal with the training set and the test set

#let's define some global list:
Representation_Of_Words_By_Indexes = {}

#more to define:
UNK = "UNKNOWN_WORD"
WINDOW_START = "START"
WINDOW_END = "END"

def divide_word_sequence_into_windows(word_sequence):
    """

    :param word_sequence:
    :return: return an array of windows when each window contain 5 words (as requiredin the assigment)
    """



def convert_word_to_index(word_to_convert):
    """
    The first step in using an embedding layer is to encode this sentence by indices.
     In this case we assign an index to each unique word

    :param word_to_convert:
    :return: return the index which represent the word.
    """

    if word_to_convert not in Representation_Of_Words_By_Indexes:
        #if the word is not in the list its index is UNK - Unknown
        #words we have not seen in the training action we'll map them to the same vector in
        #the embedding matrix - unk
        return Representation_Of_Words_By_Indexes[UNK]
    else:
        #if the word is in the list, return its index
        return Representation_Of_Words_By_Indexes[word_to_convert]

