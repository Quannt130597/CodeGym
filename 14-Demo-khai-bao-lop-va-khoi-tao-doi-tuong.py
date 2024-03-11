# Khai báo lớp HCN
class HCN:
    # Khai báo thuộc tính chieu_dai
    chieu_dai = 0
    # Khai báo thuộc tính chieu_rong
    chieu_rong = 0
# Khai báo phương thức tinh_dien_tich
def tinh_dien_tich (self):
    # Lấy thuộc tính chieu_dai * thuộc tính chieu_rong
    # Sau đó trả về kết quả
    return self.chieu_dai * self.chieu_rong
# Tương tự phương thức trên
def tinh_chu_vi (self):
    return (self.chieu_dai + self.chieu_rong) * 2
# Khởi tạo đối tượng HCN
hcn_1 = HCN()
# Đặt giá trị cho chieu_dai
hcn_1.chieu_dai = 4
# Đặt giá trị cho chieu_rong
hcn_1.chieu_rong = 5
# Gọi phương thức tinh_dien_tich
dien_tich = hcn_1.tinh_dien_tich()
# Gọi phương thức tinh_chu_vi
chu_vi = hcn_1.tinh_chu_vi()

print ("diện tích: ", dien_tich)
print ("chu vi: ", chu_vi)

hcn_2 = HCN()
hcn_1.chieu_dai = 10
hcn_1.chieu_rong = 8
dien_tich = hcn_1.tinh_dien_tich()
chu_vi = hcn_1.tinh_chu_vi()
print ("diện tích: ", dien_tich)
print ("chu vi: ", chu_vi)