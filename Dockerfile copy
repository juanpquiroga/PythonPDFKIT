FROM python:3.7.4-slim-buster
ENV PYTHONUNBUFFERED 1
LABEL Name=pythonwkhtml

RUN apt-get update

RUN apt-get install -y wget fontconfig libfreetype6 libjpeg62-turbo libpng16-16 libx11-6 libxcb1 libxext6 libxrender1 xfonts-75dpi xfonts-base
RUN wget https://downloads.wkhtmltopdf.org/0.12/0.12.5/wkhtmltox_0.12.5-1.buster_amd64.deb
RUN dpkg -i wkhtmltox_0.12.5-1.buster_amd64.deb
RUN apt-get install -f
RUN rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . $APP_HOME
RUN chown -R "$USER:$USER" .
RUN pip install -r requirements.txt
