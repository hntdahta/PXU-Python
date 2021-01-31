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

        item = menu()
        while item in ["1", "2", "3", "4"]:
            if item == "1":
                controller.show_all_sinhvien()
            elif item == "2":
                hoten = input("Nhập họ tên: ")
                tuoi = int(input("Nhập tuổi: "))
                sdt = input("Nhập số điện thoại: ")
                controller.them_sinhvien(hoten, tuoi, sdt)
                print("Thêm sinh viên thành công!")
            elif item =="3":
                id = int(input("Nhập id sinh viên cần cập nhật: "))
                hoten = input("Nhập họ tên: ")
                tuoi = int(input("Nhập tuổi: "))
                sdt = input("Nhập số điện thoại: ")
                controller.update_sinhvien(hoten, tuoi, sdt, id)
                print("Cập nhật sinh viên thành công!")
            elif item =="4":
                id = int(input("Nhập id sinh viên cần xóa: "))
                controller.delete_sinhvien(id)
                print("Xóa thành công!")
            item = menu()
    except db_exceptions.DatabaseConnection as err:
        print(err)

def menu():
    print("1: Hiển thị tất cả sinh viên")
    print("2: Thêm mới sinh viên")
    print("3: Cập nhật sinh viên")
    print("4: Xóa sinh viên")
    choice = input("Bạn hãy chọn các số từ 1 đến 4. Ngược lại là thoát khỏi chương trình.")
    return choice

if __name__ == "__main__":
    start()