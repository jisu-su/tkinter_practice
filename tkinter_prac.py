import tkinter as tk
# 기본 창 생성
root = tk.Tk()
# 창 크기 설정
root.geometry("400x300")
# 창 배경색 설정
root.configure(bg="black")
# "Hello, Wordl!" 라벨 생성
Label = tk.Label(root, text="Hello, World!", fg="white", bg="black", font=("Arial", 24))

root.mainloop()