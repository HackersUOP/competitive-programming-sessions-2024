def solve(s):
    last_index = {char: idx for idx, char in enumerate(s)}
    partitions = []
    start = 0
    end = 0
    
    for i, char in enumerate(s):
        end = max(end, last_index[char])
        if i == end:
            partitions.append(end - start + 1)
            start = end + 1
    return partitions

s = input()
ans = solve(s)
print(" ".join(str(num) for num in ans))
