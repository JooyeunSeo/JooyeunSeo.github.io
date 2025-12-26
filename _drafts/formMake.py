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
    title = input("제목: ")
    runtime_ms = input("runtime(ms): ")
    runtime_rate = input("runtime(%): ")
    if not runtime_ms: runtime_ms = "0"
    if not runtime_rate: runtime_rate = "100.00"
    memory_mb = input("memory(mb): ")
    memory_rate = input("memory(%): ")
    number, name = title.split(". ")
    filename = date + '-' + '(' + number + ')' + name.replace(' ', '-').lower()
    print(f"\n{filename}\n'LeetCode: {name}' 풀이 정리\n{title}")
    print(f" Runtime: **{runtime_ms}** ms \| Beats **{runtime_rate}%**    \n Memory: **{memory_mb}** MB \| Beats **{memory_rate}%**    ")

def post_title_and_last_modified_time():
    now = dt.datetime.now()
    date = str(now).split(" ")[0]
    title = input("제목: ")
    title = title.replace(" ", "-").lower()
    formatted = now.strftime("%Y-%m-%dT%H:%M:%S")
    korean_utc = "+09:00"
    print(date + "-" + title)
    print(formatted + korean_utc)

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

def sup_or_sub():
    txt = input()
    if txt[-1] == 'i':
        print(f"{txt[0]}<sub>i</sub>")
    elif txt[1:].isalnum() or '^' in txt:
        txt = txt.replace('^', '')
        print(f"{txt[0]}<sup>{txt[1:]}</sup>")

def underline():
    is_list = input("리스트이면 입력, 단어나 문장이면 pass: ")
    if is_list:
        str_list = input("리스트 입력: ")
        new_list = list(str_list[1:-1].split(','))
        for i in range(len(new_list)):
            is_underline = input(f"밑줄이면 입력, 아니면 pass(index {i}): ")
            if is_underline:
                new_list[i] = f"<u>{new_list[i]}</u>"
        print(str(new_list).replace(' ', '').replace("'", ''))
    else:
        txt = input("단어나 문장 입력: ")
        print(f"<u>{txt}</u>")

#################################################

# ----------- 🖋️ 블로그 포스트 양식 실행  # -----------
def run_file():
    print(
        "✅ 실행할 함수 선택\n" \
        "1: 👾 리트코드 포스팅 파일이름 & bigO 시간 형식\n" \
        "2: 📝 일반 포스팅 파일이름 형식 및 시간 포맷\n" \
        "3: 🔗 새 창으로 링크 열기\n" \
        "4: 🌈 글자에 형광펜 칠하기\n" \
        "5. 🟨 색깔 박스 만들기\n" \
        "6. 📖 약어 태그 만들기\n" \
        "7. 🧮 위/아래 첨자 태그 붙이기\n" \
        "8. ✏️ 리스트의 원소나 글자에 밑줄치기"
        )
    
    while True:
        select = input()

        if select == "1":
            leetcode_post_title_and_bigOnotation()
            break
        elif select == "2":
            post_title_and_last_modified_time()
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
        elif select == "7":
            sup_or_sub()
            break
        elif select == "8":
            underline()
            break
        else:
            print("명시된 숫자 중 하나만 입력 가능")
run_file()
#################################################