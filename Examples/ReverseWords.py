class Solution:
    def reverseWords(self, s: str) -> str:
        # Step 1: Parse words manually without using split() or strip()
        n = len(s)
        words = []
        i = 0

        while i < n:
            # Skip spaces
            while i < n and s[i] == ' ':
                i += 1
            if i >= n:
                break
            # Accumulate non-space chars as a word
            j = i
            while j < n and s[j] != ' ':
                j += 1
            words.append(s[i:j])
            i = j

        # Step 2: Reverse the list of words
        left, right = 0, len(words) - 1
        while left < right:
            words[left], words[right] = words[right], words[left]
            left += 1
            right -= 1

        # Step 3: Join with single space
        return ' '.join(words)
ss = Solution()
print(ss.reverseWords("hello FASAKS FELLOWS"))