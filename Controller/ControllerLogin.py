
class ControllerLogin:
    def __init__(self, view_login, model_login):
        self.view_login = view_login
        self.model_login = model_login

        self.view_login.login_button.config(command=self.kiemtra_dangnhap)

    def kiemtra_dangnhap2(self):
        pass
    def kiemtra_dangnhap(self):
        username = self.view_login.get_username()
        password = self.view_login.get_password()
        kq = self.model_login.kiemtra_user(username,password)

        self.view_login.hienthi_thongbao(kq, username)
