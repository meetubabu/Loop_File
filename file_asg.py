import os

# Task create N table in a file
outfile=open("C:\\Users\meetu\\learnings\\Assignments\\Nfile.txt","w")
N=input("Enter the value for N:")
for i in range(1,11):
    line=str(N)+"*"+str(i)+"="+str(N*i)
    outfile.write(line+"\n")
outfile.close()

# create Even and Odd files, range(100)

outfile1=open("C:\\Users\meetu\\learnings\\Assignments\\odd.txt","w")
outfile2=open("C:\\Users\meetu\\learnings\\Assignments\\even.txt","w")

for i in range(100):
    if i%2==0:
        outfile2.write(str(i)+"\n")
    else:
        outfile1.write(str(i)+"\n")

outfile1.close()
outfile2.close()

    
