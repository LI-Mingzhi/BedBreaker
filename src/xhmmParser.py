#!/usr/bin/python -tt

'''
Created on Nov 21, 2012

@author: niklas
'''
import re
import bbClasses

def main(inputFile, outputFile):
    FH_INPUT = open(inputFile, "rU")
    FH_OUTPUT = open(outputFile, "w")
    
    # TODO: Automatically determine which samples are in the input files and create one output file per sample
    
    for line in FH_INPUT:
        
        ## Skip first line
        if not re.search(r'^SAMPLE', line):
            splitline = line.rstrip('\n').split('\t')
            
            chromosome = splitline[4]
            start_pos = re.match(r'(.*):(\d+)-(\d+)', splitline[2]).group(2)
            end_pos = re.match(r'(.*):(\d+)-(\d+)', splitline[2]).group(3)
            sv_type = splitline[1]
            
            entry = bbClasses.BEDentry(chromosome, start_pos, end_pos, sv_type)
            print entry.printEntryShort(),
            FH_OUTPUT.write(entry.printEntryShort())

    
    
    FH_INPUT.close()
    FH_OUTPUT.close()    

if __name__ == '__main__':
    main()