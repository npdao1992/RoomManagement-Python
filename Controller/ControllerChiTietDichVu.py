class ControllerChiTietDichVu:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.button_them.config(command=self.them_ctdv)
        self.view.button_xoa.config(command=self.xoa_ctdv)
        self.view.button_sua.config(command=self.sua_ctdv)

        self.view.button_lammoi.config(command=self.lammoi_ctdv)

        self.kiemtra_user()
        self.load_ctdv()
        self.update_combobox_mapdk()
        self.update_combobox_tendv()


    def update_combobox_mapdk(self):
        print("Load MAPDK vào combo")
        self.model.load_mapdk()
        self.view.combo_mapdk['values'] = [mapdk.MAPDK for mapdk in self.model.ds_mapdk]
        self.view.combo_mapdk.current(0)

    # Hàm để cập nhật dữ liệu ComboBox MAPT
    def update_combobox_tendv(self):
        print("Load TENDV vào combo")
        self.model.load_tendv()
        self.view.combo_tendv['values'] = [tendv.TENDV for tendv in self.model.ds_tendv]
        self.view.combo_tendv.current(0)
        # for row in self.model.ds_map:
        #     print(row.MAPT)

    def load_ctdv(self):
        print("Load ctdv")
        self.model.load_data_ctdv_treeview()
        for index, ctdv in enumerate(self.model.ds_ctdv, start=1):
            self.view.treeview.insert("", index="end", text=".", values=(index, ctdv.MAPDK, ctdv.TENDV, ctdv.TUNGAY, ctdv.DENNGAY, ctdv.SC, ctdv.SM, ctdv.GIA))

    def load_ctdv_update(self):
        print("Load ctdv sau khi có thay đổi")
        self.model.load_data_ctdv_update()
        for index, ctdv in enumerate(self.model.ds_ctdv, start=1):
            self.view.treeview.insert("", index="end", text=".", values=(index, ctdv.MAPDK, ctdv.TENDV, ctdv.TUNGAY, ctdv.DENNGAY, ctdv.SC, ctdv.SM, ctdv.GIA))
            # print("Cập nhật mới treeview")



    def them_ctdv(self):
        print("Thao tác thêm Chi tiết dịch vụ")
        kq = 1
        try:
            MAPDK = self.view.combo_mapdk.get()
            TENDV = self.view.combo_tendv.get()
            TUNGAY = self.view.cal_tungay.get_date()
            DENNGAY = self.view.cal_denngay.get_date()
            SC = self.view.entry_socu.get()
            SM = self.view.entry_somoi.get()

            formatted_date_tungay = TUNGAY.strftime('%Y/%m/%d')
            formatted_date_denngay = DENNGAY.strftime('%Y/%m/%d')


            # Lấy MADV từ TENDV để thêm vào SQL SERVER CTDV
            MADV = self.model.lay_MADV(TENDV)
            # Kiểm tra có tồn tại chưa
            kq_kiemtra = self.model.kiemtra_ctdv(MAPDK, MADV.MADV, formatted_date_tungay, formatted_date_denngay,)
            if kq_kiemtra == 1:
                self.view.hienthi_thongbao(kq_kiemtra)

            else:
                kq_them = self.model.them_ctdv(MAPDK, MADV.MADV, formatted_date_tungay, formatted_date_denngay, SC, SM)
                if kq_them == 0:
                    self.view.delete_treeview()
                    self.load_ctdv_update()
                    self.view.hienthi_thongbao(kq_them)

                    self.lammoi_ctdv()
                else:
                    self.view.hienthi_thongbao(kq)

        except Exception as e:
            self.view.hienthi_thongbao(kq)
            # self.view.messagebox.showerror("Lỗi", f"Error: {e}")
            # print("Them that bai")

    def sua_ctdv(self):
        print("Thao tác sửa Chi tiết dịch vụ")
        try:
            MAPDK = self.view.combo_mapdk.get()
            TENDV = self.view.combo_tendv.get()
            TUNGAY = self.view.cal_tungay.get_date()
            DENNGAY = self.view.cal_denngay.get_date()
            SC = self.view.entry_socu.get()
            SM = self.view.entry_somoi.get()

            formatted_date_tungay = TUNGAY.strftime('%Y/%m/%d')
            formatted_date_denngay = DENNGAY.strftime('%Y/%m/%d')

            # Lấy MADV từ TENDV để thêm vào SQL SERVER CTDV
            MADV = self.model.lay_MADV(TENDV)

            # Kiểm tra có tồn tại chưa
            kq_kiemtra = self.model.kiemtra_ctdv(MAPDK, MADV.MADV, formatted_date_tungay, formatted_date_denngay, )
            # print("B")
            # print(kq_kiemtra)
            if kq_kiemtra == 0:
                self.view.hienthi_thongbao_update(kq_kiemtra)
            else:
                kq_sua = self.model.sua_ctdv(MAPDK, MADV.MADV, formatted_date_tungay, formatted_date_denngay, SC, SM)
                # print(kq_sua)
                if kq_sua == 1:
                    self.view.delete_treeview()
                    self.load_ctdv_update()
                    self.view.hienthi_thongbao_update(kq_sua)

                    self.lammoi_ctdv()
                else:
                    self.view.hienthi_thongbao_update(0)

        except Exception as e:
            self.view.hienthi_thongbao_update(0)

    def xoa_ctdv(self):
        print("Thao tác xóa Chi tiết dịch vụ")
        try:
            MAPDK = self.view.combo_mapdk.get()
            TENDV = self.view.combo_tendv.get()
            TUNGAY = self.view.cal_tungay.get_date()
            DENNGAY = self.view.cal_denngay.get_date()

            formatted_date_tungay = TUNGAY.strftime('%Y/%m/%d')
            formatted_date_denngay = DENNGAY.strftime('%Y/%m/%d')

            # Lấy MADV từ TENDV để thêm vào SQL SERVER CTDV
            MADV = self.model.lay_MADV(TENDV)

            # Kiểm tra có tồn tại chưa
            kq_kiemtra = self.model.kiemtra_ctdv(MAPDK, MADV.MADV, formatted_date_tungay, formatted_date_denngay)
            if kq_kiemtra == 0:
                self.view.hienthi_thongbao_delete(kq_kiemtra)
            else:
                kq_xoa = self.model.xoa_ctdv(MAPDK, MADV.MADV, formatted_date_tungay, formatted_date_denngay)
                # print(kq_xoa)
                if kq_xoa == 1:
                    self.view.delete_treeview()
                    self.load_ctdv_update()
                    self.view.hienthi_thongbao_delete(kq_xoa)

                    self.lammoi_ctdv()
                else:
                    self.view.hienthi_thongbao_delete(0)

        except Exception as e:
            self.view.hienthi_thongbao_delete(0)

    def lammoi_ctdv(self):
        print("Thao tác làm mới")
        self.view.delete_treeview()
        self.view.combo_mapdk.config(state='normal')
        self.view.combo_mapdk.current(0)
        self.view.combo_tendv.config(state='normal')
        self.view.combo_tendv.current(0)
        self.view.cal_tungay.config(state='normal')
        self.view.cal_tungay.set_date(None)
        self.view.cal_denngay.config(state='normal')
        self.view.cal_denngay.set_date(None)
        # self.view.entry_gia.config(state='normal')
        # self.view.entry_gia.delete(0, 'end')
        # self.view.entry_gia.config(state='disabled')
        self.view.entry_socu.delete(0, 'end')
        self.view.entry_somoi.delete(0, 'end')

        # for i in range(1, 3):
        #     self.view.entry_gia.config(state='disabled')
        #     if i == 3:
        #         break
        self.load_ctdv_update()
    # def them_ctdv(self):
    #     print("Thêm Chi tiết dịch vụ)

    def kiemtra_user(self):
        if self.view.username == "admin":
            # print(self.view.username)
            pass
        else:
            self.view.button_them.config(state='disabled')
            self.view.button_xoa.config(state='disabled')
            self.view.button_sua.config(state='disabled')