#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from MVC.View.IconThemXoaSuaLM import IconThemXoaSuaLM

class ViewPhong():
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
        # self.treeview = ttk.Treeview(self.frame_chitiet)
        # self.treeview.configure(selectmode="extended", columns=('STT', 'MAPT', 'TENPT', 'TINHTRANG', 'DCHIPT', 'GIA'),show=["headings"])
        self.treeview = ttk.Treeview(self.frame_chitiet, columns=("STT", "MAPT", "TENPT", "TINHTRANG", "DCHIPT", "GIA"),
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

        # self.treeview = ttk.Treeview(columns=('', 'MaNV', 'HoTen', 'LuongCoBan', 'LuongHangThang'),
        #                              show=["headings"])
        self.treeview.heading('STT', text='STT')
        self.treeview.heading('MAPT', text='Mã Phòng')
        self.treeview.heading('TENPT', text='Tên Phòng')
        self.treeview.heading('TINHTRANG', text='Tình Trạng')
        self.treeview.heading('DCHIPT', text='Địa Chỉ')
        self.treeview.heading('GIA', text='Giá')
        # self.treeview.grid(row=7, column=0, columnspan=5)

        self.treeview.column("STT", width=50, minwidth=50, stretch=tk.NO, anchor="center")
        self.treeview.column("MAPT", width=100, minwidth=100, stretch=tk.NO, anchor="center")
        self.treeview.column("TENPT", width=100, minwidth=100, stretch=tk.NO, anchor="center")
        self.treeview.column("TINHTRANG", width=100, minwidth=100, stretch=tk.NO, anchor="center")
        self.treeview.column("DCHIPT", width=180, minwidth=180, stretch=tk.NO, anchor="center")
        # self.treeview.column("GIA", width=150, minwidth=150, stretch=tk.NO)

        self.treeview.bind(sequence="<<TreeviewSelect>>", func=self.on_item_selected)
        self.treeview.place(height=350, width=680, x=20, y=50)


        self.label_map = tk.Label(self.frame_chitiet)
        self.label_map.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#ff0000",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Mã phòng :')
        self.label_map.place(x=720, y=50)
        self.label_tenp = tk.Label(self.frame_chitiet)
        self.label_tenp.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Tên phòng :')
        self.label_tenp.place(anchor="nw", x=720, y=80)
        self.label_tinhtrang = tk.Label(self.frame_chitiet)
        self.label_tinhtrang.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Tình trạng :')
        self.label_tinhtrang.place(anchor="nw", x=720, y=110)
        self.label_diachi = tk.Label(self.frame_chitiet)
        self.label_diachi.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Địa chỉ :')
        self.label_diachi.place(anchor="nw", x=720, y=140)
        self.label_gia = tk.Label(self.frame_chitiet)
        self.label_gia.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Giá (VNĐ):')
        self.label_gia.place(anchor="nw", x=720, y=170)
        self.entry_map = tk.Entry(self.frame_chitiet)
        self.entry_map.place(anchor="nw", x=850, y=50)
        self.entry_tenp = tk.Entry(self.frame_chitiet)
        self.entry_tenp.place(anchor="nw", x=850, y=80)

        # self.entry_tinhtrang = tk.Entry(self.frame_chitiet)
        # self.entry_tinhtrang.place(anchor="nw", x=850, y=110)

        # Biến để lưu trạng thái của Radiobutton
        # self.var_loai = tk.StringVar()
        #
        # self.radiobutton_ct = tk.Radiobutton(self.frame_chitiet)
        # self.radiobutton_ct.configure(text="Còn trống", variable=self.var_loai, value="Còn trống")
        # self.radiobutton_ct.place(anchor="nw", x=845, y=110)
        # self.radiobutton_do = tk.Radiobutton(self.frame_chitiet)
        # self.radiobutton_do.configure(text="Đã ở", variable=self.var_loai, value="Đã ở")
        # self.radiobutton_do.place(anchor="nw", x=925, y=110)

        # Thiết lập giá trị mặc định cho biến StringVar
        # self.var_loai.set("Còn trống")

        # self.check_ct = tk.BooleanVar()
        # self.checkbutton_ct = tk.Checkbutton(self.frame_chitiet, text="Còn trống", variable=self.check_ct)
        # self.checkbutton_ct.place(anchor="nw", x=845, y=110)
        #
        # self.check_do = tk.BooleanVar()
        # self.checkbutton_do = tk.Checkbutton(self.frame_chitiet, text="Đã ở", variable=self.check_do)
        # self.checkbutton_do.place(anchor="nw", x=925, y=110)

        # Tạo hộp chọn Combobox
        self.combo = ttk.Combobox(self.frame_chitiet)
        # Các giá trị của hộp chọn
        self.combo['values'] = ("Còn trống", "Đã ở", "Đang sửa chữa")
        # Thiết lập giá trị được chọn
        self.combo.current(0)
        self.combo.config(state="readonly")
        self.combo.place(anchor="nw", x=850, y=110, width=125)


        self.entry_diachi = tk.Entry(self.frame_chitiet)
        self.entry_diachi.place(anchor="nw", x=850, y=140)
        self.entry_gia = tk.Entry(self.frame_chitiet)
        self.entry_gia.place(anchor="nw", x=850, y=170)

        # # Mở ảnh sử dụng PIL
        # image_path = "View/images/icon-them.jpg"
        # image = Image.open(image_path)
        # image = image.resize((32, 32), Image.BILINEAR)
        # # Chuyển đổi ảnh thành định dạng phù hợp cho Tkinter
        # self.tk_image = ImageTk.PhotoImage(image)

        # self.icon_them = ImageTk.PhotoImage(Image.open("View/images/icon-them1.png"))
        # self.icon_xoa = ImageTk.PhotoImage(Image.open("View/images/icon-them1.png"))
        # self.icon_sua = ImageTk.PhotoImage(Image.open("View/images/icon-them1.png"))

        self.iconThem = IconThemXoaSuaLM().iconThem()
        self.iconXoa = IconThemXoaSuaLM().iconXoa()
        self.iconSua = IconThemXoaSuaLM().iconSua()
        self.iconLM = IconThemXoaSuaLM().iconLM()


        self.button_them = tk.Button(self.frame_chitiet)
        self.button_them.configure(
            # background="#2f4454",
            # font="{Times New Roman} 12 {bold}",
            # foreground="#ffffff",
            borderwidth=0,
            highlightthickness=0,
            # text='Thêm',
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

        # self.buttons = {
        #     "Load": tk.Button(self.frame_chitiet, text="Load")
        # }
        # self.buttons["Load"].grid(row=9, column=1, padx=10)

        self.frame_chitiet.place(
            anchor="nw", height=420, width=985, x=10, y=220)

    def test(self):
        print(self.entry_map.get())

    def hienthi_thongbao(self, kq, params=None):
        if params is None:
            if kq == 0:
                messagebox.showinfo("Thành công", "Thêm phòng trọ thành công.")
                return
            if kq == 1:
                messagebox.showerror("Lỗi", "Thêm phòng trọ thất bại.")
                return
        else:
            if kq == 0:
                messagebox.showinfo("Thành công", "Thêm phòng trọ " + params + " thành công.")
                return
            if kq == 1:
                messagebox.showerror("Lỗi", "Mã phòng trọ " + params + " đã tồn tại.")
                return


    def hienthi_thongbao_update(self, kq, params=None):
        if params is None:
            if kq == 1:
                messagebox.showinfo("Thành công", "Sửa phòng trọ thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Sửa phòng trọ thất bại.")
                return
        else:
            if kq == 1:
                messagebox.showinfo("Thành công", "Sửa phòng trọ " + params + " thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Sửa phòng trọ " + params + " thất bại.")
                return

    def hienthi_thongbao_delete(self, kq, params=None):
        if params is None:
            if kq == 1:
                messagebox.showinfo("Thành công", "Xóa phòng trọ thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Xóa phòng trọ thất bại.")
                return
        else:
            if kq == 1:
                messagebox.showinfo("Thành công", "Xóa phòng trọ " + params + " thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Xóa phòng trọ " + params + " thất bại.")
                return

    def on_item_selected(self, event):
        self.entry_map.config(state='normal')
        selected_item = self.treeview.selection()
        if selected_item:
            values = self.treeview.item(selected_item, "values")
            item_text = self.treeview.item(selected_item, 'text')

            # Cập nhật giá trị của các Entry
            self.entry_map.delete(0, tk.END)
            self.entry_map.insert(0, values[1])
            self.entry_map.config(state='disabled')

            self.entry_tenp.delete(0, tk.END)
            self.entry_tenp.insert(0, values[2])

            # self.entry_tinhtrang.delete(0, tk.END)
            # self.entry_tinhtrang.insert(0, values[3])
            self.combo.delete(0, tk.END)
            # self.combo.insert(0,values[3])
            self.combo.set(values[3])

            self.entry_diachi.delete(0, tk.END)
            self.entry_diachi.insert(0, values[4])

            self.entry_gia.delete(0, tk.END)
            self.entry_gia.insert(0, values[5])

    def insert_treeview(self, index, pt):
        self.treeview.insert("", index=tk.END, text=".", values=(index, pt.MAPT, pt.TENPT, pt.TINHTRANG, pt.DCHIPT, pt.GIA))


    def delete_treeview(self):
        # Xóa tất cả các mục từ TreeView và cập nhật lại danh sách hiển thị
        # print("Đã xoá dữ liệu đang hiển thị treeview")
        for item in self.treeview.get_children():
            self.treeview.delete(item)
            # print("Đã xoá dữ liệu đang hiển thị treeview")


