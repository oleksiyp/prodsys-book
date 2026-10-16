"""Figure 7.1: three governors on Catalog's replica count."""
from chartkit import Plot
from dg import Diagram
from registry import figure


@figure
def fig_7_1():
    d = Diagram("fig-7-1", 864, 372, "Three governors on one lever",
                "A sketch of Catalog's replica count over half an hour. An engineer scales it from 20 to 60; "
                "within a minute the GitOps agent restores the manifest's 20; the autoscaler then trims the "
                "idle pods toward its floor of 12, and the GitOps agent resets them to 20 again, drawing a "
                "sawtooth while the engineer believes the service is at 60.")
    p = Plot(d, x=72, y=40, w=744, h=232, xr=(0, 36), yr=(0, 70))
    p.axes(xticks=[0, 6, 12, 18, 24, 30, 36], yticks=[0, 12, 20, 40, 60],
           xlabel="MINUTES", ylabel="CATALOG REPLICAS")
    events = [(0, 20), (3, 60), (4, 20), (9, 18), (10, 16), (11, 14), (12, 20), (17, 18), (18, 16),
              (19, 14), (21, 20), (26, 18), (27, 16), (28, 14), (30, 20), (35, 18)]
    pts = []
    for i, (t, r) in enumerate(events):
        if pts:
            pts.append((t, pts[-1][1]))
        pts.append((t, r))
    pts.append((36, pts[-1][1]))
    p.hline(60, "WHAT THE ENGINEER BELIEVED", side="above", at=0.82)
    p.hline(12, "HPA FLOOR", side="below", at=0.97)
    p.line(pts, kind="accent")
    p.annotate(3, 60, "KUBECTL SCALE → 60", dx=8, dy=-8, kind="accent")
    p.annotate(4, 40, "GITOPS REVERTS → 20", dx=8, dy=3)
    p.annotate(10, 15, "HPA TRIMS IDLE PODS", dx=-4, dy=20, anchor="end")
    p.annotate(12, 20, "GITOPS RESETS → 20", dx=4, dy=-10)
    d.legend([("arrow:accent", "Actual replicas"), ("arrow:muted:dashed", "Belief and floor")])
    return d
