# Input: S = { “the”, “quick”, “brown”, “fox”, “quick”}, word1 = “the”, word2 = “fox”
# Output: 3
# Explanation: Minimum distance between the words “the” and “fox” is 3

# Input: S = {“geeks”, “for”, “geeks”, “contribute”,  “practice”}, word1 = “geeks”, word2 = “practice”
# Output: 2
# Explanation: Minimum distance between the words “geeks” and “practice” is 2





def shortestDistance(s, word1, word2) :

    d1 = -1 
    d2 = -1
    ans = 100000000

    # Traverse the string
    for i in range(len(s)) :
        if (s[i] == word1) :
            d1 = i
        if (s[i] == word2) :
            d2 = i
        if (d1 != -1 and d2 != -1) :
            ans = min(ans, abs(d1 - d2))
    return ans


if __name__ == "__main__" :

    S = [ "the", "quick", "brown", "fox", "quick" ]
    word1 = "the"; word2 = "fox"
    print(shortestDistance(S, word1, word2))

