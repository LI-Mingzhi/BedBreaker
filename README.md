BedBreaker
=========

A format converter that converts multiple formats to the BED format. Currently supported input format are outputs from: BreakDancer and XHMM.

Usage: python BedBreaker /path/to/inputFile /path/to/outputFile inputType -minScore INT

where inputType is either bd (BreakDancer output) or xhmm (XHMM output)

Then load the BED file into e.g. IGV and visualize the results!