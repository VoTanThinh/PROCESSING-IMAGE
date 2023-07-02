import cv2; # thư viện opencv
from PIL import Image; #thư viện xử lí ảnh
import numpy as np; # thư viện ính toán 
from math import *

# khai báo đường dẫn cho file hình
filehinh = r'lena.jpg'

# đọc ảnh màu dùng thư viện opencv hiển thị
img= cv2.imread(filehinh, cv2.IMREAD_COLOR)

#đọc ảnh màu dúng thư viện pil để tính toán thay vì opencv
imgPIL= Image.open(filehinh)

#tạo 1 ảnh có cùng kích thước  và mode với ảnh imgPIL
#ẢNH này chứa các kết quả chuyển đồi RGB sáng Grayscale

K= Image.new(imgPIL.mode, imgPIL.size)
M= Image.new(imgPIL.mode, imgPIL.size)
N= Image.new(imgPIL.mode, imgPIL.size)
U= Image.new(imgPIL.mode, imgPIL.size)
#lấy kích thước anh từ imgPIL
#width= A.size[0]   #tiên biến width và size 0 là chiều ngang
#height= A.size[1]   #tiên biến height và size 1 là chiều cao

width= K.size[0]   #tiên biến width và size 0 là chiều ngang
height= K.size[1]   #tiên biến height và size 1 là chiều cao


#mỗi ảnh là 1 ma trân 2 chiều nên ta dùng 2 vào for
# đọc hết các điểm pixel có trong ảnh
for x in range(width):
    for y in range(height):
        # Lấy giá trị điểm ảnh tại các vị trí x,y
        R, G, B = imgPIL.getpixel((x, y))     #là veecto 3 phần tử RGB trả về từ hàm getpixel tại vị trí x, y

        Y = np.uint8(16 + (65.738 * R + 129.0577 * G + 25.064 * B) / 256)

        Cb = np.uint8(128 - (37.945 * R)/256 - (74.494 * G)/256 + (112.439 * B) / 256)

        Cr = np.uint8(128 + (112.439 * R) / 256 - (94.154 * G) / 256 - (18.285 * B) / 256)

        K.putpixel((x, y), (Y, Y, Y))
        M.putpixel((x, y), (Cb , Cb , Cb ))
        N.putpixel((x, y), (Cr, Cr, Cr))
        U.putpixel((x, y), (Cr,Cb, Y))


                
        
        


        

#chuyển đổi ảnh từ PIL sang để hiển thị bằng openCV
Y = np.array(K) 
Cr= np.array(N)
Cb = np.array(M)
YCbCr= np.array(U)

#hiển thị ảnh dùng thư viện opennCV
#cv2.imshow('ANH RBG Goc cua co gai lena',img)
cv2.imshow('Mau Y', Y)
cv2.imshow('Mau Cr', Cr)
cv2.imshow('Mau Cb', Cb)
cv2.imshow('Mau YCbCr', YCbCr)
#bấm phím bất kì đóng cữa sổ lại
cv2.waitKey(0)


#giải phóng bộ nhớ cấp phát cho các của sổ hiển thị
cv2.destroyAllWindows()









