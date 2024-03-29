class ModelPhieuThanhToan:
    def __init__(self):
        self.ds_ptt = []
        self.ds_mapdk = []
        self.ds_tiendv = []
        self.ds_tienp = []

    def load_makh(self):
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """select MAPTT from PHIEUTHANHTOAN ORDER BY MAPTT ASC"""
        results = conn.query(sql_query)
        self.ds_ptt.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()

    def load_mapdk(self):
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """select MAPDK from PHIEUDK ORDER BY MAPDK ASC"""
        results = conn.query(sql_query)
        self.ds_mapdk.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()



    def load_data_ptt_update(self):
        self.ds_ptt = []
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """select * from PHIEUTHANHTOAN ORDER BY MAPTT ASC"""
        results = conn.query(sql_query)
        self.ds_ptt.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()

    def load_data_ptt_treeview(self):
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """select * from PHIEUTHANHTOAN ORDER BY MAPTT ASC"""
        results = conn.query(sql_query)
        self.ds_ptt.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()

    def kiemtra_ptt(self, MAPTT):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            # Thực hiện một truy vấn kiem tra MAPT có bị trùng hay không
            sql_query_kiemtra = """SELECT COUNT(*) FROM PHIEUTHANHTOAN WHERE MAPTT = ?"""
            results_kiemtra = conn.query_kiemtra(sql_query_kiemtra, (MAPTT,))

            # Ngắt kết nối SQL Server
            conn.close()

            if results_kiemtra[0] > 0:
                print(f"Mã Phiếu thanh toán {MAPTT} đã tồn tại. Không thể thêm !")
                return 1
            else:
                return 0
        except Exception as e:
            print(e)

    def them_ptt(self, MAPTT, MAPDK, NGTT, SOTHANG, TONGTIEN):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng PHIEUTHANHTOAN
            sql_query_themptt = """INSERT INTO PHIEUTHANHTOAN (MAPTT, MAPDK, NGTT, SOTHANG, TONGTIEN) VALUES (?, ?, ?, ?, ?)"""
            results_themptt = conn.query_them(sql_query_themptt, (MAPTT, MAPDK, NGTT, SOTHANG, TONGTIEN,))

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_themptt:
                print(f"Thêm Phiếu thanh toán {MAPTT} thành công.")
                return 0
            else:
                return 1
        except Exception as e:
            print(f"Lỗi khi thêm Phiếu thanh toán {MAPTT}: {e}")

    def sua_ptt(self, MAPTT, MAPDK, NGTT, SOTHANG, TONGTIEN):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng PHIEUTHANHTOAN
            sql_query_suaptt = f"""UPDATE PHIEUTHANHTOAN SET MAPDK='{MAPDK}', NGTT='{NGTT}', SOTHANG='{SOTHANG}', TONGTIEN='{TONGTIEN}' WHERE MAPTT ='{MAPTT}'"""
            # print("A")
            results_suaptt = conn.query_sua(sql_query_suaptt)
            # print(results_suapdk)
            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_suaptt:
                print(f"Sửa Phiếu thanh toán {MAPTT} thành công.")
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Lỗi khi sửa Phiếu thanh toán {MAPTT}: {e}")

    def xoa_ptt(self, MAPTT):

        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng PHIEUTHANHTOAN
            sql_query_xoaptt = f"""DELETE FROM PHIEUTHANHTOAN WHERE MAPTT = '{MAPTT}'"""
            results_xoaptt = conn.query_sua(sql_query_xoaptt)

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_xoaptt:
                print(f"Xóa Phiếu thanh toán {MAPTT} thành công.")
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Lỗi khi xoá phòng trọ {MAPTT}: {e}")


    def tien_dichvu(self, ngay, MAPDK):
        try:
            self.ds_tiendv = []
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            sql_query_kiemtra = f"""SELECT * 
                                    FROM CTDV, DICHVU
                                    WHERE CTDV.MADV= DICHVU.MADV AND '{ngay}' BETWEEN TUNGAY AND DENNGAY
                                     AND CTDV.MAPDK = '{MAPDK}'"""
            results_kiemtra = conn.query(sql_query_kiemtra)

            if results_kiemtra:
                self.ds_tiendv.extend(results_kiemtra)

            # Ngắt kết nối SQL Server
            conn.close()
        except Exception as e:
            print(e)

    def tien_phong(self, MAPDK):
        try:
            self.ds_tienp = []
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            sql_query_kiemtra = """SELECT DISTINCT(PHONGTRO.GIA)
                                FROM CTDV, PHIEUDK,PHONGTRO
                                WHERE CTDV.MAPDK=PHIEUDK.MAPDK AND PHIEUDK.MAPT=PHONGTRO.MAPT AND PHIEUDK.MAPDK = ?"""
            results_kiemtra = conn.query(sql_query_kiemtra, (MAPDK,))

            if results_kiemtra:
                self.ds_tienp.extend(results_kiemtra)
            # Ngắt kết nối SQL Server
            conn.close()
        except Exception as e:
            print(e)