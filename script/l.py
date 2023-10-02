import time
import subprocess
import json
from datetime import datetime
import pygetwindow as gw
import os

# 获取脚本所在的目录
script_dir = os.path.dirname(os.path.abspath(__file__))

# 设置工作目录为脚本所在的目录
os.chdir(script_dir)


# 读取配置文件
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

# 获取要运行的脚本名称
script_to_run = config.get('script_to_run')

while True:
    # 获取当前时间和工作日
    current_time = datetime.now()
    current_day = current_time.strftime("%A")  # 获取当前工作日的名称
    current_time_str = current_time.strftime("%H:%M")
    
    # 检查当前时间是否在配置文件中指定的运行时间列表中
    if current_day in config['schedule']:
        run_times = config['schedule'][current_day]
        if current_time_str in run_times:
            # 获取当前聚焦的窗口
            active_window = gw.getActiveWindow()
            
            # 判断当前聚焦的窗口标题是否为空
            is_desktop = (active_window is not None and active_window.title == "")
            
            # 如果当前聚焦的窗口标题为空
            if not is_desktop:
                print(f"运行脚本 {script_to_run} 在 {current_day} {current_time_str}...")
                subprocess.run(["python", script_to_run])  # 假设要运行的脚本是一个Python脚本
    
    # 等待一段时间后再次检测
    time.sleep(600)  # 每隔十分钟检测一次
