BedBreaker
=========

A format converter that converts multiple formats to the BED format. Currently supported input format are outputs from: BreakDancer and XHMM.

Usage: python BedBreaker /path/to/inputFile /path/to/outputFile inputType -minScore INT -onlyCommon INT

where inputType is either bd (BreakDancer output) or xhmm (XHMM output). Optionally, only SVs shared among all samples in the file may be converted; specify the number of samples in the file with the -onlyCommon flag.

Then load the BED file into e.g. IGV and visualize the results!
