FROM python:latest
MAINTAINER Eric Hernandez "eric.vim.root@gmail.com"
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]