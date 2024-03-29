
class ControllerPhieuThanhToan:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.button_them.config(command=self.them_ptt)
        self.view.button_xoa.config(command=self.xoa_ptt)
        self.view.button_sua.config(command=self.sua_ptt)
        self.view.button_lammoi.config(command=self.lammoi_ptt)
        self.view.button_tinhtien.config(command=self.tinhtien_hangthang)


        self.kiemtra_user()
        self.load_ptt()
        self.update_combobox_mapdk()


    # Hàm để cập nhật dữ liệu ComboBox MAPDK
    def update_combobox_mapdk(self):
        print("Load MAPDK vào combo")
        self.model.load_mapdk()
        self.view.combo_mapdk['values'] = [mapdk.MAPDK for mapdk in self.model.ds_mapdk]
        self.view.combo_mapdk.current(0)

    def load_ptt(self):
        print("Load PTT")
        self.model.load_data_ptt_treeview()
        for index, ptt in enumerate(self.model.ds_ptt, start=1):
            self.view.treeview.insert("", index="end", text=".", values=(index, ptt.MAPTT, ptt.MAPDK, ptt.NGTT, ptt.SOTHANG, ptt.TONGTIEN))

    def load_ptt_update(self):
        print("Load PTT sau khi có thay đổi")
        self.model.load_data_ptt_update()
        for index, ptt in enumerate(self.model.ds_ptt, start=1):
            self.view.treeview.insert("", index="end", text=".", values=(index, ptt.MAPTT, ptt.MAPDK, ptt.NGTT, ptt.SOTHANG, ptt.TONGTIEN))
            # print("Cập nhật mới treeview")

    def them_ptt(self):
        print("Thao tác thêm Phiếu thanh toán")
        kq = 1
        try:
            MAPTT = self.view.entry_maptt.get()
            MAPDK = self.view.combo_mapdk.get()
            NGTT = self.view.cal_ngtt.get_date()
            SOTHANG = self.view.combo_sothang.get()
            TONGTIEN = self.view.entry_tongtien.get()

            formatted_date_ngtt = NGTT.strftime('%Y/%m/%d')


            if MAPTT == "":
                self.view.hienthi_thongbao(kq)
                return

            # Kiểm tra MAPTT có bị trùng hay không
            kq_kiemtra = self.model.kiemtra_ptt(MAPTT)
            if kq_kiemtra == 1:
                self.view.hienthi_thongbao(kq_kiemtra, MAPTT)
            else:
                # Thêm Phiếu thanh toán bằng cách gọi hàm them_ptt
                kq_them = self.model.them_ptt(MAPTT, MAPDK, formatted_date_ngtt, SOTHANG, TONGTIEN)
                # print(kq_them)
                if kq_them == 0:
                    self.view.delete_treeview()
                    self.load_ptt_update()
                    self.view.hienthi_thongbao(kq_them, MAPTT)

                    self.lammoi_ptt()
                else:
                    self.view.hienthi_thongbao(kq_kiemtra, MAPTT)

        except Exception as e:
            self.view.hienthi_thongbao(kq)
            # self.view.messagebox.showerror("Lỗi", f"Error: {e}")
            # print("Them that bai")


    def xoa_ptt(self):
        print("Thao tác xóa Phiếu thanh toán")
        try:
            MAPTT = self.view.entry_maptt.get()

            if MAPTT == "":
                self.view.hienthi_thongbao_delete(0)
                return

            # Xoá Phiếu thanh toán bằng cách gọi hàm xoa_pdk
            kq_xoa = self.model.xoa_ptt(MAPTT)
            # print(kq_xoa)
            if kq_xoa == 1:
                self.view.delete_treeview()
                self.load_ptt_update()
                self.view.hienthi_thongbao_delete(kq_xoa, MAPTT)

                self.lammoi_ptt()
            else:
                self.view.hienthi_thongbao_delete(0)

        except Exception as e:
            self.view.hienthi_thongbao_delete(0)

    def sua_ptt(self):
        print("Thao tác sửa Phiếu thanh toán")
        try:
            MAPTT = self.view.entry_maptt.get()
            MAPDK = self.view.combo_mapdk.get()
            NGTT = self.view.cal_ngtt.get_date()
            SOTHANG = self.view.combo_sothang.get()
            TONGTIEN = self.view.entry_tongtien.get()

            if MAPTT == "":
                self.view.hienthi_thongbao_update(0)
                return

            # Sửa Phiếu thanh toán bằng cách gọi hàm sua_ptt
            kq_sua = self.model.sua_ptt(MAPTT, MAPDK, NGTT, SOTHANG, TONGTIEN)
            # print(kq_sua)
            if kq_sua == 1:
                self.view.delete_treeview()
                self.load_ptt_update()
                self.view.hienthi_thongbao_update(kq_sua, MAPTT)

                self.lammoi_ptt()
            else:
                self.view.hienthi_thongbao_update(0)

        except Exception as e:
            self.view.hienthi_thongbao_update(0)

    def lammoi_ptt(self):
        print("Thao tác làm mới")
        self.view.delete_treeview()
        self.view.entry_maptt.config(state='normal')
        self.view.entry_maptt.delete(0, 'end')
        self.view.combo_mapdk.current(0)
        self.view.cal_ngtt.set_date(None)
        self.view.combo_sothang.current(0)
        self.view.entry_tongtien.config(state='normal')
        self.view.entry_tongtien.delete(0, 'end')
        self.view.entry_tongtien.config(state='disabled')
        self.load_ptt_update()

    def kiemtra_user(self):
        if self.view.username == "admin":
            pass
        else:
            self.view.button_them.config(state='disabled')
            self.view.button_xoa.config(state='disabled')
            self.view.button_sua.config(state='disabled')
            self.view.button_tinhtien.config(state='disabled')


    def tinhtien_hangthang(self):
        tiendichvu = 0
        tienphong = 0
        tongtien = 0

        MAPDK = self.view.combo_mapdk.get()
        NGTT = self.view.cal_ngtt.get_date()
        formatted_date_ngtt = NGTT.strftime('%Y/%m/%d')
        # print(formatted_date_ngtt)
        self.model.tien_dichvu(formatted_date_ngtt, MAPDK)
        if tiendichvu > 0:
            tiendichvu = 0
        for item in self.model.ds_tiendv:
            # print(item.SM)
            # print(item.SC)
            if item.SM == 0 and item.SC == 0:
                tiendichvu = float(float(tiendichvu) + float(item.GIA))
            else:
                tiendichvu = float(tiendichvu + float((float(item.SM) - float(item.SC)) * float(item.GIA)))

        # print(tiendichvu)

        GIA = self.model.tien_phong(MAPDK)
        for item in self.model.ds_tienp:
            tienphong = float(item.GIA)
            # print(tienphong)
        tongtien = tiendichvu + tienphong
        # SC = 0
        # SM = 10
        # GIA = 1000
        # tiendichvu = (SM - SC) * GIA
        # tienphong = 1000000
        # tongtien = tienphong + tiendichvu
        self.view.hienthi_tongtien(tongtien)
