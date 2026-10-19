"""Figure 1.4 — the operator's lineage on a timeline, 1945 to today."""
from html import escape

from dg import Diagram
from registry import figure

Y0, PX = 1945, 9.0
X0 = 48


def _x(year):
    return X0 + (year - Y0) * PX


@figure
def fig_1_4():
    d = Diagram("fig-1-4", 864, 344, "Who runs the software, 1945 to today",
                "A timeline of running software: the computer operator of the closed shop from the 1950s, the "
                "system administrator from the 1980s, site reliability engineering and DevOps from 2003 and 2009, "
                "and today coding agents as authors. Events marked: the 1947 Mark II logbook, GM-NAA I/O in 1956, "
                "System/360 in 1964, ITIL in the late 1980s, Google's first SRE team in 2003, Flickr and the first "
                "DevOpsDays in 2009, and coding agents today.")
    AX = 168  # axis y
    # eras, above the axis
    eras = [(1950, 1980, "Computer operator", "the closed shop"),
            (1980, 2003, "System administrator", "scripts and config files"),
            (2003, 2024, "SRE and DevOps", "ops as a software problem")]
    for a, b, name, sub in eras:
        x1, x2 = _x(a), _x(b)
        d.extra.append(f'<rect class="dg-n dg-n-store" x="{x1 + 2:g}" y="64" width="{x2 - x1 - 4:g}" height="48" rx="6"/>')
        d.extra.append(f'<text class="dg-name" x="{(x1 + x2) / 2:g}" y="86">{escape(name)}</text>')
        d.extra.append(f'<text class="dg-sub" x="{(x1 + x2) / 2:g}" y="101">{escape(sub)}</text>')
    xa = _x(2024)
    d.extra.append(f'<rect class="dg-n dg-n-focal" x="{xa + 2:g}" y="64" width="{_x(2030) - xa - 2:g}" height="48" rx="6"/>')
    d.extra.append(f'<text class="dg-label dg-l-accent" x="{(xa + _x(2030)) / 2 + 1:g}" y="91">AGENTS</text>')
    d.extra.append(f'<text class="dg-eyebrow" x="{X0}" y="48" style="text-anchor:start">WHO STANDS BETWEEN THE CODE AND ITS USERS</text>')
    # axis and decade ticks
    d.zones.append(f'<line class="dg-axis" x1="{X0}" y1="{AX}" x2="{_x(2030):g}" y2="{AX}"/>')
    for yr in range(1950, 2031, 10):
        x = _x(yr)
        d.zones.append(f'<line class="dg-axis" x1="{x:g}" y1="{AX - 4}" x2="{x:g}" y2="{AX + 4}"/>')
        d.zones.append(f'<text class="dg-tick" x="{x:g}" y="{AX - 10}" text-anchor="middle">{yr}</text>')
    # events, below the axis on three staggered levels
    events = [(1947, 2, "1947", "Mark II logbook:", "the first bug, taped in"),
              (1956, 1, "1956", "GM-NAA I/O cuts", "setup time between jobs"),
              (1964, 0, "1964", "IBM System/360", "spreads the operator's job"),
              (1989, 0, "LATE 1980S", "ITIL: change boards,", "and the wall between"),
              (2003, 2, "2003", "Google's first SRE team,", "seven engineers"),
              (2009, 1, "2009", "Flickr's 10 deploys a day;", "first DevOpsDays, Ghent"),
              (2026, 0, "TODAY", "the author may not", "be a person at all")]
    for yr, lvl, head, l1, l2 in events:
        x = _x(yr)
        ty = AX + 32 + lvl * 48
        accent = yr in (2026,)
        dot = "dg-dot-accent" if accent else "dg-dot-ink"
        d.nodes.append(f'<line class="dg-ill-soft" x1="{x:g}" y1="{AX}" x2="{x:g}" y2="{ty - 10}"/>')
        d.nodes.append(f'<circle class="dg-dot {dot}" cx="{x:g}" cy="{AX}" r="4"/>')
        anchor = "end" if yr >= 2026 else "start"
        tx = x + 2 if anchor == "start" else x + 6
        hcls = "dg-label dg-l-accent" if accent else "dg-label"
        d.extra.append(f'<text class="{hcls}" x="{tx:g}" y="{ty}" style="text-anchor:{anchor}">{escape(head)}</text>')
        d.extra.append(f'<text class="dg-note" x="{tx:g}" y="{ty + 13}" text-anchor="{anchor}">{escape(l1)}</text>')
        d.extra.append(f'<text class="dg-note" x="{tx:g}" y="{ty + 25}" text-anchor="{anchor}">{escape(l2)}</text>')
    return d
