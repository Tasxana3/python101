from tkinter import * # "*"(wildcard import) คือการ import library ทั้งหมด
#นำเข้าองค์ประกอบพื้นฐานทั้งหมดจาก Tkinter เช่น Tk, Button, Frame, เป็นต้น
#Tkinter ย่อมาจาก TK Interface เป็น library สำหรับการพัฒนา GUI
from tkinter import ttk # theme of tk
#ttk เป็นmoduleตัวหนึ่ง หรือไฟล์1ไฟล์ในtkinter
from tkinter import messagebox

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

## สร้างปุ่มและเรียก pack() เพื่อติดตั้งปุ่มบน GUI
#b1 = Button(GUI,text='เงินมีอยู่กี่บาท')
#b1.pack(ipadx=20, ipady=20) # เรียกใช้ pack() เพื่อให้ปุ่มแสดงใน GUI
# หากไม่ได้เรียกใช้ pack(), grid(), หรือ place() ปุ่มจะไม่ปรากฏบนหน้าจอ

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='white')
L1.place(x=150,y=20)

##############################

def Button1() :
    text = 'Arctic Monkeys'
    messagebox.showinfo('Rock band',text)
   
FB1 = Frame(GUI) 
FB1.place(x=60, y=100)
b1 = Button(FB1,text='Favourite Rock band',command=Button1)
b1.pack(ipadx= 10, ipady=10)

##############################
def Button2() :
    text = 'ตอนนี้มีเงินในบัญชีอยู่ 20 ล้าน'
    messagebox.showinfo('เงินในบัญชี',text)
    #.showwarning #.showerror
    
FB2 = Frame(GUI) #คล้ายกระดานwhiteboard
#LabelFrame ( GUI,text='Money') = ใส่กรอบเพิ่มอีกชั้น โดยมีคำว่า Moneyวางอยู่บนเส้น

FB2.place(x=300, y=100)
b2 = Button(FB2,text='เงินมีอยู่กี่บาท',command=Button2)
b2.pack(ipadx= 10, ipady=10)
# เพิ่มpadx=20,pady=30 คือการระบุขนาดกรอบที่เพิ่มอีกชั้น
#แต่การใช้.place ปุ่มจะเล็กกว่า pack เราจึงต้องใส่เฟรมให้มัน
#จะได้ปุ่มดูใหญ่ขึ้น ( pack=center / place=custom )

##############################

def Button3() :
    text = 'data analysis'
    messagebox.showinfo('อาชีพ ',text)
   
FB3 = Frame(GUI) 
FB3.place(x=60, y=200)
b3 = Button(FB3,text='อยากทำงานอะไร',command=Button3)
b3.pack(ipadx= 10, ipady=10)



##############################

def Button4() :
    text = '17'
    messagebox.showinfo('อายุ',text)
   
FB4 = Frame(GUI) 
FB4.place(x=300, y=200)
b4 = Button(FB4,text='อายุเท่าไหร่',command=Button4)
b4.pack(ipadx= 10, ipady=10)

##############################

def Button5() :
    text = 'Cat'
    messagebox.showinfo('Pets',text)
   
FB5 = Frame(GUI) 
FB5.place(x=60, y=300)
b5 = Button(FB5,text='Cats or Dogs?',command=Button5)
b5.pack(ipadx= 10, ipady=10)

##############################

def Button6() :
    text = 'BETTER!'
    messagebox.showinfo('Develop',text)
   
FB6 = Frame(GUI) 
FB6.place(x=300, y=300)
b6 = Button(FB6,text='better or worse?',command=Button6)
b6.pack(ipadx= 10, ipady=10)
GUI.mainloop()


#run module for mac : fn+F5 
#command+S = save ห้ามsaveชื่อเดียวกับlibrary
