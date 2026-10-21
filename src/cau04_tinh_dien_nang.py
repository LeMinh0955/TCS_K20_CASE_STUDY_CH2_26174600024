cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000
dien_nang_kwh1 = cong_suat_w * so_phut / 60 / 1000
chi_phi_1 = dien_nang_kwh1 * don_gia_kwh
#du doan
#dien_nang_kwh1 = 0.375
#chi_phi_1 = 1125.0
print(type(dien_nang_kwh1))
print(type(chi_phi_1))
print(dien_nang_kwh1)
print(chi_phi_1)

so_phut = 60
dien_nang_kwh2 = cong_suat_w * so_phut / 60 / 1000
chi_phi_2 = dien_nang_kwh2 * don_gia_kwh
print(type(dien_nang_kwh2))
print(type(chi_phi_2))
print(dien_nang_kwh2)
print(chi_phi_2 )

#So sánh kết qua
# Khi giảm so_phut từ 90 xuống 60 (giảm 1.5 lần):
# Điện năng tiêu thụ giảm từ 0.375 kWh xuống 0.25 kWh
# Chi phí điện giảm từ 1125.0 VND xuống 750.0 VND

dien_nang_chenh_lech = dien_nang_kwh1 - dien_nang_kwh2
chi_phi_chenh_lech = chi_phi_1 - chi_phi_2
print(dien_nang_chenh_lech)
print(chi_phi_chenh_lech)
