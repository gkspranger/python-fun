from collections import defaultdict

d = defaultdict(object)

d["one"]

for i in d:
    print(i)

# 0 == default value
d = defaultdict(lambda: 0)

d["one"]
d["two"] = 2

print(d)
