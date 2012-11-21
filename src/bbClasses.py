'''
Created on Nov 21, 2012

@author: niklas
'''

class BEDentry:
    
    strand = ""
    score = ""
    
#    def __init__(self, chr, start, end, type, score, strand):
#        self.chr = chr
#        self.start = str(int(start)-1)
#        self.end = str(int(end)-1)
#        self.type = type
#        self.score = score
#        self.strand = strand

    def __init__(self, chr, start, end, type):
        self.chr = chr
        self.start = str(int(start)-1)
        self.end = str(int(end)-1)
        self.type = type
        
    def setStrand(self, strand):
        self.strand = strand
    
    def setScore(self, score):
        self.score = score
        
    def printEntry(self):
        return "chr" + self.chr + '\t' + self.start + '\t' + self.end + '\t' + self.type + '\t' + self.score + '\t' + self.strand + '\n'
    
    def printEntryShort(self):
        return "chr" + self.chr + '\t' + self.start + '\t' + self.end + '\t' + self.type + '\n'