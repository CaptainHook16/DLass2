import numpy as np
from itertools import izip

#this file contains helper functions to deal with the training set and the test set

#let's define some global list:
Representation_Of_Words_By_Indexes = {}
Representation_Of_classes_By_Indexes ={}
#define set let us assign an index to each unique word - avoid giving the same word many indexes
Dictionary_of_words = set()

#more to define:
UNK = "UNKNOWN_WORD"
WINDOW_START = "START"
WINDOW_END = "END"

def divide_word_sequence_into_windows(word_sequences):
    """
    for test set which not has the class for each word
    :param word_sequences:
    :return: return an array of windows when each window contain 5 words (as requiredin the assigment)
    """

    windows_array = []
    for sequence in word_sequences:
        words = []
        #adds start*2, end*2 for each sentence for appropriate windows
        words.append(WINDOW_START)
        words.append(WINDOW_START)
        words.extend(sequence)
        words.append(WINDOW_END)
        words.append(WINDOW_END)

        for index, (cure_word) in enumerate(words):
            if cure_word!=WINDOW_END and cure_word!=WINDOW_START:
                new_window = []
                new_window.append(convert_word_to_index(words[index-2]))
                new_window.append(convert_word_to_index(words[index - 1]))
                new_window.append(convert_word_to_index(cure_word))
                new_window.append(convert_word_to_index(words[index + 1]))
                new_window.append(convert_word_to_index(words[index + 2]))
                windows_array.append(new_window)
    return windows_array

def divide_word_class_sequence_into_windows(word_sequences):
    """
    for test set which not has the class for each word
    :param word_sequences:
    :return: return an array of windows when each window contain 5 words (as requiredin the assigment)
    """

    windows_array = []
    classes = []
    for sequence in word_sequences:
        words_classes_matrix =[]
        words_classes_matrix.extend([(WINDOW_START, WINDOW_START), (WINDOW_START, WINDOW_START)])
        words_classes_matrix.extend(sequence)
        words_classes_matrix.extend([(WINDOW_END, WINDOW_END) , (WINDOW_END, WINDOW_END)])
        #adds start*2, end*2 for each sentence for appropriate windows


        for index, (cure_word,match_class) in enumerate(words_classes_matrix):
            if cure_word!=WINDOW_END and cure_word!=WINDOW_START:
                new_window = []
                new_window.append(convert_word_to_index(words_classes_matrix[index-2][0]))
                new_window.append(convert_word_to_index(words_classes_matrix[index - 1][0]))
                new_window.append(convert_word_to_index(cure_word))
                new_window.append(convert_word_to_index(words_classes_matrix[index + 1][0]))
                new_window.append(convert_word_to_index(words_classes_matrix[index + 2][0]))
                #asign indexes to lists
                classes.append(Representation_Of_classes_By_Indexes[match_class])
                windows_array.append(new_window)
    return windows_array, classes







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

