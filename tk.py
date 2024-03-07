#khai báo thư viện 
from tkinter import*
#tạo cửa sổ nền
window = Tk()
#đặt tiêu đề cho cửa sổ nền
window.title('anhtuanbin')
#đặt kích thước
window.geometry('500x700')
#đặt ảnh icon
window.iconbitmap('')
#cửa sổ nền thay đổi màu 
window.config(background="black")
#lam cho o vuong ko thay doi phong to duoc
window.resizable(False,False)
#dùng hàm mainloop để
window.mainloop()