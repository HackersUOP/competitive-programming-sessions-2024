str1 = input()
str2 = input()

def minDistance(word1: str, word2: str) -> int:
    m = len(word1)
    n = len(word2)

    if m < n:
        return minDistance(word2, word1)

    dp = [i for i in range(n + 1)]

    for i in range(1, m + 1):
        prev = dp[0]
        dp[0] = i
        for j in range(1, n + 1):
            temp = dp[j]
            if word1[i - 1] == word2[j - 1]:
                dp[j] = prev
            else:
                dp[j] = min(prev, dp[j], dp[j - 1]) + 1
            prev = temp

    return dp[n]

print(minDistance(str1, str2))
