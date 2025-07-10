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
    head, sub = title, title
    head = "(" + head.replace(". ", ")")
    head = head.replace(" ", "-").lower()
    head = date + "-" + head
    sub = sub.split(". ")[1]
    print(f"{head}\n'LeetCode: {sub}' 풀이 정리")

def post_title():
    now = dt.datetime.now()
    date = str(now).split(" ")[0]
    title = input()
    title = title.replace(" ", "-").lower()
    title_form = date + "-" + title
    print(title_form)

def a_tag_new_window():
    link = input("link: ")
    text = input("text: ")
    print(f'<a href="{link}" target="_blank">{text}</a>')

def highlight_tag():
    highlight_text = input("highlight text: ")
    print(f"<mark>{highlight_text}</mark>")


#####################
leetcode_post_title()
# post_title()
# a_tag_new_window()
# highlight_tag()