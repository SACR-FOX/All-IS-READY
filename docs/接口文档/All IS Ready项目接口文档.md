---
title: All IS Ready v1.0.0
language_tabs:
  - shell: Shell
  - http: HTTP
  - javascript: JavaScript
  - ruby: Ruby
  - python: Python
  - php: PHP
  - java: Java
  - go: Go
toc_footers: []
includes: []
search: true
highlight_theme: darkula
headingLevel: 2

---

# All IS Ready

> v1.0.0

# UserProfile

## POST 用户注册

POST /api/Register

> Body 请求参数

```yaml
type: object
properties:
  username:
    type: string
    description: 用户名
  password:
    type: string
    description: 密码
  stuID:
    type: string
    description: 学号（可不填）
  Header:
    type: string
    description: 头像
    format: binary
required:
  - username
  - password
```

### 请求参数

| 名称         | 位置   | 类型             | 必选    | 说明      |
| ---------- | ---- | -------------- | ----- | ------- |
| body       | body | object         | false | none    |
| » username | body | string         | true  | 用户名     |
| » password | body | string         | true  | 密码      |
| » stuID    | body | string         | false | 学号（可不填） |
| » Header   | body | string(binary) | false | 头像      |

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

## PUT 修改用户信息&加入组织

PUT /api/User/Detail/InfoModify/

> Body 请求参数

```yaml
type: object
properties:
  Passwd:
    type: string
  Uname:
    type: string
  OrgID:
    type: string
    description: 班级ID
  STUID:
    type: string
    description: 学号
  Header:
    type: string
    description: 头像
    format: binary
```

### 请求参数

| 名称       | 位置    | 类型             | 必选    | 说明   |
| -------- | ----- | -------------- | ----- | ---- |
| token    | query | string         | true  | none |
| body     | body  | object         | false | none |
| » Passwd | body  | string         | false | none |
| » Uname  | body  | string         | false | none |
| » OrgID  | body  | string         | false | 班级ID |
| » STUID  | body  | string         | false | 学号   |
| » Header | body  | string(binary) | false | 头像   |

> 返回示例

> 成功

```json
{
  "UID": 1,
  "Uname": "LSD",
  "OrgID": 1,
  "STUID": 1,
  "Rank": 1,
  "Header": "/media/userHeader/communitygreen_IR1YtN7.png",
  "EXP": 3055,
  "Accumulation": 12800
}
```

```json
{
  "Uname": [
    "用户名已存在"
  ]
}
```

```json
{
  "Passwd": [
    "请确保这个字段至少包含 6 个字符。"
  ]
}
```

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

状态码 **200**

| 名称       | 类型     | 必选   | 约束   | 说明   |
| -------- | ------ | ---- | ---- | ---- |
| » result | string | true | none | none |

## GET 查看用户信息

GET /api/User/Detail/%3CUID%3E/

### 请求参数

| 名称    | 位置    | 类型     | 必选   | 说明   |
| ----- | ----- | ------ | ---- | ---- |
| token | query | string | true | none |

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

| 名称       | 类型     | 必选   | 约束   | 说明   |
| -------- | ------ | ---- | ---- | ---- |
| » UID    | string | true | none | none |
| » Uname  | string | true | none | none |
| » OrgID  | string | true | none | none |
| » STUID  | string | true | none | 暂时不用 |
| » Rank   | string | true | none | none |
| » Header | string | true | none | none |
| » EXP    | string | true | none | none |

## POST 用户登录

POST /api/User/Login

> Body 请求参数

```yaml
type: object
properties:
  username:
    type: string
  password:
    type: string
required:
  - username
  - password
```

### 请求参数

| 名称         | 位置   | 类型     | 必选    | 说明   |
| ---------- | ---- | ------ | ----- | ---- |
| body       | body | object | false | none |
| » username | body | string | true  | none |
| » password | body | string | true  | none |

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

| 名称       | 类型      | 必选   | 约束   | 说明   |
| -------- | ------- | ---- | ---- | ---- |
| » result | string  | true | none | none |
| » code   | integer | true | none | none |
| » token  | string  | true | none | none |

状态码 **401**

| 名称       | 类型      | 必选   | 约束   | 说明   |
| -------- | ------- | ---- | ---- | ---- |
| » result | string  | true | none | none |
| » code   | integer | true | none | none |

# ToDoList

## PUT 修改完成状况

PUT /api/ToDoList/Action/%3CID%3E/Done/

### 请求参数

| 名称    | 位置    | 类型     | 必选   | 说明   |
| ----- | ----- | ------ | ---- | ---- |
| token | query | string | true | 事项ID |

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

| 名称       | 类型     | 必选   | 约束   | 说明   |
| -------- | ------ | ---- | ---- | ---- |
| » result | string | true | none | none |

## DELETE 删除事项

DELETE /api/ToDoList/Action/%3CID%3E/

### 请求参数

| 名称    | 位置    | 类型     | 必选   | 说明   |
| ----- | ----- | ------ | ---- | ---- |
| token | query | string | true | none |

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
  "type": "object",
  "properties": {
    "OrgID": {
      "type": "integer",
      "title": "组织ID",
      "description": "个人创建 -1 ，为组织创建填组织ID"
    },
    "UID": {
      "type": "string",
      "title": "所属用户ID"
    },
    "Time": {
      "type": "string",
      "title": "提醒时间"
    },
    "ItemName": {
      "type": "string",
      "title": "计划名称"
    },
    "UUID": {
      "type": "string"
    },
    "Tag": {
      "type": "string"
    }
  },
  "required": [
    "OrgID",
    "UID",
    "ItemName",
    "UUID",
    "Tag"
  ]
}
```

### 请求参数

| 名称         | 位置    | 类型      | 必选    | 说明                  |
| ---------- | ----- | ------- | ----- | ------------------- |
| token      | query | string  | true  | none                |
| body       | body  | object  | false | none                |
| » OrgID    | body  | integer | true  | 个人创建 -1 ，为组织创建填组织ID |
| » UID      | body  | string  | true  | none                |
| » Time     | body  | string  | false | none                |
| » ItemName | body  | string  | true  | none                |
| » UUID     | body  | string  | true  | none                |
| » Tag      | body  | string  | true  | none                |

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

| 名称       | 类型     | 必选   | 约束   | 说明   |
| -------- | ------ | ---- | ---- | ---- |
| » result | string | true | none | none |

## GET 列出该用户所有事项

GET /api/ToDoList/All

### 请求参数

| 名称    | 位置    | 类型     | 必选   | 说明   |
| ----- | ----- | ------ | ---- | ---- |
| token | query | string | true | none |

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

## GET 情况统计

GET /api/ToDoList/Statistics

### 请求参数

| 名称    | 位置    | 类型     | 必选    | 说明   |
| ----- | ----- | ------ | ----- | ---- |
| token | query | string | false | none |

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

## GET 列出该用户今日所有事项

GET /api/ToDoList/Today

### 请求参数

| 名称    | 位置    | 类型     | 必选   | 说明   |
| ----- | ----- | ------ | ---- | ---- |
| token | query | string | true | none |

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

## POST 按组织号批量导入

POST /api/ToDoList/GroupImport

> Body 请求参数

```yaml
type: object
properties:
  OrgID:
    type: string
```

### 请求参数

| 名称      | 位置    | 类型     | 必选    | 说明   |
| ------- | ----- | ------ | ----- | ---- |
| token   | query | string | false | none |
| body    | body  | object | false | none |
| » OrgID | body  | string | false | none |

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

## PUT 修改ToDoList项

PUT /http:101.37.175.115/api/ToDoList/Action/%3CID%3E/Modify/

> Body 请求参数

```yaml
type: object
properties:
  Tag:
    type: string
  ItemName:
    type: string
  Time:
    type: string
```

### 请求参数

| 名称         | 位置    | 类型     | 必选    | 说明   |
| ---------- | ----- | ------ | ----- | ---- |
| token      | query | string | true  | 事项ID |
| body       | body  | object | false | none |
| » Tag      | body  | string | false | none |
| » ItemName | body  | string | false | none |
| » Time     | body  | string | false | none |

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

| 名称       | 类型     | 必选   | 约束   | 说明   |
| -------- | ------ | ---- | ---- | ---- |
| » result | string | true | none | none |

# File

## GET 文件在线预览连接

GET /api/Files/Detail/OnlinePreview/

> Body 请求参数

```yaml
type: object
properties:
  OrgID:
    type: string
    description: 查询组织则带上
  FileID:
    type: string
    description: 文件ID
required:
  - FileID
```

### 请求参数

| 名称       | 位置    | 类型     | 必选    | 说明      |
| -------- | ----- | ------ | ----- | ------- |
| token    | query | string | true  | none    |
| body     | body  | object | false | none    |
| » OrgID  | body  | string | false | 查询组织则带上 |
| » FileID | body  | string | true  | 文件ID    |

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

| 名称       | 类型     | 必选   | 约束   | 说明   |
| -------- | ------ | ---- | ---- | ---- |
| » Uri    | string | true | none | none |
| » result | string | true | none | none |

## GET 显示指定文件夹下文件列表

GET /api/Files/Detail/FileList/

> Body 请求参数

```yaml
type: object
properties:
  Folder:
    type: string
  OrgID:
    type: string
    description: 若是组织文件，则加上
required:
  - Folder
```

### 请求参数

| 名称       | 位置    | 类型     | 必选    | 说明         |
| -------- | ----- | ------ | ----- | ---------- |
| token    | query | string | true  | none       |
| body     | body  | object | false | none       |
| » Folder | body  | string | true  | none       |
| » OrgID  | body  | string | false | 若是组织文件，则加上 |

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

| 名称       | 类型     | 必选   | 约束   | 说明   |
| -------- | ------ | ---- | ---- | ---- |
| » result | string | true | none | none |

## GET 显示文件夹列表

GET /api/Files/Detail/FolderList/

> Body 请求参数

```yaml
type: object
properties:
  OrgID:
    type: string
    description: 若是组织文件则带上
```

### 请求参数

| 名称      | 位置    | 类型     | 必选    | 说明        |
| ------- | ----- | ------ | ----- | --------- |
| token   | query | string | true  | none      |
| body    | body  | object | false | none      |
| » OrgID | body  | string | false | 若是组织文件则带上 |

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

| 名称         | 类型       | 必选   | 约束   | 说明   |
| ---------- | -------- | ---- | ---- | ---- |
| » data     | [object] | true | none | none |
| »» FID     | string   | true | none | none |
| »» Fname   | string   | true | none | none |
| »» Uri     | string   | true | none | none |
| »» Theme   | string   | true | none | none |
| »» Renewal | string   | true | none | none |
| » result   | string   | true | none | none |

## POST 上传云端

POST /api/Files/upload

> Body 请求参数

```yaml
type: object
properties:
  "OrgID ":
    type: string
    description: 个人上传 填-1
  FolderName:
    type: string
  FileName:
    type: string
    description: 重命名就加上
  book:
    type: string
    format: binary
required:
  - "OrgID "
  - FolderName
  - book
```

### 请求参数

| 名称           | 位置    | 类型             | 必选    | 说明       |
| ------------ | ----- | -------------- | ----- | -------- |
| token        | query | string         | true  | none     |
| body         | body  | object         | false | none     |
| » OrgID      | body  | string         | true  | 个人上传 填-1 |
| » FolderName | body  | string         | true  | none     |
| » FileName   | body  | string         | false | 重命名就加上   |
| » book       | body  | string(binary) | true  | none     |

> 返回示例

> 成功

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

| 名称       | 类型     | 必选   | 约束   | 说明   |
| -------- | ------ | ---- | ---- | ---- |
| » result | string | true | none | none |

# ClassSchedule

## POST 组织批量导入课程

POST /api/Schedule/GroupImport/

> Body 请求参数

```yaml
type: object
properties:
  OrgID:
    type: string
    description: 组织ID
required:
  - OrgID
```

### 请求参数

| 名称      | 位置    | 类型     | 必选    | 说明   |
| ------- | ----- | ------ | ----- | ---- |
| token   | query | string | true  | none |
| body    | body  | object | false | none |
| » OrgID | body  | string | true  | 组织ID |

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

| 名称       | 类型     | 必选   | 约束   | 说明  |
| -------- | ------ | ---- | ---- | --- |
| » result | string | true | none | 结果  |

## DELETE 删除课程

DELETE /api/Schedule/Action/%3CScheduleID%3E/

### 请求参数

| 名称    | 位置    | 类型     | 必选   | 说明   |
| ----- | ----- | ------ | ---- | ---- |
| token | query | string | true | none |

> 返回示例

### 返回结果

| 状态码 | 状态码含义                                                           | 说明   | 数据模型   |
| --- | --------------------------------------------------------------- | ---- | ------ |
| 204 | [No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5) | 删除成功 | Inline |

### 返回数据结构

## PUT 修改课程信息

PUT /api/Schedule/Action/%3CScheduleID%3E/Modify/

> Body 请求参数

```yaml
type: object
properties:
  DurationStart:
    type: string
    description: 课程开始相对时间
  DurationEnd:
    type: string
    description: 课程结束相对时间
  Location:
    type: string
    description: 课程位置
  CurName:
    type: string
    description: 课程名称
  Tag:
    type: string
    description: 标签颜色
```

### 请求参数

| 名称              | 位置    | 类型     | 必选    | 说明       |
| --------------- | ----- | ------ | ----- | -------- |
| \token          | query | string | false | none     |
| body            | body  | object | false | none     |
| » DurationStart | body  | string | false | 课程开始相对时间 |
| » DurationEnd   | body  | string | false | 课程结束相对时间 |
| » Location      | body  | string | false | 课程位置     |
| » CurName       | body  | string | false | 课程名称     |
| » Tag           | body  | string | false | 标签颜色     |

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

## GET 查看当天课程表

GET /api/Schedule/Today/

> Body 请求参数

```yaml
type: object
properties: {}
```

### 请求参数

| 名称    | 位置    | 类型     | 必选    | 说明   |
| ----- | ----- | ------ | ----- | ---- |
| token | query | string | false | none |
| body  | body  | object | false | none |

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

## GET 查看下一节课程

GET /api/Schedule/Next/

### 请求参数

| 名称    | 位置    | 类型     | 必选   | 说明   |
| ----- | ----- | ------ | ---- | ---- |
| token | query | string | true | none |

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

## POST 添加课程

POST /175.115/api/Schedule/Action/

> Body 请求参数

```yaml
type: object
properties:
  Day:
    type: string
    description: 课程所在星期
    example: 3 （礼拜三）
  OrgID:
    type: string
    description: 组织ID
  DurationStart:
    type: string
    description: 课程开始相对时间戳
  DurationEnd:
    type: string
    description: 课程结束相对时间戳
  Loaction:
    type: string
    description: 上课地点
  CurName:
    type: string
    description: 课程名称
  Tag:
    type: string
    description: 标签颜色
  UUID:
    type: string
    description: 课程唯一标识
required:
  - Day
  - DurationStart
  - DurationEnd
  - CurName
  - UUID
```

### 请求参数

| 名称              | 位置    | 类型     | 必选    | 说明        |
| --------------- | ----- | ------ | ----- | --------- |
| token           | query | string | true  | none      |
| body            | body  | object | false | none      |
| » Day           | body  | string | true  | 课程所在星期    |
| » OrgID         | body  | string | false | 组织ID      |
| » DurationStart | body  | string | true  | 课程开始相对时间戳 |
| » DurationEnd   | body  | string | true  | 课程结束相对时间戳 |
| » Loaction      | body  | string | false | 上课地点      |
| » CurName       | body  | string | true  | 课程名称      |
| » Tag           | body  | string | false | 标签颜色      |
| » UUID          | body  | string | true  | 课程唯一标识    |

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

## PUT 修改帖子

PUT /api/Community/Post/%3CPostID%3E/Modify/

> Body 请求参数

```yaml
type: object
properties:
  HasImage:
    type: string
    description: True 修改图片 False 仅修改内容
    example: True False
  Content:
    type: string
  PostPic:
    type: string
    description: HasImage 为True时修改图片，带上
    format: binary
required:
  - HasImage
```

### 请求参数

| 名称         | 位置    | 类型             | 必选    | 说明                     |
| ---------- | ----- | -------------- | ----- | ---------------------- |
| token      | query | string         | true  | none                   |
| body       | body  | object         | false | none                   |
| » HasImage | body  | string         | true  | True 修改图片 False 仅修改内容  |
| » Content  | body  | string         | false | none                   |
| » PostPic  | body  | string(binary) | false | HasImage 为True时修改图片，带上 |

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

## PUT 修改话题

PUT /api/Community/Topic/%3CTopicID%3E/Modify/

> Body 请求参数

```yaml
type: object
properties:
  Title:
    type: string
  HasImage:
    type: string
    description: 是否修改头图
    example: True False
  TopicPic:
    type: string
    description: "HasImage=True 带上  "
    format: binary
required:
  - HasImage
```

### 请求参数

| 名称         | 位置    | 类型             | 必选    | 说明               |
| ---------- | ----- | -------------- | ----- | ---------------- |
| token      | query | string         | true  | none             |
| body       | body  | object         | false | none             |
| » Title    | body  | string         | false | none             |
| » HasImage | body  | string         | true  | 是否修改头图           |
| » TopicPic | body  | string(binary) | false | HasImage=True 带上 |

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

## GET 显示话题下所有帖子

GET /api/Community/Post_All

> Body 请求参数

```yaml
type: object
properties: {}
```

### 请求参数

| 名称      | 位置    | 类型     | 必选    | 说明   |
| ------- | ----- | ------ | ----- | ---- |
| token   | query | string | true  | none |
| page    | query | string | true  | none |
| TopicID | query | string | true  | none |
| body    | body  | object | false | none |

> 返回示例

> 成功

```json
{
  "next": false,
  "previous": false,
  "count": 2,
  "result": [
    {
      "PostID": 1,
      "TopicID": 10,
      "UID": 1,
      "Time": 1649816781,
      "HasImage": false,
      "Content": "支持一下",
      "Stars": 0
    },
    {
      "PostID": 2,
      "TopicID": 10,
      "UID": 1,
      "Time": 1649817052,
      "HasImage": true,
      "Content": "支持一下",
      "pics": [
        "http://127.0.0.1:8000/media/PostImage/home2.png",
        "http://127.0.0.1:8000/media/PostImage/jiahao.png"
      ],
      "Stars": 0
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

## GET 显示话题信息

GET /api/Community/Topic/%3CTopicID%3E/

> Body 请求参数

```yaml
type: object
properties:
  PostID:
    type: string
```

### 请求参数

| 名称       | 位置    | 类型     | 必选    | 说明   |
| -------- | ----- | ------ | ----- | ---- |
| token    | query | string | false | none |
| body     | body  | object | false | none |
| » PostID | body  | string | false | none |

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

## GET 显示所有社区

GET /api/Community/Action

### 请求参数

| 名称    | 位置    | 类型     | 必选   | 说明   |
| ----- | ----- | ------ | ---- | ---- |
| token | query | string | true | none |
| page  | query | string | true | 默认1  |

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

## POST 查询点赞情况

POST /api/Community/checkStar/

> Body 请求参数

```yaml
type: object
properties:
  ID:
    type: string
  type:
    type: string
    description: 点赞类型 主题:0  帖子:1
required:
  - ID
  - type
```

### 请求参数

| 名称     | 位置    | 类型     | 必选    | 说明              |
| ------ | ----- | ------ | ----- | --------------- |
| token  | query | string | true  | none            |
| body   | body  | object | false | none            |
| » ID   | body  | string | true  | none            |
| » type | body  | string | true  | 点赞类型 主题:0  帖子:1 |

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

## GET 点赞话题

GET /api/Community/Topic/Star/

> Body 请求参数

```yaml
type: object
properties: {}
```

### 请求参数

| 名称    | 位置    | 类型     | 必选    | 说明   |
| ----- | ----- | ------ | ----- | ---- |
| token | query | string | true  | none |
| body  | body  | object | false | none |

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

## POST 点赞帖子

POST /api/Community/Post/

> Body 请求参数

```yaml
type: object
properties: {}
```

### 请求参数

| 名称    | 位置    | 类型     | 必选    | 说明   |
| ----- | ----- | ------ | ----- | ---- |
| token | query | string | true  | none |
| body  | body  | object | false | none |

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

## PUT 修改社区资料

PUT /api/Community/Action/%3CCommunityID%3E/Modify/

> Body 请求参数

```yaml
type: object
properties:
  PostID:
    type: string
```

### 请求参数

| 名称       | 位置    | 类型     | 必选    | 说明   |
| -------- | ----- | ------ | ----- | ---- |
| token    | query | string | true  | none |
| body     | body  | object | false | none |
| » PostID | body  | string | false | none |

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

## POST 创建话题

POST /api/Community/Topic/Create/

> Body 请求参数

```yaml
type: object
properties:
  CommunityID:
    type: string
  HasImage:
    type: string
    example: True False
  Title:
    type: string
  TopicPic:
    type: string
    description: HasImage为True时填
    format: binary
required:
  - HasImage
```

### 请求参数

| 名称            | 位置    | 类型             | 必选    | 说明              |
| ------------- | ----- | -------------- | ----- | --------------- |
| token         | query | string         | true  | none            |
| body          | body  | object         | false | none            |
| » CommunityID | body  | string         | false | none            |
| » HasImage    | body  | string         | true  | none            |
| » Title       | body  | string         | false | none            |
| » TopicPic    | body  | string(binary) | false | HasImage为True时填 |

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

| 名称       | 类型     | 必选   | 约束   | 说明   |
| -------- | ------ | ---- | ---- | ---- |
| » result | string | true | none | none |

## GET 显示所有话题

GET /api/Community/Topic_All

> Body 请求参数

```yaml
type: object
properties:
  CommunityID:
    type: string
required:
  - CommunityID
```

### 请求参数

| 名称            | 位置    | 类型     | 必选    | 说明    |
| ------------- | ----- | ------ | ----- | ----- |
| token         | query | string | true  | none  |
| CommunityID   | query | string | true  | none  |
| page          | query | string | true  | 默认第1页 |
| body          | body  | object | false | none  |
| » CommunityID | body  | string | true  | none  |

> 返回示例

> 成功

```json
{
  "count": 2,
  "next": null,
  "previous": null,
  "results": [
    {
      "TopicID": 10,
      "CommunityID": 1,
      "UID": 1,
      "Time": 1649809036,
      "HasImage": true,
      "Title": "话题二",
      "ImageUri": "http://localhost:8000/media/TopicHeader/task-filling_uYaH7RK.png",
      "Stars": 1
    },
    {
      "TopicID": 12,
      "CommunityID": 1,
      "UID": 1,
      "Time": 1652770187,
      "HasImage": true,
      "Title": "社区-主题创建测试",
      "ImageUri": "http://localhost:8000/media/TopicHeader/qingdan.png",
      "Stars": 0
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
type: object
properties:
  CommunityName:
    type: string
  AdministratorID:
    type: string
    description: 创建者/管理者ID
  Poster:
    type: string
    description: 社区头像
    format: binary
  Description:
    type: string
required:
  - CommunityName
```

### 请求参数

| 名称                | 位置   | 类型             | 必选    | 说明        |
| ----------------- | ---- | -------------- | ----- | --------- |
| body              | body | object         | false | none      |
| » CommunityName   | body | string         | true  | none      |
| » AdministratorID | body | string         | false | 创建者/管理者ID |
| » Poster          | body | string(binary) | false | 社区头像      |
| » Description     | body | string         | false | none      |

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

| 名称       | 类型     | 必选   | 约束   | 说明   |
| -------- | ------ | ---- | ---- | ---- |
| » result | string | true | none | none |

## POST 发帖

POST /api/Community/Post/Create/

> Body 请求参数

```yaml
type: object
properties:
  TopicID:
    type: string
  HasImage:
    type: string
    example: True False
  Content:
    type: string
    description: 文字内容
  PostPic:
    type: string
    description: HasImage 为True 时 带上
    format: binary
required:
  - TopicID
  - HasImage
  - Content
```

### 请求参数

| 名称         | 位置    | 类型             | 必选    | 说明                  |
| ---------- | ----- | -------------- | ----- | ------------------- |
| token      | query | string         | true  | none                |
| body       | body  | object         | false | none                |
| » TopicID  | body  | string         | true  | none                |
| » HasImage | body  | string         | true  | none                |
| » Content  | body  | string         | true  | 文字内容                |
| » PostPic  | body  | string(binary) | false | HasImage 为True 时 带上 |

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

| 名称       | 类型     | 必选   | 约束   | 说明   |
| -------- | ------ | ---- | ---- | ---- |
| » result | string | true | none | none |

# Organization

## PUT 修改组织任务

PUT /api/Organization/Task/Action/%3CTaskID%3E/Modify/

> Body 请求参数

```yaml
type: object
properties:
  OrgID:
    type: string
    description: 组织ID
  TimeStart:
    type: string
    description: 任务开始时间
  TimeDue:
    type: string
    description: 任务到期时间
  Description:
    type: string
    description: 任务描述
  TaskName:
    type: string
    description: 任务标题
required:
  - OrgID
  - TimeStart
  - TimeDue
  - Description
  - TaskName
```

### 请求参数

| 名称            | 位置    | 类型     | 必选    | 说明     |
| ------------- | ----- | ------ | ----- | ------ |
| TimeStart     | query | string | false | none   |
| TimeDue       | query | string | false | none   |
| CID           | query | string | false | none   |
| Description   | query | string | false | none   |
| TaskName      | query | string | false | none   |
| Creator       | query | string | false | none   |
| body          | body  | object | false | none   |
| » OrgID       | body  | string | true  | 组织ID   |
| » TimeStart   | body  | string | true  | 任务开始时间 |
| » TimeDue     | body  | string | true  | 任务到期时间 |
| » Description | body  | string | true  | 任务描述   |
| » TaskName    | body  | string | true  | 任务标题   |

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

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

## GET 创建组织任务

GET /api/Organization/Task/Action/

> Body 请求参数

```yaml
type: object
properties:
  OrgID:
    type: string
    description: 组织ID
  TimeStart:
    type: string
    description: 任务开始时间
  TimeDue:
    type: string
    description: 任务到期时间
  Description:
    type: string
    description: 描述
  TaskName:
    type: string
    description: 任务标题
  Creator:
    type: string
    description: 创建者姓名
  CID:
    type: string
    description: 绑定课程ID
required:
  - OrgID
  - TimeStart
  - TimeDue
  - TaskName
```

### 请求参数

| 名称            | 位置   | 类型     | 必选    | 说明     |
| ------------- | ---- | ------ | ----- | ------ |
| body          | body | object | false | none   |
| » OrgID       | body | string | true  | 组织ID   |
| » TimeStart   | body | string | true  | 任务开始时间 |
| » TimeDue     | body | string | true  | 任务到期时间 |
| » Description | body | string | false | 描述     |
| » TaskName    | body | string | true  | 任务标题   |
| » Creator     | body | string | false | 创建者姓名  |
| » CID         | body | string | false | 绑定课程ID |

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

## POST 确认收到任务

POST /api/Organization/Task/ACK

> Body 请求参数

```yaml
type: object
properties:
  TaskID:
    type: string
required:
  - TaskID
```

### 请求参数

| 名称       | 位置    | 类型     | 必选    | 说明   |
| -------- | ----- | ------ | ----- | ---- |
| token    | query | string | true  | 组织ID |
| body     | body  | object | false | none |
| » TaskID | body  | string | true  | none |

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

| 名称       | 类型     | 必选   | 约束   | 说明   |
| -------- | ------ | ---- | ---- | ---- |
| » result | string | true | none | none |

## GET 查看任务详情

GET /Organization/Task/Action/%3CTaskID%3E/

### 请求参数

| 名称    | 位置    | 类型     | 必选    | 说明   |
| ----- | ----- | ------ | ----- | ---- |
| token | query | string | false | none |

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

| 名称    | 位置    | 类型     | 必选    | 说明   |
| ----- | ----- | ------ | ----- | ---- |
| page  | query | string | false | none |
| token | query | string | true  | none |

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

## POST 创建组织

POST /api/Organization/Action/

> Body 请求参数

```yaml
type: object
properties:
  MonitorID:
    type: string
    description: 班级负责人ID
  OrgName:
    type: string
    description: 组织名称
  Description:
    type: string
    description: 描述
required:
  - OrgName
```

### 请求参数

| 名称            | 位置    | 类型     | 必选    | 说明      |
| ------------- | ----- | ------ | ----- | ------- |
| token         | query | string | true  | none    |
| body          | body  | object | false | none    |
| » MonitorID   | body  | string | false | 班级负责人ID |
| » OrgName     | body  | string | true  | 组织名称    |
| » Description | body  | string | false | 描述      |

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

## DELETE 删除任务

DELETE /api/Organization/Task/%3CTaskID%3E/

### 请求参数

| 名称    | 位置    | 类型     | 必选   | 说明   |
| ----- | ----- | ------ | ---- | ---- |
| token | query | string | true | none |

> 返回示例

### 返回结果

| 状态码 | 状态码含义                                                           | 说明   | 数据模型   |
| --- | --------------------------------------------------------------- | ---- | ------ |
| 204 | [No Content](https://tools.ietf.org/html/rfc7231#section-6.3.5) | 删除成功 | Inline |

### 返回数据结构

## PUT 修改组织信息

PUT /api/Organization/Action/%3COrgID%3E/modify/

> Body 请求参数

```yaml
type: object
properties:
  OrgName:
    type: string
  MonitorID:
    type: string
  Description:
    type: string
```

### 请求参数

| 名称            | 位置    | 类型     | 必选    | 说明   |
| ------------- | ----- | ------ | ----- | ---- |
| token         | query | string | false | none |
| body          | body  | object | false | none |
| » OrgName     | body  | string | false | none |
| » MonitorID   | body  | string | false | none |
| » Description | body  | string | false | none |

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

### 返回结果

| 状态码 | 状态码含义                                                   | 说明  | 数据模型   |
| --- | ------------------------------------------------------- | --- | ------ |
| 200 | [OK](https://tools.ietf.org/html/rfc7231#section-6.3.1) | 成功  | Inline |

### 返回数据结构

# 经验&奖励系统

## GET 获取用户排名基础信息

GET /http:101.37.175.115/api/Reward/Situation/

### 请求参数

| 名称    | 位置    | 类型     | 必选   | 说明   |
| ----- | ----- | ------ | ---- | ---- |
| token | query | string | true | none |

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

POST /101.37.175.115:8000/api/Reward/Add/

> Body 请求参数

```yaml
type: object
properties:
  ItemName:
    type: string
    description: Timer
    example: Timer
  Durations:
    type: string
    description: Timer项必填
required:
  - ItemName
```

### 请求参数

| 名称          | 位置    | 类型     | 必选    | 说明       |
| ----------- | ----- | ------ | ----- | -------- |
| token       | query | string | true  | none     |
| body        | body  | object | false | none     |
| » ItemName  | body  | string | true  | Timer    |
| » Durations | body  | string | false | Timer项必填 |

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

| 名称    | 位置    | 类型     | 必选    | 说明   |
| ----- | ----- | ------ | ----- | ---- |
| token | query | string | false | none |

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

### 返回数据结构

# 数据模型
