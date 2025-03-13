class Solution:
    def isPalindrome(self, s: str) -> bool:
        startPos = 0;
        endPos = len(s)-1;
        while startPos < endPos:
            if not(s[startPos].isalnum()):
                startPos = startPos+1;
            elif not(s[endPos].isalnum()):
                endPos =endPos-1;
            elif((s[startPos].lower())==(s[endPos].lower())):
                startPos =startPos+ 1;
                endPos =endPos-1;
            else:
                return False;
        return True;
