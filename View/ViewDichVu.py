#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

from MVC.View.ViewChiTietDichVu import ViewChiTietDichVu

from MVC.Model.ModelChiTietDichVu import ModelChiTietDichVu
from MVC.Controller.ControllerChiTietDichVu import ControllerChiTietDichVu

from MVC.View.IconThemXoaSuaLM import IconThemXoaSuaLM

class ViewDichVu():
    def __init__(self, master=None, username=None):
        self.username = username
        # build ui

        self.frame_chitiet = tk.Frame(master)
        self.frame_chitiet.configure(height=420, width=985)
        self.lablel_ds = tk.Label(self.frame_chitiet)
        self.lablel_ds.configure(
            font="{Times New Roman} 22 {bold}",
            foreground="#919300",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Danh sách')
        self.lablel_ds.place(x=20,y=10)

        self.treeview = ttk.Treeview(self.frame_chitiet, columns=("STT", "MADV", "TENDV", "GIA"), show="headings")

        # Thêm thanh cuộn ngang
        self.scrollbar_ngang = ttk.Scrollbar(self.frame_chitiet, orient="horizontal", command=self.treeview.xview)
        self.scrollbar_ngang.place(width=685, x=20, y=400)
        # self.scrollbar_ngang.place(width=670, x=20, y=560)
        self.treeview.configure(xscrollcommand=self.scrollbar_ngang.set)

        # Thêm thanh cuộn dọc
        self.scrollbar_doc = ttk.Scrollbar(self.frame_chitiet, orient="vertical", command=self.treeview.yview)
        self.scrollbar_doc.place(height=350, x=700, y=50)
        self.treeview.configure(xscrollcommand=self.scrollbar_doc.set)


        self.treeview.heading('STT', text='STT')
        self.treeview.heading('MADV', text='Mã Dịch Vụ')
        self.treeview.heading('TENDV', text='Tên Dịch Vụ')
        self.treeview.heading('GIA', text='Giá Dịch Vụ')

        self.treeview.column("STT", width=50, minwidth=50, stretch=tk.NO, anchor="center")
        self.treeview.column("MADV", width=250, minwidth=250, stretch=tk.NO, anchor="center")
        self.treeview.column("TENDV", stretch=tk.NO, anchor="center")
        self.treeview.column("GIA", stretch=tk.NO, anchor="center")

        self.treeview.bind(sequence="<<TreeviewSelect>>", func=self.on_item_selected)

        self.treeview.place(height=350, width=680, x=20, y=50)
        self.label_madv = tk.Label(self.frame_chitiet)
        self.label_madv.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#ff0000",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Mã dịch vụ :')
        self.label_madv.place(x=720, y=50)
        self.label_tendv = tk.Label(self.frame_chitiet)
        self.label_tendv.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Tên dịch vụ :')
        self.label_tendv.place(anchor="nw", x=720, y=80)
        self.label_giadv = tk.Label(self.frame_chitiet)
        self.label_giadv.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Giá :')

        self.label_giadv.place(anchor="nw", x=720, y=110)

        self.entry_madv = ttk.Entry(self.frame_chitiet)
        self.entry_madv.place(anchor="nw", x=850, y=50)
        self.entry_tendv = ttk.Entry(self.frame_chitiet)
        self.entry_tendv.place(anchor="nw", x=850, y=80)
        self.entry_gia = ttk.Entry(self.frame_chitiet)
        self.entry_gia.place(anchor="nw", x=850, y=110)

        self.iconThem = IconThemXoaSuaLM().iconThem()
        self.iconXoa = IconThemXoaSuaLM().iconXoa()
        self.iconSua = IconThemXoaSuaLM().iconSua()
        self.iconLM = IconThemXoaSuaLM().iconLM()

        self.button_them = tk.Button(self.frame_chitiet)
        self.button_them.configure(
            # background="#2f4454",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#ffffff",
            # text='Thêm',
            borderwidth=0,
            highlightthickness=0,
            image=self.iconThem,
            compound="left"
        )
        self.button_them.place(anchor="nw", height=30, width=80, x=720, y=370)
        self.button_xoa = tk.Button(self.frame_chitiet)
        self.button_xoa.configure(
            # background="#2f4454",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#ffffff",
            # text='Xoá',
            borderwidth=0,
            highlightthickness=0,
            image=self.iconXoa,
            compound="left"
        )
        self.button_xoa.place(anchor="nw", height=30, width=80, x=810, y=370)
        self.button_sua = tk.Button(self.frame_chitiet)
        self.button_sua.configure(
            # background="#2f4454",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#ffffff",
            # text='Sửa',
            borderwidth=0,
            highlightthickness=0,
            image=self.iconSua,
            compound="left"
        )
        self.button_sua.place(anchor="nw", height=30, width=80, x=900, y=370)

        self.button_lammoi = tk.Button(self.frame_chitiet)
        self.button_lammoi.configure(
            # background="#8000ff",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#ffffff",
            # text='Làm mới',
            borderwidth=0,
            highlightthickness=0,
            image=self.iconLM,
            compound="left"
        )
        self.button_lammoi.place(anchor="nw", height=31, x=794, y=320)

        self.button_chitiet = tk.Button(self.frame_chitiet)
        self.button_chitiet.configure(
            borderwidth=3,
            font="{Times New Roman} 12 {bold italic}",
            highlightthickness=0,
            foreground="#2F1AAF",
            relief="groove",
            text='Dịch vụ được sử dụng')
        self.button_chitiet.place(anchor="nw", x=170, y=15)

        self.frame_chitiet.place(
            anchor="nw", height=420, width=985, x=10, y=220)


    def test(self):
        print(self.entry_madv.get())

    def manhinh_ctdv(self):
        print("Màn hình CTDV")
        # print("TEST username DV")
        # print(self.username)
        view_ctdv = ViewChiTietDichVu(self.username)
        model_ctdv = ModelChiTietDichVu()
        controller_ctdv = ControllerChiTietDichVu(view_ctdv, model_ctdv)

    def hienthi_thongbao(self, kq, params=None):
        if params is None:
            if kq == 0:
                messagebox.showinfo("Thành công", "Thêm dịch vụ thành công.")
                return
            if kq == 1:
                messagebox.showerror("Lỗi", "Thêm dịch vụ thất bại.")
                return
        else:
            if kq == 0:
                messagebox.showinfo("Thành công", "Thêm dịch vụ " + params + " thành công.")
                return
            if kq == 1:
                messagebox.showerror("Lỗi", "Mã dịch vụ " + params + " đã tồn tại.")
                return


    def hienthi_thongbao_update(self, kq, params=None):
        if params is None:
            if kq == 1:
                messagebox.showinfo("Thành công", "Sửa dịch vụ thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Sửa dịch vụ thất bại.")
                return
        else:
            if kq == 1:
                messagebox.showinfo("Thành công", "Sửa dịch vụ " + params + " thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Sửa dịch vụ " + params + " thất bại.")
                return

    def hienthi_thongbao_delete(self, kq, params=None):
        if params is None:
            if kq == 1:
                messagebox.showinfo("Thành công", "Xóa dịch vụ thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Xóa dịch vụ thất bại.")
                return
        else:
            if kq == 1:
                messagebox.showinfo("Thành công", "Xóa dịch vụ " + params + " thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Xóa dịch vụ " + params + " thất bại.")
                return

    def on_item_selected(self, event):
        self.entry_madv.config(state='normal')
        selected_item = self.treeview.selection()
        if selected_item:
            values = self.treeview.item(selected_item, "values")
            item_text = self.treeview.item(selected_item, 'text')

            # Cập nhật giá trị của các Entry
            self.entry_madv.delete(0, tk.END)
            self.entry_madv.insert(0, values[1])
            self.entry_madv.config(state='disabled')

            self.entry_tendv.delete(0, tk.END)
            self.entry_tendv.insert(0, values[2])



            self.entry_gia.delete(0, tk.END)
            self.entry_gia.insert(0, values[3])

    def insert_treeview(self, index, dv):
        self.treeview.insert("", index=tk.END, text=".", values=(index, dv.MADV, dv.TENDV, dv.GIA))


    def delete_treeview(self):
        # Xóa tất cả các mục từ TreeView và cập nhật lại danh sách hiển thị
        # print("Đã xoá dữ liệu đang hiển thị treeview")
        for item in self.treeview.get_children():
            self.treeview.delete(item)
            # print("Đã xoá dữ liệu đang hiển thị treeview")

    # def on_item_selected_treeview(self, event):
    #     print()



