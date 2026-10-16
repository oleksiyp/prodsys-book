"""Figure 2.3 — Rasmussen's migration toward the boundary of acceptable performance."""
import random

from dg import Diagram, label_width
from registry import figure


@figure
def fig_2_3():
    d = Diagram("fig-2-3", 864, 412, "Rasmussen's drifting operating point",
                "Rasmussen's model of work in a space bounded by economic failure (upper left), unacceptable "
                "workload (lower left) and functionally acceptable performance (right). Management pressure "
                "toward efficiency and the gradient toward least effort both push the operating point to the "
                "right; it wanders like a particle in random motion but travels steadily toward the safety "
                "boundary, which is invisible from inside daily work and lies beyond where people believe it is.")
    T, B = 48, 336
    # boundaries (quadratic arcs)
    d.zones.append(f'<path class="dg-ill-ink" d="M 168,{T} Q 56,{T + 40} 72,{(T + B) // 2}"/>')
    d.zones.append(f'<path class="dg-ill-ink" d="M 72,{(T + B) // 2} Q 56,{B - 40} 168,{B}"/>')
    # perceived boundary and the real one: x(t) = a + 2*(c-a)*t*(1-t), y = T + (B-T)*t
    d.zones.append(f'<path class="dg-ill-soft" stroke-dasharray="5 4" d="M 600,{T} Q 672,{(T + B) // 2} 600,{B}"/>')
    d.zones.append(f'<path class="dg-ill-accent" d="M 712,{T} Q 816,{(T + B) // 2} 712,{B}"/>')

    def safety_x(y):
        t = (y - T) / (B - T)
        return 712 + 2 * (816 - 712) * t * (1 - t)

    # gradients
    d.path([(128, 120), (424, 120)], label="MANAGEMENT PRESSURE TOWARD EFFICIENCY")
    d.path([(128, 268), (424, 268)], label="GRADIENT TOWARD LEAST EFFORT", side="below")
    # the drifting operating point
    rnd = random.Random(7)
    x, y = 176.0, 196.0
    pts = [(x, y)]
    while x < safety_x(y):
        x += rnd.uniform(4, 22)
        y += rnd.uniform(-10, 10)
        y = min(max(y, 160), 236)
        pts.append((x, y))
    d.nodes.append('<polyline class="dg-ill-accent" points="' + " ".join(f"{a:.1f},{b:.1f}" for a, b in pts) + '"/>')
    d.nodes.append(f'<circle class="dg-dot dg-dot-ink" cx="{pts[0][0]:.1f}" cy="{pts[0][1]:.1f}" r="4"/>')
    d.nodes.append(f'<circle class="dg-dot dg-dot-ink" cx="{pts[-1][0]:.1f}" cy="{pts[-1][1]:.1f}" r="4"/>')
    # boundary labels
    d.extra.append(f'<text class="dg-label" x="96" y="{T - 16}" style="text-anchor:start">BOUNDARY TO ECONOMIC FAILURE</text>')
    d.extra.append(f'<text class="dg-label" x="96" y="{B + 24}" style="text-anchor:start">BOUNDARY TO UNACCEPTABLE WORKLOAD</text>')
    d.extra.append(f'<text class="dg-label dg-l-accent" x="840" y="{T - 16}" style="text-anchor:end">BOUNDARY OF FUNCTIONALLY</text>')
    d.extra.append(f'<text class="dg-label dg-l-accent" x="840" y="{T - 4}" style="text-anchor:end">ACCEPTABLE PERFORMANCE</text>')
    d.extra.append(f'<text class="dg-label" x="600" y="{B + 24}" style="text-anchor:middle">WHERE DAILY WORK BELIEVES THE EDGE IS</text>')
    w = label_width("OPERATING POINT")
    d.labels.append(f'<rect class="dg-mask" x="{176 - w / 2:g}" y="212" width="{w}" height="12" rx="2"/>'
                    f'<text class="dg-label" x="176" y="221">OPERATING POINT</text>')
    d.extra.append(f'<text class="dg-label" x="{safety_x(B - 72) + 4:.0f}" y="{B - 72}" style="text-anchor:start">ACCIDENT</text>')
    return d
