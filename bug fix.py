from data_processing import *
from Expanded_SPAAN_Model import *

from Bio import SeqIO
import numpy as np
import tensorflow

# load the datasets (it requires about 1 minute)
x, y = process(list(SeqIO.parse("./data/original_adh_dataset.fasta", "fasta")), list(SeqIO.parse("./data/original_negative_dataset.fasta", "fasta")))
x_train, y_train, x_val, y_val, x_test, y_test = split_ds(np.array(x), np.array(y), np.random.permutation(len(x)))
