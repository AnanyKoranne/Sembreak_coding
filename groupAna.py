from collections import defaultdict

def group_anagrams(strs):
    mp = defaultdict(list)

    for x in strs:
        key = "".join(sorted(x))
        mp[key].append(x)

    return list(mp.values())

print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))

print(group_anagrams([""]))

print(group_anagrams(["a"]))

print(group_anagrams(["abc", "bca", "cab", "xyz", "zyx"]))