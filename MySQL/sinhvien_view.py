import db_exceptions
import sinhvien_db

class SinhVienView(object):

    #Hàm hiển thị tất cả dữ liệu về sinhvien
    def display_all_sinhvien(self, items):
        print("Dữ liệu về các sinh viên thu được như sau:")
        for item in items:
            print("ID: {}, họ và tên: {}, năm sinh: {}, số điện thoại: {}".format(item.idsinhvien, item.hovaten, item.namsinh, item.sdt))
        print("-----Kết thúc hiển thị dữ liệu------")

        # Hàm thông báo kết quả insert
    def ket_qua_insert(self, resultID):
        id = resultID[0]
        if id > 0:
            print("Insert thanh cong")
        else:
            print("Fail")
