import cv2 # thư viện opencv
from PIL import Image #thư viện xử lí ảnh
import numpy as np # thư viện ính toán 

# khai báo đường dẫn cho file hình
filehinh = r'lena.jpg'

# đọc ảnh màu dùng thư viện opencv hiển thị
img= cv2.imread(filehinh, cv2.IMREAD_COLOR)

#đọc ảnh màu dúng  opencv
Hinhgoc= Image.open(filehinh)

# viết hàm chuyern đổi múc xám
def CHUYENDOIANHMUCXAM(Hinhgoc):
    #tạo ảnh có cùng kích thước với hình gốc
    Average= Image.new(Hinhgoc.mode, Hinhgoc.size)

    # lấy kích thước ảnh
    width= Hinhgoc.size[0]   #tiên biến width và size 0 là chiều ngang
    height= Hinhgoc.size[1]   #tiên biến height và size 1 là chiều cao

    for x in range(width):
        for y in range(height):
            # Lấy giá trị điểm ảnh tại các vị trí x,y
            R, G, B = Hinhgoc.getpixel((x, y))     #là veecto 3 phần tử RGB trả về từ hàm getpixel tại vị trí x, y
            #điểm ảnh mức xám dùng phương pháp AVERAGE
            A = np.uint8((R + G + B) / 3)  #AVERAGE
            Average.putpixel((x, y), (A, A, A)) #ảnh gồm 3 kênh mình cho cùng giá trị A
    return Average
Average = CHUYENDOIANHMUCXAM(Hinhgoc)
hinhmucxam = np.array(Average)
# viết hàm nhận dạng đường biên
def CHUYENDOIHINHNHANDANGBIEN(Average):
    # tạo ảnh có cùng kích thước so với ảnh xám
    HINHNHANDANG= Image.new(Average.mode, Average.size)
    #lấy kích thước ảnh
    width= Average.size[0]   #tiên biến width và size 0 là chiều ngang
    height= Average.size[1]   #tiên biến height và size 1 là chiều cao

    # ma trận theo phương x
    matranlocx = np.array([(-1,-2,-1),(0,0,0),(1,2,1)],dtype=int)
    #ma trận theo phương y
    matranlocy = np.array([(-1,0,1),(-2,0,2),(-1,0,1)],dtype=int)

    Rnx = 0
    Rny = 0
    M0=0
    xt=0
    yt=0
    for x in range(1,width-1):
        for y in range(1,height-1):
            Rnx=0
            Rny=0
            for i in range(0,3,1):
                for j in range(0,3,1):
                    if(i==0):
                        xt=x-1
                    elif(i==1):
                        xt=x
                    elif(i==2):
                        xt=x+1

                    if(j==0):
                        yt=y-1
                    elif(j==1):
                        yt=y
                    elif(j==2):
                        yt=y+1
                    R, G, B = Average.getpixel((xt,yt))

                    #cộng dồn
                    Rnx += (R*matranlocx[i,j])
                    Rny += (R*matranlocy[i,j])
                    M0= np.abs(Rnx) + np.abs(Rny)
            # xét điều kiện
            if M0>130:
                M0=255
            else:
                M0=0
            HINHNHANDANG.putpixel((x,y),(M0,M0,M0))
    return HINHNHANDANG

anhnhandangbien = CHUYENDOIHINHNHANDANGBIEN(Average)
hinhlaybien = np.array(anhnhandangbien)

#hiển thị ảnh dùng thư viện opennCV
cv2.imshow('ANH GOC',img)
cv2.imshow('HINH NHAN DANG DUONG BIEN MUC XAM ', hinhlaybien )


#bấm phím bất kì đóng cữa sổ lại
cv2.waitKey(0)


#giải phóng bộ nhớ cấp phát cho các của sổ hiển thị
cv2.destroyAllWindows()



            



