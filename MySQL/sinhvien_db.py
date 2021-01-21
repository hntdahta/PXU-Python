import db_exceptions
import sqlalchemy as db

#Xây dựng hàm thiết lập kết nối đến csdl
#Trả về đối tượng là connection, metadata và engine
def ket_noi_den_csdl(database_server, username, password, database):
    connection_str = "mysql://{}:{}@{}/{}".format(username, password, database_server, database)
    engine = db.create_engine(connection_str)
    connection = engine.connect()
    metadata = db.MetaData()
    return connection, metadata, engine

#Xây dựng hàm lấy tất cả dữ liệu của bảng sinhvien
def lay_tat_ca_du_lieu_bang_sinhvien(connection, metadata, engine):
    # Lấy đối tượng sinhvien từ bảng sinhvien trong csdl
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)

    # Lấy tất cả dữ liệu của bảng sinhvien - tương đương câu lênh SELECT * FROM sinhvien
    query = db.select([sinhvien])

    ResultProxy = connection.execute(query)
    ResultSet = ResultProxy.fetchall()

    return ResultSet

#Hàm insert
def them_sinhvien(connection, metadata, engine,
                hovaten, namsinh, sdt):
    # Lấy đối tượng sinhvien từ bảng sinhvien trong csdl
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
    # Chèn 1 dòng vào bảng sinhvien
    query = db.insert(sinhvien).values(hovaten=hovaten, namsinh=namsinh,sdt = sdt)
    ResultProxy = connection.execute(query)
    # Trả về giá trị id vừa được sinh
    return ResultProxy.inserted_primary_key

#Hàm update
def update_sinhvien(connection, metadata, engine, hovaten, namsinh, sdt, idsinhvien):
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
    query_insert = db.update(sinhvien).values(hovaten=hovaten,namsinh=namsinh,sdt=sdt).where(sinhvien.columns.idsinhvien == idsinhvien)
    ResultProxy = connection.execute(query_insert)
    return ResultProxy

#Hàm delete
def delete_sinhvien(connection, metadata, engine, idsinhvien):
    sinhvien = db.Table('sinhvien', metadata, autoload=True, autoload_with=engine)
    query_delete = db.delete(sinhvien).where(sinhvien.columns.idsinhvien == idsinhvien)
    ResultProxy = connection.execute(query_delete)
    return  ResultProxy