s = "ycce"
t = "ycsce"

count = 0
if len(s)<len(t):
    output=len(t)-len(s)
elif len(t)<len(s):
    output=len(s)-len(t)
elif len(s)==len(t):
    for i in range(len(s)):
        if s[i]!=t[i]:
            count=count+1
    output=count
print(output)
    
