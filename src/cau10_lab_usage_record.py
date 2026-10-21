from datetime import datetime
ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_thiet_bi = float(input("Nhập công suất thiết bị (W): "))
thoi_gian_su_dung = float(input("Nhập thời gian sử dụng (phút): "))
don_gia_dien_kwh = float(input("Nhập đơn giá điện (VNĐ/kWh): "))
dien_nang_tieu_thu_kwh = cong_suat_thiet_bi * thoi_gian_su_dung / 60 / 1000
chi_phi_tien_dien = dien_nang_tieu_thu_kwh * don_gia_dien_kwh
su_dung = (thoi_gian_su_dung > 60)
thoi_diem = datetime.now()
thoi_diem_su_dung = thoi_diem.strftime("%d/%m/%Y %H:%M:%S")

print(f"Ma phien: {ma_phien}")
print(f"May: {ma_may}")
print(f"Cong suat: {cong_suat_thiet_bi:.2f} W")
print(f"Thoi luong: {thoi_gian_su_dung} phut")
print(f"Dien nang: {dien_nang_tieu_thu_kwh:.3f} kWh")
print(f"Chi phi: {chi_phi_tien_dien:.2f} VND")
print(f"Tren 60 phut: {su_dung}")
print(f"Ghi nhan luc: {thoi_diem_su_dung}")