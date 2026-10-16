"""Figure 10.6: the October region failover game day, EU-1 to EU-2."""
from dg import Diagram
from registry import figure


@figure
def fig_10_6():
    d = Diagram("fig-10-6", 864, 520, "The region failover game day",
                "Every event homed in EU-1 is failed over to EU-2. The core held: Seat Inventory standbys were "
                "promoted in about four minutes and fencing rejected late writes from EU-1 leaders. Three edges "
                "did not: the Sale Gate was pre-warmed only in EU-1, Bot Screening's risk data reached EU-2 only "
                "by a daily copy, and an Orders reconciliation job whose schedule named EU-1 sat idle for six hours.")
    W, H = 200, 56
    A, B = 40, 624
    R = [136, 224, 312, 400]
    d.zone(16, 112, 248, 376, "EU-1 · FAILED OUT")
    d.zone(600, 112, 248, 376, "EU-2 · TAKES OVER")
    # traffic
    d.path([(392, 88), (392, 164), (A + W, 164)], dashed=True, label="BEFORE", at=1, side="above")
    d.path([(472, 88), (472, 164), (B, 164)], label="AFTER", at=1, side="above")
    # seat ledger
    d.path([(A + W, 240), (B, 240)], label="SYNCHRONOUS REPLICATION · ~18 MS")
    d.path([(A + W, 264), (B, 264)], kind="accent", dashed=True, label="LATE WRITES · FENCED, REJECTED",
           side="below")
    # risk data
    d.path([(A + W, 340), (B, 340)], dashed=True, label="DAILY COPY ONLY")
    # nodes
    d.node(332, 32, 200, 56, "Fans + synthetic buyers", "small events · test event", "input")
    d.node(A, R[0], W, H, "Sale Gate", "pre-warmed here")
    d.node(A, R[1], W, H, "Seat Inventory", "leaders until failover")
    d.node(A, R[2], W, H, "Risk data", "Bot Screening account", "store")
    d.node(A, R[3], W, H, "Orders reconciliation", "schedule names EU-1")
    d.node(B, R[0], W, H, "Sale Gate", "cold starts", "optional")
    d.node(B, R[1], W, H, "Seat Inventory", "promoted in ~4 min")
    d.node(B, R[2], W, H, "Risk data", "yesterday's signals", "optional")
    d.node(B, R[3], W, H, "Orders reconciliation", "idle for 6 h", "optional")
    d.note(432, 424, "no hold or sale lost; each finding", anchor="middle")
    d.note(432, 438, "became a ticket with an owner", anchor="middle")
    d.legend([("backend", "Held"), ("optional", "Found at the edges"), ("arrow:muted", "Traffic, replication"),
              ("arrow:muted:dashed", "Before, or copied daily"), ("arrow:accent:dashed", "Fenced write")])
    return d
