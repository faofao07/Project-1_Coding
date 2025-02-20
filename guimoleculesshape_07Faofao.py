import tkinter as tk
from tkinter import messagebox

# สร้างฟังก์ชันสำหรับทำนายรูปร่างโมเลกุล
def predict_shape():
    try:
        element1 = entry_element1.get()
        atom1 = int(entry_atom1.get())
        element2 = entry_element2.get()
        atom2 = int(entry_atom2.get())

        moleculemass = {
            'H': 7, 'Be': 2, 'B': 3, 'C': 4, 'Si': 4, 'Ge': 4, 'Sn': 4, 'Pb': 4,
            'N': 5, 'P': 5, 'As': 5, 'Sb': 5, 'Bi': 5, 'O': 6, 'S': 6, 'Se': 6,
            'Te': 6, 'Po': 6, 'F': 7, 'Cl': 7, 'Br': 7, 'I': 7, 'At': 7, 'He': 8,
            'Ne': 8, 'Ar': 8, 'Kr': 8, 'Xe': 8, 'Rn': 8,
        }

        A = ((moleculemass[element1] * atom1) + (moleculemass[element2] * atom2)) // 8
        E = (((moleculemass[element1] * atom1) + (moleculemass[element2] * atom2)) % 8) / 2

        if (A, E) == (2, 0):
            result = "รูปร่างเส้นตรง สูตร AB2"
        elif (A, E) == (3, 0):
            result = "รูปร่างสามเหลี่ยมแบบราบ สูตร AB3"
        elif (A, E) == (4, 0):
            result = "รูปร่างทรงสี่หน้า สูตร AB4"
        elif (A, E) == (5, 0):
            result = "รูปร่างพีระมิดคู่ฐานสามเหลี่ยม สูตร AB5"
        elif (A, E) == (6, 0):
            result = "รูปร่างทรงแปดหน้า สูตร AB6"
        elif (A, E) == (2, 1):
            result = "รูปร่างมุมงอ สูตร AB2E"
        elif (A, E) == (3, 1):
            result = "รูปร่างพีระมิดฐานสามเหลี่ยม สูตร AB3E"
        elif (A, E) == (4, 1):
            result = "รูปร่างทรงสี่หน้าบิดเบี้ยว สูตร AB4E"
        elif (A, E) == (5, 1):
            result = "รูปร่างพีระมิดฐานสี่เหลี่ยม สูตร AB5E"
        elif (A, E) == (2, 2):
            result = "รูปร่างมุมงอ สูตร AB2E2"
        elif (A, E) == (3, 2):
            result = "รูปร่างรูปตัวที สูตร AB3E2"
        elif (A, E) == (4, 2):
            result = "รูปร่างสี่เหลี่ยมแบนราบ สูตร AB4E2"
        elif (A, E) == (2, 3):
            result = "รูปร่างเส้นตรง สูตร AB2E3"
        else:
            result = "ข้อมูลมีความผิดพลาด โปรดตรวจสอบความถูกต้อง"

        # แสดงผลลัพธ์ในช่องข้อความ
        label_result.config(text=result)

    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณากรอกข้อมูลให้ครบถ้วนและถูกต้อง")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมทำนายรูปร่างโมเลกุลของสารประกอบโคเวเลนต์ที่มีธาตุองค์ประกอบ 2 ชนิด โดย ครูพี่เฟา")

# สร้างส่วนของการป้อนข้อมูล
label_element1 = tk.Label(root, text="ธาตุองค์ตัวประกอบในโมเลกุลตัวที่ 1:")
label_element1.grid(row=0, column=0)
entry_element1 = tk.Entry(root)
entry_element1.grid(row=0, column=1)

label_atom1 = tk.Label(root, text="จำนวนของธาตุตัวที่ 1:")
label_atom1.grid(row=1, column=0)
entry_atom1 = tk.Entry(root)
entry_atom1.grid(row=1, column=1)

label_element2 = tk.Label(root, text="ธาตุองค์ตัวประกอบในโมเลกุลตัวที่ 2:")
label_element2.grid(row=2, column=0)
entry_element2 = tk.Entry(root)
entry_element2.grid(row=2, column=1)

label_atom2 = tk.Label(root, text="จำนวนของธาตุตัวที่ 2:")
label_atom2.grid(row=3, column=0)
entry_atom2 = tk.Entry(root)
entry_atom2.grid(row=3, column=1)

# สร้างปุ่มสำหรับทำนายรูปร่าง
button_predict = tk.Button(root, text="ทำนายรูปร่าง", command=predict_shape)
button_predict.grid(row=4, columnspan=2)

# สร้างช่องข้อความแสดงผลลัพธ์
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.grid(row=5, columnspan=2)

# เริ่มต้นโปรแกรม GUI
root.mainloop()
