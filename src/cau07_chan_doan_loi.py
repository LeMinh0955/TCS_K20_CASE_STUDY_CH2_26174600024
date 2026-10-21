ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))
so_phut = float(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")

#LỖI 1:
# dong 5
# unsupported operand type(s) for /: 'str' and 'int'
#Nguyên nhân: Biến cong_suat_w nhận dữ liệu từ input() có kiểu chuỗi (str).
#phép tính cong_suat_w * so_phut tạo ra chuỗi lặp lại, sau đó chuỗi này
# không thể chia '/' cho số nguyên 60 được.
#Cách sửa: Thêm float() để chuyển kiểu dữ liệu: float(input("Nhập công suất W: ")) 

# LỖI 2:
# Dòng 3
#invalid literal for int() with base 10: '90.5'
#nguyên nhân: Sử dụng int() ép buộc số phút nhập vào phải là số nguyên. Khi
#người dùng nhập số phút lẻ/thập phân (ví dụ 90.5) chương trình sẽ bị lỗi.
#cách sửa: Chuyển sang ép kiểu float(): float(input("Nhập số phút: "))