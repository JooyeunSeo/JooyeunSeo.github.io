import datetime as dt
import os

##########################  OS별 맞춤 적용 필요할 때  ##########################
def clear_screen(self):
    if os.name == 'nt':         # Windows
        os.system('cls')
    elif os.name == 'posix':    # macOS or Linux
        os.system('clear')
    else:
        pass                    # pass in different environments
###########################################################################

#############  블로그 포스트 작성할 때 필요한 양식  #############
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

def notice_box():
    color = input(
        "🌈 박스 색상 선택\n" \
        "1: light gray\n" \
        "2: gray\n" \
        "3: blue\n" \
        "4: yellow\n" \
        "5. green\n" \
        "6. red\n"
        )
    if color == "1":
        box_name = "notice"
    elif color == "2":
        box_name = "notice--primary"
    elif color == "3":
        box_name = "notice--info"
    elif color == "4":
        box_name = "notice--warning"
    elif color == "5":
        box_name = "notice--success"
    elif color == "6":
        box_name = "notice--danger"
    print(f'<div class="{box_name}" markdown="1"></div>')
########################################################

# ----------- 실행  -----------#
def run_file():
    select = input(
        "✅ 실행할 함수 선택\n" \
        "1: 리트코드 포스팅 파일이름 형식\n" \
        "2: 일반 포스팅 파일이름 형식\n" \
        "3: 새 창으로 링크 열기\n" \
        "4: 글자에 형광펜 칠하기\n" \
        "5. 색깔 박스 만들기\n"
        )
    if select == "1":
        leetcode_post_title()
    elif select == "2":
        post_title()
    elif select == "3":
        a_tag_new_window()
    elif select == "4":
        highlight_tag()
    elif select == "5":
        notice_box()
run_file()