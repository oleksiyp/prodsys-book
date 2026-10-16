"""Figure 13.5 — the hierarchy of controls, with Encore's actions placed on it."""
from dg import Diagram
from registry import figure

BANDS = [
    ("Eliminate", "Nodes hosting shard leaders are never drained during a sale",
     "(the hazard is gone, whoever is on call)"),
    ("Substitute", "Freeze scope derived from the traced dependency graph,",
     "not a hand-kept list of services"),
    ("Engineer", "Reconciler reads the calendar and holds from T−2h; cold-cache",
     "test gates admission changes; bot rule drops to observe-only"),
    ("Procedure", "Exception register reviewed monthly; readiness review asks",
     "about cache state; every bot rule has an owner and a review date"),
    ("Remind", "“Remind engineers to check cache state”",
     "a wish, not a control"),
]


@figure
def fig_13_5():
    d = Diagram("fig-13-5", 864, 412, "The hierarchy of controls at Encore",
                "An inverted pyramid of five kinds of remedy, from the most reliable at the top to the least at "
                "the bottom: eliminate the hazard, substitute something safer, engineer a barrier, add procedure "
                "and training, and remind people. Beside each level sits the Encore change from the Vesper Hale "
                "review that belongs there; the bottom level holds a reminder, which is a wish.")
    top, bh, gap = 52, 52, 8
    L, R = 40, 360           # widest band
    shrink = 28              # per side, per band
    d.label_at("WORKS EVEN WHEN NOBODY REMEMBERS", (L + R) / 2, top, horizontal=True, side="above")
    for i, (name, l1, l2) in enumerate(BANDS):
        y0 = top + i * (bh + gap)
        a0, b0 = L + i * shrink, R - i * shrink
        a1, b1 = a0 + shrink - 4, b0 - shrink + 4
        cls = "dg-ill-fill-accent" if i == len(BANDS) - 1 else "dg-ill-fill"
        d.zones.append(f'<polygon class="{cls}" points="{a0},{y0} {b0},{y0} {b1},{y0 + bh} {a1},{y0 + bh}"/>')
        d.nodes.append(f'<text class="dg-name" x="{(L + R) // 2}" y="{y0 + bh // 2 + 4}">{name}</text>')
        d.path([(b0 - 8, y0 + bh // 2), (392, y0 + bh // 2)], kind="muted", arrow=False)
        d.extra.append(f'<text class="dg-note" x="400" y="{y0 + bh // 2 - 3}">{l1}</text>')
        d.extra.append(f'<text class="dg-note" x="400" y="{y0 + bh // 2 + 11}">{l2}</text>')
    yb = top + 5 * (bh + gap) - gap
    d.label_at("WORKS ONLY IF SOMEONE REMEMBERS", (L + R) / 2, yb, horizontal=True, side="below",
               kind="accent")
    d.legend([("backend", "Kind of remedy, most reliable at the top"),
              ("focal", "Depends on someone remembering")])
    return d
