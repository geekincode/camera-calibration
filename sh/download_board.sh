#!/bin/bash
source /etc/profile

SUDO=''
if [ $UID -ne 0 ];then
    SUDO='sudo'
fi
echo "当前用户为：$USER"
while IFS= read -r -n1 char; do
    echo -n "$char"
    sleep 0.1
done <<< "当前用户为：$USER"
echo "ROS系统版本: "${ROS_DISTRO}

if [ ! -d "sh" ]; then
  mkdir sh
fi

echo "开始下载脚本文件..."
if [ ! -d "src" ]; then
  mkdir src
fi

if [ ! -d "download" ]; then
  mkdir download
fi

if [ ! -d "tools" ]; then
  mkdir tools
fi

$SUDO wget -q https://raw.githubusercontent.com/geekincode/camera-calibration/refs/heads/main/src/auto.py -O src/auto.py
$SUDO python3 src/auto.py

xdg-open ./download/calib.io_checker_200x150_8x11_15.pdf
