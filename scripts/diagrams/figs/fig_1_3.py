"""Figure 1.3 — where Encore runs: two EU regions, cells, serverless edges, a synchronous seat ledger, GitOps."""
from dg import Diagram
from registry import figure


@figure
def fig_1_3():
    d = Diagram("fig-1-3", 864, 548, "Where Encore runs",
                "Two EU regions, EU-1 and EU-2, each with a core Kubernetes cluster, six Professional tenant "
                "cells with a database per tenant, a serverless Sale Gate edge and serverless self-service cells "
                "of about 50 venues. Fans and partners read from either region. Each event's writes are pinned "
                "to a home region; the seat ledger there commits synchronously to a standby in the other region. "
                "Both regions reconcile toward the encore-deploy Git repository.")
    # connectors
    d.path([(392, 72), (392, 96), (312, 96), (312, 148)])
    d.path([(472, 72), (472, 96), (552, 96), (552, 148)])
    d.path([(312, 360), (312, 380), (552, 380), (552, 360)], kind="accent",
           label="SYNCHRONOUS COMMIT · RPO 0", side="below")
    d.path([(392, 448), (392, 428), (220, 428), (220, 408)], dashed=True, label="RECONCILE", side="below")
    d.path([(472, 448), (472, 428), (644, 428), (644, 408)], dashed=True, label="RECONCILE", side="below")
    d.note(528, 44, "reads: either region")
    d.note(528, 57, "writes: the event's home region")
    for i, (x0, name) in enumerate(((24, "EU-1"), (448, "EU-2"))):
        d.zone(x0, 120, 392, 288, f"{name} · REGION")
        d.zone(x0 + 12, 228, 368, 60, "SIX PROFESSIONAL CELLS · A DATABASE PER TENANT")
        for k in range(6):
            d.node(x0 + 20 + k * 60, 240, 52, 36, f"P{i * 6 + k + 1}")
        left, right = x0 + 16, x0 + 200
        core_x, gate_x = (left, right) if i == 0 else (right, left)
        d.node(core_x, 148, 176, 56, "Core cluster", "Kubernetes, the services")
        d.node(gate_x, 148, 176, 56, "Sale Gate edge", "serverless, pre-warmed", "optional")
        self_x, ledger_x = (left, right) if i == 0 else (right, left)
        d.node(self_x, 304, 176, 56, "Self-service cells", "serverless, ~50 venues", "optional")
        if i == 0:
            d.node(ledger_x, 304, 176, 56, "Seat ledger", "event A's writes land here", "store")
        else:
            d.node(ledger_x, 304, 176, 56, "Seat ledger standby", "event A, in step", "store")
    d.node(348, 24, 168, 48, "Fans and partners", "public API, apps", "input")
    d.node(348, 448, 168, 48, "encore-deploy", "Git: desired state", "store")
    d.legend([("backend", "Kubernetes cluster"), ("optional", "Serverless"), ("store", "Ledger or repository"),
              ("arrow:accent", "Synchronous commit"), ("arrow:muted:dashed", "GitOps pull")])
    return d
