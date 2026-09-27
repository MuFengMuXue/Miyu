#!/usr/bin/env python3
"""qq-bg-image 的桩模型：主对话从后往前找最近的一条要紧消息来回。

- 最近是 send_message_to_user 的工具结果 → 回正文 TEXT-AFTER（记下工具结果原文）；
- 最近是带 `<upload-failed>` 的用户消息 → 回 NOTICE-REPLY（她收到了「没发出去」的回报）；
- 最近是带 TKIMG 的用户消息 → 调 send_message_to_user 发 STUB_IMAGE 那张图。
回合尾巴那几条运行时块不带记号，跳过。其余旁路（判官、好感度之类）回 `{}`。
"""
import json
import os
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ["STUB_PORT"])
LOG = os.environ["STUB_LOG"]
IMAGE = os.environ["STUB_IMAGE"]


def text_of(message):
    content = message.get("content")
    if isinstance(content, list):
        return "".join(part.get("text", "") for part in content if isinstance(part, dict))
    return content or ""


def log(row):
    with open(LOG, "a", encoding="utf-8") as out:
        out.write(json.dumps(row, ensure_ascii=False) + "\n")


def decide(messages):
    for message in reversed(messages):
        role, text = message.get("role"), text_of(message)
        if role == "tool":
            log({"role": "main", "saw": "tool_result", "output": text[:400]})
            return {"content": "TEXT-AFTER"}
        if role == "user" and "<upload-failed>" in text:
            log({"role": "main", "saw": "notice", "text": text[:400]})
            return {"content": "NOTICE-REPLY"}
        if role == "user" and "TKIMG" in text:
            log({"role": "main", "saw": "ask"})
            return {"tool_calls": [{
                "index": 0, "id": f"call_{int(time.time() * 1000) % 10_000_000}", "type": "function",
                "function": {"name": "send_message_to_user",
                             "arguments": json.dumps({"images": [{"path": IMAGE}]})},
            }]}
    return {"content": "OTHER"}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        body = json.dumps({"data": [{"id": "stub-model", "object": "model"}]}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
        messages = body.get("messages", [])
        reply = decide(messages) if body.get("tools") else {"content": "{}"}
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.send_header("Connection", "close")
        self.end_headers()
        chunk = {"id": "stub", "object": "chat.completion.chunk", "model": "stub-model",
                 "choices": [{"index": 0, "delta": {"role": "assistant", **reply}, "finish_reason": None}]}
        done = {"id": "stub", "object": "chat.completion.chunk", "model": "stub-model",
                "choices": [{"index": 0, "delta": {}, "finish_reason": "tool_calls" if "tool_calls" in reply else "stop"}],
                "usage": {"prompt_tokens": 100, "completion_tokens": 10, "total_tokens": 110}}
        try:
            for event in (chunk, done):
                self.wfile.write(f"data: {json.dumps(event, ensure_ascii=False)}\n\n".encode())
            self.wfile.write(b"data: [DONE]\n\n")
            self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            pass
        self.close_connection = True


ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
