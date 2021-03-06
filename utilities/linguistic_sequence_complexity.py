#!/usr/bin/env python3

from copy import copy
from sys import float_info
import argparse
import somaticseq.sequencing_features as seq_features

eps = float_info.epsilon



def all_possible_dna_sequences(seq_length):

    seqs = ['G', 'C', 'T', 'A']
    
    for _ in range(seq_length-1):
        
        seqs_i = copy(seqs)
        seqs = []
        for sub_seq in seqs_i:
            
            for i in 'TCGA':
                extended_seq = sub_seq + i
                seqs.append( extended_seq )
    
    return set(seqs)



def max_vocab(seq_length):
    # According to:
    # https://doi.org/10.1093/bioinformatics/18.5.679
    counts = 0
    for k in range(1, seq_length+1):
        counts = counts + min(4**k, seq_length - k + 1)
    
    return counts




'''
def LSC(sequence, up_to_n=50, at_least_to_n=10):
    #Calculate the number of unique N-string within a sequence divided by min(4^i or N-i+1) as U(i).
    #Then, take the product of all the U(i)'s.
    
    seq_length    = len(sequence)
    up_to_n       = min(up_to_n, seq_length)
    at_least_to_n = min(at_least_to_n, seq_length)
    
    LSC = 1
    
    for i in range(1, seq_length+1):
        
        set_of_seq_n = set()
        tree_level = min(4**i, seq_length - i + 1)
        
        for n, nth_base in enumerate(sequence):
            
            if n+i <= len(sequence):
                sub_seq = sequence[n:n+i]
                set_of_seq_n.add( sub_seq )

        num_uniq_subseqs = len(set_of_seq_n)
        U_i = num_uniq_subseqs / tree_level
        
        if i > up_to_n:
            break
        elif (i >= at_least_to_n) and (1.0 - U_i <= eps):
            break
        else:
            LSC = LSC * U_i

    return LSC
'''


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Annotate with snpSift and snpEff with dbSNP and COSMIC", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-seq',  '--sequence', type=str,  help="input vcf file")
    args = parser.parse_args()

    print( seq_features.LC(args.sequence) )
