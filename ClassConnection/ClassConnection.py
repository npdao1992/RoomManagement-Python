
import pyodbc

class MSSQLConnection:
    # def __init__(self, drive='SQL Server', server='DESKTOP-R6QS1C7\SQLEXPRESS', database='QLPhongTro', username='',password=''):
    def __init__(self, drive='SQL Server', server='DESKTOP-3TIVFAT', database='QLPT', username='',password=''):
        self.drive=drive
        self.server = server
        self.database = database
        self.username=username
        self.password=password
        self.connection=None
        self.cursor = None

    def connect(self):
        try:
            self.connection = pyodbc.connect(f'DRIVER={self.drive};'
                                             f'SERVER={self.server};'
                                             f'DATABASE={self.database};'
                                             f'UID={self.username};'
                                             f'PWD={self.password}')
            print("connect")
        except Exception as e:
            print("errol", e)


    def query(self, sql, params=None):
        try:
            if params is None:
                cursor = self.connection.cursor()
                cursor.execute(sql)
                return cursor.fetchall()
            else:
                cursor = self.connection.cursor()
                cursor.execute(sql, params)
                return cursor.fetchall()
        except Exception as e:
            print("errol", e)

    def query_them(self, sql, params=None):
        try:
            if params is None:
                cursor = self.connection.cursor()
                cursor.execute(sql)
                return cursor
            else:
                cursor = self.connection.cursor()
                cursor.execute(sql, params)
                return cursor
        except Exception as e:
            print("errol", e)

    def query_sua(self, sql, params=None):
        try:
            if params is None:
                cursor = self.connection.cursor()
                cursor.execute(sql)
                return cursor
            else:
                cursor = self.connection.cursor()
                cursor.execute(sql, params)
                return cursor
        except Exception as e:
            print("errol", e)

    def query_kiemtra(self, sql, params=None):
        try:
            if params is None:
                cursor = self.connection.cursor()
                cursor.execute(sql)
                return cursor.fetchone()
            else:
                cursor = self.connection.cursor()
                cursor.execute(sql, params)
                return cursor.fetchone()
        except Exception as e:
            print("errol", e)

    def close(self):
        if self.connection:
            self.connection.close()
            print("connection closed")

    def commit(self):
        if self.connection:
            self.connection.commit()
            print("Cập nhật dữ liệu vào SQL Server thành công")

# #sử dụng class
# conn = MSSQLConnection()
# conn.connect()
#
#
# username = 'admin'
# password = '123'
#
# ds = []
# #ví dụ truy vấn
# sql_query = f"SELECT * FROM Users WHERE username = '{username}' AND password = '{password}'"
# results = conn.query(sql_query)
#
# ds.extend(results)
# for row in ds:
#     print(row.password)
# # for row in results:
# #     print(row.MaNhanVien)
# conn.close()