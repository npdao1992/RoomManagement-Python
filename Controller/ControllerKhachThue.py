class ControllerKhachThue:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.button_themkh.config(command=self.them_kt)
        self.view.button_xoakh.config(command=self.xoa_kt)
        self.view.button_suakh.config(command=self.sua_kt)

        self.view.button_lammoi.config(command=self.lammoi_kt)

        self.kiemtra_user()
        self.load_kt()

    def load_kt(self):
        print("Load KT")
        self.model.load_data_kt_treeview()
        for index, kt in enumerate(self.model.ds_kt, start=1):
            self.view.treeview.insert("", index="end", text=".", values=(index, kt.MAKH, kt.TENKH, kt.CMND_CCCD, kt.NGSINH, kt.GIOITINH, kt.SDT, kt.DCHI, kt.NGNGHIEP))

    def load_kt_update(self):
        print("Load KT sau khi có thay đổi")
        self.model.load_data_kt_update()
        for index, kt in enumerate(self.model.ds_kt, start=1):
            self.view.treeview.insert("", index="end", text=".", values=(index, kt.MAKH, kt.TENKH, kt.CMND_CCCD, kt.NGSINH, kt.GIOITINH, kt.SDT, kt.DCHI, kt.NGNGHIEP))
            # print("Cập nhật mới treeview")



    def them_kt(self):
        print("Thao tác thêm Khách thuê")
        kq = 1
        try:
            MAKH = self.view.entry_makh.get()
            TENKH = self.view.entry_tenkh.get()
            CMND_CCCD = self.view.entry_cmnd.get()
            NGSINH = self.view.cal_ngaysinhkh.get_date()
            GIOITINH = self.view.combo_gioitinhkh.get()
            SDT = self.view.entry_sdtkh.get()
            DCHI = self.view.entry_diachikh.get()
            NGNGHIEP = self.view.entry_nghenghiep.get()

            formatted_date_ngaysinhkh = NGSINH.strftime('%Y/%m/%d')

            if MAKH == "":
                self.view.hienthi_thongbao(kq)
                return

            # Kiểm tra MAPT có bị trùng hay không
            kq_kiemtra = self.model.kiemtra_kt(MAKH)
            if kq_kiemtra == 1:
                self.view.hienthi_thongbao(kq_kiemtra, MAKH)

            else:
                # Thêm phòng trọ bằng cách gọi hàm them_pt
                kq_them = self.model.them_kt(MAKH, TENKH, CMND_CCCD, formatted_date_ngaysinhkh, GIOITINH, SDT, DCHI, NGNGHIEP)
                if kq_them == 0:
                    self.view.delete_treeview()
                    self.load_kt_update()
                    self.view.hienthi_thongbao(kq_them, MAKH)

                    self.lammoi_kt()

            # Load lại dữ liệu sau khi thêm phòng trọ
            # self.load_nhan_vien_callback()

            # self.cap_nhat_du_lieu_treeview()

        except Exception as e:
            self.view.hienthi_thongbao(kq)
            # self.view.messagebox.showerror("Lỗi", f"Error: {e}")
            # print("Them that bai")

    def sua_kt(self):
        print("Thao tác sửa Khách thuê")
        try:
            MAKH = self.view.entry_makh.get()
            TENKH = self.view.entry_tenkh.get()
            CMND_CCCD = self.view.entry_cmnd.get()
            NGSINH = self.view.cal_ngaysinhkh.get_date()
            GIOITINH = self.view.combo_gioitinhkh.get()
            SDT = self.view.entry_sdtkh.get()
            DCHI = self.view.entry_diachikh.get()
            NGNGHIEP = self.view.entry_nghenghiep.get()


            if MAKH == "":
                self.view.hienthi_thongbao_update(0)
                return 0

            # Sửa phòng trọ bằng cách gọi hàm sua_pt
            kq_sua = self.model.sua_kt(MAKH, TENKH, CMND_CCCD, NGSINH, GIOITINH, SDT, DCHI, NGNGHIEP)
            # print(kq_sua)
            if kq_sua == 1:
                self.view.delete_treeview()
                self.load_kt_update()
                self.view.hienthi_thongbao_update(kq_sua, MAKH)

                self.lammoi_kt()
            else:
                self.view.hienthi_thongbao_update(0)

        except Exception as e:
            self.view.hienthi_thongbao_update(0)

    def xoa_kt(self):
        print("Thao tác xóa Khách thuê")
        try:
            MAKH = self.view.entry_makh.get()

            # Xoá phòng trọ bằng cách gọi hàm xoa_pt
            kq_xoa = self.model.xoa_kt(MAKH)
            # print(kq_xoa)
            if kq_xoa == 1:
                self.view.delete_treeview()
                self.load_kt_update()
                self.view.hienthi_thongbao_delete(kq_xoa, MAKH)

                self.lammoi_kt()
            else:
                self.view.hienthi_thongbao_delete(0)

        except Exception as e:
            self.view.hienthi_thongbao_delete(0)

    def lammoi_kt(self):
        print("Thao tác làm mới")
        self.view.delete_treeview()
        self.view.entry_makh.config(state='normal')
        self.view.entry_makh.delete(0, 'end')
        self.view.entry_tenkh.delete(0, 'end')
        self.view.entry_cmnd.delete(0, 'end')
        self.view.cal_ngaysinhkh.set_date(None)
        self.view.combo_gioitinhkh.current(0)
        self.view.entry_sdtkh.delete(0, 'end')
        self.view.entry_diachikh.delete(0, 'end')
        self.view.entry_nghenghiep.delete(0, 'end')
        self.load_kt_update()


    def kiemtra_user(self):
        if self.view.username == "admin":
            pass
        else:
            self.view.button_themkh.config(state='disabled')
            self.view.button_xoakh.config(state='disabled')
            self.view.button_suakh.config(state='disabled')
    # def them_kt(self):
    #     print("Thêm Khách Thuê")