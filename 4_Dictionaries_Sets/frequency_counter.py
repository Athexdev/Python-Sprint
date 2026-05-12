#Dictionary, frequency count

a = "debesh"
count = {}

for i in a:
    if i in count:
        # The letter is already a key, so add 1 to its value
        count[i] = count[i] + 1
    else:
        # The letter is new, so create the key and set it to 1
        count[i] = 1

print(count)

The Input:
purchases = ["Apple", "Banana", "Apple", "Orange", "Banana", "Apple"]

The Mission:
Write a script that outputs:

Unique items: ['Apple', 'Banana', 'Orange']

Counts: {'Apple': 3, 'Banana': 2, 'Orange': 1}

purchases = ["Apple", "Banana", "Apple", "Orange", "Banana", "Apple"]
count={}

for i in purchases:
    if i in count:
        count[i]=count[i]+1
    else:
        count[i]=1
print(list(set(purchases)))       
print(count)


**Bonus Program**
  try:
    print("NOTE : This program can handle every input !!")
    s=input("enter your word:")
    s=s.lower()
    d={}
    for i in s:
        if i in d:
            d[i]=d[i]+1
        else:
            d[i]=1
    i=0
    j=len(s)-1
    status=True

    while i<j:
        if s[i]!=s[j]:
            status=False
            break
        else:
            i=i+1
            j=j-1
    if status==True:
        print("Status : Palindrome",
        "\n--> Lenth of your word is:",len(s),
        "\n--> More Details:",d)
    else:
        print("Status :Not Palindrome",
        "\n--> Lenth of your word is:",len(s),
        "\n--> More Details:",d)
    
except Exception:
    print("kindly check your program and try again !!")
