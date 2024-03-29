class ModelDichVu:
    def __init__(self):
        self.ds_dv = []


    def load_data_dv_update(self):
        self.ds_dv = []
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """select * from DICHVU ORDER BY MADV ASC"""
        results = conn.query(sql_query)
        self.ds_dv.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()
    def load_data_dv_treeview(self):
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """select * from DICHVU ORDER BY MADV ASC"""
        results = conn.query(sql_query)
        self.ds_dv.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()


    def kiemtra_dv(self, MADV):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            # Thực hiện một truy vấn kiem tra MAPT có bị trùng hay không
            sql_query_kiemtra = """SELECT COUNT(*) FROM DICHVU WHERE MADV = ?"""
            results_kiemtra = conn.query_kiemtra(sql_query_kiemtra, (MADV,))

            # Ngắt kết nối SQL Server
            conn.close()

            if results_kiemtra[0] > 0:
                print(f"Mã nhân viên {MADV} đã tồn tại. Không thể thêm !")
                return 1
            else:
                return 0
        except Exception as e:
            print(e)

    def them_dv(self, MADV, TENDV, GIA=0):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng DICHVU
            sql_query_themdv = """INSERT INTO DICHVU (MADV, TENDV, GIA) VALUES (?, ?, ?)"""
            results_themdv = conn.query_them(sql_query_themdv, (MADV, TENDV, GIA))

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_themdv:
                print(f"Thêm dịch vụ {MADV} thành công.")
                return 0
            else:
                return 1
        except Exception as e:
            print(f"Lỗi khi thêm phòng trọ {MADV}: {e}")

    def xoa_dv(self, MADV):

        try:

            if MADV == "":
                return 0

            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng PHONGTRO
            sql_query_xoadv = f"""DELETE FROM DICHVU WHERE MADV = '{MADV}'"""
            results_xoadv = conn.query_sua(sql_query_xoadv)

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_xoadv:
                print(f"Xóa phòng trọ {MADV} thành công.")
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Lỗi khi xoá phòng trọ {MADV}: {e}")

    def sua_dv(self, MADV, TENDV, GIA):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng PHONGTRO
            sql_query_suadv = f"""UPDATE DICHVU SET TENDV=N'{TENDV}', GIA={GIA} WHERE MADV ='{MADV}'"""
            results_suadv = conn.query_sua(sql_query_suadv)

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_suadv:
                print(f"Sửa dịch vụ {MADV} thành công.")
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Lỗi khi sửa dịch vụ {MADV}: {e}")
