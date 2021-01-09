class Car:

    def __init__(self, name, color, engine):
        self.name = name
        self.color = color
        self.engine = engine

    @classmethod
    def get_All_Car(self):
        database = [("AB","vàng", 550), ("Wave","trắng", 160), ("SH","đỏ", 460), ("Exiter","đen", 780), ("Honda","tím", 50)]
        result = []
        for idx, (name, color, engine) in enumerate(database):
            tam = Car(name, color, engine)
            result.append(tam)
        return result