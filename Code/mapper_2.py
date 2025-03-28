import sys


# input comes from STDIN (standard input)
for j in sys.stdin:
    # remove leading and trailing whitespace
    j = j.strip()
    # split the line into words
    wordfilename,count=j.split('\t',1)
    word,filename=wordfilename.split(' ',1)
    z=word+' '+count;
    print('%s\t%s' % (filename, z))