for i in range (1,10):
    print(i)
for i in range(1,10,2): #prints range 1-10 except 10 an 2
    print(i)
s=0
for i in range(1,11):
    s+=i #equivalent to s=s+i
print(s)

i=1
s=0
while i<=10:
    s +=i
    i+=1 #stops the loop, says i will increase by 1 each time.
print(s)