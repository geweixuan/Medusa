@echo off
:: 注意：环境变量设置，系统全局环境变量无法生效情况下使用
:: python3
:: set PATH=%PATH%;E:\tools\python_64bit;E:\tools\python_64bit\Scripts
:: python2.7
:: set PATH=%PATH%;E:\tools\Python27;E:\tools\Python27\Scripts

:: python打包
goto package
:: 复制所需资源
goto copy_resource

::python打包
:package
echo "=============================start package============================="
::pyinstaller -w -i .\data\resources\graphics\icon_logo.ico Mario_Bros.py -y
::pyinstaller -w medusa_request.py -y
pyinstaller medusa_request.spec

::复制运行所需case模板
:copy_resource
echo "=============================copy dependency resources============================="
md dist\Medusa\case
xcopy case dist\Medusa\case /d /e /s /y

::使用call需要放在定义后边
::echo "=============================start package============================="
::call package
::call copy_resource