# http2websocket proxy

[![Python Version](https://img.shields.io/badge/python-3.9.13-blue)
![License](https://img.shields.io/github/license/AkagiYui/http2websocket)
![GitHub commit activity](https://img.shields.io/github/commit-activity/m/AkagiYui/http2websocket)
![lines](https://img.shields.io/tokei/lines/github/AkagiYui/http2websocket)](https://github.com/AkagiYui/http2websocket)

A proxy sending HTTP requests to WebSocket client.
Make the WebSocket client a Webhook server.

把 http 请求转发到 WebSocket 客户端的代理，为 WebSocket 客户端实现 Webhook server 的功能。

## 快速开始 Quick Start

1. 使用 docker 部署。 Deploy with docker.

```shell
docker run -d -p 80:80 ddio001/http2websocket
```

2. 发起 WebSocket 连接。 Create a WebSocket connection.

3. 发起 http 请求。 Send http requests.

```shell
curl 'http://localhost/haha' -H 'Content-Type: application/json' --data '{"msg":"wow"}'
```

4. 在 WebSocket 客户端查看消息。 View messages in WebSocket client.

```json
{
  "path": "/haha",
  "method": "POST",
  "headers" :{
    "Content-Type": "application/json"
  },
  "content": {
    "msg": "wow"
  }
}
```

## 开发相关 Development

- 操作系统 OS：[Windows 10 19044.1586](https://www.microsoft.com/zh-cn/windows)
- 系统架构 Architecture：amd64

### 使用技术 Technology Stack

- Python: [3.9.13](https://www.python.org/) [下载地址](https://www.python.org/downloads/release/python-3913/)
- ASGI Server: [uvicorn 0.18.2](https://www.uvicorn.org/)

### 运行时Python包  Runtime Python Package

- [uvicorn 0.18.2](https://www.uvicorn.org/) ASGI web 服务器
- [fastapi 0.79.0](https://fastapi.tiangolo.com/zh/) HTTP/Websocket服务器
- [websockets 10.3](https://websockets.readthedocs.io/en/stable/) Websocket 协议框架

## 从代码开始 Start from Code

### 调试 Debugging

1. 安装依赖。 Install requirements.

```shell
pip install fastapi[all]
```

2. 启动服务器。 Start the server.

```shell
cd src
uvicorn main:app --reload
```

### 构建 Docker Image

```shell
docker build -t http2websocket .
```
