#Store a list of first names. Count the occurrences of ‘a’ within the list

names=["athira","achu","ammu","hari"]
n=0

for x in names:
  n=n+x.count("a")
print("number of 'a'=",n)