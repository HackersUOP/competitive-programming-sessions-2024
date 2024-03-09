def helper(str, enc):
    m, n = len(str), len(enc)
    i = j = x = 0
    while i < m and j < n:
        if enc[j].isdigit():
            if enc[j] == "0" and x == 0:
                return False
            x = x * 10 + int(enc[j])
        else:
            i += x
            x = 0
            if i >= m or str[i] != enc[j]:
                return False
            i += 1
        j += 1
    return i + x == m and j == n

M = int(input())
S = input()
L = int(input())
E = input()

result = helper(S, E)
print("TRUE" if result else "FALSE")
