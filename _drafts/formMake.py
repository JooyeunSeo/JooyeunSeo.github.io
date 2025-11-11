import datetime as dt
import os

###################  💻 OS별 맞춤 적용 필요할 때  ###################
def clear_screen(self):
    if os.name == 'nt':         # Windows
        os.system('cls')
    elif os.name == 'posix':    # macOS or Linux
        os.system('clear')
    else:
        pass                    # pass in different environments
################################################################

# -----------  🖋️ 블로그 포스트 양식 함수  # -----------
def leetcode_post_title_and_bigOnotation():
    now = dt.datetime.now()
    date = str(now).split(" ")[0]
    title = input()
    runtime_ms = input("runtime(ms): ")
    runtume_rate = input("runtime(%): ")
    memory_mb = input("memory(mb): ")
    memory_rate = input("memory(%): ")
    number, name = title.split(". ")
    filename = date + '-' + '(' + number + ')' + name.replace(' ', '-').lower()
    print(f"{filename}\n'LeetCode: {name}' 풀이 정리")
    print(f" Runtime: **{runtime_ms}** ms \| Beats **{runtume_rate}%**    \n Memory: **{memory_mb}** MB \| Beats **{memory_rate}%**    ")

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
    text = input("write the text: ")
    print(f"<mark>{text}</mark>")

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

def abbreviation_tag():
    abbreviation = input("write the abbreviation: ")
    full_word = input("write the full word: ")
    print(f"*[{abbreviation}]: {full_word}")
#################################################

# ----------- 🖋️ 블로그 포스트 양식 실행  # -----------
def run_file():
    print(
        "✅ 실행할 함수 선택\n" \
        "1: 👾 리트코드 포스팅 파일이름 & bigO 시간 형식\n" \
        "2: 📝 일반 포스팅 파일이름 형식\n" \
        "3: 🔗 새 창으로 링크 열기\n" \
        "4: 🌈 글자에 형광펜 칠하기\n" \
        "5. 🟨 색깔 박스 만들기\n" \
        "6. 📖 약어 태그 만들기\n"
        )
    
    while True:
        select = input()

        if select == "1":
            leetcode_post_title_and_bigOnotation()
            break
        elif select == "2":
            post_title()
            break
        elif select == "3":
            a_tag_new_window()
            break
        elif select == "4":
            highlight_tag()
            break
        elif select == "5":
            notice_box()
            break
        elif select == "6":
            abbreviation_tag()
            break
        else:
            print("명시된 숫자 중 하나만 입력 가능")
run_file()
#################################################