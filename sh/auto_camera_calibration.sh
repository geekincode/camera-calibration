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
# 检测ROS版本
ROS_DISTRO="humble"
echo "检测到ROS版本为：$ROS_DISTRO"

# 检测相机驱动是否已安装
# if [ ! -f "/etc/ros/rosdep/sources.list.d/20-default.list" ]; then
#     echo "ROS未安装，正在安装ROS..."
#     # 在这里添加安装ROS的命令
# fi

# 安装相机标定包
# echo "安装相机标定包..."
# sudo apt update
# sudo apt install ros-${ROS_DISTRO}-camera-calibration
echo "检测相机标定包是否已安装..."
if dpkg -l | grep -q "ros-${ROS_DISTRO}-camera-calibration"; then
    echo "相机标定包已安装"
else
    echo "相机标定包未安装，正在安装..."
    sudo apt update
    sudo apt install -y ros-${ROS_DISTRO}-camera-calibration
fi

# 检测相机驱动是否已安装
echo "检测相机驱动是否已安装..."
if find ./src -name "hik_camera.launch.py" | grep -q "hik_camera.launch.py"; then
    echo "相机驱动已安装"
else
    echo "相机驱动未安装，正在下载和安装相机驱动..."
    # 在这里添加下载和安装相机驱动的命令
    # 示例：
    # cd ~/ros2_ws/src
    # git clone https://github.com/your-repo/hik_camera.git
    # cd ~/ros2_ws
    # colcon build
    # source ~/ros2_ws/install/setup.bash
fi

sleep 100

# 运行相机驱动
echo "运行相机驱动..."
ros2 launch hik_camera hik_camera.launch.py

# 下载标定板
echo "下载标定板..."
wget https://calib.io/zh/pages/camera-calibration-pattern-generator

# 检测标定板是否下载成功
if [ -f "pattern.png" ]; then
    echo "标定板下载成功"
else
    echo "标定板下载失败，请检查网络连接或链接是否正确"
    exit 1
fi

# 设置标定参数
CALIB_SIZE="7x10"
CALIB_SQUARE="0.015"

# 运行标定程序
echo "运行标定程序..."
ros2 run camera_calibration cameracalibrator --size $CALIB_SIZE --square $CALIB_SQUARE --ros-args -r image:=/image_raw

# 提示用户标定完成
echo "标定完成，请检查标定结果。"