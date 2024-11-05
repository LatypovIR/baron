FROM python:3.9-alpine
WORKDIR /baron
COPY ./ /baron
RUN apk update && pip install -r /baron/requirements.txt --no-cache-dir
CMD ["python", "main.py"]
