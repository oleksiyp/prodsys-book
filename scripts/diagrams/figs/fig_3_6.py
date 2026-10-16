"""Figure 3.6 — calibrated trust (after Lee and See, 2004)."""
from chartkit import Plot
from dg import Diagram
from registry import figure


@figure
def fig_3_6():
    d = Diagram("fig-3-6", 864, 412, "Calibrated trust",
                "After Lee and See (2004). Trust in automation plotted against its actual capability. On the "
                "diagonal, trust matches capability. Above it lies overtrust, which leads to misuse, such as "
                "approving curtain-up's plan unread; below it lies distrust, which leads to disuse, such as "
                "muting an alert channel that cried wolf.")
    p = Plot(d, x=96, y=48, w=432, h=288, xr=(0, 1), yr=(0, 1))
    lab = {0: "LOW", 1: "HIGH"}
    p.axes(xticks=[0, 1], yticks=[0, 1], xlabel="WHAT THE AUTOMATION CAN ACTUALLY DO",
           ylabel="HOW MUCH PEOPLE TRUST IT", grid=False, xfmt=lambda v: lab[v], yfmt=lambda v: lab[v])
    d.zones.append('<polygon class="dg-area dg-ar-accent" points="'
                   + " ".join(f"{p.px(a):.1f},{p.py(b):.1f}" for a, b in [(0, 0), (0, 1), (1, 1)]) + '"/>')
    d.zones.append('<polygon class="dg-area dg-ar-soft" points="'
                   + " ".join(f"{p.px(a):.1f},{p.py(b):.1f}" for a, b in [(0, 0), (1, 0), (1, 1)]) + '"/>')
    p.line([(0, 0), (1, 1)], kind="ink")
    p.annotate(0.12, 0.9, "OVERTRUST: MISUSE", dx=0, dy=0, kind="accent")
    p.annotate(0.97, 0.1, "DISTRUST: DISUSE", dx=0, dy=0, anchor="end")
    p.annotate(0.3, 0.3, "CALIBRATED", dx=10, dy=14)
    pts = [(0.45, 0.85, "approving the plan unread"), (0.7, 0.22, "muting the alert channel"),
           (0.62, 0.62, "running curtain-up, reading its report")]
    for x, y, _ in pts:
        p.dot(x, y, kind="ink")
    for (x, y, text), side in zip(pts, ("right", "right", "right")):
        px, py = p.pt(x, y)
        d.extra.append(f'<line class="dg-ill-soft" x1="{px + 6:.1f}" y1="{py:.1f}" x2="544" y2="{py:.1f}"/>')
        d.extra.append(f'<text class="dg-note" x="552" y="{py + 3:.1f}">{text}</text>')
    return d
