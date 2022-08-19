# Given a string of coin flips, return the number that would need to be flipped to make the sequence 'beautiful' (all heads before tails).
# Nathaniel Branscum, August 2022

def flipBeautiful(string: str) -> int:
    # convert to list
    s = []
    count = 0
    for c in string:
        s.append(c)
    # reverse the list
    s.reverse()
    try:
        lastHead = s.index("H")
        while lastHead < len(s):
            if s[lastHead] == "T":
                count += 1
            lastHead += 1
        return count
    # if no heads, then it's already perfect
    except:
        return 0
