# python
import numpy as np
import matplotlib.pyplot as plt

one_hot_dict = {'A': 0, 'T': 1, 'C': 2, 'G': 3}

dna_sequence = input("sequence please")

DNA_array = np.zeros((len(dna_sequence),4))
for i,base in enumerate(dna_sequence):
    dna_one_hot = one_hot_dict[base]
    DNA_array[i,dna_one_hot] = 1 
print(DNA_array)


#for position in sequence, column = position
#  for base in sequence, dictionary {}