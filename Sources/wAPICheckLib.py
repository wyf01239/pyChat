import os
from importlib import import_module

def wMain(name, file, url, urliswhl):
    '''
    name: str, 库名称, (最好)能在 Pypl 上搜索到
    file: str, 本地安装文件 (whl / tar.gz) 地址, 格式: "./xxx/xxx/xxx.tar.gz" or "./xxx/xxx/xxx.whl"
    url: str, 自定义安装文件下载地址, 文件后缀只能为 .whl 或 .tar.gz
    urliswhl: True / False, 指定下载地址指向的文件是否为 .whl 格式, 如此参数为 False 代表下载地址指向的文件为 .tar.gz 格式
    返回: 已经安装: -1 / 成功: 0 / 失败： 1
    !PS: 从指定 URL 安装, 仅在有 curl.exe 的电脑上可用; 如果不想指定安装文件或下载地址, 请设置为 None.
    '''
    wErr = False
    try:
        import_module(name)
        return -1
    except:
        print("[wAPICheckLib] 未安装库 " + name + ", 正在从本地文件启动安装")
        #
        if os.name == "nt":
            wret = os.system("python -m pip install " + file)
        else:
            wret = os.system("python3 -m pip install " + file)
        if wret != 0:
            print("[wAPICheckLib] 安装失败, 正在尝试从 Pypl 获取 " + name)
            if os.name == "nt":
                wret2 = os.system("python -m pip install " + name)
            else:
                wret2 = os.system("python3 -m pip install " + name)
            if wret2 != 0:
                if os.name == "nt":
                    print("[wAPICheckLib] 获取失败, 正在尝试从 " +
                          url + " 下载并安装 " + name)
                    os.system(
                        "if not exist %TEMP%\\wyf9\\CmdAdmin\\dlLib\\ md %TEMP%\\wyf9\\CmdAdmin\\dlLib\\")
                    os.system(
                        "set TEMP=&&@if exist %TEMP%\\wyf9\\CmdAdmin\\dlLib\\dlLibTemp* (del /f /q %TEMP%\\wyf9\\CmdAdmin\\dlLib\\*)")
                    if urliswhl == True:
                        wret31 = os.system(
                            "curl -o %TEMP%\\wyf9\\CmdAdmin\\dlLib\\dlLibTemp.whl " + url)
                        if wret31 != 0:
                            wErr = True
                        else:
                            wret32 = os.system(
                                "python -m pip install " + "%TEMP%\\wyf9\\CmdAdmin\\dlLib\\dlLibTemp.whl")
                            if wret32 != 0:
                                wErr = True
                    else:
                        wret31 = os.system(
                            "curl -o %TEMP%\\wyf9\\CmdAdmin\\dlLib\\dlLibTemp.tar.gz " + url)
                        if wret31 != 0:
                            wErr = True
                        else:
                            wret32 = os.system(
                                "python -m pip install " + "%TEMP%\\wyf9\\CmdAdmin\\dlLib\\dlLibTemp.tar.gz")
                            if wret32 != 0:
                                wErr = True
                else:
                    wErr = True
            else:
                pass
        else:
            pass
    if wErr == True:
        print("[wAPICheckLib] " + name + " 安装失败, 请自行安装库: " + name +
              "(https://pypi.org/project/" + name + " 或 " + url + ")")
        return 1
    else:
        print("[wAPICheckLib] 成功安装库 " + name)
        return 0