"""Figure 6.1 — the CAST control structure of the Vesper Hale on-sale."""
from dg import Diagram
from registry import figure


@figure
def fig_6_1():
    d = Diagram("fig-6-1", 864, 464, "The control structure of the Vesper Hale on-sale",
                "A CAST control structure: the readiness review and freeze exempt the node-upgrade reconciler "
                "and leave Catalog out of scope; the reconciler, the On-Sale team, the Catalog team and the Bot "
                "Screening rule each act on the purchase path; Cue advises the incident commander. Two feedback "
                "paths are missing: the reconciler never reads the on-sale calendar, and the bot rule never sees "
                "purchase-path error rates.")
    TA, TB, TC, H = 32, 176, 344, 56
    W = 160
    REC, ONS, CAT, BOT = 24, 224, 424, 624
    # --- control actions from the top tier
    d.path([(96, TA + H), (96, TB)], kind="accent", dashed=True, label="NOT READ", side="left")
    d.path([(216, TA + H), (216, 132), (144, 132), (144, TB)], label="EXEMPT", at=1)
    d.path([(304, TA + H), (304, TB)], label="FREEZE · REVIEW", side="right")
    d.path([(464, TA + H), (464, TB)], label="NOT IN SCOPE", side="right")
    d.path([(632, 60), (696, 60)], label="RESTART?")
    # incident commander: directs the response, hears the alerts
    d.path([(800, TA + H), (800, TC)])
    d.path([(824, TC), (824, TA + H)], kind="link")
    # --- control actions onto the purchase path, feedback back up
    mid_hi, mid_lo = 264, 304
    d.path([(104, TB + H), (104, TC)])
    d.label_at("DRAINS NODE 10:02", 104, mid_lo, horizontal=False, side="right")
    d.path([(264, TB + H), (264, TC)])
    d.label_at("ADMISSION 1,500/S", 264, mid_lo, horizontal=False, side="right")
    d.path([(344, TC), (344, TB + H)], kind="link")
    d.label_at("WARM-CACHE TEST", 344, mid_hi, horizontal=False, side="right", kind="link")
    d.path([(504, TB + H), (504, TC)])
    d.label_at("DEPLOY 09:52", 504, mid_lo, horizontal=False, side="right")
    d.path([(640, TB + H), (640, TC)])
    d.label_at("BLOCKS 30,000", 640, mid_hi, horizontal=False, side="left")
    d.path([(760, TC), (760, TB + H)], kind="accent", dashed=True)
    d.label_at("NO ERROR SIGNAL", 760, mid_lo, horizontal=False, side="left", kind="accent")
    # --- nodes
    d.node(24, TA, 144, H, "On-sale calendar", "owned by On-Sale", "store")
    d.node(200, TA, 280, H, "Readiness review", "freeze scope · exceptions in chat")
    d.node(528, TA, 104, H, "Cue", "ops assistant", "optional")
    d.node(696, TA, 144, H, "Incident commander", "Marta")
    d.node(REC, TB, W, H, "Reconciler", "node upgrades (platform)")
    d.node(ONS, TB, W, H, "On-Sale team", "Gate admission rate")
    d.node(CAT, TB, W, H, "Catalog team", "rolling deploys")
    d.node(BOT, TB, W, H, "Bot Screening", "velocity rule")
    d.node(24, TC, 816, H, "The purchase path",
           "Gate · Seat Inventory shard leaders · seat-map geometry cache · checkout", "focal")
    d.legend([("backend", "Controller"), ("focal", "Controlled process"),
              ("arrow:muted", "Control action"), ("arrow:link", "Feedback"),
              ("arrow:accent:dashed", "Missing feedback")])
    return d
