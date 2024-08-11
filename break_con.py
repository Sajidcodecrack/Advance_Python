n=[4,2,12,75,90]
m=[2,4,5,6,74,2]
for s in n:
    if(s==75):
        break;
    print(s)
print("Next one ")
for x in m:
    if(x==5):
        continue;
    print(x)