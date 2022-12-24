def get_min_key(st):
    b_map ={}
    min = 0
    min_key = ""
    for c in st:
        if c not in b_map.keys():
            b_map[c] = 1
            min = 1
            min_key = c
        else:
            b_map[c] = b_map[c]+1

        if b_map[c] < min:
            min = b_map[c]
            min_key = c
    return min_key

def rec(st, n):
    map = {}
    s = [st[i:i+n] for i in range(0, len(st), n)]

    for c in s:
        if c not in map.keys():
            map[c] = 1
        else:
            map[c] = map[c]+1

    if len(map.keys()) != 1:
        return rec(st, n+1)
    
    map['pattern'] = list(map.keys())[0]
    map['div'] = map[list(map.keys())[0]]

    if st == list(map.keys())[0] and len(st)>1:
        min_key = get_min_key(st)
        return rec(st.replace(min_key,""), 1)

    del map[list(map.keys())[0]]
    return map

def solution(s):
    map = rec(s,1)
    map['input'] = s
    return map

print(solution('a'))
print(solution('aa'))
print(solution('abcabc'))
print(solution('abcabcabc'))
print(solution('aaT'))
print(solution('ababT'))
print(solution('abccbaabccba'))
print(solution('aabbaaaabbaa'))
