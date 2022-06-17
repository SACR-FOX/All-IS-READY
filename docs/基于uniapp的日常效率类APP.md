---
title: 基于uniapp的日常效率类的APP
author:
  - 李晟迪(1912190417)
  - 黄陈雷(1912190424)
  - 叶轶楠(191219019)
description: |

---

# 一、项目介绍

## 背景

在我们的日常学习生活中，时间管理、文件资料管理是十分重要的，我们会为没有一款优秀的学习助手App而发愁。All IS Ready是一款面向在校学生党的日常效率类助手App，它共有7大功能：To Do List、课程时间表、文件资料管理、学习定时器、学习排行榜、班级任务发布和学习课程社区，可以帮助我们了解每日待办事项、个人课表和班级任务情况。我们也可以通过All IS Ready来对文件资料进行管理，学习定时和与同学们比比学习时长。

## 项目需求分析

- 注册

用户可进行帐号注册。

- 登录

用户根据注册的帐号，输入账号密码后，即可登录成功。

- 主页

主页使用轻盈磁贴式Panel，详实又不失序，快速知道用户的各种需求。快捷导航至

- 学习计时器

用户可以给自己定一个学习计划，自主添加学习事项，设定学习时间，进行学习计时。并且每天看看完成了哪些事，达成了目标的百分之几。学习时长也公开于用户的组织间，进行学习时长的排行。

- 课程时间表

记录用户的课程安排或是定期计划，不同性质的课程赋予不同的主题色，每天的课程一目了然，并且可以云端同步，多端查看。同时，用户可以在按钮处选择自己添加课程或组织批量导入课程，方便美观。

- To Do List

随时将你想做的事，以简单的方式记录下来，All IS Ready能为你生成当日事项安排表或是事件日历，适时提醒，完成奖励，轻松规划你的任务。云端备份，多端同步。在班级组织中，负责人创建任务，可实现全班一键添加，更加高效。

- 文件资料管理

用户可以将需要浏览的文件，按主题归类整理。All IS Ready可以轻松打开本地文件进行浏览，也可以将文件上传至云端，在线打开。

- 账户资料云端备份

用户注册后，将账户资料备份至云端进行保存，永久有效。

- 学习排行榜

看看今天又是谁在霸占着学习排行榜？学习排行榜将实时统计用户所在组织成员的每日学习积累值，让用户的勤奋被更多的人看见。

- 学习课程社区

根据不同的课程，用户可以自主创建课程社区，创建社区话题，并在社区话题下面畅所欲言，分享自己的学习经验或学习感受，与更多的同学交流！

- 班级任务模块

班级负责人可以在此创建组织任务，创建组织课表，发布组织文件。班级内的成员可以在此进行学习排行，比比谁的今日学习时长更长。

![8ea07de0bb8ef081908135754baed03](C:\Users\hp\AppData\Local\Temp\WeChat Files\8ea07de0bb8ef081908135754baed03.png)

## 计划和分工

后端：李晟迪

前端：黄陈雷    叶轶楠

# 二、界面原型设计

## 1.登录注册

<img src="C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220610000736497.png" alt="image-20220610000736497" style="zoom:50%;" /><img src="C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220610001129398.png" alt="image-20220610001129398" style="zoom:50%;" />

登录和注册放在同一个界面中，用户可以通过tapbar 进行切换操作，并且在在此页面进行简单的账号密码勘误。

## 2.主页：

<img src="C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220609235636793.png" alt="image-20220609235636793" style="zoom:50%;" />

主页是用户的入口，是用户基本信息的展示的主要页面，也是各个功能之间的”交通枢纽“。在页面使用磁铁的视觉效果可以让信息更加的简单明了。

## 3.计时器：

<img src="C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220610001657590.png" alt="image-20220610001657590" style="zoom:50%;" />

计时器的主要界面，采用第三方的圆形进度条插件，在界面最显眼的位置显示的当前任务的完成情况，更加的直观和清晰。

## 4.课程表

<img src="C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220610002809835.png" alt="image-20220610002809835" style="zoom:50%;" />

用户可以手动添加课程表，若是已经参与了组织(例如一个班级)，则可以通过组织一件导入课表

## 5.文件管理：

<img src="C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220610005238712.png" alt="image-20220610005238712" style="zoom:50%;" />

用户保存和预览文件的。左部显示文件夹列表，右部显示当前文件列表下的所有文件的列表。通过点击便可以预览文件的列表。

## 6.班级排行榜

<img src="C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220610005910105.png" alt="image-20220610005910105" style="zoom:50%;" />

根据组织进行排行，每当用户采取一系列学习操作后会获得经验值，这些数值会在排行中体现出来。

## 7.班级组织

<img src="C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220610010116983.png" alt="image-20220610010116983" style="zoom:50%;" /><img src="C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220610010728209.png" alt="image-20220610010728209" style="zoom:50%;" /><img src="C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220610010749505.png" alt="image-20220610010749505" style="zoom:50%;" />

班级的组织页面，用户在加入组织后会在此处显示组织管理人发送的通知并进行相应的确认操作。组织管理人也可以通过此处进行任务的发布。

# 三、系统架构设计

## 总体：

![p8](C:\Users\hp\Desktop\LSD\LSD\p8.png)

### 前端：

前端包括To Do List、课程时间表、文件资料管理、学习定时器、学习排行榜、班级任务组织和学习社区模块。

其中学习定时器的内容是根据To Do List模块的待办事项来定的，学习定时器的学习时长关系到学习排行榜的排行情况。班级发布的任务，可以在To Do List中显示；班级的课表可以直接导入到课程时间表中。

由于这次的项目，每个模块之间的关系需要紧密地联系起来，所以我们加入了一个班级任务组织模块，将To Do List、学习定时器、学习排行榜紧密地联系了起来。此外，学习社区、文件资料管理与这些模块又息息相关。

这样设计的优点在于，每个模块之间是紧密联系的，几个模块之间相互制约，相互实现。缺点在于

前端的框架使用了VUE框架。VUE框架只关注视图层，是一个构建数据的视图集合。其视图，数据，结构分离，让数据的赋值和修改更加便捷，只需要操作相关数据即可完成，在实际的使用过程中，非常方便。

文件资料管理模块使用了阿里云OSS对象存储技术，将PDF文件上传至阿里云的OSS服务器中，可以实现云端存储和在线访问。

### 后端：

后端服务采用Django 框架，其优点是开发快，Python语言灵活强大，对主流库的支持性好，成熟稳定。ORM操作设计优秀。在Django框架的基础上采用 Django restframework 框架，进一步提升系统规范性，开发便捷性，（接口符合Restfull规范）。利用Django-crontab，通过crontab 调用服务函数 实现定时任务较SQL事务更方便安全

# 四、API设计

## 接口设计思路：

本应用涉及的数据模块多且复杂 按分类，分别有用户个人数据、组织数据、社区数据，数据集间又相互关联。因此宜采用关系型数据库来描述和管理。我们采用MySql数据库， 其优点是稳定成熟支持性好。其中媒体文件中用户、社区头像头图、社区帖子图片等文件与记录型数据一起存放于服务器media路径中，在数据库中存放文件索引，以供高频访问。用户PDF文件则存放于OSS服务器，在数据库中记录用户文件结构，形成索引。对数据库操作采用Django 封装的ORM 方式进行。数据修改迁移通过migrate方法同步至MySQL。在显示下节课程时，由于需要时时刷新，所以我们利用redis作为查询的缓冲。避免占用太大资源。

## UserProfile

## PUT 修改用户信息

PUT /api/User/Detail/InfoModify/

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 说明   |
| ----- | ----- | ------ | --- | ---- |
| token | query | string | 是   | none |

> 返回示例

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## POST 用户注册

POST /api/User/Register

> Body 请求参数

```yaml
username: string
password: string
stuID: string
header: string
```

### 请求参数

| 名称       | 位置   | 类型             | 必选  | 说明      |
| -------- | ---- | -------------- | --- | ------- |
| body     | body | object         | 否   | none    |
| username | body | string         | 是   | 用户名     |
| password | body | string         | 是   | 密码      |
| stuID    | body | string         | 否   | 学号（可不填） |
| header   | body | string(binary) | 否   | 头像      |

> 返回示例

> 成功

```json
{
  "result": "ok"
}
```

```json
{
  "result": "username already exist"
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## GET 查看用户信息

GET /api/User/Detail/%3CUID%3E/

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 说明   |
| ----- | ----- | ------ | --- | ---- |
| token | query | string | 是   | none |

> 返回示例

> 成功

```json
{
  "UID": 1,
  "Uname": "LSD",
  "OrgID": 1,
  "STUID": 1,
  "Rank": 1,
  "Header": "http://localhost:8000/media/userHeader/communitygreen_IR1YtN7.png",
  "EXP": 3055,
  "Accumulation": 12800
}
```

```json
{
  "detail": "未找到。" 
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

状态码 **200**

| 名称     | 类型     | 必选   | 约束   | 中文名  | 说明   |
| ------ | ------ | ---- | ---- | ---- | ---- |
| UID    | string | true | none |      | none |
| Uname  | string | true | none |      | none |
| OrgID  | string | true | none | 班级ID | none |
| STUID  | string | true | none | 学号   | 暂时不用 |
| Rank   | string | true | none | 等级   | none |
| Header | string | true | none | 头像   | none |
| EXP    | string | true | none | 经验值  | none |

## POST 用户登录

POST /api/User/Login

> Body 请求参数

```yaml
username: string
password: string
```

### 请求参数

| 名称       | 位置   | 类型     | 必选  | 说明   |
| -------- | ---- | ------ | --- | ---- |
| body     | body | object | 否   | none |
| username | body | string | 是   | none |
| password | body | string | 是   | none |

> 返回示例

> 成功

```json
{
  "result": "check passed",
  "code": 200,
  "token": "eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJVSUQiOjEsIlVuYW1lIjoiTFNEIiwiT3JnSUQiOjEsIlJhbmsiOjEwMCwiRVhQIjozNDAsImV4cCI6MTY1MDYyNzM2OX0.vbKxsjSxSIriiz0EgSLyOmzkcjXW87j8LV-5-Y4wMuA",
  "UID": 1,
  "OrgID": 1
}
```

```json
{
  "result": "用户名或密码错误",
  "code": 401
}
```

### 返回结果

| 状态码 | 状态码含义                                                           | 说明  | 数据模型   |
| --- | --------------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)         | 成功  | Inline |
| 401 | [Unauthorized](https://tools.ietf.org/html/rfc7235#section-3.1) | 失败  | Inline |

### 返回数据结构

状态码 **200**

| 名称     | 类型      | 必选   | 约束   | 中文名 | 说明   |
| ------ | ------- | ---- | ---- | --- | ---- |
| result | string  | true | none | 结果  | none |
| code   | integer | true | none |     | none |
| token  | string  | true | none |     | none |

状态码 **401**

| 名称     | 类型      | 必选   | 约束   | 中文名 | 说明   |
| ------ | ------- | ---- | ---- | --- | ---- |
| result | string  | true | none |     | none |
| code   | integer | true | none |     | none |

# ToDoList

## POST 按组织号批量导入

POST /api/ToDoList/GroupImport

> Body 请求参数

```yaml
OrgID: string
```

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 说明   |
| ----- | ----- | ------ | --- | ---- |
| token | query | string | 否   | none |
| body  | body  | object | 否   | none |
| OrgID | body  | string | 否   | none |

> 返回示例

> 成功

```json
{
  "result": "err"
}
```

```json
{
  "result": "ok"
}
```

```json
{
  "result": "match nothing"
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## GET 情况统计

GET /api/ToDoList/Statistics

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 说明   |
| ----- | ----- | ------ | --- | ---- |
| token | query | string | 否   | none |

> 返回示例

> 成功

```json
{
  "today": 2,
  "all_in_plan": 3,
  "finished": 1
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## PUT 修改ToDoList项

PUT /http:101.37.175.115/api/ToDoList/Action/%3CID%3E/Modify/

> Body 请求参数

```yaml
Tag: string
ItemName: string
Time: string
```

### 请求参数

| 名称       | 位置    | 类型     | 必选  | 说明   |
| -------- | ----- | ------ | --- | ---- |
| token    | query | string | 是   | 事项ID |
| body     | body  | object | 否   | none |
| Tag      | body  | string | 否   | none |
| ItemName | body  | string | 否   | none |
| Time     | body  | string | 否   | none |

> 返回示例

> 成功

```json
{
  "ID": 10,
  "OrgID": 2,
  "ItemName": "qd",
  "Time": 1651890796,
  "Status": false,
  "Tag": 2
}
```

```json
{
  "Time": [
    "interval invalid"
  ]
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

状态码 **200**

| 名称     | 类型     | 必选   | 约束   | 中文名 | 说明   |
| ------ | ------ | ---- | ---- | --- | ---- |
| result | string | true | none |     | none |

## GET 列出该用户今日所有事项

GET /api/ToDoList/Today

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 说明   |
| ----- | ----- | ------ | --- | ---- |
| token | query | string | 是   | none |

> 返回示例

> 成功

```json
[
  {
    "ID": 1,
    "OrgID": -1,
    "ItemName": "早课2",
    "Time": 1651813726,
    "Status": false,
    "Tag": 6
  },
  {
    "ID": 7,
    "OrgID": 1,
    "ItemName": "作业1",
    "Time": 1651813726,
    "Status": false,
    "Tag": 2
  }
]
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## GET 根据Tag 筛选展示

GET /api/ToDoList/AllByTag

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 说明   |
| ----- | ----- | ------ | --- | ---- |
| token | query | string | 是   | none |
| Tag   | query | string | 是   | none |

> 返回示例

> 成功

```json
[
  {
    "ID": 8,
    "OrgID": 1,
    "ItemName": "作业2",
    "Time": 1649428986,
    "Status": false,
    "Tag": 6
  },
  {
    "ID": 1,
    "OrgID": -1,
    "ItemName": "早课2",
    "Time": 1651813726,
    "Status": false,
    "Tag": 6
  },
  {
    "ID": 7,
    "OrgID": 1,
    "ItemName": "作业1",
    "Time": 1651813726,
    "Status": false,
    "Tag": 6
  }
]
```

> 请求有误

```json
{
  "result": "bad request"
}
```

### 返回结果

| 状态码 | 状态码含义                                                            | 说明   | 数据模型   |
| --- | ---------------------------------------------------------------- | ---- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)          | 成功   | Inline |
| 400 | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求有误 | Inline |

### 返回数据结构

## DELETE 删除事项

DELETE /api/ToDoList/Action/%3CID%3E/

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 说明   |
| ----- | ----- | ------ | --- | ---- |
| token | query | string | 是   | none |

> 返回示例

### 返回结果

| 状态码 | 状态码含义                                                           | 说明   | 数据模型   |
| --- | --------------------------------------------------------------- | ---- | ------ |
| 204 | [No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5) | 删除成功 | Inline |

### 返回数据结构

## POST 添加ToDoList

POST /http:/101.37.175.115/api/ToDoList/Action/

> Body 请求参数

```json
{
  "OrgID": 0,
  "UID": "string",
  "Time": "string",
  "ItemName": "string",
  "UUID": "string",
  "Tag": "string"
}
```

### 请求参数

| 名称       | 位置    | 类型      | 必选  | 中文名    | 说明                  |
| -------- | ----- | ------- | --- | ------ | ------------------- |
| token    | query | string  | 是   |        | none                |
| body     | body  | object  | 否   |        | none                |
| OrgID    | body  | integer | 是   | 组织ID   | 个人创建 -1 ，为组织创建填组织ID |
| UID      | body  | string  | 是   | 所属用户ID | none                |
| Time     | body  | string  | 否   | 提醒时间   | none                |
| ItemName | body  | string  | 是   | 计划名称   | none                |
| UUID     | body  | string  | 是   |        | none                |
| Tag      | body  | string  | 是   |        | none                |

> 返回示例

> 成功

```json
{
  "ID": 9,
  "OrgID": -1,
  "ItemName": "吃饭",
  "Time": 1649473215,
  "Status": false,
  "Tag": 2
}
```

```json
{
  "Time": [
    "interval invalid"
  ]
}
```

### 返回结果

| 状态码 | 状态码含义                                                        | 说明  | 数据模型   |
| --- | ------------------------------------------------------------ | --- | ------ |
| 201 | [Created](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 成功  | Inline |

### 返回数据结构

状态码 **201**

| 名称     | 类型     | 必选   | 约束   | 中文名 | 说明   |
| ------ | ------ | ---- | ---- | --- | ---- |
| result | string | true | none |     | none |

## PUT 修改完成状况

PUT /api/ToDoList/Action/%3CID%3E/Done/

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 是   |     | 事项ID |

> 返回示例

> 成功

```json
{
  "result": "success"
}
```

> 禁止访问

```json
{
  "result": "user not match"
}
```

### 返回结果

| 状态码 | 状态码含义                                                          | 说明   | 数据模型   |
| --- | -------------------------------------------------------------- | ---- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)        | 成功   | Inline |
| 403 | [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3) | 禁止访问 | Inline |

### 返回数据结构

状态码 **200**

| 名称     | 类型     | 必选   | 约束   | 中文名 | 说明   |
| ------ | ------ | ---- | ---- | --- | ---- |
| result | string | true | none |     | none |

## GET 列出该用户所有事项

GET /api/ToDoList/All

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 是   |     | none |

> 返回示例

> 成功

```json
[
  {
    "ID": 1,
    "OrgID": -1,
    "ItemName": "早课2",
    "Time": 1649344533,
    "Status": true,
    "Tag": 6
  },
  {
    "ID": 7,
    "OrgID": 1,
    "ItemName": "作业1",
    "Time": 1649428986,
    "Status": false,
    "Tag": 2
  },
  {
    "ID": 8,
    "OrgID": 1,
    "ItemName": "作业2",
    "Time": 1649428986,
    "Status": false,
    "Tag": 3
  },
  {
    "ID": 4,
    "OrgID": -1,
    "ItemName": "后天抬水",
    "Time": 1649430000,
    "Status": true,
    "Tag": 2
  }
]
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

# File

## POST 上传云端

POST /api/Files/upload

> Body 请求参数

```yaml
"OrgID ": string
FolderName: string
FileName: string
book: string
```

### 请求参数

| 名称         | 位置    | 类型             | 必选  | 中文名 | 说明       |
| ---------- | ----- | -------------- | --- | --- | -------- |
| token      | query | string         | 是   |     | none     |
| body       | body  | object         | 否   |     | none     |
| OrgID      | body  | string         | 是   |     | 个人上传 填-1 |
| FolderName | body  | string         | 是   |     | none     |
| FileName   | body  | string         | 否   |     | 重命名就加上   |
| book       | body  | string(binary) | 是   |     | none     |

> 返回示例

> oss服务器错误

```json
{
  "result": "oss upload failed"
}
```

```json
{
  "UID": 1,
  "OrgID": -1,
  "FolderName": "雅思",
  "FileName": "雅思口语part1",
  "Renewal": 1650594491
}
```

> 请求有误

```json
{
  "result": "no file detect"
}
```

> 记录不存在

```json
{
  "detail": "未找到。"
}
```

> 服务器错误

```json
{
  "result": "cache save failed"
}
```

### 返回结果

| 状态码 | 状态码含义                                                                      | 说明    | 数据模型   |
| --- | -------------------------------------------------------------------------- | ----- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)                    | 成功    | Inline |
| 400 | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)           | 请求有误  | Inline |
| 404 | [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)             | 记录不存在 | Inline |
| 500 | [Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1) | 服务器错误 | Inline |

### 返回数据结构

状态码 **200**

| 名称       | 类型     | 必选   | 约束   | 中文名 | 说明   |
| -------- | ------ | ---- | ---- | --- | ---- |
| » result | string | true | none |     | none |

## GET 显示指定文件夹下文件列表

GET /api/Files/FileList

> Body 请求参数

```yaml
{}
```

### 请求参数

| 名称     | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ------ | ----- | ------ | --- | --- | ---- |
| token  | query | string | 是   |     | none |
| Folder | query | string | 是   |     | none |
| OrgID  | query | string | 否   |     | none |

> 返回示例

> 成功

```json
{
  "list": [
    {
      "FileName": "8LinuxUbuntu.docx",
      "ID": 6
    }
  ]
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

状态码 **200**

| 名称       | 类型     | 必选   | 约束   | 中文名 | 说明   |
| -------- | ------ | ---- | ---- | --- | ---- |
| » result | string | true | none |     | none |

## GET 显示文件夹列表

GET /api/Files/FolderList

> Body 请求参数

```yaml
{}
```

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明        |
| ----- | ----- | ------ | --- | --- | --------- |
| token | query | string | 是   |     | none      |
| OrgID | query | string | 否   |     | 若是组织文件则带上 |
| body  | body  | object | 否   |     | none      |

> 返回示例

> 成功

```json
{
  "list": [
    {
      "FolderName": "申请"
    },
    {
      "FolderName": "雅思"
    }
  ]
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

状态码 **200**

| 名称         | 类型       | 必选   | 约束   | 中文名 | 说明   |
| ---------- | -------- | ---- | ---- | --- | ---- |
| » data     | [object] | true | none |     | none |
| »» FID     | string   | true | none |     | none |
| »» Fname   | string   | true | none |     | none |
| »» Uri     | string   | true | none |     | none |
| »» Theme   | string   | true | none |     | none |
| »» Renewal | string   | true | none |     | none |
| » result   | string   | true | none |     | none |

## GET 文件在线预览连接

GET /api/Files/OnlinePreview

> Body 请求参数

```yaml
{}
```

### 请求参数

| 名称     | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ------ | ----- | ------ | --- | --- | ---- |
| token  | query | string | 是   |     | none |
| FileID | query | string | 是   |     | none |
| OrgID  | query | string | 否   |     | none |
| body   | body  | object | 否   |     | none |

> 返回示例

> 成功

```json
{
  "url": "http://all-is-ready-file-storage.oss-cn-hangzhou.aliyuncs.com/userPDF/1/%E9%9B%85%E6%80%9D/%E9%9B%85%E6%80%9D%E5%8F%A3%E8%AF%ADpart1?OSSAccessKeyId=LTAI5tNtrJxgmQ5pgAMjGoH2&Expires=1650605739&Signature=FuKxVAw4SEIRKL37VDxoqHa0fgQ%3D"
}
```

> 无内容

```json
{
  "result": "no such file"
}
```

> OSS服务器错误

```json
{
  "result": "OSS sign err"
}
```

### 返回结果

| 状态码 | 状态码含义                                                                      | 说明       | 数据模型   |
| --- | -------------------------------------------------------------------------- | -------- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)                    | 成功       | Inline |
| 204 | [No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5)            | 无内容      | Inline |
| 500 | [Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1) | OSS服务器错误 | Inline |

### 返回数据结构

状态码 **200**

| 名称     | 类型     | 必选   | 约束   | 中文名 | 说明   |
| ------ | ------ | ---- | ---- | --- | ---- |
| Uri    | string | true | none |     | none |
| result | string | true | none |     | none |

# ClassSchedule

## POST 组织批量导入课程

POST /api/Schedule/GroupImport/

> Body 请求参数

```yaml
{}
```

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 是   |     | none |
| body  | body  | object | 否   |     | none |

> 返回示例

> 成功

```json
{
  "result": "ok"
}
```

```json
{
  "result": "internal error"
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

状态码 **200**

| 名称     | 类型     | 必选   | 约束   | 中文名 | 说明  |
| ------ | ------ | ---- | ---- | --- | --- |
| result | string | true | none |     | 结果  |

## PUT 修改课程信息

PUT /api/Schedule/Action/%3CScheduleID%3E/Modify/

> Body 请求参数

```yaml
DurationStart: string
DurationEnd: string
Location: string
CurName: string
Tag: string
```

### 请求参数

| 名称            | 位置    | 类型     | 必选  | 中文名 | 说明       |
| ------------- | ----- | ------ | --- | --- | -------- |
| token         | query | string | 否   |     | none     |
| body          | body  | object | 否   |     | none     |
| DurationStart | body  | string | 否   |     | 课程开始相对时间 |
| DurationEnd   | body  | string | 否   |     | 课程结束相对时间 |
| Location      | body  | string | 否   |     | 课程位置     |
| CurName       | body  | string | 否   |     | 课程名称     |
| Tag           | body  | string | 否   |     | 标签颜色     |

> 返回示例

> 成功

```json
{
  "ScheduleID": 22,
  "DurationStart": 68400,
  "DurationEnd": 73000,
  "CurName": "test_by_lsd_and_hdn",
  "Tag": 2,
  "Location": "C423"
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## GET 查看下一节课程

GET /api/Schedule/Next/

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 是   |     | none |

> 返回示例

> 成功

```json
{
  "CurName": "uuid TEst",
  "Location": "E309",
  "Tag": 4
}
```

```json
{
  "result": "internal error"
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## GET 查看当天课程表

GET /api/Schedule/byDay

> Body 请求参数

```yaml
{}
```

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 是   |     | none |
| Day   | query | string | 是   |     | 礼拜几  |
| body  | body  | object | 否   |     | none |

> 返回示例

> 成功

```json
{
  "content": [
    {
      "ScheduleID": 18,
      "CurName": "uuid TEst",
      "Location": "E309",
      "Tag": 4,
      "Start": "22:43",
      "End": "25:01"
    },
    {
      "ScheduleID": 6,
      "CurName": "test2",
      "Location": "",
      "Tag": 3,
      "Start": "25:00",
      "End": "25:01"
    }
  ],
  "result": "ok"
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## DELETE 删除课程

DELETE /api/Schedule/Action/%3CScheduleID%3E/

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 是   |     | none |

> 返回示例

### 返回结果

| 状态码 | 状态码含义                                                           | 说明   | 数据模型   |
| --- | --------------------------------------------------------------- | ---- | ------ |
| 204 | [No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5) | 删除成功 | Inline |

### 返回数据结构

## POST 添加课程

POST /175.115/api/Schedule/Action/

> Body 请求参数

```yaml
Day: 3 （礼拜三）
OrgID: string
DurationStart: string
DurationEnd: string
Loaction: string
CurName: string
Tag: string
UUID: string
UID: string
```

### 请求参数

| 名称            | 位置    | 类型     | 必选  | 中文名 | 说明        |
| ------------- | ----- | ------ | --- | --- | --------- |
| token         | query | string | 是   |     | none      |
| body          | body  | object | 否   |     | none      |
| Day           | body  | string | 是   |     | 课程所在星期    |
| OrgID         | body  | string | 否   |     | 组织ID      |
| DurationStart | body  | string | 是   |     | 课程开始相对时间戳 |
| DurationEnd   | body  | string | 是   |     | 课程结束相对时间戳 |
| Loaction      | body  | string | 否   |     | 上课地点      |
| CurName       | body  | string | 是   |     | 课程名称      |
| Tag           | body  | string | 否   |     | 标签颜色      |
| UUID          | body  | string | 是   |     | 课程唯一标识    |
| UID           | body  | string | 是   |     | none      |

> 返回示例

> 成功

```json
{
  "ScheduleID": 22,
  "DurationStart": 68400,
  "DurationEnd": 73000,
  "CurName": "test_by_lsd",
  "Tag": 2,
  "Location": "C423"
}
```

### 返回结果

| 状态码 | 状态码含义                                                        | 说明  | 数据模型   |
| --- | ------------------------------------------------------------ | --- | ------ |
| 201 | [Created](https://tools.ietf.org/html/rfc7231#section-6.3.2) | 成功  | Inline |

### 返回数据结构

# Community

## POST 创建话题

POST /api/Community/Topic/Create/

> Body 请求参数

```yaml
CommunityID: string
HasImage: True False
Title: string
TopicPic: string
```

### 请求参数

| 名称          | 位置    | 类型             | 必选  | 中文名 | 说明              |
| ----------- | ----- | -------------- | --- | --- | --------------- |
| token       | query | string         | 是   |     | none            |
| body        | body  | object         | 否   |     | none            |
| CommunityID | body  | string         | 否   |     | none            |
| HasImage    | body  | string         | 是   |     | none            |
| Title       | body  | string         | 否   |     | none            |
| TopicPic    | body  | string(binary) | 否   |     | HasImage为True时填 |

> 返回示例

> 成功

```json
{
  "result": "ok"
}
```

> 服务器错误

```json
{
  "result": "internal error"
}
```

```json
{
  "result": "save image faild"
}
```

### 返回结果

| 状态码 | 状态码含义                                                                      | 说明    | 数据模型   |
| --- | -------------------------------------------------------------------------- | ----- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)                    | 成功    | Inline |
| 400 | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)           | 请求有误  | Inline |
| 500 | [Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1) | 服务器错误 | Inline |

### 返回数据结构

状态码 **200**

| 名称     | 类型     | 必选   | 约束   | 中文名 | 说明   |
| ------ | ------ | ---- | ---- | --- | ---- |
| result | string | true | none |     | none |

## PUT 修改社区资料

PUT /api/Community/Action/%3CCommunityID%3E/Modify/

> Body 请求参数

```yaml
PostID: string
```

### 请求参数

| 名称     | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ------ | ----- | ------ | --- | --- | ---- |
| token  | query | string | 是   |     | none |
| body   | body  | object | 否   |     | none |
| PostID | body  | string | 否   |     | none |

> 返回示例

> 成功

```json
{
  "CommunityID": 1,
  "CommunityName": "OS-2022",
  "PostCount": 0,
  "AdministratorID": 1,
  "Renewal": 1652770187,
  "Poster": "/media/communityHeader/jiahao.png",
  "Description": "社区资料修改测试2"
}
```

> 禁止访问

```json
{
  "result": "Permission Denied"
}
```

> 记录不存在

```json
{
  "result": "CommunityID not match"
}
```

```json
{
  "result": "user not exit"
}
```

> 服务器错误

```json
{
  "result": "get pic failed"
}
```

### 返回结果

| 状态码 | 状态码含义                                                                      | 说明    | 数据模型   |
| --- | -------------------------------------------------------------------------- | ----- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)                    | 成功    | Inline |
| 403 | [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)             | 禁止访问  | Inline |
| 404 | [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)             | 记录不存在 | Inline |
| 500 | [Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1) | 服务器错误 | Inline |

### 返回数据结构

## GET 显示所有社区

GET /api/Community/Action

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 是   |     | none |
| page  | query | string | 是   |     | 默认1  |

> 返回示例

> 成功

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "CommunityID": 1,
      "CommunityName": "OS2022",
      "PostCount": 0,
      "AdministratorID": 1,
      "Renewal": 0,
      "Poster": "http://localhost:8000/media/communityHeader/IMG_0615_W0D3Ngq.jpg",
      "Description": "操作系统课程社区"
    },
    {
      "CommunityID": 2,
      "CommunityName": "编译原理",
      "PostCount": 0,
      "AdministratorID": 2,
      "Renewal": 0,
      "Poster": "http://localhost:8000/media/communityHeader/IMG_3994.JPG",
      "Description": "编译原理社区"
    }
  ]
}
```

> 记录不存在

```json
{
  "detail": "无效页面。"
}
```

### 返回结果

| 状态码 | 状态码含义                                                          | 说明    | 数据模型   |
| --- | -------------------------------------------------------------- | ----- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)        | 成功    | Inline |
| 404 | [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4) | 记录不存在 | Inline |

### 返回数据结构

## POST 创建社区

POST /api/Community/Action/

> Body 请求参数

```yaml
CommunityName: string
AdministratorID: string
Poster: string
Description: string
```

### 请求参数

| 名称              | 位置   | 类型             | 必选  | 中文名 | 说明        |
| --------------- | ---- | -------------- | --- | --- | --------- |
| body            | body | object         | 否   |     | none      |
| CommunityName   | body | string         | 是   |     | none      |
| AdministratorID | body | string         | 否   |     | 创建者/管理者ID |
| Poster          | body | string(binary) | 否   |     | 社区头像      |
| Description     | body | string         | 否   |     | none      |

> 返回示例

> 成功

```json
{
  "CommunityID": 3,
  "CommunityName": "移动开发",
  "PostCount": 0,
  "AdministratorID": 2,
  "Renewal": 0,
  "Poster": "http://localhost:8000/media/communityHeader/IMG_3994_vJeOunp.JPG",
  "Description": "社区创建测试"
}
```

> 请求有误

```json
{
  "CommunityName": [
    "社区名已存在"
  ]
}
```

### 返回结果

| 状态码 | 状态码含义                                                            | 说明   | 数据模型   |
| --- | ---------------------------------------------------------------- | ---- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)          | 成功   | Inline |
| 400 | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求有误 | Inline |

### 返回数据结构

状态码 **200**

| 名称       | 类型     | 必选   | 约束   | 中文名 | 说明   |
| -------- | ------ | ---- | ---- | --- | ---- |
| » result | string | true | none |     | none |

## PUT 修改话题

PUT /api/Community/Topic/%3CTopicID%3E/Modify/

> Body 请求参数

```yaml
Title: string
HasImage: True False
TopicPic: string
```

### 请求参数

| 名称       | 位置    | 类型             | 必选  | 中文名 | 说明               |
| -------- | ----- | -------------- | --- | --- | ---------------- |
| token    | query | string         | 是   |     | none             |
| body     | body  | object         | 否   |     | none             |
| Title    | body  | string         | 否   |     | none             |
| HasImage | body  | string         | 是   |     | 是否修改头图           |
| TopicPic | body  | string(binary) | 否   |     | HasImage=True 带上 |

> 返回示例

> 成功

```json
{
  "TopicID": 12,
  "CommunityID": 1,
  "UID": 1,
  "Time": 1652770187,
  "HasImage": true,
  "Title": "话题修改测试2",
  "ImageUri": "/media/TopicHeader/biaoge.png",
  "Stars": 0
}
```

> 禁止访问

```json
{
  "result": "Permission Denied"
}
```

> 记录不存在

```json
{
  "result": "ID not Match"
}
```

> 服务器错误

```json
{
  "result": "get pic failed"
}
```

### 返回结果

| 状态码 | 状态码含义                                                                      | 说明    | 数据模型   |
| --- | -------------------------------------------------------------------------- | ----- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)                    | 成功    | Inline |
| 403 | [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)             | 禁止访问  | Inline |
| 404 | [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)             | 记录不存在 | Inline |
| 500 | [Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1) | 服务器错误 | Inline |

### 返回数据结构

## GET 显示所有话题

GET /api/Community/Topic_All

> Body 请求参数

```yaml
CommunityID: string
```

### 请求参数

| 名称          | 位置    | 类型     | 必选  | 中文名 | 说明    |
| ----------- | ----- | ------ | --- | --- | ----- |
| token       | query | string | 是   |     | none  |
| CommunityID | query | string | 是   |     | none  |
| page        | query | string | 是   |     | 默认第1页 |
| body        | body  | object | 否   |     | none  |

> 返回示例

> 成功

```json
{
  "next": false,
  "previous": false,
  "count": 2,
  "data": [
    {
      "TopicID": 10,
      "UID": 1,
      "header": "http://101.37.175.115/media/userHeader/communitygreen.png",
      "Creator": "LSD",
      "Time": 1649809036,
      "HasImage": true,
      "ImageUri": "http://101.37.175.115/media/TopicHeader/biaoge_eYunvQd.png",
      "Title": "话题修改测试5",
      "Stars": 1
    },
    {
      "TopicID": 12,
      "UID": 1,
      "header": "http://101.37.175.115/media/userHeader/communitygreen.png",
      "Creator": "LSD",
      "Time": 1652770187,
      "HasImage": true,
      "ImageUri": "http://101.37.175.115/media/TopicHeader/biaoge.png",
      "Title": "话题修改测试2",
      "Stars": 0
    }
  ]
}
```

```json
{
  "result": "empty"
}
```

> 记录不存在

```json
{
  "detail": "无效页面。"
}
```

### 返回结果

| 状态码 | 状态码含义                                                          | 说明    | 数据模型   |
| --- | -------------------------------------------------------------- | ----- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)        | 成功    | Inline |
| 404 | [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4) | 记录不存在 | Inline |

### 返回数据结构

## POST 点赞话题

POST /api/Community/Topic/%3CTopicID%3E/Star/

> Body 请求参数

```yaml
{}
```

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 是   |     | none |
| body  | body  | object | 否   |     | none |

> 返回示例

> 成功

```json
{
  "result": "ok"
}
```

> 禁止访问

```json
{
  "result": "already thumbed"
}
```

> 记录不存在

```json
{
  "result": "TopicID don't match"
}
```

> 服务器错误

```json
{
  "result": "internal err"
}
```

### 返回结果

| 状态码 | 状态码含义                                                                      | 说明    | 数据模型   |
| --- | -------------------------------------------------------------------------- | ----- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)                    | 成功    | Inline |
| 403 | [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)             | 禁止访问  | Inline |
| 404 | [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)             | 记录不存在 | Inline |
| 500 | [Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1) | 服务器错误 | Inline |

### 返回数据结构

## GET 显示话题信息

GET /api/Community/Topic/%3CTopicID%3E/

> Body 请求参数

```yaml
PostID: string
```

### 请求参数

| 名称     | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ------ | ----- | ------ | --- | --- | ---- |
| token  | query | string | 否   |     | none |
| body   | body  | object | 否   |     | none |
| PostID | body  | string | 否   |     | none |

> 返回示例

> 成功

```json
{
  "TopicID": 11,
  "CommunityID": 2,
  "UID": 1,
  "Time": 1649810112,
  "HasImage": true,
  "Title": "话题三",
  "ImageUri": "http://localhost:8000/media/TopicHeader/communitygreen.png",
  "Stars": 0
}
```

> 记录不存在

```json
{
  "detail": "未找到。"
}
```

### 返回结果

| 状态码 | 状态码含义                                                          | 说明    | 数据模型   |
| --- | -------------------------------------------------------------- | ----- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)        | 成功    | Inline |
| 404 | [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4) | 记录不存在 | Inline |

### 返回数据结构

## GET 显示话题下所有帖子

GET /api/Community/Post_All

> Body 请求参数

```yaml
{}
```

### 请求参数

| 名称      | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ------- | ----- | ------ | --- | --- | ---- |
| token   | query | string | 是   |     | none |
| page    | query | string | 是   |     | none |
| TopicID | query | string | 是   |     | none |

> 返回示例

> 成功

```json
{
  "next": false,
  "previous": false,
  "count": 2,
  "result": [
    {
      "PostID": 2,
      "TopicID": 10,
      "UID": 1,
      "header": "http://101.37.175.115/media/userHeader/communitygreen.png",
      "Creator": "LSD",
      "Time": 1649817052,
      "HasImage": true,
      "Content": "支持一下",
      "pics": [
        "http://101.37.175.115/media/PostImage/home2.png",
        "http://101.37.175.115/media/PostImage/jiahao.png"
      ],
      "Stars": 0
    },
    {
      "PostID": 1,
      "TopicID": 10,
      "UID": 1,
      "header": "http://101.37.175.115/media/userHeader/communitygreen.png",
      "Creator": "LSD",
      "Time": 1649816781,
      "HasImage": false,
      "Content": "支持一下",
      "Stars": 1
    }
  ]
}
```

> 服务器错误

```json
{
  "result": "internal error"
}
```

### 返回结果

| 状态码 | 状态码含义                                                                      | 说明    | 数据模型   |
| --- | -------------------------------------------------------------------------- | ----- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)                    | 成功    | Inline |
| 500 | [Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1) | 服务器错误 | Inline |

### 返回数据结构

## POST 发帖

POST /api/Community/Post/Create/

> Body 请求参数

```yaml
TopicID: string
HasImage: True False
Content: string
PostPic: string
```

### 请求参数

| 名称       | 位置    | 类型             | 必选  | 中文名 | 说明                  |
| -------- | ----- | -------------- | --- | --- | ------------------- |
| token    | query | string         | 是   |     | none                |
| body     | body  | object         | 否   |     | none                |
| TopicID  | body  | string         | 是   |     | none                |
| HasImage | body  | string         | 是   |     | none                |
| Content  | body  | string         | 是   |     | 文字内容                |
| PostPic  | body  | string(binary) | 否   |     | HasImage 为True 时 带上 |

> 返回示例

> 成功

```json
{
  "result": "ok"
}
```

> 请求有误

```json
{
  "result": "话题ID错误"
}
```

> 服务器错误

```json
{
  "result": "save image faild"
}
```

```json
{
  "result": "internal error"
}
```

### 返回结果

| 状态码 | 状态码含义                                                                      | 说明    | 数据模型   |
| --- | -------------------------------------------------------------------------- | ----- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)                    | 成功    | Inline |
| 400 | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1)           | 请求有误  | Inline |
| 500 | [Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1) | 服务器错误 | Inline |

### 返回数据结构

状态码 **200**

| 名称     | 类型     | 必选   | 约束   | 中文名 | 说明   |
| ------ | ------ | ---- | ---- | --- | ---- |
| result | string | true | none |     | none |

## POST 查询点赞情况

POST /api/Community/checkStar/

> Body 请求参数

```yaml
ID: string
type: string
```

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明             |
| ----- | ----- | ------ | --- | --- | -------------- |
| token | query | string | 是   |     | none           |
| body  | body  | object | 否   |     | none           |
| ID    | body  | string | 是   |     | none           |
| type  | body  | string | 是   |     | 点赞类型 主题:0 帖子:1 |

> 返回示例

> 成功

```json
{
  "result": false
}
```

```json
{
  "result": true
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## PUT 修改帖子

PUT /api/Community/Post/%3CPostID%3E/Modify/

> Body 请求参数

```yaml
HasImage: True False
Content: string
PostPic: string
```

### 请求参数

| 名称       | 位置    | 类型             | 必选  | 中文名 | 说明                     |
| -------- | ----- | -------------- | --- | --- | ---------------------- |
| token    | query | string         | 是   |     | none                   |
| body     | body  | object         | 否   |     | none                   |
| HasImage | body  | string         | 是   |     | True 修改图片 False 仅修改内容  |
| Content  | body  | string         | 否   |     | none                   |
| PostPic  | body  | string(binary) | 否   |     | HasImage 为True时修改图片，带上 |

> 返回示例

> 成功

```json
{
  "PostID": 5,
  "TopicID": 11,
  "UID": 1,
  "Time": 1652771706,
  "HasImage": true,
  "Content": "帖子修改测试2",
  "Stars": 0
}
```

> 记录不存在

```json
{
  "result": "ID not Match"
}
```

> 服务器错误

```json
{
  "result": "save image faild"
}
```

### 返回结果

| 状态码 | 状态码含义                                                                      | 说明    | 数据模型   |
| --- | -------------------------------------------------------------------------- | ----- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)                    | 成功    | Inline |
| 404 | [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)             | 记录不存在 | Inline |
| 500 | [Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1) | 服务器错误 | Inline |

### 返回数据结构

## POST 点赞帖子

POST /api/Community/Post/%3CPostID%3E/Star/

> Body 请求参数

```yaml
{}
```

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 是   |     | none |
| body  | body  | object | 否   |     | none |

> 返回示例

> 成功

```json
{
  "result": "ok"
}
```

> 禁止访问

```json
{
  "result": "already thumbed"
}
```

> 记录不存在

```json
{
  "result": "PostID don't match"
}
```

> 服务器错误

```json
{
  "result": "internal err"
}
```

### 返回结果

| 状态码 | 状态码含义                                                                      | 说明    | 数据模型   |
| --- | -------------------------------------------------------------------------- | ----- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)                    | 成功    | Inline |
| 403 | [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3)             | 禁止访问  | Inline |
| 404 | [Not Found](https://tools.ietf.org/html/rfc7231#section-6.5.4)             | 记录不存在 | Inline |
| 500 | [Internal Server Error](https://tools.ietf.org/html/rfc7231#section-6.6.1) | 服务器错误 | Inline |

### 返回数据结构

# Organization

## POST 创建组织任务

POST /api/Organization/Task/Action/

> Body 请求参数

```yaml
OrgID: string
TimeStart: string
TimeDue: string
Description: string
TaskName: string
Creator: string
CID: string
```

### 请求参数

| 名称          | 位置    | 类型     | 必选  | 中文名 | 说明     |
| ----------- | ----- | ------ | --- | --- | ------ |
| token       | query | string | 是   |     | none   |
| body        | body  | object | 否   |     | none   |
| OrgID       | body  | string | 是   |     | 组织ID   |
| TimeStart   | body  | string | 是   |     | 任务开始时间 |
| TimeDue     | body  | string | 是   |     | 任务到期时间 |
| Description | body  | string | 否   |     | 描述     |
| TaskName    | body  | string | 是   |     | 任务标题   |
| Creator     | body  | string | 否   |     | 创建者姓名  |
| CID         | body  | string | 否   |     | 绑定课程ID |

> 返回示例

> 成功

```json
{
  "TaskID": 4,
  "OrgID": 1,
  "CID": 12,
  "TimeStart": 1652166954,
  "TimeDue": 1652339754,
  "Status": true,
  "Description": "大部分将卡萨顶顶",
  "TaskName": "测试测试测试",
  "Creator": "李晟迪",
  "AckCount": 0
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## GET 查看组织信息

GET /api/Organization/Info

> Body 请求参数

```yaml
{}
```

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 是   |     | none |
| OrgID | query | string | 是   |     | none |
| body  | body  | object | 否   |     | none |

> 返回示例

> 成功

```json
{
  "Monitor": "xycf",
  "aggregate": 4,
  "OrgName": "计科1902",
  "OrgID": 1,
  "Description": "移动软件开发介绍"
}
```

```json
{
  "result": "empty"
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## POST 创建组织

POST /api/Organization/Action/

> Body 请求参数

```yaml
MonitorID: string
OrgName: string
Description: string
```

### 请求参数

| 名称          | 位置    | 类型     | 必选  | 中文名 | 说明      |
| ----------- | ----- | ------ | --- | --- | ------- |
| token       | query | string | 是   |     | none    |
| body        | body  | object | 否   |     | none    |
| MonitorID   | body  | string | 否   |     | 班级负责人ID |
| OrgName     | body  | string | 是   |     | 组织名称    |
| Description | body  | string | 否   |     | 描述      |

> 返回示例

> 成功

```json
{
  "OrgID": 2,
  "OrgName": "操作系统2022",
  "MonitorID": 2,
  "Description": "dsafsadakjfa"
}
```

> 请求有误

```json
{
  "OrgName": [
    "组织名已存在"
  ]
}
```

### 返回结果

| 状态码 | 状态码含义                                                            | 说明   | 数据模型   |
| --- | ---------------------------------------------------------------- | ---- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)          | 成功   | Inline |
| 400 | [Bad Request](https://tools.ietf.org/html/rfc7231#section-6.5.1) | 请求有误 | Inline |

### 返回数据结构

## PUT 修改组织信息

PUT /api/Organization/Action/%3COrgID%3E/modify/

> Body 请求参数

```yaml
OrgName: string
MonitorID: string
Description: string
```

### 请求参数

| 名称            | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ------------- | ----- | ------ | --- | --- | ---- |
| token         | query | string | 否   |     | none |
| body          | body  | object | 否   |     | none |
| » OrgName     | body  | string | 否   |     | none |
| » MonitorID   | body  | string | 否   |     | none |
| » Description | body  | string | 否   |     | none |

> 返回示例

> 成功

```json
{
  "OrgID": 2,
  "OrgName": "操作系统2022",
  "MonitorID": 3,
  "Description": "修改描述测试"
}
```

```json
{
  "result": "permission denied"
}
```

### 返回结果

| 状态码 | 状态码含义                                                          | 说明   | 数据模型   |
| --- | -------------------------------------------------------------- | ---- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)        | 成功   | Inline |
| 403 | [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3) | 禁止访问 | Inline |

### 返回数据结构

## PUT 修改组织任务

PUT /api/Organization/Task/Action/%3CTaskID%3E/Modify/

> Body 请求参数

```yaml
OrgID: string
TimeStart: string
TimeDue: string
Description: string
TaskName: string
```

### 请求参数

| 名称          | 位置   | 类型     | 必选  | 中文名 | 说明     |
| ----------- | ---- | ------ | --- | --- | ------ |
| body        | body | object | 否   |     | none   |
| OrgID       | body | string | 是   |     | 组织ID   |
| TimeStart   | body | string | 是   |     | 任务开始时间 |
| TimeDue     | body | string | 是   |     | 任务到期时间 |
| Description | body | string | 是   |     | 任务描述   |
| TaskName    | body | string | 是   |     | 任务标题   |

> 返回示例

> 成功

```json
{
  "TaskID": 4,
  "OrgID": 1,
  "CID": 12,
  "TimeStart": 1652166954,
  "TimeDue": 1652339754,
  "Status": true,
  "Description": "修改测试",
  "TaskName": "测试测试测试",
  "Creator": "李晟迪",
  "AckCount": 0
}
```

> 禁止访问

```json
{
  "result": "permission denied"
}
```

### 返回结果

| 状态码 | 状态码含义                                                          | 说明   | 数据模型   |
| --- | -------------------------------------------------------------- | ---- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)        | 成功   | Inline |
| 403 | [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3) | 禁止访问 | Inline |

### 返回数据结构

## POST 确认收到任务

POST /api/Organization/Task/ACK

> Body 请求参数

```yaml
TaskID: string
```

### 请求参数

| 名称     | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ------ | ----- | ------ | --- | --- | ---- |
| token  | query | string | 是   |     | 组织ID |
| body   | body  | object | 否   |     | none |
| TaskID | body  | string | 是   |     | none |

> 返回示例

> 成功

```json
{
  "TaskID": "1",
  "Status": true
}
```

> 禁止访问

```json
{
  "result": "sanction denied"
}
```

```json
{
  "result": "Task Due"
}
```

### 返回结果

| 状态码 | 状态码含义                                                          | 说明   | 数据模型   |
| --- | -------------------------------------------------------------- | ---- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1)        | 成功   | Inline |
| 403 | [Forbidden](https://tools.ietf.org/html/rfc7231#section-6.5.3) | 禁止访问 | Inline |

### 返回数据结构

状态码 **200**

| 名称     | 类型     | 必选   | 约束   | 中文名 | 说明   |
| ------ | ------ | ---- | ---- | --- | ---- |
| result | string | true | none | 结果  | none |

## GET 查询任务收到状态

GET /api/Organization/Task/ACK

### 请求参数

| 名称     | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ------ | ----- | ------ | --- | --- | ---- |
| token  | query | string | 是   |     | none |
| TaskID | query | string | 是   |     | none |

> 返回示例

> 成功

```json
{
  "TaskID": "1",
  "Status": true
}
```

```json
{
  "TaskID": "2",
  "Status": false
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## DELETE 删除任务

DELETE /api/Organization/Task/%3CTaskID%3E/

> Body 请求参数

```yaml
{}
```

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 是   |     | none |
| body  | body  | object | 否   |     | none |

> 返回示例

### 返回结果

| 状态码 | 状态码含义                                                           | 说明   | 数据模型   |
| --- | --------------------------------------------------------------- | ---- | ------ |
| 204 | [No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5) | 删除成功 | Inline |

### 返回数据结构

## GET 查看任务详情

GET /Organization/Task/Action/%3CTaskID%3E/

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 否   |     | none |

> 返回示例

> 成功

```json
{
  "TaskID": 3,
  "OrgID": 2,
  "CID": -1,
  "TimeStart": 1649386815,
  "TimeDue": 1649473354,
  "Status": true,
  "Description": "师傅啊阿啊",
  "TaskName": "铁怕落炉",
  "Creator": "李晟迪",
  "AckCount": 0
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## GET 获取所属组织所有任务

GET /api/Organization/Task/All

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| page  | query | string | 否   |     | none |
| token | query | string | 是   |     | none |

> 返回示例

> 成功

```json
{
  "next": false,
  "previous": false,
  "count": 3,
  "data": [
    {
      "TaskID": 1,
      "TaskName": "做核算",
      "Status": false,
      "TimeStart": 1649386815,
      "TimeDue": 1649473354,
      "Description": "去二田",
      "Creator": "李晟迪",
      "AckCount": 1,
      "CID": 2
    },
    {
      "TaskID": 2,
      "TaskName": "去衢州菜瓜",
      "Status": false,
      "TimeStart": 1649386815,
      "TimeDue": 1649473354,
      "Description": "晟迪萨阿里",
      "Creator": "李晟迪",
      "AckCount": 0,
      "CID": -1
    },
    {
      "TaskID": 4,
      "TaskName": "测试测试测试",
      "Status": true,
      "TimeStart": 1652166954,
      "TimeDue": 1652339754,
      "Description": "大部分将卡萨顶顶",
      "Creator": "李晟迪",
      "AckCount": 0,
      "CID": 12
    }
  ]
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

# 经验&奖励系统

## GET 获取用户排名基础信息

GET /http:101.37.175.115/api/Reward/Situation/

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 是   |     | none |

> 返回示例

> 成功

```json
{
  "percent": 25,
  "Rank": 1,
  "Accumulation": 11740
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## POST 获取奖励

POST /api/Reward/Add/

> Body 请求参数

```yaml
ItemName: Timer
Durations: string
```

### 请求参数

| 名称        | 位置    | 类型     | 必选  | 中文名 | 说明       |
| --------- | ----- | ------ | --- | --- | -------- |
| token     | query | string | 是   |     | none     |
| body      | body  | object | 否   |     | none     |
| ItemName  | body  | string | 是   |     | Timer    |
| Durations | body  | string | 否   |     | Timer项必填 |

> 返回示例

> 成功

```json
{
  "UID": 1,
  "Uname": "LSD",
  "Rank": 1,
  "EXP": 3035,
  "Accumulation": 12800
}
```

```json
{
  "result": "expect Durations"
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## GET 班级学习排行榜

GET /api/Reward/Rank

### 请求参数

| 名称    | 位置    | 类型     | 必选  | 中文名 | 说明   |
| ----- | ----- | ------ | --- | --- | ---- |
| token | query | string | 否   |     | none |

> 返回示例

> 成功

```json
{
  "result": "ok",
  "data": [
    {
      "Uname": "LSD",
      "header": "http://127.0.0.1:8000/media/userHeader/communitygreen_IR1YtN7.png",
      "Rank": 9,
      "Accumulation": 17400
    },
    {
      "Uname": "xycf",
      "header": "http://127.0.0.1:8000/media/userHeader/communitygreen_QKz6u1n.png",
      "Rank": 99,
      "Accumulation": 0
    }
  ]
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

# 五、数据库设计

  本应用涉及的数据模块多且复杂 按分类，分别有用户个人数据、组织数据、社区数据，数据集间又相互关联。因此宜采用关系型数据库来描述和管理。我们采用MySql数据库， 其优点是稳定成熟支持性好。其中媒体文件中用户、社区头像头图、社区帖子图片等文件与记录型数据一起存放于服务器media路径中，在数据库中存放文件索引，以供高频访问。用户PDF文件则存放于OSS服务器，在数据库中记录用户文件结构，形成索引。对数据库操作采用Django 封装的ORM 方式进行。数据修改迁移通过migrate方法同步至MySQL。

> 表名：Organization    

        描述组织相关属性，记录创建者ID,用于权限控制

![p9](C:\Users\hp\Desktop\LSD\LSD\p9.png)

> 表名：User

        描述用户相关属性，除用户基本信息外，还包括 用户头像、学习时长、及经验值信息

<img src="C:\Users\hp\Desktop\LSD\LSD\p10.png" alt="p10" style="zoom:80%;" />

> 表名：Schedule

        描述课程表项相关属性，除基本信息外，还包括所属组织ID、该项UUID,用于组织批量

        导入实现。课程开始、及结束时间是以相对当天0点以秒为单位的时间戳整型值，方便

        计算和排序。Tag标签项用于分类筛选

<img src="C:\Users\hp\Desktop\LSD\LSD\p11.png" alt="p11" style="zoom:80%;" />

> 表名：ToDoList

        描述待办事项相关属性，除基本信息外，还包括所属组织ID、该项UUID,用于组织同步

        导入实现。提醒时间是时间戳整型值，方便判断相对时间和排序。Tag标签项用于分类

        筛选

![p12](C:\Users\hp\Desktop\LSD\LSD\p12.png)

> 表名：OrgTask

        描述组织任务相关属性，除基本信息外，还包括AckCount已知人数统计。任务开始、及

        结束时间是时间戳整型值，方便计算任务状态。

![p13](C:\Users\hp\Desktop\LSD\LSD\p13.png)

> 表名：TaskAck

        记录组织任务收到状况，记录个人提交状态，并避免重复统计任务AckCount值

![p15](C:\Users\hp\Desktop\LSD\LSD\p15.png)

> 表名：Community

       描述课程社区相关属性，除基本信息外，还包括帖子数及最后更新时间，提供社区热度

       计算排序支持。

![p16](C:\Users\hp\Desktop\LSD\LSD\p16.png)

> 表名：CommunityTopic

        描述社区主题相关属性，除基本信息外，还包括点赞数用于主题热度排序

![p17](C:\Users\hp\Desktop\LSD\LSD\p17.png)

> 表名：TopicPost

        描述主题下帖子相关属性

![p18](C:\Users\hp\Desktop\LSD\LSD\p18.png)

> 表名：PostImage

        帖子图片索引表,用于多图地址查询

![p19](C:\Users\hp\Desktop\LSD\LSD\p19.png)

> 表名：FileModel

        用户PDF索引表，用于生成OSS实际地址请求链接

![p21](C:\Users\hp\Desktop\LSD\LSD\p21.png)

> 表名：CommunityStars

        记录社区主题、帖子点赞情况。

![p22](C:\Users\hp\Desktop\LSD\LSD\p22.png)

# 六、前端的实现

这部分分模块来描述前端的具体实现，比如：

## 6.1主页的实现

主页作为用户的入口界面，是用户信息的主要的“聚集地”，所以本页面的主要的实现都围绕在数据的获取和显示，本页面的主要实现方法都集中在接口的调用上。

:warning:本页首次实现了storage数据的获取：

```javascript
getUserMsg() {
    return new Promise((req, rej) = >{
        uni.getStorage({
            key: "userMsg",
            success: (res) = >{
                console.log("success") this.userMsg = res.data req("success")
            },
            fail: (err) = >{
                console.log("err") uni.reLaunch({
                    url: "../Login/Login"  //如果没找到用户的数据，则说明没有登录，返回登录界面
                })
            }
        })
    })
},
```

同时，本页实现了用户的登出操作，在登出的同时删除本地的storage数据

```javascript
logout() {
    uni.removeStorage({
        key: "userMsg",
        success: (res) = >{
            console.log(res) uni.navigateTo({
                url: "../Login/Login"  //登出的同时回到用户界面
            })
        }
    })
},
```

## 6.3 用户管理的实现

登录和注册使用的Uview组建的u-input输入框组件作为输入手段。使用uni.request 向后端请求数据。当获取到后端

```json
{
"result":"check passed",
"code":200,
"token":"eyJ0eXAiOiJqd3QiLCJhbGciOiJIUzI1NiJ9.eyJVSUQiOjEsI***",
"UID":1,
"OrgID":1
}
```

的数据后，获取用户的数据。

注册界面同理，在注册完成后直接请求登录。

由于在程序的运行过程中，用户的token需要不断地被使用，所以必须在缓存中存入一些用户的基本信息，这里使用了uni.setStorage()函数存入数据

```javascript
setStorage(userMsg){
    uni.setStorage({
        key : "userMsg",  //设置key，方便查找
        data: userMsg
    })
}
```

:warning::值得注意的是，为了避免用户需要的频繁的进行登录操作，我设置了判断函数，若检测到在storage中存有用户的相关信息就会直接进行登录操作

```javascript
getStorage(){
    return new Promise((req,rej) =>{
        uni.getStorage({
            key:"userMsg",
            success:(res)=>{
                console.log("success")
                this.userMsg = res.data
                uni.reLaunch({
                    url:"../index/index"
                })
                req("success")
            },
            fail: (err) => {
                req("404")
            }
        })
    })
},
```

## 6.3 TodoList的实现

TodoList的实现主体时uniapp的scrollview实现。当从后端获取到数狙后使用v-if渲染到页面上。

添加TodoList的操作采用了Uview下的popup弹出框组件，和Uviewde的u-datetime-picker组件，通过v-model组件绑定数据后实时获取用户的输入信息。

:warning::本页面的难点在于数据的分类操作，后端的数据并没有进行分类，所以我们在前端进行了分类操作，这里使用了过滤器

```javascript
tagFilter(list) {
    let that = this
    var result = []
    if (that.tag <= 3 && that.tag > 0) {
        result = list.filter(item = >{
            if (that.tag == 3) {  
                return item.Tag >= 3
            } else {
                return item.Tag == that.tag
            }
        })
    } else if (that.tag == 4) {
        result = list.filter(item = >{
            return ! item.Status
        })
    } else if (that.tag == 5) {
        result = list.filter(item = >{
            return item.Status
        })
    } else {
        result = list
    }
    return result;
},
```

通过数组自带的filter()函数对字典中的值进行筛选分类。

:warning:同时时间戳和时间字符串的转换也在本页第一次进行了实现和定义

```javascript
filters: {
    timeStamp: function(value) {
        var date = new Date(value); //时间戳为10位需*1000，时间戳为13位的话不需乘1000
        var year = date.getFullYear();
        var month = ("0" + (date.getMonth() + 1)).slice( - 2);
        var sdate = ("0" + date.getDate()).slice( - 2);
        var hour = ("0" + date.getHours()).slice( - 2);
        var minute = ("0" + date.getMinutes()).slice( - 2);
        // var second = ("0" + date.getSeconds()).slice(-2);
        // 拼接
        var result = year + "-" + month + "-" + sdate + " " + hour + ":" + minute;
        // 返回
        return result;
    },
}
```

在filters:中定义的过滤器,在html中如下使用：

```html
<text v-if="date_flag">{{date_value | timeStamp}}</text>
```

## 6.4计时器的实现

计时器界面是用户自行设置:timer_clock:计时任务并且执行，且在执行完成后向后端发送信息并获取经验值。使用setTimeOut()函数就能在实现简单的计时功能，

```javascript
//倒计时
async counter() {
    this.date = this.poject_now.date / (this.poject_now.percent / 100)
    // console.log(this.date)
    let that = this let per = that.poject_now.percent
    // console.log(per)
    // console.log(this.poject_now.date)
    if (that.poject_now.date == 0 || !that.timer_flag) {
        this.work_flag = false console.log(this.count) await this.sendEXP(this.count) this.count = 0 console.log("end")        clearTimeout(this.timer)
    } else {

        this.poject_now.date = this.poject_now.date - 1 this.poject_now.percent = Math.round((this.poject_now.date / (that.date)) * 100) this.count += 1 this.learning_time += 1 console.log(this.count) setTimeout(that.counter, 1000)
    }
},
```

:warning::在本页面的实现难点在于计时器数据的异步转同步的过程。由于每次在进行setTimeOut()便会创造一个线程，即便页面结束之后也不会结束。这会会导致计时数据的混乱。所以我限制了用户的操作，只有在手动结束上一个线程或者上一个计时结束之后执行clearTimeOut()之后才能再开进程

```javascript
counterEnd() {
    let that = this
    if (this.icon_flag == 0) {
        this.timer_flag = false this.icon_flag = 1 this.starButton = true this.timer = null

    } else {
        this.icon_flag = 0 this.work_flag = false that.poject_now = {
            "name": "当前没有任务",
            "date": 0,
            "percent": 0,
            "color": 0,
        }
    }
},
```

## 6.5文件预览

文件预览界面主要的实现的是从OSS服务器上获取文件数据并在前端展示

本页面在实现的过程中产出诸多的问题，在实现的过程中使用了两种种方法：

- uni.openDocument

- PDF.js
1. uni.openDocument

```javascript
uni.downloadFile({  //先将文件流数据缓存到本地
    url: url,
    success: (res) = >{ 
        console.log(res.tempFilePath) if (res.statusCode === 200) {
            uni.openDocument({   //打开文件预览
                filePath: encodeURI(res.tempFilePath),

                success: function(res) {
                    console.log(res) console.log('打开文档成功');
                },
                fail: (err) = >{
                    console.log(err)
                }
            });
        }
    },
    fail: (err) = >{
        console.log(err)
    }
});
```

​    2.PDF.js

PDF.js的目录结构：![image-20220609230930400](C:\Users\hp\AppData\Roaming\Typora\typora-user-images\image-20220609230930400.png)

```javascript
loadFile(url) {
    console.log(url) uni.downloadFile({
        url: url,
        success: (res) = >{

            if (res.statusCode === 200) {
                // let blob = new BLOB
                let fileUrl = encodeURIComponent(res.tempFilePath) // encodeURIComponent 函数可把字符串作为 URI 组件进行编码。                            
                console.log(fileUrl)
               //将数据流发向PDF.js的组件库，返回数据页面
                this.allUrl = this.viewerUrl + '?file=' + fileUrl console.log(this.allUrl) uni.saveFile({
                    tempFilePath: res.tempFilePath,
                    success: (res) = >{
                        console.log(res.savedFilePath)
                    }
                })

            }
        },
        fail: (err) = >{
            console.log(err)
        }
    });
},
```

:key:：通过PDF.js将喧染好的页面传回本页面，并且使用<web-view></web-view>直接在页面上显示

:warning:：两个手段在H5端并不[支持](https://uniapp.dcloud.io/api/file/file.html#opendocument)

## 6.6组织页面

本页面由于需求的特殊性，所以需要有用户通过二维码跟换组织和通过二维码分享组织的功能，由于uniapp缺少相应的库文件，在这里我们使用了第三方的组件实现二维码的生产和读取功能。

```javascript
var QRCode = require('../../utils/weapp-qrcode.js')
genCode() {
    var that = this
    qr = new QRCode('canvas', {

        text: String(that.$data.newID),
        width: 150,
        height: 150,
        colorDark: this.$data.color,
        colorLight: "white",
        correctLevel: QRCode.CorrectLevel.H,
    })
}
```

:key:在组织任务的界面，我们通过在列表界面和详情界面的两次验证来控制用户的确认状态，防止用户的重复确认导致的问题

## 6.7 课程时间表功能的实现

### 查看本周课程数据功能

主要使用了Tabs标签组件和从后端GET到的数据来实现周一、周二...的显示。同时，根据课程类型的不同，分成了专业课、选修课、通识课、体育课、公共课和其他课，每一门课程的显示颜色都不一样，便于用户区分这些课程。颜色显示技术是根据用户创建课程表时选择的标签不同，向后端传输0-5，5种不同的Tag。前端根据获取到后端传来的Tag的不同，在列表中选择不同的颜色进行显示。

<img src="C:\Users\hp\AppData\Local\Temp\WeChat Files\50fc9d31ac25d88e22f83c2dc6715bf.png" alt="50fc9d31ac25d88e22f83c2dc6715bf" style="zoom:67%;" />

### 添加课程的功能部分

点击右上角的“+”号按钮会跳转到添加课程页面，用户可以完成一个表单，填写课程名称、课程地点、课程日期、课程开始时间、课程结束时间和标签分组。同时，前端自动使用自定义的uuid方法来从‘0123456789abcdef’中随机拿去24个字符，获取全球唯一的uuid。对课程开始和结束时间对hour部分和min部分进行计算，获取秒数。用户点击“创建”按钮，即可POST提交该表单数据，创建新的课程，同步显示在用户的课程表上。

<img src="C:\Users\hp\AppData\Local\Temp\WeChat Files\989e6525fde4e659d6d6b55a859fcba.png" alt="989e6525fde4e659d6d6b55a859fcba" style="zoom:67%;" />

### 组织批量导入课程功能

点击左下角的“+”号悬浮按钮，即可自动获取当前用户所在的组织ID，从组织处批量导入课程数据。

## 6.8 社区、话题和帖子功能的实现

### 社区显示功能

根据用户登录后获取的token，向后端GET请求所有社区的数据。从请求到的社区数据中，提取社区名字、社区头像、帖子数量、最近更新时间和社区描述。将这些数据通过for循环，放入在提前写好的社区组件中，显示所有的社区数据。

<img src="C:\Users\hp\AppData\Local\Temp\WeChat Files\ac604cabccddb24f9d990c59a2989ce.png" alt="ac604cabccddb24f9d990c59a2989ce" style="zoom:67%;" />

### 创建社区功能

点击左下角的“+”号悬浮按钮，进入创建社区页面。在该页面中输入社区名字和社区描述，选择社区头像，点击右上角的“发布”，即可创建社区。此时的POST需要向服务器传输社区名字、用户ID、社区描述和图像等参数。此部分的主要难点在于如何将图片上传至服务器，带有图片的POST方法有一些不同，需要在选择图片时，将图片的本地地址存在一个数组里，在上传时使用uploadFile方法，将图片的本地地址放在filePath参数中，name参数中放数据库中图片的字段名来进行上传。创建成功后，自动返回到社区广场页面。

![f25e7ebf15c3ae639204a77c223af70](C:\Users\hp\AppData\Local\Temp\WeChat Files\f25e7ebf15c3ae639204a77c223af70.png)

### 话题广场显示功能

用户可以从社区广场，点击具体社区跳转到相应的话题广场。跳转时通过setStorage方法来本地存储社区ID、社区名字、社区描述、社区头像和最近更新时间，在话题广场页面通过getStorage来取出存储的数据，并在话题广场上部来显示该话题广场的信息。通过GET方法，向服务器请求话题数据，将这些数据通过for循环，放入在提前写好的话题组件中，显示所有的话题数据。

<img src="C:\Users\hp\AppData\Local\Temp\WeChat Files\97cfb81c71df6e6f9f1a0872dfd9cc4.png" alt="97cfb81c71df6e6f9f1a0872dfd9cc4" style="zoom:67%;" />

### 创建话题功能

点击左下角的“+”号悬浮按钮，进入创建话题页面。在该页面中输入话题名字选择社区头像，点击右上角的“发布”，即可创建话题。此时的POST需要向服务器传输话题名字、所属社区ID、社区描述和图像等参数。此部分的主要难点和之前的创建社区一样，可以沿用。在上传时使用uploadFile方法，向服务器上传相应的数据。创建成功后，自动返回到话题广场页面。

![b256a37e329998840c233bc2b6978a2](C:\Users\hp\AppData\Local\Temp\WeChat Files\b256a37e329998840c233bc2b6978a2.png)

### 话题帖子显示、帖子点赞功能

用户可以从话题广场，点击具体社区跳转到相应的话题帖子广场。跳转时通过setStorage方法来本地存储话题ID、话题标题、话题头像、话题创建者和最近更新时间，在话题帖子页面通过getStorage来取出存储的数据，并在话题帖子广场上部来显示该话题帖子广场的信息。通过GET方法，向服务器请求话题数据，将这些数据通过for循环，放入在提前写好的话题组件中，显示所有的话题数据。

此部分难点在于对话题帖子的点赞功能实现。需要先通过POST方法，向服务器传输当前话题帖子的ID，获取帖子的点赞情况，如果该用户对某特定话题帖子没有点过赞，则可以进行点赞；如果该用户对某特定话题帖子点过赞，则点赞时会提示“已经点过赞了”，并且不会向服务器请求点赞。

![827a453bf241a615074fd59dd42fcf1](C:\Users\hp\AppData\Local\Temp\WeChat Files\827a453bf241a615074fd59dd42fcf1.png)

### 创建话题帖子功能

点击左下角的“+”号悬浮按钮，进入创建话题帖子页面。创建话题帖子和之前的创建社区、创建话题不同，前两个只需要向服务器上传一张图片，而创建话题帖子则最多会上传9张图片。因此在此处使用了robby-image-upload组件，在每次添加一张图片时，会将这张图片的本地地址存储到一个数组中，点击发布按钮会先使用push方法，将这些图片数组再添加到一个数组中，将该数组POST上传到服务器中。

![e4bafe8b27e066083782d0eaa359d47](C:\Users\hp\AppData\Local\Temp\WeChat Files\e4bafe8b27e066083782d0eaa359d47.png)

## 6.9学习排行榜功能的实现

### 学习排行榜显示

根据用户登录时获取的token，向服务器请求学习排行榜数据。对数据进行解析，将前三名的用户单独取出，将其头像放在上方的1、2、3名中。再在组件中遍历数据，通过slice方法截取4-9名用户的用户名、头像和学习时长，放置在下方的列表中。

![b341c3596ebc659be21bdd27163c102](C:\Users\hp\AppData\Local\Temp\WeChat Files\b341c3596ebc659be21bdd27163c102.png)

# 七、后端的实现

后端采用Django+Django restframework+MySQL+Redis.

![截屏2022-06-10 04.27.23](C:\Users\hp\Documents\WeChat Files\wxid_pbtzklatw2zt22\FileStorage\MsgAttach\a11fddc25c8ba25046d9f7f610ed5289\File\2022-06\LSD_new_pic\LSD_new_pic\截屏2022-06-10 04.27.23.png)

利用DRF提供的序列化器、视图集实现序列化、反序列化、数据验证、路由绑定。

![截屏2022-06-10 04.29.03](C:\Users\hp\Documents\WeChat Files\wxid_pbtzklatw2zt22\FileStorage\MsgAttach\a11fddc25c8ba25046d9f7f610ed5289\File\2022-06\LSD_new_pic\LSD_new_pic\截屏2022-06-10 04.29.03.png)

![截屏2022-06-10 04.29.03](C:\Users\hp\Documents\WeChat Files\wxid_pbtzklatw2zt22\FileStorage\MsgAttach\a11fddc25c8ba25046d9f7f610ed5289\File\2022-06\LSD_new_pic\LSD_new_pic\截屏2022-06-10 04.29.03.png)

利用pymysql实现对MySQL的驱动。利用pyjwt实现用户验证。利用django-crontab实现执行每日定时任务。利用oss2 SDK实现对oss服务的操作。利用django-redis实现对redis的驱动。

![截屏2022-06-10 04.31.58](C:\Users\hp\Documents\WeChat Files\wxid_pbtzklatw2zt22\FileStorage\MsgAttach\a11fddc25c8ba25046d9f7f610ed5289\File\2022-06\LSD_new_pic\LSD_new_pic\截屏2022-06-10 04.31.58.png)

![截屏2022-06-10 04.32.33](C:\Users\hp\Documents\WeChat Files\wxid_pbtzklatw2zt22\FileStorage\MsgAttach\a11fddc25c8ba25046d9f7f610ed5289\File\2022-06\LSD_new_pic\LSD_new_pic\截屏2022-06-10 04.32.33.png)

<img src="C:\Users\hp\Documents\WeChat Files\wxid_pbtzklatw2zt22\FileStorage\MsgAttach\a11fddc25c8ba25046d9f7f610ed5289\File\2022-06\LSD_new_pic\LSD_new_pic\截屏2022-06-10 04.33.03.png" alt="截屏2022-06-10 04.33.03" style="zoom: 67%;" />

![截屏2022-06-10 04.33.35](C:\Users\hp\Documents\WeChat Files\wxid_pbtzklatw2zt22\FileStorage\MsgAttach\a11fddc25c8ba25046d9f7f610ed5289\File\2022-06\LSD_new_pic\LSD_new_pic\截屏2022-06-10 04.33.35.png)

# 八、系统测试

## 8.1 单元测试

> 后端

使用Django TestCase包下方法编写各模块test.py，测试各模型创建、各工具函数执行状况，判断是否与给定输出值相等，不等则输出相应信息。系统自动统计测试结果，给出差异值帮助判断。

![p27](C:\Users\hp\Desktop\LSD\LSD\p27.png)

![p25](C:\Users\hp\Desktop\LSD\LSD\p25.png)

例：测试UserProfile模块下User类对象创建是否成功

![p24](C:\Users\hp\Desktop\LSD\LSD\p24.png)

例：测试common.py下经验等级转换函数及timetool.py下各时间计算类函数处理结果。

![p26](C:\Users\hp\Desktop\LSD\LSD\p26.png)

## 8.2 集成测试

> 后端：

        使用Django TestCase包下方法编写各模块test.py。在github action中编写Action workflow。安装相关依赖测试系统在如下环境下的工作状态。（python 3.7~3.9）

![p7](C:\Users\hp\Desktop\LSD\LSD\p7.png)

![p6](C:\Users\hp\Desktop\LSD\LSD\p6.png)

![p28](C:\Users\hp\Desktop\LSD\LSD\p28.png)

## 8.3 测试部署及结果

![p29](C:\Users\hp\Desktop\LSD\LSD\p29.png)

![p5](C:\Users\hp\Desktop\LSD\LSD\p5.png)

# 九、系统部署

项目后端部署于阿里云服务器 IP地址：101.37.175.115，用uwsgi实现多线程并发处理，用nginx实现静态资源分发，利用Pycharm 中差异上传搭配uwsgi python热重载实现热部署和时时同步可维护性。前端ios使用uniapp自带调试基座链接。OSS服务器 bucket名：all-is-ready-file-storage 。

![p3](C:\Users\hp\Desktop\LSD\LSD\p3.png)

![p1](C:\Users\hp\Desktop\LSD\LSD\p1.png)

![p2](C:\Users\hp\Desktop\LSD\LSD\p2.png)

# 十、功能展示

[BILIBILI](https://b23.tv/hmkmVJE)

# 十一、清单

- 前端代码：./front-end 文件项目
- 后端代码:：./back_end项目
- 原型设计文件：./docs/原型设计 目录
- 接口文档：./docs/接口文档
- 实验报告文档：./docs/报告
- ……

# 十二、总结

- ## 叶轶楠

本次的实验我主要负责前端页面的开发工作。这次的开发内容是一个有关于学习工具的集合体，不管是前端还是后端都有不小的难度。在完成本次的作业过程中出现了很多的问题，在团队的合作下得以解决。本次的项目使用的前端框架是uniapp和vue。由于已经有了相应的经验，所以在代码的熟悉度上没有什么问题，所以也在组内负责一部份的debug和代码修改的工作。虽然本次的项目完成了基本功能的开发，但仍有一些功能由于技术上的问题而被删除。UI的设计也存在设计上的缺陷

- ## 黄陈雷

经过一个学期的学习和努力，我们的ALL IS READY最终顺利完工了。这次我主要负责前端部分，而前端使用了uniapp来进行开发。由于从未学习过uniapp，因此先自学了一下uniapp，感觉比较容易上手。在项目开发的过程中，感觉uniapp的开发比Android Studio方便了许多。之前两个学期的两个项目是使用Android Studio进行开发，感觉bug比较多，也比较繁琐，而uniapp相对来说方便容易了许多。由于在做这个项目之前，自己先做了一个项目练手，感觉在这个项目的开发过程中还是比较顺利的，基本没有碰到什么特别大的问题，也让我对uniapp更加的熟悉了。对于这次的项目，我感觉还是比较满意的，因为页面和接口数量比较多，工作量比较大，但还是顺利地完成了项目的开发。如果之后有机会的话，可以把项目完善一些，比如UI美化、功能联结等。

- ## 李晟迪

通过本次课程，使我对移动开发方面的技能得到了更深的锻炼，特别是对后端新框架、新验证机制，新存储实现思路的实践，让我对移动软件领域的各部分的实现和系统整体的设计有了更深入的了解。通过uniapp的实操，也更加强了我在前端主流框架的应用能力。学习例如Github Action Restfull 等也使我的实际工程能力得到提高。

# 十二、参考文献

系统所参考的文献或者代码，比如：

- uni-app: https://uniapp.dcloud.io/ 
- tmui:[https://tmui.design]()
