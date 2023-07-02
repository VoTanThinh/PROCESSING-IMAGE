from email.mime import message
import cv2
import tkinter as tk
from tkinter.ttk import *
from tkinter import *
from PIL import ImageTk ,Image
from matplotlib.pyplot import show
import numpy as np
from tkinter import messagebox
from tensorflow import keras
from tkinter import filedialog
from keras.utils import load_img
from keras.utils.image_utils import img_to_array
import os
import numpy as np
from keras.models import load_model
from keras.utils import  img_to_array

window = tk.Tk()
window.title("Đồ Án Cuối Kì")
colorBackground = "white" # chỉnh màu cho background
window.geometry("950x600")
window['bg'] = colorBackground
window.attributes('-topmost',True)

#Load hình 
imgLogo = Image.open("logonews.png")
resizeimage=imgLogo.resize((380,80),Image.ANTIALIAS)        #giảm hiểu nhòe cho hình ảnh
imgShowLogo =  ImageTk.PhotoImage(resizeimage)              #chuyển đổi hình ảnh đã hay đổi kích hước

imgTornato = Image.open("animal.jpg").resize((400,300),Image.ANTIALIAS)
imgShowTornato = ImageTk.PhotoImage(imgTornato)

imgkhoa = Image.open("logoCKM.png").resize((90,85),Image.ANTIALIAS)
imgShowkhoa = ImageTk.PhotoImage(imgkhoa)

imgtc = Image.open("wildlife.jpg").resize((550,320),Image.ANTIALIAS)
imgShowtc = ImageTk.PhotoImage(imgtc)



window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)               #mở rộng ra hoặc co lại theo kích thước của cữa sổ

# Chương trình con ===========================
def show_frame(frame):
    frame.tkraise() 

def loginx():
    username = entry1.get()        # nhập dữ liệu bằng cách sử dụng phương phap get
    password = entry2.get()
    if(username == "1" and password =="1"):
         show_frame(frame1)
         entry1.delete(0,'end')   #xóa nội dung của entry 1 và 2 bằng cách sử dụng 0 và end  
         entry2.delete(0,'end')   
    else:
        messagebox.showerror("","Sai tên tài khoản hoặc mật khẩu!")


def predict_disease(image_path):     # hàm đưa ra dự đoán dựa trên hình ảnh
    img = Image.open(image_path).resize((256, 256))     #mở hình ảnh và sau đó thay đổi kích thước ảnh
    img_array = np.array(img) / 255.0   # sau đó chuyển hình ảnh thành 1 mảng numpy và mối pixel chia cho 255  để đảm vảo giá trj nằm trong khoảng từ 0-1
    img_array = np.expand_dims(img_array, axis=0)       # thêm các chiều mới chp mảng đề phù hợp với đầu vào của chương trình

    # Make prediction using the loaded model
    prediction = model.predict(img_array)                 # đưa ra kết quả dự đoán
    # Assuming the model outputs one-hot encoded labels, convert prediction to class labels
    class_labels = ['\tChim cánh cụt Hoàng Đế: Chủ yếu ở xung quanh Nam Georgia và quần đảo Sandwich Nam\n\t\tCao khoảng 1,2m và nặng khoảng 40kg',
                    '\tGấu Kodiak: Chủ yếu sống trên đảo Kodiak, Alaska, Mỹ và Bắc Canada\n\t\tLà một trong những động vật nguy hiểm nhất Bắc Mỹ',
                    '\tHổ Siberia: Chủ yếu sinh sống ở miền đông Nga\n\t\tLà loài hổ lớn nhất và là một trong những động vật nguy hiểm nhất thế giới',
                    '\tSư tử Congo: Sinh sống chủ yếu ở Châu Phi\n\t\tLà động vật ký sinh lớn thứ hai sống trên đất liền sau con người\n\t\tLà loài sư tử lớn thứ hai trên thế giới','\tVoi Châu Phi: Sinh sống chủ yếu từ miền Nam sa mạc Sahara tới Nam Phi\n\t\tDo nạn săn bắn trái phép và mất môi trường sống nên số lượng voi Châu Phi đang giảm rất nhanh']
    predicted_label = class_labels[np.argmax(prediction)]   # lấy chỉ số dự đoan của lớp có xác suất cao nhất và sau đó lấy phần tử tương ứng từ class_labels làm nhãn dự đoán

    result_label.config(text="Prediction: " + predicted_label)   # hiển thị kết quả sau khi dự đoán

def TachVatKhoiAnh(image_path):      #tạo 1 hàm để tách vật ra khỏi phong nền
    img = cv2.imread(image_path)     # đọc file ảnh từ đường dẫn
    mask = np.zeros(img.shape[:2], np.uint8)    # khỏi tạo 1 mặt nạ có kích thước giiongs với kt ảnh gốc  có giá trị bằng 0
    # xác định vùng background và foreground
    backgroundModel = np.zeros((1,65),np.float64)
    foregroundModel = np.zeros((1,65),np.float64)

    rect = (50, 50, img.shape[1]-100, img.shape[0]-100) # khởi tạo hình chữ nhật bao quanh vật thể
    cv2.grabCut(img, mask, rect, backgroundModel, foregroundModel, 5, cv2.GC_INIT_WITH_RECT) # cập nhật mặt nạ phân loại các điểm thành bg và fg

    # cập nhật mask chỉ giữ lại vùng fg
    mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
    img = img*mask2[:,:,np.newaxis]     # nhân ma trận img với mask2 để phân ảnh vủng fg và loại bỏ vùng bg
    return img

    

# Function to handle button click event
def open_image():
    image_path = filedialog.askopenfilename(initialdir="test_images", title="Select Image",
                                            filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png")))
    predict_disease(image_path)   #gọi để dự toán dựa trên hình ảnh đã chọn
    img1 = TachVatKhoiAnh(image_path)   # gọi hàm grapcut để tách nền ra khỏi hình ảnh con vật
    
    # Display the selected image in the GUI
    img = Image.open(image_path).resize((256,256))
    img_tk = ImageTk.PhotoImage(img)      #hiển thị hình ảnh lên trong giao diện TK
    img_label = tk.Label(window, image=img_tk)   
    img_label.image = img_tk #tạo biến để chứa hình ảnh để tránh bị thu giữ bỡi bộ thu gom rac của python
    img_label.place(x=100,y=220)    # vị trí đặt nhãn

    resized_img1 = cv2.resize(img1, (256, 256))   # thay đổi kích thước của hình ảnh và gán vào resized_img1
    pil_img1 = Image.fromarray(resized_img1)       # chuyển 1 mảng numpy thành 1 đối tượng hình ảnh
    tk_img1 = ImageTk.PhotoImage(pil_img1)      #tạo  một đối tượng để hiển thị hình ảnh rên python
    img1_label = tk.Label(window, image=tk_img1)   # tạo nhãn đẻ chứa hình ảnh tk_img1
    img1_label.image = tk_img1   #tạo biến để chứa hình ảnh để tránh bị thu giữ bỡi bộ thu gom rac của python
    img1_label.place(x=600,y=220)   # vị trí đặt nhãn

# End chương trình con ========================
login = tk.Frame(window)       # tạo ra các cữa sổ giao diện theo thứ tự frame 1 frame 2
frame1 = tk.Frame(window)
frame2 = tk.Frame(window)
#frame3 = tk.Frame(window)

frame1.grid(row=0,column=0,sticky='nsew')   #tạo 1 khung frame 1 ở hàng 0 cột 0 và khung sẽ dãn theo các hướng động tây nam bắc
frame2.grid(row=0,column=0,sticky='nsew')
login.grid(row=0,column=0,sticky='nsew')
#frame3.grid(row=0,column=0,sticky='nsew')

#login['bg'] = 'white'
#login code
global entry1,entry2    # khai bao entry1 và 2 toàn cục cho phép sử dụng chúng trong toàn bộ chường trình
Label(login,text="UserName").place(x = 600,y = 300)    # vị trí hiển thị các label bên trong khung login
Label(login,text="PassWord").place(x = 600,y = 330)
entry1 = Entry(login,bd=5)      # độ giày khung
entry1.place(x = 670, y= 300)
entry2 = Entry(login,bd=5,show="*")    
entry2.place(x = 670,y=330)

login_img = tk.Label(login,text="",image=imgShowLogo)
login_img.place(x = 0,y= 0)
#lbl = tk.Label(login,text="",image = imgShowtc,bg=colorBackground)
#lbl.place(x = 20 , y = 190)
login_img_1 = tk.Label(login,text="",image=imgShowkhoa)             #hiển thị trong cữa sổ login  với tham số nội dung để trống và chỉ định  hình ảnh cuuar nhãn
login_img_1.place(x = 850,y= 0)

login_img_3 = tk.Label(login,text="",image=imgShowtc)
login_img_3.place(x = 20,y= 190)


lblNameID1 = tk.Label(login,text = "Trường Đại Học Sư Phạm Kỹ Thuật TPHCM",bg= colorBackground,font=('Arial',13,'bold'),fg="#000080")   #fg chỉ định màu chữ  kiểu chữ kichsthuoc độ đậm
lblNameID1.place(x=500,y=0 )
lblNameID2 = tk.Label(login,text = "Khoa Cơ Khí Chế Tạo Máy",bg=colorBackground,font=("Arial",13,'bold'),fg="#000080")
lblNameID2.place(x=600,y=25 )
lblNameID3 = tk.Label(login,text = "Bộ Môn Cơ Điện Tử",bg= colorBackground,font=("Aria",13,'bold'),fg="#000080")
lblNameID3.place(x=630,y=50)
lblNameID5 = tk.Label(login,text = "Đề Tài:  Nhận Dạng Động Vật Hoang Dã Ứng Dụng Xử Lý Ảnh Và Trí Tuệ Nhân Tạo",bg= colorBackground,font=("Arial",15,"bold"),fg="#000080")
lblNameID5.place(x=100,y=120)



Button(login,text="Login",height=1,width=12,bd=9,command=loginx,bg="blue",font=('Arial',11,'bold')).place(x=670, y = 380 )
# hiển thị, chiều cao, rộng, độ dày,   hàm được gọi khi nhân nút , màu nền
show_frame(login) 

# frame 1 code
frame1_btn = tk.Button(frame1,text = "Processing",height=2,width=18,bd=9,command=lambda:show_frame(frame2),bg="green",font=('Arial',11,'bold'))
frame1_btn.place(x = 400,y = 510)
frame1_btnLogout = tk.Button(frame1,text = "Logout",command=lambda:show_frame(login),bg="red")
frame1_btnLogout.place(x = 900,y = 0) 

frame1_img = tk.Label(frame1,text="",image=imgShowLogo)
frame1_img.place(x = 0,y= 0)
lbl = tk.Label(frame1,text="",image = imgShowTornato,bg=colorBackground)
lbl.place(x = 480 , y = 180)

lblNameID1 = tk.Label(frame1,text = "Trường Đại Học Sư Phạm Kỹ Thuật TPHCM",bg= colorBackground,font=('Arial',13,'bold'),fg="#000080")
lblNameID1.place(x=500,y=0)
lblNameID2 = tk.Label(frame1,text = "Khoa Cơ khí Chế tạo máy",bg=colorBackground,font=("Arial",13,'bold'),fg="#000080")
lblNameID2.place(x=600,y=25 )
lblNameID3 = tk.Label(frame1,text = "Bộ Môn Cơ Điện Tử",bg= colorBackground,font=("Aria",13,'bold'),fg="#000080")
lblNameID3.place(x=630,y=50)
lblNameID4 = tk.Label(frame1,text = "Ngành Công Nghệ Kỹ Thuật Cơ Điện Tử",bg= colorBackground,font=("Arial",13,'bold'),fg="#000080")
lblNameID4.place(x=520,y=75)
lblNameID5 = tk.Label(frame1,text = "Đề Tài:  Nhận Dạng Động Vật Hoang Dã Ứng Dụng Xử Lý Ảnh Và Trí Tuệ Nhân Tạo",bg= colorBackground,font=("Arial",15,"bold"),fg="#000080")
lblNameID5.place(x=100,y=120)
lblNameID9 = tk.Label(frame1,text = "GVHD: TS. Nguyễn Văn Thái",bg= colorBackground,font=("Arial",13,"bold"),fg="#000080")
lblNameID9.place(x=60,y=180)
lblNameID6 = tk.Label(frame1,text = "SVTH: ",bg= colorBackground,font=("Arial",13,"bold"),fg="#000080")
lblNameID6.place(x=60,y=210)
lblNameID6 = tk.Label(frame1,text = "1. Võ Văn Thuận        20146084",bg= colorBackground,font=("Arial",13,"bold"),fg="#000080")
lblNameID6.place(x=60,y=235)
lblNameID7 = tk.Label(frame1,text = "2. Lê Minh Tiên          20146196",bg= colorBackground,font=("Arial",13,"bold"),fg="#000080")
lblNameID7.place(x=60,y=260)
lblNameID8 = tk.Label(frame1,text = "3. Võ Tấn Thịnh         20146536",bg= colorBackground,font=("Arial",13,"bold"),fg="#000080")
lblNameID8.place(x=60,y=285)




#Code frame 2
#Load Model
model = keras.models.load_model('CuoiKi.h5') 
#video = cv2.VideoCapture(0)
frame2_btn = tk.Button(frame2,text = "Back",command=lambda:show_frame(frame1),bg="green")
frame2_btn.place(x = 900, y = 0 )
frame2_img = tk.Label(frame2,text="",image=imgShowLogo)
frame2_img.place(x = 0,y= 0)

lblNameID1 = tk.Label(frame2,text = "Trường Đại Học Sư Phạm Kỹ Thuật TPHCM",bg= colorBackground,font=('Arial',13,'bold'),fg="#000090")
lblNameID1.place(x=500,y=0)
lblNameID2 = tk.Label(frame2,text = "Khoa Cơ Khí Chế Tạo Máy",bg=colorBackground,font=("Arial",13,'bold'),fg="#000080")
lblNameID2.place(x=600,y=25 )
lblNameID3 = tk.Label(frame2,text = "Bộ Môn Cơ Điện Tử",bg= colorBackground,font=("Aria",13,'bold'),fg="#000080")
lblNameID3.place(x=630,y=50)
lblNameID4 = tk.Label(frame2,text = "Ngành Công Nghệ Kỹ Thuật Cơ Điện Tử",bg= colorBackground,font=("Arial",13,'bold'),fg="#000080")
lblNameID4.place(x=520,y=75)
lblNameID5 = tk.Label(frame2,text = "Đề Tài:  Nhận Dạng Động Vật Hoang Dã Ứng Dụng Xử Lý Ảnh Và Trí Tuệ Nhân Tạo",bg= colorBackground,font=("Arial",15,"bold"),fg="#000080")
lblNameID5.place(x=100,y=120)
lblNameID10 = tk.Label(frame2,text = "Select Image",bg= colorBackground,font=("Arial",13,"bold"),fg="#000080")
lblNameID10.place(x=120,y=200)
lblNameID11 = tk.Label(frame2,text = "GrabCut Image",bg= colorBackground,font=("Arial",13,"bold"),fg="#000080")
lblNameID11.place(x=620,y=200)
# Create a button to open an image for prediction
open_button = tk.Button(frame2,text="Open Image", command=open_image,bg="yellow")
open_button.place(x=465,y=165)
# Create a label to display the prediction result
result_label = tk.Label(frame2,text="Prediction: ",bg= colorBackground,font=("Arial",13,"bold"),fg="#000080",justify=LEFT)
result_label.place(x=0,y=500)


window.mainloop()