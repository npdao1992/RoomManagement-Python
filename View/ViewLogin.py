import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class ViewLogin(tk.Frame):
    def __init__(self, master=None, notebook_callback=None):
        super().__init__(master)
        self.master = master
        self.notebook_callback = notebook_callback
        self.create_widgets()

    def load_image(self):
        image_path = "View/images/icon-pt-login.png"

        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        return img
    def create_widgets(self):
        # Tạo frame chứa các widget để có thể thêm padding và cách biệt với background
        self.frame_all = tk.Frame(self, width=925, height=500, bg='white')

        self.img = self.load_image()
        self.image_label = tk.Label(self.frame_all, image=self.img, border=0, bg='white')
        self.image_label.place(x=50, y=50)

        self.frame_login = tk.Frame(self.frame_all,width=350,height=350,bg='white')
        self.frame_login.place(x=480, y=100)
        # Tạo các widget và đặt chúng trong frame
        self.title_label = tk.Label(self.frame_all, text="Đăng nhập", fg='#008000', bg='white')
        self.title_label.config(font=('Poppins', 23, 'bold'))
        self.title_label.place(x=570, y=60)

        def on_enter(e):
            self.username_entry.delete(0, 'end')

        def on_leave(e):
            if self.username_entry.get() == '':
                self.username_entry.insert(0, 'Tên đăng nhập')

        self.username_entry = tk.Entry(self.frame_login, width=25, fg='black', border=0, bg='white')
        self.username_entry.config(font=('Poppins', 11,))
        self.username_entry.bind("<FocusIn>", on_enter)
        self.username_entry.bind("<FocusOut>", on_leave)
        self.username_entry.insert(0, 'Tên đăng nhập')
        self.username_entry.place(x=30, y=60)

        self.gachchan = tk.Frame(self.frame_login, width=295, height=2, bg='black').place(x=25, y=87)

        def on_enter(e):
            self.password_entry.delete(0, 'end')

        def on_leave(e):
            if self.password_entry.get() == '':
                self.password_entry.insert(0, 'Mật khẩu')

        self.password_entry = tk.Entry(self.frame_login, width=21, fg='black', border=0, bg='white')
        self.password_entry.config(font=('Poppins',11, ))
        self.password_entry.bind("<FocusIn>", on_enter)
        self.password_entry.bind("<FocusOut>", on_leave)
        self.password_entry.insert(0, 'Mật khẩu')
        self.password_entry.place(x=30, y=130)

        self.gachchan2 = tk.Frame(self.frame_login, width=295, height=2, bg='black').place(x=25, y=157)

        self.login_button = tk.Button(self.frame_login, width=39, pady=7, text='Đăng nhập', bg='#008000', fg='white', border=0)
        self.login_button.place(x=35,y=204)

        self.label_tt = tk.Label(self.frame_login, text="Bạn chưa có tài khoản?", fg="black", bg='white')
        self.label_tt.config(font=('Poppins', 9,))
        self.label_tt.place(x=75, y=250)

        self.register_button = tk.Button(self.frame_login, width=6, text='Đăng ký', border=0, bg='white', fg='#008000')
        self.register_button.place(x=215, y=250)

        self.frame_all.pack(expand=True)


    def get_username(self):
        username = self.username_entry.get()
        return username

    def get_password(self):
        password = self.password_entry.get()
        return password

    def hienthi_thongbao(self, kq, username):
        if kq:
            messagebox.showinfo("Thông báo", "Đăng nhập thành công!")
            self.destroy()  # Đóng cửa sổ đăng nhập

            # Gọi hàm callback để chuyển đến giao diện notebook
            if self.notebook_callback:
                self.notebook_callback(username)
        else:
            messagebox.showerror("Lỗi", "Tên đăng nhập hoặc mật khẩu không đúng.")
