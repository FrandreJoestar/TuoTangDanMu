# TuoTangDanMu
一个拖堂提醒器（老师：听我说我谢谢你）




## 教程

接下来我会讲解如何正确使用 **拖堂弹幕** ，学会这个很有必要，能让你更好的生存下去。

* ### k.py

**1. 修改字号和字体**


```py
font = ImageFont.truetype('SanJiNengLiangHeiJianTi-2.ttf', 36)
```

> 字体文件自行准备

**2. 修改弹幕颜色**

```py
draw.text((x, y), text, fill=(255, 0, 0), font=font)
```

> fill括号里的就是颜色RGB值

**3. 修改弹幕移动速度**

```py
def move_image():
        nonlocal x, image_obj
        if image_obj is None:
            image_obj = canvas.create_image(x, y, image=image, anchor=tk.NW)
        else:
            x += 5  # 移动速度
            canvas.coords(image_obj, x, y)
            if x > screen_width:
                root.destroy()
                return
        root.after(50, move_image)
```

* ### config.json

这是l.py的配置文件

```JSON
{
    "schedule": {
        "Monday": ["10:00", "15:00", "18:30"],
        "Tuesday": ["09:30", "13:45", "17:15"],
        "Wednesday": ["11:15", "14:20", "19:00"],
        "Thursday": ["10:30", "16:00", "20:45"],
        "Friday": ["09:00", "12:30", "16:45"],
        "Sunday": ["19:39","19:41","19:45","19:47"]
    },
    "script_to_run": "k.py"
}
```

你可以设置每天的课间时间来运行脚本



#### 你要做的

- [x] 不要尝试激怒老师
- [x] 在适当场合使用
- [x] 提前准备好检讨（doge）

