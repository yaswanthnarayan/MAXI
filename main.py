s=input()
ol=[]
l=[]
for i in range(len(s)):
    ns=s[i]
    ol.append(s[i])
    for j in range(i+1,len(s)):
        if s[j] not in ol:
            ns+=s[j]
            l.append(len(ns))
print(max(l))