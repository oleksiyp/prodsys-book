"""Figure 3.3 — the manual failover: skill decays while the automation succeeds."""
import math

from chartkit import Plot
from dg import Diagram
from registry import figure


@figure
def fig_3_3():
    d = Diagram("fig-3-3", 864, 388, "The failover nobody has practiced",
                "An illustrative curve of readiness to perform Seat Inventory's manual failover. It decays for the "
                "19 months after the last manual failover in production, while about 60 automatic failovers "
                "succeed without exercising the manual path. When the Reliability team checks, 4 of 34 engineers "
                "have ever done it. Monthly drills then hold readiness up in a sawtooth; the first drill finds two "
                "stale commands.")
    p = Plot(d, x=72, y=40, w=720, h=256, xr=(0, 32), yr=(0, 1))
    p.axes(xticks=[0, 6, 12, 19, 25, 31], yticks=[], xlabel="MONTHS SINCE THE LAST MANUAL FAILOVER",
           ylabel="READINESS FOR THE MANUAL PATH (ILLUSTRATIVE)", grid=False)
    decay = [(t / 4, 0.9 * math.exp(-(t / 4) / 9)) for t in range(0, 77)]
    p.line(decay, kind="ink")
    saw, level = [(19, decay[-1][1])], decay[-1][1]
    for m in range(20, 32):
        saw.append((m, level * math.exp(-1 / 9) if m > 20 else level * math.exp(-1 / 9)))
        level = min(0.88, 0.2 + level + 0.25 * (1 - level)) if m == 20 else min(0.88, level + 0.22 * (1 - level))
        saw.append((m, level))
    saw.append((32, level * math.exp(-1 / 9)))
    p.line(saw, kind="accent")
    p.vline(19, label="CHECK: 4 OF 34 HAVE DONE IT", at=0.08)
    p.annotate(20, saw[2][1], "FIRST DRILL: TWO STALE COMMANDS", dx=-(p.px(20) - p.px(19)) - 8, dy=-4, anchor="end")
    # automatic failovers along the bottom: about 60 in 19 months
    yb = p.py(0) - 6
    for i in range(60):
        x = p.px(0.15 + i * 18.7 / 60 + 0.12 * math.sin(i * 2.3))
        d.nodes.append(f'<line class="dg-ill-soft" x1="{x:.1f}" y1="{yb - 8:.1f}" x2="{x:.1f}" y2="{yb:.1f}"/>')
    p.annotate(0.2, 0.06, "ABOUT 60 AUTOMATIC FAILOVERS, NONE ON THE MANUAL PATH", dx=0, dy=-8)
    d.legend([("arrow:muted", "No practice: skill decays"), ("arrow:accent", "Monthly drills from month 20")])
    return d
