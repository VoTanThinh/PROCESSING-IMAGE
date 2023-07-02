import cv2 # thư viện opencv
from PIL import Image #thư viện xử lí ảnh
import numpy as np # thư viện ính toán 

# khai báo đường dẫn cho file hình
filehinh = r'lena.jpg'

# đọc ảnh màu dùng thư viện opencv hiển thị
img= cv2.imread(filehinh, cv2.IMREAD_COLOR)

#đọc ảnh màu dúng thư viện pil để tính toán thay vì opencv
imgPIL= Image.open(filehinh)



def TINHVECTO(imPIL):
    R1=0
    G1=0
    B1=0
    for i in range(80,150,1):
        for j in range(400,500,1):
            # lấy giá trị điểm ảnh tại vị trí i,j
            R, G, B = imgPIL.getpixel((i, j))
            R1+=R
            G1+=G
            B1+=B
    # tính kích thước ảnh
    size = abs(80-150)*abs(400-500)
    R1/=size
    G1/= size
    B1/=size
    return R1,G1,B1

R1,G1,B1 = TINHVECTO(imgPIL)

def HAMPHANDOANANH(imgPIL,R1,G1,B1):
    PHANDOANANH= Image.new(imgPIL.mode, imgPIL.size) # có cùng kích thước với imgPIL

    #lấy kích thước anh từ imgPIL
    width= PHANDOANANH.size[0]   #tiên biến width và size 0 là chiều ngang
    height= PHANDOANANH.size[1]   #tiên biến height và size 1 là chiều cao

    # set ngương A =45
    A=45

    #mỗi ảnh là 1 ma trân 2 chiều nên ta dùng 2 vào for
    # đọc hết các điểm pixel có trong ảnh
    for x in range(width):
        for y in range(height):
            # Lấy giá trị điểm ảnh tại các vị trí x,y
            R, G, B = imgPIL.getpixel((x, y))     #là veecto 3 phần tử RGB trả về từ hàm getpixel tại vị trí x, y

            #công thức A
            H=np.sqrt(pow((R-R1),2)+pow((G-G1),2)+pow((B-B1),2))

            if(H<A):
                Ra=255
                Ga=255
                Ba=255
            else:
                Ra=R
                Ga=G
                Ba=B



            #gán giá trị vừa tính cho ảnh mức xám
            PHANDOANANH.putpixel((x, y), (Ba, Ga, Ra)) 
    return PHANDOANANH
       


k=HAMPHANDOANANH(imgPIL,R1,G1,B1)  
#chuyển đổi ảnh từ PIL sang để hiển thị bằng openCV
U = np.array(k)     



#hiển thị ảnh dùng thư viện opennCV
cv2.imshow('ANH RBG Goc cua co gai lena',img)
cv2.imshow('Phan doan anh ', U)


#bấm phím bất kì đóng cữa sổ lại
cv2.waitKey(0)


#giải phóng bộ nhớ cấp phát cho các của sổ hiển thị
cv2.destroyAllWindows()