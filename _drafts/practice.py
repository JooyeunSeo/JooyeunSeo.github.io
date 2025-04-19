import datetime as dt   
import os

##########################  OS별 맞춤  ##########################
def clear_screen(self):
    if os.name == 'nt':         # Windows
        os.system('cls')
    elif os.name == 'posix':    # macOS or Linux
        os.system('clear')
    else:
        pass                    # pass in different environments
################################################################

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
    title_form = date + "-" + title
    print(title_form)

def new_window_link():
    link = input("link: ")
    text = input("text: ")
    print(f'<a href="{link}" target="_blank">{text}</a>')

def highlight_tag():
    highlight_text = input("highlight text: ")
    print(f"<mark>{highlight_text}</mark>")

################################
leetcode_post_title()
#------------------------------#
class Solution:
    def leetcodetest(self):
        return "leetcode test"
#------------------------------#

#---------------#
test = Solution()
testcase = test.leetcodetest()
print(testcase)