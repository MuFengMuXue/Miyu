#!/usr/bin/env python3
"""真判官看一眼（09-26）：她回得慢时对方追问，真模型判官会不会只在该回的时候回。

主对话是 stub.py 的慢回答，判官走你配置里的 Lite 档（和线上一样）。每一轮：问一句（LQn），第 10 秒
发一种追问，等答案发出去再等 10 秒，看有没有另起一轮回追问。要真模型、会花一点钱，不进红绿账：

    BIN=<miyu> python3 testkit/qq-urge/live_judge.py [--rounds 3]
"""
import argparse
import importlib.util
import json
import os
import re
import socket
import subprocess
import sys
import threading
import time
import urllib.request
from pathlib import Path

for _herdr_key in [key for key in os.environ if key.startswith("HERDR_")]:
    del os.environ[_herdr_key]

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO / "testkit"))
import sandbox_dir  # noqa: E402

BIN = Path(os.environ.get("BIN") or REPO / "target" / "debug" / "miyu")
SANDBOX = sandbox_dir.make("miyu-qq-urge-live-")
HOME, RUNTIME = SANDBOX / "home", SANDBOX / "runtime"
VARIANT = SANDBOX / "variant.txt"
spec = importlib.util.spec_from_file_location("fake", REPO / "testkit" / "fake-onebot" / "run.py")
fake = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fake)
ADMIN, MEMBER = 810000001, 810000002
# (追问原文, 期望): 只催 / 原样重复 → 不该单独回；补了新问题 → 该回。
VARIANTS = [("??", False), ("人呢", False), ("帮我看看 rime 在 windows 上怎么装啊", False),
            ("另外 macOS 上能用吗", True)]


def free_port():
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return probe.getsockname()[1]


PORT, QQ_PORT, STUB_PORT = free_port(), free_port(), free_port()
fake.PORT = QQ_PORT
LOCK = threading.Lock()
SENDS = []


def pump(ws):
    while True:
        try:
            frame = ws.recv()
        except Exception:
            return
        if not isinstance(frame, dict) or "action" not in frame:
            continue
        action, params = frame["action"], frame.get("params", {})
        if action in ("send_group_msg", "send_msg"):
            with LOCK:
                SENDS.append(fake.render(params.get("message")))
        try:
            ws.send({"status": "ok", "retcode": 0, "data": fake.api_data(action, params), "echo": frame.get("echo")})
        except Exception:
            return


def write_config():
    real = json.loads(re.sub(r"^\s*//.*$", "", (Path.home() / ".miyu/config/config.jsonc").read_text("utf-8"), flags=re.M))
    lite = real.get("model_tiers", {}).get("lite", [])
    judge_ids = {entry["provider_id"] for entry in lite}
    providers = [p for p in real["providers"] if p["id"] in judge_ids]
    providers.append({"id": "stub", "display_name": "Stub", "base_url": f"http://127.0.0.1:{STUB_PORT}/v1",
                      "protocol": "openai-chat", "api_key": "stub", "models": ["stub-model"]})
    config = {
        "active_provider": "stub",
        "active_provider_models": [{"provider_id": "stub", "model": "stub-model"}],
        "providers": providers,
        "model_tiers": {"lite": lite},
        "memory": {"enabled": False},
        # 群聊限流关掉：一个群友短时间连发十几条 @，防刷屏兜底会把后面几轮整个挡掉（09-26 实测），
        # 测的就不是判官了。
        "platforms": {"qq": {"enabled": True, "reverse_ws_port": QQ_PORT, "access_token": "",
                             "admin_users": [ADMIN], "max_reply_chars": 0,
                             "group_chats": {"whitelist_rate_limit": {"max_messages": 0, "window_seconds": 60},
                                             "non_whitelist_rate_limit": {"max_messages": 0, "window_seconds": 60}},
                             "plugins": {"reply_processor": {"enabled": False}}}},
    }
    (HOME / "config").mkdir(parents=True, exist_ok=True)
    (HOME / "config" / "config.jsonc").write_text(json.dumps(config, ensure_ascii=False, indent=2), "utf-8")
    return lite


def wait_for(predicate, timeout, step=0.3):
    deadline = time.time() + timeout
    while time.time() < deadline:
        if predicate():
            return True
        time.sleep(step)
    return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--rounds", type=int, default=3)
    parser.add_argument("--only", help="只跑这一种追问（原文）")
    args = parser.parse_args()
    RUNTIME.mkdir(parents=True, exist_ok=True)
    lite = write_config()
    print("判官模型:", ", ".join(f"{e['provider_id']}/{e['model']}" for e in lite), flush=True)
    VARIANT.write_text("\0", encoding="utf-8")
    stub = subprocess.Popen([sys.executable, str(Path(__file__).with_name("stub.py"))],
                            env=dict(os.environ, STUB_PORT=str(STUB_PORT), STUB_LOG=str(SANDBOX / "stub.jsonl"),
                                     STUB_VARIANT_FILE=str(VARIANT)))
    env = dict(os.environ, MIYU_HOME=str(HOME), XDG_RUNTIME_DIR=str(RUNTIME), MIYU_LOG="info", LANG="zh_CN.UTF-8")
    daemon = subprocess.Popen([str(BIN), "__daemon", "--port", str(PORT)], env=env, cwd=str(HOME),
                              stdin=subprocess.DEVNULL, stdout=(SANDBOX / "daemon.log").open("w"), stderr=subprocess.STDOUT)
    tally = {}
    try:
        wait_for(lambda: _http_ok(f"http://127.0.0.1:{PORT}/"), 40)
        time.sleep(1.5)
        ws = fake.WS.connect("")
        threading.Thread(target=pump, args=(ws,), daemon=True).start()
        time.sleep(1.5)
        n = 0
        for round_index in range(args.rounds):
            for text, expect_reply in VARIANTS:
                if args.only and text != args.only:
                    continue
                n += 1
                VARIANT.write_text(text, encoding="utf-8")
                mark = len(SENDS)
                start = time.time()
                fake.group_msg(ws, f"LQ{n} 帮我看看 rime 在 windows 上怎么装", sender=MEMBER, at_self=True, name="催催")
                time.sleep(max(0, start + 10 - time.time()))
                fake.group_msg(ws, text, sender=MEMBER, at_self=True, name="催催")
                wait_for(lambda: any("A-DONE" in s for s in SENDS[mark:]), 60)
                wait_for(lambda: any("SECOND-REPLY" in s for s in SENDS[mark:]), 12)
                replied = any("SECOND-REPLY" in s for s in SENDS[mark:])
                ok = replied == expect_reply
                tally.setdefault(text, []).append(ok)
                print(f"{'✅' if ok else '❌'} 第{round_index + 1}轮 「{text}」 {'又回了一条' if replied else '没再回'}"
                      f"（期望{'回' if expect_reply else '不回'}）", flush=True)
                time.sleep(3)
    finally:
        daemon.terminate()
        try:
            daemon.wait(15)
        except subprocess.TimeoutExpired:
            daemon.kill()
        stub.terminate()
    # 决策日志写在 daemon 的日志文件里（标准输出只有启动那几行）。
    logs = (SANDBOX / "daemon.log").read_text(errors="replace") + "".join(
        p.read_text(errors="replace") for p in (HOME / "cache" / "logs").glob("miyu.*.log"))
    reasons = re.findall(r"正在回答：([^\n]+)", logs)
    print("\n决策日志里「正在回答」那一行:", len(reasons), "次；其中判成催促不回的", sum("不单独回" in r for r in reasons), "次")
    # 每条追问的判官理由（群聊记录里的原话只截短）。
    for block in re.findall(r"【主动回复判断：[^】]+】(?:\n[^\n【]*){0,20}", logs):
        if "正在回答" in block:
            verdict = re.search(r"【主动回复判断：([^】]+)】", block).group(1)
            message = (re.search(r"消息：([^\n]*)", block) or [None, ""])[1][:30]
            reason = (re.search(r"判断理由：([^\n]*)", block) or [None, ""])[1][:160]
            print(f"  [{verdict}] {message} | {reason}")
    print("汇总:", {text: f"{sum(v)}/{len(v)}" for text, v in tally.items()})


def _http_ok(url):
    try:
        urllib.request.urlopen(url, timeout=2)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    main()
