import torch
from torch.utils.data import Dataset, DataLoader
from torch.utils.data.sampler import SubsetRandomSampler
from torchvision import datasets, transforms
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
import utils1 as ut1

import sys


#let's define our parameters:
learning_rate = 0.01
window_size = 5 #2 neighbors + target word
hidden_l_size = 100
tags_number = 10
input_layer_size = 250 #window x vector_size = 5 x 50 =250
epochs_number = 3
vector_embedding = 50
batch_normalization_size = 1024

def get_data_and_labales(train_file):
    """
    this function create a dataset for the train

    :param train_file:
    :return:train data
    """


def Start_Action(argument):
    """

    :param argument:
    :return: none
    """
    #ner or pos (user input)
    mapping_type = argument[0]

    train_set = 0

if __name__ == "__main__":
    Start_Action(sys.argv[1:])

