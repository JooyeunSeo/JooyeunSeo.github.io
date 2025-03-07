import datetime as dt   
import os


#######################################
def leetcode_post_title():
    now = dt.datetime.now()
    date = str(now).split(" ")[0]
    title = input()
    title = "(" + title.replace(". ", ")")
    title = title.replace(" ", "-").lower()
    title_form = date + "-" + title
    print(title_form)


def post_title():
    now = dt.datetime.now()
    date = str(now).split(" ")[0]
    title = input()
    title = title.replace(" ", "-").lower()
    title_form = date + "-" + title + ".md"
    print(title_form)


def new_window_link():
    link = input("link: ")
    text = input("text: ")
    print(f'<a href="{link}" target="_blank">{text}</a>')


def highlight_tag():
    highlight_text = input("highlight text: ")
    print(f"<mark>{highlight_text}</mark>")
#--------------------------------------------#
leetcode_post_title()
#--------------------------------------------#
##########################  OS별 맞춤  ##########################
def clear_screen(self):
    if os.name == 'nt':         # Windows
        os.system('cls')
    elif os.name == 'posix':    # macOS or Linux
        os.system('clear')
    else:
        pass                    # pass in different environments
################################################################
#--------------------------------------------------------------#
class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        i = -1                          # 자리수에 따라 지수로 곱할 값
        sum = 0                         # 모든 자리수를 더한 결과값
        for c in columnTitle[::-1]:     # 뒤에서부터 순서대로 체크
            convert = int(26 * 26**i) * (ord(c) - 64)
            sum += convert
            i += 1
        return sum

#--------------------------------------------------------------#
test = Solution()
testcase = test.titleToNumber("AA")
print(testcase)