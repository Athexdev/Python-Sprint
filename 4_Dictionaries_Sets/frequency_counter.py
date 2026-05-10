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
