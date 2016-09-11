#XSS数据接收平台

XSS Receiver Platform based on tornado.

##平台说明

可自由更改生成好的JS

##平台部署

```
docker pull index.alauda.cn/tutum/mongodb
docker run -d --name mongodb -p 27017:27017 -p 28017:28017 -e MONGODB_PASS="mypass" index.alauda.cn/tutum/mongodb
```

```
docker pull index.alauda.cn/security/xss-receiver
docker run --link mongodb -p 80:80 index.alauda.cn/security/xss-receiver
```


##目前支持功能

+ 导出数据
+ XSS cookie的接收

##目录结构

```
handlers                        Handler处理类文件夹
myjs                            我的JS文件夹
templates                       公共模版文件夹
static                          静态资源文件夹
themes/default/templates        网站模版文件夹
app.py                          网站入口
configs.py                      配置文件
Dockerfile                      Docker部署文件
requirements.txt
setting.py                      settings
urls.py                         URL转发
```

##js公共模块

##TODO

##关于