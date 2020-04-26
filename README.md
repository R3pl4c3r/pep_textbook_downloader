高中人教电子课本下载器
=
环境：python3.7
## 下载依赖
```bash
pip -r requirements.txt     # Windows用这个
pip3 -r requirements.txt    # macOS/Linux用这个
```
### 如果下载速度慢可以使用清华镜像
* Windows
在`C:\Users\xxx\`创建pip文件夹，文件夹内创建一个pip.ini文件
* macOS/Linux 
`
mkdir ~/.pip && vim ~/.pip/pip.conf	# vim这个编辑器可以换成你自己常用的
`

文件内容：
```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```
## 使用
```bash
python textbooks.py     # Windows
python3 textbooks.py    # macOS/Linux
```
## 已知问题
1. wget可能会在下载到末尾时下载不动，记录一下当前文件的序号，然后停止程序并删除未下载完的文件，再修改以下部分重新运行即可
```python
def downloadPdf(bkName, bkUrl):
    for i in range(0, len(bkName)):         # 把0替换为那个序号
        url = bkUrl[i]
        print(i)
        print('\n')
        wget.download(url, bkName[i]+".pdf")
```
2. 人教社上传的书并不全
## 课本文件仓库
[pep_textbook](https://github.com/R3pl4c3r/pep_textbook)
