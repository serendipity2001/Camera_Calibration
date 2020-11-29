from tkinter import *
from PIL import Image, ImageTk
import tt

def Camera_Calibration():
    def calibration():
        path = entry1.get()
        tt.cal(path)

    newWindow = Tk()
    # 设置标题
    newWindow.title('Camera Calibration')
    # 标签控件布局
    Label(newWindow, text="输入图片文件夹",font=('楷体 20')).grid(row=0)
    # Entry控件布局
    entry1 = Entry(newWindow)
    entry1.grid(row=0, column=1)
    # '退出'按钮退出；'确定'按钮打印计算结果
    Button(newWindow, text='退出', command=newWindow.quit,font=('楷体 20')).grid(row=2, column=0, sticky=W, padx=5, pady=5)
    Button(newWindow, text='确定', command=calibration, font=('楷体 20')).grid(row=2, column=1, sticky=W, padx=5, pady=5)
    # 进入消息循环
    newWindow.mainloop()


#初始化Tk()
myWindow = Tk()
#设置标题
myWindow.title('Camera Calibration')
myWindow.resizable(width=True, height=True)
#创建两个按钮
b2=Button(myWindow, text='退出标定', font='楷体 50',relief='raised',width=10, height=2, command=myWindow.quit)
b2.grid(row=1, column=1, sticky=E+W, padx=5, pady=5)
b1=Button(myWindow, text='开始标定',font='楷体 50', relief='raised', width=10, height=2, command=Camera_Calibration)
b1.grid(row=0, column=1, sticky=E+W, padx=5,pady=5)

#进入消息循环
myWindow.mainloop()

