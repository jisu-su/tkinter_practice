import tkinter as tk
# 기본 창 생성
root = tk.Tk()

# if문을 넣으면 좋을 거 같다. 만약에(if) 버튼이 눌린다면 “버튼이 클릭되었습니다”가 되도록 아니라면(else) 변하지 않는다. 
# 창 크기랑 배경색도 묶을 수 있을까,,,?

# 창 이름 정하기
root.title("button")
# 창 크기 설정
root.geometry("500x300")
# 창 배경색 설정
root.configure(bg="lightyellow")
# 버튼을 누르면 실행될 함수 
# def click_button():
#     label.config(text="버튼이 클릭되었습니다")

if click_button : 
    label.config(text="버튼이 클릭되었습니다")
else :
    label.config(text="버튼을 눌러보세요")

label= tk.Label(root, text="버튼을 눌러보세요", font=("맑은고딕",16))
label.pack(pady=20)

button = tk.Button(root, text="클릭", command=click_button)
button.pack()

root.mainloop()
