"""Figure 5.4: the Vesper Hale on-sale as a chart: admission rate, the degraded window and the canonical events."""
from dg import Diagram, label_width
from chartkit import Plot
from html import escape
from registry import figure

EVENTS = [(-8, "09:52 CATALOG DEPLOY"), (0, "10:00 GATE OPENS"), (2, "10:02 DRAIN · SHARD 3 FAILOVER"),
          (4, "10:04 PAGE"), (7, "10:07 SEV1 · MARTA IS IC"), (11, "10:11 CUE CORRELATES"),
          (14, "10:14 STATUS PAGE"), (16, "10:16 WHAT IS BROKEN NOW?"), (19, "10:19 ADMISSION 900/S"),
          (24, "10:24 SUPPORT: FANS TOLD THEY ARE BOTS"), (31, "10:31 BOT RULE OFF"),
          (47, "10:47 RECOVERED"), (70, "11:10 1,200/S")]


@figure
def fig_5_4():
    # x in minutes after 10:00
    p_x, p_w, xr = 72, 744, (-10, 80)
    px = lambda m: p_x + (m - xr[0]) / (xr[1] - xr[0]) * p_w
    # lay out event labels: a descending staircase, so no leader line crosses a label
    rows, gap = {}, 8
    for i in range(len(EVENTS) - 1, -1, -1):
        m, text = EVENTS[i]
        right = px(m) + label_width(text) + gap
        later = [rows[j] for j in range(i + 1, len(EVENTS)) if px(EVENTS[j][0]) <= right]
        rows[i] = max(later) + 1 if later else 0
    nrows = max(rows.values()) + 1
    lane = 292
    height = lane + nrows * 18 + 16
    d = Diagram("fig-5-4", 864, height, "The Vesper Hale on-sale, 09:50 to 11:20",
                "The Sale Gate's admission rate per event: 1,500 fans per second from 10:00, lowered to 900 at "
                "10:19 and returned to 1,200 at 11:10. Checkout was degraded from 10:00 to 10:47. Below the "
                "chart, the events of the response at their logged times; the incident was resolved at 12:00.")
    p = Plot(d, x=p_x, y=40, w=p_w, h=200, xr=xr, yr=(0, 1600))
    hh = lambda m: f"{10 + (m // 60):02d}:{m % 60:02d}" if m >= 0 else f"09:{60 + m:02d}"
    p.axes(xticks=[-10, 0, 10, 20, 30, 40, 50, 60, 70, 80], yticks=[0, 500, 1000, 1500], xfmt=hh,
           yfmt=lambda v: f"{v:,}", ylabel="ADMISSION RATE · FANS/S PER EVENT")
    p.band(0, 47, kind="accent")
    d.label_at("47 MIN OF DEGRADED CHECKOUT", px(33), p.py(1250), horizontal=True, side="below", kind="accent")
    p.band(2, 3, kind="soft")
    p.line([(-10, 0), (0, 0), (0, 1500), (19, 1500), (19, 900), (70, 900), (70, 1200), (80, 1200)], kind="ink")
    p.annotate(56, 900, "900/S", dx=0, dy=-8)
    p.annotate(72, 1200, "1,200/S", dx=0, dy=-8)
    p.annotate(1, 1500, "1,500/S", dx=4, dy=-6)
    d.note(816, 278, "12:00 RESOLVED →", anchor="end")
    for i, (m, text) in enumerate(EVENTS):
        x = px(m)
        y = lane + rows[i] * 18
        d.zones.append(f'<line class="dg-grid" x1="{x:.1f}" y1="240" x2="{x:.1f}" y2="{y + 6}"/>')
        d.nodes.append(f'<circle class="dg-dot dg-dot-ink" cx="{x:.1f}" cy="240" r="3"/>')
        w = label_width(text)
        d.labels.append(f'<rect class="dg-mask" x="{x - 2:.1f}" y="{y}" width="{w}" height="12" rx="2"/>'
                        f'<text class="dg-label" x="{x - 2 + w / 2:.1f}" y="{y + 9}">{escape(text)}</text>')
    return d
