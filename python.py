import re
file=open('regex_sum_.txt')
sum=0;
inp=file.read()
y=re.findall('[0-9]+',inp);
for i in y:
    sum=sum+int(i);


print(sum)