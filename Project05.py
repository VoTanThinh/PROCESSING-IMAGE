import cv2;                   # thư viện opencv
from PIL import Image;        #thư viện xử lí ảnh
import numpy as np;           # thư viện ính toán 
import matplotlib.pyplot as plt; #thư viện vẽ biểu đồ

def ChuyenDoiAnhMauRBGSangAnhXamLuminance(imgPIL): # Hàm tính thep phương phap luminance

    #tạo 1 ảnh có cùng kích thước  và mode với ảnh imgPIL
    #ẢNH này chứa các kết quả chuyển đồi RGB sáng Grayscale
    Average= Image.new(imgPIL.mode, imgPIL.size)

    #lấy kích thước anh từ imgPIL
    width= Average.size[0]   #tiên biến width và size 0 là chiều ngang
    height= Average.size[1]   #tiên biến height và size 1 là chiều cao

    #mỗi ảnh là 1 ma trân 2 chiều nên ta dùng 2 vào for
    # đọc hết các điểm pixel có trong ảnh
    for x in range(width):
        for y in range(height):
            # Lấy giá trị điểm ảnh tại các vị trí x,y
            R, G, B = imgPIL.getpixel((x, y))     #là veecto 3 phần tử RGB trả về từ hàm getpixel tại vị trí x, y

            gray = np.uint8(0.2126*R + 0.7152*G +0.0722*B)    #LUMINANCE

            #gán giá trị vừa tính cho mức xám
            Average.putpixel((x, y), (gray, gray, gray)) #ảnh gồm 3 kênh mình cho cùng giá trị gray
    return Average
        
#hàm Tính histogram của hình mức xám
def TinhHistogram(HinhXamPIL):
    #Mỗi  pixel  có giá trị tử 0-255, nên phải khai báo 1 mảng có
    #256 phần tử để chứa số đếm các pixel có cùng giá trị

    his = np.zeros(256)
    #Kích thước ảnh
    w= HinhXamPIL.size[0]  # theo chiều ngang
    h= HinhXamPIL.size[1]   # theo chiều dọc
    for x in range(w):
        for y in range(h):
            #lấy giá trị ảnh tại x,y
            gR, gG, gB = HinhXamPIL.getpixel((x,y)) #là veecto 3 phần tử RGB trả về từ hàm getpixel tại vị trí x, y
            #giá trị gray tính ra cũng chính là phần tử thứ gray
            #trong mảng his đã khai báo ở trên, sễ tắng số đếm của các phần tử thứ gray  1
            his[gR]+=1
    return his


# vẽ biểu đồ his togram bằng thứ viện maplot
def VeBieuDoHistogram(his):
    w = 5
    h = 4
    plt.figure('Biểu đồ histogram ảnh xám ', figsize=(((w,h))), dpi= 100 )
    trucX =np.zeros(256) #khai báo 1 mảng 256 phần tử
    trucX =np.linspace(0,256,256)
    plt.plot(trucX, his, color='orange')  # vẽ lên đồ thị
    plt.title('biểu đồ Histogram')  # tên biểu đồ
    plt.xlabel('giá trị mức xám')# trục đứng
    plt.ylabel('số điểm cùng giá trị màu xám') #trục ngang
    plt.show() # hiển thị đồ thị sau khi vẽ

#BEGIN#BẮT ĐẦU CHƯƠNG TRÌNH CHÍNH
#lưu ý các hàm con cần phải khai báo trước khi hcuowng trình chính gọi

filehinh = r'bird_small.jpg' # khaai báo đường dẫn ảnh

img= cv2.imread(filehinh, cv2.IMREAD_COLOR) # đọc ảnh màu dùng thư viện opencv hiển thị

#đọc ảnh màu dúng thư viện pil để thực hiện tác vụ xử lí ảnh và tính toán tính toán thay vì opencv
imgPIL= Image.open(filehinh)

#chuyển ảnh sang mức xám
HinhmucxamPIL = ChuyenDoiAnhMauRBGSangAnhXamLuminance(imgPIL)

#tính histogram
his= TinhHistogram(HinhmucxamPIL)

# CHUYỂN PIL sang opencv để hiển thị
HinhXamCV= np.array(HinhmucxamPIL)

#END CHƯƠNG TRÌNH CHÍNH
#hiển thị ảnh dùng thư viện opennCV
cv2.imshow('ảnh mức xám',HinhXamCV)
cv2.imshow('ảnh mức xám',img)
#Hiển thị biểu đồ histogram 
VeBieuDoHistogram(his)



#bấm phím bất kì đóng cữa sổ lại
cv2.waitKey(0)


#giải phóng bộ nhớ cấp phát cho các của sổ hiển thị
cv2.destroyAllWindows()


