#!/usr/bin/env python3
"""qq-urge 的桩模型：一个端口同时扮判官和主对话。

- 判官请求（系统提示以 "You are a proactive-reply judge" 开头）：一律判回，每次判断记一行日志。
- 主对话（请求里带 tools）：看所有用户消息里**最靠后**的记号（当前消息后面还跟着回合尾巴）：TKNEW → NEW-REPLY，
  「??」→ URGE-REPLY，TKB → B-REPLY，TKQn → An-DONE；An-DONE 要慢慢流 20 秒（模拟第一条回得慢）。
  回复里不带任何记号，免得进了群聊记录又被当成记号。
- 其余旁路（好感度之类）回 `{}`。
"""
import json
import os
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

PORT = int(os.environ["STUB_PORT"])
LOG = os.environ["STUB_LOG"]
SLOW_SECONDS = float(os.environ.get("STUB_SLOW_SECONDS", "20"))


def text_of(message):
    content = message.get("content")
    if isinstance(content, list):
        return "".join(part.get("text", "") for part in content if isinstance(part, dict))
    return content or ""


def log(row):
    with open(LOG, "a", encoding="utf-8") as out:
        out.write(json.dumps(row, ensure_ascii=False) + "\n")


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        self.reply_json({"data": [{"id": "stub-model", "object": "model"}]})

    def reply_json(self, obj):
        body = json.dumps(obj).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def answer(self, text, stream, pace=0.0):
        try:
            self._answer(text, stream, pace)
        except (BrokenPipeError, ConnectionResetError):
            pass  # 取代当前生成时引擎会掐断这条流，正常。

    def _answer(self, text, stream, pace):
        usage = {"prompt_tokens": 100, "completion_tokens": 10, "total_tokens": 110}
        if not stream:
            self.reply_json({"id": "x", "object": "chat.completion", "model": "stub-model",
                             "choices": [{"index": 0, "message": {"role": "assistant", "content": text},
                                          "finish_reason": "stop"}], "usage": usage})
            return
        self.send_response(200)
        self.send_header("Content-Type", "text/event-stream")
        self.end_headers()
        pieces = [text[i:i + 3] for i in range(0, len(text), 3)] or [""]
        for piece in pieces:
            chunk = {"id": "x", "object": "chat.completion.chunk", "model": "stub-model",
                     "choices": [{"index": 0, "delta": {"content": piece}, "finish_reason": None}]}
            self.wfile.write(f"data: {json.dumps(chunk)}\n\n".encode())
            self.wfile.flush()
            if pace:
                time.sleep(pace)
        done = {"id": "x", "object": "chat.completion.chunk", "model": "stub-model",
                "choices": [{"index": 0, "delta": {}, "finish_reason": "stop"}], "usage": usage}
        self.wfile.write(f"data: {json.dumps(done)}\n\ndata: [DONE]\n\n".encode())
        self.wfile.flush()

    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))))
        messages = body.get("messages", [])
        stream = bool(body.get("stream"))
        system = text_of(messages[0]) if messages else ""
        last_user = next((text_of(m) for m in reversed(messages) if m.get("role") == "user"), "")
        if system.startswith("You are a proactive-reply judge"):
            log({"role": "judge", "current": last_user.split("Current message content", 1)[-1][:200]})
            verdict = {"should_reply": True, "to_bot": True, "relevance": 9, "willingness": 9,
                       "social": 9, "timing": 9, "continuity": 9, "reasoning": "stub"}
            self.answer(json.dumps(verdict), stream)
            return
        if not body.get("tools"):
            self.answer("{}", stream)
            return
        # 当前消息后面还跟着回合尾巴（几条运行时块），不是最后一条用户消息：在所有用户消息里找。
        users = "\n".join(text_of(m) for m in messages if m.get("role") == "user")
        marks = {"TKNEW": "NEW-REPLY", "??": "URGE-REPLY", "TKB": "B-REPLY",
                 "TKQ1": "A1-DONE", "TKQ2": "A2-DONE", "TKQ3": "A3-DONE"}
        latest = max(marks, key=lambda mark: users.rfind(mark))
        reply = marks[latest]
        log({"role": "main", "reply": reply})
        slow = reply.endswith("-DONE")
        if slow:
            reply += " " + "·" * 30
        pace = SLOW_SECONDS / 14 if slow else 0.0
        self.answer(reply, stream, pace)


ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
