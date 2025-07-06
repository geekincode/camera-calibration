# -*- coding: utf-8 -*-
import os
import sys
import importlib
import subprocess

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 定义要下载的文件的 URL 和保存路径
url_prefix = "https://raw.githubusercontent.com/geekincode/camera-calibration/refs/heads/main/"
pdf_path= "doc/calib.io_checker_200x150_8x11_15.pdf"
base_url = os.path.join(url_prefix, 'tools/base.py')
current_dir = os.getcwd()
board_output_path = "./download/calib.io_checker_200x150_8x11_15.pdf"

zhuxi_text = """                                                                                                    
                                                                                                    
                                                                                           $$$      
                                         .                                               =$$$$$$.   
   .$$=  $$$$  $**^^>>>>>            $$$$=                       .$$-           *$$$$$$$$$>,        
   $$$$  $$$$  $$$$$$$$$$            $$$$*                      .$$.  =$$$$$$$->^.    $$,           
   -$$$$ $$$$  $$$$$$$$$$            $$$$-                 $$$$$$$$*-=,.     =$$$$$ $$>.            
    $$$$$$$$$$$$$$$,.$$$$            $$$$.              ,$>^.$$,   $$,^$$$$,$, $$, $$,              
    *$ $$$$$$$$$$$$  $$$$   $$$$$$$$$$$$$$$$$$$$$$        .$...=$*^>.        ^$= $$.                
     $ $$$$$$$$$$$$  $$$$   $$$$$$$$$$$$$$$$$$$$$$        $$.          ^       .$$                  
  =$$$.  $$$$  $$$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$      .$*           .$$$-=$$-                     
   $$$$ .$$$$  $$$$$$$$$$   $$$$$$$$$$$$$$$$$$$$$$                        $$-                       
   $$$$-$$$$$$^$$$^  $$$$           $$$$$*                            . .,   =                      
    $$$$$$$$$$$$$$^  $$$$          .$$$$$$                           $$$     .,                     
    .  $$$$$$$$$$$$$$$$$$          $$$$$$$.                        $$. .$= ,> .                   - 
    $$.$$$$$$$.$$$$$$$$$$         -$$$$$$$$                      *$=. $$, $  $ $ $     .$$          
   ,$$$$$$$$$  $$$$$$$$$$        ,$$$$$$$$$$                    $$. =$- =..$ $$$$-  $^.-.*$$$       
   $$$$$$$$$$  $$$,  $$$$       $$$$$$. $$$$$,                $$-..$$$$$$$$$$$$$$ -.-$-, >$ $       
   $$$$$ $$$$  $$$,  $$$$     -$$$$$$.  =$$$$$$,            $$$.  .            .$. ^$- >.- $        
   $$$$  $$$$  $$$$$$$$$$   $$$$$$$$     =$$$$$$$$,  ,$>=$$$$$$$$$$$$$$$$$$$$$$.=$$$*.=$$$*         
   $$$$  $$$$  $$$$$$$$$$  *$$$$$$$       .$$$$$$^ .=>>^*$$,                     $$.                
  =$$$   $$$$ .$$$$$$$$$=   ^$$$$           $$$$>      $$,                     ,$^                  
   ^$$   $$$$ ,$$$  .$$$>    $$               .$       ..                                           
                                                                                                    
   .$$                              $$$$^  .$$$$-     ^$$$$     $$$$  $.                 $$$$$      
  $$$$>  $$$$$$$$$$$$$$$$  $$$$$$$   $$$$  $$$$=  .   *$$$$     $$$$ $$$$    $$$$$$$$$   $$$$$      
  ^$$$$  $$$$$$$$$$$$$$$$  $$$$$$$$$$$$$$$$$$$$$$$,   *$$$$     $$$$>$$$$$   $$$$$$$$$   $$$$$      
   $$$$$ $$$$$$$$$$$$$$$$  $$$$$$$$$$$$$$$$$$$$$$$-   *$$$$>>>> $$$$  $$$$   $$$$$$$$$   $$$$$      
    $$$$$   .$$$$$$        $$$.$$$ $$$$$$$$$$$$$$$    $$$$$$$$$ $$$$   $...  $$$$ $$$$   $$$$$      
    =$$. ,$$$$$$$*   ^$$   $$$ $$$ $$$$$$$$$$$$$$$    -$$$$$$$$ $$$$$$$$$$$  $$$$ $$$$   $$$$$      
    .   $$$$$$$$$$  $$$$$  $$$ $$$      =$$$          -$$$$$$$$$$$$$$$$$$$$  $$$$-$$$$   $$$$$      
 -$$$$$$^$$$$ $$$$$$$$$$$  $$$ $$$$$$$$$$$$$$$$$$$$   ,$$$$   $$$$$$$$$$$$$  $$$$$$$$    $$$$$      
 ,$$$$$$ $  $$$$$$$$$$$.   $$$ $$$$$$$$$$$$$$$$$$$$   ,$$$$   $$$$$$^  $$    $$$$$$$$    $$$$$.     
 ,$$$$$$ ^$$$$$$$$$$$,     $$$$$$$^$$$$$$$$$$$,$$.  **^$$$$***, *$$$^ *$$$=  $$$$$$$$    $$$$$$     
 .$$$$$$$$$$$$.$$$$$$$$.   $$$$$$$ $$$$$$$$$$$*$$$. $$$$$$$$$$$  $$$$.$$$$$  $$$$ $$$$   $$$$$$     
   .$$$$=$$$.$$$$$$$$$$$=  $$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$*  $$$$$$$$$   $$$$ *$$$. $$$$$$$.    
   .$$$$ $ $$$$$$$$$$$$$$$ $$$ $$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$*  $$$$$$$$    $$$$  $$$$ $$$$$$$$    
    $$$$ $$$$$$$ $$$ $$$$= $$$ $$$ $$$$$-$$*$$$ $   $$$$  >$$$*  $$$$$$$     $$$$=$$$$$$$$$$$$$$    
    $$$$$$$$$$  $$$$  =$$. $$$ $$$$$$$$$=$$$$$$$$$$ $$$$  >$$$^ .$$$$$$ $$.  $$$$$$$$$-$$$$*$$$$$   
    $$$$ $$$ $$$$$$$    .  $$$ $$$$$$$$$$$$*$$$$$$  $$$$  ^$$$^$$$$$$$. $$$$ $$$$$$$$$$$$$$  $$$$$  
   $$$$$ $   $$$$$$^       $$$$$$$$$$$$$$$$ $$$$$   $$$$$$$$$$$$$$$$$$$$$$$..$$$$.  $$$$$$    $$$$$$
  $$$$$$$$.  $$$$=         $$$$$$$.$$$$$$$..$$$$ $$ $$$$$$$$$$$$$$$$$$$$$$$..$$$$.  $$$$$$    $$$$$$
  $$        $$.     .$>        $.      $$$  =$$$. , $$$$^   $$>=>      .$       $       ^.       .*$
  $$$**$$$. $  $$$$, -       ..  >  ,^  $    $= $   $$$  $.  $> .      .$$$  $$$$.      .,*****^  ^ 
     ...   $$   ==  .$  $$$$. ^-  ==$  $  .$   $        =$$   ^   $$$$. >$-  $$$$$$        .. .  $$ 
                                                                                                    
                                                                                                    

                                                                                                    """

download_tools_command = "wget -q {} -O {} --no-check-certificate".format(base_url,base_url.replace(url_prefix,''))
os.system(download_tools_command)

from tools.base import *

PrintUtils.print_delay(zhuxi_text, 0.0005)
PrintUtils.print_delay(f"当前工作目录: {current_dir}", 0.05)
PrintUtils.print_delay("这是自动配置相机标定的脚本", 0.05)
PrintUtils.print_delay("开始下载棋盘格标定板文件...", 0.05)

# 构造 wget 命令
download_board_command = f"wget -v {url_prefix+pdf_path} -O {board_output_path}"
download_hik_camera_command = "cd src && git clone https://github.com/FaterYU/ros2_hik_camera.git"
download_camera_calibration_command = "sudo apt install ros-${ROS_DISTRO}-camera-calibration" #需要密码?!

try:
    CmdTask(download_board_command).run()
    PrintUtils.print_delay("下载成功！")
except subprocess.CalledProcessError as e:
    PrintUtils.print_delay("下载失败！")
    print("错误信息：", e.stderr)

try:
    CmdTask(download_hik_camera_command).run()
    PrintUtils.print_delay("下载成功！")
except subprocess.CalledProcessError as e:
    PrintUtils.print_delay("下载失败！")
    print("错误信息：", e.stderr)

PrintUtils.print_delay("开始运行海康相机驱动...")
os.system("colcon build")
subprocess.run(f"gnome-terminal -- /bin/bash -c 'cd {current_dir} && source install/setup.bash && ros2 launch hik_camera hik_camera.launch.py ; exec bash'", shell=True, executable="/bin/bash")

PrintUtils.print_delay("开始进行相机标定...")
# try:
#     CmdTask(download_camera_calibration_command).run()
#     PrintUtils.print_delay("下载成功！")
# except subprocess.CalledProcessError as e:
#     PrintUtils.print_delay("下载失败！")
#     print("错误信息：", e.stderr)
subprocess.run("gnome-terminal -- /bin/bash -c 'ros2 run camera_calibration cameracalibrator --size 7x10 --square 0.015 --ros-args -r image:=/image_raw ; exec bash'", shell=True, executable="/bin/bash")

PrintUtils.print_delay("请按Ctrl+C退出")
