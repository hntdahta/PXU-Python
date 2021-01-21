import db_exceptions
import sinhvien_db
import sinhvien_model, sinhvien_view, sinhvien_controller

def start():
    #Khởi tạo đối tượng model
    try:
        model = sinhvien_model.SinhVienModel("localhost", "root", "root", "qlsvpxu")
        #Khởi tạo đối tượng view
        view = sinhvien_view.SinhVienView()
        #Khởi tạo controller
        controller = sinhvien_controller.SinhVienController(model, view)

        #Them Tuan Anh vao csdl
        controller.them_sinhvien("Tuan", 23, "65656116")

        #Cập nhật csdl
        controller.update_sinhvien("Dat", 1996, "232315454", 2)

        #Xóa csdl
        controller.delete_sinhvien(2)

        #Hiển thị tất cả dữ liệu của bảng sinhvien
        controller.show_all_sinhvien()
    except db_exceptions.DatabaseConnection as err:
        print(err)

if __name__ == "__main__":
    start()