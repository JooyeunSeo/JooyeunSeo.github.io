from typing import List
##################### 리트코드 붙여넣기 #####################
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        n = len(text)
        i = 0
        result = []

        while i < n-2:
            if text[i] == first and text[i+1] == second:
                result.append(text[i+2])
                i += 3
            else:
                i += 1
        
        return result

################### 객체 생성 & 메소드 호출 ####################
test = Solution()
testcase = test.findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good")
print(testcase)
###########################################################