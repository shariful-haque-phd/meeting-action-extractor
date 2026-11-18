import argparse, json, re
from pathlib import Path

DATE_PATTERNS=[
    r"\bby\s+(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b",
    r"\bby\s+(\d{1,2}[/-]\d{1,2}(?:[/-]\d{2,4})?)\b",
    r"\bby\s+(tomorrow|next week|end of day|eod|end of month)\b"
]
ACTION_RX=re.compile(r"\b(will|need to|needs to|please|action:|todo:|to do:)\b",re.I)
DECISION_RX=re.compile(r"\b(decided|agreed|approved|decision:|we will proceed|selected)\b",re.I)
OWNER_RX=re.compile(r"^\s*([A-Z][A-Za-z.' -]{1,40})\s*:\s*(.*)$")

def deadline(text):
    for p in DATE_PATTERNS:
        m=re.search(p,text,re.I)
        if m:return m.group(0)
    return None

def extract(lines):
    actions=[]; decisions=[]; current_speaker=None
    for raw in lines:
        line=raw.strip()
        if not line: continue
        m=OWNER_RX.match(line)
        body=line
        if m:
            current_speaker=m.group(1).strip()
            body=m.group(2).strip()
        if DECISION_RX.search(body):
            decisions.append({"text":body,"speaker":current_speaker})
        if ACTION_RX.search(body):
            owner=current_speaker
            mm=re.match(r"([A-Z][A-Za-z.' -]{1,30})\s+(will|needs to|need to)\b",body)
            if mm: owner=mm.group(1).strip()
            actions.append({"text":body,"owner":owner,"deadline":deadline(body)})
    return {"decisions":decisions,"action_items":actions}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("transcript"); ap.add_argument("--output",default="actions.json"); a=ap.parse_args()
    result=extract(Path(a.transcript).read_text(errors="replace").splitlines())
    out=Path(a.output); out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))
if __name__=="__main__":main()
