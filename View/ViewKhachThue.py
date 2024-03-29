#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from MVC.View.IconThemXoaSuaLM import IconThemXoaSuaLM
class ViewKhachThue():
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
        self.treeview = ttk.Treeview(self.frame_chitiet, columns=("STT", "MAKH", "TENKH", "CMND_CCCD", "NGSINH", "GIOITINH", "SDT","DCHI", "NGNGHIEP"),show="headings")

        # Thêm thanh cuộn ngang
        self.scrollbar_ngang = ttk.Scrollbar(self.frame_chitiet, orient="horizontal", command=self.treeview.xview)
        self.scrollbar_ngang.place(width=685, x=20, y=400)
        self.treeview.configure(xscrollcommand=self.scrollbar_ngang.set)

        # Thêm thanh cuộn dọc
        self.scrollbar_doc = ttk.Scrollbar(self.frame_chitiet, orient="vertical", command=self.treeview.yview)
        self.scrollbar_doc.place(height=350, x=700, y=50)
        self.treeview.configure(xscrollcommand=self.scrollbar_doc.set)


        self.treeview.heading('STT', text='STT')
        self.treeview.heading('MAKH', text='Mã Khách Hàng')
        self.treeview.heading('TENKH', text='Tên Khách Hàng')
        self.treeview.heading('CMND_CCCD', text='CMND/CCCD')
        self.treeview.heading('NGSINH', text='Ngày Sinh')
        self.treeview.heading('GIOITINH', text='Giới Tính')
        self.treeview.heading('SDT', text='SĐT')
        self.treeview.heading('DCHI', text='Địa Chỉ')
        self.treeview.heading('NGNGHIEP', text='Nghề Nghiệp')

        self.treeview.column("STT", width=50, minwidth=50, stretch=tk.NO, anchor="center")
        self.treeview.column("MAKH", width=100, minwidth=100, stretch=tk.NO, anchor="center")
        self.treeview.column("TENKH", width=150, minwidth=150, stretch=tk.NO, anchor="center")
        self.treeview.column("CMND_CCCD", width=100, minwidth=100, stretch=tk.NO, anchor="center")
        self.treeview.column("NGSINH", width=140, minwidth=140, stretch=tk.NO, anchor="center")
        self.treeview.column("GIOITINH", width=140, minwidth=140, stretch=tk.NO, anchor="center")
        self.treeview.column("SDT", width=140, minwidth=140, stretch=tk.NO, anchor="center")
        self.treeview.column("DCHI", width=140, minwidth=140, stretch=tk.NO, anchor="center")
        self.treeview.column("NGNGHIEP", width=140, minwidth=140, stretch=tk.NO, anchor="center")


        self.treeview.bind(sequence="<<TreeviewSelect>>", func=self.on_item_selected)
        self.treeview.place(height=350, width=680, x=20, y=50)

        self.label_makh = tk.Label(self.frame_chitiet)
        self.label_makh.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#ff0000",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Mã KH :')
        self.label_makh.place(x=720, y=50)
        self.label_tenkh = tk.Label(self.frame_chitiet)
        self.label_tenkh.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Tên KH :')
        self.label_tenkh.place(anchor="nw", x=720, y=80)
        self.label_cmnd = tk.Label(self.frame_chitiet)
        self.label_cmnd.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='CMND/CCCD :')
        self.label_cmnd.place(anchor="nw", x=720, y=110)

        self.label_ngaysinhkh = tk.Label(self.frame_chitiet)
        self.label_ngaysinhkh.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Ngày Sinh :')
        self.label_ngaysinhkh.place(anchor="nw", x=720, y=140)
        self.label_gioitinhkh = tk.Label(self.frame_chitiet)
        self.label_gioitinhkh.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Giới Tính :')
        self.label_gioitinhkh.place(anchor="nw", x=720, y=170)
        self.label_sdtkh = tk.Label(self.frame_chitiet)
        self.label_sdtkh.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='SĐT :')
        self.label_sdtkh.place(anchor="nw", x=720, y=200)


        self.label_diachikh = tk.Label(self.frame_chitiet)
        self.label_diachikh.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Địa chỉ :')
        self.label_diachikh.place(anchor="nw", x=720, y=230)
        self.label_nghenghiep = tk.Label(self.frame_chitiet)
        self.label_nghenghiep.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Nghề nghiệp :')
        self.label_nghenghiep.place(anchor="nw", x=720, y=260)

        self.entry_makh = ttk.Entry(self.frame_chitiet)
        self.entry_makh.place(anchor="nw", x=850, y=50)
        self.entry_tenkh = ttk.Entry(self.frame_chitiet)
        self.entry_tenkh.place(anchor="nw", x=850, y=80)
        self.entry_cmnd = ttk.Entry(self.frame_chitiet)
        self.entry_cmnd.place(anchor="nw", x=850, y=110)

        self.cal_ngaysinhkh = DateEntry(self.frame_chitiet, width=12, background='darkblue', foreground='white',
                                    borderwidth=2, date_pattern='yyyy/MM/dd', state='readonly', allow_none=True)
        self.cal_ngaysinhkh.place(anchor="nw", x=850, y=140, width=125)


        # Tạo hộp chọn Combobox
        self.combo_gioitinhkh = ttk.Combobox(self.frame_chitiet)
        # Các giá trị của hộp chọn
        self.combo_gioitinhkh['values'] = ("Nam", "Nữ")
        # Thiết lập giá trị được chọn
        self.combo_gioitinhkh.current(0)
        self.combo_gioitinhkh.config(state="readonly")
        self.combo_gioitinhkh.place(anchor="nw", x=850, y=170, width=125)

        self.entry_sdtkh = ttk.Entry(self.frame_chitiet)
        self.entry_sdtkh.place(anchor="nw", x=850, y=200)

        self.entry_diachikh = ttk.Entry(self.frame_chitiet)
        self.entry_diachikh.place(anchor="nw", x=850, y=230)
        self.entry_nghenghiep = ttk.Entry(self.frame_chitiet)
        self.entry_nghenghiep.place(anchor="nw", x=850, y=260)

        self.iconThem = IconThemXoaSuaLM().iconThem()
        self.iconXoa = IconThemXoaSuaLM().iconXoa()
        self.iconSua = IconThemXoaSuaLM().iconSua()
        self.iconLM = IconThemXoaSuaLM().iconLM()

        self.button_themkh = tk.Button(self.frame_chitiet)
        self.button_themkh.configure(
            # background="#2f4454",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#ffffff",
            # text='Thêm',
            borderwidth=0,
            highlightthickness=0,
            image=self.iconThem,
            compound="left"
        )
        self.button_themkh.place(anchor="nw", height=30, width=80, x=720, y=370)
        self.button_xoakh = tk.Button(self.frame_chitiet)
        self.button_xoakh.configure(
            # background="#2f4454",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#ffffff",
            # text='Xoá',
            borderwidth=0,
            highlightthickness=0,
            image=self.iconXoa,
            compound="left"
        )
        self.button_xoakh.place(anchor="nw", height=30, width=80, x=810, y=370)
        self.button_suakh = tk.Button(self.frame_chitiet)
        self.button_suakh.configure(
            # background="#2f4454",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#ffffff",
            # text='Sửa',
            borderwidth=0,
            highlightthickness=0,
            image=self.iconSua,
            compound="left"
        )
        self.button_suakh.place(anchor="nw", height=30, width=80, x=900, y=370)

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
        self.frame_chitiet.place(
            anchor="nw", height=420, width=985, x=10, y=220)

    def test(self):
        print(self.entry_makh.get())

    def hienthi_thongbao(self, kq, params=None):
        if params is None:
            if kq == 0:
                messagebox.showinfo("Thành công", "Thêm khách thuê thành công.")
                return
            if kq == 1:
                messagebox.showerror("Lỗi", "Thêm khách thuê thất bại.")
                return
        else:
            if kq == 0:
                messagebox.showinfo("Thành công", "Thêm khách thuê " + params + " thành công.")
                return
            if kq == 1:
                messagebox.showerror("Lỗi", "Mã khách thuê " + params + " đã tồn tại.")
                return

    def hienthi_thongbao_update(self, kq, params=None):
        if params is None:
            if kq == 1:
                messagebox.showinfo("Thành công", "Sửa khách thuê thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Sửa khách thuê thất bại.")
                return
        else:
            if kq == 1:
                messagebox.showinfo("Thành công", "Sửa khách thuê " + params + " thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Sửa khách thuê " + params + " thất bại.")
                return


    def hienthi_thongbao_delete(self, kq, params=None):
        if params is None:
            if kq == 1:
                messagebox.showinfo("Thành công", "Xóa khách thuê thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Xóa khách thuê thất bại.")
                return
        else:
            if kq == 1:
                messagebox.showinfo("Thành công", "Xóa khách thuê " + params + " thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Xóa khách thuê " + params + " thất bại.")
                return

    def on_item_selected(self, event):
        self.entry_makh.config(state='normal')
        selected_item = self.treeview.selection()
        if selected_item:
            values = self.treeview.item(selected_item, "values")
            item_text = self.treeview.item(selected_item, 'text')

            # Cập nhật giá trị của các Entry
            self.entry_makh.delete(0, tk.END)
            self.entry_makh.insert(0, values[1])
            self.entry_makh.config(state='disabled')

            self.entry_tenkh.delete(0, tk.END)
            self.entry_tenkh.insert(0, values[2])

            self.entry_cmnd.delete(0, tk.END)
            self.entry_cmnd.insert(0, values[3])

            # self.cal_ngaysinhkh.delete(0, tk.END)
            self.cal_ngaysinhkh.set_date(values[4])

            self.combo_gioitinhkh.delete(0, tk.END)
            self.combo_gioitinhkh.set(values[5])

            self.entry_sdtkh.delete(0, tk.END)
            self.entry_sdtkh.insert(0, values[6])

            self.entry_diachikh.delete(0, tk.END)
            self.entry_diachikh.insert(0, values[7])

            self.entry_nghenghiep.delete(0, tk.END)
            self.entry_nghenghiep.insert(0, values[8])


    def insert_treeview(self, index, kt):
        self.treeview.insert("", index=tk.END, text=".", values=(index, kt.MAKH, kt.TENKH, kt.CMND_CCCD, kt.NGSINH, kt.GIOITINH, kt.SDT, kt.DCHI, kt.NGNGHIEP))


    def delete_treeview(self):
        # Xóa tất cả các mục từ TreeView và cập nhật lại danh sách hiển thị
        for item in self.treeview.get_children():
            self.treeview.delete(item)

    # def on_item_selected_treeview(self, event):
    #     print()
