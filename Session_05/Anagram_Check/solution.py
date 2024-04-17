def is_anagram(s, t):
    # Convert both strings to lowercase
    s = s.lower()
    t = t.lower()
    
    # Sort the characters in both strings
    sorted_s = sorted(s)
    sorted_t = sorted(t)
    
    # Check if the sorted strings are equal
    return sorted_s == sorted_t

# Input
s = input()
t = input()

# Output
if is_anagram(s, t):
    print("TRUE")
else:
    print("FALSE")
