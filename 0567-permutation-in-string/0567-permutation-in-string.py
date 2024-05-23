class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_freq = defaultdict(int)
        for char in s1:
            s1_freq[char] += 1

        window_freq = defaultdict(int)
        left = 0
        for right in range(len(s2)):
            window_freq[s2[right]] += 1

            if right - left + 1 > len(s1):
                window_freq[s2[left]] -= 1
                if window_freq[s2[left]] == 0:
                    del window_freq[s2[left]]
                left += 1

            if window_freq == s1_freq:
                return True

        return False