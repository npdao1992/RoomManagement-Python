class ModelLogin:
    def __init__(self):
        ...



    def kiemtra_user(self, username, password):
        from MVC.ClassConnection.ClassConnection import MSSQLConnection
        # Khai báo class kết nối
        conn = MSSQLConnection()
        # Kết nối SQL Server
        conn.connect()

        # Thực hiện một truy vấn
        sql_query = f"SELECT * FROM Users WHERE username = '{username}' AND password = '{password}'"
        results = conn.query(sql_query)

        # Ngắt kết nối SQL Server
        conn.close()

        # Nếu tồn tại người dùng có tên và mật khẩu trùng khớp
        if results:
            return True
        else:
            return False
