# Tsinghua-Application-Automation

## 概述

该工具用于提交清华大学进出校审批。

该工具是Selenium的简单应用。请根据真实情况填写表单，该工具仅供测试使用。

## 使用

1. 配置环境：

    - 安装对应于你系统版本和架构的Chrome，自行Google，无GUI也可
    - 下载和上一步整数版本号一致的[ChromeDriver](https://chromedriver.chromium.org/)，并放入`$PATH`
    - 为你的Python安装Selenium模块

2. 克隆[本仓库](https://https://github.com/zhoutq1998/auto_apply)到本地

3. 支持两种运行方式：

    - 运行`python3 auto.py your_username your_password`会申请当天的出校
    - 运行`python3 auto.py your_username your_password n`会申请当天及之后n-1天的出校，共n天