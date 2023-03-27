#!/usr/bin/env python

# This script counts and derives the percentage of each nucleotide in an input DNA sequence

import sys

# Check for invalid input
if len(sys.argv) == 1:
    print("Please enter a DNA sequence as an argument")
    sys.exit(1)

# Get the sequence from the command line argument and convert to uppercase
seq = sys.argv[1].upper()

# Check if the sequence is a valid DNA sequence
if set(seq) - set('ACGT'):
    print("Invalid DNA sequence entered")
    sys.exit(1)

# Initialize counters for each nucleotide and total sequence length
a_count = 0
c_count = 0
g_count = 0
t_count = 0
seq_length = len(seq)

# Iterate through the sequence and count each nucleotide
for nucleotide in seq:
    if nucleotide == 'A':
        a_count += 1
    elif nucleotide == 'C':
        c_count += 1
    elif nucleotide == 'G':
        g_count += 1
    elif nucleotide == 'T':
        t_count += 1

# Calculate the percentage of each nucleotide
a_percent = a_count / seq_length * 100
c_percent = c_count / seq_length * 100
g_percent = g_count / seq_length * 100
t_percent = t_count / seq_length * 100

# Print the results
print(f"Sequence: {seq}")
print(f"A count: {a_count}")
print(f"C count: {c_count}")
print(f"G count: {g_count}")
print(f"T count: {t_count}")
print(f"A percentage: {a_percent:.2f}%")
print(f"C percentage: {c_percent:.2f}%")
print(f"G percentage: {g_percent:.2f}%")
print(f"T percentage: {t_percent:.2f}%")
print(f"Sequence length: {seq_length}")
