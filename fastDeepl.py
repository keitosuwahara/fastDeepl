import tkinter
import glob
from PIL import Image
import keyboard
import shutil
import os
import pyautogui

print("翻訳開始")
if keyboard.read_key() == "space":
    print("space")
        
#範囲を指定して切り取った画像の保存場所："ocr_images"
#古い画像を削除するため、毎回フォルダ毎削除し、再度フォルダを作成
shutil.rmtree("./ocr_images")
os.mkdir("./ocr_images")


#OCRを行いたい、未処理の画像の保存場所："images"
pngs = glob.glob("screenshot/*.png")
img1 = Image.open(pngs[0])
W,H = img1.size

#指定範囲した画像に名前をつける番号：cnt
cnt = 1


#スクリーンショットのフォルダパス
screenshot_folder_path = "./screenshot"
#スクリーンショットのパス
screenshot_path = "./screenshot/screen.png"

#まずスクショのフォルダを消す

#そのパソコンの画面幅
scr_width, scr_height= pyautogui.size()



#コールバック関数：タッチパッドを押した時
def Push(event):
    global x_start,y_start
    x_start = event.x
    y_start = event.y
    canvas.create_rectangle(x_start,y_start,x_start+1,y_start+1,outline="red",tag="rect")

#コールバック関数：タッチパッドから指を離したとき
def Release(event):
    global x_end,y_end,cnt
    x_end = event.x
    y_end = event.y
    canvas.create_rectangle(x_start,y_start,x_end,y_end,outline="red")
    img = Image.open(pngs[0])
    img.crop((x_start,y_start,x_end,y_end)).save(f"ocr_images/{cnt}.png")
    cnt = cnt + 1

#コールバック関数：タッチパッド上で指を動かしている時
def Motion(event):
    x_end = event.x
    y_end = event.y
    canvas.coords("rect",x_start,y_start,x_end,y_end)




screenshot = pyautogui.screenshot(region=(0, 0, scr_width, scr_height))
screenshot.save(screenshot_path)
#スクショを半分のサイズにする
img = Image.open(screenshot_path)
(width, height) = (int(img.width * 0.65), int(img.height * 0.65))
resized_img = img.resize((width, height))
resized_img.save(screenshot_path, quality=90)


root = tkinter.Tk()
root.geometry(f"{int(scr_width*0.65)}x{int(scr_height*0.65)}")
root.title("翻訳範囲選択")
root.attributes("-topmost",True)

# キャンバス作成
canvas = tkinter.Canvas(root, bg="#deb887", width=int(scr_width*0.65), height=int(scr_height*0.65))
# キャンバス表示
canvas.place(x=0, y=0)
img = tkinter.PhotoImage(file="./screenshot/screen.png", width=int(scr_width*0.65), height=int(scr_height*0.65))
canvas.create_image(0, 0, image=img, anchor=tkinter.NW)

#コールバック関数の設定
root.bind("<ButtonPress-1>",Push)
root.bind("<ButtonRelease-1>",Release)
root.bind("<Button1-Motion>",Motion)
root.mainloop()



#OCR・tesseractを実行するpyファイルの呼び出し
import ocr