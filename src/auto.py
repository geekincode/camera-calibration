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
base_url = os.path.join(url_prefix, 'tools/base.py')
src_url = os.path.join(url_prefix, 'src/auto.py')
output_path = "./download/calib.io_checker_200x150_8x11_15.pdf"

PrintUtils.print_delay("开始下载脚本文件...", 0.05)
download_tools_command = "wget {} -O {} --no-check-certificate".format(base_url,base_url.replace(url_prefix,''))
CmdTask(download_tools_command).run()
download_src_command = "wget {} -O {} --no-check-certificate".format(src_url,src_url.replace(url_prefix,''))
CmdTask(download_src_command).run()


PrintUtils.print_delay("开始下载棋盘格标定板文件...", 0.05)

# 构造 wget 命令
download_board_command = f"wget -v {url_prefix+pdf_path} -O {output_path}"

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
    CmdTask(download_board_command).run()
    # print("输出：", result.stdout, flush=True)
    # PrintUtils.print_delay(result.stderr,0.001)
    PrintUtils.print_delay("下载成功！")
except subprocess.CalledProcessError as e:
    PrintUtils.print_delay("下载失败！")
    print("错误信息：", e.stderr)

