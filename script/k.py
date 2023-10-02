import time
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import PhotoImage
import os

# 获取脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 设置工作目录为脚本所在的目录
os.chdir(script_dir)



def create_image(minutes):
    # 创建一个透明背景的图片
    img = Image.new('RGBA', (500, 100), (255, 255, 255, 0))

    # 创建一个绘图对象
    draw = ImageDraw.Draw(img)

    # 设置字体和字号
    font = ImageFont.truetype('SanJiNengLiangHeiJianTi-2.ttf', 36)

    # 设置文本内容
    text = f"老师你已经拖堂{minutes}分钟了"

    # 使用textbbox来获取文本的宽度和高度
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # 计算文本在图片中的位置
    x = (img.width - text_width) / 2
    y = (img.height - text_height) / 2

    # 绘制文本
    draw.text((x, y), text, fill=(255, 0, 0), font=font)

    return img

def display_image(image_path):
    # 创建Tkinter窗口
    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-transparentcolor", "white")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry(f"{screen_width}x{screen_height}+0+0")
    canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='white')
    canvas.pack()

    # 加载并显示图片
    image = PhotoImage(file=image_path)
    x = 0
    y = 0
    image_obj = None

    def move_image():
        nonlocal x, image_obj
        if image_obj is None:
            image_obj = canvas.create_image(x, y, image=image, anchor=tk.NW)
        else:
            x += 10  # 移动速度
            canvas.coords(image_obj, x, y)
            if x > screen_width:
                root.destroy()
                return
        root.after(50, move_image)

    move_image()

    # 设置窗口为永久置顶
    root.attributes('-topmost', True)

    root.mainloop()

def main():
    start_time = time.time()
    minutes = 0

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time
        current_minutes = int(elapsed_time / 10)

        if current_minutes > minutes:
            minutes = current_minutes
            # 每隔一分钟绘制一张图片
            img = create_image(minutes)
            img.save(f'{minutes}.png')

            # 显示图片在Tkinter窗口中
            display_image(f'{minutes}.png')

if __name__ == "__main__":
    main()
