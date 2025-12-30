import tkinter as tk

# 춘식이 만들기 함수 이름
def draw_chunsik_face(canvas):
    # 얼굴 (노란색 원)
    canvas.create_oval(100, 100, 300, 300, fill="yellow", outline="black", width=3)
    
    # 귀 (노란색 삼각형)
    # 왼쪽 귀
    canvas.create_polygon(120, 80, 150, 100, 100, 100, fill="yellow", outline="black") 
    # 오른쪽 귀 
    canvas.create_polygon(280, 80, 250, 100, 300, 100, fill="yellow", outline="black")  
    
    # 눈 (검은색 원)
    # 왼쪽 눈
    canvas.create_oval(150, 150, 170, 170, fill="black")  
    # 오른쪽 눈
    canvas.create_oval(230, 150, 250, 170, fill="black") 
    
    # 코 (흰색 타원)
    canvas.create_oval(190, 180, 210, 200, fill="white", outline="black")
    
    # 볼터치 (핑크색 원)
    # 왼쪽 볼터치
    canvas.create_oval(120, 220, 160, 260, fill="pink", outline="black")  
    # 오른쪽 볼터치
    canvas.create_oval(240, 220, 280, 260, fill="pink", outline="black")  
    
    # 수염 (검은색 선)
    # 왼쪽 수염
    canvas.create_line(140, 200, 100, 190, fill="black", width=2)
    canvas.create_line(140, 220, 100, 230, fill="black", width=2)
    # 오른쪽 수염
    canvas.create_line(260, 200, 300, 190, fill="black", width=2)
    canvas.create_line(260, 220, 300, 230, fill="black", width=2)

def main():
    # tkinter 창 생성하기
    root = tk.Tk()
    root.title("춘식이 얼굴")
    
    # Canvas 위젯 생성하기
    canvas = tk.Canvas(root, width=400, height=400, bg="white")
    canvas.pack()
    
    # 춘식이 얼굴 그리기
    draw_chunsik_face(canvas)
    
    # tkinter 메인 루프 실행하기
    root.mainloop()

if __name__ == "__main__":
    main()