#khai báo thư viện 
from tkinter import*
#tạo cửa sổ nền
window = Tk()
def click():
    lbl=Label(window,text="amazing",font="arial 12",bg='white',fg='grey')
    lbl.pack()#dung de dinh vi lable cố định
 
#đặt tiêu đề cho cửa sổ nền
window.title('anhtuanbin')
#đặt kích thước
window.geometry('500x700')
#đặt ảnh icon
window.iconbitmap('')
#cửa sổ nền thay đổi màu 
window.config(background="black")
#Làm cho ô vuông không phóng to được 
window.resizable(False,False)
#tạo lable
lbl=Label(window,text="anh tuan bin",font="arial 12",bg='white',fg='grey')
lbl.pack()#dung de dinh vi lable cố định
lbl=Label(window,text="HANG IN THERE !",font="arial 12",bg='white',fg='grey')
lbl.place(x=200,y=28)#dùng để định vị lable bằng trục x,y
nut=Button(window,text='button',bg='white',fg='grey',command=click)
nut.place(x=300,y=20)
#lệnh entry đề hiện thị văn bản 1 dòng để chấp nhận các giá trị từ người dùng 
entry=Entry(window,font="arial",bg='white',fg='black',bd=4,width=25)
entry.place(x=12,y=35)
#dùng hàm mainloop để
window.mainloop()