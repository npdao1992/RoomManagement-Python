class ControllerDichVu:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.button_them.config(command=self.them_dv)
        self.view.button_xoa.config(command=self.xoa_dv)
        self.view.button_sua.config(command=self.sua_dv)
        self.view.button_lammoi.config(command=self.lammoi_dv)

        self.view.button_chitiet.config(command=self.chitiet_dv)

        self.kiemtra_user()
        self.load_dv()

    def load_dv(self):
        print("Load DV")
        self.model.load_data_dv_treeview()
        for index, dv in enumerate(self.model.ds_dv, start=1):
            self.view.treeview.insert("", index="end", text=".", values=(index, dv.MADV, dv.TENDV, dv.GIA))

    def load_dv_update(self):
        print("Load DV sau khi có thay đổi")
        self.model.load_data_dv_update()
        for index, dv in enumerate(self.model.ds_dv, start=1):
            self.view.treeview.insert("", index="end", text=".",
                                      values=(index, dv.MADV, dv.TENDV, dv.GIA))
            # print("Cập nhật mới treeview")

    def them_dv(self):
        print("Thao tác thêm Dịch vụ")
        kq = 1
        try:
            MADV = self.view.entry_madv.get()
            TENDV = self.view.entry_tendv.get()
            GIA = float(self.view.entry_gia.get())

            # Kiểm tra MAPT có bị trùng hay không
            kq_kiemtra = self.model.kiemtra_dv(MADV)
            if kq_kiemtra == 1:
                self.view.hienthi_thongbao(kq_kiemtra, MADV)
            else:
                # Thêm phòng trọ bằng cách gọi hàm them_pt
                kq_them = self.model.them_dv(MADV, TENDV, GIA)
                if kq_them == 0:
                    self.view.delete_treeview()
                    self.load_dv_update()
                    self.view.hienthi_thongbao(kq_them, MADV)

                    self.lammoi_dv()



        except Exception as e:
            self.view.hienthi_thongbao(kq)
            # self.view.messagebox.showerror("Lỗi", f"Error: {e}")
            # print("Them that bai")

    def xoa_dv(self):
        print("Thao tác xóa Dịch vụ")
        try:
            MADV = self.view.entry_madv.get()

            # Xoá phòng trọ bằng cách gọi hàm xoa_pt
            kq_xoa = self.model.xoa_dv(MADV)
            # print(kq_xoa)
            if kq_xoa == 1:
                self.view.delete_treeview()
                self.load_dv_update()
                self.view.hienthi_thongbao_delete(kq_xoa, MADV)

                self.lammoi_dv()
            else:
                self.view.hienthi_thongbao_delete(0)

        except Exception as e:
            self.view.hienthi_thongbao_delete(0)


    def sua_dv(self):
        print("Thao tác sửa Dịch vụ")
        try:
            MADV = self.view.entry_madv.get()
            TENDV = self.view.entry_tendv.get()

            GIA = float(self.view.entry_gia.get())

            # Sửa phòng trọ bằng cách gọi hàm sua_pt
            kq_sua = self.model.sua_dv(MADV, TENDV, GIA)
            # print(kq_sua)
            if kq_sua == 1:
                self.view.delete_treeview()
                self.load_dv_update()
                self.view.hienthi_thongbao_update(kq_sua, MADV)

                self.lammoi_dv()
            else:
                self.view.hienthi_thongbao_update(0)

        except Exception as e:
            self.view.hienthi_thongbao_update(0)

    def lammoi_dv(self):
        print("Thao tác làm mới")
        self.view.delete_treeview()
        self.view.entry_madv.config(state='normal')
        self.view.entry_madv.delete(0, 'end')
        self.view.entry_tendv.delete(0, 'end')
        # self.view.combo.delete(0, 'end')

        self.view.entry_gia.delete(0, 'end')
        self.load_dv_update()


    def chitiet_dv(self):
        print("Thao tác gọi màn hình chi tiết Dịch vụ")
        try:
            self.view.manhinh_ctdv()
        except Exception as e:
            self.view.messagebox.showerror("Lỗi", f"Error: {e}")
            # print("Them that bai")

    def kiemtra_user(self):
        if self.view.username == "admin":
            pass
        else:
            self.view.button_them.config(state='disabled')
            self.view.button_xoa.config(state='disabled')
            self.view.button_sua.config(state='disabled')