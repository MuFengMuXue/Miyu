#!/usr/bin/env python3
"""QQ 群里她回得慢、对方连着催：两条说的是一件事就只回一条（用户 09-26）。

沙箱 daemon + 假 NapCat（反向 WS）+ 桩模型（stub.py，兼扮判官）。两段，前一段收完再开后一段：
  A  群友 @ 她问一句（TKQ1），桩慢慢写 20 秒；第 10 秒（已经过了 7 秒的「取代当前生成」窗口）他催「??」。
  B  再问一句（TKQ2），第 10 秒补一个新问题（TKNEW）——补了新东西的照样要回。
（新问题别跟在催促后面 7 秒内发：那会走「取代当前生成」，把正在写的答案整个换掉，测的就不是这件事。）

    BIN=<miyu> python3 testkit/qq-urge/run.py

判定：
  judge_saw_pending_answer  判「??」的那次判官请求里带着 bot_answer_in_progress_for（她正在回答他）
  urge_not_replied          「??」没有单独再回一条
  answer_once               第一条答案只发了一次
  new_info_answered         B 段：原问题答了一次，补的新问题也回了
  decision_log_explains     决策日志里写明了「正在回答」
"""
import importlib.util
import json
import os
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
SANDBOX = sandbox_dir.make("miyu-qq-urge-")
print("沙箱", SANDBOX, flush=True)
HOME = SANDBOX / "home"
RUNTIME = SANDBOX / "runtime"
STUB_LOG = SANDBOX / "stub.jsonl"

spec = importlib.util.spec_from_file_location("fake", REPO / "testkit" / "fake-onebot" / "run.py")
fake = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fake)
ADMIN, MEMBER = 810000001, 810000002


def free_port():
    with socket.socket() as probe:
        probe.bind(("127.0.0.1", 0))
        return probe.getsockname()[1]


PORT, QQ_PORT, STUB_PORT = free_port(), free_port(), free_port()
fake.PORT = QQ_PORT
results = {}
LOCK = threading.Lock()
SENDS = []


def check(name, ok, detail=""):
    results[name] = bool(ok)
    print(f"{'✅' if ok else '❌'} {name}  {str(detail)[:300]}", flush=True)


def write_config():
    (HOME / "config").mkdir(parents=True, exist_ok=True)
    config = {
        "active_provider": "stub",
        "active_provider_models": [{"provider_id": "stub", "model": "stub-model"}],
        "providers": [{
            "id": "stub", "display_name": "Stub", "base_url": f"http://127.0.0.1:{STUB_PORT}/v1",
            "protocol": "openai-chat", "api_key": "stub", "models": ["stub-model"],
        }],
        "memory": {"enabled": False},
        "prompt": {"active_persona": ""},
        "platforms": {"qq": {
            "enabled": True, "reverse_ws_port": QQ_PORT, "access_token": "",
            "admin_users": [ADMIN],
            "max_reply_chars": 0,
            "plugins": {"reply_processor": {"enabled": False}},
        }},
    }
    (HOME / "config" / "config.jsonc").write_text(json.dumps(config, ensure_ascii=False, indent=2), "utf-8")


def wait_for(predicate, timeout, step=0.3):
    deadline = time.time() + timeout
    while time.time() < deadline:
        value = predicate()
        if value:
            return value
        time.sleep(step)
    return None


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


def sends():
    with LOCK:
        return list(SENDS)


def stub_rows():
    if not STUB_LOG.exists():
        return []
    return [json.loads(line) for line in STUB_LOG.read_text(encoding="utf-8").splitlines() if line.strip()]


def main():
    assert BIN.exists(), f"missing binary {BIN}"
    RUNTIME.mkdir(parents=True, exist_ok=True)
    write_config()
    stub = subprocess.Popen([sys.executable, str(Path(__file__).with_name("stub.py"))],
                            env=dict(os.environ, STUB_PORT=str(STUB_PORT), STUB_LOG=str(STUB_LOG)))
    env = dict(os.environ, MIYU_HOME=str(HOME), XDG_RUNTIME_DIR=str(RUNTIME), MIYU_LOG="info")
    log_path = SANDBOX / "daemon.log"
    daemon = subprocess.Popen([str(BIN), "__daemon", "--port", str(PORT)], env=env, cwd=str(HOME),
                              stdin=subprocess.DEVNULL, stdout=log_path.open("w"), stderr=subprocess.STDOUT)
    try:
        assert wait_for(lambda: _http_ok(f"http://127.0.0.1:{PORT}/"), 40), "daemon not up"
        time.sleep(1.5)
        ws = fake.WS.connect("")
        threading.Thread(target=pump, args=(ws,), daemon=True).start()
        time.sleep(1.5)

        # A：只催一下
        start = time.time()
        fake.group_msg(ws, "TKQ1 帮我看看这个怎么装", sender=MEMBER, at_self=True, name="催催")
        wait_for(lambda: any(r["role"] == "main" for r in stub_rows()), 20)
        time.sleep(max(0, start + 10 - time.time()))
        fake.group_msg(ws, "??", sender=MEMBER, at_self=True, name="催催")
        wait_for(lambda: any("A1-DONE" in s for s in sends()), 60)
        time.sleep(10)  # 要是「??」另起了一轮，这时候也该回了
        out = sends()
        rows = stub_rows()
        check("judge_saw_pending_answer", any(r["role"] == "judge" and r["busy"] and r["urge"] for r in rows),
              [r for r in rows if r["role"] == "judge"])
        check("urge_not_replied", not any("URGE-REPLY" in s for s in out), out)
        check("answer_once", sum("A1-DONE" in s for s in out) == 1, out)

        # B：补了新问题
        mark = len(sends())
        start = time.time()
        fake.group_msg(ws, "TKQ2 那这个呢", sender=MEMBER, at_self=True, name="催催")
        time.sleep(max(0, start + 10 - time.time()))
        fake.group_msg(ws, "TKNEW 另外 Windows 上能用吗", sender=MEMBER, at_self=True, name="催催")
        wait_for(lambda: any("NEW-REPLY" in s for s in sends()[mark:]), 90)
        time.sleep(3)
        later = sends()[mark:]
        check("new_info_answered",
              sum("A2-DONE" in s for s in later) == 1 and any("NEW-REPLY" in s for s in later), later)
        logs = log_path.read_text(errors="replace") + "".join(
            p.read_text(errors="replace") for p in (HOME / "cache" / "logs").glob("miyu.*.log"))
        check("decision_log_explains", "正在回答" in logs or "Answer in progress" in logs)
    finally:
        daemon.terminate()
        try:
            daemon.wait(15)
        except subprocess.TimeoutExpired:
            daemon.kill()
        stub.terminate()
    passed = sum(results.values())
    print(f"\n{passed}/{len(results)} passed")
    sys.exit(0 if passed == len(results) else 1)


def _http_ok(url):
    try:
        urllib.request.urlopen(url, timeout=2)
        return True
    except Exception:
        return False


if __name__ == "__main__":
    main()
