"""Figure 6.3 — freeze exceptions per quarter, and the running total nobody kept."""
from dg import Diagram
from chartkit import Plot
from registry import figure

Q = [3, 11, 13, 14]


@figure
def fig_6_3():
    d = Diagram("fig-6-3", 864, 352, "Freeze exceptions in the year before Vesper Hale",
                "Bar chart of change-freeze exceptions granted in chat per quarter over the year before the "
                "Vesper Hale on-sale: 3, 11, 13 and 14, with a running total that reaches 41. None was followed "
                "by an incident, and no one was counting.")
    p = Plot(d, x=72, y=48, w=744, h=208, xr=(0, 4.6), yr=(0, 45))
    names = {0.5: "Q1", 1.5: "Q2", 2.5: "Q3", 3.5: "Q4", 4.3: "ON-SALE"}
    p.axes(xticks=list(names), yticks=[0, 10, 20, 30, 40], xfmt=lambda t: names[t],
           ylabel="EXCEPTIONS GRANTED IN CHAT", xlabel="THE TWELVE MONTHS BEFORE VESPER HALE")
    for i, v in enumerate(Q):
        x0, x1 = p.px(i + 0.5) - 40, p.px(i + 0.5) + 40
        y = p.py(v)
        d.zones.append(f'<rect class="dg-ill-fill" x="{x0:.1f}" y="{y:.1f}" width="80" '
                       f'height="{p.py(0) - y:.1f}" rx="2"/>')
        d.note(round(p.px(i + 0.5)), round(y - 6), str(v), anchor="middle")
    total, pts = 0, [(0, 0)]
    for i, v in enumerate(Q):
        total += v
        pts.append((i + 1, total))
    p.line(pts, kind="accent")
    for x, y in pts[1:]:
        p.dot(x, y, kind="ink", r=3)
    p.annotate(4, 41, "RUNNING TOTAL 41 · NONE FOLLOWED BY AN INCIDENT", dx=-8, dy=-4, anchor="end",
               kind="accent")
    p.annotate(2, 14, "14", dx=-6, dy=-6, anchor="end")
    p.annotate(3, 27, "27", dx=-6, dy=-6, anchor="end")
    p.vline(4.3, kind="soft")
    p.annotate(4.3, 30, "THE 42ND?", dx=6, dy=0)
    d.legend([("backend", "Exceptions that quarter"), ("arrow:accent", "Running total, kept by nobody")])
    return d
