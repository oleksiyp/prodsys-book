"""Figure 1.10 — one bad minute crosses every layer of the stack."""
from html import escape

from dg import Diagram
from registry import figure


@figure
def fig_1_10():
    d = Diagram("fig-1-10", 864, 452, "One bad minute crosses the stack",
                "Six layers of Encore's production stack as horizontal bands. A node drain in the runtime appears "
                "as a latency spike in telemetry, a burning error budget in the SLO layer, a page and an incident, "
                "a review in learning, and finally a change shipped through delivery. Each layer sees only its "
                "own part of the event.")
    layers = ["Learning", "Incident process", "SLOs", "Telemetry", "Delivery", "Runtime"]
    T, RH, NH, NW = 32, 56, 40, 120
    cols = [204, 308, 412, 516, 620, 720]
    for i, name in enumerate(layers):
        y = T + i * RH
        d.zones.append(f'<rect class="dg-zone" x="24" y="{y}" width="816" height="{RH - 8}" rx="6"/>')
        d.extra.append(f'<text class="dg-name" x="100" y="{y + RH // 2}">{escape(name)}</text>')
    ev = [(5, "Node drain", "reconciler, on time", "focal"),
          (3, "Latency spike", "seat map p99 climbs", "backend"),
          (2, "Budget burns", "seat-map SLO", "backend"),
          (1, "Page, incident", "on-call, then IC", "backend"),
          (0, "Review", "why it made sense", "backend"),
          (4, "Change ships", "drain policy fixed", "backend")]
    boxes = []
    for (row, name, sub, kind), x in zip(ev, cols):
        y = T + row * RH + 4
        boxes.append((x, y, row))
    for (x, y, row), (nx, ny, nrow) in zip(boxes, boxes[1:]):
        cy = y + NH // 2
        tx = nx + NW // 2
        if nrow < row:
            d.path([(x + NW, cy), (tx, cy), (tx, ny + NH)])
        else:
            d.path([(x + NW, cy), (tx, cy), (tx, ny)])
    for (row, name, sub, kind), (x, y, _) in zip(ev, boxes):
        d.node(x, y, NW, NH, name, sub, kind)
    # time strip
    ty = T + 6 * RH + 8
    d.zones.append(f'<line class="dg-axis" x1="204" y1="{ty}" x2="840" y2="{ty}"/>')
    for x0, x1, lab in ((204, 412, "SECONDS"), (412, 620, "MINUTES"), (620, 840, "DAYS")):
        d.zones.append(f'<line class="dg-axis" x1="{x0}" y1="{ty - 4}" x2="{x0}" y2="{ty + 4}"/>')
        d.extra.append(f'<text class="dg-tick" x="{(x0 + x1) / 2:g}" y="{ty + 16}" text-anchor="middle">{lab}</text>')
    d.legend([("focal", "Where it starts"), ("backend", "What each layer sees"), ("arrow:muted", "How it shows up next")])
    return d
