#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class ViewThongTin(ttk.Frame):
    def __init__(self, master=None, image_path=None, username=None):
        super().__init__(master)
        self.image_path = image_path
        self.username = username
        self.load_content()


    def load_image(self, image_path):
        image_path = "View/images/bn-2.jpg"

        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        # img = img.resize((870, 220))
        return img

    def load_content(self):
        # print(self.username)

        # img = self.load_image(self.image_path)
        # self.image_path = "View/images/icon_pt.jpg"
        img = self.load_image(self.image_path)


        # build ui
        self.frame_ThongTin = tk.Frame(self)
        self.frame_ThongTin.configure(height=720, width=1100)
        self.label_ThongTin = tk.Label(self.frame_ThongTin)
        self.label_ThongTin.configure(
            font="Poppins 24 bold",
            foreground="#2F1AAF",
            state="normal",
            takefocus=False,
            text='Quản Lý Phòng Trọ')
        self.label_ThongTin.place(anchor="center", x=520, y=50)
        self.labelframe_ThongTin = tk.LabelFrame(self.frame_ThongTin)
        self.labelframe_ThongTin.configure(
            background="#ffffff", borderwidth=8, height=550, width=1000,highlightbackground="blue",  # Đặt màu cho đường viền khi không có focus
     )
        self.label_tieude = tk.Label(self.labelframe_ThongTin)
        self.label_tieude.configure(
            background="#ffffff",
            font="Poppins 16 bold",
            foreground="#A3A443",
            takefocus=False,
            text='THÔNG TIN NHÀ TRỌ')
        self.label_tieude.place(anchor="center", x=450, y=40)
        self.label_tentro = tk.Label(self.labelframe_ThongTin)
        self.label_tentro.configure(
            background="#ffffff",
            font="{Times New Roman} 14 {bold}",
            foreground="#090040",
            state="normal",
            takefocus=True,
            text='Tên trọ :')
        self.label_tentro.place(x=50, y=80)
        self.label_mota = tk.Label(self.labelframe_ThongTin)
        self.label_mota.configure(
            background="#ffffff",
            font="{Times New Roman} 14 {bold}",
            foreground="#090040",
            state="normal",
            takefocus=True,
            text='Mô tả :')
        self.label_mota.place(x=50, y=160)
        self.label_ngaylap = tk.Label(self.labelframe_ThongTin)
        self.label_ngaylap.configure(
            background="#ffffff",
            font="{Times New Roman} 14 {bold}",
            foreground="#090040",
            state="normal",
            takefocus=True,
            text='Ngày lập :')
        self.label_ngaylap.place(x=50, y=120)

        self.label_cot = tk.Label(self.labelframe_ThongTin)
        self.label_cot.configure(
            background="#919300",
            )
        self.label_cot.place(x=520, y=80, height=110, width=15)

        # self.label_cot2 = tk.Label(self.labelframe_ThongTin)
        # self.label_cot2.configure(
        #     background="#090040",
        # )
        # self.label_cot2.place(x=410, y=55, height=3, width=100)

        self.label_tenchu = tk.Label(self.labelframe_ThongTin)
        self.label_tenchu.configure(

            background="#ffffff",
            font="{Times New Roman} 14 {bold}",
            foreground="#090040",
            justify="left",
            state="normal",
            takefocus=True,
            text='Tên chủ :')
        self.label_tenchu.place(x=550, y=80)
        self.label_diachi = tk.Label(self.labelframe_ThongTin)
        self.label_diachi.configure(
            background="#ffffff",
            font="{Times New Roman} 14 {bold}",
            foreground="#090040",
            state="normal",
            takefocus=True,
            text='Địa chỉ :')
        self.label_diachi.place(x=550, y=160)
        self.label_sdt = tk.Label(self.labelframe_ThongTin)
        self.label_sdt.configure(
            background="#ffffff",
            font="{Times New Roman} 14 {bold}",
            foreground="#090040",
            state="normal",
            takefocus=True,
            text='SĐT :')
        self.label_sdt.place(x=550, y=120)


        self.label_hinh = tk.Label(self.labelframe_ThongTin, image=img)
        self.label_hinh.image = img
        # self.label_hinh.pack()
        self.label_hinh.place(height=300, width=870, y=210, x=50)




        self.label_tent = tk.Label(self.labelframe_ThongTin)
        self.label_tent.configure(
            background="#ffffff",
            font="{Times New Roman} 14 {bold}",
            state="normal",
            takefocus=True,
            text='Nhà Trọ Python')
        self.label_tent.place(x=150, y=80)
        self.label_ngay = tk.Label(self.labelframe_ThongTin)
        self.label_ngay.configure(
            background="#ffffff",
            font="{Times New Roman} 14 {bold}",
            state="normal",
            takefocus=True,
            text='01/01/2023')
        self.label_ngay.place(x=150, y=120)
        self.label_mo = tk.Label(self.labelframe_ThongTin)
        self.label_mo.configure(
            background="#ffffff",
            font="{Times New Roman} 14 {bold}",
            state="normal",
            takefocus=True,
            text='Phòng trọ sạch sẽ & an ninh')
        self.label_mo.place(x=150, y=160)
        self.label_xinc = tk.Label(self.frame_ThongTin)
        self.label_xinc.configure(
            # background="#ffffff",
            font="{Times New Roman} 13 ",
            justify="left",
            takefocus=True,
            foreground="#090040",
            text='Xin chào:')


        self.label_xinc.place(x=50, y=90)
        self.label_tenc = tk.Label(self.frame_ThongTin)
        self.label_tenc.configure(
            # background="#ffffff",
            foreground="#BE0000",
            font="{Times New Roman} 16 {bold}",
            justify="left",
            takefocus=True,
            text='')

        if self.username:
            self.label_tenc.config(text=self.username)


        self.label_tenc.place(x=130, y=86)
        self.label_s2 = tk.Label(self.labelframe_ThongTin)
        self.label_s2.configure(
            background="#ffffff",
            font="{Times New Roman} 14 {bold}",
            justify="left",
            state="normal",
            takefocus=True,
            text='Lý Vương SQL')
        self.label_s2.place(x=650, y=80)
        self.label_s = tk.Label(self.labelframe_ThongTin)
        self.label_s.configure(
            background="#ffffff",
            font="{Times New Roman} 14 {bold}",
            justify="left",
            state="normal",
            takefocus=True,
            text='0971888812')
        self.label_s.place(x=650, y=120)
        self.label_d = tk.Label(self.labelframe_ThongTin)
        self.label_d.configure(
            background="#ffffff",
            font="{Times New Roman} 14 {bold}",
            state="normal",
            takefocus=True,
            text='127 Hồ Văn Huê, Phú Nhuận')
        self.label_d.place(x=650, y=160)
        self.labelframe_ThongTin.place(anchor="nw", x=50, y=120)

        self.frame_ThongTin.pack(side="top")