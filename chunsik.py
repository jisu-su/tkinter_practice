import tkinter as tk

# 춘식이 얼굴 창에 띄우기! 
# 함수 이름
def draw_chunsik_face(canvas):
    # 얼굴 노란 원 그리기
    canvas.create_oval(100, 100, 300, 300, fill="yellow", outline="black", width=3)
    # 눈 검은색 원 2개 그리기
    canvas.create_oval(150, 150, 170, 170, fill="black")
    canvas.create_oval(230, 150, 250, 170, fill="black")
    # 코 갈색 삼각형 그리기
    canvas.create_polygon(190, 180, 210, 180, 200, 200, fill="brown")
    # 입 갈색 곡선 그리기
    canvas.create_arc(170, 190, 230, 250, start=0, extent=-180, style=tk.ARC, outline="brown", width=2)
    # 볼 주황색 원 2개 그리기
    canvas.create_oval(120, 220, 160, 260, fill="orange", outline="black")
    canvas.create_oval(240, 220, 280, 260, fill="orange", outline="black")

def main():
    # 창 생성하기
    root = tk.Tk()
    root.title("춘식이 얼굴")

    # canvas 위젯 생성
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()

    # 춘식이 얼굴 그리기 호출
    draw_chunsik_face(canvas)

    # tkinter 메인 루프 실행하기
    root.mainloop()

if __name__ == "__main__":
    main()