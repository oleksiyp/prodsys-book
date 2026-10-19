"""Figure 4.1: Encore's OpenTelemetry pipeline, from SDKs through two collector tiers to backends."""
from dg import Diagram
from registry import figure


@figure
def fig_4_1():
    d = Diagram("fig-4-1", 864, 408, "Encore's telemetry pipeline",
                "Gate functions, Kubernetes services and the service mesh emit telemetry through OpenTelemetry "
                "SDKs to agent collectors, which batch and forward it, keyed by trace ID, to a gateway tier. The "
                "gateway redacts what must not be stored, routes security events to their own account and tail-"
                "samples traces, keeping errors, checkouts slower than 2 s and a 10% baseline. Metrics are kept "
                "13 months, wide events 14 days and sampled traces 30 days.")
    H = 56
    r1, r2, r3, r4 = 40, 120, 200, 296
    SX, SW = 24, 144
    AX, AW = 216, 128
    GX, GW = 432, 200
    BX, BW = 696, 144
    c = lambda r: r + H // 2
    # connectors
    for r in (r1, r2, r3):
        d.path([(SX + SW, c(r)), (AX, c(r))])
    d.path([(AX + AW, c(r1)), (GX, c(r1))], label="BY TRACE ID")
    d.path([(GX + GW // 2, r1 + H), (GX + GW // 2, r2)])
    d.path([(GX + GW // 2, r2 + H), (GX + GW // 2, r3)])
    d.path([(GX + GW, c(r1)), (BX, c(r1))])
    d.path([(GX + GW, c(r2)), (BX, c(r2))], kind="link")
    d.path([(GX + GW, c(r3)), (BX, c(r3))], kind="accent")
    d.path([(GX + GW // 2, r3 + H), (GX + GW // 2, c(r4)), (BX, c(r4))], kind="accent")
    # nodes
    d.zone(GX - 16, r1 - 16, GW + 32, r3 + H - r1 + 32, "GATEWAY TIER")
    d.node(SX, r1, SW, H, "Gate functions", "serverless · OTel SDK", "input")
    d.node(SX, r2, SW, H, "Services", "Kubernetes · OTel SDK", "input")
    d.node(SX, r3, SW, H, "Service mesh", "a span per hop", "input")
    d.node(AX, r1, AW, r3 + H - r1, "Agent collectors", "batch · forward")
    d.node(GX, r1, GW, H, "Redact", "strip what must not be stored")
    d.node(GX, r2, GW, H, "Route", "security events → own account")
    d.node(GX, r3, GW, H, "Tail sample", "errors · > 2 s · 10% baseline", "focal")
    d.node(BX, r1, BW, H, "Metrics", "unsampled · 13 months", "store")
    d.node(BX, r2, BW, H, "Security account", "separate account", "external")
    d.node(BX, r3, BW, H, "Wide events", "full detail · 14 days", "store")
    d.node(BX, r4, BW, H, "Traces", "sampled · 30 days", "store")
    d.legend([("input", "Instrumented code"), ("backend", "Collector"), ("focal", "Bill decided here"),
              ("store", "Backend · retention"), ("external", "Isolated"), ("arrow:accent", "Sampled")])
    return d
