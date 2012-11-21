'''
Created on Nov 21, 2012

@author: niklas
'''

class BEDentry:
    def __init__(self, chr, start, end, type, score, strand):
        self.chr = chr
        self.start = str(int(start)-1)
        self.end = str(int(end)-1)
        self.type = type
        self.score = score
        self.strand = strand
        
    def printEntry(self):
        return self.chr + '\t' + self.start + '\t' + self.end + '\t' + self.type + '\t' + self.score + '\t' + self.strand + '\n'