"""Figure 5.3: the Vesper Hale response in ICS shape: roles, and the lines communication ran along."""
from dg import Diagram
from registry import figure


@figure
def fig_5_3():
    d = Diagram("fig-5-3", 864, 440, "Roles and lines of communication at Vesper Hale",
                "Marta, the incident commander, directs three roles: Rui as ops lead, with Jonas of Seat Inventory "
                "and Noor of Bot Screening under him; a scribe keeping the log, with Cue drafting the timeline; and "
                "Elif as comms lead. Elif speaks outward to fans through the status page and upward to "
                "stakeholders, and at 10:24 carried Support's report inward, that fans were being told they were bots.")
    d.zone(16, 24, 600, 352, "INCIDENT CHANNEL · RESPONDERS")
    # command lines
    d.path([(288, 104), (288, 136), (168, 136), (168, 168)])
    d.path([(388, 104), (388, 168)])
    d.path([(432, 104), (432, 136), (536, 136), (536, 168)])
    d.path([(96, 224), (96, 288)])
    d.path([(240, 224), (240, 288)])
    # Cue
    d.path([(388, 288), (388, 224)], kind="link", label="DRAFT TIMELINE", side="right")
    d.path([(344, 288), (344, 256), (288, 256), (288, 224)], kind="link", dashed=True)
    # outward, upward, inward
    d.path([(568, 168), (568, 76), (672, 76)], label="OUTWARD", at=1)
    d.path([(600, 196), (672, 196)], label="UPWARD")
    d.path([(672, 316), (536, 316), (536, 224)], kind="accent", label="INWARD · 10:24", at=0, side="below")
    # nodes
    d.node(232, 48, 208, 56, "Incident commander", "Marta · does not type", "focal")
    d.node(32, 168, 272, 56, "Ops lead", "Rui · directs every change")
    d.node(320, 168, 136, 56, "Scribe", "keeps the log")
    d.node(472, 168, 128, 56, "Comms lead", "Elif · Reliability")
    d.node(32, 288, 128, 56, "Seat Inventory", "Jonas")
    d.node(176, 288, 128, 56, "Bot Screening", "Noor · from 10:27")
    d.node(320, 288, 136, 56, "Cue", "read-only", "optional")
    d.node(672, 48, 168, 56, "Status page", "fans · every 15 min", "external")
    d.node(672, 168, 168, 56, "Stakeholders", "leadership · tenants", "input")
    d.node(672, 288, 168, 56, "Support", "fans writing in", "input")
    d.note(388, 364, "suggests; acts only on approval", anchor="middle")
    d.note(756, 360, "“the site says I'm a bot”", anchor="middle")
    d.legend([("focal", "Command"), ("backend", "Responder role"), ("optional", "Assistant"),
              ("input", "Audience inside Encore"), ("external", "Public"), ("arrow:link", "Cue's output")])
    return d
