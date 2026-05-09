**Manual String Reversal**
Question: Reverse a string without using [::-1] or reversed().

Python
# Answer
def rev(a):
    ans = ""
    for i in a:
        ans = i + ans  # Adding the character to the front
    return ans

word = "Debesh"
print(rev(word))


**Two-Pointer Palindrome Check**
Question: Check if a string is a palindrome using the two-pointer technique (efficient memory usage).

Python
# Answer
a = "Radar"
a = a.lower()
status = True
i = 0
j = len(a) - 1

while i < j:
    if a[i] != a[j]:
        status = False
        break
    else:
        i += 1
        j -= 1

if status:
    print("Palindrome")
else:
    print("Not a Palindrome")


**Vowel Counter (Membership Testing)**
Question: Count the vowels in a string and flag if it is "vowel heavy" (vowels > 50% of length).

Python
# Answer
a = "ashodeepi"
a = a.lower()
count = 0
vowels = "aeiou"

for i in a:
    if i in vowels:
        count += 1

if count > len(a) / 2:
    print("Vowel Heavy")
else:
    print(f"Vowel count: {count}")
