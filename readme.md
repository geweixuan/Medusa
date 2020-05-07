# 一、故事背景
无上的力量即为绝伦的美貌。美杜莎的心中一直靠着这样的想法得以慰藉——她在蛇发女妖三姐妹中年纪最小，也是海洋女神的女儿中最为可人的尤物——因为只有她跟姐妹们不一样，她是凡人。这反而救了她的命，那一天，一群蒙面之徒侵入了蛇发女妖居住的领域，将她两个不朽之身的姐姐从家里拖走，对她们的美貌还是泪水都无动于衷。其中一个入侵者也抓住了美杜莎，但是厌恶地看了一眼后就推向了一旁：“这女的散发着凡胎的臭味。我们可不要。”美杜莎受尽了凌辱，满腔愤懑地逃向了母亲所在的神庙，在女神面前哭诉自己的遭遇。“您拒绝赐予我永生—因此我乞求您，赐予我力量！有了力量我就可以去拯救姐姐们，为受到的不公复仇！”经过长时间的考虑，女神接受了她女儿的请求，美杜莎无与伦比的娇美相貌变成了象征着可怕力量的脸孔。但是她一刻也没有对自己的抉择后悔。她明白，睥睨万物才是值得拥有的美貌—这才是能够改变世界的力量。——from Dota2
# 二、言归正传
本框架主要用于自动化测试。包括接口自动化测试和Web UI自动化测试框架。用例统一由excel维护，用例运行结果通过自动生成html形式测试报告展现。
# 三、技术选型
主要通过requests库实现接口自动化操作、通过selenuim实现Web UI自动化测试。
### 1、接口自动化测试
- requests: python实现的简单易用的http库
### 2、Web UI自动化测试
- nose: python自带框架unittest的扩展，使测试更简单高效
- selenium: 一个强大的开源Web功能测试工具系列， 模拟人为的对浏览器的操作
### 3、公共依赖
- html-testRunner: python标准库的unittest模块的一个扩展,它可以生成HTML的测试报告
- openpyxl、xlrd: python操作excel库
- ddt: python数据驱动，说的简单一点，就是数据测试数据的参数化
### 4、使用教程之接口测试
- 1.通过excel模板编写测试用例
- 2.按照要求修改工程配置
- 3.运行medusa_request.py
- 4.查看测试报告
### 5、使用教程之Web UI测试
modify test from browser 1
