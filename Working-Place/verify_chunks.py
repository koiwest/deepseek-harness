#!/usr/bin/env python3
# QA: compare speaker headers in output chunks vs original transcript line ranges.
import re, sys, pathlib

SRC = "/Users/apple/Downloads/AI行业创业方向与生态建设讨论_原文.md"
OUT = pathlib.Path("/Users/apple/Documents/deepseek/Working-Place/out")

chunks = [
    ("c01", 3, 302), ("c02", 303, 602), ("c03", 603, 902), ("c04", 903, 1202),
    ("c05", 1203, 1502), ("c06", 1503, 1802), ("c07", 1803, 2102),
    ("c08", 2103, 2402), ("c09", 2403, 2702), ("c10", 2703, 3118),
]

src_lines = SRC and pathlib.Path(SRC).read_text(encoding="utf-8").splitlines() or []
hdr = re.compile(r"^(Ryan|叶奇意|Patrick)\s+(\d{2}:\d{2}(?::\d{2})?)\s*$")

def headers(text_lines):
    out = []
    for ln in text_lines:
        m = hdr.match(ln)
        if m:
            out.append((m.group(1), m.group(2)))
    return out

problems = 0
for cid, start, end in chunks:
    src_seg = headers(src_lines[start-1:end])
    for kind in ("fix", "polish"):
        p = OUT / kind / f"{cid}.md"
        if not p.exists():
            print(f"[MISSING] {kind}/{cid}.md")
            problems += 1
            continue
        got = headers(p.read_text(encoding="utf-8").splitlines())
        n = len(got)
        # report header mismatches vs source
        mism = []
        for (g_spk, g_t), (s_spk, s_t) in zip(got, src_seg):
            if g_spk != s_spk or g_t != s_t:
                mism.append((s_spk, s_t, g_spk, g_t))
        print(f"{kind}/{cid}.md: {n} headers (src {len(src_seg)}) "
              + ("OK" if len(got) == len(src_seg) and not mism else
                 f"MISMATCH {len(mism)}" + (f" e.g. {mism[0]}" if mism else "")))
        if mism:
            problems += 1
        # quick sanity: no obvious leftover garble keywords
        text = p.read_text(encoding="utf-8")
        for bad in ("honeys", "honest", "difficult", "SOPIC", "dick sick", "deep sick",
                    "纹身图", "interfusion", "chinese BT", "拆GPP", "eight twenty four",
                    "托尔", "写教", "early doctor", "remote model", "pretty model",
                    "AS小龙", "旷世", "意图", "壹图", "商涛", "拉马", "pipeline",
                    "新事项", "张明王鑫", "人心里", "USK", "MT ", "accessory",
                    "word model", "38页", "龙珠", "创新旗帜", "兰州科技"):
            if bad in text:
                print(f"  [GARBLE] '{bad}' still present in {kind}/{cid}.md")
                problems += 1
print(f"\nTotal problems: {problems}")
sys.exit(1 if problems else 0)
