def unique(s):
    count={}
    for i in s:
        if i in count:
           count[i]=count[i]+1
        else:
            d[i]=1
            
    for i in s:
        if count[i]==1:
            return i
    return "None"
        
word = "papel"
result = unique(word)
print("The first non-repeating character in", word, "is:", result)
