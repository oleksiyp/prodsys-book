"""Figure 4.3: one fan's purchase drawn to scale as a trace waterfall."""
from html import escape

from dg import Diagram
from registry import figure

# name, service, start ms, duration ms, depth, kind
SPANS = [
    ("POST /checkout", "API gateway", 0, 1140, 0, "backend"),
    ("admission.verify", "Sale Gate", 4, 12, 1, "backend"),
    ("bot.score", "Bot Screening", 18, 35, 1, "backend"),
    ("inventory.Hold", "Seat Inventory", 56, 48, 1, "backend"),
    ("saga.purchase", "Orders", 108, 1020, 1, "backend"),
    ("psp.authorize", "Orders · PSP", 150, 640, 2, "focal"),
    ("inventory.Sell", "Seat Inventory", 830, 31, 2, "backend"),
    ("ticket.issue", "Notification", 4200, 380, 0, "optional"),
]
X0, K = 248, 0.16           # 0 ms at x=248, 0.16 px per ms: 3 s spans 480 px
X1, T1 = 760, 4150          # right segment, after the axis break, starts at 4,150 ms
Y0, ROW = 40, 28


def xm(ms):
    return X0 + ms * K if ms <= 3000 else X1 + (ms - T1) * K


@figure
def fig_4_3():
    d = Diagram("fig-4-3", 864, 364, "One fan's purchase as a waterfall",
                "The trace of Figure 4.2 drawn to scale against the 3 s checkout budget. The checkout takes 1,140 ms; "
                "inside the purchase saga the PSP authorization takes 640 ms of its 800 ms share. Ticket issuance "
                "starts 4.2 s after the checkout began, in its own trace, joined by a span link from the SeatSold "
                "write rather than as a child.")
    out = []
    ys = [Y0 + i * ROW for i in range(len(SPANS))]
    # the PSP's 800 ms share, behind its row
    y_psp = ys[5]
    out.append(f'<rect class="dg-area dg-ar-soft" x="{xm(150):.1f}" y="{y_psp + 2}" width="{800 * K:.1f}" height="{ROW - 4}"/>')
    d.zones.append("\n".join(out))
    d.label_at("PSP SHARE OF THE BUDGET · 800 MS", xm(950) + 36, y_psp + ROW // 2, horizontal=False, side="right")
    # axis with a break
    ya = ys[-1] + ROW + 8
    ax = [f'<line class="dg-axis" x1="{X0}" y1="{ya}" x2="{X0 + 3000 * K + 16}" y2="{ya}"/>',
          f'<line class="dg-axis" x1="{X1 - 8}" y1="{ya}" x2="{840}" y2="{ya}"/>',
          f'<path class="dg-ill-soft" d="M {X0 + 3000 * K + 12},{ya + 5} l 8,-10 M {X1 - 12},{ya + 5} l 8,-10"/>']
    for t in (0, 500, 1000, 1500, 2000, 2500, 3000, 4200, 4600):
        x = xm(t)
        lab = f"{t:,}" if t <= 3000 else f"+{t / 1000:.1f} s"
        ax.append(f'<line class="dg-axis" x1="{x:.1f}" y1="{ya}" x2="{x:.1f}" y2="{ya + 4}"/>')
        ax.append(f'<text class="dg-tick" x="{x:.1f}" y="{ya + 16}" text-anchor="middle">{lab}</text>')
    ax.append(f'<text class="dg-axis-label" x="{X0 + 3000 * K}" y="{ya + 32}" text-anchor="end">MILLISECONDS SINCE THE FAN PRESSED BUY</text>')
    for y in ys:
        ax.append(f'<line class="dg-grid" x1="24" y1="{y + ROW}" x2="840" y2="{y + ROW}"/>')
    d.zones.append("\n".join(ax))
    # the 3 s budget
    xb = xm(3000)
    d.nodes.append(f'<line class="dg-series dg-s-soft" x1="{xb}" y1="{Y0 - 8}" x2="{xb}" y2="{ya}" stroke-dasharray="5 4"/>')
    d.label_at("3 S CHECKOUT BUDGET", xb, Y0 + 8, horizontal=False, side="left")
    # span link from inventory.Sell to ticket.issue
    ys_sell, ys_tick = ys[6] + ROW // 2, ys[7] + ROW // 2
    xs = round(xm(830 + 15) / 4) * 4
    d.path([(xs, ys[6] + ROW - 7), (xs, ys_tick), (round(xm(4200) / 4) * 4 - 2, ys_tick)],
           kind="link", dashed=True, label="SPAN LINK · NOT A CHILD", at=1)
    # rows
    for (name, svc, start, dur, depth, kind), y in zip(SPANS, ys):
        d.extra.append(f'<text class="dg-note" x="{24 + depth * 12}" y="{y + ROW // 2 + 3}" text-anchor="start">'
                       f'{escape(name)}</text>')
        d.extra.append(f'<text class="dg-tick" x="{X0 - 12}" y="{y + ROW // 2 + 3}" text-anchor="end">{escape(svc)}</text>')
        x, w = xm(start), max(2.0, dur * K)
        dash = ' stroke-dasharray="4,3"' if kind == "optional" else ""
        d.nodes.append(f'<rect class="dg-n dg-n-{kind}" x="{x:.1f}" y="{y + 7}" width="{w:.1f}" height="{ROW - 14}" rx="2"{dash}/>')
        if kind != "optional":
            d.extra.append(f'<text class="dg-tick" x="{x + w + 6:.1f}" y="{y + ROW // 2 + 3}" text-anchor="start">{dur:,} ms</text>')
    d.legend([("backend", "Span"), ("focal", "The PSP call"), ("optional", "Its own trace, linked"),
              ("arrow:link:dashed", "Span link")])
    return d
