class Solution:
    def longestPalindrome(self, s: str) -> str:
        palindrome = ""

        for i in range(len(s)):
            j = len(s) - 1

            while j >= 0:
                if s[j] == s[i]:
                    cur = s[i:j + 1]

                    if self.is_palindrome(cur):
                        if (len(palindrome) < len(cur)):
                            palindrome = cur
                            break

                j = j - 1;

            if  (j - i) > (len(s) - j):
                break

        return palindrome
    
    def is_palindrome(self, s: str) -> bool:
        l = list(s)
        l.reverse()
        return (''.join(l) == s)

# test here
print(Solution().longestPalindrome("cmmrracelnclsbtdmuxtfiyahrvxuwreyorosyqapfpnsntommsujibzwhgugwtvxsdsltiiyymiofbslwbwevmjrsbbssicnxptvwmsmiifypoujftxylpyvirfueagprfyyydxeiftathaygmolkcwoaavmdmjsuwoibtuqoewaexihispsshwnsurjopdwttlzyqdbkypvjsbuidsdnpgklhwfnqdvlffcysnxeywvwvblatmxbflnuykhfhjptenhcxqinomlwalvlezefqybpuepbnymzlruuirpiatqgjgcnfmrlzshauoxuoqopcikogfwpssjdeplytcapmujyvgtfmmolnuadpwblgmcaututcrwsqrlpaaqobjfnhudmsulztbdkxpfejavastxejtpbqfftdtcdhvtpbzfuqcwkxtldtjycreimiujtxudtmokcoebhodbkgkgxjzrgyuqhozqtidltodlkziyofdeszwiobkwesdijxbbagguxvofvtphqxgvidqfkljufgubjmjllxoanbizwtedykwmneaosopynzlzvrlqcmyaahdcagfatlhwtgqxsyxwjhexfiplwtrtydjzrsysrcwszlntwrpgfedhgjzhztffqnjotlfudvczwfkhuwmdzcqgrmfttwaxocohtuscdxwfvhcymjpkqexusdaccw"))
