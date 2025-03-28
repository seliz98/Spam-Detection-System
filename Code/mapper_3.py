import sys
import os


# input comes from STDIN (standard input)
for j in sys.stdin:
    # remove leading and trailing whitespace
    j = j.strip()
    # split the line into words
    wf,nN=j.split('\t',1)
    w,f=wf.split(' ',1)
    z=f+' '+nN+' '+str(1)
    print ('%s\t%s' % (w,z))