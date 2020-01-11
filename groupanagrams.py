import collections

def anagrams(strs):
    count = collections.Counter([tuple(sorted(s)) for s in strs])
    return filter(lambda x: count[tuple(sorted(x))] > 1, strs)

strs = ["abc", "cba", "tc", "ct"]

print(list(anagrams(strs)))