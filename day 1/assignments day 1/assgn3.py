str=input("Enter the string")
vowels='aeiouAEIOU'
vowel_count=0
const_count=0
space=' '
for ch in str:
    if ch in vowels:
        vowel_count+=1
    elif ch in space:
        break
    else:
        const_count+=1
print(f"there are {vowel_count} vowels")
print(f"there are {const_count} consonants")

    