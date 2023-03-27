#!/usr/bin/env python

# This is a simple Python script to differentiate between DNA and RNA sequences.

# This imports the needed modules
import sys, re
from argparse import ArgumentParser

# Parsers for input
parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

# Check for invalid input
if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

# Convert to uppercase
args = parser.parse_args()
args.seq = args.seq.upper()

# Just checked again, that the script works fine. No further changes have to be made, to distinguish DNA and RNA for now.
# Check sequence identity
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq):
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA')
else:
    print ('The sequence is not DNA nor RNA')

# Search for motif
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")
		
# Here the script finishes.