FROM python:latest
MAINTAINER Eric Hernandez "eric.vim.root@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
