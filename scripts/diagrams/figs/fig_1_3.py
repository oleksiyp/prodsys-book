"""Figure 1.3 — availability as MTBF / (MTBF + MTTR): two ways to the same number."""
from chartkit import Plot
from dg import Diagram
from registry import figure


@figure
def fig_1_3():
    d = Diagram("fig-1-3", 864, 396, "Two ways to raise availability",
                "Availability equals mean time between failures divided by the sum of that and mean time to repair. "
                "Lines of equal availability (99.9%, 99.95%, 99.99%) fan out from the origin. A service that fails "
                "once a month and takes 43 minutes to recover sits at 99.9%; it reaches 99.95% either by failing "
                "half as often or by recovering twice as fast.")
    p = Plot(d, x=72, y=40, w=720, h=272, xr=(0, 64), yr=(0, 96))
    p.axes(xticks=[0, 15, 30, 45, 60], yticks=[0, 24, 48, 72, 96],
           xlabel="MEAN TIME BETWEEN FAILURES (DAYS)", ylabel="MEAN TIME TO REPAIR (MINUTES)")
    for a, lab in ((0.999, "99.9%"), (0.9995, "99.95%"), (0.9999, "99.99%")):
        k = 1440 * (1 - a) / a
        xe = min(64, 96 / k)
        p.line([(0, 0), (xe, xe * k)], kind="soft")
        p.annotate(xe, xe * k, lab, dx=-4 if xe < 64 else 6, dy=-6 if xe < 64 else 3,
                   anchor="end" if xe < 64 else "start")
    x0, y0 = p.pt(30, 43.2)
    xr, _ = p.pt(60, 43.2)
    _, yd = p.pt(30, 21.6)
    d.path([(x0 + 6, y0), (xr - 6, y0)], label="FAIL HALF AS OFTEN", side="below")
    d.path([(x0, y0 + 6), (x0, yd - 6)], kind="accent", label="RECOVER TWICE AS FAST", side="left")
    p.dot(30, 43.2, kind="ink")
    p.dot(60, 43.2, kind="ink")
    p.dot(30, 21.6, kind="ink")
    p.annotate(30, 43.2, "FAILS MONTHLY, 43 MIN TO RECOVER", dx=8, dy=-12)
    d.legend([("arrow:muted", "Fewer failures: the hard way"), ("arrow:accent", "Faster recovery: usually the cheaper way")])
    return d
