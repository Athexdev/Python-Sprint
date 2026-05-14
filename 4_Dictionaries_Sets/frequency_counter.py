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


students = [
    {"name": "Devesh", "scores": [85, 90, 88]},
    {"name": "Rahul", "scores": [70, 75, 72]},
    {"name": "Amit", "scores": [95, 98, 92]}
]

**student database topper and average logic**

for d in students:
    average=sum(d["scores"])/len(d["scores"])
    average=round(average,2)
    print(f"{d["name"]}'s average is {average}")
    
topper=[]
for d in students:
    if sum(d["scores"])/len(d["scores"]) >90:
        topper.append(d["name"])
        
print(f"{topper} is the topper of the class ")

**the sales database problem to find the high valkue items **

sales = [("Laptop", 50000), ("Mouse", 500), ("Laptop", 52000), ("Keyboard", 1500), ("Mouse", 450)]





inventory_value= {}

for itemname,price in sales:

    if itemname in inventory_value:

        inventory_value[itemname]=inventory_value[itemname]+price

    else:

        inventory_value[itemname]=price



        

high_value_items=[itemname for itemname,price in inventory_value.items() if price>1000]

        

        

print("the high value items are:",high_value_items)    


