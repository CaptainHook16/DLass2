STUDENT={'name': 'Coral Malachi_Daniel Braunstein',
         'ID': '314882853_312510167'}

import numpy as np

# this file contains helper functions to deal with the training set and the test set
from itertools import izip

# more to define:

WINDOW_START = '*START*'
WINDOW_END = '*END*'

UNK = "UUUNKKK"
NEW_LINE = "\n"
TAB = "\t"

# let's define some global list:
Representation_Of_Indexes_By_Words = {}
Representation_Of_Words_By_Indexes = {}
Representation_Of_classes_By_Indexes = {}
Representation_Of_Indexes_By_classes = {}
# define set let us assign an index to each unique word - avoid giving the same word many indexes
Dictionary_of_classes = set()
Dictionary_of_words = []



def get_word_embeddings_dict_from_file(words_file, vector_file):
    """
    get_word_embeddings_dict_from_file function.
    reads the words and word embeddings vectors and fills word_embeddings_dict
    :param words_file: name of the file containing the words
    :param vector_file: name of the file containing the vectors of the words
    from the words_file
    :return: word embeddings dictionary
    """
    word_embeddings_dict = {}
    for word, vector_line in izip(open(words_file), open(vector_file)):
        word = word.strip("\n").strip()
        vector_line = vector_line.strip("\n").strip().split(" ")
        word_embeddings_dict[word] = np.asanyarray(map(float,vector_line))
        Dictionary_of_words.append(word)
    return word_embeddings_dict

def get_word_embeddings_matrix():
    return np.loadtxt("wordVectors.txt")




def add_class_and_word_to_dics(m_class, word):
    global Dictionary_of_words
    global Dictionary_of_classes
    Dictionary_of_classes.add(m_class)
    Dictionary_of_words.add(word)


def read_train_data(data_train):
    global Dictionary_of_words
    global Dictionary_of_classes
    tagged_sentences = []
    with open(data_train) as reading:
        # call readlines function
        m_lines = reading.readlines()
        sentence_and_tags = []
        for line in m_lines:
            if NEW_LINE == line:
                tagged_sentences.append(sentence_and_tags)
                # clean buffer
                sentence_and_tags = []
                # continue yo next iteration of the loop
                continue
            line = clean_line(line)
            word, tag = line.split()
            #add_class_and_word_to_dics(tag, word)
            Dictionary_of_classes.add(tag)
            sentence_and_tags.append((word.lower(), tag))
    Dictionary_of_classes.add(UNK)
    #Dictionary_of_words.add(UNK)
    return tagged_sentences


###############################################################
# Function Name:divide_word_class_sequence_into_windows
# Function input:word_sequences
# Function output:none
# Function Action:return an array of windows when each window contain 5 words (as requiredin the assigment)
#
################################################################
def divide_word_class_sequence_into_windows(word_sequences):

    windows_array = []
    classes = []
    for sentence in word_sequences:
        words_classes_matrix = []
        # words_classes_matrix = [(WINDOW_START, WINDOW_START), (WINDOW_START, WINDOW_START)]
        words_classes_matrix.extend([(WINDOW_START, WINDOW_START), (WINDOW_START, WINDOW_START)])
        words_classes_matrix.extend(sentence)
        words_classes_matrix.extend([(WINDOW_END, WINDOW_END), (WINDOW_END, WINDOW_END)])
        for i, (cure_word, tag) in enumerate(words_classes_matrix):
            if cure_word != WINDOW_START and cure_word != WINDOW_END:
                new_window = []
                new_window.append(convert_word_to_index(words_classes_matrix[i - 2][0]))
                new_window.append(convert_word_to_index(words_classes_matrix[i - 1][0]))
                new_window.append(convert_word_to_index(cure_word))
                new_window.append(convert_word_to_index(words_classes_matrix[i + 1][0]))
                new_window.append(convert_word_to_index(words_classes_matrix[i - 2][0]))

                windows_array.append(new_window)
                classes.append(Representation_Of_classes_By_Indexes[tag])
    return windows_array, classes



def clean_line(line):
    return line.strip(NEW_LINE).strip().strip(TAB)


def read_dev_data(dev_file):
    global Dictionary_of_words
    global Dictionary_of_classes
    m_seqs = []
    with open(dev_file) as reading:
        m_lines = reading.readlines()
        sequence = []
        for line in m_lines:
            if NEW_LINE == line:
                m_seqs.append(sequence)
                # clean buffer
                sequence = []
                # continue yo next iteration of the loop
                continue
            line = clean_line(line)
            word, tag = line.split()
            sequence.append((word.lower(), tag))
    # add unkown word to both dicts
    return m_seqs


###############################################################
# Function Name:updating_dictionaries_set
# Function input:none
# Function output:none
# Function Action:update all the dcts we created above
#
################################################################

def updating_dictionaries_set():
    global Representation_Of_Words_By_Indexes
    global Representation_Of_Indexes_By_Words
    global Representation_Of_classes_By_Indexes
    global Representation_Of_Indexes_By_classes
    global Dictionary_of_words
    print("here2")
    print(len(Dictionary_of_words))
    #Dictionary_of_words.update(set([WINDOW_START, WINDOW_END]))
    print("after2")
    print(len(Dictionary_of_words))
    Representation_Of_Words_By_Indexes = {
        m_word: m_index for m_index, m_word in enumerate(Dictionary_of_words)
    }
    Representation_Of_Indexes_By_Words = {
        m_index: m_word for m_word, m_index in Representation_Of_Words_By_Indexes.iteritems()
    }
    Representation_Of_classes_By_Indexes = {
        m_class: m_index for m_index, m_class in enumerate(Dictionary_of_classes)
    }
    Representation_Of_Indexes_By_classes = {
        m_index: m_class for m_class, m_index in Representation_Of_classes_By_Indexes.iteritems()
    }




###############################################################
# Function Name:divide_word_sequence_into_windows
# Function input:word_sequences
# Function output:return an array of windows when each window contain 5 words (as requiredin the assigment)
# Function Action:for test set which not has the class for each word
#
################################################################

def divide_word_sequence_into_windows(word_sequences):

    windows_array = []
    for sequence in word_sequences:
        # words = [WINDOW_START,WINDOW_START]
        # words.extend(sentence)
        # words.extend([WINDOW_END,WINDOW_END])
        words = []
        # adds start*2, end*2 for each sentence for appropriate windows
        words.append(WINDOW_START)
        words.append(WINDOW_START)
        words.extend(sequence)
        words.append(WINDOW_END)
        words.append(WINDOW_END)
        for index, (cure_word) in enumerate(words):
            if cure_word != WINDOW_START and cure_word != WINDOW_END:
                new_window = []
                new_window.append(convert_word_to_index(words[index - 2]))
                new_window.append(convert_word_to_index(words[index - 1]))
                new_window.append(convert_word_to_index(cure_word))
                new_window.append(convert_word_to_index(words[index + 1]))
                new_window.append(convert_word_to_index(words[index - 2]))

                windows_array.append(new_window)
    return windows_array



###############################################################
# Function Name:convert_word_to_index
# Function input:word_to_convert
# Function output:index
# Function Action:dwon explain
#
################################################################

def convert_word_to_index(word_to_convert):

    if word_to_convert not in Representation_Of_Words_By_Indexes:
        # if the word is not in the list its index is UNK - Unknown
        # words we have not seen in the training action we'll map them to the same vector in
        # the embedding matrix - unk
        return Representation_Of_Words_By_Indexes[UNK]
    else:
        # if the word is in the list, return its index
        return Representation_Of_Words_By_Indexes[word_to_convert]



###############################################################
# Function Name:get_dev_data
# Function input:dev_file
# Function output:none
# Function Action:the function return the dev data
#
################################################################


def get_dev_data(file_name):
    # We use global keyword to read and write a global variable inside a function.
    global Dictionary_of_words
    global Dictionary_of_classes
    word_sequences = read_dev_data(file_name)
    # call the divide_word_class_sequence_into_windows
    sequence, m_class = divide_word_class_sequence_into_windows(word_sequences)
    return sequence, m_class



###############################################################
# Function Name:reading_test_dataset
# Function input:dataset_to_read
# Function output:test data
# Function Action:the function return the test data
#
################################################################


def reading_test_dataset(dataset_to_read):
    # define an empty array to return
    word_sequences = []

    with open(dataset_to_read) as dataset:
        m_lines = dataset.readlines()
        sequence = []
        for cure_line in m_lines:
            if NEW_LINE == cure_line:
                word_sequences.append(sequence)
                # clean buffer
                sequence = []
                # continue yo next iteration of the loop
                continue
            word_in_sequence = cure_line.strip(NEW_LINE).strip()
            sequence.append(word_in_sequence.lower())
    return word_sequences


###############################################################
# Function Name:dictionary_embed
# Function input:m_words m_vec
# Function output:none
# Function Action:
#
################################################################

def dictionary_embed(m_words, m_vec):

    dict_embed = {}
    #use for loop
    for m_word, m_vec in izip(open(m_words), open(m_vec)):
        m_word = m_word.strip("\n").strip()
        m_vec = m_vec.strip("\n").strip().split(" ")
        #assign to dictionary
        dict_embed[m_word] = np.asanyarray(map(float,m_vec))
    return dict_embed

###############################################################
# Function Name:get_train_data
# Function input:m_dataset
# Function output:return the train data
# Function Action:the function return the train data
#
################################################################

def get_train_data(file_name):
    global Dictionary_of_words
    global Dictionary_of_classes
    # call read_train_data
    train_data = read_train_data(file_name)
    # call updating_dictionaries_set function
    updating_dictionaries_set()
    # call divide_word_class_sequence_into_windows functin
    windows_array, classes = divide_word_class_sequence_into_windows(train_data)
    return windows_array, classes


###############################################################
# Function Name:bring_test_data
# Function input:
# Function output:none
# Function Action:
#
################################################################

def bring_test_data(test_data_set):
    word_sequences = reading_test_dataset(test_data_set)
    return divide_word_sequence_into_windows(word_sequences)



WORD_EMBEDDINGS_DICT = get_word_embeddings_dict_from_file('vocab.txt', 'wordVectors.txt')
E = get_word_embeddings_matrix()