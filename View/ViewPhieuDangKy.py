#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
# from datetime import datetime
from MVC.View.IconThemXoaSuaLM import IconThemXoaSuaLM
class ViewPhieuDangKy():
    def __init__(self, master=None, username=None):
        self.username = username
        # self.current_date = datetime.now().date()
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
        self.treeview = ttk.Treeview(self.frame_chitiet, columns=("STT", "MAPDK", "TENKH", "TENPT", "NGTHUE", "NGTRA"),
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
        self.treeview.heading('MAPDK', text='Mã Phiếu Đăng Ký')
        self.treeview.heading('TENKH', text='Tên Khách Hàng')
        self.treeview.heading('TENPT', text='Tên Phòng')
        self.treeview.heading('NGTHUE', text='Ngày Thuê')
        self.treeview.heading('NGTRA', text='Ngày Trả')

        self.treeview.column("STT", width=50, minwidth=50, stretch=tk.NO, anchor="center")
        self.treeview.column("MAPDK", width=110, minwidth=100, stretch=tk.NO, anchor="center")
        self.treeview.column("TENKH", width=100, minwidth=100, stretch=tk.NO, anchor="center")
        self.treeview.column("TENPT", width=100, minwidth=100, stretch=tk.NO, anchor="center")
        self.treeview.column("NGTHUE", width=160, minwidth=180, stretch=tk.NO, anchor="center")
        self.treeview.column("NGTRA", width=160, minwidth=150, stretch=tk.NO, anchor="center")

        self.treeview.bind(sequence="<<TreeviewSelect>>", func=self.on_item_selected)
        self.treeview.place(height=350, width=680, x=20, y=50)


        self.label_mapdk = tk.Label(self.frame_chitiet)
        self.label_mapdk.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#ff0000",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Mã PDK :')
        self.label_mapdk.place(x=720, y=50)
        self.label_makh = tk.Label(self.frame_chitiet)
        self.label_makh.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#ff0000",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Tên KH :')
        self.label_makh.place(anchor="nw", x=720, y=80)
        self.label_map = tk.Label(self.frame_chitiet)
        self.label_map.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#ff0000",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Tên Phòng :')
        self.label_map.place(anchor="nw", x=720, y=110)
        self.label_ngthue = tk.Label(self.frame_chitiet)
        self.label_ngthue.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Ngày Thuê :')
        self.label_ngthue.place(anchor="nw", x=720, y=140)
        self.label_ngtra = tk.Label(self.frame_chitiet)
        self.label_ngtra.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Ngày Trả :')
        self.label_ngtra.place(anchor="nw", x=720, y=170)
        self.entry_mapdk = tk.Entry(self.frame_chitiet)
        self.entry_mapdk.place(anchor="nw", x=850, y=50)
        # self.entry_makh = tk.Entry(self.frame_chitiet)
        # self.entry_makh.place(anchor="nw", x=850, y=80)

        # Tạo hộp chọn Combobox MAKH
        self.combo_makh = ttk.Combobox(self.frame_chitiet)
        self.combo_makh['values'] = ()
        self.combo_makh.config(state="readonly")
        self.combo_makh.place(anchor="nw", x=850, y=80, width=125)

        # Tạo hộp chọn Combobox MAPT
        self.combo_map = ttk.Combobox(self.frame_chitiet)
        self.combo_map['values'] = ()
        self.combo_map.config(state="readonly")
        self.combo_map.place(anchor="nw", x=850, y=110, width=125)


        self.cal_ngthue = DateEntry(self.frame_chitiet, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy/MM/dd', state='readonly', allow_none=True)
        # self.cal_ngthue.set_date(None)  # Set giá trị mặc định là None
        self.cal_ngthue.place(anchor="nw", x=850, y=140, width=125)

        self.cal_ngtra = DateEntry(self.frame_chitiet, width=12, background='darkblue', foreground='white', borderwidth=2, date_pattern='yyyy/MM/dd', state='readonly', allow_none=True)
        # self.cal_ngtra.set_date(None)  # Set giá trị mặc định là None
        # self.cal_ngtra.delete(0, 'end')
        self.cal_ngtra.place(anchor="nw", x=850, y=170, width=125)

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

        self.frame_chitiet.place(
            anchor="nw", height=420, width=985, x=10, y=220)

        # self.buttons = {
        #     "Load": tk.Button(self.frame_chitiet, text="Load")
        # }
        # self.buttons["Load"].grid(row=9, column=1, padx=10)


    def test(self):
        print(self.entry_mapdk.get())

    def hienthi_thongbao(self, kq, params=None):
        if params is None:
            if kq == 0:
                messagebox.showinfo("Thành công", "Thêm phiếu đăng ký thành công.")
                return
            if kq == 1:
                messagebox.showerror("Lỗi", "Thêm phiếu đăng ký thất bại.")
                return
        else:
            if kq == 0:
                messagebox.showinfo("Thành công", "Thêm phiếu đăng ký " + params + " thành công.")
                return
            if kq == 1:
                messagebox.showerror("Lỗi", "Mã phiếu đăng ký " + params + " đã tồn tại.")
                return


    def hienthi_thongbao_update(self, kq, params=None):
        if params is None:
            if kq == 1:
                messagebox.showinfo("Thành công", "Sửa phiếu đăng ký thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Sửa phiếu đăng ký thất bại.")
                return
        else:
            if kq == 1:
                messagebox.showinfo("Thành công", "Sửa phiếu đăng ký " + params + " thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Sửa phiếu đăng ký " + params + " thất bại.")
                return

    def hienthi_thongbao_delete(self, kq, params=None):
        if params is None:
            if kq == 1:
                messagebox.showinfo("Thành công", "Xóa phiếu đăng ký thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Xóa phiếu đăng ký thất bại.")
                return
        else:
            if kq == 1:
                messagebox.showinfo("Thành công", "Xóa phiếu đăng ký " + params + " thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Xóa phiếu đăng ký " + params + " thất bại.")
                return

    def on_item_selected(self, event):
        self.entry_mapdk.config(state='normal')
        self.combo_makh.config(state='normal')
        self.combo_map.config(state='normal')

        selected_item = self.treeview.selection()
        if selected_item:
            values = self.treeview.item(selected_item, "values")
            item_text = self.treeview.item(selected_item, 'text')

            # Cập nhật giá trị của các Entry
            self.entry_mapdk.delete(0, tk.END)
            self.entry_mapdk.insert(0, values[1])
            self.entry_mapdk.config(state='disabled')

            self.combo_makh.delete(0, tk.END)
            self.combo_makh.set(values[2])
            self.combo_makh.config(state='disabled')

            self.combo_map.delete(0, tk.END)
            self.combo_map.set(values[3])
            self.combo_map.config(state='disabled')

            # self.cal_ngthue.delete(0, tk.END)
            self.cal_ngthue.set_date(values[4])

            # self.cal_ngtra.delete(0, tk.END)
            self.cal_ngtra.set_date(values[5])

    def insert_treeview(self, index, pdk):
        self.treeview.insert("", index=tk.END, text=".", values=(index, pdk.MAPDK, pdk.TENKH, pdk.TENPT, pdk.NGTHUE, pdk.NGTRA))


    def delete_treeview(self):
        # Xóa tất cả các mục từ TreeView và cập nhật lại danh sách hiển thị
        # print("Đã xoá dữ liệu đang hiển thị treeview")
        for item in self.treeview.get_children():
            self.treeview.delete(item)
            # print("Đã xoá dữ liệu đang hiển thị treeview")


