class ModelPhieuDangKy:
    def __init__(self):
        self.ds_pdk = []
        self.ds_map = []
        self.ds_makh = []

    def load_makh(self, ngayhientai):
        self.ds_makh = []
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        # sql_query = """select DISTINCT(KHACHHANG.TENKH)
        #                 from KHACHHANG LEFT JOIN  PHIEUDK ON KHACHHANG.MAKH=PHIEUDK.MAKH
        #                 WHERE (PHIEUDK.NGTRA < ?) OR (PHIEUDK.NGTRA IS NULL)
        #                 ORDER BY KHACHHANG.TENKH ASC"""
        sql_query = """SELECT DISTINCT KH.TENKH
                        from KHACHHANG KH LEFT JOIN  PHIEUDK PDK ON KH.MAKH=PDK.MAKH
                        WHERE KH.MAKH NOT IN (
                            SELECT DISTINCT MAKH
                            FROM PHIEUDK
                            WHERE NGTRA > ?
                        )"""
        results = conn.query(sql_query, (ngayhientai,))
        self.ds_makh.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()

    def load_map(self):
        self.ds_map = []
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn kiểm tra ngày trả nhỏ hơn ngày hiện tại và tình trạng phòng là Còn trống
        # sql_query = """SELECT PHONGTRO.MAPT
        #                 FROM PHONGTRO LEFT JOIN  PHIEUDK ON PHONGTRO.MAPT=PHIEUDK.MAPT
        #                 WHERE TINHTRANG = N'Còn trống' AND NGTRA < ?
        #                 ORDER BY PHONGTRO.MAPT ASC"""
        sql_query = """SELECT DISTINCT(PHONGTRO.TENPT)
                                FROM PHONGTRO LEFT JOIN  PHIEUDK ON PHONGTRO.MAPT=PHIEUDK.MAPT
                                WHERE TINHTRANG = N'Còn trống'
                                ORDER BY PHONGTRO.TENPT ASC"""
        results = conn.query(sql_query)
        self.ds_map.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()



    def load_data_pdk_update(self):
        self.ds_pdk = []
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """SELECT * 
                        FROM PHIEUDK, KHACHHANG, PHONGTRO
                        WHERE PHIEUDK.MAKH=KHACHHANG.MAKH AND PHIEUDK.MAPT=PHONGTRO.MAPT
                        ORDER BY MAPDK ASC"""
        results = conn.query(sql_query)
        self.ds_pdk.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()

    def load_data_pdk_treeview(self):
        self.ds_pdk = []
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = """SELECT * 
                        FROM PHIEUDK, KHACHHANG, PHONGTRO
                        WHERE PHIEUDK.MAKH=KHACHHANG.MAKH AND PHIEUDK.MAPT=PHONGTRO.MAPT
                        ORDER BY MAPDK ASC"""
        results = conn.query(sql_query)
        self.ds_pdk.extend(results)

        # Ngắt kết nối SQL Server
        conn.close()

    def kiemtra_pdk(self, MAPDK):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            # Thực hiện một truy vấn kiem tra MAPT có bị trùng hay không
            sql_query_kiemtra = """SELECT COUNT(*) FROM PHIEUDK WHERE MAPDK = ?"""
            results_kiemtra = conn.query_kiemtra(sql_query_kiemtra, (MAPDK,))

            # Ngắt kết nối SQL Server
            conn.close()

            if results_kiemtra[0] > 0:
                print(f"Mã Phiếu đăng ký {MAPDK} đã tồn tại. Không thể thêm !")
                return 1
            else:
                return 0
        except Exception as e:
            print(e)

    def capnhat_tinhtrang_pt(self, MAPT):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            sql_query_suapdk = f"""UPDATE PHONGTRO SET TINHTRANG=N'Đã ở' WHERE MAPT ='{MAPT}'"""
            conn.query_sua(sql_query_suapdk)
            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()
        except Exception as e:
            print(e)

    def capnhat_tinhtrang_pt_ngtra_denhang(self, ngayhientai):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            sql_query_suapdk = f"""UPDATE PHONGTRO SET TINHTRANG=N'Còn trống' 
                                    FROM PHONGTRO JOIN PHIEUDK ON PHONGTRO.MAPT = PHIEUDK.MAPT
                                    WHERE PHONGTRO.TINHTRANG=N'Đã ở' AND PHIEUDK.NGTRA < ?"""
            conn.query_sua(sql_query_suapdk, (ngayhientai,))
            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()
        except Exception as e:
            print(e)


    def capnhat_tinhtrang_pt_ngtra_conhang(self, ngayhientai):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            sql_query_suapdk = f"""UPDATE PHONGTRO SET TINHTRANG=N'Đã ở' 
                                    FROM PHONGTRO JOIN PHIEUDK ON PHONGTRO.MAPT = PHIEUDK.MAPT
                                    WHERE PHONGTRO.TINHTRANG=N'Còn trống' AND PHIEUDK.NGTRA >= ?"""
            conn.query_sua(sql_query_suapdk, (ngayhientai,))
            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()
        except Exception as e:
            print(e)

    def lay_MAKH(self, TENKH):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            sql_query_kiemtra = """SELECT DISTINCT(MAKH) FROM KHACHHANG WHERE TENKH = ? ORDER BY MAKH ASC"""
            results_kiemtra = conn.query_kiemtra(sql_query_kiemtra, (TENKH,))

            # Ngắt kết nối SQL Server
            conn.close()

            if results_kiemtra:
                return results_kiemtra
        except Exception as e:
            print(e)

    def lay_MAPT(self, TENPT):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()

            sql_query_kiemtra = """SELECT DISTINCT(MAPT) FROM PHONGTRO WHERE TENPT = ? ORDER BY MAPT ASC"""
            results_kiemtra = conn.query_kiemtra(sql_query_kiemtra, (TENPT,))

            # Ngắt kết nối SQL Server
            conn.close()

            if results_kiemtra:
                return results_kiemtra
        except Exception as e:
            print(e)

    def them_pdk(self, MAPDK, MAKH, MAPT, NGTHUE, NGTRA):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng PHIEUDK
            sql_query_thempdk = """INSERT INTO PHIEUDK (MAPDK, MAKH, MAPT, NGTHUE, NGTRA) VALUES (?, ?, ?, ?, ?)"""
            results_thempdk = conn.query_them(sql_query_thempdk, (MAPDK, MAKH, MAPT, NGTHUE, NGTRA,))

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_thempdk:
                print(f"Thêm phiếu đăng ký {MAPDK} thành công.")
                return 0
            else:
                return 1
        except Exception as e:
            print(f"Lỗi khi thêm phiếu đăng ký {MAPT}: {e}")

    def sua_pdk(self, MAPDK, MAKH, MAPT, NGTHUE, NGTRA):
        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng PHIEUDK
            sql_query_suapdk = f"""UPDATE PHIEUDK SET MAKH='{MAKH}', MAPT='{MAPT}', NGTHUE='{NGTHUE}', NGTRA='{NGTRA}' WHERE MAPDK ='{MAPDK}'"""
            # print("A")
            results_suapdk = conn.query_sua(sql_query_suapdk)
            # print(results_suapdk)
            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_suapdk:
                print(f"Sửa phiếu đăng ký {MAPDK} thành công.")
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Lỗi khi sửa phiếu đăng ký {MAPDK}: {e}")

    def xoa_pdk(self, MAPDK):

        try:
            from MVC.ClassConnection.ClassConnection import MSSQLConnection
            # Khai báo class kết nối
            conn = MSSQLConnection()
            # Kết nối SQL Server
            conn.connect()
            # print("A")

            # Thêm vào bảng PHIEUDK
            sql_query_xoapdk = f"""DELETE FROM PHIEUDK WHERE MAPDK = '{MAPDK}'"""
            results_xoapdk = conn.query_sua(sql_query_xoapdk)

            # Cập nhật xuống cơ sở dữ liệu
            conn.commit()

            # Ngắt kết nối SQL Server
            conn.close()

            if results_xoapdk:
                print(f"Xóa phiếu đăng ký {MAPDK} thành công.")
                return 1
            else:
                return 0
        except Exception as e:
            print(f"Lỗi khi xoá phòng trọ {MAPDK}: {e}")