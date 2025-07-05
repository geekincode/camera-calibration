#!/bin/bash
source /etc/profile
echo "ROS系统版本: "${ROS_DISTRO}

python3 src/auto.py

if [ ! -d "download" ]; then
  mkdir download
fi

xdg-open ./download/calib.io_checker_200x150_8x11_15.pdf
