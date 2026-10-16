"""Figure 2.2 — Reason's Swiss cheese, with the retry storm's defenses as the slices."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_2_2():
    d = Diagram("fig-2-2", 864, 364, "The retry storm through the cheese",
                "Reason's Swiss cheese model applied to Encore's first big outage. A slow payment provider is the "
                "trigger; four defenses stand between it and the fans: retries, connection pools, health checks "
                "and the autoscaler. Each has holes left by latent conditions set far from the sharp end, and on "
                "the day they lined up, letting the slowdown through to an outage of the purchase path.")
    TY = 152            # trajectory height
    top, bot = 48, 240  # slice extent
    slices = [
        (240, "Retries", ["at every layer;", "nobody owns the sum"], [96, 200]),
        (368, "Connection pools", ["shared with the", "health checks"], [80, 212]),
        (496, "Health checks", ["measure the pool,", "not the instance"], [104, 196]),
        (624, "Autoscaler", ["policy written for", "a different overload"], [88, 208]),
    ]
    # trajectory first, so slices sit on top; the holes on the line are cut through again below
    d.arrows.append(f'<path class="dg-a dg-a-accent" d="M 160,{TY} L 732,{TY}" marker-end="url(#fig-2-2-m-accent)"/>')
    for cx, name, hole, extra in slices:
        x0, x1 = cx - 20, cx + 20
        d.zones.append(f'<polygon class="dg-ill-fill" points="{x0},{top + 16} {x1},{top} {x1},{bot - 16} {x0},{bot}"/>')
        for hy in extra:
            d.zones.append(f'<ellipse class="dg-mask" cx="{cx}" cy="{hy}" rx="9" ry="15"/>'
                           f'<ellipse class="dg-ill-soft" cx="{cx}" cy="{hy}" rx="9" ry="15"/>')
        d.zones.append(f'<ellipse class="dg-mask" cx="{cx}" cy="{TY}" rx="10" ry="17"/>'
                       f'<ellipse class="dg-ill-soft" cx="{cx}" cy="{TY}" rx="10" ry="17"/>')
        d.extra.append(f'<text class="dg-name" x="{cx}" y="{bot + 24}">{escape(name)}</text>')
        for i, line in enumerate(hole):
            d.extra.append(f'<text class="dg-sub" x="{cx}" y="{bot + 40 + i * 12}">{escape(line)}</text>')
    d.node(24, TY - 28, 128, 56, "PSP slows", "200 ms to 8 s", "input")
    d.node(740, TY - 28, 100, 56, "Outage", "purchase path", "focal")
    d.extra.append('<text class="dg-eyebrow" x="432" y="32">DEFENSES, EACH WITH HOLES LEFT BY LATENT CONDITIONS</text>')
    d.legend([("input", "Trigger at the sharp end"), ("arrow:accent", "The day the holes lined up"),
              ("focal", "Loss")])
    return d
