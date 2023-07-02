import cv2 # thư viện opencv
from PIL import Image #thư viện xử lí ảnh
import numpy as np # thư viện ính toán 
from math import *

# khai báo đường dẫn cho file hình
filehinh = r'lena.jpg'

# đọc ảnh màu dùng thư viện opencv hiển thị
img= cv2.imread(filehinh, cv2.IMREAD_COLOR)

#đọc ảnh màu dúng thư viện pil để tính toán thay vì opencv
imgPIL= Image.open(filehinh)

#tạo 1 ảnh có cùng kích thước  và mode với ảnh imgPIL
#ẢNH này chứa các kết quả chuyển đồi RGB sáng Grayscale
L= Image.new(imgPIL.mode, imgPIL.size)
K= Image.new(imgPIL.mode, imgPIL.size)
M= Image.new(imgPIL.mode, imgPIL.size)
P= Image.new(imgPIL.mode, imgPIL.size)
#lấy kích thước anh từ imgPIL

width= K.size[0]   #tiên biến width và size 0 là chiều ngang
height= K.size[1]   #tiên biến height và size 1 là chiều cao

#mỗi ảnh là 1 ma trân 2 chiều nên ta dùng 2 vào for
# đọc hết các điểm pixel có trong ảnh
for x in range(1,width-1):
    for y in range(1,height-1):
        #các biến chứa giá trị cộng dồn của các điểm ảnh nằm trong mặt nạ
        Rs = 0
        Gs = 0
        Bs = 0
        # tiến hành quét các điểm trên mặt nạ

        for i in range(x-1,x+2):
            for j in range(y-1,y+2):
                
                #lấy thông tin màu RGB tại các điểm trong mặt nạ
                # tại vị trí(i,j)
                R, G, B = imgPIL.getpixel((i,j))
                 #Cộng dồn tất cả điểm ảnh đó cho mỗi kênh RGB
                Rs+=R
                Gs+=G
                Bs+=B
                
        # KẾT thúc quét và cộng dồn điểm ảnh trong mặt nạ thì tính trung bình cộngcho mỗi kênh tron sách6.6-1
        # chính xác hơn là ct 6.6-2 cho từng kênh RGB
        E = 3*3  
        Rs = np.uint(Rs / E)
        Gs = np.uint(Gs / E)
        Bs = np.uint(Bs / E)
        #SET điểm ảnh đã mượt (làm mờ)vào ảnh bitmap
        
        L.putpixel((x, y), (Bs, Gs, Rs))



#mỗi ảnh là 1 ma trân 2 chiều nên ta dùng 2 vào for
# đọc hết các điểm pixel có trong ảnh
for x in range(2,width-2):
    for y in range(2,height-2):
        #các biến chứa giá trị cộng dồn của các điểm ảnh nằm trong mặt nạ
        Rs = 0
        Gs = 0
        Bs = 0
        # tiến hành quét các điểm trên mặt nạ

        for i in range(x-2,x+3):
            for j in range(y-2,y+3):
                
                #lấy thông tin màu RGB tại các điểm trong mặt nạ
                # tại vị trí(i,j)
                R, G, B = imgPIL.getpixel((i,j))
                 #Cộng dồn tất cả điểm ảnh đó cho mỗi kênh RGB
                Rs+=R
                Gs+=G
                Bs+=B
                
        # KẾT thúc quét và cộng dồn điểm ảnh trong mặt nạ thì tính trung bình cộngcho mỗi kênh tron sách6.6-1
        # chính xác hơn là ct 6.6-2 cho từng kênh RGB
        E = 5*5  
        Rs = np.uint(Rs / E)
        Gs = np.uint(Gs / E)
        Bs = np.uint(Bs / E)
        #SET điểm ảnh đã mượt (làm mờ)vào ảnh bitmap
        
        K.putpixel((x, y), (Bs, Gs, Rs))

#mỗi ảnh là 1 ma trân 2 chiều nên ta dùng 2 vào for
# đọc hết các điểm pixel có trong ảnh
for x in range(3,width-3):
    for y in range(3,height-3):
        #các biến chứa giá trị cộng dồn của các điểm ảnh nằm trong mặt nạ
        Rs = 0
        Gs = 0
        Bs = 0
        # tiến hành quét các điểm trên mặt nạ

        for i in range(x-3,x+4):
            for j in range(y-3,y+4):
                
                #lấy thông tin màu RGB tại các điểm trong mặt nạ
                # tại vị trí(i,j)
                R, G, B = imgPIL.getpixel((i,j))
                 #Cộng dồn tất cả điểm ảnh đó cho mỗi kênh RGB
                Rs+=R
                Gs+=G
                Bs+=B
                
        # KẾT thúc quét và cộng dồn điểm ảnh trong mặt nạ thì tính trung bình cộngcho mỗi kênh tron sách6.6-1
        # chính xác hơn là ct 6.6-2 cho từng kênh RGB
        E = 7*7  
        Rs = np.uint(Rs / E)
        Gs = np.uint(Gs / E)
        Bs = np.uint(Bs / E)
        #SET điểm ảnh đã mượt (làm mờ)vào ảnh bitmap
        
        M.putpixel((x, y), (Bs, Gs, Rs))
       
for x in range(4,width-4):
    for y in range(4,height-4):
        #các biến chứa giá trị cộng dồn của các điểm ảnh nằm trong mặt nạ
        Rs = 0
        Gs = 0
        Bs = 0
        # tiến hành quét các điểm trên mặt nạ

        for i in range(x-4,x+5):
            for j in range(y-4,y+5):
                
                #lấy thông tin màu RGB tại các điểm trong mặt nạ
                # tại vị trí(i,j)
                R, G, B = imgPIL.getpixel((i,j))
                 #Cộng dồn tất cả điểm ảnh đó cho mỗi kênh RGB
                Rs+=R
                Gs+=G
                Bs+=B
                
        # KẾT thúc quét và cộng dồn điểm ảnh trong mặt nạ thì tính trung bình cộngcho mỗi kênh tron sách6.6-1
        # chính xác hơn là ct 6.6-2 cho từng kênh RGB
        E = 9*9  
        Rs = np.uint(Rs / E)
        Gs = np.uint(Gs / E)
        Bs = np.uint(Bs / E)
        #SET điểm ảnh đã mượt (làm mờ)vào ảnh bitmap
        
        P.putpixel((x, y), (Bs, Gs, Rs))
       
#chuyển đổi ảnh từ PIL sang để hiển thị bằng openCV
Z = np.array(M) 
Y = np.array(K) 
X = np.array(L)
N = np.array(P)
#hiển thị ảnh dùng thư viện opennCV
#cv2.imshow('ANH RBG Goc cua co gai lena',img)
cv2.imshow('hình làm mượt ma trận 33', X)
cv2.imshow('hình làm mượt ma trận 55', Y)
cv2.imshow('hình làm mượt ma trận 77', Z)
cv2.imshow('hình làm mượt ma trận 99', N)
#bấm phím bất kì đóng cữa sổ lại
cv2.waitKey(0)


#giải phóng bộ nhớ cấp phát cho các của sổ hiển thị
cv2.destroyAllWindows()









