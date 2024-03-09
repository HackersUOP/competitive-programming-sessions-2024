N = int(input())
S = input()

S = S.strip()
last = S[S.rfind(' ') + 1:]
print(last)
