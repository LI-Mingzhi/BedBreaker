#!/usr/bin/python -tt

'''
Created on Nov 14, 2012

@author: niklas
'''

import argparse


def main():
    
    argparser = argparse.ArgumentParser()
    
    argparser.add_argument("input",
                           help="Path to the input file. This is the output file from BreakDancer")
    
    argparser.add_argument("output",
                           help="Path to the output BED file")
                  
    args = argparser.parse_args()
    
    print "Hello, this is the input arguments"
    
    print "\"input\" argument:", args.input
    print "\"output\" argument:", args.output
    
    # TODO: Input sanity check
    inputFile = args.input
    outputFile = args.output
    
    FH_INPUT = open(inputFile, "rU")
    FH_OUTPUT = open(outputFile, "w")
    
    ## TODO: Read input and do stuff
    
    FH_INPUT.close()
    FH_OUTPUT.close()
        
if __name__ == '__main__':
    main()