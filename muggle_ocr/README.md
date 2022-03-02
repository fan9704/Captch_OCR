# （白嫖）这是一个为麻瓜设计的本地OCR模块

只需要简单几步操作即可拥有两大通用识别模块，让你在工作中畅通无阻。



测试图片 test1.png

![](https://kerlomz-blog.oss-cn-beijing.aliyuncs.com/test1.png)

测试图片 test2.jpg

![](https://kerlomz-blog.oss-cn-beijing.aliyuncs.com/test2.jpg)

## SDK类参数

| 参数名     | 必选 | 类型      | 说明                                   |
| ---------- | ---- | --------- | -------------------------------------- |
| model_type | No   | ModelType | 指定预置模型类型                       |
| conf_path  | No   | str       | 指定自定义模型yaml配置文件（绝对路径） |

以上参数两者选其一即可，默认 model_type 为 ModelType.OCR, 若指定 conf_path 参数则优先使用自定义模型。




## 核心API

1. ```SDK.predict(image_bytes: bytes)```



## 使用指北

**注意: 因模块过新，阿里/清华等第三方源可能尚未更新镜像，因此手动指定使用境外源，为了提高依赖的安装速度，可预先自行安装依赖：tensorflow/numpy/opencv-python/pillow/pyyaml**

1. ```pip install muggle-ocr```

2. 调用示例：

   ```python
   import time
   
   # 1. 导入包
   import muggle_ocr
   
   """
   使用预置模型，预置模型包含了[ModelType.OCR, ModelType.Captcha] 两种
   其中 ModelType.OCR 用于识别普通印刷文本, ModelType.Captcha 用于识别4-6位简单英数验证码
   
   """
   
   # 打开印刷文本图片
   with open(r"test1.png", "rb") as f:
       ocr_bytes = f.read()
   
   # 打开验证码图片
   with open(r"test2.jpg", "rb") as f:
       captcha_bytes = f.read()
   
   # 2. 初始化；model_type 可选: [ModelType.OCR, ModelType.Captcha]
   sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.OCR)
   
   # ModelType.Captcha 可识别光学印刷文本
   for i in range(5):
       st = time.time()
       # 3. 调用预测函数
       text = sdk.predict(image_bytes=ocr_bytes)
       print(text, time.time() - st)
   
   # ModelType.Captcha 可识别4-6位验证码
   sdk = muggle_ocr.SDK(model_type=muggle_ocr.ModelType.Captcha)
   for i in range(5):
       st = time.time()
       # 3. 调用预测函数
       text = sdk.predict(image_bytes=captcha_bytes)
       print(text, time.time() - st)
   
   """
   使用自定义模型
   支持基于 https://github.com/kerlomz/captcha_trainer 框架训练的模型
   训练完成后，进入导出编译模型的[out]路径下, 把[graph]路径下的pb模型和[model]下的yaml配置文件放到同一路径下。
   将 conf_path 参数指定为 yaml配置文件 的绝对或项目相对路径即可，其他步骤一致，如下示例：
   """
   with open(r"test3.jpg", "rb") as f:
       b = f.read()
   sdk = muggle_ocr.SDK(conf_path="./ocr.yaml")
   text = sdk.predict(image_bytes=b)
   ```

   

**输出结果:**

```shell script
MuggleOCR Session [ocr] Loaded.
曹文轩教授作序推荐 0.010004520416259766
曹文轩教授作序推荐 0.009941339492797852
曹文轩教授作序推荐 0.0109710693359375
曹文轩教授作序推荐 0.00901031494140625
曹文轩教授作序推荐 0.010967493057250977

MuggleOCR Session [captcha] Loaded.
ceey 0.010970592498779297
ceey 0.009973287582397461
ceey 0.010970592498779297
ceey 0.009973526000976562
ceey 0.009973287582397461
```



OCR和验证码识别的速度基本都在10ms左右，低配CPU可能需要15-20ms。本模块仅支持单行识别，如有多行识别需求请自行采用目标检测预裁图片。

对本项目感兴趣的可以加QQ群交流：857149419