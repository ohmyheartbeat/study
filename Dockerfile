# 基于的基础镜像

FROM python:2.7.15-alpine

# 维护者信息

MAINTAINER Long  guanglong.sun@hand-china.com

# 代码添加到code文件夹

ADD ./app  /code

# 设置code文件夹是工作目录

WORKDIR /code

# 安装支持

RUN pip install -r requirements.txt

EXPOSE 9098

CMD ["python", "/code/app.py"]


