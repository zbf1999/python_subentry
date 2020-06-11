#抠图
#https://www.remove.bg/zh   登陆这个网站，拿到自己的key

from removebg import RemoveBg
rmbg = RemoveBg("your key", "error.log")     #fill in your key
path = 'image/removebg'
rmbg.remove_background_from_img_file(f"D:/Desktop/9.jpg")    #照片path

#解决pip请求超时
#pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package