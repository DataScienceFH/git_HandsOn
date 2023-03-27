#!/usr/bin/env python

# This script counts and derives the percentage of each nucleotide in an input DNA sequence

import sys

# Check for invalid input
if len(sys.argv) == 1:
    print("Please enter a DNA sequence as an argument")
    sys.exit(1)

# Get the sequence from the command line argument and convert to uppercase
seq = sys.argv[1].upper()

# Initialize counters for each nucleotide
a_count = 0
c_count = 0
g_count = 0
t_count = 0

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

# Calculate the total count and percentage of each nucleotide
total_count = a_count + c_count + g_count + t_count
a_percent = a_count / total_count * 100
c_percent = c_count / total_count * 100
g_percent = g_count / total_count * 100
t_percent = t_count / total_count * 100

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
