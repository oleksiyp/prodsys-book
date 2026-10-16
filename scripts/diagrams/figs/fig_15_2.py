"""Figure 15.2 — SRE team models on the context–reach trade-off."""
from html import escape

from dg import Diagram, label_width
from chartkit import Plot
from registry import figure

MODELS = [  # name, reach, context, label side
    ("EMBEDDED", 0.14, 0.86, "right"),
    ("CENTRAL", 0.52, 0.42, "right"),
    ("PLATFORM-ALIGNED", 0.72, 0.30, "right"),
    ("CONSULTING", 0.88, 0.14, "left"),
]


@figure
def fig_15_2():
    d = Diagram("fig-15-2", 864, 400, "SRE team models: context against reach",
                "A chart with reach, the number of teams a reliability engineer touches, across, and context, "
                "depth of knowledge of one system, up. Embedded sits high on context and low on reach; central "
                "and platform-aligned sit in the middle; consulting reaches far with little context. The four lie "
                "near a trade-off line; a hybrid with champions in every team aims above it, where Encore's "
                "arrangement now sits.")
    p = Plot(d, x=72, y=48, w=720, h=256, xr=(0, 1), yr=(0, 1))
    p.axes(xlabel="REACH: TEAMS A RELIABILITY ENGINEER TOUCHES →",
           ylabel="CONTEXT: DEPTH IN ONE SYSTEM ↑", grid=False)
    p.line([(0.04, 0.96), (0.98, 0.04)], kind="soft", dashed=True)
    p.annotate(0.30, 0.66, "THE TRADE-OFF LINE", dx=4, dy=0)
    # hybrid target region
    cx, cy = p.pt(0.70, 0.72)
    d.zones.append(f'<ellipse class="dg-ill-fill-accent" cx="{cx:.1f}" cy="{cy:.1f}" rx="128" ry="52"/>')
    p.annotate(0.70, 0.72, "HYBRID WITH CHAMPIONS", dx=-64, dy=-28)
    for name, x, y, side in MODELS:
        p.dot(x, y, kind="ink", r=5)
        if side == "right":
            p.annotate(x, y, name, dx=10, dy=3)
        else:
            p.annotate(x, y, name, dx=-10, dy=3, anchor="end")
    p.dot(0.66, 0.70, kind="accent", r=5)
    p.annotate(0.66, 0.70, "ENCORE: PLATFORM PAGER + CONSULT + CHAMPIONS", dx=-125, dy=-62)
    d.legend([("start", "A team model"), ("focal", "Where a hybrid aims; the red dot is Encore now")])
    return d
