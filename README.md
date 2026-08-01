first commit
Team5-7: 宋宇、李苏阳、林晓晨、王松、徐思强

# Python3 虚拟环境使用方法

本项目使用名为 `.test5900` 的 Python 虚拟环境。

## 创建虚拟环境

macOS / Ubuntu:

```bash
python3 -m venv .test5900
```

Windows:

```powershell
python -m venv .test5900
```

如果 Windows 中 `python` 命令不可用，可以使用：

```powershell
py -3 -m venv .test5900
```

## 进入虚拟环境

macOS / Ubuntu:

```bash
source .test5900/bin/activate
```

Windows PowerShell:

```powershell
.\.test5900\Scripts\Activate.ps1
```

Windows Command Prompt:

```cmd
.test5900\Scripts\activate.bat
```

## 退出虚拟环境

macOS / Ubuntu / Windows:

```bash
deactivate
```

## 安装 requirements 依赖

进入项目目录：

```bash
cd DSCI5900weeksHomeWork
```

先创建并进入 `.test5900` 虚拟环境，然后使用清华源安装依赖：

macOS / Ubuntu:

```bash
python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

Windows PowerShell:

```powershell
python -m pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
```

安装完成后，可以验证 `coverage` 是否安装成功：

```bash
python -m coverage --version
```

如果后续安装了新的第三方库，可以重新生成 `requirements.txt`：

macOS / Ubuntu:

```bash
python -m pip freeze > requirements.txt
```

Windows PowerShell:

```powershell
python -m pip freeze > requirements.txt
```
