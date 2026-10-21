tong_phut = 135
cong_suat_w = 250
so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print(f"Tổng thời gian: {so_gio} giờ {so_phut_con_lai} phút")

su_dung_lau = tong_phut > 60
print(su_dung_lau)

du_lieu_hop_le = cong_suat_w > 0 and tong_phut > 0
print(du_lieu_hop_le)

kq1 = 100 + 20 * 3
kq2 = (100 + 20) * 3

print(kq1) #ket qua ra 160
print(kq2) #ket qua ra 360