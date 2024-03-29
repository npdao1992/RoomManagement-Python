import tkinter as tk
from tkinter import ttk
from MVC.View.ViewLogin import ViewLogin
from MVC.Model.ModelLogin import ModelLogin
from MVC.Controller.ControllerLogin import ControllerLogin

from MVC.View.ViewThongTin import ViewThongTin
from MVC.View.ViewQuanLy import ViewQuanLy
from PIL import Image, ImageTk
class MyApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quản Lý Phòng Trọ")
        self.icon_path = ImageTk.PhotoImage(Image.open("View/images/icon-tieude.png"))
        self.wm_iconphoto(True, self.icon_path)
        # Hiển thị giao diện đăng nhập
        self.show_login()

    def show_login(self):
        self.login_frame = ViewLogin(self, self.show_notebook)
        # self.ten = self.login_frame.get_username()
        model_login = ModelLogin()
        controller_login = ControllerLogin(self.login_frame, model_login)
        self.login_frame.pack()


    def show_notebook(self, username):
        # print(self.ten)
        # Đăng nhập thành công, hiển thị giao diện notebook
        self.login_frame.destroy()

        self.notebook = ttk.Notebook(self)



        # tab1_image_path = "View/images/icon_pt.jpg"
        # tab_frame1 = ViewThongTin(self, tab1_image_path, "A")
        # self.notebook.add(tab_frame1, text="Thông tin")

        tab1_image_path = "View/images/icon_pt.jpg"
        self.create_tab("Thông Tin", ViewThongTin, tab1_image_path, username)

        tab2_image_path = ""
        self.create_tab("Quản Lý", ViewQuanLy, tab2_image_path, username)

        self.notebook.pack(expand=1, fill="both")
        # self.notebook.configure(bg="lightblue")

    def create_tab(self, tab_name, tab_class, image_path, *args, **kwargs):
        tab_frame = tab_class(self, image_path, *args, **kwargs)
        self.notebook.add(tab_frame, text=tab_name)

    def run(self):
        self.mainloop()


if __name__ == "__main__":
    app = MyApp()
    app.run()
