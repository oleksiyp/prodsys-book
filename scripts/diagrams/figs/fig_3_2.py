"""Figure 3.2 — the pre-warm's yearly cost in human hours, for each generation."""
from chartkit import Plot
from dg import Diagram
from registry import figure


@figure
def fig_3_2():
    d = Diagram("fig-3-2", 864, 384, "What the pre-warm costs a year",
                "Engineer-hours per year spent on the on-sale pre-warm against the number of on-sales a year. The "
                "wiki page took 70 to 120 minutes each time, so at 160 on-sales it cost roughly 190 to 320 hours. "
                "The script cut that to about 12 minutes, 32 hours; curtain-up needs about 5 minutes of review, "
                "some 13 hours. Every generation still grows with the number of on-sales.")
    p = Plot(d, x=72, y=40, w=720, h=264, xr=(0, 200), yr=(0, 400))
    p.axes(xticks=[0, 40, 80, 120, 160, 200], yticks=[0, 100, 200, 300, 400],
           xlabel="ON-SALES A YEAR", ylabel="ENGINEER-HOURS A YEAR")
    lo, hi = 70 / 60, 120 / 60
    d.zones.append('<polygon class="dg-area dg-ar-soft" points="'
                   + " ".join(f"{p.px(a):.1f},{p.py(b):.1f}" for a, b in [(0, 0), (200, 200 * hi), (200, 200 * lo)])
                   + '"/>')
    p.line([(0, 0), (200, 200 * lo)], kind="ink")
    p.line([(0, 0), (200, 200 * hi)], kind="ink", dashed=True)
    p.line([(0, 0), (200, 200 * 12 / 60)], kind="ink")
    p.line([(0, 0), (200, 200 * 5 / 60)], kind="accent")
    p.vline(160, label="ENCORE: ABOUT 160", at=0.8)
    for h in (160 * lo, 160 * hi, 160 * 12 / 60):
        p.dot(160, h, kind="ink")
    p.dot(160, 160 * 5 / 60, kind="ink")
    p.annotate(160, 160 * hi, "WIKI, SLOW DAY: 320 H", dx=-8, dy=-6, anchor="end")
    p.annotate(160, 160 * lo, "WIKI, 70 MIN: 187 H", dx=-8, dy=-6, anchor="end")
    p.annotate(160, 160 * 12 / 60, "PREWARM.PY: 32 H", dx=-8, dy=-6, anchor="end")
    p.annotate(160, 160 * 5 / 60, "CURTAIN-UP REVIEW: 13 H", dx=8, dy=14, kind="accent")
    d.legend([("arrow:muted", "Wiki page, 70 to 120 minutes"), ("arrow:muted", "Script, 12 minutes"),
              ("arrow:accent", "Curtain-up, 5 minutes of review")])
    return d
