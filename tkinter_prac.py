import tkinter as tk
# 기본 창 생성
root = tk.Tk()
# 창 크기 설정
root.geometry("500x300")
# 창 배경색 설정
root.configure(bg="lightblue")
# "Hello, Wordl!" 라벨 생성
Label = tk.Label(root, text="Hello, World!", fg="red", bg="white", font=("Courier", 35))
# 정중앙에 만들어 보기
Label.pack(expand=True)

root.mainloop()
