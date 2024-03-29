#!/usr/bin/python3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkcalendar import DateEntry
from MVC.View.IconThemXoaSuaLM import IconThemXoaSuaLM
class ViewChiTietDichVu(tk.Toplevel):
    def __init__(self, username=None):
        super().__init__()
        self.username = username

        # print("TEST username CTDV")
        # print(self.username)
        # Tạo cửa sổ
        self.title("Dịch vụ được sử dụng")

        # build ui
        self.frame_ChiTietDV = tk.Frame(master=self)
        self.frame_ChiTietDV.configure(height=600, width=1000)
        self.label_ThongTin = tk.Label(self.frame_ChiTietDV)
        self.label_ThongTin.configure(
            font="Poppins 24 bold",
            foreground="#2F1AAF",
            state="normal",
            takefocus=False,
            text='Dịch vụ được sử dụng')
        self.label_ThongTin.place(anchor="center", x=500, y=50)
        self.frame_chitiet = tk.Frame(self.frame_ChiTietDV)
        self.frame_chitiet.configure(height=985, width=370)
        self.lablel_ds = tk.Label(self.frame_chitiet)
        self.lablel_ds.configure(
            font="{Times New Roman} 22 {bold}",
            foreground="#919300",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Danh sách')
        self.lablel_ds.place(x=20, y=130)
        self.label_mapdk = tk.Label(self.frame_chitiet)
        self.label_mapdk.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#ff0000",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Mã PDK :')
        self.label_mapdk.place(x=20)
        self.label_tendv = tk.Label(self.frame_chitiet)
        self.label_tendv.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#ff0000",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Tên DV :')
        self.label_tendv.place(anchor="nw", x=20, y=30)

        # self.entry_mapdk = ttk.Entry(self.frame_chitiet)
        # self.entry_mapdk.place(anchor="nw", x=110)
        # Tạo hộp chọn Combobox MAKH
        self.combo_mapdk = ttk.Combobox(self.frame_chitiet)
        self.combo_mapdk['values'] = ()
        self.combo_mapdk.config(state="readonly")
        self.combo_mapdk.place(anchor="nw", x=110, width=125)


        # self.entry_madv = ttk.Entry(self.frame_chitiet)
        # self.entry_madv.place(anchor="nw", x=110, y=30)
        # Tạo hộp chọn Combobox MAKH
        self.combo_tendv = ttk.Combobox(self.frame_chitiet)
        self.combo_tendv['values'] = ()
        self.combo_tendv.config(state="readonly")
        self.combo_tendv.place(anchor="nw", x=110, y=30, width=125)

        self.iconThem = IconThemXoaSuaLM().iconThem()
        self.iconXoa = IconThemXoaSuaLM().iconXoa()
        self.iconSua = IconThemXoaSuaLM().iconSua()
        self.iconLM = IconThemXoaSuaLM().iconLM()
        print(self.iconThem)

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
        self.button_them.place(anchor="nw", height=30, width=80, x=645, y=80)
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
        self.button_xoa.place(anchor="nw", height=30, width=80, x=750, y=80)
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
        self.button_sua.place(anchor="nw", height=30, width=80, x=865, y=80)
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
        self.button_lammoi.place(anchor="nw", height=31, x=740, y=30)

        self.treeview = ttk.Treeview(self.frame_chitiet, columns=(
        "STT", "MAPDK", "TENDV", "TUNGAY", "DENGAY", "SC", "SM", "DONGIA"), show="headings")


        # self.scrollbar_ngang = ttk.Scrollbar(self.frame_chitiet)
        # self.scrollbar_ngang.configure(orient="horizontal")
        # self.scrollbar_ngang.place(anchor="nw", width=940, x=20, y=455)
        # self.scrollbar_doc = ttk.Scrollbar(self.frame_chitiet)
        # self.scrollbar_doc.configure(orient="vertical")
        # self.scrollbar_doc.place(anchor="nw", height=310, x=945, y=165)

        # Thêm thanh cuộn ngang
        self.scrollbar_ngang = ttk.Scrollbar(self.frame_chitiet, orient="horizontal", command=self.treeview.xview)
        self.scrollbar_ngang.place(anchor="nw", width=940, x=20, y=455)
        self.treeview.configure(xscrollcommand=self.scrollbar_ngang.set)

        # Thêm thanh cuộn dọc
        self.scrollbar_doc = ttk.Scrollbar(self.frame_chitiet, orient="vertical", command=self.treeview.yview)
        self.scrollbar_doc.place(anchor="nw", height=310, x=945, y=165)
        self.treeview.configure(xscrollcommand=self.scrollbar_doc.set)

        self.treeview.heading('STT', text='STT')
        self.treeview.heading('MAPDK', text='Mã Phiếu Đăng Ký')
        # self.treeview.heading('MADV', text='Mã Chi tiết dịch vụ')
        self.treeview.heading('TENDV', text='Tên Dịch Vụ')
        self.treeview.heading('TUNGAY', text='Từ Ngày')
        self.treeview.heading('DENGAY', text='Đến Ngày')
        self.treeview.heading('SC', text='Số Cũ')
        self.treeview.heading('SM', text='Số Mới')
        self.treeview.heading('DONGIA', text='Đơn Giá')

        self.treeview.column("STT", width=50, minwidth=50, stretch=tk.NO, anchor="center")
        self.treeview.column("MAPDK", width=150, minwidth=200, stretch=tk.NO, anchor="center")
        # self.treeview.column("MADV", width=150, minwidth=150, stretch=tk.NO)
        self.treeview.column("TENDV", width=100, minwidth=100, stretch=tk.NO, anchor="center")
        self.treeview.column("TUNGAY", width=140, minwidth=120, stretch=tk.NO, anchor="center")
        self.treeview.column("DENGAY", width=140, minwidth=120, stretch=tk.NO, anchor="center")
        self.treeview.column("SC", width=110, minwidth=80, stretch=tk.NO, anchor="center")
        self.treeview.column("SM", width=110, minwidth=80, stretch=tk.NO, anchor="center")
        self.treeview.column("DONGIA", width=150, minwidth=100, stretch=tk.NO, anchor="center")

        self.treeview.bind(sequence="<<TreeviewSelect>>", func=self.on_item_selected)
        self.treeview.place(height=300, width=940, x=20, y=170)


        self.label_tungay = tk.Label(self.frame_chitiet)
        self.label_tungay.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#ff0000",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Từ Ngày :')
        self.label_tungay.place(anchor="nw", x=20, y=60)
        self.label_dengay = tk.Label(self.frame_chitiet)
        self.label_dengay.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#ff0000",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Đến Ngày :')
        self.label_dengay.place(anchor="nw", x=270, y=60)

        self.entry_socu = ttk.Entry(self.frame_chitiet)
        self.entry_socu.place(anchor="nw", x=110, y=90)
        # self.entry_tungay = ttk.Entry(self.frame_chitiet)
        # self.entry_tungay.place(anchor="nw", x=110, y=60)
        # self.entry_dengay = ttk.Entry(self.frame_chitiet)
        # self.entry_dengay.place(anchor="nw", x=400, y=60)
        self.cal_tungay = DateEntry(self.frame_chitiet, width=12, background='darkblue', foreground='white',
                                    borderwidth=2, date_pattern='yyyy/MM/dd', state='readonly', allow_none=True)
        self.cal_tungay.place(anchor="nw", x=110, y=60, width=125)

        self.cal_denngay = DateEntry(self.frame_chitiet, width=12, background='darkblue', foreground='white',
                                   borderwidth=2, date_pattern='yyyy/MM/dd', state='readonly', allow_none=True)
        self.cal_denngay.place(anchor="nw", x=400, y=60, width=125)

        self.label_socu = tk.Label(self.frame_chitiet)
        self.label_socu.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Số Cũ :')
        self.label_socu.place(x=20, y=90)
        self.label_somoi = tk.Label(self.frame_chitiet)
        self.label_somoi.configure(
            font="{Times New Roman} 12 {bold}",
            foreground="#2F1AAF",
            relief="flat",
            state="normal",
            takefocus=True,
            text='Số Mới :')
        self.label_somoi.place(x=270, y=90)
        # self.label_gia = tk.Label(self.frame_chitiet)
        # self.label_gia.configure(
        #     font="{Times New Roman} 12 {bold}",
        #     foreground="#ff0000",
        #     relief="flat",
        #     state="normal",
        #     takefocus=True,
        #     text='Đơn Giá (VNĐ) :')
        # self.label_gia.place(x=270, y=30)
        # self.label_tendv = tk.Label(self.frame_chitiet)
        # self.label_tendv.configure(
        #     font="{Times New Roman} 12 {bold}",
        #     foreground="#ff0000",
        #     relief="flat",
        #     state="normal",
        #     takefocus=True,
        #     text='Tên DV :')
        # self.label_tendv.place(x=300, y=30)
        # self.entry_gia = ttk.Entry(self.frame_chitiet, state='disabled')
        # self.entry_gia.place(anchor="nw", x=400, y=30)
        # self.entry_tendv = ttk.Entry(self.frame_chitiet)
        # self.entry_tendv.place(anchor="nw", x=400, y=30)
        self.entry_somoi = ttk.Entry(self.frame_chitiet)
        self.entry_somoi.place(anchor="nw", x=400, y=90)
        self.frame_chitiet.place(
            anchor="nw", height=490, width=980, x=10, y=100)
        self.frame_ChiTietDV.pack(side="top")

    def test(self):
        print(self.entry_madv.get())

    def hienthi_thongbao(self, kq, params=None):
        if params is None:
            if kq == 0:
                messagebox.showinfo("Thành công", "Thêm Dịch vụ được sử dụng thành công.")
                return
            if kq == 1:
                messagebox.showerror("Lỗi", "Thêm Dịch vụ được sử dụng thất bại.")
                return
        else:
            if kq == 0:
                messagebox.showinfo("Thành công", "Thêm Dịch vụ được sử dụng " + params + " thành công.")
                return
            if kq == 1:
                messagebox.showerror("Lỗi", "Dịch vụ được sử dụng " + params + " đã tồn tại.")
                return


    def hienthi_thongbao_update(self, kq, params=None):
        if params is None:
            if kq == 1:
                messagebox.showinfo("Thành công", "Sửa Dịch vụ được sử dụng thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Sửa Dịch vụ được sử dụng thất bại.")
                return
        else:
            if kq == 1:
                messagebox.showinfo("Thành công", "Sửa Dịch vụ được sử dụng " + params + " thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Sửa Dịch vụ được sử dụng " + params + " thất bại.")
                return

    def hienthi_thongbao_delete(self, kq, params=None):
        if params is None:
            if kq == 1:
                messagebox.showinfo("Thành công", "Xóa Dịch vụ được sử dụng thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Xóa Dịch vụ được sử dụng thất bại.")
                return
        else:
            if kq == 1:
                messagebox.showinfo("Thành công", "Xóa Dịch vụ được sử dụng " + params + " thành công.")
                return
            if kq == 0:
                messagebox.showerror("Lỗi", "Xóa Dịch vụ được sử dụng " + params + " thất bại.")
                return

    def on_item_selected2(self, event):
        print("CTDV")
    def on_item_selected(self, event):
        self.combo_mapdk.config(state='normal')
        self.combo_tendv.config(state='normal')
        self.cal_tungay.config(state='normal')
        self.cal_denngay.config(state='normal')
        # self.entry_gia.config(state='normal')

        selected_item = self.treeview.selection()
        if selected_item:
            values = self.treeview.item(selected_item, "values")
            item_text = self.treeview.item(selected_item, 'text')

            # Cập nhật giá trị
            self.combo_mapdk.delete(0, tk.END)
            self.combo_mapdk.set(values[1])
            self.combo_mapdk.config(state='disabled')

            self.combo_tendv.delete(0, tk.END)
            self.combo_tendv.set(values[2])
            self.combo_tendv.config(state='disabled')

            self.cal_tungay.set_date(values[3])
            self.cal_tungay.config(state='disabled')
            self.cal_denngay.set_date(values[4])
            self.cal_denngay.config(state='disabled')

            self.entry_socu.delete(0, tk.END)
            self.entry_socu.insert(0, values[5])
            self.entry_somoi.delete(0, tk.END)
            self.entry_somoi.insert(0, values[6])

            # self.entry_gia.delete(0, tk.END)
            # self.entry_gia.insert(0, values[7])
            # self.entry_gia.config(state='disabled')

    def insert_treeview(self, index, ctdv):
        self.treeview.insert("", index=tk.END, text=".", values=(index, ctdv.MAPDK, ctdv.TENDV, ctdv.TUNGAY, ctdv.DENNGAY, ctdv.SC, ctdv.SM, ctdv.GIA))


    def delete_treeview(self):
        # Xóa tất cả các mục từ TreeView và cập nhật lại danh sách hiển thị
        # print("Đã xoá dữ liệu đang hiển thị treeview")
        for item in self.treeview.get_children():
            self.treeview.delete(item)
            # print("Đã xoá dữ liệu đang hiển thị treeview")

    # def on_item_selected_treeview(self, event):
    #     print()



