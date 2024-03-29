
class ControllerPhong:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.button_them.config(command=self.them_pt)
        self.view.button_xoa.config(command=self.xoa_pt)
        self.view.button_sua.config(command=self.sua_pt)
        self.view.button_lammoi.config(command=self.lammoi_pt)

        self.kiemtra_user()
        self.load_pt()

    def load_pt(self):
        print("Load PT")
        self.model.load_data_pt_treeview()
        for index, pt in enumerate(self.model.ds_pt, start=1):
            self.view.treeview.insert("", index="end", text=".", values=(index, pt.MAPT, pt.TENPT, pt.TINHTRANG, pt.DCHIPT, pt.GIA))

    def load_pt_update(self):
        print("Load PT sau khi có thay đổi")
        self.model.load_data_pt_update()
        for index, pt in enumerate(self.model.ds_pt, start=1):
            self.view.treeview.insert("", index="end", text=".", values=(index, pt.MAPT, pt.TENPT, pt.TINHTRANG, pt.DCHIPT, pt.GIA))
            # print("Cập nhật mới treeview")

    def them_pt(self):
        print("Thao tác thêm Phòng Trọ")
        kq = 1
        try:
            MAPT = self.view.entry_map.get()
            TENPT = self.view.entry_tenp.get()
            TINHTRANG = self.view.combo.get()
            DCHIPT = self.view.entry_diachi.get()
            GIA = float(self.view.entry_gia.get())

            # Kiểm tra MAPT có bị trùng hay không
            kq_kiemtra = self.model.kiemtra_pt(MAPT)
            if kq_kiemtra == 1:
                self.view.hienthi_thongbao(kq_kiemtra, MAPT)
            else:
                # Thêm phòng trọ bằng cách gọi hàm them_pt
                kq_them = self.model.them_pt(MAPT, TENPT, TINHTRANG, DCHIPT, GIA)
                if kq_them == 0:
                    self.view.delete_treeview()
                    self.load_pt_update()
                    self.view.hienthi_thongbao(kq_them, MAPT)

                    self.lammoi_pt()


            # Load lại dữ liệu sau khi thêm phòng trọ
            # self.load_nhan_vien_callback()

            # self.cap_nhat_du_lieu_treeview()

        except Exception as e:
            self.view.hienthi_thongbao(kq)
            # self.view.messagebox.showerror("Lỗi", f"Error: {e}")
            # print("Them that bai")


    def xoa_pt(self):
        print("Thao tác xóa Phòng Trọ")
        try:
            MAPT = self.view.entry_map.get()

            # Xoá phòng trọ bằng cách gọi hàm xoa_pt
            kq_xoa = self.model.xoa_pt(MAPT)
            # print(kq_xoa)
            if kq_xoa == 1:
                self.view.delete_treeview()
                self.load_pt_update()
                self.view.hienthi_thongbao_delete(kq_xoa, MAPT)

                self.lammoi_pt()
            else:
                self.view.hienthi_thongbao_delete(0)

        except Exception as e:
            self.view.hienthi_thongbao_delete(0)

    def sua_pt(self):
        print("Thao tác sửa Phòng Trọ")
        try:
            MAPT = self.view.entry_map.get()
            TENPT = self.view.entry_tenp.get()
            TINHTRANG = self.view.combo.get()
            DCHIPT = self.view.entry_diachi.get()
            GIA = float(self.view.entry_gia.get())

            # Sửa phòng trọ bằng cách gọi hàm sua_pt
            kq_sua = self.model.sua_pt(MAPT, TENPT, TINHTRANG, DCHIPT, GIA)
            # print(kq_sua)
            if kq_sua == 1:
                self.view.delete_treeview()
                self.load_pt_update()
                self.view.hienthi_thongbao_update(kq_sua, MAPT)

                self.lammoi_pt()
            else:
                self.view.hienthi_thongbao_update(0)

        except Exception as e:
            self.view.hienthi_thongbao_update(0)

    def lammoi_pt(self):
        print("Thao tác làm mới")
        self.view.delete_treeview()
        self.view.entry_map.config(state='normal')
        self.view.entry_map.delete(0, 'end')
        self.view.entry_tenp.delete(0, 'end')
        # self.view.combo.delete(0, 'end')
        self.view.combo.current(0)
        self.view.entry_diachi.delete(0, 'end')
        self.view.entry_gia.delete(0, 'end')
        self.load_pt_update()

    def kiemtra_user(self):
        if self.view.username == "admin":
            pass
        else:
            self.view.button_them.config(state='disabled')
            self.view.button_xoa.config(state='disabled')
            self.view.button_sua.config(state='disabled')


