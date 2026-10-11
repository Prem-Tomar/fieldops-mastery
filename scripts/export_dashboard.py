"""Generate a portable read-only HTML dashboard from repository records."""
import json
from pathlib import Path

from dashboard_server import ROOT, Store


def export_dashboard(root=ROOT, destination=None):
    root = Path(root)
    destination = Path(destination) if destination else root / "output/dashboard/index.html"
    state = Store(root).state()
    # The snapshot never carries session credentials or owner write controls.
    state["session"] = {"login": None, "canReview": False, "token": None,
                        "authError": "Read-only snapshot. Open the local reviewer dashboard to save evidence or accept gates. Regenerate this snapshot after accepted progress."}
    state["catalog"] = {"tasks": [{"id": task["id"], "concepts": task["concepts"]} for task in state["catalog"]["tasks"]]}
    serialized = json.dumps(state, ensure_ascii=True).replace("<", "\\u003c").replace(">", "\\u003e").replace("&", "\\u0026")
    template = (ROOT / "dashboard/index.html").read_text(encoding="utf-8")
    css = (ROOT / "dashboard/style.css").read_text(encoding="utf-8")
    js = (ROOT / "dashboard/app.js").read_text(encoding="utf-8")
    template = template.replace('<link rel="stylesheet" href="/style.css">', f"<style>{css}</style>")
    template = template.replace('<script src="/app.js" defer></script>', "")
    template = template.replace("</body>", f"<script>window.FIELDOPS_SNAPSHOT={serialized};</script><script>{js}</script></body>")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(template, encoding="utf-8")
    return destination


if __name__ == "__main__":
    print(export_dashboard())
