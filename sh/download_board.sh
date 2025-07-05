#!/bin/bash
source /etc/profile
echo "ROS系统版本: "${ROS_DISTRO}

if [ ! -d "src" ]; then
  mkdir src
fi

if [ ! -d "download" ]; then
  mkdir download
fi

if [ ! -d "tools" ]; then
  mkdir tools
fi

wget -q https://raw.githubusercontent.com/geekincode/camera-calibration/refs/heads/main/src/auto.py -O src/auto.py
python3 src/auto.py

xdg-open ./download/calib.io_checker_200x150_8x11_15.pdf
