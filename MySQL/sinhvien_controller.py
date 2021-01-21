import db_exceptions
import sinhvien_db

class SinhVienController(object):
    #Phương thức khởi tạo
    def __init__(self, model, view):
        self.model = model
        self.view = view

    #Phương thức hiển thị tất cả dữ liệu của bảng sinhvien
    def show_all_sinhvien(self):
        items = self.model.get_all_sinhvien()
        self.view.display_all_sinhvien(items)

    #Phương thức insert
    def them_sinhvien(self, hovaten, namsinh, sdt):
        resultID = self.model.them_sinhvien(hovaten, namsinh, sdt)
        self.view.ket_qua_insert(resultID)

    #Phương thức update
    def update_sinhvien(self, hovaten, namsinh, sdt, idsinhvien):
        self.model.update_sinhvien(hovaten,namsinh,sdt, idsinhvien)

    #Phương thức delete
    def delete_sinhvien(self, idsinhvien):
        self.model.delete_sinhvien(idsinhvien)