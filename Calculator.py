import tkinter as tk

# ฟังก์ชันสำหรับการคำนวณ
def click_button(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current_text + value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())  # ใช้ eval เพื่อคำนวณนิพจน์ที่ผู้ใช้กรอก
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("Calculator")
window.geometry("400x500")

# สร้างช่องสำหรับแสดงผล
entry = tk.Entry(window, width=16, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# สร้างปุ่ม
buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0),
]

# สร้างปุ่มแต่ละปุ่ม
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 20), command=calculate)
    elif text == 'C':
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 20), command=clear)
    else:
        button = tk.Button(window, text=text, width=5, height=2, font=("Arial", 20), command=lambda t=text: click_button(t))

    button.grid(row=row, column=col, padx=5, pady=5)

# เริ่มโปรแกรม
window.mainloop()
