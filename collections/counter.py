from collections import Counter

l = [1,2,3,2,1,3,4,5,6,6,4,3,3,2,2]

# count the number of times each value appeared
print(Counter(l))

s = "lkasjdlkasjdlkanclkajsdlkadjpiqjwdljknsdlfi"
print(Counter(s))

t = """
this is a sentence and it will do a count on this string
and is going to show me how many times me will see a world
in the sentence appear
"""

words = t.split(" ")
print(Counter(words))

c = Counter(words)
print(c.has_key("me"))
print(c.keys())
print(c.most_common(3))
