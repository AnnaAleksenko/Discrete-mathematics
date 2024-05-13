A1=str(input())
A1=A1.upper()
m=len(A1)
ch=0
A=[""]*m
for i in range (0,m):
    A[i]=A1[i]
for i in range (0,m-1):
    for j in range (i+1,m):
        if (A[i]!="*" and A[j]!="*" and (A[i]==A[j])):
            ch+=1
            A[j]= "*"
for i in range (0,ch):
    A.remove("*")
print("Можно составить",len(A)**5,"слов")


