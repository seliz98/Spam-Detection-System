import sys
import os
from math import log10,sqrt

D=10.0
# input comes from STDIN (standard input)
for j in sys.stdin:
    # remove leading and trailing whitespace
    j = j.strip()
    # split the line into words
    wf,nNm=j.split('\t',1)
    n,N,m=nNm.split(' ',2)
    n=float(n)
    N=float(N)
    m=float(m)
    tfidf= (n/N)*log10(D/m)
    print ('%s\t%s' % (wf,round(tfidf)))