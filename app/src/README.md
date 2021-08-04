## app测试框架结构

### config层
放配置文件，把所有的项目相关的配置均放到这里，
用yaml格式进行配置，实现代码和配置分离


### data层
放数据文件，可以把所有的testcase的参数化相关的
文件放到这里，一般可采用xlsx、csv、xml等格式。
实现数据与代码分离

### drivers层
放所需的驱动，如Chromedriver、IEDriverServer等

### log层
所有生成的日志均存放在这里，可将日志分类，如运行时日志
test log，错误日志error log等

### report层
放程序运行生成的报告，一般可有html报告、excel报告等

### src源码层

#### test层：放所有测试相关的文件

##### case层：测试用例

##### common层：项目相关的抽象通用代码

##### page层：页面类（Page-Object思想）

##### suite层：组织的测试套件

#### utils层
所有的支撑代码都在这里，包括读取config的类、
写log的类、读取excel、xml的类、生成报告的类
（如HTMLTestRunner）、数据库连接、发送邮件
等类和方法，都在这里。

#### READEME.md
加个说明性的文件，告诉团队成员框架需要的环境以及用法

***

### 使用环境

***

### 使用方法
