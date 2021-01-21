import db_exceptions
import sqlalchemy as db

#Xây dựng hàm thiết lập kết nối đến csdl
#Trả về đối tượng là connection, metadata và engine
def ket_noi_den_csdl(database_server, username, password, database):
    try:
        connection_str = "mysql://{}:{}@{}/{}".format(username, password, database_server, database)
        engine = db.create_engine(connection_str)
        connection = engine.connect()
        metadata = db.MetaData()
        return connection, metadata, engine
    except:
        raise db_exceptions.DatabaseConnection("Thông tin kết nối username = {}, pass = {}, "
                                               "database = {} hoặc server ={} không đúng".format(username,
                                                                                                 password,
                                                                                                 database,
                                                                                                 database_server))
#Xây dựng hàm lấy tất cả dữ liệu của bảng sinhvien
def lay_tat_ca_du_lieu_bang_sinhvien(connection, metadata, engine):
    try:
        # Lấy đối tượng sinhvien từ bảng sinhvien trong csdl
        sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)

        # Lấy tất cả dữ liệu của bảng sinhvien - tương đương câu lênh SELECT * FROM sinhvien
        query = db.select([sinhvien])

        ResultProxy = connection.execute(query)
        ResultSet = ResultProxy.fetchall()

        return ResultSet
    except:
        raise db_exceptions.SelectError("Xảy ra lỗi trong quá trình thực hiện lấy dữ liệu")

#Hàm insert
def them_sinhvien(connection, metadata, engine,
                hovaten, namsinh, sdt):
    try:
        # Lấy đối tượng sinhvien từ bảng sinhvien trong csdl
        sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
        # Chèn 1 dòng vào bảng sinhvien
        query = db.insert(sinhvien).values(hovaten=hovaten, namsinh=namsinh,sdt = sdt)
        ResultProxy = connection.execute(query)
        # Trả về giá trị id vừa được sinh
        return ResultProxy.inserted_primary_key
    except:
        raise db_exceptions.InsertError("Xảy ra lỗi trong quá trình thực hiện thêm dữ liệu")

#Hàm update
def update_sinhvien(connection, metadata, engine, hovaten, namsinh, sdt, idsinhvien):
    try:
        sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
        query_insert = db.update(sinhvien).values(hovaten=hovaten,namsinh=namsinh,sdt=sdt).where(sinhvien.columns.idsinhvien == idsinhvien)
        ResultProxy = connection.execute(query_insert)
        return ResultProxy
    except:
        raise db_exceptions.UpdateError("Xảy ra lỗi trong quá trình thực hiện sửa dữ liệu")

#Hàm delete
def delete_sinhvien(connection, metadata, engine, idsinhvien):
    try:
        sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
        query_delete = db.delete(sinhvien).where(sinhvien.columns.idsinhvien == idsinhvien)
        ResultProxy = connection.execute(query_delete)
        return  ResultProxy
    except:
        raise db_exceptions.DeleteError("Xảy ra lỗi trong quá trình thực hiện xóa dữ liệu")