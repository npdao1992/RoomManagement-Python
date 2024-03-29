#!/usr/bin/python3
import tkinter as tk
import tkinter.ttk as ttk
from MVC.View.ViewPhong import ViewPhong
from PIL import Image, ImageTk, ImageDraw
from MVC.View.IconThemXoaSuaLM import IconThemXoaSuaLM

from MVC.View.ViewDichVu import ViewDichVu
from MVC.View.ViewKhachThue import ViewKhachThue
from MVC.View.ViewPhieuDangKy import ViewPhieuDangKy
from MVC.View.ViewPhieuThanhToan import ViewPhieuThanhToan

from MVC.Model.ModelPhong import ModelPhong
from MVC.Controller.ControllerPhong import ControllerPhong

from MVC.Model.ModelDichVu import ModelDichVu
from MVC.Controller.ControllerDichVu import ControllerDichVu

from MVC.Model.ModelKhachThue import ModelKhachThue
from MVC.Controller.ControllerKhachThue import ControllerKhachThue

from MVC.Model.ModelPhieuDangKy import ModelPhieuDangKy
from MVC.Controller.ControllerPhieuDangKy import ControllerPhieuDangKy

from MVC.Model.ModelPhieuThanhToan import ModelPhieuThanhToan
from MVC.Controller.ControllerPhieuThanhToan import ControllerPhieuThanhToan

class ViewQuanLy(ttk.Frame):
    def __init__(self, master=None, image_path=None, username=None):
        super().__init__(master)
        self.image_path = image_path
        self.username = username
        self.load_content()



    def load_image(self, image_path):
        # image_path = "images/icon_them.jpg"
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        # img = img.resize((870, 220))
        return img



    def load_content(self):
        # build ui
        self.frame_ThongKe = tk.Frame(self)
        self.frame_ThongKe.configure(height=720, width=1100)
        self.label_ThongTin = tk.Label(self.frame_ThongKe)
        self.label_ThongTin.configure(
            font="Poppins 24 bold",
            foreground="#2F1AAF",
            state="normal",
            takefocus=False,
            text='Quản Lý Phòng Trọ')
        self.label_ThongTin.place(anchor="center", x=500, y=50)

        # Tạo một Frame bên trong Tab 2 (Quản Lý) để chứa các nút button
        self.frame_button = tk.Frame(self.frame_ThongKe)
        self.frame_button.configure(height=200, width=200)


        self.icon_phong = IconThemXoaSuaLM().iconPhong()
        self.icon_dichvu = IconThemXoaSuaLM().iconDichVu()
        self.icon_khachthue = IconThemXoaSuaLM().iconKhachThue()
        self.icon_phieudangky = IconThemXoaSuaLM().iconPhieuDK()
        self.icon_phieuthantoan = IconThemXoaSuaLM().iconPhieuTT()


        self.button_phong = tk.Button(self.frame_button)
        self.button_phong.configure(
            # background="#0085FF",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#ffffff",
            # text='PHÒNG',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.show_content(1),
            image=self.icon_phong,
            compound="left"
        )
        self.button_phong.place(anchor="nw", height=90, width=140, x=0, y=20)
        self.button_dichvu = tk.Button(self.frame_button)
        self.button_dichvu.configure(
            # background="#ff8000",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#800000",
            # text='DỊCH VỤ',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.show_content(2),
            image=self.icon_dichvu,
            compound="left"
        )
        self.button_dichvu.place(
            anchor="nw", height=90, width=140, x=150, y=20)
        self.button_khachthue = tk.Button(self.frame_button)
        self.button_khachthue.configure(
            # background="#00ffff",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#800000",
            # text='KHÁCH THUÊ',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.show_content(3),
            image=self.icon_khachthue,
            compound="left"
        )
        self.button_khachthue.place(
            anchor="nw", height=90, width=170, x=300, y=20)
        # self.frame_button.place(
        #     anchor="nw",
        #     height=100,
        #     width=550,
        #     x=90,
        #     y=100)
        self.button_phieudangky = tk.Button(self.frame_button)
        self.button_phieudangky.configure(
            # background="#33e61a",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#800000",
            # text='PHIẾU ĐĂNG KÝ',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.show_content(4),
            image=self.icon_phieudangky,
            compound="left"
        )
        self.button_phieudangky.place(
            anchor="nw", width=200, height=90, x=480, y=20)
        self.button_phieuthanhtoan = tk.Button(self.frame_button)
        self.button_phieuthanhtoan.configure(
            # background="#eedd11",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#800000",
            # text='PHIẾU THANH TOÁN',
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.show_content(5),
            image=self.icon_phieuthantoan,
            compound="left"
        )
        self.button_phieuthanhtoan.place(
            anchor="nw", width=230, height=90, x=690, y=20)

        self.frame_button.place(
            anchor="nw",
            height=200,
            width=940,
            x=30,
            y=100)

        # Dictionary để lưu trữ các frame của từng nút
        self.content_frames = {
            1: self.create_content_frame(self.frame_ThongKe, "Phong"),
            2: self.create_content_frame(self.frame_ThongKe, "DichVu"),
            3: self.create_content_frame(self.frame_ThongKe, "KhachThue"),
            4: self.create_content_frame(self.frame_ThongKe, "PhieuDangKy"),
            5: self.create_content_frame(self.frame_ThongKe, "PhieuThanhToan"),
        }

        # Hiển thị giao diện của nút Button 1 khi ứng dụng khởi chạy
        self.show_content(1)

        self.frame_ThongKe.pack(side="top")

    def create_content_frame(self, parent, content):
        content_frame = tk.Frame(parent)
        content_frame.place(anchor="nw", height=370, width=985, x=10, y=220)
        # print(content)

        return content_frame

    def show_content(self, button_number):
        # Ẩn tất cả các frame con
        for frame in self.content_frames.values():
            frame.place_forget()

        # Hiển thị frame của nút được chọn
        # current_frame = self.content_frames[button_number]
        if button_number == 1:
            print("Màn hình Phòng trọ")
            view_pt = ViewPhong(self.frame_ThongKe, self.username)
            model_pt = ModelPhong()
            controller_pt = ControllerPhong(view_pt, model_pt)
        elif button_number == 2:
            print("Màn hình Dịch vụ")
            view_dv = ViewDichVu(self.frame_ThongKe, self.username)
            model_dv = ModelDichVu()
            controller_dv = ControllerDichVu(view_dv, model_dv)
        elif button_number == 3:
            print("Màn hình Khách thuê")
            view_kt = ViewKhachThue(self.frame_ThongKe, self.username)
            model_kt = ModelKhachThue()
            controller_kt = ControllerKhachThue(view_kt, model_kt)
        elif button_number == 4:
            print("Màn hình Phiếu Đăng Ký")
            view_pdk = ViewPhieuDangKy(self.frame_ThongKe, self.username)
            model_pdk = ModelPhieuDangKy()
            controller_pdk = ControllerPhieuDangKy(view_pdk, model_pdk)
        elif button_number == 5:
            print("Màn hình Phiếu Thanh Toán")
            view_ptt = ViewPhieuThanhToan(self.frame_ThongKe, self.username)
            model_ptt = ModelPhieuThanhToan()
            controller_ptt = ControllerPhieuThanhToan(view_ptt, model_ptt)
