#!/usr/bin/env python3
"""Ctrl+S 暂存输入框（用户 09-26，照 Claude Code 的 stash）。

输入框里写了一半，想先跑一条命令：Ctrl+S 存起来、清空，顶行右边挂一个暗色的「> 暂存」（英文界面
`> stashed`）；
干完别的再按一次，草稿原样回来，标记消失。

    cargo build
    python3 testkit/tui/input_stash.py

判定：
  stash_clears_the_box     按下去草稿从输入框里消失
  stash_mark_shown         顶行右边出现「> 暂存」（中文界面）
  mark_survives_a_turn     中间发一句话、这一轮跑完，标记还在
  second_press_restores    再按一次，草稿回到输入框
  mark_gone_after_restore  取回之后标记没了

复用 round26 的沙箱与 PTY 辅助。**TUI 走查一次只跑一个**。
"""
import os
import sys
from pathlib import Path

for _herdr_key in [key for key in os.environ if key.startswith("HERDR_")]:
    del os.environ[_herdr_key]

sys.path.insert(0, str(Path(__file__).resolve().parent))
import run as h  # noqa: E402
import round26 as r  # noqa: E402

DRAFT = "写了一半的草稿 TKDRAFT"
# 走查钉中文界面（LANG=zh_CN），标记跟界面语言走。
MARK = "> 暂存"
CTRL_S = b"\x13"


def shows(screen, needle):
    return any(needle in line for line in screen)


def main():
    report = {}
    stub, daemon, tui, master, sink = r.start({"STUB_REPLY": "收到 TKREPLY", "STUB_CHUNK_SLEEP": "0.01"})
    try:
        os.write(master, DRAFT.encode())
        screen = r.wait_screen(master, sink, lambda s: shows(s, "TKDRAFT"), 10.0)
        if screen is None:
            r.save("stash-typed", r.LAST["screen"] or [])
            report["draft_typed"] = False
            return report

        os.write(master, CTRL_S)
        screen = r.wait_screen(master, sink, lambda s: not shows(s, "TKDRAFT") and shows(s, MARK), 6.0)
        after = screen or r.LAST["screen"] or []
        r.save("stash-pressed", after)
        report["stash_clears_the_box"] = not shows(after, "TKDRAFT")
        report["stash_mark_shown"] = shows(after, MARK)

        os.write(master, "TKSEND 你好".encode())
        h.drain_until(master, sink, "TKSEND", 5.0)
        os.write(master, b"\r")
        screen = r.wait_screen(master, sink, lambda s: shows(s, "TKREPLY") and shows(s, MARK), 30.0)
        mid = screen or r.LAST["screen"] or []
        r.save("stash-after-turn", mid)
        report["mark_survives_a_turn"] = shows(mid, "TKREPLY") and shows(mid, MARK)

        os.write(master, CTRL_S)
        screen = r.wait_screen(master, sink, lambda s: shows(s, "TKDRAFT") and not shows(s, MARK), 6.0)
        back = screen or r.LAST["screen"] or []
        r.save("stash-restored", back)
        report["second_press_restores"] = shows(back, "TKDRAFT")
        report["mark_gone_after_restore"] = not shows(back, MARK)
        return report
    finally:
        r.stop(tui, daemon, stub)


if __name__ == "__main__":
    result = main()
    for name, ok in result.items():
        print(f"{'✅' if ok else '❌'} {name}")
    passed = sum(1 for ok in result.values() if ok)
    print(f"\n{passed}/{len(result)} passed")
    sys.exit(0 if result and passed == len(result) else 1)
