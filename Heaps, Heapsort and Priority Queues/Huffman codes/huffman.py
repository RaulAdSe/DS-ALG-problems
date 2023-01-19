#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 10:13:51 2022

@author: alumne
"""

# The construction of a Huffman coding is relatively simple: Repeatedly, choose the two less frequent symbols, 
# arbitrarily assign a bit (0 or 1) to each one to make them different, and
# consider them both a unique symbol from now on. Stop when only one symbol remains.

from easyinput import read, read_line
from heapq import heapify, heappop, heappush


def huffman_average_bits(n):
    pq=[]
    for i in range(n):
        freq = read(float)
        heappush(pq, freq)
    average = 0
    
    while(len(pq)>1):   # Pararé quan quedi un element
        a = pq[0]
        heappop(pq)
        b = pq[0]
        heappop(pq)
        average += (a+b)/100    # Vaig calculant average respecte els trec menys frequents
        heappush(pq, a+b)
        
    return average
        
    

if __name__ == '__main__':
    n = read(int)
    print('expected number of bits per letter: ' + str("{0:.4f}".format(huffman_average_bits(n))))



