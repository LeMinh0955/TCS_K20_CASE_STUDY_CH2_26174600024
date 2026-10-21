ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat = float(input("Nhập công suất (W): "))
so_phut = int(input("Nhập thời gian (phút): "))
don_gia_dien_kwh = float(input("Nhập đơn giá điện (VNĐ/kWh): "))
dien_nang_kwh = cong_suat * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_dien_kwh
print(ma_phien)
print(ma_may)
print(cong_suat)
print(so_phut)
print(don_gia_dien_kwh)
print(dien_nang_kwh)
print(chi_phi)