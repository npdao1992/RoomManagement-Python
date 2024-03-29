
from datetime import datetime
class ControllerPhieuDangKy:
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.current_date = datetime.now().date()

        self.view.button_them.config(command=self.them_pdk)
        self.view.button_xoa.config(command=self.xoa_pdk)
        self.view.button_sua.config(command=self.sua_pdk)
        self.view.button_lammoi.config(command=self.lammoi_pdk)

        self.kiemtra_user()
        self.load_pdk()
        self.update_combobox_map()
        self.update_combobox_makh()

        self.formatted_date_ngayhientai = self.current_date.strftime('%Y/%m/%d')
        self.capnhat_tinhtrang_pt_ngtra_denhang(self.formatted_date_ngayhientai)
        self.capnhat_tinhtrang_pt_ngtra_conhang(self.formatted_date_ngayhientai)

    # Hàm để cập nhật dữ liệu ComboBox MAKH
    def update_combobox_makh(self):
        print("Load MAKH vào combo")
        nghientai = self.current_date.strftime('%Y/%m/%d')
        self.model.load_makh(nghientai)
        self.view.combo_makh['values'] = [makh.TENKH for makh in self.model.ds_makh]
        self.view.combo_makh.current(0)

    # Hàm để cập nhật dữ liệu ComboBox MAPT
    def update_combobox_map(self):
        print("Load MAPT vào combo")
        self.model.load_map()

        # for map in self.model.ds_map:
        #         print(map.MAPT)
        self.view.combo_map['values'] = [map.TENPT for map in self.model.ds_map]
        self.view.combo_map.current(0)
        # for row in self.model.ds_map:
        #     print(row.MAPT)

    def load_pdk(self):
        print("Load PDK")
        self.model.load_data_pdk_treeview()
        for index, pdk in enumerate(self.model.ds_pdk, start=1):
            self.view.treeview.insert("", index="end", text=".", values=(index, pdk.MAPDK, pdk.TENKH, pdk.TENPT, pdk.NGTHUE, pdk.NGTRA))

    def load_pdk_update(self):
        print("Load PDK sau khi có thay đổi")
        self.model.load_data_pdk_update()
        for index, pdk in enumerate(self.model.ds_pdk, start=1):
            self.view.treeview.insert("", index="end", text=".", values=(index, pdk.MAPDK, pdk.TENKH, pdk.TENPT, pdk.NGTHUE, pdk.NGTRA))
            # print("Cập nhật mới treeview")

    def capnhat_tinhtrang_pt(self, MAPT):
        print("Cập nhật tình trạng Còn trống thành Đã ở")
        self.model.capnhat_tinhtrang_pt(MAPT)

    def capnhat_tinhtrang_pt_ngtra_denhang(self, ngayhientai):
        print("Cập nhật tình trạng thành Còn trống nếu ngày trả đến hạng")
        self.model.capnhat_tinhtrang_pt_ngtra_denhang(ngayhientai)

    def capnhat_tinhtrang_pt_ngtra_conhang(self, ngayhientai):
        print("Cập nhật tình trạng thành Đã ở nếu ngày trả còn hạng")
        self.model.capnhat_tinhtrang_pt_ngtra_conhang(ngayhientai)

    def them_pdk(self):
        print("Thao tác thêm Phiếu đăng ký")
        kq = 1
        try:
            MAPDK = self.view.entry_mapdk.get()
            TENKH = self.view.combo_makh.get()
            TENPT = self.view.combo_map.get()
            NGTHUE = self.view.cal_ngthue.get_date()
            NGTRA = self.view.cal_ngtra.get_date()

            formatted_date_ngthue = NGTHUE.strftime('%Y/%m/%d')
            formatted_date_ngtra = NGTRA.strftime('%Y/%m/%d')

            # Lấy MAKH từ TENKH và MAPT từ TENPT
            MAKH = self.model.lay_MAKH(TENKH)
            MAPT = self.model.lay_MAPT(TENPT)


            if MAPDK == "":
                self.view.hienthi_thongbao(kq)
                return

            # Kiểm tra MAPDK có bị trùng hay không
            kq_kiemtra = self.model.kiemtra_pdk(MAPDK)
            if kq_kiemtra == 1:
                self.view.hienthi_thongbao(kq_kiemtra, MAPDK)
            else:
                # Thêm phiếu đăng ký bằng cách gọi hàm them_pdk
                kq_them = self.model.them_pdk(MAPDK, MAKH.MAKH, MAPT.MAPT, formatted_date_ngthue, formatted_date_ngtra)
                # print(kq_them)
                if kq_them == 0:

                    self.capnhat_tinhtrang_pt(MAPT.MAPT)

                    self.view.delete_treeview()
                    self.load_pdk_update()
                    self.view.hienthi_thongbao(kq_them, MAPDK)

                    self.lammoi_pdk()
                    self.update_combobox_map()
                    self.update_combobox_makh()
                else:
                    self.view.hienthi_thongbao(kq_kiemtra, MAPDK)

        except Exception as e:
            self.view.hienthi_thongbao(kq)
            # self.view.messagebox.showerror("Lỗi", f"Error: {e}")
            # print("Them that bai")


    def xoa_pdk(self):
        print("Thao tác xóa Phiếu đăng ký")
        try:
            MAPDK = self.view.entry_mapdk.get()

            if MAPDK == "":
                self.view.hienthi_thongbao_delete(0)
                return

            # Xoá phiếu đăng ký bằng cách gọi hàm xoa_pdk
            kq_xoa = self.model.xoa_pdk(MAPDK)
            # print(kq_xoa)
            if kq_xoa == 1:
                self.view.delete_treeview()
                self.load_pdk_update()
                self.view.hienthi_thongbao_delete(kq_xoa, MAPDK)

                self.lammoi_pdk()
                self.update_combobox_map()
                self.update_combobox_makh()
            else:
                self.view.hienthi_thongbao_delete(0)

        except Exception as e:
            self.view.hienthi_thongbao_delete(0)

    def sua_pdk(self):
        print("Thao tác sửa Phiếu đăng ký")
        try:
            MAPDK = self.view.entry_mapdk.get()
            TENKH = self.view.combo_makh.get()
            TENPT = self.view.combo_map.get()
            NGTHUE = self.view.cal_ngthue.get_date()
            NGTRA = self.view.cal_ngtra.get_date()

            # Lấy MAKH từ TENKH và MAPT từ TENPT
            MAKH = self.model.lay_MAKH(TENKH)
            MAPT = self.model.lay_MAPT(TENPT)

            if MAPDK == "":
                self.view.hienthi_thongbao_update(0)
                return

            # # Kiểm tra xem ngày có được chọn hay không
            # if NGTHUE:
            #     formatted_date_ngthue = NGTHUE.strftime('%Y-%m-%d')
            # else:
            #     formatted_date_ngthue = None
            #
            # if NGTRA:
            #     formatted_date_ngtra = NGTRA.strftime('%Y-%m-%d')
            # else:
            #     formatted_date_ngtra = None


            # Sửa phiếu đăng ký bằng cách gọi hàm sua_pdk
            kq_sua = self.model.sua_pdk(MAPDK, MAKH.MAKH, MAPT.MAPT, NGTHUE, NGTRA)
            # print(kq_sua)
            if kq_sua == 1:
                self.view.delete_treeview()
                self.load_pdk_update()
                self.view.hienthi_thongbao_update(kq_sua, MAPDK)

                self.lammoi_pdk()
                self.update_combobox_map()
                self.update_combobox_makh()
            else:
                self.view.hienthi_thongbao_update(0)

        except Exception as e:
            self.view.hienthi_thongbao_update(0)

    def lammoi_pdk(self):
        print("Thao tác làm mới")
        self.view.delete_treeview()
        self.view.entry_mapdk.config(state='normal')
        self.view.entry_mapdk.delete(0, 'end')
        # self.view.entry_makh.delete(0, 'end')
        # self.view.combo.delete(0, 'end')
        self.view.combo_makh.current(0)
        self.view.combo_map.current(0)
        self.view.cal_ngthue.set_date(None)
        self.view.cal_ngtra.set_date(None)
        self.load_pdk_update()

        self.capnhat_tinhtrang_pt_ngtra_denhang(self.formatted_date_ngayhientai)
        self.capnhat_tinhtrang_pt_ngtra_conhang(self.formatted_date_ngayhientai)

    def kiemtra_user(self):
        if self.view.username == "admin":
            pass
        else:
            self.view.button_them.config(state='disabled')
            self.view.button_xoa.config(state='disabled')
            self.view.button_sua.config(state='disabled')
