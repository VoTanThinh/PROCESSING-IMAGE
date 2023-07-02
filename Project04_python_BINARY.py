import cv2 # thư viện opencv
from PIL import Image #thư viện xử lí ảnh
import numpy as np     #thư viện tính toán7

# khai báo đường dẫn cho file hình
filehinh = r'lena.jpg'

# đọc ảnh màu dùng thư viện opencv hiển thị
img= cv2.imread(filehinh, cv2.IMREAD_COLOR)

#đọc ảnh màu dúng thư viện pil để thực hiện các tác vụ xử lí ảnnh và tính toán tính toán thay vì opencv
imgPIL= Image.open(filehinh)

#tạo 1 ảnh có cùng kích thước  và mode với ảnh imgPIL
    #ẢNH này chứa các kết quả chuyển đồi RGB sáng Binary
binary= Image.new(imgPIL.mode, imgPIL.size)

#lấy kích thước anh từ imgPIL
width= binary.size[0]   #tên biến width và size 0 là chiều ngang
height= binary.size[1]   #tên biến width và size 1 là chiều cao
#thiết lập giá trị ngưỡng để tính điểm ảnh nhị phân
Nguong = 130
#mỗi ảnh là 1 ma trân 2 chiều nên ta dùng 2 vào for
# đọc hết các điểm pixel có trong ảnh
for x in range(width):
    for y in range(height):
        # Lấy giá trị điểm ảnh tại các vị trí x,y
        R, G, B = imgPIL.getpixel((x, y))     #là veecto 3 phần tử RGB trả về từ hàm getpixel tại vị trí x, y

        #Công thức chuyển đổi điểm ảnh màu RGB thành
        #điểm ảnh mức xám dùng phương pháp luminace 
        gray = np.uint8(0.2126*R + 0.7152*G +0.0722*B)    #LUMINANCE

        #Xác định giá trị điểm nhị phân 
        if(gray < Nguong):
            binary.putpixel((x,y),(0,0,0)) #Xác định giá trị điểm nhị phân
        else:
            binary.putpixel((x,y),(255,255,255)) #Xác định giá trị điểm nhị phân
 

  
        
#chuyển đổi ảnh từ PIL sang để hiển thị bằng openCV
nhiphan = np.array(binary)     


#hiển thị ảnh dùng thư viện opennCV
cv2.imshow('ANH RBG Goc cua co gai lena',img)
cv2.imshow('ANH BINARY cua co gai lena', nhiphan)


#bấm phím bất kì đóng cữa sổ lại
cv2.waitKey(0)


#giải phóng bộ nhớ cấp phát cho các của sổ hiển thị
cv2.destroyAllWindows()









