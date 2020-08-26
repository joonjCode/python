grid = []
for _ in range(2):
    curr_row = []
    for _ in range(3):
        curr_row.append(0)
    grid.append(curr_row)


grid = [[0 for _ in range(3)] for _ in range(3)]


# print(grid)


lst = [1, 2, -5, 4]

# print(max(lst))
# print(max(lst, key = lambda x:x*x))
# print(min(lst, key =lambda x: x*x))

bool(2)

print(any([(lambda x: x % 2 == 1)(num) for num in lst]))

print(all([(lambda x: x % 2 == 1)(num) for num in lst]))

print([x for x in lst if x%2 ==1])
print([bool(num%2) for num in lst])