import numpy as np

global_aminoacids_list = [
    'A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y'
    ]

def get_index(aminoacid):
    for i in range(len(global_aminoacids_list)):
        if global_aminoacids_list[i] == aminoacid:
            return i

def aminoacids_frequencies(sequence):
    frequencies = [0 for el in global_aminoacids_list]
    for aa in sequence:
        frequencies[get_index(aa)] += 1
    frequencies = [el/len(sequence) for el in frequencies]
    return np.array(frequencies)
    
