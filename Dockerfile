FROM python:3.9-slim
COPY ./src /app

RUN pip --no-cache-dir install --upgrade pip \
&& pip --no-cache-dir install wheel \
&& pip --no-cache-dir install fastapi[all] \
&& rm -rf ~/.cache/pip

EXPOSE 80

WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
