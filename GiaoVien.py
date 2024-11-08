from Nguoi import Nguoi
class GiaoVien(Nguoi):
    def __init__(self, name = "", address="" , ma_gv="" , chuyen_nganh="" , luong=0.0):
        super().__init__(name, address)
        self.__ma_gv = ma_gv
        self.__chuyen_nganh = chuyen_nganh
        if(luong < 0):
            self.__luong = 0.0
        elif (luong > 10):
            self.__luong = 10.0
        else:
            self.__luong = luong
            

    def get_luong(self):
        return self.__luong

    def set_luong(self, value):
        if(value < 0):
            self.__luong = 0.0
        elif (value > 10):
            self.__luong = 10.0
        else:
            self.__luong = value
    def get_ma_gv(self):
        return self.__ma_gv

    def set_ma_gv(self, value):
        self.__ma_gv = value

    def get_chuyen_nganh(self):
        return self.__chuyen_nganh

    def set_chuyen_nganh(self, value):
        self.__chuyen_nganh = value

    def nhan_xet(self):
        if(self.get_luong() >= 15000000):
            return "tot"
        else:
            return "hong"
    
    def __str__(self):
        return super().__str__() + f" magv: {self.get_ma_gv()} nganh: {self.get_chuyen_nganh()} dtb: {self.get_luong()}"