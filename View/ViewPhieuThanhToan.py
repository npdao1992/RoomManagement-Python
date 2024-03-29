#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from MVC.View.IconThemXoaSuaLM import IconThemXoaSuaLM

class ViewPhieuThanhToan():
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
        self.treeview = ttk.Treeview(self.frame_chitiet, columns=("STT", "MAPTT", "MAPDK", "NGTT", "SOTHANG", "TONGTIEN"),
                                 show="headings")

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
        self.treeview.heading('MAPTT', text='Mã Phiếu Thanh Toán')
        self.treeview.heading('MAPDK', text='Mã Phiếu Đăng Ký')
        self.treeview.heading('NGTT', text='Ngày Thanh Toán')
        self.treeview.heading('SOTHANG', text='Tháng')
        self.treeview.heading('TONGTIEN', text='Tổng Tiền')

        self.treeview.column("STT", width=50, minwidth=50, stretch=tk.NO, anchor="center")
        self.treeview.column("MAPTT", width=140, minwidth=100, stretch=tk.NO, anchor="center")
        self.treeview.column("MAPDK", width=130, minwidth=100, stretch=tk.NO, anchor="center")
        self.treeview.column("NGTT", width=100, minwidth=100, stretch=tk.NO, anchor="center")
        self.treeview.column("SOTHANG", width=120, minwidth=150, stretch=tk.NO, anchor="center")
        self.treeview.column("TONGTIEN", width=150, minwidth=150, stretch=tk.NO, anchor="center")

        self.treeview.bind(sequence="<<TreeviewSelect>>", func=self.on_item_selected)
        self.treeview.place(height=350, width=680, x=20, y=50)


        self.label_maptt = tk.Label(self.frame_chitiet)
        self.label_maptt.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#ff0000",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Mã PTT :')
        self.label_maptt.place(x=720, y=50)
        self.label_mapdk = tk.Label(self.frame_chitiet)
        self.label_mapdk.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Mã PDK :')
        self.label_mapdk.place(anchor="nw", x=720, y=80)
        self.label_ngtt = tk.Label(self.frame_chitiet)
        self.label_ngtt.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Ngày TT :')
        self.label_ngtt.place(anchor="nw", x=720, y=110)
        self.label_sothang = tk.Label(self.frame_chitiet)
        self.label_sothang.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Tháng :')
        self.label_sothang.place(anchor="nw", x=720, y=140)
        self.label_tongtien = tk.Label(self.frame_chitiet)
        self.label_tongtien.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#ff0000",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Tổng Tiền :')
        self.label_tongtien.place(anchor="nw", x=720, y=170)

        self.entry_maptt = tk.Entry(self.frame_chitiet)
        self.entry_maptt.place(anchor="nw", x=850, y=50)
        # self.entry_makh = tk.Entry(self.frame_chitiet)
        # self.entry_makh.place(anchor="nw", x=850, y=80)

        # Tạo hộp chọn Combobox MAPDK
        self.combo_mapdk = ttk.Combobox(self.frame_chitiet)
        self.combo_mapdk['values'] = ()
        self.combo_mapdk.config(state="readonly")
        self.combo_mapdk.place(anchor="nw", x=850, y=80, width=125)

        self.cal_ngtt = DateEntry(self.frame_chitiet, width=12, background='darkblue', foreground='white',
                                    borderwidth=2, date_pattern='yyyy/MM/dd', state='readonly', allow_none=True)
        self.cal_ngtt.place(anchor="nw", x=850, y=110, width=125)

        # Tạo hộp chọn Combobox số tháng
        self.combo_sothang = ttk.Combobox(self.frame_chitiet)
        # Các giá trị của hộp chọn
        self.combo_sothang['values'] = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
        # Thiết lập giá trị được chọn
        self.combo_sothang.current(0)
        self.combo_sothang.config(state="readonly")
        self.combo_sothang.place(anchor="nw", x=850, y=140, width=125)

        self.entry_tongtien = ttk.Entry(self.frame_chitiet)
        self.entry_tongtien.configure(state='disabled')
        self.entry_tongtien.place(anchor="nw", x=850, y=170)

        self.iconThem = IconThemXoaSuaLM().iconThem()
        self.iconXoa = IconThemXoaSuaLM().iconXoa()
        self.iconSua = IconThemXoaSuaLM().iconSua()
        self.iconLM = IconThemXoaSuaLM().iconLM()
        self.iconTT = IconThemXoaSuaLM().iconTT()

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
        self.button_lammoi.place(anchor="nw", height=31, x=738, y=320)

        self.button_tinhtien = tk.Button(self.frame_chitiet)
        self.button_tinhtien.configure(
            # background="#8000ff",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#ffffff",
            # text='Tính Tiền',
            borderwidth=0,
            highlightthickness=0,
            image=self.iconTT,
            compound="left"
        )
        self.button_tinhtien.place(anchor="nw", height=31, x=858, y=320)

        self.frame_chitiet.place(
            anchor="nw", height=420, width=985, x=10, y=220)

    def test(self):
        print(self.entry_maptt.get())

    def hienthi_thongbao(self, kq, params=None):
        if params is None:
            if kq == 0:
                messagebox.showinfo("Thành công", "Thêm phiếu thanh toán thành công.")
                return
            if kq == 1:
                messagebox.showerror("Lỗi", "Thêm phiếu thanh toán thất bại.")
                return
        else:
            if kq == 0:
                messagebox.showinfo("Thành công", "Thêm phiếu thanh toán " + params + " thành công.")
                return
            if kq == 1:
                messagebox.showerror("Lỗi", "Mã phiếu thanh toán " + params + " đã tồn tại.")
                return


    def hienthi_thongbao_update(self, kq, params=None):
        if params is None:
            if kq == 1:
                messagebox.showinfo("Thành công", "Sửa phiếu thanh toán thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Sửa phiếu thanh toán thất bại.")
                return
        else:
            if kq == 1:
                messagebox.showinfo("Thành công", "Sửa phiếu thanh toán " + params + " thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Sửa phiếu thanh toán " + params + " thất bại.")
                return

    def hienthi_thongbao_delete(self, kq, params=None):
        if params is None:
            if kq == 1:
                messagebox.showinfo("Thành công", "Xóa phiếu thanh toán thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Xóa phiếu thanh toán thất bại.")
                return
        else:
            if kq == 1:
                messagebox.showinfo("Thành công", "Xóa phiếu thanh toán " + params + " thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Xóa phiếu thanh toán " + params + " thất bại.")
                return

    def on_item_selected(self, event):
        self.entry_maptt.config(state='normal')
        self.entry_tongtien.config(state='normal')
        selected_item = self.treeview.selection()
        if selected_item:
            values = self.treeview.item(selected_item, "values")
            item_text = self.treeview.item(selected_item, 'text')

            # Cập nhật giá trị của các Entry
            self.entry_maptt.delete(0, tk.END)
            self.entry_maptt.insert(0, values[1])
            self.entry_maptt.config(state='disabled')

            self.combo_mapdk.delete(0, tk.END)
            self.combo_mapdk.set(values[2])

            self.cal_ngtt.set_date(values[3])

            self.combo_sothang.delete(0, tk.END)
            self.combo_sothang.set(values[4])

            self.entry_tongtien.delete(0, tk.END)
            self.entry_tongtien.insert(0, values[5])
            self.entry_tongtien.config(state='disabled')

    def insert_treeview(self, index, ptt):
        self.treeview.insert("", index=tk.END, text=".", values=(index, ptt.MAPTT, ptt.MAPDK, ptt.NGTT, ptt.SOTHANG, ptt.TONGTIEN))


    def delete_treeview(self):
        # Xóa tất cả các mục từ TreeView và cập nhật lại danh sách hiển thị
        # print("Đã xoá dữ liệu đang hiển thị treeview")
        for item in self.treeview.get_children():
            self.treeview.delete(item)
            # print("Đã xoá dữ liệu đang hiển thị treeview")

    def hienthi_tongtien(self, tiendichvu):
        self.entry_tongtien.config(state='normal')
        self.entry_tongtien.delete(0, tk.END)
        self.entry_tongtien.insert(0, tiendichvu)
        self.entry_tongtien.config(state='disabled')
