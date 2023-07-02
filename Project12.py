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


width= K.size[0]   #tiên biến width và size 0 là chiều ngang
height= K.size[1]   #tiên biến height và size 1 là chiều cao

matran = [[0,-1,0],[-1,4,-1],[0,-1,0]]

# quét tat ca céc diém anh
for x in range (1,width-1): # quét theo chiều ngang
    for y in range (1,height-1): # quét theo chiều dọc
        # biến chứa giá trị công dồn 
        Rs = 0
        Gs = 0
        Bs = 0
        # quét céc digm anh trong mgt ng ma traif
        for a in range (-1,2):
            for b in range (-1,2):
                 # léy thong tin mau R-G-B tai diém anh trong mgt ne tai vj tri a,b
                R,G,B = imgPIL.getpixel((x+a,y+b))
                # tinh gia trị laplaceian của các điểm ảnh
                Rs = Rs + R * matran[a+1][b+1]

                Gs = Gs +G * matran[a+1][b+1]

                Bs = Bs +B * matran[a+1][b+1]
        # lấy thông tin mau R-G-8 tai vi tri xy
        R,G,B = imgPIL.getpixel((x,y))
        # tinh gid tri céc kénh
        sharpR = R + Rs
        sharpG = G + Gs
        sharpB = B + Bs
        #Xét điều kiện 
        
        if(sharpR<0):
            sharpR = 0
        elif(sharpR>255):
            sharpR = 255
        else:
            sharpR = sharpR


        if(sharpG < 0):
            sharpG = 0
        elif (sharpG > 255):
            sharpG = 255
        else:
            sharpG = sharpG


        if (sharpB < 0):
            sharpB = 0
        elif (sharpB > 255):
            sharpB = 255
        else:
            sharpB = sharpB

        # lấy ảnh làm nét 
        K.putpixel ((x,y),(sharpB, sharpG, sharpR))
        

NET = np.array(K)
#cho hiển thị 
cv2.imshow("Anh goc", img)
cv2.imshow("Anh sac net" ,NET)

#bấm bất kỳ phím nào để đóng 
cv2.waitKey(0)

#6181 phéng b} nhé d& cép phat
cv2.destroyAllWindows()