def lengthoflongestsubstring(s):
    maxi=0
    for i in range(0,len(s)):
        my_set=set()
        for j in range(i,len(s)):
            if s[j] in my_set :
                break
            maxi=max(maxi,j-i+1)
            my_set.add(s[j])
    return maxi





s="cadbzabcd"
print(lengthoflongestsubstring(s))
# answer=5    