import cv2; # thư viện opencv
from PIL import Image; #thư viện xử lí ảnh
import numpy as np; # thư viện ính toán 

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
H= Image.new(imgPIL.mode, imgPIL.size)
#lấy kích thước anh từ imgPIL

width= K.size[0]   #tiên biến width và size 0 là chiều ngang
height= K.size[1]   #tiên biến height và size 1 là chiều cao


#mỗi ảnh là 1 ma trân 2 chiều nên ta dùng 2 vào for
# đọc hết các điểm pixel có trong ảnh
for x in range(width):
    for y in range(height):
        # Lấy giá trị điểm ảnh tại các vị trí x,y
        R, G, B = imgPIL.getpixel((x, y))     #là veecto 3 phần tử RGB trả về từ hàm getpixel tại vị trí x, y

        #gán giá trị vừa tính cho mức xám
        K.putpixel((x, y), (R, G, 0)) 

        M.putpixel((x, y), (R, 0, B))

        N.putpixel((x, y), (0, G, B))

        MIN =min(R, G, B)
        H.putpixel((x, y), (MIN, MIN, MIN ))
        
        

#chuyển đổi ảnh từ PIL sang để hiển thị bằng openCV
Cyan = np.array(K) 
Magenta = np.array(M)
Yellow= np.array(N)
Black= np.array(H)

#hiển thị ảnh dùng thư viện opennCV
#cv2.imshow('ANH RBG Goc cua co gai lena',img)
cv2.imshow('Mau Cyan', Cyan)
cv2.imshow('Mau Magenta', Magenta)
cv2.imshow('Mau Yellow', Yellow)
cv2.imshow('Mau Black', Black)
#bấm phím bất kì đóng cữa sổ lại
cv2.waitKey(0)


#giải phóng bộ nhớ cấp phát cho các của sổ hiển thị
cv2.destroyAllWindows()









