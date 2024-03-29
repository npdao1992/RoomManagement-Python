class ModelChiTietDichVu:
    def __init__(self):
        self.ds_ctdv = []
        self.ds_mapdk = []
        self.ds_tendv = []

    def load_mapdk(self):
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """select MAPDK from PHIEUDK"""
        results = conn.query(sql_query)
        self.ds_mapdk.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()

    def load_tendv(self):
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """select TENDV from DICHVU"""
        results = conn.query(sql_query)
        self.ds_tendv.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()

    def load_data_ctdv_update(self):
        self.ds_ctdv = []
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """SELECT MAPDK,TENDV,TUNGAY,DENNGAY,SC,SM,GIA
                          FROM DICHVU , CTDV
                          WHERE DICHVU.MADV = CTDV.MADV
                          ORDER BY MAPDK ASC"""
        results = conn.query(sql_query)
        self.ds_ctdv.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()
    def load_data_ctdv_treeview(self):
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """SELECT MAPDK,TENDV,TUNGAY,DENNGAY,SC,SM,GIA
                          FROM DICHVU , CTDV
                          WHERE DICHVU.MADV = CTDV.MADV
                          ORDER BY MAPDK ASC"""
        results = conn.query(sql_query)
        self.ds_ctdv.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()

    def lay_MADV(self, TENDV):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            sql_query_kiemtra = """SELECT MADV FROM DICHVU WHERE TENDV = ? ORDER BY MADV ASC"""
            results_kiemtra = conn.query_kiemtra(sql_query_kiemtra, (TENDV,))

            # Ngắt kết nối SQL Server
            conn.close()

            if results_kiemtra:
                return results_kiemtra
        except Exception as e:
            print(e)
    def kiemtra_ctdv(self, MAPDK, MADV, TUNGAY, DENNGAY):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            # Thực hiện một truy vấn kiem tra MAKH có bị trùng hay không
            sql_query_kiemtra = """SELECT COUNT(*) FROM CTDV WHERE MAPDK = ? AND MADV = ? AND TUNGAY = ? AND DENNGAY = ?"""
            results_kiemtra = conn.query_kiemtra(sql_query_kiemtra, (MAPDK, MADV, TUNGAY, DENNGAY,))
            # print("A")
            # print(results_kiemtra[0])
            # Ngắt kết nối SQL Server
            conn.close()

            if results_kiemtra[0] > 0:
                print(f"CTDV đã tồn tại.")
                return 1
            else:
                return 0
        except Exception as e:
            print(e)

    def them_ctdv(self, MAPDK, MADV, TUNGAY, DENNGAY, SC=0, SM=0):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng CTDV
            sql_query_themctdv = """INSERT INTO CTDV (MAPDK, MADV, TUNGAY, DENNGAY, SC, SM) VALUES (?, ?, ?, ?, ?, ?)"""
            results_themctdv = conn.query_them(sql_query_themctdv, (MAPDK, MADV, TUNGAY, DENNGAY, SC, SM,))
            # print(results_themctdv)
            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_themctdv:
                print(f"Thêm CTDV thành công.")
                return 0
            else:
                return 1
        except Exception as e:
            print(f"Lỗi khi thêm CTDV : {e}")

    def sua_ctdv(self, MAPDK, MADV, TUNGAY, DENNGAY, SC, SM):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng Khach hang
            sql_query_suactdv = f"""UPDATE CTDV SET SC='{SC}',SM='{SM}' WHERE MAPDK ='{MAPDK}' AND MADV ='{MADV}' AND TUNGAY='{TUNGAY}' AND DENNGAY='{DENNGAY}'"""
            results_suactdv = conn.query_sua(sql_query_suactdv)

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_suactdv:
                print(f"Sửa CTDV thành công.")
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Lỗi khi sửa CTDV : {e}")

    def xoa_ctdv(self, MAPDK, MADV, TUNGAY, DENNGAY):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")
            # print(MAPDK)
            # print(MADV)
            # print(TUNGAY)
            # print(DENNGAY)


            sql_query_xoactdv = f"""DELETE FROM CTDV WHERE MAPDK = '{MAPDK}' AND MADV = '{MADV}' AND TUNGAY = '{TUNGAY}' AND DENNGAY = '{DENNGAY}'"""
            results_xoactdv = conn.query_sua(sql_query_xoactdv)

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_xoactdv:
                print(f"Xóa CTDV thành công.")
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Lỗi khi xoá CTDV : {e}")

