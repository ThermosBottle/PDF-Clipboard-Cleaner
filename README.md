# PPT2PDF_Clipboard Cleaner 将剪贴板复制PPT转化成的PDF课件时产生的回车和制表符号剔除的简易脚本
使用方法：
将脚本放置在合适的路径。
创建文本文档(后缀名`.txt`)，输入以下批处理命令：
````
@echo off
 G:cd G:\_PythonFiles\ %Scripy Path%
"G:\anaconda3\python.exe" %Python Path%
clip_copy.py
````
保存，后缀名改为`.bat`，双击运行。
按`CapsLock`切换是否清理。
