from GiaoVien import GiaoVien 
from SinhVien import SinhVien

ds = []

def infor():
    for i in ds:
        print(i)

def check_ma(ma):
    for i in ds:
            if(isinstance(i , GiaoVien)):
                if(i.get_ma_gv() == ma):
                    return True
            if(isinstance(i , SinhVien)):
                if(i.get_ma_sv() == ma):
                    return True
    return False

while True:
    print("1. nhap ds sv va gv: ")
    print("2. in thong tin: ")
    print("3. tim kiem theo ma: ")
    print("4. sua thong tin theo ma: ")
    print("5. sl sv va gv: ")
    print("6. tong luong gv: ")
    print("0. thoat: ")
    
    chon = input('nhap lua chon: ')
    if(chon == '1'):
        print("1. nhap gv: ")
        print("2. nhap sv: ")
        chon = input('nhap lua chon: ')
        if(chon == '1'):
            ma_gv = input('nhap ma gv: ')
            if(not check_ma(ma_gv)):             
                name = input('nhap ten gv: ')
                address = input('nhap dia chi gv: ')
                chuyen_nganh = input('nhap chuyen nganh gv: ')
                luong = float(input('nhap luong gv: '))
                gv = GiaoVien(name , address , ma_gv , chuyen_nganh , luong)
                ds.append(gv)
            else:
                print('ma da ton tai')
        else:
            ma_sv = input('nhap ma sv: ')
            if(not check_ma(ma_sv)):
                name = input('nhap ten sv: ')
                address = input('nhap dia chi sv: ')
                nganh = input('nhap nganh sv: ')
                dtb = float(input('nhap dtb sv: '))
                sv = SinhVien(name , address , ma_sv , nganh , dtb)
                ds.append(sv)
            else:
                print('ma da ton tai')
    if(chon == '2'):
        infor()
    if(chon == '3'):
        ma = input('nhap ma: ')
        hasds = False
        tmp = None
        for i in ds:
            if(isinstance(i , GiaoVien)):
                if(i.get_ma_gv() == ma):
                    tmp = i
                    hasds = True
                    break
            if(isinstance(i , SinhVien)):
                if(i.get_ma_sv() == ma):
                    tmp = i
                    hasds = True
                    break
        if(hasds):
            print(tmp)
        else:
            print('ma khong ton tai!')
    if(chon == '4'):
        ma = input('nhap ma: ')
        ten = input('nhap ten: ')
        dia_chi = input('nhap dia_chi: ')
        hasds = False
        tmp = None
        for i in ds:
            if(isinstance(i , GiaoVien)):
                if(i.get_ma_gv() == ma):
                    hasds = True
                    chuyen_nganh = input('nhap chuyen nganh: ')
                    luong = float(input('nhap luong gv: '))
                    i.set_name(ten)
                    i.set_address(dia_chi)
                    i.set_chuyen_nganh(chuyen_nganh)
                    i.set_luong(luong)
                    tmp = i
                    break
            if(isinstance(i , SinhVien)):
                if(i.get_ma_sv() == ma):
                    hasds = True
                    nganh = input('nhap chuyen nganh: ')
                    dtb = float(input('nhap dtb gv: '))
                    i.set_name(ten)
                    i.set_address(dia_chi)
                    i.set_nganh(nganh)
                    i.set_dtb(dtb)
                    tmp = i
                    break
        if(hasds):
            print(tmp)
        else:
            print('ma khong ton tai!')
    if(chon == '5'):
        sl_sv = 0
        sl_gv = 0
        for i in ds:
            if(isinstance(i , GiaoVien)):
                sl_gv += 1
            if(isinstance(i , SinhVien)):
               sl_sv += 1
        print('sl sv: ' , sl_sv)
        print('sl gv: ' , sl_gv)
    if(chon == '6'):
        tong_luong = 0.0
        for i in ds:
            if(isinstance(i , GiaoVien)):
                tong_luong += i.get_luong()
        print('tong luong: ' , tong_luong)