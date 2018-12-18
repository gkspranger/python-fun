# by default dicts have no order

from collections import OrderedDict

d = OrderedDict()
d["one"] = 1
d["two"] = 2
d["three"] = 3

for k,v in d.items():
    print(f"{k} = {v}")

d1 = OrderedDict()
d1["one"] = 1
d1["two"] = 2

d2 = OrderedDict()
d2["two"] = 2
d2["one"] = 1

print(d1 == d2)
