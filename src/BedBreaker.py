#!/usr/bin/python -tt

'''
Created on Nov 14, 2012

@author: niklas
'''

import argparse
import re
import bdParser

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
                           help="Input file type. [bb|xhmm] (BedBreaker|XHMM])")
                  
    args = argparser.parse_args()
    
    # TODO: Input sanity check
    inputFile = args.input
    outputFile = args.output
    inputType = args.type
    

    
    ## Determine input type
    if inputType == "bd":
        print "Input type: bd"
        #dobreakdancerstuff
        bdParser.main(inputFile, outputFile)
        
    elif inputType == "xhmm":
        #doxhmmstuff
        print "Input type: xhmm" 
    
    

        
if __name__ == '__main__':
    main()