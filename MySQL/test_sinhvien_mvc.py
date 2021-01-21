import db_exceptions
import sinhvien_db
import sinhvien_model, sinhvien_view, sinhvien_controller


def start():
    # Khởi tạo đối tượng model
    model = sinhvien_model.SinhVienModel("localhost", "root", "root", "qlsvpxu")
    # Khởi tạo đối tượng view
    view = sinhvien_view.SinhVienView()
    # Khởi tạo controller
    controller = sinhvien_controller.SinhVienController(model, view)

    # Hiển thị tất cả dữ liệu của bảng person
    controller.show_all_sinhvien()


if __name__ == "__main__":
    start()