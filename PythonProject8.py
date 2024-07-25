# Programming Assignment Unit 7

# Python Program

alphabet = "abcdefghijklmnopqrstuvwxyz"

test_dups = ["zzz","dog","bookkeeper","subdermatoglyphic", "subdermatoglyphics"]

test_miss = ["zzz","subdermatoglyphic",
"the quick brown fox jumps over the lazy dog"]

def histogram(s): d = dict() for c in s:
if c not in d: d[c] = 1
else:
d[c] += 1
return d # Part 1
def has_duplicates(s): h = histogram(s)
for k,v in h.items(): if v > 1:
return True return False

for s in test_dups:
if has_duplicates(s): print(s,"has duplicates")
else:
print(s,"has no duplicates")

# Part 2

def missing_letters(s): h = histogram(s)
m = []
for c in alphabet: if c not in h:
m.append(c) return ''.join(m)

for s in test_miss:
m = missing_letters(s) if len(m):
print(s,"is missing letters",m) else:
print(s,"uses all the letters")