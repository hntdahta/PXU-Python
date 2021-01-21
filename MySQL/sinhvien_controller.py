import db_exceptions
import sinhvien_db

class SinhVienController(object):
    #Phương thức khởi tạo
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #Phương thức hiển thị tất cả dữ liệu của bảng sinhvien
    def show_all_sinhvien(self):
        try:
            items = self.model.get_all_sinhvien()
            self.view.display_all_sinhvien(items)
        except db_exceptions.SelectError as err_msg:
            self.view.thong_bao_loi(err_msg)

    #Phương thức insert
    def them_sinhvien(self, hovaten, namsinh, sdt):
        try:
            resultID = self.model.them_sinhvien(hovaten, namsinh, sdt)
            self.view.ket_qua_insert(resultID)
        except db_exceptions.InsertError as err_msg:
            self.view.thong_bao_loi(err_msg)

    #Phương thức update
    def update_sinhvien(self, hovaten, namsinh, sdt, idsinhvien):
        try:
            self.model.update_sinhvien(hovaten,namsinh,sdt, idsinhvien)
        except db_exceptions.UpdateError as err_msg:
            self.view.thong_bao_loi(err_msg)

    #Phương thức delete
    def delete_sinhvien(self, idsinhvien):
        try:
            self.model.delete_sinhvien(idsinhvien)
        except db_exceptions.DeleteError as err_msg:
            self.view.thong_bao_loi(err_msg)