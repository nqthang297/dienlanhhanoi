import os

cats = {
    'dieu hoa': 'Sửa chữa & Bảo dưỡng Điều hòa',
    'tu lanh': 'Sửa chữa Tủ lạnh tại nhà',
    'may giat': 'Sửa chữa & Vệ sinh Máy giặt',
    'may loc nuoc': 'Sửa chữa Máy lọc nước',
    'bep tu': 'Sửa chữa Bo mạch Bếp từ'
}

base = 'assets/images'
files_by_cat = {}

for fldr in ['dieu hoa', 'tu lanh', 'may giat', 'may loc nuoc', 'bep tu']:
    p = os.path.join(base, fldr)
    files = sorted(os.listdir(p))
    files_by_cat[fldr] = files
    print(fldr, len(files))

