class ModelPhong:
    def __init__(self):
        self.ds_pt = []


    def load_data_pt_update(self):
        self.ds_pt = []
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """select * from PHONGTRO ORDER BY MAPT ASC"""
        results = conn.query(sql_query)
        self.ds_pt.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()

    def load_data_pt_treeview(self):
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """select * from PHONGTRO ORDER BY MAPT ASC"""
        results = conn.query(sql_query)
        self.ds_pt.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()

    def kiemtra_pt(self, MAPT):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            # Thực hiện một truy vấn kiem tra MAPT có bị trùng hay không
            sql_query_kiemtra = """SELECT COUNT(*) FROM PHONGTRO WHERE MAPT = ?"""
            results_kiemtra = conn.query_kiemtra(sql_query_kiemtra, (MAPT,))

            # Ngắt kết nối SQL Server
            conn.close()

            if results_kiemtra[0] > 0:
                print(f"Mã nhân viên {MAPT} đã tồn tại. Không thể thêm !")
                return 1
            else:
                return 0
        except Exception as e:
            print(e)

    def them_pt(self, MAPT, TENPT, TINHTRANG, DCHIPT, GIA=0):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng PHONGTRO
            sql_query_thempt = """INSERT INTO PHONGTRO (MAPT, TENPT, TINHTRANG, DCHIPT, GIA) VALUES (?, ?, ?, ?, ?)"""
            results_thempt = conn.query_them(sql_query_thempt, (MAPT, TENPT, TINHTRANG, DCHIPT, GIA,))

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if sql_query_thempt:
                print(f"Thêm phòng trọ {MAPT} thành công.")
                return 0
            else:
                return 1
        except Exception as e:
            print(f"Lỗi khi thêm phòng trọ {MAPT}: {e}")

    def sua_pt(self, MAPT, TENPT, TINHTRANG, DCHIPT, GIA):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng PHONGTRO
            sql_query_suapt = f"""UPDATE PHONGTRO SET TENPT=N'{TENPT}', TINHTRANG=N'{TINHTRANG}', DCHIPT=N'{DCHIPT}', GIA={GIA} WHERE MAPT ='{MAPT}'"""
            results_suapt = conn.query_sua(sql_query_suapt)

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_suapt:
                print(f"Sửa phòng trọ {MAPT} thành công.")
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Lỗi khi sửa phòng trọ {MAPT}: {e}")

    def xoa_pt(self, MAPT):

        try:

            if MAPT == "":
                return 0

            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng PHONGTRO
            sql_query_xoapt = f"""DELETE FROM PHONGTRO WHERE MAPT = '{MAPT}'"""
            results_xoapt = conn.query_sua(sql_query_xoapt)

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_xoapt:
                print(f"Xóa phòng trọ {MAPT} thành công.")
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Lỗi khi xoá phòng trọ {MAPT}: {e}")