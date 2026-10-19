"""Figure 7.5 — the Friday of the added dates, from curtain-up to sold out."""
from dg import Diagram, label_width
from chartkit import Plot
from registry import figure


def hhmm(m):
    return f"{m // 60:02d}:{m % 60:02d}"


def budget(t):
    """Window error budget spent (%), 10:00–11:00: flat, then the Dutch slowdown from 10:09."""
    if t <= 609:
        return 0.4 * (t - 600) / 9
    if t <= 640:
        return 0.4 + (18 - 0.4) * (t - 609) / 31
    return 18 + 4 * (t - 640) / 20


@figure
def fig_7_5():
    d = Diagram("fig-7-5", 864, 424, "The added dates' Friday morning",
                "A timeline of the Friday, with the morning before 10:00 compressed: curtain-up at 07:30, the "
                "freeze at 08:00 with two exceptions registered, and at 09:40 a pre-warm check that timed out and "
                "was rerun by hand. From 10:00 the Gate is open; at 10:09 a Dutch bank's card authentication "
                "slows, the slow burn-rate alert fires and the commander decides not to act; the window's error "
                "budget spent climbs to about 22%, and all four dates sell out within the hour.")
    top, h = 96, 232
    a = Plot(d, x=72, y=top, w=272, h=h, xr=(420, 600), yr=(0, 30))
    b = Plot(d, x=376, y=top, w=440, h=h, xr=(600, 660), yr=(0, 30))
    a.axes(xticks=[420, 480, 540], xfmt=hhmm, grid=False,
           ylabel="BEFORE THE GATE (COMPRESSED)")
    b.axes(xticks=[600, 615, 630, 645, 660], yticks=[0, 10, 20, 30], xfmt=hhmm,
           yfmt=lambda v: f"{v}%", ylabel="WINDOW ERROR BUDGET SPENT", xlabel="FRIDAY, CET")
    yb = top + h
    d.extra.append(f'<path class="dg-ill-soft" d="M 350,{yb + 5} L 356,{yb - 5} M 358,{yb + 5} L 364,{yb - 5}"/>')
    pts = [(t, budget(t)) for t in range(600, 661)]
    b.area(pts, kind="accent")
    b.line(pts, kind="accent")
    b.annotate(660, 22, "≈22%", dx=-6, dy=-8, anchor="end", kind="accent")
    row = lambda k: (top + 12 + 20 * k - top) / h  # vline label position as a fraction of the plot
    a.vline(450, "07:30 CURTAIN-UP", at=row(0))
    a.vline(480, "08:00 FREEZE · 2 EXCEPTIONS", at=row(1))
    a.vline(580, kind="soft")
    d.label_at("09:40 PRE-WARM CHECK RERUN BY HAND", a.px(580), top + 12 + 20 * 3,
               horizontal=False, side="left")
    b.vline(609, "10:09 DUTCH CARD AUTH SLOWS", at=row(0))
    d.label_at("SLOW-BURN ALERT · STATUS NOTE, NO ACTION", b.px(609), top + 12 + 20,
               horizontal=False, side="right")
    # under the axis, so it clears the 10:09 line that runs the full height of the plot
    d.label_at("10:00 GATE OPENS", 376 + label_width("10:00 GATE OPENS") / 2, yb + 24, horizontal=True, side="below")
    d.label_at("ALL FOUR DATES SOLD OUT", 816, top + 12, horizontal=False, side="left")
    d.legend([("arrow:accent", "Window error budget spent"), ("arrow:muted", "Event (dashed line)")])
    return d
