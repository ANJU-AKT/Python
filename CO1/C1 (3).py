#3 (1)Generate positive list of numbers from a given list of integers

n1=[-4,-3,-2,-1,1,2,3,4,-5,-6,-7,8,9]
n2=[x for x in n1 if x>0]
print(n2)

#(2)Square of N numbers
n=int(input("Enter the limit="))
print([x*x for x in range(n+1)])

#(3))Form a list of vowels selected from a given word
word=input("Enter a word=")
vowel=["A","E","I","O","U","a","e","i","o","u"]
l=[x for x in word if x in vowel ]
print(l)

#(4))List ordinal value of each element of a word (Hint: use ord() to get ordinal values)
w=input("Enter a word=")
li=[ord(x) for x in w]
print(li)

