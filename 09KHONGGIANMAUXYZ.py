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

        X =np.uint8( 0.4124564 * R + 0.3575761 * G + 0.1804375 * B)

        Y = np.uint8(0.2126729 * R + 0.7151522 * G + 0.0721750 * B)

        Z = np.uint8(0.0193339 * R + 0.1191920 * G + 0.9503041 * B )  

        K.putpixel((x, y), (X, X, X))
        M.putpixel((x, y), (Y , Y , Y ))
        N.putpixel((x, y), (Z, Z, Z))
        U.putpixel((x, y), (Z, Y, X))


                
        
        


        

#chuyển đổi ảnh từ PIL sang để hiển thị bằng openCV
X = np.array(K) 
Y = np.array(M)
Z= np.array(N)
XYZ= np.array(U)

#hiển thị ảnh dùng thư viện opennCV
#cv2.imshow('ANH RBG Goc cua co gai lena',img)
cv2.imshow('Mau X', X)
cv2.imshow('Mau Y',Y)
cv2.imshow('Mau Z', Z)
cv2.imshow('Mau ZYZ', XYZ)
#bấm phím bất kì đóng cữa sổ lại
cv2.waitKey(0)


#giải phóng bộ nhớ cấp phát cho các của sổ hiển thị
cv2.destroyAllWindows()









