import cv2 # thư viện opencv
from PIL import Image #thư viện xử lí ảnh
import numpy as np # thư viện ính toán 

# khai báo đường dẫn cho file hình
filehinh = r'lena.jpg'

# đọc ảnh màu dùng thư viện opencv hiển thị
img= cv2.imread(filehinh, cv2.IMREAD_COLOR)

#đọc ảnh màu dúng thư viện pil để tính toán thay vì opencv
imgPIL= Image.open(filehinh)

#tạo 1 ảnh có cùng kích thước  và mode với ảnh imgPIL
#ẢNH này chứa các kết quả chuyển đồi RGB sáng Grayscale
Average= Image.new(imgPIL.mode, imgPIL.size)
Lightness= Image.new(imgPIL.mode, imgPIL.size)
Luminance= Image.new(imgPIL.mode, imgPIL.size)
#lấy kích thước anh từ imgPIL
width= Average.size[0]   #tiên biến width và size 0 là chiều ngang
height= Average.size[1]   #tiên biến height và size 1 là chiều cao

#mỗi ảnh là 1 ma trân 2 chiều nên ta dùng 2 vào for
# đọc hết các điểm pixel có trong ảnh
for x in range(width):
    for y in range(height):
        # Lấy giá trị điểm ảnh tại các vị trí x,y
        R, G, B = imgPIL.getpixel((x, y))     #là veecto 3 phần tử RGB trả về từ hàm getpixel tại vị trí x, y




        #Công thức chuyển đổi ảnh màu RGB
        #điểm ảnh mức xám dùng phương pháp AVERAGE
        A = np.uint8((R + G + B) / 3)  #AVERAGE


        MIN =min(R, G, B)
        MAX = max(R, G, B)                      #LIGHTNESS
        L = np.uint8((MIN +MAX)/2)



        LU = np.uint8(0.2126*R + 0.7152*G +0.0722*B)    #LUMINANCE






        #gán giá trị vừa tính cho ảnh mức xám
        Average.putpixel((x, y), (A, A, A)) #ảnh gồm 3 kênh mình cho cùng giá trị A
        Lightness.putpixel((x, y), (L, L, L)) #ảnh gồm 3 kênh mình cho cùng giá trị L
        Luminance.putpixel((x, y), (LU, LU, LU)) #ảnh gồm 3 kênh mình cho cùng giá trị LU

        
#chuyển đổi ảnh từ PIL sang để hiển thị bằng openCV
A = np.array(Average)     
L = np.array(Lightness)
LU = np.array(Luminance)


#hiển thị ảnh dùng thư viện opennCV
cv2.imshow('ANH RBG Goc cua co gai lena',img)
cv2.imshow('ANH Muc XAM cua co gai lena dung Average', A)
cv2.imshow('ANH Muc XAM cua co gai lena dung Lightness', L)
cv2.imshow('ANH Muc XAM cua co gai lena dung Luminancc', LU )

#bấm phím bất kì đóng cữa sổ lại
cv2.waitKey(0)


#giải phóng bộ nhớ cấp phát cho các của sổ hiển thị
cv2.destroyAllWindows()









