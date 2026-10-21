#du doan
#Phep tinh: ket_thuc (15g05m ngay 14/10/2026) - bat_dau (13g15m ngay 14/10/2026)
# Du doan ket qua: 1:50:00 (1 gio 50 phut)
# Du doan kieu du lieu: datetime.timedelta
from datetime import datetime
thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")
print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))
bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))

# giai thich su khac nhau
#datetime: Dai dien cho moc thoi gian cu the (nam, thang, ngay, gio, phut, giay).
#str: la chuoi ki tu van ban the hien thoi gian de hien thi.
#imedelta: Dai dien cho khoang thoi gian (do chech lech giua 2 moc datetime).