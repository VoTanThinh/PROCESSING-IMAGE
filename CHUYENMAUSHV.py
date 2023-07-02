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
        t1 = ((R - G) + (R - B)) / 2

        t2 =sqrt((R - G) * (R - G) + (R - B) * (G - B))

      

        theta =acos(t1/t2)

        L=0
         
        if (B <= G):
            L=np.uint8(theta)
        else:
            L=np.uint8(360-theta*180/pi )

        
        S = np.uint8((1 - 3 *min(R, G, B)  / (R + G + B))*255)
        

        I = max(R,G,B)

        K.putpixel((x, y), (L, L, L))
        M.putpixel((x, y), (S , S , S ))
        N.putpixel((x, y), (I, I, I))
       
        U.putpixel((x, y), (I, S, L))


                
        
        


        

#chuyển đổi ảnh từ PIL sang để hiển thị bằng openCV
H = np.array(K) 
S = np.array(M)
V= np.array(N)
HSV= np.array(U)

#hiển thị ảnh dùng thư viện opennCV
#cv2.imshow('ANH RBG Goc cua co gai lena',img)
cv2.imshow('Mau H', H)
cv2.imshow('Mau S', S)
cv2.imshow('Mau V', V)
cv2.imshow('Mau HSV', HSV)
#bấm phím bất kì đóng cữa sổ lại
cv2.waitKey(0)


#giải phóng bộ nhớ cấp phát cho các của sổ hiển thị
cv2.destroyAllWindows()









