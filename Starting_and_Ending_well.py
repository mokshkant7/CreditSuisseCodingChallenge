import re

def question06(portfolios):
    s=input('Enter the starting letter: ')
    e=input('Enter the ending letter: ')
    l=list()
    pos=0
    for i in portfolios:
        #print(i) so see the word.
        if i[0]==s and i[-1]==e:
            l.append(pos)
            #print(l) to see the position of the stocks based on start and end.
        pos=pos+1

    l.sort()
    return l[-1] #returning the position of max index based on conditions.
