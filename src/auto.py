# -*- coding: utf-8 -*-
import os
import sys
import importlib
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tools.base import *

PrintUtils.print_delay("这是自动配置相机标定的脚本")

# 定义要下载的文件的 URL 和保存路径
url_prefix = "https://raw.githubusercontent.com/geekincode/camera-calibration/refs/heads/main/"
pdf_path= "doc/calib.io_checker_200x150_8x11_15.pdf"
output_path = "./download/calib.io_checker_200x150_8x11_15.pdf"

PrintUtils.print_delay("开始下载棋盘格标定板文件...", 0.1)

# 构造 wget 命令
wget_command = f"wget -v {url_prefix+pdf_path} -O {output_path}"

# 使用 subprocess.run 执行命令
try:
    # result = subprocess.run(
    #     wget_command, 
    #     shell=True, 
    #     check=True, 
    #     text=True, 
    #     capture_output=True,
    #     encoding='utf-8'  # 确保正确解码输出
    # )
    CmdTask(wget_command).run()
    # print("输出：", result.stdout, flush=True)
    # PrintUtils.print_delay(result.stderr,0.001)
    PrintUtils.print_delay("下载成功！")
except subprocess.CalledProcessError as e:
    PrintUtils.print_delay("下载失败！")
    print("错误信息：", e.stderr)

