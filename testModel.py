import model
import criterion
from model import *
from criterion import *
import torch 
import torch.utils.data
from random import sample
import numpy as np
import itertools
import argparse

def get_unique():
    dict_data = open("dict.txt",'r').readlines()
    # dict_data_list = [dict_data.split() for j in dict_data]

    # unique = list(set(list(itertools.chain.from_iterable(dict_data_list))))
    unique = []
    tot = 153
    for u in range(tot):
        v = dict_data[u].split()[0]
        unique.append(v)

    return unique

##################################################
# print("Loading data and labels\n")

# #if(True):
# # data I/O
data_raw = open('train_data.txt', 'r').readlines() # should be simple plain text file
data_raw_test = open('test_data.txt', 'r').readlines() # should be simple plain text file
data_test = [j.split() for j in data_raw_test]


# ''' getting number of sentences'''
data = [i.split() for i in data_raw]

unique = list(set(list(itertools.chain.from_iterable(data_test)) + list(itertools.chain.from_iterable(data))))

print("no. of unique words: ",len(unique))

# label_raw = open('train_labels.txt', 'r').read().split()
# l = [len(i) for i in data]

# data_size, vocab_size = len(data), len(unique)
# labels = [int(label) for label in label_raw]
# ''' in case of one hot representation
# number of words in vocab will decide the dimension of the one hot vector '''

# unique = get_unique()

print(unique)
# print("no. of unique words: ",len(unique))

char_to_ix = { ch:i for i,ch in enumerate(unique) }
ix_to_char = { i:ch for i,ch in enumerate(unique) }
d=list(char_to_ix.keys())

def onehot(number):
	
    oh = np.zeros(len(unique))
    index = char_to_ix[number]
    oh[index]=1
    
    return oh

def in_to_onehot(input):
	l=[]
	for i in input:
	    l.append(onehot(i))
	return l
	
# zero_vector = np.zeros(len(unique))


in_test = [in_to_onehot(d_test) for d_test in data_test]

print("\nTesting started ..............\n")

# torch.save(model_0,'model2.bin')
model_0 = torch.load("model1.bin")

hidden_dim = 6


file = open('test_max_pred1.csv','w')
for i in range(len(data_raw_test)):
    
    input_vect = torch.tensor(in_test[i])
    hprev = torch.zeros(hidden_dim).double()

    output = model_0.forward_test(input_vect,hprev)
    print(output.shape)
    out = list(output.numpy()[0])
    predict = { val:inx for inx,val in enumerate(out) }
    predicted_label = predict[max(out)]
    file.write(str(predicted_label)+"\n")
    
file.close()




# if __name__== "__main__":
#         parser = argparse.ArgumentParser()
#         parser.add_argument("-modelName", help="input model path")
#         parser.add_argument("-data",help="path to test data")
#         # parser.add_argument("-target",help="path to training labels")

#         args = parser.parse_args()
        
#         print("==================input args===================")
#         print(args.modelName)
#         print(args.data)
#         # print(args.target)
