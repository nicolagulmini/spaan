from data_processing import *
from Expanded_SPAAN_Model import *

from Bio import SeqIO
import numpy as np
import tensorflow

x, y = [], []
for protein in list(SeqIO.parse("./data/nan.fasta", "fasta")):
    tmp = [
                aminoacids_frequencies(protein.seq),
                multiplet_frequencies(protein.seq, 3),
                multiplet_frequencies(protein.seq, 4),
                multiplet_frequencies(protein.seq, 5),
                dipeptide_frequencies(protein.seq),
                charge_composition(protein.seq),
                hydrophobic_composition(protein.seq)
    ]
    cond = 1
    for el in tmp:
        if isinstance(el, int):
            cond = 0
    if cond == 1:
        for el in tmp:
            for entry in el:
                if (entry == float("inf") or entry == float("-inf")):
                    cond = 0
                    break
    if cond == 1:
        x.append(tmp)
        y.append(1)
    break
print(x)