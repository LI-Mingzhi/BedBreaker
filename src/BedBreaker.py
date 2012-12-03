#!/usr/bin/python -tt

'''
Created on Nov 14, 2012

@author: niklas
'''

import argparse
import re
import bdParser
import xhmmParser
import sys

def isNotZero(numReads):
    if numReads == "0":
        return False
    else:
        return True

def main():
    
    argparser = argparse.ArgumentParser()
    
    argparser.add_argument("input",
                           help="Path to the input file. This is the output file from BreakDancer")
    
    argparser.add_argument("output",
                           help="Path to the output BED file")
    
    argparser.add_argument("type",
                           help="Input file type. [bd|xhmm] (BreakDancer|XHMM])")
    
    argparser.add_argument("-minScore",
                           type=int,
                           help="Minimum score threshold (1-99)")
    
    argparser.add_argument("-onlyCommon",
                           type=int,
                           help="Enter the number of samples in the BreakDancer output to only consider SVs that are shared among all samples in the file.")
    
    args = argparser.parse_args()
    
    # TODO: Input sanity check
    inputFile = args.input
    outputFile = args.output
    inputType = args.type
    
    if not args.minScore:
        minScore = 0
    else:
        minScore = args.minScore
    
    if not args.onlyCommon:
        onlyCommon = 0
    else:
        onlyCommon = args.onlyCommon
    
    
    ## Determine input type
    if inputType == "bd":
        print "Input type: bd"
        #dobreakdancerstuff
        print onlyCommon
        bdParser.main(inputFile, outputFile, minScore, onlyCommon)
        
    elif inputType == "xhmm":
        print "Input type: xhmm"
        #doxhmmstuff
        xhmmParser.main(inputFile, outputFile)

    else:
        sys.exit("Incorrect input type: " + inputType)
    

        
if __name__ == '__main__':
    main()