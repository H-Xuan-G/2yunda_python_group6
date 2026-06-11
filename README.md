# 班级活动报名与统计网页

> 第15周 Flask 动态网页小组协作项目

## 项目简介

这是一个用 Flask 搭建的班级活动报名与统计网页，支持部署到 Vercel。

**网页功能：**
- 首页：填写姓名、小组、活动方向、一句话说明
- 结果页：显示总报名人数、各活动方向统计、最近报名列表

## 文件结构

```
class_event_signup/
├── app.py                # Flask 主程序
├── requirements.txt      # Python 依赖
├── vercel.json           # Vercel 部署配置
├── README.md             # 项目说明
├── data/
│   ├── event_info.py     # 活动名称和说明（组员 A 修改）
│   ├── options.py        # 小组和活动方向选项（组员 B 修改）
│   ├── page_text.py      # 页面文案（组员 C 修改）
│   └── registrations.py  # 默认报名数据（组员 D 修改）
├── templates/
│   ├── index.html        # 首页模板
│   └── result.html       # 结果页模板
└── static/
    └── style.css         # 网页样式
```

## 本地运行

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

打开浏览器访问 http://127.0.0.1:5000

## 协作分工

| 角色 | 负责文件 | 分支名 |
|------|----------|--------|
| 组员 A | data/event_info.py | member-a-event-info |
| 组员 B | data/options.py | member-b-options |
| 组员 C | data/page_text.py | member-c-page-text |
| 组员 D | data/registrations.py | member-d-sample-data |

**重要规则：每个组员只改自己负责的 data 文件，不要改 app.py、templates 或 static。**

## 协作流程

1. 组员 Fork 组长主仓库
2. 组员 Clone 自己的 Fork
3. 组员创建任务分支，只修改负责的文件
4. 组员提交 Pull Request
5. 组长 Review 并 Merge

## Vercel 部署

1. 打开 [Vercel](https://vercel.com) 用 GitHub 登录
2. 选择 Add New → Project
3. 导入 `class_event_signup` 仓库
4. Framework Preset 选 **Other**
5. 点击 Deploy

## 线上访问

> Vercel 部署完成后，在此处填写线上地址：https://your-project.vercel.app
