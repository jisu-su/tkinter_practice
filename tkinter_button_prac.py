import tkinter as tk
# 기본 창 생성
root = tk.Tk()

# if문을 넣으면 좋을 거 같다. 만약에(if) 버튼이 눌린다면 “버튼이 클릭되었습니다”가 되도록 아니라면(else) 변하지 않는다. 
# 창 크기랑 배경색도 묶을 수 있을까,,,?

# 하드코딩 피하기! 변수를 한대 묶어 보기
WINDOW_NAME = "button"
WINDOW_SIZE = "500x300"
WINDOW_COLOR = "lightyellow"
# 함수로 묶기
def set_window():
    root.title(WINDOW_NAME)
    root.geometry(WINDOW_SIZE)
    root.configure(bg=WINDOW_COLOR)
# 함수 실행을 위해 호출해주기
set_window()

#함수 안에 if문 넣기
# def click_button():
#     # cget을 이용해서 버튼을 누를 때마다 다른 문구가 나오도록 설정(토글)
#     if label.cget("text") == "버튼을 눌러보세요":
#         label.config(text="버튼이 클릭되었습니다")
#     else :
#         label.config(text="버튼을 눌러보세요")
# 삼항 연산자 이용하기 (얘도 함수가 필요하다) , 토글
def click_button():
    new_text = "버튼이 클릭되었습니다" if label.cget("text") == "버튼을 눌러보세요" else "버튼을 눌러보세요"
    label.config(text=new_text)

label= tk.Label(root, text="버튼을 눌러보세요", font=("맑은고딕",16))
label.pack(pady=20)

button = tk.Button(root, text="클릭", command=click_button)
button.pack()

root.mainloop()
