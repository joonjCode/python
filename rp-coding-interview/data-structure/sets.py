
def count_unique(s):
    seen_c = [] # 0(1)
    for c in s: # 0(n)
        if c not in seen_c: #0(n)
            seen_c.append(c)
    return len(seen_c)


def count_unique2(s):
    seen_c =set() # 0(1)
    for c in s: # 0(n)
        if c not in seen_c: #0(1), similar to hash 
            seen_c.add(c)
    return len(seen_c)   #0(n)


def count_unique3(s):
    
    # return len({c for c in s})   #0(n)
    return len(set(s))


print(count_unique('aabb'))
print(count_unique('abcdef'))


print(set('hello'))

print(set({'hello':5}))
x = {'foo', 'bar'}
print(x)

# Elem
print('foo' in x)
print('baz' not in x)


