# -*- coding: utf-8 -*-
"""
Tidy Numbers Problem
@author: Kostas Klimantakis/dai16010
"""
import os.path

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start

def deleteContent(f):
    with open(f, "w"):
        pass

def isTidy(s):
    i=0
    c=0
    while i<len(s)-1:
        if(s[i]<=s[i+1]): c=c+1
        i=i+1
    if(c==len(s)-1):
        return 1
    else:
        return 0
    
def find_prob(s):
    i=0
    c=0
    while i<len(s)-1:
        if(s[i]>s[i+1]): return i
        i=i+1

def make_tidy(n):
    s=str(n)
    if isTidy(s)==1:
        L=list(s)
    else:
        while isTidy(s)==0:
            i=len(s)-1
            p=find_prob(s)
            #converts str s into list
            L=list(s)
            L[p]=str(int(L[p])-1)
            while i>p:
                L[i]='9'
                s=L
                i=i-1
    return L
    

def showCodeSection(cs):
    print("\n**")
    print("***")
    print("****")
    print("*****",cs)
    print("****")
    print("***")
    print("**\n")
    


#opens the input file (file must be in the same dir)
fname = input("File name:")
while not os.path.exists(fname):
    print("File not found.Try again.")
    fname = input("File name:")
    
infile = open(fname,"r")

showCodeSection("Parsed Input File:")

#starts reading from infile file
mystr = infile.read()
#close inflie
infile.close()

#reads number of cases
number_of_cases=int(mystr[:mystr.index('\n')])
print("Number Of Cases:",number_of_cases)
    
#a list whith the num. of every case
cases=range(1, int(number_of_cases)+1)

#an array for the input data
data = [] #akatergasto
output = []

#init pointers
start=mystr.index('\n')+1
end=find_nth(mystr,'\n',2)

#number of \n
i=3
        #main loop
for c in cases:
    data.append(int(mystr[start:end]))
    print('Case #',c,': ',mystr[start:end] , sep="")
    #updates pointers
    start=end+1
    end=find_nth(mystr,'\n',i)
    i=i+1

z=0
for d in data:
    mt=make_tidy(d)
    while isTidy(mt)==0 and z<10:
        mt=make_tidy(d)
        print(mt)
        z=z+1
#atermon
    output.append(mt)

#opens and clears the outfile file
outfile = open("solution.out",'a')
deleteContent("solution.out")

#formats the solution
solution_str = ''
i=0
while i<number_of_cases:
    j=0
    while j<len(output[i]):
        if(output[i][j]=='0' and j==0):
            j=j+1
            solution_str = solution_str + output[i][j]
        else:
            solution_str = solution_str + output[i][j]
        j=j+1
    solution_str = solution_str + '\n'
    i=i+1

        #end of main loop
i=0
j=1

#writes the 1st line of output
outfile.write("Case #")
outfile.write(str(j))
outfile.write(": ")

#debug string
deb_str = ''
deb_str = deb_str + "Case #"
deb_str = deb_str + str(j)
deb_str = deb_str + ": "

#writes on file
while i<len(solution_str):
    if solution_str[i]!='\n':
        outfile.write(str(solution_str[i]))
        deb_str = deb_str + str(solution_str[i])
    else:
        outfile.write('\n')
        deb_str = deb_str + '\n'
        if j<number_of_cases:
            j=j+1
            outfile.write("Case #")
            outfile.write(str(j))
            outfile.write(": ")
            deb_str = deb_str + "Case #"
            deb_str = deb_str + str(j)
            deb_str = deb_str + ": "
    i=i+1

#closes the outfile file
outfile.close()

showCodeSection("Output File:")
print(deb_str)

wait = input("YOUR FILE IS READY(in source's directory).\nPRESS ENTER TO EXIT.")
