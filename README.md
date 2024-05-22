# PDF Clipboard Cleaner 
剔除复制PDF文字时剪贴板中多余的回车和特殊符号的简易脚本。  

使用方法：  
- 安装Python。
- 将脚本放置在合适的路径。  
- 创建文本文档(后缀名`.txt`)，输入以下批处理命令（**注意修改盘符、路径并删除注释**）：  
````
@echo off
 G:cd G:\_PythonFiles\ %.py File Path%
"G:\anaconda3\python.exe" %Python Path%
clip_copy.py
````
- 保存，后缀名改为`.bat`，双击运行。  
- 按`CapsLock`切换是否清理换行。  


注：用于Xmind等思维导图软件有奇效。
