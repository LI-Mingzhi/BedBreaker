#!/usr/bin/python -tt

'''
Created on Nov 14, 2012

@author: niklas
'''

import argparse
import re

## TODO: Create a class for an entry
## Chr, start, end, type, score, strand

def getOrientationInfo(orientation):
    ## Orientation is: <no_reads><pos_strand><no_reads><neg_strand>. E.g. 12+12-
    ori_parts = re.search(r'(\d+)(\+)(\d+)(\-)', orientation)
    posReads = ori_parts.group(1)
    negReads = ori_parts.group(3)
    return (posReads, negReads)

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
                  
    args = argparser.parse_args()
    
    #print "Hello, this is the input arguments"
    
    #print "\"input\" argument:", args.input
    #print "\"output\" argument:", args.output
    
    # TODO: Input sanity check
    inputFile = args.input
    outputFile = args.output
    
    FH_INPUT = open(inputFile, "rU")
    FH_OUTPUT = open(outputFile, "w")
    
    ## Read input
    for line in FH_INPUT:
        
        ## Skip the header
        if not re.search(r'^#', line):
            splitline = line.split('\t')
            
            chromosomes = [splitline[0], splitline[3]]
            start_pos = splitline[1]
            end_pos = splitline[4]
            score = splitline[8]
            sv_type = splitline[6]
            
            ## Check whether or not the chromosomes in the SV breakpoints are the same
            if chromosomes[0] == chromosomes[1]:
                
                oInfo = (getOrientationInfo(splitline[2]), getOrientationInfo(splitline[5]))
                                                      
                ## Check if the strands are the same
                ## Positive strand:
                if isNotZero(oInfo[0][0]) and isNotZero(oInfo[0][1]):
                    ## If yes: move on to printing
                    chrToPrint = "chr %s" % chromosomes[0]
                    startEndToPrint = "%s %s %s" % (start_pos, '\t', end_pos)
                    strandToPrint = "+"
                    
                    ### PRINT THE INFO
                    print chrToPrint, startEndToPrint, sv_type, score, strandToPrint
                
                ## Check if only one breakpoint has reads on the positive strand    
#                else:                    
#                    
#                    if isNotZero(oInfo[0][0]):
#                        ## Reads are present only at the first position
#                        ## TODO: Figure out how to handle this
#                        
#                    elif isNotZero(oInfo[0][1]):
#                        ## Reads are present only at the first position
#                        ## TODO: Figure out how to handle this
                
                ## Negative strand:
                if isNotZero(oInfo[1][0]) and isNotZero(oInfo[1][1]):
                    ## If yes: move on to printing
                    chrToPrint = "chr %s" % chromosomes[0]
                    startEndToPrint = "%s %s %s" % (start_pos, '\t', end_pos)
                    strandToPrint = "-"
                    
                    ### PRINT THE INFO
                    print chrToPrint, startEndToPrint, sv_type, score, strandToPrint
                    
                #Chromosome = "chr %s%s" % (splitline[0], '\t')
                #Start_Stop"%s %s %s" % (splitline[1], '\t', splitline[4])
            
            else:

                for chr in chromosomes:
                    
                    oInfo = (getOrientationInfo(splitline[2]), getOrientationInfo(splitline[5]))
                                                          
                    ## Check if the strands are the same
                    ## Positive strand:
                    if isNotZero(oInfo[0][0]) and isNotZero(oInfo[0][1]):
                        ## If yes: move on to printing
                        chrToPrint = "chr %s" % chr
                        startEndToPrint = "%s %s %s" % (start_pos, '\t', end_pos)
                        strandToPrint = "+"
                        
                        ### PRINT THE INFO
                        print chrToPrint, startEndToPrint, sv_type, score, strandToPrint
                    
                    ## Check if only one breakpoint has reads on the positive strand    
    #                else:                    
    #                    
    #                    if isNotZero(oInfo[0][0]):
    #                        ## Reads are present only at the first position
    #                        ## TODO: Figure out how to handle this
    #                        
    #                    elif isNotZero(oInfo[0][1]):
    #                        ## Reads are present only at the first position
    #                        ## TODO: Figure out how to handle this
                    
                    ## Negative strand:
                    if isNotZero(oInfo[1][0]) and isNotZero(oInfo[1][1]):
                        ## If yes: move on to printing
                        chrToPrint = "chr %s" % chr
                        startEndToPrint = "%s %s %s" % (start_pos, '\t', end_pos)
                        strandToPrint = "-"
                        
                        ### PRINT THE INFO
                        print chrToPrint, startEndToPrint, sv_type, score, strandToPrint

            
            #OrientationInfo2 = getOrientationInfo(splitline[5])
            
            #for i in range(0, 1):
            #    for j in range(0, 1):
            #       if OrientationInfo[i][j] != "0":
                        
            
            FH_OUTPUT.write("\n")
    
    
    
    FH_INPUT.close()
    FH_OUTPUT.close()
        
if __name__ == '__main__':
    main()