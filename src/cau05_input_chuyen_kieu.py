ma_may = input("Nhập mã máy: ")
cong_suat =input("Nhập công suất (W): ")
so_phut = input("Nhập thời gian (phút): ")
don_gia_dien_kwh = input("Nhập đơn giá điện (VNĐ/kWh): ")

cong_suat = float(cong_suat)
so_phut = int(so_phut)
don_gia_dien_kwh = float(don_gia_dien_kwh)

print(ma_may,type(ma_may))
print(cong_suat,type(cong_suat))
print(so_phut,type(so_phut))
print(don_gia_dien_kwh,type(don_gia_dien_kwh))

dien_nang_kwh = cong_suat * so_phut / 60 / 1000
print(dien_nang_kwh)
chi_phi = dien_nang_kwh * don_gia_dien_kwh
print(chi_phi)
