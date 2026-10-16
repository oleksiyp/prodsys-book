"""Figure 2.5 — above and below the line of representation (after the STELLA report)."""
from dg import Diagram
from registry import figure


@figure
def fig_2_5():
    d = Diagram("fig-2-5", 864, 420, "Above and below the line",
                "After the STELLA report (2017). Encore's people sit above the line of representation, each with a "
                "partial mental model. Below it sit the services, clusters and the payment provider, which nobody "
                "sees directly. Between them are the representations (dashboards, alerts, traces, deploy tools) "
                "through which people see the system and act on it.")
    W, H = 152, 52
    xs = [160, 332, 504, 676]
    R1, R2, R3 = 48, 180, 300
    people = [("On-call engineer", "model: their service"), ("On-Sale team", "model: tonight's plan"),
              ("Reliability team", "model: past incidents"), ("Incident commander", "model: what is burning")]
    reps = [("Dashboards, SLOs", None), ("Alerts and pages", None), ("Traces and logs", None),
            ("Deploy tools", None)]
    below = [("Gate, Inventory", "services, shards", "backend"), ("Orders, Payments", "the saga", "backend"),
             ("Kubernetes cells", "nodes, reconcilers", "backend"), ("Payment provider", "outside party", "external")]
    # line of representation
    LY = R2 + H // 2
    d.zones.append(f'<line class="dg-ill-accent" stroke-dasharray="6 4" x1="24" y1="{LY}" x2="840" y2="{LY}"/>')
    for i, x in enumerate(xs):
        c = x + W // 2
        # sees: up from below to reps to people (left); acts: down (right)
        d.path([(c - 24, R3), (c - 24, R2 + H)], label="SEES" if i == 0 else None, side="left")
        d.path([(c - 24, R2), (c - 24, R1 + H)], label="SEES" if i == 0 else None, side="left")
        d.path([(c + 24, R1 + H), (c + 24, R2)], label="ACTS" if i == 0 else None, side="right")
        d.path([(c + 24, R2 + H), (c + 24, R3)], label="ACTS" if i == 0 else None, side="right")
    for x, (n, s) in zip(xs, people):
        d.node(x, R1, W, H, n, s, "input")
    for x, (n, s) in zip(xs, reps):
        d.node(x, R2, W, H, n, s, "store")
    for x, (n, s, k) in zip(xs, below):
        d.node(x, R3, W, H, n, s, k)
    d.extra.append(f'<text class="dg-eyebrow" x="24" y="{R1 - 16}" style="text-anchor:start">ABOVE THE LINE: PEOPLE, EACH WITH A PARTIAL MODEL</text>')
    d.extra.append(f'<text class="dg-eyebrow" x="24" y="{R3 + H + 20}" style="text-anchor:start">BELOW THE LINE: WHAT NOBODY SEES DIRECTLY</text>')
    d.extra.append(f'<text class="dg-label dg-l-accent" x="24" y="{LY - 16}" style="text-anchor:start">LINE OF</text>')
    d.extra.append(f'<text class="dg-label dg-l-accent" x="24" y="{LY - 6}" style="text-anchor:start">REPRESENTATION</text>')
    d.legend([("input", "People"), ("store", "Representations"), ("backend", "The running system"),
              ("external", "Outside party"), ("arrow:muted", "Seeing and acting, only through representations")])
    return d
