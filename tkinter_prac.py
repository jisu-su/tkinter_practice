import tkinter as tk
# 기본 창 생성
root = tk.Tk()
# 창 크기 설정
root.geometry("500x300")
# "Hello, Wordl!" 라벨 생성
Label = tk.Label(root, text="Hello, World!", fg="red", bg="black", font=("Courier", 24))
# 좌우, 상하 여백 설정
Label.pack(pady=20, padx=20)

root.mainloop()
