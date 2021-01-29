#!/usr/bin/env python3
import os
import sys

def parse_file(path):
    """
    anlayze a given txt file and return information about its spaces,tabs and lines

    :arg path:the path of the txt file to be analyzed

    :return: tuples containing the number of spaces,the number of tabs,the number of lines
    """
    fd=open(path)
    i=0
    spaces=0
    tabs=0
    for i,line in enumerate(fd):
        spaces +=line.count(' ')
        tabs += line.count('\t')
    fd.close()

    return spaces,tabs,i+1

def main(path):
    """
    function is used to print the analysis result of the file

    :arg path: the path of the txt file to be analyzed
    :return:True if the file exits,False otherwise
    """
    if os.path.exists(path):
        spaces,tabs,lines=parse_file(path)
        print("Spaces {}. tabs {}. lines {}".format(spaces,tabs,lines))
        return True
    else:
        return False

if __name__=='__main__':
    if len(sys.argv)>1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)

