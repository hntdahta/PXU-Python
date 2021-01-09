from Model import Car

def startView():
    print('Ví dụ về mô hình MVC - dạng đơn giản nhất')
    key = input('Bạn có muốn xem tất cả dữ liệu không? [y/n] ')
    return key

def endView():
    print('Bye')
def showAllView(list):
    for Car in list:
        print(Car.name, '--', Car.engine, '--',Car.color)
    print('Tổng cộng có ',len(list), 'Car')