from Nguoi import Nguoi
class SinhVien(Nguoi):
    def __init__(self, name = "", address="" , ma_sv="" , nganh="" , dtb=0.0):
        super().__init__(name, address)
        self.__ma_sv = ma_sv
        self.__nganh = nganh
        if(dtb < 0):
            self.__dtb = 0.0
        elif (dtb > 10):
            self.__dtb = 10.0
        else:
            self.__dtb = dtb

    def get_dtb(self):
        return self.__dtb

    def set_dtb(self, value):
        if(self.value < 0):
            self.__dtb = 0.0
        elif (value > 10):
            self.__dtb = 10.0
        else:
            self.__dtb = value

    def get_ma_sv(self):
        return self.__ma_sv

    def set_ma_sv(self, value):
        self.__ma_sv = value

    def get_nganh(self):
        return self.__nganh

    def set_nganh(self, value):
        self.__nganh = value

    def nhan_xet(self):
        if(self.get_dtb() >= 5):
            return "dat"
        else:
            return "hong"
    
    def __str__(self):
        return super().__str__() + f" masv: {self.get_ma_sv()} nganh: {self.get_nganh()} dtb: {self.get_dtb()}"