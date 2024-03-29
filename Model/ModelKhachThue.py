class ModelKhachThue:
    def __init__(self):
        self.ds_kt = []

    def load_data_kt_update(self):
        self.ds_kt = []
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """select * from KHACHHANG ORDER BY MAKH ASC"""
        results = conn.query(sql_query)
        self.ds_kt.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()
    def load_data_kt_treeview(self):
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """select * from KHACHHANG ORDER BY MAKH ASC"""
        results = conn.query(sql_query)
        self.ds_kt.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()

    def kiemtra_kt(self, MAKH):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            # Thực hiện một truy vấn kiem tra MAKH có bị trùng hay không
            sql_query_kiemtra = """SELECT COUNT(*) FROM KHACHHANG WHERE MAKH = ?"""
            results_kiemtra = conn.query_kiemtra(sql_query_kiemtra, (MAKH,))

            # Ngắt kết nối SQL Server
            conn.close()

            if results_kiemtra[0] > 0:
                print(f"Mã khách thuê {MAKH} đã tồn tại. Không thể thêm !")
                return 1
            else:
                return 0
        except Exception as e:
            print(e)

    def them_kt(self, MAKH, TENKH, CMND_CCCD, NGSINH, GIOITINH, SDT, DCHI, NGNGHIEP):
        try:
            # if MAKH == "":
            #     return 0
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng KHACHHANG
            sql_query_themkt = """INSERT INTO KHACHHANG (MAKH, TENKH, CMND_CCCD, NGSINH, GIOITINH, SDT, DCHI, NGNGHIEP) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"""
            results_themkt = conn.query_them(sql_query_themkt, (MAKH, TENKH, CMND_CCCD, NGSINH, GIOITINH, SDT, DCHI, NGNGHIEP,))

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if sql_query_themkt:
                print(f"Thêm khách thuê {MAKH} thành công.")
                return 0
            else:
                return 1
        except Exception as e:
            print(f"Lỗi khi thêm khách thuê {MAKH}: {e}")

    def sua_kt(self, MAKH, TENKH, CMND_CCCD, NGSINH, GIOITINH, SDT, DCHI, NGNGHIEP):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng Khach hang
            sql_query_suakt = f"""UPDATE KHACHHANG SET TENKH=N'{TENKH}', CMND_CCCD='{CMND_CCCD}', NGSINH='{NGSINH}',GIOITINH=N'{GIOITINH}',SDT='{SDT}', DCHI=N'{DCHI}', NGNGHIEP=N'{NGNGHIEP}' WHERE MAKH ='{MAKH}'"""
            results_suakt = conn.query_sua(sql_query_suakt)

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_suakt:
                print(f"Sửa khách thuê {MAKH} thành công.")
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Lỗi khi sửa khách thuê {MAKH}: {e}")

    def xoa_kt(self, MAKH):

        try:

            if MAKH == "":
                return 0

            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng PHONGTRO
            sql_query_xoakt = f"""DELETE FROM KHACHHANG WHERE MAKH = '{MAKH}'"""
            results_xoakt = conn.query_sua(sql_query_xoakt)

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_xoakt:
                print(f"Xóa Khách thuê {MAKH} thành công.")
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Lỗi khi xoá Khách thuê {MAKH}: {e}")

