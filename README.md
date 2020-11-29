# OpenCV-CameraCalibration
使用Python及OpenCV实现相机参数标定
# 简介：
摄像机标定(Camera calibration)简单来说是从世界坐标系换到图像坐标系的过程，也就是求最终的投影矩阵 P 的过程，下面相关的部分主要参考UIUC的计算机视觉的课件（网址Spring 2016 CS543 / ECE549 Computer vision）。 
# 相机标定的原理
## 基本的坐标系：
        · 世界坐标系(world coordinate system)；
        · 相机坐标系(camera coordinate system)；
        · 图像坐标系(image coordinate system)；
    一般来说，标定的过程分为两个部分：
        · 第一步是从世界坐标系转换为相机坐标系，这一步是三维点到三维点的转换，包括 R ，t（相机外参）等参数；
        · 第二部是从相机坐标系转为图像坐标系，这一步是三维点到二维点的转换，包括 K（相机内参）等参数；

## 从世界坐标系到相机坐标系：
这一步是三维点到三维点的转换，包括R ,t （相机外参）等参数
![image](https://github.com/Einstein-666/Camera_Calibration/blob/main/images/101.png)

## 相机坐标系转换为图像坐标系:
这一步是三维点到二维点的转换，包括K（相机内参）等参数
![image](https://github.com/Einstein-666/Camera_Calibration/blob/main/images/102.png)

![image](https://github.com/Einstein-666/Camera_Calibration/blob/main/images/103.png)

根据上述的关系图可以推导出下面的变换公式：
![image](https://github.com/Einstein-666/Camera_Calibration/blob/main/images/104.png)
## 像主点的偏移：
![image](https://github.com/Einstein-666/Camera_Calibration/blob/main/images/105.png)

可以推出
![image](https://github.com/Einstein-666/Camera_Calibration/blob/main/images/106.png)
## 内参矩阵K：
![image](https://github.com/Einstein-666/Camera_Calibration/blob/main/images/107.png)
## 外参矩阵[R | t]:
表示三个方向的偏转：
![image](https://github.com/Einstein-666/Camera_Calibration/blob/main/images/108.png)
## 投影矩阵P
（在这里可以认为旋转矩阵 R 为单位矩阵 I ，平移矩阵 t 都为0）
![image](https://github.com/Einstein-666/Camera_Calibration/blob/main/images/109.png)
根据上述变换最终可以得到一个投影矩阵P的公式为：
![image](https://github.com/Einstein-666/Camera_Calibration/blob/main/images/110.png)
总结一下，公是大致如下：
![image](https://github.com/Einstein-666/Camera_Calibration/blob/main/images/111.png)
## 畸变参数
在几何光学和阴极射线管显示中，畸变是对直线投影的一种偏移。简单来说直线投影是场景内的一条直线投影到图片上也保持为一条直线。那畸变简单来说就是一条直线投影到图片上不能保持为一条直线了，这是一种光学畸变。畸变一般可以分为两大类，包括径向畸变和切向畸变。主要的一般径向畸变有时也会有轻微的切向畸变。
# 特别说明：  
本文原理部分参考地址：https://blog.csdn.net/weixin_43843780/article/details/89294131 

代码部分参考： https://github.com/Nocami/PythonComputerVision-6-CameraCalibration 
