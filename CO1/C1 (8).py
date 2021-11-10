"""Get a string from an input string where all occurrences of first character replaced with
‘$’, except first character.
[eg: onion -> oni$n] """

s1=input("Enter a string=")
c=s1[0]
s1=s1.replace(s1[0],"$")
print(c+s1[1:])
