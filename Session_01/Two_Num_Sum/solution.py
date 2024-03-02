N = int(input())
arr = list(map(int, input().split()))
target_sum = int(input())

found_pair = False
seen = set()

for num in arr:
    complement = target_sum - num
    if complement in seen:
        found_pair = True
        print(min(num, complement), max(num, complement))
        break
    seen.add(num)

if not found_pair:
    print("NONE")
