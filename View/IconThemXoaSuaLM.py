#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class IconThemXoaSuaLM():
    def __init__(self):
        self.icon_them = None
        self.icon_xoa = None
        self.icon_sua = None
        self.icon_lm = None
    def iconThem(self):
        self.icon_them = ImageTk.PhotoImage(Image.open("View/images/bg_them.png"))
        return self.icon_them

    def iconXoa(self):
        self.icon_xoa = ImageTk.PhotoImage(Image.open("View/images/bg_xoa.png"))
        return self.icon_xoa

    def iconSua(self):
        self.icon_sua = ImageTk.PhotoImage(Image.open("View/images/bg_sua.png"))
        return self.icon_sua

    def iconLM(self):
        self.icon_lm = ImageTk.PhotoImage(Image.open("View/images/bg_reload.png"))
        return self.icon_lm

    def iconTT(self):
        self.icon_tt = ImageTk.PhotoImage(Image.open("View/images/bg_tinhtien.png"))
        return self.icon_tt

    def iconPhong(self):
        self.icon_p = ImageTk.PhotoImage(Image.open("View/images/bg_phong.png"))
        return self.icon_p

    def iconDichVu(self):
        self.icon_dv = ImageTk.PhotoImage(Image.open("View/images/bg_dichvu.png"))
        return self.icon_dv

    def iconKhachThue(self):
        self.icon_kt = ImageTk.PhotoImage(Image.open("View/images/bg_khachthue.png"))
        return self.icon_kt

    def iconPhieuDK(self):
        self.icon_pdk = ImageTk.PhotoImage(Image.open("View/images/bg_phieudk.png"))
        return self.icon_pdk

    def iconPhieuTT(self):
        self.icon_ptt = ImageTk.PhotoImage(Image.open("View/images/bg_phieutt.png"))
        return self.icon_ptt

