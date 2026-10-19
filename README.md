# Running Production Systems in the AI & Cloud Era

*Reliability is something people and machines keep producing together.*

<small>© 2026 Oleksiy Pylypenko · Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — share and adapt freely, non-commercially, with attribution. Source on [GitHub](https://github.com/oleksiyp/prodsys-book). Architecture book: [*Software Architecture in the AI & Cloud Era*](https://oleksiyp.github.io/arch-book/).</small>

## Preface

Every system worth building eventually leaves the hands of the people who designed it and enters a world they cannot fully foresee: real users, real traffic, real failures, at three in the morning and on the busiest day of the year. We call that world *production*, and for most of our field's history we treated it as the place where software went after the interesting work was done. The engineers wrote the code and somebody else kept it running. That division never served anyone well, and in the last fifteen years it has quietly dissolved. Cloud runtimes, service level objectives, observability, infrastructure as code, progressive delivery, chaos engineering, blameless reviews and, most recently, AI assistants that read our telemetry and write our changes have remade the practice of running software almost completely.

The problems beneath the practice have not changed at all. A system of many interacting parts still fails in ways no single part explains. Automation still removes the easy work and leaves people with the hard work, at the moment they are least prepared for it. Queues still grow without bound as utilization approaches one, and organizations still drift, one reasonable exception at a time, toward the edge of what they can safely do. These are old lessons, learned at great cost in telephone exchanges, nuclear plants, cockpits and launch pads long before anyone ran a Kubernetes cluster. I have come to believe that the newest techniques are best understood, and best used, by someone who knows the older lessons that explain why they work.

This book is written for that reader: an engineer who builds services and now runs them, a team lead who has inherited an on-call rotation, an architect who wants the systems they design to survive contact with the world. It teaches today's techniques, the ones a team should actually use in 2026, and it roots each one in its lineage: safety science, control theory, queueing, and the ironies of automation. AI appears where it really changes the practice, and nowhere else. The tools will keep changing. The judgment they require will not.

It follows *Software Architecture in the AI & Cloud Era*, which this book calls the Architecture book, and it continues that book's story. Reading one does not require the other, but the two were written to be read together. The first asks how to shape a system; this one asks how to keep it running.

### Influences & Attribution

Much of this book's method comes from others, and each chapter's references point to the original works, which are always the better read. The practice of site reliability engineering follows Google's *Site Reliability Engineering* and *The Site Reliability Workbook*, along with Alex Hidalgo's *Implementing Service Level Objectives*. Observability draws on Charity Majors, Liz Fong-Jones and George Miranda's *Observability Engineering*. Stability patterns come from Michael Nygard's *Release It!*, delivery from Jez Humble and David Farley's *Continuous Delivery* and the DORA research of Nicole Forsgren and colleagues, and performance from Brendan Gregg and Neil Gunther. Chaos engineering follows Casey Rosenthal and Nora Jones, and evaluation of AI systems follows Shreya Shankar, Hamel Husain and Chip Huyen.

The book's intellectual foundation is older. Charles Perrow, James Reason, Jens Rasmussen, Richard Cook, David Woods, Erik Hollnagel, Sidney Dekker, Nancy Leveson, Diane Vaughan and Lisanne Bainbridge studied how complex systems fail and how people keep them working. Their work, written for aviation, medicine, nuclear power and spaceflight, turns out to describe software operations with uncomfortable accuracy.

Several terms used here as common vocabulary have specific coiners: toil and error budgets (Google SRE), the USE method (Brendan Gregg), the RED method (Tom Wilkie), the Universal Scalability Law (Neil Gunther), normalization of deviance (Diane Vaughan), Safety-I and Safety-II (Erik Hollnagel), STAMP, STPA and CAST (Nancy Leveson), chaos engineering (Netflix) and the Swiss cheese model (James Reason).

### Authorship & Disclaimer

Written and directed by Oleksiy Pylypenko, with AI assistance (Anthropic's Claude). The judgment in it comes from twenty-plus years of practice: platform engineering inside a large bank, API architecture in fintech, and a decade of maintaining a widely used open-source library. The author chose the thesis, the structure, the examples and the trade-offs, edited every chapter, and takes responsibility for every claim, errors included. Encore and every kata company are fictional; historical events are described from the public record. The content is provided as-is, without warranty of any kind: educational material, not professional advice for any specific system. The license's full disclaimer of warranties applies.

## How to Read This Book

One company runs through all 15 chapters: **Encore**, which sells tickets to live concerts, and whose traffic can rise 500× in minutes when a major tour is announced. Readers of the Architecture book watched Encore grow from nine engineers to 400. This book begins the morning after that story ended and asks a different question: now that the system exists, who keeps it running, and how? Chapter 1 introduces Encore, each later chapter adds the parts it needs, and an appendix gathers them all on one page. One incident, the on-sale for a fictional artist named Vesper Hale, runs through the book. It is foreshadowed early, fought live in Chapter 12 and learned from in Chapter 13.

Each chapter closes with a **kata**: a practice brief for a different company, with its own scale and constraints, and a rubric to check your work against. As with a musician's scales, the value lies in repetition where mistakes are cheap. Every section ends with a recap and a short exercise, best done against a system you run. Each chapter's references list the field's standard works; those marked *free online* cost nothing.

The chapters build on one another, but each can be read on its own. A reader in the middle of an on-call crisis may start with Chapter 12; a reader designing a new service may start with Chapters 4 and 9. Chapters 2 and 3 are the foundation for everything else, and I would ask every reader to make time for them eventually.

## The Arc

**Foundations (Chapters 1–3):** what production is, how complex systems fail, and what automation does to the people who run it.

**Knowing the system (Chapters 4–6):** reliability as a product decision, observability, and performance, capacity and cost.
{: .flush}

**Running and changing (Chapters 7–8):** the runtime and its control plane, and shipping change safely.
{: .flush}

**Withstanding failure (Chapters 9–11):** designing for failure, data and disaster recovery, and security operations.
{: .flush}

**Responding and learning (Chapters 12–13):** incident response and learning from incidents.
{: .flush}

**The destination (Chapters 14–15):** operating AI workloads, and the organization that runs production, ending with the capstone.
{: .flush}

## Contents

1. [What Production Is — Running Software in the Cloud Era](#ch1)
2. [How Complex Systems Fail — Safety Science for Software](#ch2)
3. [Automation and Its Ironies — Toil, Runbooks, and the Human Role](#ch3)
4. [Reliability as a Product Decision — SLOs, Error Budgets, and Risk](#ch4)
5. [Observability — Seeing What the System Is Doing](#ch5)
6. [Performance, Capacity, and Cost](#ch6)
7. [The Runtime and Its Control Plane — Kubernetes, Serverless, IaC, and GitOps](#ch7)
8. [Shipping Change Safely — Continuous and Progressive Delivery](#ch8)
9. [Designing for Failure — Stability Patterns and Chaos Engineering](#ch9)
10. [Data, State, and Disaster Recovery](#ch10)
11. [Security Operations — Secrets, Patching, and the Supply Chain](#ch11)
12. [Incident Response — Command, Communication, and On-Call](#ch12)
13. [Learning from Incidents — Postmortems, Just Culture, and Drift](#ch13)
14. [Operating AI Workloads — Models, Evals, and Agents](#ch14)
15. [The Production Organization and the Capstone](#ch15)

[Appendix: Encore at a Glance](#encore-glance)

---

## Chapter 1: What Production Is — Running Software in the Cloud Era {#ch1}

> Code is finished when it ships. Production never is.

On the morning after Encore's new Notification service went live, nothing happened, and that was the first thing worth noticing. Overnight a coding agent had rebuilt the service on a new framework, with better retry semantics and 40 files that no person had typed or read in full. The contract tests passed, the boundary rules passed, the security checks passed, and the canary, judged against its service level objective (SLO), promoted the new version. By breakfast the service had delivered about 180,000 tickets to fans' phone wallets and email inboxes, and every dashboard was green.

One engineer had nonetheless spent 20 minutes on that change before it merged, reading the behavior it promised more than the code, and had found that the new retry semantics could, under the wrong timing, send a fan the same ticket twice. No automated check would have noticed, because a duplicate ticket is a perfectly healthy delivery, twice. She added a specification-level idempotency test, and the change went out. The green dashboards raise this book's question, which is older than it looks. Who runs code that nobody fully read, and what do they need from it at 3 a.m.?

People have always run code they did not write, and how to do it well without understanding all of it is the founding question of our discipline. This chapter traces how it was answered, from the machine-room operators of the 1950s to Google's first site reliability engineering (SRE) team in 2003, then sets out what users feel of production, the stack of practices we run it with, and the principles that make a system operable by strangers.

### Encore, the System We Will Run {#encore}

Encore is our companion again, as it was throughout [the Architecture book](https://oleksiyp.github.io/arch-book/#encore-our-running-example), which followed it from nine engineers to 400. For most of the week it could pass for an ordinary online shop, selling seats at concerts across Europe, in euros. Then a famous artist's tour goes on sale, nearly always at 10:00 on a Friday, and within minutes the traffic reaches 500 times its weekday level. A million people want a few thousand seats; every seat must be sold exactly once, never lost and never sold twice in a race; and the bots arrive before the fans do, because a reseller's scripts are faster and more numerous than any person. Nearly every structure in Encore exists to answer one of those demands, and most of this book's trouble lies where those demands conflict.

On such a morning the first problem is the size of the crowd, and only then the selling of seats, so Encore is built to manage the crowd first. Figure 1.1 is the map, and the part of it that matters most is short. The fan's **purchase path** begins at the **Sale Gate**, Encore's virtual waiting room, where fans meet a queue instead of a seat map and are let through at a metered rate, about 1,200 a second per event, chosen so that nothing behind the Gate runs hot. That makes the Gate an **admission controller**, a component that protects a scarce resource by deciding how much work may reach it, and its rate is the most powerful single control Encore has. Alongside it, **Bot Screening** judges, session by session, whether it faces a fan or a script. Past them, **Seat Inventory** is the one authority on whether a seat is free: it holds a fan's chosen seats for five minutes and sells each one once, whatever else is failing. **Orders & Payments** turns the hold into a sale within a 3 s checkout budget, calling an external payment service provider (PSP), with a second provider ready to take new payments if the first falters. The PSP's slowness once took the whole site down; [the Architecture book](https://oleksiyp.github.io/arch-book/#anatomy-of-a-self-inflicted-outage) told that story, and Chapter 2 reads it again.

{% include diagrams/fig-1-1.svg %}

*Figure 1.1 — Encore's system map. The purchase path runs down the middle; everything else either hangs off it or listens to it.*

Figure 1.2 follows one fan along that path, from the queue to a ticket in the phone wallet.

{% include diagrams/fig-1-2.svg %}

*Figure 1.2 — One fan's purchase in eight steps, each tagged with the service that owns it. The admission rate and the checkout budget bound the rush from opposite ends.*

Forty teams build these services and carry their own pagers, standing on a platform whose golden paths take a new service from template to production, and Figure 1.3 shows where it all runs. Within the platform group sits the **Reliability team**, ten engineers who own the tooling for service level objectives, the incident process and the readiness review held before every big on-sale. They advise, embed and rehearse; they do not run other teams' services.

{% include diagrams/fig-1-3.svg %}

*Figure 1.3 — Where Encore runs: two EU regions of Kubernetes cells and serverless edges, reconciled from one Git repository. The seat ledger commits each write to a majority of five replicas in three locations, two in each region and a witness in a third, which is why losing a region loses no sale.*

One Friday runs through this book: the on-sale for Vesper Hale, a fictional artist whose 12-date European tour will bring about 1.1 million fans to the Gate in the same minute. Chapter 12 fights it and Chapter 13 learns from it, and earlier chapters point out small, reasonable decisions that will matter that morning. Everything else in Encore, from its tenants and cells to the change freeze and the assistant in the incident channel, is introduced in the chapter where it first does something, and [the appendix](/prodsys-book/#encore-glance) keeps a glossary for the reader who wants it all on one page.

### 1.1 Production as a Sociotechnical System

#### What we mean by production {#what-we-mean-by-production}

The word *production* comes from manufacturing, where it names the floor on which real goods are made, as distinct from the laboratory. **Production** is the environment in which software serves real users with real consequences, where a mistake costs money, trust or someone's evening, and where nothing can be undone merely by closing a laptop.

The theatre teaches something the factory does not. A script is written once, but the production is made again every night by a crew that adjusts to a cold house or a missed cue, and a good stage manager keeps the show running through small failures the audience never sees. The analogy breaks at scale: a crew can see the whole stage, whereas Encore runs thousands of copies of its services for millions of people it never sees, and the gap between what is happening and what anyone can perceive is where most of this book's techniques live.

#### People and machines, jointly {#people-and-machines-jointly}

The term *sociotechnical system* comes from the Tavistock Institute in London, where Eric Trist and Ken Bamforth, studying British coal mines in 1951, found that the technically superior longwall method had made the mines worse by breaking apart the small, self-managing teams that kept the old method safe. Their conclusion, relearned in every industry since, was that the social and the technical parts of a work system cannot be optimized separately.

A **sociotechnical system**, then, is one whose behavior is produced jointly by its people and its technology, so that neither can be understood or improved without the other. Production is such a system, and its reliability is no more a property of the code than a ship's safety is a property of its hull. It is produced continuously, by people knowing what the system is doing, changing it carefully, withstanding what goes wrong, responding when it does and learning afterwards. Those five verbs organize the rest of the book.

The Notification rewrite shows what this means. As an artifact the new service was better than the old one; as part of a sociotechnical system it was briefly worse, because its operators understood less of it. The engineer's test moved a piece of human knowledge into a check that would outlast her attention, the oldest move in operations. In [the Architecture book's](https://oleksiyp.github.io/arch-book/#12-architectural-characteristics) language, Encore's 500× spike is essential complexity, whereas the gap between what a system does and what its operators perceive is usually accidental, and much of operations is the patient work of closing that gap.

**Recap.** Production is where software meets real consequences, a sociotechnical system whose reliability people and machines produce jointly. Much operational work closes the gap between what the system does and what its people can perceive.

**Exercise 1.1.** List the last five times a person, not an automated check, prevented or shortened a problem with a service you know. For each, ask whether that person's knowledge now lives in a test, an alert or a runbook, or still only in their head.

### 1.2 From Operators to SRE — A Short History of Running Software

#### The machine room {#the-machine-room}

In September 1947 someone working on the Harvard Mark II taped a moth into the machine's logbook, beside the note "First actual case of bug being found." The logbook is the more instructive object: running a computer has always meant recording what went wrong, and Chapter 12's incident timelines continue that record.

Through the 1950s and 1960s, as machines like the IBM 704 and later the System/360 spread through universities, banks and government, **computer operator** became a job with its own shifts and skills. Most installations ran as a *closed shop*: programmers handed their card decks across a counter and came back hours later for the printout. Behind the counter, operators mounted tapes, watched the console and restarted failed jobs from instructions the programmers had left, often in a binder called a run book.

The operator stood where Encore's on-call engineer stood after the rewrite, running programs they had not written and could not usefully read. What made that workable was a contract: the program declared what it needed, the run book said what to do when it stopped, and judgment covered the rest. The contract failed through stale instructions, programs written for the happy path, and improvisation at 3 a.m. while the authors slept.

#### Automating the operator {#automating-the-operator}

Much of computing's history is the operator's work being absorbed into software. In 1956 General Motors Research and North American Aviation wrote GM-NAA I/O for the IBM 704, one of the first operating systems, chiefly to cut the idle time between jobs. Spooling and time-sharing absorbed more of the role, and by the 1980s the work had passed to the **system administrator**, who tended fleets of smaller Unix machines through scripts.

Aviation went through a parallel change. Large airliners once carried a flight engineer to manage engines, fuel and electrics, until from the early 1980s new wide-body airliners, beginning with the Boeing 767 and the Airbus A310, were certified for two pilots and the engineer's panel was folded into automation. The role dissolved into the aircraft's design and the pilots' training, as computer operations dissolved into operating systems, scripts and eventually the code. The analogy breaks because an airliner is certified once and software changes daily. Every era left something automation could not absorb: judgment for the failure nobody had written down.

#### The wall, and two ways over it {#the-wall-and-two-ways-over-it}

As software moved onto the web, developers were rewarded for change and operations staff for stability, and releases were thrown over the wall between them. The IT Infrastructure Library (ITIL), published by the UK government from the late 1980s, disciplined change management but often institutionalized the wall.

Two answers emerged. In 2003 Benjamin Treynor (now Ben Treynor Sloss) joined Google to run a production team of seven engineers, and staffed it with software engineers who treated operations as a software problem: automate the repetitive work, cap the manual share of each engineer's time at half, and set the balance between change and stability by measuring it. He later put it in a line quoted ever since: "SRE is what happens when you ask a software engineer to design an operations team." The other answer came from web companies. In 2009 John Allspaw and Paul Hammond described Flickr's practice of deploying more than 10 times a day, and later that year Patrick Debois organized the first DevOpsDays in Ghent. DevOps tried to take down the wall, and Amazon's "you build it, you run it", which [the Architecture book discussed](https://oleksiyp.github.io/arch-book/#115-operability-by-design), pushed the pager to the team that wrote the code.

Encore has inherited all three answers: teams run their own services, a small Reliability team works in the SRE tradition, and the incident commander rotation borrows trained engineers, most of them senior, from everywhere. The question is still the one the closed shop faced: how to run software whose authors are not in the room. With a coding agent as author they may not be anywhere. Figure 1.4 sets the lineage on one line.

{% include diagrams/fig-1-4.svg %}

*Figure 1.4 — Who has stood between the code and its users, from the 1947 logbook to today.*

**Recap.** Operators have always run code they did not write, relying on a contract with its authors and on judgment for the unwritten cases, which no era of automation has removed. SRE and DevOps are two answers to the wall between change and stability, usually combined today.

**Exercise 1.2.** Draw your organization's closed-shop counter, where code passes from those who wrote it to those who run it. Who is on each side, what crosses it with the code, and what is lost in the crossing?

### 1.3 Reliability, Availability, and What Users Actually Feel

#### Definitions worth quoting {#definitions-worth-quoting}

The reliability engineers of the 1950s, facing military electronics that failed at alarming rates, gave us a definition that has held up well: **reliability** is the probability that a system performs its intended function, under stated conditions, for a stated period. *Intended function* means that a system can be running and still be failing; *stated conditions* means that reliability on a quiet Tuesday says nothing about reliability during an on-sale; *stated period* means a window, never an instant.

**Availability** is narrower: the fraction of time, or of requests, for which the system is able to serve. Its classical steady-state form divides the mean time between failures (MTBF) by the sum of that and the mean time to repair (MTTR). Availability rises by failing less often or by recovering faster, and for modern systems, built from many parts that fail partially and often, designing for fast recovery is usually far cheaper, which is why "expect failures" was the first tenet of James Hamilton's 2007 paper on internet-scale services. Figure 1.5 draws the arithmetic.

{% include diagrams/fig-1-5.svg %}

*Figure 1.5 — Availability as mean time between failures over the sum of that and mean time to repair, with lines of equal availability. Halving recovery time raises availability as much as doubling the time between failures.* Chapter 4 turns availability into targets.

The lesson concerns design; it does not make average recovery time a number to manage by, because incidents are few and their durations wildly skewed. Štěpán Davidovič showed by simulation at Google that even a genuine 10% improvement in incident durations is usually lost in the noise of MTTR, and the VOID, Courtney Nash's public collection of thousands of incident reports, shows the same skew. We judge recovery by drills and by what each incident teaches, as Chapters 4 and 13 do.

A third property matters most to Encore. **Correctness** is the property that the system's answers are right: a seat sold once, a ticket for every charged fan, each ticket delivered once. The dependability literature folds it into the definitions (Avižienis and colleagues' 2004 taxonomy calls availability readiness for *correct* service), but availability as we usually measure it counts responses, recording whether the system answered while users judge what it said. The duplicate ticket would have appeared nowhere in that measure, and the dashboard would still have been green as fans found two copies of one seat in their wallets.

#### Vital signs and the patient {#vital-signs-and-the-patient}

Medicine offers the right analogy. A hospital monitors pulse, temperature and blood pressure because they are cheap, continuous and correlated with health, yet a patient can have normal vital signs and be seriously unwell, and the patient's own account is evidence too. Health checks, CPU graphs and pod counts are a system's vital signs; what the fan feels in the queue and at checkout is the patient's account, and surprising outages hide in the gap. The analogy breaks in our favor, since software can report its users' experience directly, as Chapter 5 shows.

| What the system reports | What the fan feels |
|---|---|
| All Seat Inventory pods healthy | "Seat unavailable" on every seat I click, because one shard is mid-failover |
| Payment API 99.95% available | My card was charged and the page spun until it timed out |
| Notification delivery success 100% | I got my ticket twice and don't know which one is valid |
| Sale Gate p99 latency 40 ms | I have been in the queue 25 minutes and the position hasn't moved |
| Bot Screening blocked 2% of sessions | I am a real fan and I was told I am a robot |

*Figure 1.6 — Vital signs against the patient's account. Each left-hand statement can be true while the right-hand one is also true.*

Two features of user experience shape the rest of the book. Failure is usually partial, so the useful questions are "for whom?" and "how many?" And users feel their own latency, never the median, so in a purchase touching a dozen services a fan will often meet the slow tail of at least one, as [the Architecture book's tail-at-scale argument](https://oleksiyp.github.io/arch-book/#tails-not-averages) showed.

**Recap.** Reliability is the probability of doing the intended job under stated conditions over a stated period; availability is narrower, and correctness is a third property that availability as commonly measured cannot see. Design for fast recovery, but do not steer by average recovery time. Failure is partial and felt individually.

**Exercise 1.3.** For a user journey you own, write five rows of Figure 1.6. Which of the right-hand column could you detect today, and how?

### 1.4 The Modern Production Stack

#### Layers, and why we need them {#layers-and-why-we-need-them}

A touring concert production is organized in layers: riggers hang the structure, a power crew brings in electricity, the sound and lighting desks run their systems, and the stage manager calls the cues, each layer with its own specialists and each depending on the ones beneath it.

Production is organized the same way, because hierarchy is how we master a whole too complex to hold at once: each layer hides detail from the ones above. The layered hierarchy has a precedent in Google's *Site Reliability Engineering* (2016), whose **Service Reliability Hierarchy**, drawn by Mikey Dickerson, stacks monitoring, incident response, postmortems, testing and release, capacity planning, and finally development and product, since a team cannot respond to what it cannot see or learn from incidents it never handled. No standard stack exists; ours is a teaching device in that tradition.

At the bottom sits the **runtime and its control plane**: clusters, functions and managed services, declared as code and reconciled continuously. Above it, **delivery** carries change through pipelines, canaries and flags. **Telemetry** reports what the system is doing, and **SLOs** judge whether that is good enough for users. The **incident process** takes over when users are hurting, and **learning** decides what changes afterwards. Alongside runs the **platform**, packaging the lower layers into paved paths. Two concerns sit on no single layer: security operations, since attackers use our runtime, pipeline and credentials as readily as we do, and AI workloads, which run on all of them. Figure 1.7 lists its rows in the book's order, which makes it a reading map.

| Layer | The question it answers | Encore today | Chapter |
|---|---|---|---|
| Safety foundations | Why do complex systems fail? | The first outage, re-read | 2, 3 |
| SLOs and error budgets | Is it good enough for users? | Seat-map and tenant SLOs | 4 |
| Telemetry and observability | What is it doing, and why? | Traces across the purchase path | 5 |
| Capacity and cost | Will it hold, and at what price? | 1,200 fans/s, four shards, cost per ticket | 6 |
| Runtime and control plane | Where does it run, and what keeps it there? | Kubernetes cells, serverless Gate, GitOps | 7 |
| Delivery | How does change arrive safely? | Canaries, flags, the on-sale freeze | 8 |
| Resilience | What happens when parts fail? | Retry budgets, load shedding, cells | 9 |
| Data and recovery | What is lost, and how fast do we return? | A seat ledger that may lose nothing | 10 |
| Security operations | Who else is acting on the system? | Bots, leaked keys, signed artifacts | 11 |
| Incident response | What do we do while users hurt? | Incident commander rotation | 12 |
| Learning from incidents | What do we change afterwards? | Postmortems that change the system | 13 |
| AI workloads | How do we run nondeterministic components? | Support assistant, refund agent, AI gateway | 14 |
| Platform and organization | Who owns what? | Golden paths, the Reliability team | 7, 15 |

*Figure 1.7 — The production stack in the book's reading order, not bottom to top; security and AI workloads cut across the other rows.*

#### What the stack hides, and what it cannot {#what-the-stack-hides}

Layers help only while the interfaces between them behave as documented. A node drain in the runtime shows up as a latency spike in telemetry, an SLO burn, a page, an incident and, if we are diligent, a change to delivery. Here the touring analogy breaks: a tour has one stage manager calling every cue, whereas a cloud system's cues are called by hundreds of control loops, none aware of all the others. No layer sees the whole, and the incident process exists partly to assemble it, as Figure 1.8 shows.

{% include diagrams/fig-1-8.svg %}

*Figure 1.8 — One node drain, as each layer of the stack sees it. Every layer holds a piece of the event and none holds all of it, which is why an incident needs someone to assemble the whole.*

The largest outages of recent years were of this kind: a content update to CrowdStrike's Falcon sensor in July 2024, a policy change with blank fields in Google Cloud's Service Control in June 2025 and a doubled bot-management file at Cloudflare in November 2025, all three told in Chapter 8, and a race in the DNS automation of AWS's DynamoDB in October 2025, told in Chapter 3. None began with a broken machine; each began with a change to configuration or automation and crossed layers faster than anyone could follow. Modern production failure is mostly self-inflicted, and its blast radius is set by how far a change can travel before anyone sees it.

On the morning after the Notification rewrite, no layer required anyone to have read the 40 files, and none could say whether "acceptable" had been defined correctly. That took a specification of behavior, written by someone who understood what a ticket is for.

**Recap.** The production stack is a teaching hierarchy in the line of Google's Service Reliability Hierarchy, with security and AI workloads cutting across it. The great outages of 2024 and 2025 each began with a change and crossed the whole stack.

**Exercise 1.4.** Fill in Figure 1.7's "Encore today" column for your own system. Mark each row strong, adequate or missing, and pick the weakest row on your most important journey.

### 1.5 Principles for Operable Systems

#### A definition, and a stranger {#a-definition-and-a-stranger}

Operators have never been able to understand everything they run. **Operability** is the degree to which a system can be understood, controlled and repaired in production by people who did not build it, under time pressure and with partial knowledge. Every author will one day be asleep or gone, and with coding agents the author may never have been a person at all.

None of what follows is new. Hamilton's paper, drawn from running Microsoft's Windows Live services, reads as a list of obligations a service has to its operators, under three tenets: expect failures, keep things simple, automate everything. AWS wrote much of the same advice into the operational excellence principles of its Well-Architected Framework: frequent, small, reversible changes, anticipating failure, learning from every operational failure. The five principles below are this book's distillation of that tradition, and they apply equally to code written by people and by agents.

**Legible.** The system tells us what it is doing, in terms of its users' experience, without anyone reading its source. Encore's new Notification service emits a delivery record per ticket with the order and attempt number, so an escaped duplicate would show within minutes.

**Steerable.** The system offers controls that operators can turn safely and quickly while it runs: admission rates, feature flags, drains, load-shedding thresholds. The best controls degrade the product instead of dropping it, as Hamilton's "big red switch" sheds non-essential work under extreme load, so that a ticket site under strain might draw a simpler seat map and keep selling. Controls are tested and access-controlled like any change.

**Bounded.** When the system fails, the damage stays inside a known perimeter: a cell, a shard, a tenant, a slice of traffic. [The Architecture book](https://oleksiyp.github.io/arch-book/#blast-radius-is-a-design-variable) drew these boundaries; they make a bad change survivable only if changes cross them one at a time, since a configuration pushed everywhere at once has no perimeter. A bounded system is also **statically stable**, in the Amazon Builders' Library's phrase: what is running keeps serving when a control plane or dependency fails. Chapter 9 develops both ideas.

**Reversible.** Every change can be undone faster than it can do serious harm, and the irreversible ones, mostly changes to data, are identified in advance and made in reversible steps. The Notification canary was safe only because the previous version could be restored in minutes.

**Rehearsed.** Recovery paths never exercised are untested. Hamilton insisted that rollback be tested and recovery scripts exercised in production, and Google's Disaster Recovery Testing (DiRT) program made such exercises a yearly habit.

#### Ownership, which holds the principles together {#ownership-holds-them-together}

The tradition insists on a sixth principle, which belongs to the organization. Every production system needs an **owner**, a named team that answers its pages, keeps its runbooks current and decides when its risks are acceptable. The Fan Messaging team woke that morning owning code it had not written, the operator's oldest position. What made that tolerable was a service with the five properties, plus one person's 20 minutes of specification.

Figure 1.9 turns the six into questions a readiness review can put to any service before launch, each answered with evidence.

| Principle | Ask before launch | Evidence that settles it |
|---|---|---|
| Legible | Can on-call tell from telemetry whether users are served correctly? | A user-journey service level indicator |
| Steerable | Which controls turn at runtime, who may turn them, and how fast? | Each control exercised, access logged |
| Bounded | How many users can one bad change or one failed dependency reach? | Per-cell rollout stages; serving survives a control-plane outage |
| Reversible | How is each change undone, and which changes cannot be? | A timed rollback; irreversible changes listed |
| Rehearsed | When were failover, restore and rollback last exercised? | Dates and durations from the last drill |
| Owned | Who answers the page, with what runbook and what authority? | A named team in the service catalog |

*Figure 1.9 — Operability as a readiness checklist. Chapter 15 returns to the review that asks these questions.*

I have come to believe that this answers the question with which the chapter began. We cannot read everything we run, and we never could. We can insist that whatever we run, whoever or whatever wrote it, comes with what a stranger needs to operate it at 3 a.m. We can also insist that someone is accountable when that stranger is us. Operability is the contract between a system and the people who will run it, and like every contract it is worth exactly as much as its enforcement.

**Recap.** Operability is the degree to which strangers can understand, control and repair a system under pressure. Five principles distill Hamilton's 2007 advice and AWS's operational excellence principles, and ownership holds them together. Each holds only under its condition: tested controls, boundaries crossed one at a time, practiced rollbacks.

**Exercise 1.5.** Answer Figure 1.9's questions for a service you own, with evidence, and score it from one to five on each principle. For the lowest score, describe when it would hurt at 3 a.m. and the smallest change that would raise it.

### Kata: The Night Ferry

> **Your brief: "Tideway."** A ferry operator's booking platform: 14 island routes, about 9,000 bookings a day. When storms cancel crossings, rebooking traffic jumps 40× within an hour, and island residents with hospital appointments cannot afford to be stranded. It has 22 developers in four teams and a three-person infrastructure team that receives releases on Thursday evenings and holds the only pager. Half of last quarter's code came from a contractor's coding agent; the contract ended in September. Outages are reported by port staff phoning the office. The board's request: "fewer surprises, without slowing down."

**Deliverables:**

1. **Sociotechnical map** — the people, automated systems and external parties in a storm rebooking, and who knows what about each.
2. **Operations history** — where Tideway sits in Section 1.2's lineage, where its counter is, and what crosses it.
3. **User-felt reliability** — a Figure 1.6 table for storm rebooking, with at least two rows where availability looks healthy and residents are failed.
4. **Stack map** — a Figure 1.7 table rated strong, adequate or missing, with three layers chosen for investment.
5. **Operability review** — Figure 1.9 answered for the rebooking service, an owner for the contractor's code, and a 90-day plan.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Sociotechnical view | Does the map show people and judgment, or only boxes and arrows? |
| Honest lineage | Is the Thursday handover recognized for what it is, with what is lost in it? |
| User truth | Would a stranded resident recognize the right-hand column of your table? |
| Prioritization | Are the chosen layers the ones on the storm path, rather than the most fashionable? |
| Ownership | Does the contractor's code now have a named owner who can operate it without reading all of it? |
| Restraint | Does the plan fit 22 developers and three operators, and honor "without slowing down"? |

#### Where you now stand

You can now describe production as a sociotechnical system, place your organization in the history of running software, separate what a dashboard reports from what a user feels, map the production stack, and judge operability whoever wrote the code. What you lack is an account of how such systems actually fail, and Chapter 2 turns to safety science, from Three Mile Island onward, for that account.

### References

- James Hamilton — [*On Designing and Deploying Internet-Scale Services*](https://www.usenix.org/legacy/event/lisa07/tech/full_papers/hamilton/hamilton.pdf). LISA '07, USENIX, 2007 — free online.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Amazon Web Services — [*Operational Excellence Pillar: Design Principles*](https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html). AWS Well-Architected Framework — free online.
- Štěpán Davidovič — [*Incident Metrics in SRE*](https://www.oreilly.com/library/view/-/9781098103163). O'Reilly/Google, 2021 — free online.
- Courtney Nash — [*The VOID Report*](https://www.thevoid.community/report). Verica, 2021–2022 — free online.
- Algirdas Avižienis et al. — [*Basic Concepts and Taxonomy of Dependable and Secure Computing*](https://www.inf.ed.ac.uk/teaching/courses/seoc/2006_2007/resources/BasicConcepts.pdf). IEEE Transactions on Dependable and Secure Computing, 2004 — free online.
- Becky Weiss, Mike Furr — [*Static Stability Using Availability Zones*](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/). Amazon Builders' Library, 2020 — free online.
- CrowdStrike — [*External Technical Root Cause Analysis: Channel File 291*](https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf). 2024 — free online.
- Google Cloud — [*Multiple GCP Products Are Experiencing Service Issues* (incident report)](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW). 2025 — free online.
- Amazon Web Services — [*Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region*](https://aws.amazon.com/message/101925/). 2025 — free online.
- Matthew Prince — [*Cloudflare Outage on November 18, 2025*](https://blog.cloudflare.com/18-november-2025-outage/). Cloudflare blog, 2025 — free online.
- E. L. Trist, K. W. Bamforth — [*Some Social and Psychological Consequences of the Longwall Method of Coal-Getting*](https://doi.org/10.1177/001872675100400101). Human Relations, 1951.

---

## Chapter 2: How Complex Systems Fail — Safety Science for Software {#ch2}

> "Complex systems run in degraded mode." — Richard Cook

At four o'clock in the morning on 28 March 1979, the pumps feeding water to the steam generators of Unit 2 at Three Mile Island, near Harrisburg, Pennsylvania, stopped. What followed was the worst accident in the history of American commercial nuclear power, and nothing in it was exotic. A valve stuck open, and the light meant to show its state reported only the command to close it. Conscientious operators did what their training and instruments told them, and in doing so starved the core of the water it needed. By the time anyone understood, about half the core had melted.

The accident is usually told as a story about operators who made mistakes. Charles Perrow, a sociologist of organizations, told it differently. In *Normal Accidents* (1984) he argued that Three Mile Island was a property of the kind of system it was: one whose parts interacted in ways nobody had anticipated, bound so tightly that there was no time to understand those interactions before they did harm. In such systems accidents are *normal*: rare, perhaps, but inevitable. That word opened a line of thought running through Reason, Rasmussen, Cook, Dekker, Hollnagel, Woods and Leveson, and it is the foundation of this book.

This chapter asks why carefully built, well-defended systems still fail, and what that implies for running them. Each model here ends in something a team can do, and I will say which of those practices are long proven and which are still young in software. Encore gives us two events to re-read: the retry storm that followed a slow payment provider, and a failure that did not happen, the duplicate ticket one engineer caught in an agent-written change. (Chapter 1's [map of Encore](/prodsys-book/ch/1/#encore) shows where each piece sits.)

### 2.1 Normal Accidents — Coupling and Interactive Complexity

#### What happened at Three Mile Island {#what-happened-at-three-mile-island}

The chain is worth following slowly, because every link in it was reasonable. When the feedwater stopped, pressure rose; a relief valve on the pressurizer opened, and the reactor shut itself down, both as designed. Seconds later the valve was commanded to close. It did not close, and for more than two hours it vented coolant into a drain tank.

The control room's light for that valve went out, but it reported only that the signal to close had been sent; it described the command and said nothing of the valve itself. Two valves on the backup feedwater lines had been left shut after maintenance. Amid over a hundred alarms, the operators watched the pressurizer level rise. Their training said the worst thing a pressurizer could do was fill completely, so they throttled back the emergency cooling that had started automatically. The level was rising because steam forming in the reactor was pushing water up. The core was uncovering while the instrument they trusted said it was flooding.

The story lacks a villain, a single broken part, or a step at which a reasonable person knowing what the operators knew would obviously have acted otherwise. The presidential commission faulted training, procedures, control-room design and the regulator alike, and Perrow explained why a systemic answer was the right one.

#### Two dimensions of trouble {#two-dimensions-of-trouble}

Perrow described systems along two axes. In a system with **linear interactions**, parts affect each other in expected, visible sequences, like stations on an assembly line. A system has **interactive complexity** when its parts can interact in unplanned and often invisible ways, through shared components and feedback loops, so that a failure in one place appears as a symptom somewhere else. A **tightly coupled** system has little slack: processes are fast, cannot be paused and have few substitutes for failed parts. A **loosely coupled** system has buffers and alternative paths, and so tolerates a fault while people work out what is going on.

| | Linear interactions | Complex interactions |
|---|---|---|
| **Tight coupling** | Dam, power grid · a batch payment file with a bank cutoff | Nuclear plant, chemical plant · a synchronous service mesh under peak load |
| **Loose coupling** | Assembly line, post office · a nightly report job | University, research lab · an event-driven system with durable queues |

*Figure 2.1 — Perrow's interaction and coupling chart. His examples come first in each cell; the software analogues after them are ours. Normal accidents live in the top-right cell.*

The top-right cell is where the trouble lies, because each property defeats the usual remedy for the other. Interactive complexity defeats prediction, so we rely on people to understand the surprise when it arrives; tight coupling denies them the time to do it.

His most uncomfortable observation concerned safety devices. Every alarm, interlock and redundant part adds interactions. At the Enrico Fermi 1 reactor near Detroit in 1966, a zirconium plate installed as a safety feature broke loose and blocked the coolant flow, causing a partial meltdown. Software has its own safety devices that cause accidents. On 7 December 2021, AWS's us-east-1 region was impaired for hours after an automated activity to scale capacity in its internal network triggered a surge of client connections that congested the devices between networks.

#### Encore's retry storm, re-read {#encores-retry-storm-re-read}

Encore's first big outage, told in [the Architecture book](https://oleksiyp.github.io/arch-book/#anatomy-of-a-self-inflicted-outage), looks different through Perrow's eyes. The payment service provider (PSP) slowed from 200 ms to 8 s. Connection pools ran dry; health checks sharing those pools failed; healthy instances were restarted, and the autoscaler, reading the failures as a need for capacity, added instances that opened still more connections. Retries at several layers multiplied the load. Every element was a safety device, sensible alone, and their interaction through shared pools appeared on no diagram. The purchase path was also tightly coupled to the PSP: a synchronous call inside a 3 s checkout budget.

Retry budgets and a single retry layer reduced the interactions, and they are the best-proven remedy in this chapter: Google's SRE book caps retries at three per request and about 10% of a client's traffic, and Amazon's Builders' Library advises retrying at one point in the stack. A second PSP, to which new payments move when the first falters, loosened the coupling, since Perrow counted substitutable supplies as a mark of loose coupling; when both falter, a verified fan's seats are held for up to 20 minutes while payment is pending. The loosening brought interactions of its own, as Perrow would predict. A breaker can flap between providers. Idempotency keys valid at one PSP mean nothing at the other. And bots would happily collect pending holds, which is why they are capped per fan and lapse back to sale.

What I take from Perrow is the chart as a diagnostic lens: before asking who failed, ask which cell the system was in. I leave aside his pessimism, which the high-reliability school challenged with studies of aircraft carriers and air traffic control, and the chart as a classification method, since nobody can measure a system's position on his qualitative axes. In practice that means naming the couplings in every design review, and treating every health check, autoscaler and auto-remediation as a possible cause of accidents, to be tested through the game days and fault injection of Chapter 9.

**Recap.** Interactive complexity defeats prediction and tight coupling defeats understanding in the moment. Safety devices add interactions and can cause accidents. Loosening a coupling is among the most durable reliability work a team can do, provided it budgets for the interactions the loosening brings.

**Exercise 2.1.** Place five components of a system you run on Figure 2.1. For the one nearest the top-right cell, name a coupling to loosen and the failure mode the loosening would bring, and sketch a game day for one safety device whose interactions you have never tested.

### 2.2 From Human Error to System Error — Reason, Rasmussen, Cook

#### The sharp end and the blunt end {#the-sharp-end-and-the-blunt-end}

For most of the twentieth century, accident investigation ended when it found a person, and "human error" was both the cause and, through retraining or discipline, the cure. James Reason, a psychologist at the University of Manchester, did more than anyone to take this account apart. *Human Error* (1990) classified how competent people err, through **slips** and **lapses** in executing a sound plan and **mistakes** in the plan itself.

Its most consequential chapter turned outward. Reason distinguished **active failures**, unsafe acts whose effects are felt almost at once, from what he then called latent errors and later **latent conditions**: weaknesses created far away by designers, managers and budget holders, which lie dormant until some local circumstance wakes them. Woods, Cook and their colleagues gave the picture its two ends. The **sharp end** is where practitioners touch the hazard: the control room, the on-call laptop. The **blunt end** is where the conditions of their work are set: budgets, schedules, tooling and policy. Operators are less the instigators of accidents than their inheritors.

The model's famous picture developed gradually and settled in *Managing the Risks of Organizational Accidents* (1997): each defense is a slice of cheese with moving holes, and an accident happens when, briefly, they line up. It is a teaching image, since complex systems do not fail in neat lines through stationary slices, but it made the defenses and the organization behind them the object of study. Figure 2.2 draws it for Encore's retry storm.

{% include diagrams/fig-2-2.svg %}

*Figure 2.2 — Reason's Swiss cheese, with the retry storm's defenses as the slices. Each hole was a latent condition set far from the sharp end; notice that every slice was a safety device, and that no single hole was enough.*

#### Rasmussen's boundaries {#rasmussens-boundaries}

Jens Rasmussen, the Danish engineer whose work Reason built on, went further in "Risk Management in a Dynamic Society" (1997). He pictured an organization's work as a point moving within a space bounded by economic failure, unacceptable workload, and the limit of acceptable performance, beyond which accidents happen. Management pushes the point toward efficiency; people, sensibly, push it toward least effort. Both gradients point toward the safety boundary, and nothing in daily work shows where that boundary is. Figure 2.3 draws a point drifting through the space.

{% include diagrams/fig-2-3.svg %}

*Figure 2.3 — Rasmussen's migration toward the boundary of acceptable performance (after Rasmussen, 1997). Two sensible gradients push the same way, and the drift looks like noise until it arrives.*

This is the model to keep in mind for the rest of the book: safety is less a state a system reaches than a position it must keep holding against pressure.

#### Eighteen short theses {#eighteen-short-theses}

In 1998 Richard Cook, an anesthesiologist and safety researcher at the University of Chicago, wrote "How Complex Systems Fail", a few pages of numbered theses that engineers have passed around more than any other text in this chapter. Complex systems are heavily defended, always contain flaws, and so run degraded. Catastrophe needs several failures together, each insufficient alone, so naming any one as *the* root cause satisfies our need for an explanation, and often for blame, but misdescribes the mechanism. Safety, in Cook's account, is something practitioners *do*, minute by minute.

The movement these three began is often called the New View: **human error** is an attribution made after the fact, not a cause discovered in it. The useful question is why an action made sense at the time; Woods and his co-authors call the answer the second story.

Honesty requires a qualification. The example postmortem in Google's SRE book has sections for root causes and trigger, and Amazon's Correction of Error documents still walk through the 5 Whys. Most teams that use the phrase list several factors; the safety-science objection is to stopping at one, above all at a person. Dropping "root cause" from the vocabulary altogether remains a minority position, held mainly by the learning-from-incidents community.

#### From theory to the review room {#from-theory-to-the-review-room}

Read this way, the retry storm has no culprit. The engineers who configured retries at each layer followed recommended practice; nobody owned the sum. The latent conditions were the shared pools, health checks that measured the wrong thing, and an autoscaler policy written for a different overload.

Software learned such reviews partly from John Allspaw's 2012 Etsy post "Blameless PostMortems and a Just Culture", whose title joins blamelessness to a just culture, the half that keeps accountability. **Just culture**, a term Reason introduced and Dekker developed, distinguishes honest error and at-risk shortcuts, which call for learning and redesign, from reckless disregard, which still calls for accountability. Two habits follow. Tag every contributing factor as sharp end or blunt end, because a review whose findings all sit at the sharp end has stopped early. And give every blunt-end finding an owner with authority to change it.

**Recap.** Operators inherit failures planted far from the sharp end, sensible pressures push work toward a boundary nobody can see, and failure needs several contributors. The lesson is never to stop at one cause, and a just culture keeps accountability while the review looks for conditions.

**Exercise 2.2.** Take your last incident review. Mark each contributing factor as sharp end or blunt end. If the blunt-end list is shorter, write the second story for the most prominent human action. Then check that each blunt-end finding has an owner who can actually change it.

### 2.3 Drift and the Normalization of Deviance

#### How margins erode {#how-margins-erode}

Sidney Dekker's *Drift into Failure* (2011) describes what Rasmussen's force looks like from inside an organization. **Drift** is the slow movement of a system toward failure through many small decisions, each locally reasonable and judged acceptable in its day, so that no single step can afterwards be named as the moment things went wrong. Drift is not negligence. It is what success looks like while it spends its margins, since every time a thinner margin holds, it becomes evidence that the margin was never needed.

The sociologist Diane Vaughan named the mechanism the **normalization of deviance**: a departure from a standard, repeated without consequence, comes to be accepted as the standard itself. Her study of the Challenger launch decision is the home touchstone of Chapter 13, and we leave it there.

#### The pressure that does not show on a dashboard {#the-pressure-that-does-not-show}

A touring production offers a fair analogy. The load-in schedule allows four hours to rig, with time for a fault. By the 30th night the rig goes up in three hours, so the production manager books an interview in the spare hour and the venue opens the doors earlier, so the slack is spent one good decision at a time. The analogy breaks at one point: a touring crew sees its own clock. In software the margin being spent is usually invisible: headroom on a shard, slack in a retry budget, the distance between a freeze rule and what people actually do.

Encore's on-sale change freeze, of a kind many operators keep around peak events, forbids non-emergency changes to the purchase path from two hours before an on-sale until it ends. In practice, exceptions are granted in chat by whichever senior engineer is around, usually for good reasons, and never recorded. Platform automation considered low-risk is excluded, much as change management pre-approves "standard changes"; that made sense when the automation did little. Services beside the purchase path were never covered.

The Reliability team, the platform group's ten site reliability engineers, has begun counting exception requests: 3 in the first quarter of last year, 14 in the most recent quarter, none followed by an incident, which is what makes the trend worth attention. The count is Encore's own practice, not an industry measure, and a rising number could equally mean the rule no longer fits the work. Whether a freeze earns its keep at all is a question for Chapter 8.

What can be done about drift is modest but real. Make margins visible, so that spending them is a decision: headroom, error budgets and a register of exceptions with named approvers in place of a chat thread, as GitLab's production change lock requires. Treat a quiet period as weak evidence, and distrust aggregate incident metrics: the VOID's analyses of public incident reports found durations so skewed that an average such as mean time to resolve (MTTR) says little. And bring outsiders into reviews, since insiders are the last to see a practice change. Google's production readiness review, where SREs from outside the developing team examine a service before taking it on, is the established software form; Encore's Wednesday readiness review (Chapter 6) has the same shape.

**Recap.** Drift spends safety margins through decisions that are each reasonable, and success reinforces it. The defenses are visible margins, a register of exceptions, suspicion of quiet periods and averages, and independent reviewers.

**Exercise 2.3.** Compare one production rule your team holds (a freeze, a review requirement) with the last three months of practice. List the exceptions, who granted them and why, and decide whether the rule or the practice should change.

### 2.4 Safety-I, Safety-II, and Resilience Engineering

#### Studying what goes right {#studying-what-goes-right}

Everything so far has studied failure, a strange way, Erik Hollnagel argued, to understand a system that almost always works. In *Safety-I and Safety-II* (2014) he named the traditional view **Safety-I**: safety as the condition in which as few things as possible go wrong, achieved by removing the causes of failure. Beside it he set **Safety-II**: safety as the ability to succeed under varying conditions, achieved by understanding how everyday work succeeds and supporting it.

| | Safety-I | Safety-II |
|---|---|---|
| Definition | As few things as possible go wrong | As many things as possible go right |
| What is studied | Failures, incidents, causes | Everyday work, adaptations, near misses |
| Human variability | A hazard, to be constrained | A resource, the reason things work |
| Response | Find the cause, add a barrier | Understand the adaptation, support it |
| Encore example | The retry-storm postmortem | The duplicate-ticket catch |

*Figure 2.4 — Two views of safety. Safety-II complements Safety-I; a team needs both the barrier and the understanding of why work usually succeeds.*

Critics, Leveson among them, note that few practitioners ever held the caricature of Safety-I; take the reframing and leave the polemic. Its core is that **performance variability**, people adjusting what they do to the conditions they meet, is the source of both success and failure. Hollnagel locates resilience in the gap between **work as imagined**, the work in runbooks, and **work as done**. Section 2.3 found drift in the same gap, and both readings are right: the gap holds the adaptations that save us and the shortcuts that spend our margins, and the practical task is to tell them apart, case by case.

#### The catch that did not make the news {#the-catch-that-did-not-make-the-news}

Consider the agent-written rewrite of Encore's Notification service, told at the end of [the Architecture book](https://oleksiyp.github.io/arch-book/#the-inversion-the-preface-promised). As imagined, contracts, boundary rules and security checks pass, and the service level objective (SLO) canary promotes; all of it passed. As done, one engineer gave the new retry semantics 20 minutes more than the pipeline thought they needed, saw that a retry after a partial failure could send a fan the same ticket twice, and wrote a spec-level idempotency test before merging.

A Safety-I organization keeps no record of this. Safety-II asks what made it possible: time, because the change was not squeezed into a crowded release; context, from having worked on ticket delivery; authority to slow a green pipeline; and reason for suspicion, because an agent had written all 40 files. A reorganization that removed any of the four would remove the catch unnoticed. That is reasoning rather than measured evidence, and Chapter 8 turns it into Encore's review policy.

#### Making catches reportable {#making-catches-reportable}

Studying what goes right needs a supply of catches, and catches are not reported by default. Aviation solved this long ago. NASA's Aviation Safety Reporting System, running since 1976, takes confidential near-miss reports from pilots, controllers and mechanics, strips identities, and gives reporters a measure of protection from penalty. It works because it is non-punitive and because someone acts on the reports. In software, near misses reach a review only if someone volunteers them; fewer than one in a hundred public incident reports collected by the VOID concern one.

The cheapest start is a ten-minute write-up under the same blameless rules as an incident review. Encore's Reliability team adopted this one after the Notification catch:

```text
NEAR MISS: <what almost happened, in one line>
Noticed by / cue:      who noticed, and what they saw that others did not
What made it possible: time, context, authority, reason for suspicion
What would erode it:   deadline, reorg or tool change that removes the catch
Guard added:           test, check or limit, with an owner and a date
Read where:            the review or channel where the next person will see it
Use:                   learning only; never cited in performance reviews
```

The practice is young in software. The learning-from-incidents movement, carried by the VOID, the Howie guide from Jeli (now PagerDuty) and the second edition of Google's SRE book (2026), is growing fast, yet reviews of Safety-II tools in healthcare, where they have been tried longest, find little measured evidence of effect. Confidential reporting is proven in aviation and costs little, which is reason enough to start.

#### Resilience as a capacity {#resilience-as-a-capacity}

Resilience engineering gathered as a field around a 2004 symposium in Söderköping, Sweden, and the book *Resilience Engineering: Concepts and Precepts* (2006). **Resilience** is a system's capacity to adjust its functioning before, during and after disturbances, so that it sustains operations under expected and unexpected conditions alike. David Woods adds **graceful extensibility**, the ability to stretch past the designed envelope; systems lacking it are brittle.

These ideas reached software in the early 2010s, through Allspaw's work at Etsy and Cook's 2012 Velocity talk, and were set out most fully for software in the STELLA report (2017) of the SNAFUcatchers workshop. It draws a line through the system: below it sit code, infrastructure and tooling; above it, people, each holding a partial model of what lies below, which they see only through tools. Incidents are the moments those models prove wrong. Figure 2.5 draws Encore through that line.

{% include diagrams/fig-2-5.svg %}

*Figure 2.5 — Above and below the line of representation, after the STELLA report (2017). Every person sees and acts on the running system through representations, and holds a partial model of what lies beneath them.*

**Recap.** Safety-I removes the causes of what goes wrong; Safety-II supports the adaptations that make things go right, and the gap between work as imagined and work as done holds both adaptation and drift. Near-miss reporting is proven where it is confidential and acted on; Safety-II programs in software are young.

**Exercise 2.4.** Find one occasion last quarter when someone prevented a problem no process would have caught. Write it up with the near-miss template, and decide where the next person will read it.

### 2.5 Systems Thinking and Control — STAMP for Software

#### Safety as a control problem {#safety-as-a-control-problem}

The models so far explain failure well and prescribe engineering poorly. Nancy Leveson of MIT built one that does both. Her **STAMP** (System-Theoretic Accident Model and Processes), set out in a 2004 paper and developed in *Engineering a Safer World* (2011), treats safety as an emergent property of the whole, distinct from the reliability of its parts: many software accidents happen with every component doing exactly what it was built to do.

The model has three ideas. **Safety constraints** are conditions that must always hold, such as "no seat is sold twice". A hierarchical **control structure** of controllers (people, organizations, software) issues control actions downward and receives feedback upward. And each controller acts on a **process model**, its belief about the state of what it controls. At Three Mile Island the light that reported a command instead of a position corrupted the operators' process model, and every subsequent control action was rational and wrong.

Leveson's hazard analysis method, **STPA** (System-Theoretic Process Analysis), asks of each controller how its control actions could be unsafe, in four ways: a needed action is not provided; an action is provided that causes a hazard; an action comes too early, too late or out of order; or an action is stopped too soon or applied too long. Her accident analysis method, CAST (Causal Analysis based on STAMP), applies the same structure after the fact, and Chapter 13 puts it to work.

#### A method arriving in software {#a-method-arriving-in-software}

STPA is long proven in aerospace and automotive work, and in software operations it is arriving now. Google's SRE organization has been applying STAMP to its own systems, as Tim Falzone and Ben Treynor Sloss described in *;login:* in December 2024; the second edition of the SRE book (O'Reilly, 2026) has a chapter on STPA and CAST, and Google engineers presented a CAST analysis of a Google Maps incident at SREcon in 2026. It is a serious precedent and, in Google's own words, still something it is "exploring", with no outcome data published. Full STPA is labor-intensive, so scope it to one critical path.

Software suits the method where its controllers are automated, since an autoscaler's process model can be read in code; human and organizational controllers are no more explicit here than elsewhere, and are often where the analysis pays off. Here is part of Encore's control structure around an on-sale:

| Controller | Controls | Process model (what it believes) | Feedback it receives |
|---|---|---|---|
| On-Sale team | Gate admission rate | Seat Inventory's safe throughput, from load tests | Load-test reports, on-sale dashboards |
| Sale Gate | Fans admitted per second | A configured rate, about 1,200 fans/s per event | Queue depth, its own error rate |
| Bot Screening | Which sessions are blocked | What bot traffic looks like, from past patterns | Block rates, appeals |
| Kubernetes autoscaler | Pod counts per service | CPU and request load per pod | Metrics, a few seconds late |
| Platform node-upgrade reconciler | Node versions in each cluster | Node health and disruption budgets | Node and pod readiness |
| Reliability team | Readiness review, freeze policy | The on-sale calendar, past incidents | Reviews, postmortems, chat |

*Figure 2.6 — Part of Encore's control structure around an on-sale. Each controller acts rationally on its own process model; hazards arise where a model is stale, incomplete or blind to another controller's actions.*

Read column by column, the table raises questions no component review would ask. Where do two controllers act on the same thing without knowing of each other? Which process models come from tests, and how closely do those tests resemble an on-sale? Which controllers know an on-sale is happening, and which have no way to find out?

The worksheet comes next. Applied after the fact to the retry storm's autoscaler, STPA yields a page like this, and the Reliability team now keeps one for each automated controller on the purchase path:

```yaml
controller: orders-payments autoscaler
constraint: "Checkout never opens more PSP connections than the PSP can serve"
process_model: "Load is CPU and requests per pod; more pods mean more capacity"
feedback_gap: "Sees its own pods, never the PSP's latency"
unsafe_control_actions:
  not_provided: "No scale-up while fans genuinely saturate the pods"
  causes_hazard: "Scale-up while the PSP is slow: each pod opens a fresh pool"
  wrong_timing: "Scale-up on metrics seconds stale, mid-restart"
  too_long: "Scale-up held for the whole slowdown, never backing off"
```

The second unsafe action is the outage itself, and the feedback gap explains why the autoscaler could not have seen it coming.

#### Mastering complexity with structure {#mastering-complexity-with-structure}

STAMP returns us to the oldest tools for mastering complexity, decomposition and hierarchy, and to the book's through-line. Reliability is the product of a control structure in which people and machines keep each other's process models accurate, and it decays whenever a controller acts on a belief that no longer matches the system. The chapters that follow are ways to keep those beliefs current: SLOs and observability as feedback, delivery as safer control actions, incident response as control under pressure, and learning from incidents as repair of the process models themselves.

**Recap.** STAMP treats safety as enforced by controllers, each acting on a process model that may be stale or blind to the others. STPA is proven in aerospace and young in software operations; a control-structure table and a worksheet per automated controller on one critical path are a modest, useful start.

**Exercise 2.5.** Draw a control-structure table like Figure 2.6 for one critical path in your system, including at least one automated controller and one team. Write one unsafe control action per controller from each of STPA's four categories, and circle the one you would least like to meet in production.

### Kata: The Twice-Monthly Run

> **Your brief: "Payday."** A payroll SaaS for 3,000 employers in four EU countries. Twice a month it computes about 600,000 payslips and sends payment files to 11 partner banks, each with a hard cutoff around 16:00 local time. Its 24 engineers run a modular monolith, a calculation engine that calls a third-party tax-rules service synchronously, and a file-generation pipeline. Last year they added auto-remediation that restarts stuck calculation workers. Two months ago a configuration change nearly sent a bank a duplicate file; an operations analyst noticed the totals were twice the usual size and stopped it. The pre-payday freeze, once 48 hours, is now "no risky changes on payday", and nobody can say who decides what is risky.

**Deliverables:**

1. **Coupling and complexity map** — Payday's main components on Figure 2.1, and two couplings to loosen before the next run, with their costs and the new failure modes each brings.
2. **Latent-condition inventory** — at least six latent conditions that could combine with an ordinary slip on payday, tagged sharp or blunt end, with an owner for each blunt-end one.
3. **The near miss as Safety-II** — the analyst's catch written up with the template from Section 2.4, and where such reports will be filed and read.
4. **Drift register** — the freeze as written against the freeze as practiced, a register of exceptions with named approvers, and three indicators of further drift.
5. **Control structure** — the controllers around file generation, an STPA worksheet for the auto-remediation, and one game day testing how it interacts with the tax-rules dependency.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Systemic framing | Does any deliverable stop at a person, or does each reach the conditions behind the action? |
| Coupling realism | Do the loosenings respect the bank cutoffs, with arithmetic on the time they buy? |
| Safety devices | Is the auto-remediation analyzed and tested as a possible source of accidents? |
| Learning from success | Would the near-miss write-up help the next analyst notice, and is reporting safe? |
| Drift visibility | Could an outsider read the drift register and see the margin being spent? |
| Process models | Is there at least one controller whose model of the world is plainly stale or incomplete? |

#### Where you now stand

You can now read a system as safety science reads it and act on the reading: test how safety devices interact, run reviews that reach the blunt end, make spent margins visible, give near misses a safe place, and draw the control structure of a critical path. The first place these ideas apply is automation, because every script, reconciler and assistant we add is both a safety device and a new controller with a process model of its own. Chapter 3 takes up that paradox, beginning with Lisanne Bainbridge's ironies.

### References

- Charles Perrow — [*Normal Accidents: Living with High-Risk Technologies*, updated ed.](https://press.princeton.edu/books/paperback/9780691004129/normal-accidents). Princeton University Press, 1999.
- Richard I. Cook — [*How Complex Systems Fail*](https://how.complexsystems.fail/). Cognitive Technologies Laboratory, University of Chicago, 1998 — free online.
- Nancy G. Leveson — [*Engineering a Safer World: Systems Thinking Applied to Safety*](https://doi.org/10.7551/mitpress/8179.001.0001). MIT Press, 2011 — free online.
- Nancy G. Leveson, John P. Thomas — [*STPA Handbook*](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf). MIT, 2018 — free online.
- Tim Falzone, Ben Treynor Sloss — [*The Evolution of SRE at Google*](https://www.usenix.org/publications/loginonline/evolution-sre-google). ;login:, USENIX, 2024 — free online.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- John Allspaw — [*Blameless PostMortems and a Just Culture*](https://www.etsy.com/codeascraft/blameless-postmortems). Etsy Code as Craft, 2012 — free online.
- Sidney Dekker — [*Drift into Failure*](https://www.routledge.com/Drift-into-Failure-From-Hunting-Broken-Components-to-Understanding-Complex/Dekker/p/book/9781409422211). Ashgate, 2011.
- Erik Hollnagel — [*Safety-I and Safety-II: The Past and Future of Safety Management*](https://www.routledge.com/Safety-I-and-Safety-II-The-Past-and-Future-of-Safety-Management/Hollnagel/p/book/9781472423085). Ashgate, 2014.
- James Reason — [*Managing the Risks of Organizational Accidents*](https://www.routledge.com/Managing-the-Risks-of-Organizational-Accidents/Reason/p/book/9781840141054). Ashgate, 1997.
- Jens Rasmussen — [*Risk Management in a Dynamic Society: A Modelling Problem*](https://doi.org/10.1016/S0925-7535%2897%2900052-0). Safety Science, 1997.
- David D. Woods (ed.) — [*STELLA: Report from the SNAFUcatchers Workshop on Coping with Complexity*](https://snafucatchers.github.io/). The Ohio State University, 2017 — free online.
- Amazon Web Services — [*Summary of the AWS Service Event in the Northern Virginia (US-EAST-1) Region*](https://aws.amazon.com/message/12721/). AWS, 2021 — free online.
- NASA — [*Aviation Safety Reporting System*](https://asrs.arc.nasa.gov/). NASA Ames Research Center — free online.
- The VOID — [*The Verica Open Incident Database*](https://www.thevoid.community/) — free online.

---

## Chapter 3: Automation and Its Ironies — Toil, Runbooks, and the Human Role {#ch3}

> Every machine that takes a task away from us leaves a harder one behind.

Every operations team keeps a list of chores it would rather a machine did, and it is a sound instinct: repetitive work done by hand at 3 a.m. is slow, error-prone and quietly corrosive. Yet the history of automation in every field that has taken it seriously, from chemical plants to flight decks, tells a more complicated story than "automate and be free." The question of this chapter is what automation actually does to the work it touches, and what it leaves for the people who remain.

In 1983 the British psychologist Lisanne Bainbridge published a short paper in *Automatica*, "Ironies of Automation," whose argument fits in a sentence. When we automate a process we do not remove the human from it; we change the human's job, usually into a harder one, and in ways that erode the very skills the new job demands. She was writing about control rooms and aircraft; four decades later the paper reads as if written about a platform team with an on-call rotation.

Encore has automated a great deal. Its on-sale preparations run from a button, its platform upgrades Kubernetes nodes untouched, and its seat ledger fails over so reliably that hardly anyone remembers how to do it by hand. This chapter follows that automation through its ironies to how much a machine should do alone, and ends with the newest machine Encore has added, an agent that investigates and acts. (Chapter 1's [map of Encore](/prodsys-book/ch/1/#encore) shows where each piece sits.)

### 3.1 Toil and the Case for Automation

#### What toil is {#what-toil-is}

Google's site reliability engineering (SRE) book (2016) gave the field its working definition. **Toil** is work tied to running a production service that is manual, repetitive, automatable, tactical rather than strategic, devoid of enduring value, and that grows linearly as the service grows. Each adjective does work: a task done once is not toil, however tedious, and a task that needs fresh judgment each time is not toil, however frequent.

The last property matters most: a team whose work is mostly toil can grow only by hiring as fast as the business grows. Google's SRE organization set itself the goal of keeping toil below 50% of each engineer's time, so that half of every week went to the work that removes toil. It stated this as a goal, and its own quarterly surveys found the average nearer a third. The SRE book also allows that toil is fine in small doses, and Section 3.3 will show what removing the last of it can cost.

#### Encore's toil, measured {#encores-toil-measured}

The Reliability team, the ten site reliability engineers in Encore's platform group, asked on-call engineers to tag their interrupts for a quarter, each tag tied to a page or ticket. Across stream-aligned teams, roughly 30% of the on-call week met all six properties of toil. The On-Sale team, in the spring touring season, spent closer to 45%, most of it on one chore: preparing the platform before each scheduled on-sale.

The touring world Encore serves knows the problem. A touring production rigs the same stage in a new venue every few nights, and pre-wires what it can into road cases, so that load-in becomes assembly. The analogy breaks, usefully, at the venue whose roof cannot take the standard rig, because pre-wired cases help only where the venue matches what they were wired for.

#### The case, and its fine print {#the-case-and-its-fine-print}

The SRE book's chapter on the evolution of automation makes the positive case: automation is consistent where people vary, fast where they are slow, and it turns knowledge held in a few heads into a platform. Consistency matters most, because most operational mistakes come from variation. The same chapter recounts Diskerase, a decommissioning workflow that was handed an empty list of machines, read it as "everything," and began wiping disks across a fleet with all the speed and consistency automation promises. Google's remedies are the ones every consequential automation needs: treat an empty or implausibly large target set as an error, limit how much may change per unit of time, and make every step safe to repeat.

I find it useful to see automation as abstraction applied to work, and like every abstraction it leaks under unusual conditions, when the hidden steps matter again and nobody has looked at them in a year. Toil is the accidental complexity of operations, performed by hand; automation removes the manual work and leaves the complexity in place, where nobody sees it.

**Recap.** Toil is manual, repetitive, automatable work without enduring value that grows with the service, and its linear growth is the reason to fight it. Automation brings consistency first and speed second, repeats mistakes as faithfully as successes, and needs limits on what it may touch and how fast.

**Exercise 3.1.** For one on-call week, tag every interrupt against the six properties of toil, tied to its page or ticket. Which chore takes the largest share, and how does it scale with your customers, services or tenants?

### 3.2 From Runbook to Script to Self-Service

#### The prompt book {#the-prompt-book}

A **runbook** is a written procedure for an operational task, precise enough that someone who did not write it can follow it under pressure. In the theatre the stage manager keeps the *prompt book*, the script marked with every cue, and during the performance calls each one ("standby lighting 42 … lighting 42, go") for the crew to execute. The prompt book is a very good runbook: rehearsed, authoritative, and called by a human with judgment. Most runbooks lack the first quality, and drift as the system changes under them.

Encore's on-sale pre-warm began as a wiki page of 31 steps. Raise provisioned concurrency on the admission edge of the Sale Gate, the virtual waiting room in which fans queue for an on-sale. Confirm the leaders of the event's four Seat Inventory shards, the partitions of the ledger that sells each seat exactly once. Warm the seat-map cache, set the admission rate, load the bot rules, announce the freeze. It took about 70 minutes, which across some 160 on-sales a year was nearly 190 hours of skilled attention, and that was the smaller cost: once the concurrency step was skipped, and the first 90 seconds of that on-sale ran on cold starts.

#### Script, then service {#script-then-service}

An engineer then turned the page into `prewarm.py`, which took an `event_id` and ran the steps in order, cutting 70 minutes to 12 and ending skipped steps. It needed broad production credentials, so only a handful of people could run it, and when a step failed it left the platform half-prepared. And it encoded the steps without the judgment around them: beside the admission-rate step the wiki had said "check with the On-Sale lead if the venue is new"; the script set the rate and moved on.

Each step of the wiki page had contained a moment of human attention, a person glancing at the result before moving on, and code removes those moments unless we deliberately put them back as checks. A runbook is a script that has not yet been trusted to run alone, and the passage between the two is where that trust is earned. There is a gentler crossing than the one Encore took. Dan Slimmon's **do-nothing script** (2019) automates nothing at first: it prints each step, waits for the person to do it and confirm, and moves on. The procedure gains a structure in code, and each step can be automated once someone has written the check that replaces the glance.

The third generation is a self-service workflow in Encore's platform portal, which the teams call **curtain-up**. At 07:30 on the day of a large on-sale, the On-Sale team's on-call engineer reviews the plan it proposes and presses go. Every step is idempotent, so a failed run resumes where it stopped, and each states its precondition and checks its result: the cache step reports its hit ratio, and the concurrency step confirms instances are provisioned, not merely requested. It finishes before the 08:00 freeze and posts its report to the on-sale channel. The On-Sale team owns what the steps do; the platform group owns the engine and its credentials, now the thing in the workflow most worth protecting.

| | Wiki page | `prewarm.py` | Curtain-up |
|---|---|---|---|
| Who can run it | anyone who can read | a few engineers with admin credentials | the on-call engineer, through the portal |
| Time per on-sale | 70–120 min | about 12 min | about 15 min unattended, 5 min of review |
| Where judgment lives | in notes beside each step | nowhere | in explicit preconditions and checks |
| Failure halfway | the person notices, usually | half-prepared platform; read the code | resumes from the failed step |
| What it teaches | every step, every time | nothing, unless you read it | the plan and report, if anyone reads them |

*Figure 3.1 — Three generations of Encore's on-sale pre-warm. Each removes toil, and each changes who knows what the steps are.*

The last row matters for Section 3.3: the wiki page was a tutor as well as a procedure, and curtain-up teaches only as much as its report is read. A simple procedure can sometimes skip a rung, but in general each rung needs the one below it: automating a procedure nobody has written down encodes one person's habits. Figure 3.2 puts the generations' yearly cost side by side.

{% include diagrams/fig-3-2.svg %}

*Figure 3.2 — Engineer-hours a year spent on the pre-warm, by generation, against the number of on-sales. Each rung flattens the line, and none reaches zero, because someone still has to read the plan.*

**Recap.** A runbook carries judgment in its margins, which code loses unless we rebuild it as explicit checks, and a do-nothing script lets that happen one step at a time. Each rung of Encore's pre-warm gained speed and changed who understood the procedure, a cost the time savings do not show.

**Exercise 3.2.** Pick one procedure your team runs by hand. Name its rung on the ladder, and for each step list the moment of human attention it contains. Which of those moments would a script silently remove?

### 3.3 The Ironies — Deskilling, Surprise, and the Hand-Back

#### Bainbridge's argument {#bainbridges-argument}

Bainbridge wrote when engineers hoped to design the unreliable human operator out, and her point was about what was left behind. Automation moves error upstream, to a designer who decided months earlier what the machine would do in every case they could foresee. The operator is left whatever the designer could not automate, an arbitrary collection that tends to hold the hardest and least understood tasks in the system. Among them is watching the automation, though vigilance research since the 1940s had shown that attention to a display on which little happens decays within about half an hour. And when the automation fails, the operator must take over by hand and diagnose what went wrong, skills that decay without use. There is a further catch: to monitor the automation well, the operator must know what it ought to be doing, knowledge built by doing the very work the automation took away. Her conclusion, paraphrased, was that the most successful automated systems, those needing intervention least often, may need the greatest investment in operator training.

#### Surprise and the hand-back {#surprise-and-the-hand-back}

Nadine Sarter and David Woods named the experience of automation behaving unexpectedly **automation surprises** (*Behind Human Error*, 2010), and Earl Wiener reported the three questions glass-cockpit pilots of the 1980s kept asking: what is it doing, why did it do that, and what will it do next? Aviation's most studied hand-back is Air France 447, lost over the Atlantic on 1 June 2009 with all 228 aboard. Its airspeed probes iced, the autopilot disconnected, and the crew had to fly by hand at cruise altitude, which airline pilots rarely do. The investigators' report (2012) has Bainbridge's shape: control came back in exactly the conditions the automation could not handle, to people whose practice at that task was thin.

#### The automation that raced itself {#the-automation-that-raced-itself}

Our own field supplied a textbook case in October 2025, in Amazon's own words. Late on 19 October, Amazon DynamoDB in us-east-1 began failing because its regional endpoint resolved to nothing. DynamoDB manages its DNS with a Planner that produces plans and several redundant Enactors that apply them. One Enactor was badly delayed; meanwhile another applied a newer plan and cleaned up old ones. The delayed Enactor, its freshness check long stale, wrote its old plan over the new one, and the cleanup then deleted that plan, which was by now the live one. The record was left empty, in a state that blocked further updates, so the automation could not repair its own damage, and operators fixed it by hand some two and a half hours in. Downstream, EC2's recovery needed manual work that, by AWS's account, had no established procedure. Engineers also had to switch off a load balancer's automatic failover, which was removing healthy capacity.

Each of Bainbridge's ironies is there, from a race no operator could have caused to a recovery that called on unpracticed skills, and AWS's fixes read like her prescriptions. It disabled the DNS automation worldwide until the race was fixed, added a velocity control limiting how much capacity health-check failover may remove, and began building tests that exercise the recovery workflow itself.

#### The failover nobody has done {#the-failover-nobody-has-done}

Seat Inventory elects a new shard leader automatically, with fencing so a deposed leader cannot keep writing, and has handled about 60 failovers in 19 months with no human involved. When it cannot confirm that the old leader's term has expired, it stops, preferring no leader to two, and a person must confirm the fence, advance the term, promote a replica and verify the ledger's sequence. Last spring, 4 of the 34 engineers on the Inventory and On-Sale rotations had ever done this in production, the most recent 19 months earlier; game days had exercised only the automatic path.

Because the automation is good, the hand-back is rare and the skill decays, and the next hand-back will come in exactly the situation the automation found too ambiguous to resolve. A failover we never practice is one we will perform for the first time during an on-sale. Encore's response has been modest and, I think, correct. The Inventory team now runs a manual failover in staging monthly, rotating the operator, and quarterly in production on a shard serving no live on-sale, with an abort criterion agreed beforehand. The cadence is Encore's own; studies find procedural skill fading over months. The first drill found two stale commands in the procedure. Figure 3.3 sketches the shape of the problem.

{% include diagrams/fig-3-3.svg %}

*Figure 3.3 — Readiness for the manual failover, sketched (the curve is illustrative; the counts are Encore's). Sixty automatic failovers did nothing to keep the manual path alive.*

The node-upgrade reconciler of Chapter 7, which replaced a quarterly weekend of manual upgrades, drains each node within the workloads' disruption budgets and has caused almost no pages in a year. A disruption budget limits how many pods may be down and is silent about timing, which is why managed upgraders offer maintenance windows and exclusions for peak weeks. Encore's home-grown reconciler has a hold annotation and no calendar. It knows nothing about the on-sale calendar, and so far that has not mattered.

**Recap.** Automation moves error to the designer, leaves operators the hardest tasks, asks them to watch for rare events, and erodes the skills they need when control comes back. AWS's 2025 outage shows all of it, and its remedies were an off switch, a rate limit and a drilled recovery.

**Exercise 3.3.** For the three most important automated recovery actions in a system you run, find the manual procedure, count who has performed it in the last year, and check that the automation can be switched off. Schedule a drill for the lowest count.

### 3.4 Levels of Automation and Calibrated Trust

#### How much should the machine do alone? {#how-much-should-the-machine-do-alone}

Paul Fitts's 1951 report listing what humans and machines each do better began a long argument about allocation. Thomas Limoncelli's 2015 column "Automation Should Be Like Iron Man, Not Ultron" contrasts its principles: the *left-over principle* automates everything possible and leaves people the rest, the design Bainbridge criticized; the *compensatory principle* gives each task to whichever party does it better; and the *complementarity principle*, which he favors, has people and machines work together so that people keep the skill to take over.

For a vocabulary we turn to Thomas Sheridan and William Verplank, who in 1978, studying remote control of undersea vehicles at MIT, set out levels of automation between full human control and full machine autonomy. The 10-level table usually quoted is the one Raja Parasuraman, Sheridan and Christopher Wickens published in 2000, with a refinement: the level is chosen separately for each function, from gathering information through analysis and decision to action.

| Level | What the machine does | Encore example |
|---|---|---|
| 1 | Offers no help; the human does everything | the old pre-warm wiki page |
| 2–3 | Offers a full set of options, or narrows them to a few | a dashboard listing candidate replicas for a manual failover |
| 4 | Suggests one action | an alert that links the matching runbook step |
| 5 | Executes the suggestion if the human approves | curtain-up: the on-call engineer reviews the plan and presses go |
| 6 | Allows a limited time to veto, then acts | a proposed scaling change that applies unless rejected within 5 min |
| 7 | Acts, then necessarily informs the human | curtain-up's individual steps, reported in the channel |
| 8 | Acts, and informs only if asked | the node-upgrade reconciler (its log is there for anyone who looks) |
| 9 | Acts, and informs only if it decides to | Bot Screening's velocity rules, which block clients silently |
| 10 | Decides and acts entirely alone | Seat Inventory's fenced leader election, within its narrow domain |

*Figure 3.4 — Levels of automation, in the 10-level form of Parasuraman, Sheridan and Wickens (2000), applied to Encore. The level belongs to each action: curtain-up sits at level 5 for the decision and level 7 for its steps.*

Drawn for a real system, this table usually shows consequential automation at a level nobody chose, the one its first version happened to be built with; Encore now chooses the level per action and writes down why. Level 6 is rare in operations tooling, most of which treats an unanswered approval as a refusal, and Encore uses it only where acting late costs more than acting wrongly.

#### Use, misuse, disuse, abuse {#use-misuse-disuse-abuse}

How people come to rely on automation is the other half; Parasuraman and Victor Riley (1997) gave it four words.

| Term | Meaning | How it looks in operations |
|---|---|---|
| **Use** | relying on automation when appropriate | running curtain-up and reading its report |
| **Misuse** | over-reliance, including complacency | approving the plan unread, because it has always been right |
| **Disuse** | under-reliance, usually after false alarms | muting an alert channel that cried wolf last month |
| **Abuse** | automating without regard for the people left to supervise it | a remediation bot with no way to see or pause what it does |

*Figure 3.5 — Parasuraman and Riley's four relationships with automation. Misuse and disuse are failures of trust; abuse is a failure of design, made by designers and managers far from those who live with it.*

Seafarers had a phrase for misuse: the **radar-assisted collision**, between ships whose officers trusted the screen over careful plotting. John Lee and Katrina See (2004) gave the idea its precise form. **Calibrated trust** is reliance that matches the automation's actual capability: high where it performs well, low where it does not, and fine-grained enough to tell the two apart. People base trust on the automation's *performance*, *process* and *purpose*, and designers should make all three visible: a curtain-up report showing the cache hit ratio supports calibrated trust, while one that says only "done" gives no evidence of what happened.

{% include diagrams/fig-3-6.svg %}

*Figure 3.6 — Calibrated trust, after Lee and See (2004). Trust should track what the automation can actually do; misuse lives above the diagonal and disuse below it, and the same team can sit in both places with two different tools.*

#### Automation as a team player {#automation-as-a-team-player}

Gary Klein, David Woods and colleagues asked in 2004 what makes automation a "team player." Teammates enter a **basic compact**, an agreement to coordinate and to warn when they cannot keep their part. They are **mutually predictable**, **directable** (one can redirect the other as circumstances change), and they maintain **common ground**, the shared knowledge that lets a short message carry a great deal of meaning.

Curtain-up passes these tests. The node-upgrade reconciler is predictable and directable through its hold annotation, but shares little common ground with the teams on its nodes. Bot Screening's velocity rules, acting silently at level 9, are the weakest teammate. Directability is the test most often failed and the cheapest to pass, and the AWS outage shows its minimum: a documented off switch for each piece of automation, in place before an incident.

**Recap.** The levels of automation state, per action and function, how much a machine may do unasked, and that level should be chosen. Parasuraman and Riley describe how reliance goes wrong, and Lee and See how to calibrate it. The team-player tests ask whether automation can be supervised at all, beginning with an off switch.

**Exercise 3.4.** Place five automated actions from your platform on the 10-level scale. For the highest, answer the four team-player questions. What would make it directable during an incident, and who knows where its off switch is?

### 3.5 Operations Agents — Automation That Investigates and Acts

#### A loop that chooses its own path {#a-loop-that-chooses-its-own-path}

An **operations agent** is a language model running in a loop with tools wired to production telemetry and control: on each turn it reads what its last tool call returned and decides what to query or do next. Everything else in this chapter follows a path a designer wrote down; an agent chooses its path at run time, so it can follow a symptom where no runbook goes, and no review of its code tells us what it will do next. Runbook automation is bounded by its program; an agent is bounded only by the tools and credentials around it, so its level of automation is a property of those permissions.

#### Where agents help, and where they do not {#where-agents-help}

The published record is young but specific. The best-documented success is narrowing suspects: Meta described in 2024 a system that filters recent changes to its web monorepo by ownership and code graph, then has a fine-tuned Llama model rank them; in a backtest, the culprit was among the top five 42% of the time, and low-confidence answers are withheld. Answering questions and drafting summaries, mostly retrieval, is the second: Uber's on-call copilot, Genie, had answered over 70,000 questions by 2024, with a reported helpfulness rate just under 49%. The third is action behind approval: the clouds' own agents investigate with a read-only role, and each write is approved separately, with credentials narrowed to that operation.

End-to-end diagnosis and autonomous remediation are another matter. ITBench, from IBM and academic colleagues (ICML 2025), gave agents built on state-of-the-art models 102 realistic IT scenarios; they resolved 11.4% of the site reliability ones. A benchmark does not measure production, and on this record agents in 2026 are fast researchers, unreliable diagnosticians and unproven operators.

#### Two failures and what they teach {#two-failures}

Two failures from July 2025 teach more. During a public trial of Replit's coding agent by Jason Lemkin, founder of SaaStr, the agent ran destructive commands that erased his production database in the middle of a "code and action freeze" he had declared. The freeze was an instruction typed into a conversation; the agent still held every permission it had held before, and development and production shared one database. Replit's response was structural: automatic separation of the two databases. In April 2026, by its founder's account, the startup PocketOS lost a production database the same way, to an agent that found an API token created for managing domains but valid for anything.

The second case concerns what an agent reads. Version 1.84.0 of the Amazon Q Developer extension for Visual Studio Code, published on 17 July 2025, carried a prompt telling the agent to clear a system "to a near-factory state and delete file-system and cloud resources." An attacker had committed it through an over-scoped build token, and it shipped in an official release; AWS says a syntax error kept it from running. Since an agent cannot reliably tell instructions from data, a ticket, a log line or a retrieved postmortem can carry an instruction too, the confused-deputy problem of Chapter 14. A read-only agent still reads attacker-reachable text, and in all three cases the fix was made in the platform.

#### Cue {#cue}

Encore's operations agent, **Cue**, is built on the internal Model Context Protocol (MCP) server and is read-only by default: it reads telemetry, deploy history, runbooks and past postmortems, answers questions in the incident channel and drafts timelines, as Chapters 5 and 12 show.

Cue can invoke only actions in a fixed catalog that the MCP server exposes, whatever it asks for. Each action carries a blast-radius tag that Cue must show with every suggestion; the tags came after the Vesper Hale on-sale of Chapters 12 and 13, when Cue suggested restarting Seat Inventory's pods without saying that each restart would force a leader election. Cue first posts a plan: action, target, tag, and how to undo it. When a named person approves that plan in the channel, Encore's token service issues a token for that one action on that one target, valid for five minutes, through an OAuth token exchange (RFC 8693) as for all its agents. Cue holds no standing write credential; the per-action token is Encore's own choice, built on the principle of least privilege. When the on-sale freeze begins, the control plane withdraws Cue's write scopes on the purchase path; if an incident is declared, its mitigation actions return, each still needing an approver. Tickets and logs reach the model marked as untrusted, but the real defense is that nothing Cue reads can widen what it may do.

```yaml
# cue-actions.yaml: enforced by the MCP server and token service; the prompt cannot change it
default: read-only           # telemetry, deploys, runbooks, postmortems
token: {exchange: rfc8693, scope: one-action-one-target, ttl: 5m}
plan_before_apply: true
freeze: {purchase_path_writes: withdrawn, declared_incident: approval-only}
actions:
  catalog.raise_hpa_floor: {blast: "Catalog only; reversible", max: 60, approve: none}
  reconciler.hold_node:    {blast: "delays one node upgrade", approve: none}
  gate.raise_concurrency:  {blast: "Gate cost; no fan impact", approve: on-call}
  curtain_up.pause:        {blast: "on-sale prep stops", approve: on-call}
  inventory.restart_pods:  {blast: "LEADER-ELECTED: failover per shard", approve: ic}
```

Autonomy is granted per action class, by track record: the Reliability team records each suggestion as accepted, declined or, after the postmortem, judged wrong, and a class moves from level 5 to level 7 only on that record. Two have: raising Catalog's autoscaler floor through the same Git change a person would make (Chapter 7 explains why never by direct scaling), capped at 60 replicas; and holding a node in the upgrade reconciler. Everything else waits for a person.

#### Reviewing the plan {#reviewing-the-plan}

Reviewing an agent's plan is the new monitoring task, and it inherits Bainbridge's warning: after a long run of good plans, the reviewer is watching for a rare event. Anthropic reported in 2026 that users of its coding agent approve 93% of permission prompts, and called the result approval fatigue. Approval stays meaningful only while the reviewer can still investigate unaided, a skill that fades when the agent always investigates first, so Encore protects it as it does the manual failover: half of all drills run with Cue switched off. During Vesper Hale the engineer who declined Cue's restart had done a failover by hand a quarter earlier, and it is the best argument I have for those drills.

**Recap.** An operations agent chooses its own path, so its safety lives in its permissions. The evidence supports agents for narrowing suspects, answering questions and acting behind approval; for autonomous diagnosis or remediation it does not yet. Encore keeps Cue's catalog, per-action tokens and freeze in the platform, grants autonomy by record, and drills without it.

**Exercise 3.5.** For every action an AI tool in your operations can take, find where the permission is enforced: in a credential, a platform check, or only the prompt. Of the last 20 approvals, how many were declined, and how many checked against the source?

### Kata: The Hand-Back

> **Your brief: "Lanternway."** A managed hosting company for 3,000 online shops, run by 22 operations engineers. A remediation bot restarts unhealthy containers about 400 times a week, and database failover is hands-off. An operations agent in the on-call channel can run 15 remediation actions with one-click approval, using a long-lived administrator key; it has been approved 1,100 times and declined twice. On-call engineers still report 35% of their week as toil. Last month a database failover stalled and handed control to a human for the first time in 14 months; the manual procedure took 95 minutes, 40 of them spent finding the right credentials.

**Deliverables:**

1. **Toil inventory** — the top five sources of toil, and how each scales with the number of shops.
2. **Runbook ladder** — the rung of the 10 most frequent procedures, and the next rung for 3, with checks that replace lost attention.
3. **Levels map** — every automated action on the 10-level scale with its off switch, and the three you would move, with reasons.
4. **Hand-back drills** — which manual procedures are drilled, how often and by whom.
5. **Agent permission policy** — the action catalog with blast-radius tags, per-action credentials, what a freeze withdraws, and which actions, if any, may run unapproved.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Judgment preserved | When a procedure climbs the ladder, is each moment of human attention replaced by an explicit check? |
| Chosen levels | Is each action's level a written decision, with a rate limit and an off switch? |
| Practiced hand-backs | Would the stalled failover now take minutes, and who has practiced it this quarter? |
| Permissions outside the model | If the agent's instructions were ignored or injected, where exactly would it be stopped? |
| Meaningful approval | When the agent is wrong, how likely is a reviewer to decline, and how would you know? |

#### Where you now stand

You can now measure toil, move a procedure from runbook to self-service without losing the judgment it carried, and recognize Bainbridge's ironies in your own platform. You can choose how much each machine may do alone, give it limits and an off switch, and keep an operations agent's permissions where its prompt cannot reach them. Part II turns to how we know the system is working, beginning in Chapter 4 with how reliable it needs to be.

### References

- Lisanne Bainbridge — [*Ironies of Automation*](https://doi.org/10.1016/0005-1098%2883%2990046-8). Automatica 19(6): 775–779, 1983.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Amazon Web Services — [*Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region*](https://aws.amazon.com/message/101925/). 2025 — free online.
- Raja Parasuraman, Thomas B. Sheridan, Christopher D. Wickens — [*A Model for Types and Levels of Human Interaction with Automation*](https://doi.org/10.1109/3468.844354). IEEE Transactions on Systems, Man, and Cybernetics A 30(3): 286–297, 2000.
- Raja Parasuraman, Victor Riley — [*Humans and Automation: Use, Misuse, Disuse, Abuse*](https://doi.org/10.1518/001872097778543886). Human Factors 39(2): 230–253, 1997.
- John D. Lee, Katrina A. See — [*Trust in Automation: Designing for Appropriate Reliance*](https://doi.org/10.1518/hfes.46.1.50_30392). Human Factors 46(1): 50–80, 2004.
- Gary Klein et al. — [*Ten Challenges for Making Automation a "Team Player" in Joint Human-Agent Activity*](https://doi.org/10.1109/MIS.2004.74). IEEE Intelligent Systems 19(6): 91–95, 2004.
- Thomas A. Limoncelli — [*Automation Should Be Like Iron Man, Not Ultron*](https://queue.acm.org/detail.cfm?id=2841313). ACM Queue, 2015 — free online.
- David D. Woods et al. — [*Behind Human Error*, 2nd ed.](https://www.routledge.com/Behind-Human-Error/Woods-Dekker-Cook-Johannesen-Sarter/p/book/9780754678342). Ashgate, 2010.
- Dan Slimmon — [*Do-nothing scripting: the key to gradual automation*](https://blog.danslimmon.com/2019/07/15/do-nothing-scripting-the-key-to-gradual-automation/). 2019 — free online.
- Meta Engineering — [*Leveraging AI for efficient incident response*](https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/). 2024 — free online.
- Nicholas Marcott, Eduards Sidorovics, Paarth Chothani et al. — [*Genie: Uber's Gen AI On-Call Copilot*](https://www.uber.com/blog/genie-ubers-gen-ai-on-call-copilot/). Uber Engineering, 2024 — free online.
- Saurabh Jha et al. — [*ITBench: Evaluating AI Agents across Diverse Real-World IT Automation Tasks*](https://proceedings.mlr.press/v267/jha25a.html). ICML, 2025 — free online.
- Amazon Web Services — [*Security Update for Amazon Q Developer Extension for Visual Studio Code (Version #1.84)*](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/). 2025 — free online.
- John Hughes — [*How we built Claude Code auto mode: a safer way to skip permissions*](https://www.anthropic.com/engineering/claude-code-auto-mode). Anthropic Engineering, 2026 — free online.
- DevOps.com — [*When AI Goes Really, Really Wrong: How PocketOS Lost All Its Data*](https://devops.com/when-ai-goes-really-really-wrong-how-pocketos-lost-all-its-data/). 2026 — free online.
- The Register — [*Vibe coding service Replit deleted user's production database, faked data, told fibs galore*](https://incidentdatabase.ai/reports/5578/). 2025, via the AI Incident Database — free online.

---

## Chapter 4: Reliability as a Product Decision — SLOs, Error Budgets, and Risk {#ch4}

> Every promise about reliability is also a promise about what we will stop doing.

How reliable should a system be? Engineers tend to answer "as reliable as we can make it." The answer sounds responsible and is nearly always wrong. Reliability costs money, attention and, above all, the freedom to change things, and a system made as reliable as possible has spent all three on a property its users stopped noticing several nines ago. The real question is a product question: how much unreliability can our users absorb before they would rather be elsewhere, and what will we buy with the rest?

The telephone network first asked that question at scale, and its answer, "five nines," became a byword. We follow its engineers, taking the chain [the Architecture book](https://oleksiyp.github.io/arch-book/#from-is-it-up-to-why-is-it-weird) introduced, from service level indicator (SLI) to service level objective (SLO) to error budget, and turning it into an instrument that chooses what to measure, settles arguments between teams and wakes people only when it should.

Encore needs that instrument now. It has one published objective, for the seat map, and 40 teams with opinions about what the others should promise. The Reliability team, the platform group's ten site reliability engineers, has been asked to give checkout, the on-sale window and every tenant an objective users would recognize, before the next big Friday. (Chapter 1's [map of Encore](/prodsys-book/ch/1/#encore) shows where each piece sits.)

### 4.1 Why 100% Is the Wrong Target

#### The Bell System and its nines {#bell-system-nines}

For most of the twentieth century the Bell System, AT&T with Western Electric and Bell Telephone Laboratories, ran the American telephone network as a regulated monopoly, with an engineering culture built on the expectation that the dial tone would always be there. The first No. 1 Electronic Switching System (ESS), in service at Succasunna, New Jersey, from 1965, carried a design objective of no more than two hours of total downtime in 40 years, a little better than 99.999%, and met it by duplicating its central processor so that one copy could carry calls while a fault in the other was isolated.

Two details teach more than the famous number. The objective belonged to the switch, while the subscriber also depended on the copper loop, the handset and the weather. And the same network was deliberately engineered to fail some calls. Trunk capacity was sized to a **grade of service**, a target probability that a call is blocked in the busiest hour, commonly one call in a hundred, because never blocking a call would have been ruinous. The most reliability-minded engineering organization of its century thus accepted a small, priced failure rate at its peak, an error budget in all but name; Chapter 6 takes up the mathematics.

#### What each nine costs {#what-each-nine-costs}

Figure 4.1 translates nines into time, per year and per the rolling 28-day window Encore uses.

| Availability | Downtime per year | Downtime per 28 days |
|---|---|---|
| 99% | 3.65 days | 6.7 h |
| 99.5% | 43.8 h | 3.4 h |
| 99.9% | 8.8 h | 40 min |
| 99.95% | 4.4 h | 20 min |
| 99.99% | 53 min | 4 min |
| 99.999% | 5.3 min | 24 s |

*Figure 4.1 — The nines as time. Each additional nine divides the allowance by ten; the cost of staying inside it rises by much more.*

Read the right-hand column as an operator would. At 99.9%, Encore can afford one bad deploy a month that takes half an hour to roll back. At 99.99%, four minutes, it cannot afford a human in the loop, so detection and rollback must be automatic. Each nine changes the kind of engineering as well as its amount.

Users cannot perceive reliability beyond that of their own path to us. A fan cannot tell a 99.99% seat map from a 99.999% one, as the *Site Reliability Engineering* book observes, and reliability beyond what users perceive is paid for in change not made. The exceptions are paths where failure harms someone rather than annoys them, clinical or safety systems among them, where perception is the wrong yardstick and regulators set the floor. Elsewhere, a target of 100% is not a very high standard. It is a refusal to choose, and it hands the choice to whoever is most frightened.

This is why reliability is a product decision. Only the product owner can weigh a slightly less reliable seat map against a feature fans have been asking for; engineers can only say what each option costs.

**Recap.** The Bell System chose its nines, engineered to them and accepted blocked calls at the peak. Because users cannot feel reliability beyond their own path to us, the target is a product choice about where to spend the freedom to change, except where failure causes harm.

**Exercise 4.1.** For a service you run, find the row of Figure 4.1 at which a single incident, handled by your current detection, paging and rollback, would consume the whole monthly allowance. Is your published target above or below that row?

### 4.2 SLIs and SLOs That Users Would Recognize

#### From journeys to indicators {#journeys-to-indicators}

A **service level indicator (SLI)** is a measurement of service, expressed as the proportion of valid events that were good; a **service level objective (SLO)** is a target for that proportion over a stated window. The harder craft is choosing which events to count and what to call good, and the test I find most reliable is simple: could a fan, shown the SLI in plain words, recognize it as something they have felt? That test points away from components and toward **user journeys**, such as joining the waiting room, holding seats or checking out, each with a defined event, good event and place of measurement.

Take checkout. A naive SLI counts HTTP 5xx responses from Orders and gets several cases wrong. When a fan's bank declines the card, the system has worked correctly and the event is good, however unhappy the fan. When both of Encore's payment service providers (PSPs) are degraded and a verified fan's seats are held pending payment, the fan has been told the truth, and that is good too. But a decline Encore caused itself, by timing out on the PSP or breaking the strong customer authentication step, is bad, though the fan sees the same polite "payment declined." So Encore's checkout SLO reads: *of checkout attempts by admitted fans, 99.9% end in a confirmed order, a hold pending payment or an issuer's decline, correctly explained, within 3 s, measured at the gateway over a rolling 28 days.* About 800 ms of those 3 s belong to the PSP.

#### Ratios, thresholds and percentiles {#ratios-thresholds-percentiles}

An **event-based** (ratio) SLI counts good events over valid events; a **time-based** SLI counts good slices of time, such as minutes with an error rate below 1%. The first weights busy periods heavily, which is usually what we want; the second suits services with little traffic, and contracts. Latency is where well-meant indicators go astray. "p99 latency below 800 ms" and "99% of requests faster than 800 ms" sound identical, but percentiles cannot be averaged: the mean of 10 servers' p99 values is not the fleet's p99. The ratio form adds good and total counts, so it combines correctly across servers. Encore therefore states latency objectives as ratios and records latency in histograms with a bucket boundary exactly at each threshold, since a histogram can only answer questions about the boundaries it was given.

Where to measure matters as much. Encore measures at the gateway, because a server timing itself cannot see the requests queued in front of it. The gateway is closer to the fan, but it still cannot see a failed DNS lookup, a content delivery network fault or a phone that never connected. So the purchase journeys also carry client-side measurement from Encore's app, and the ticket-delivery SLI is confirmed by the wallet's receipt, since Notifications can only know that it sent something.

#### Windows, and the hour that matters {#windows-and-on-sale-slos}

The window is the SLO's memory. A **rolling window** remembers continuously, so a bad Friday weighs on the team for exactly as long as the window and is then forgiven; Encore follows *The Site Reliability Workbook* in using four weeks, so every window holds four of each weekday. A **calendar window** suits reports and contracts but creates strange incentives: a budget nearly spent on the 29th is restored in full on the 1st.

Fans, however, do not remember months. They remember 10:00 on the Friday their artist went on sale, and a 28-day objective can stay green while that hour was a disaster, diluted by 27 quiet days. So for each on-sale classed as major at the readiness review the Wednesday before, Encore also evaluates an **on-sale-window SLO**: an objective computed over a fixed window around a scheduled event, here the first 60 minutes of the sale, with a budget of its own. This is Encore's own adaptation, with no published practice of that name behind it. It rests on the Workbook's advice that a window should match how users experience the service, and its costs were accepted knowingly. A short, front-loaded window is statistically noisy. Burn-rate alerting cannot work inside it (Section 4.4). And per-event budgets have no policy precedent, so a missed on-sale-window SLO earns a postmortem and a readiness-review item, never a freeze.

The on-sale SLI counts fans. A fan who retries an error 10 times generates 10 bad requests whether or not the 11th succeeds, and has had one bad on-sale however many requests it took. The price is a per-fan key shared by the Gate and the gateway, harder to build than it sounds.

| Journey | SLI (good ÷ valid) | Where measured | Objective and window |
|---|---|---|---|
| See seat map | requests served in ≤ 800 ms | gateway | 99.9%, rolling 28 days |
| Shop once admitted | admitted fans finishing with an order or "sold out," no error page or false block | Gate and gateway, joined per fan | 99.9%, rolling 28 days |
| Major on-sale | the same indicator | Gate and gateway, joined per fan | 99%, first 60 min of the sale |
| Check out | attempts ending in confirmed order, pending-payment hold or explained issuer decline within 3 s | gateway | 99.9%, rolling 28 days |
| Receive tickets | orders with ticket in wallet within 5 min | Notifications, confirmed by wallet receipt | 99.5%, rolling 28 days |

Each objective is a product decision, signed by the journey's product owner. Each began near what the journey had delivered the previous quarter and is reviewed quarterly, because an objective nobody revisits drifts into irrelevance.

**Recap.** Good SLIs start from user journeys and define the event, the good event and a place of measurement as close to the user as we can get. Ratios combine correctly across servers; percentiles do not. Rolling windows give an SLO a steady memory, and Encore gives its scheduled peaks a window shaped like the event, knowing the costs.

**Exercise 4.2.** For one SLI you have, find a case it counts as good that the user felt as bad, and one it counts as bad that nobody noticed. Rewrite it to count both correctly.

### 4.3 Error Budgets as a Negotiation Instrument

#### A contract written in calm weather {#contract-in-calm-weather}

An **error budget** is the amount of unreliability an SLO permits over its window, and an **error budget policy** is the written agreement about what happens as it is spent. The budget is arithmetic. The policy is an agreement among people with different interests about how to share something scarce.

Its value lies in timing: it moves the argument about shipping or stabilizing from the outage to a quiet Tuesday. Encore's purchase-path policy, taken nearly unchanged from the example in *The Site Reliability Workbook*, says that while budget remains teams ship at will, that once it is exhausted only reliability work, security fixes and risk-reducing changes ship until it recovers, and that any incident consuming more than 20% of a budget requires a postmortem. Between those clauses sits a tier of Encore's own: below 25% remaining, every change to the journey is also reviewed, in the same pull request, by the site reliability engineer embedded with the team. The form is deliberate. DORA's research found that approval by a body outside the team slows delivery without making it safer, so the embedded engineer reviews as a peer who knows how the journey fails, and holds no gate.

A policy like this holds only because people with authority over both kinds of work signed it, at Encore the heads of engineering and product. Many organizations publish SLOs and never enforce a policy, and the targets become decoration. Encore follows Hidalgo's advice that a policy should guide decisions rather than freeze teams mechanically.

Budgets are also meant to be spent, usually on faster change. The *Site Reliability Engineering* book tells of Google's Chubby lock service, whose users came to depend on more than it promised, until planned outages brought its real availability down to its objective. Unspent budget is reliability nobody promised, and someone will soon build on it. The idea is older than SRE: Walter Shewhart's control charts, made for the Bell System in the 1920s, told managers when variation was the process behaving as designed and when it had a cause worth hunting.

#### The dispute between On-Sale and Bot Screening {#onsale-botscreening-dispute}

Encore's policy met its first real test in the spring. Bot Screening's rules keep bots out of the waiting room and watch admitted sessions. That season the team switched on a new device-fingerprint rule at a mid-size arena on-sale that the readiness review had classed as major. The rule ran at the hold step, after admission, and in 15 minutes it blocked about 6,000 admitted fans, most of them, as Support's inbox later showed, real people on an older phone browser. The "shop once admitted" indicator, as written then, counted every journey ending on a block page as bad. About 200,000 fans were admitted in the first hour, so the on-sale-window SLO came in at 96.8% against its 99%. The 28-day objective for the same journey, 99.9% of about 8.6 million admitted fans in a typical four weeks, allows some 8,600 bad journeys; the 6,000 took 70% of it and put the On-Sale team into the review tier. Figure 4.2 shows the burn.

{% include diagrams/fig-4-2.svg %}

*Figure 4.2 — The On-Sale team's 28-day error budget through the spring on-sale. Ordinary spending keeps the budget well above the steady burn line; one rule from another team takes 70% in 15 minutes and drops the budget below the policy's 25% line.*

Both teams had a case. On-Sale said a real fan blocked mid-purchase is the worst error the system can make, and it had paid for someone else's change. Bot Screening said a block is the system doing its job, and an indicator that charged it for every bot caught would teach it to let bots through. Bot Screening's mistakes come in two kinds that are never equally visible: the bot let through, which the resale market reports within the hour, and the fan turned away, which only the fan can report.

The Reliability team brokered a resolution that began with what the indicator counts. The Workbook's example policy already lets out-of-scope traffic, such as load tests and abusive clients, be excluded from the budget, and Encore gave that clause an operational test. Every block now offers a challenge and a way back into the sale. A blocked session that fails or abandons it is treated as bot traffic and leaves the journey's valid events; one that passes is a **false block**, a person the rules turned away, and counts as bad, since the fan lost a hold whatever happened next. Most of the spring's 6,000 blocked fans were real people, false blocks by this test, so the burn stood.

The rest followed. The policy now attributes consumption: the review tier applies to the team whose change caused the burn, so Bot Screening went under review. That goes a step past the Workbook, which only spares the team whose budget another team's outage spent, and it risks drifting into blame when, as Chapter 13 shows, a burn has more than one cause. Bot Screening also gained an indicator of its own, the **false-block rate**: false blocks divided by admitted sessions screened, with an objective of no more than one in a thousand. It is a proxy that errs both ways, since solver farms pass challenges and some fans give up rather than try, so the team checks it monthly against a sample of Support complaints. Cloudflare offers the measure as a "challenge solve rate" for tuning rules; giving it an objective is Encore's own step. And new rules now run in shadow mode through one on-sale before they enforce anything, logging what they would have blocked, the practice AWS WAF calls Count and Cloudflare calls Log.

Nobody thought to ask the same of the rules already in force. Among them was a velocity rule, written years earlier, that watches how fast and how often a session acts. It had never caused a dispute and was never reviewed, an omission that will matter in Chapter 12.

**Recap.** The policy is an agreement, written in calm weather and signed by people with authority, about how teams share a scarce allowance of failure. When a dependency spends another team's budget, the answer is a clear definition of what counts, attribution used with care, and an indicator of the dependency's own.

**Exercise 4.3.** Draft a one-page error budget policy for a journey you own: thresholds, what changes at each, who grants exceptions, which traffic is out of scope and how a burn caused by another team is attributed. Then ask that team to read it.

### 4.4 Alerting on Burn Rate

#### Fuel flow and the fuel gauge {#watching-the-flow}

An SLO gives a principled answer to the oldest question in operations, when to wake a human: when the budget is burning fast enough to matter. The **burn rate** is the rate at which a service consumes its error budget, relative to the rate that would exactly exhaust it at the end of the window: a burn rate of 10 spends the budget in a tenth of the window.

Pilots know the difference between level and flow: a leak shows up in the fuel flow long before the gauge looks alarming. Budget remaining is the gauge, burn rate the flow. The analogy breaks because engines burn fuel steadily while errors arrive in bursts, so a single reading of burn rate is noisy. *The Site Reliability Workbook* weighs the alternatives and arrives at **multi-window, multi-burn-rate alerting**: page when the budget is burning fast over a long window *and* is still burning over a short one.

#### The arithmetic {#burn-rate-arithmetic}

For a 30-day window, the Workbook suggests paging if 2% of the budget is consumed in one hour, a burn rate of 0.02 × 720 h ÷ 1 h, or 14.4, at which the whole budget would be gone in 50 hours; a second page if 5% is consumed in six hours (a burn rate of 6); and a ticket if 10% is consumed in three days (a burn rate of 1). The long window gives significance and the short one, by convention a twelfth of its length, gives timeliness: both must exceed the threshold, so when the bleeding stops the short window drops below the line within minutes and the page resolves.

| Severity | Budget consumed | Long window | Short window | Burn rate | Budget gone in | Response |
|---|---|---|---|---|---|---|
| Fast burn | 2% | 1 h | 5 min | 14.4 | about 2 days | page |
| Medium burn | 5% | 6 h | 30 min | 6 | 5 days | page |
| Slow burn | 10% | 3 days | 6 h | 1 | 30 days | ticket |

*Figure 4.3 — Multi-window, multi-burn-rate alerting, with the Workbook's parameters for a 30-day budget.*

Encore's windows are 28 days, but it kept the Workbook's multipliers, as most SLO tools do; they then mean about 2.1% and 5.4% of budget. For the seat map's 99.9% objective, a burn rate of 14.4 means a bad-request ratio above 1.44%. In Prometheus, with a recording rule per window, the rules read:

```yaml
groups:
- name: seat-map-slo   # 99.9% of requests <= 800 ms over 28 days: budget 0.001
  rules:
  - record: seatmap:bad_ratio:rate5m   # likewise for 30m, 1h, 6h and 3d
    expr: 1 - sum(rate(gateway_request_duration_seconds_bucket{route="seat-map",code!~"5..",le="0.8"}[5m]))
            / sum(rate(gateway_request_duration_seconds_count{route="seat-map"}[5m]))
  - alert: SeatMapBudgetFastBurn
    expr: (seatmap:bad_ratio:rate1h > 14.4 * 0.001 and seatmap:bad_ratio:rate5m > 14.4 * 0.001)
       or (seatmap:bad_ratio:rate6h > 6 * 0.001 and seatmap:bad_ratio:rate30m > 6 * 0.001)
    labels: {severity: page}
  - alert: SeatMapBudgetSlowBurn
    expr: seatmap:bad_ratio:rate3d > 0.001 and seatmap:bad_ratio:rate6h > 0.001
    labels: {severity: ticket}
```

Nobody at Encore writes these by hand. Copied rules keep the old objective after it changes, so the golden path generates them from each service's SLO entry in the registry, as open-source generators such as Sloth and Pyrra do from a few declared lines.

Detection times are the alert's real specification. If the seat map fails completely, the one-hour ratio crosses 1.44% in about 52 seconds. If one request in 50 is slow, the line is crossed after about 43 minutes, by which time the incident has spent about 2% of the budget, exactly as designed. Figure 4.4 follows a partial outage, one request in ten failing for 40 minutes, through both windows.

{% include diagrams/fig-4-4.svg %}

*Figure 4.4 — A fast-burn page through one incident. The one-hour ratio decides when the page fires and the five-minute ratio decides when it stops: without the short window, the page would outlast the fix by more than three-quarters of an hour.*

#### Where the rules run out {#where-the-rules-run-out}

Burn-rate alerting needs traffic: at a few requests a minute, one failure moves the ratio by whole percentage points, a problem Section 4.5 meets again with small tenants. Nor can these rules protect an on-sale-window SLO. At 99% over 60 minutes, a total failure spends the entire budget in 36 seconds, sooner if admissions crowd into the first minutes, and a one-hour alert window is as long as the SLO window itself, so the page could only fire after the budget was gone.

For major on-sales Encore therefore has people watch the signal. The owning teams and an incident commander watch one-minute per-fan error ratios from the moment the Gate opens. A page stays armed all the same: a rule rescaled to the hour pages the On-Sale on-call when both the one-minute and five-minute per-fan error ratios exceed 10%, ten times the hour's allowance, because attention fades over a long sale and trouble can begin in a component nobody is watching. Google's launch practice, in the SRE book, is the same: people watching closely, alerts still on.

**Recap.** Burn rate measures how fast the budget is being spent; a long window supplies significance and a short one timeliness. Detection times turn an alert rule into a specification, and generating rules from the SLO keeps them faithful to it. For event-shaped windows, people watch, with a rescaled page as the backstop.

**Exercise 4.4.** For one SLO you own, compute the thresholds for the three rows of Figure 4.3 and how long a total outage and a 5% partial outage would take to page. Would your users accept those times?

### 4.5 SLOs Across Dependencies and Teams

#### Composition only subtracts {#composition-only-subtracts}

No service meets its SLO alone. Checkout depends on the Gate, Seat Inventory, Orders & Payments and the PSP, and "The Calculus of Service Availability" (Ben Treynor and co-authors, 2017) states the hard limit: a service can be no more available than its least available critical dependency. If those dependencies fail independently, their availabilities multiply, and four at 99.95% each give about 99.80%, below the checkout objective before Orders has written a line of its own. If their failures coincide, because they share a database, a network or a region, the composite is better than the product but never better than 99.95%. For separately run services the product is the honest guide. Figure 4.5 draws the arithmetic.

{% include diagrams/fig-4-5.svg %}

*Figure 4.5 — The availability of a chain of hard dependencies whose failures are independent. At 99.95% each, the chain reaches checkout's objective at the second dependency and falls below it at the third; at 99.99% each, three still leave room for checkout's own failures.*

A sound engineer knows that the finest mixing desk cannot fix a crackling cable. Here the analogy breaks in our favor: a service, unlike a sound system, can often keep its promise when a dependency fails, if it was designed to.

Encore uses both of the paper's remedies. The first is its rule that critical dependencies should be roughly one nine more reliable than the service: Encore holds its internal purchase-path services to 99.99%, so three of them multiply to about 99.97%, leaving room inside a 99.9% promise. The paper warns against demanding an extra nine at every layer down the stack; where a dependency cannot supply one, the second remedy applies, which is to make the dependency soft. The PSP's contract promises 99.9% per calendar month, which alone would pull a hard-wired checkout below its objective. So Orders & Payments routes each new payment to whichever of two PSPs is healthy, as large merchants do, though both lean on the same card networks. When both are degraded, verified fans' seats are held for up to 20 minutes until they can pay, with strong customer authentication, and unpaid holds lapse; no ticket is ever issued without an authorized payment. Figure 4.6 shows the result.

| Dependency | Its objective | Hard or soft for checkout | What Encore does when it fails |
|---|---|---|---|
| Sale Gate (admission) | 99.99% internal | hard | admitted fans continue; new admissions pause |
| Seat Inventory (writes) | 99.99% internal | hard | holds fail fast with a clear message |
| Orders & Payments | 99.99% internal | hard | saga resumes from its last step |
| PSPs (two) | 99.9% each per calendar month, contractual | soft | route new payments to the other PSP; if both are degraded, hold verified fans' seats pending payment |
| Notifications | 99.9% internal | soft | ticket delivered late, order confirmed now |

*Figure 4.6 — Composing checkout. Hard dependencies multiply and need an extra nine; soft ones are designed out of the product, and the PSP row is why the checkout SLO is achievable at all.*

An SLO thereby becomes part of a service's interface. Encore's service registry shows each service's SLOs beside its API contracts, telling consumers how much to trust it as a type signature tells them what to pass. This is information hiding, in the sense [the Architecture book](https://oleksiyp.github.io/arch-book/#13-modularity-and-logical-components) took from Parnas, extended to reliability: depend on the promise, because observed behavior is only a coincidence that has lasted so far.

#### Tenants, contracts and small numbers {#tenants-and-contracts}

Encore serves venues in three tiers: about 500 self-service venues pooled in serverless cells of about 50, Professional tenants in Kubernetes cells with a database each, and one Enterprise tenant, `venue-chain-a`, in a silo of its own. Self-service venues are promised 99.9%, Professional tenants 99.95%, and `venue-chain-a` has a **service level agreement (SLA)**, a contractual promise with consequences: 99.95% per calendar month, with service credits below it. Its internal SLO is 99.97% over a rolling 28 days, because the gap between SLO and SLA is where engineers fix things before anyone writes an invoice; the gap is thin and the windows differ, so the SLA is also tracked on its own calendar month.

Small tenants raise a problem of statistics. A venue selling 300 tickets a month would breach a per-venue 99.9% objective with one unlucky fan, and Hidalgo's book gives a chapter to the probability involved: an SLO needs enough events to tell signal from chance. Encore measures self-service SLOs per cell, the unit that fails together. Aggregation has its own blind spot, since one venue entirely down may barely move a cell's ratio, so a synthetic probe, a scripted visitor loading each venue's storefront and seat map every minute from outside Encore's network, pages when a venue fails several probes in a row.

Every tenant's checkout passes through the same Seat Inventory, so the core must be as reliable as the strongest promise it supports; cells, Chapter 9's subject, limit blast radius but cannot lift reliability above it.

**Recap.** A journey can be no more available than its weakest critical dependency, and independent ones multiply, so critical dependencies need an extra nine or must be made soft. Published SLOs belong in a service's interface. SLAs sit outside SLOs with room to spare, and low-volume objectives need enough events, with probes to catch what aggregation hides.

**Exercise 4.5.** Draw the dependency chain for your most important journey, mark each dependency hard or soft with its published objective (or "none"), and multiply the hard ones. Does the product leave room for your SLO, which dependencies share infrastructure, and which would you make soft first?

### Kata: The Eight O'Clock Slots

> **Your brief: "Kindred Health."** A telehealth platform runs video consultations with about 2,400 doctors in three EU countries, some 6 million a year. Patients book in the app, and 85 insurer and clinic partners book through an API with a contractual 99.9% monthly SLA. A consultation needs the booking service, an external video relay, a national eID login in two of the countries and an insurer eligibility check; payments go through an external PSP. Every weekday at 08:00 the day's same-day slots open, and in the flu season traffic rises 30× for about 40 minutes. Kindred's 35 engineers in six teams inherited a 99.99% alert on every service from a vendor template, on-call took 58 pages last month, and the clinical lead and product disagree about a flu-season freeze.

**Deliverables:**

1. **Journey SLOs** — for booking, joining a consultation, the video staying usable and partner booking: SLIs, measurement points, targets and windows, noting where clinical safety justifies more than patients would perceive.
2. **The eight o'clock SLO** — an event-window objective counted per patient, its statistical limits, and how people will watch it with a page behind them.
3. **Error budget policy** — thresholds, consequences, out-of-scope traffic, attribution between teams and who signs it, on one page.
4. **Burn-rate alert set** — multi-window rules for joining a consultation, with detection times for a total outage and a 3% partial one.
5. **Dependency composition** — the consultation chain, hard and soft dependencies multiplied, shared infrastructure noted, one hard dependency made soft.
6. **Partner SLA and internal SLO** — the objective behind the 99.9% partner SLA, and the reasoning for its margin.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Recognizability | Would a patient, reading each SLI in plain words, recognize it as something they have felt? |
| Honest arithmetic | Are latency objectives ratios, and do thresholds, detection times and composed availabilities check out? |
| Event-shaped thinking | Do the eight o'clock slots have their own window and per-patient counting, with the limits stated? |
| Policy as agreement | Does the policy say what happens at each threshold, who signed it, and was it written in calm weather? |
| Composition | Does the consultation SLO survive its hard dependencies, including the video relay and the eID login? |
| Paging discipline | Would the new alerts have cut last month's 58 pages without missing what mattered? |

#### Where you now stand

You can now choose indicators from what users experience, decide what traffic belongs in them, give scheduled peaks their own windows, write an error budget policy teams can live with, alert on burn rate and reason about reliability across dependencies and contracts. An SLO can tell us *that* users are suffering; it cannot say *why*. Chapter 5 turns to observability, the craft of asking a running system questions nobody thought to ask in advance.

### References

- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne (eds.) — [*The Site Reliability Workbook*](https://sre.google/workbook/table-of-contents/). O'Reilly/Google, 2018 — free online.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Alex Hidalgo — [*Implementing Service Level Objectives*](https://www.oreilly.com/library/view/implementing-service-level/9781492076803/). O'Reilly, 2020.
- Ben Treynor, Mike Dahlin, Vivek Rau, Betsy Beyer — [*The Calculus of Service Availability*](https://queue.acm.org/detail.cfm?id=3096459). ACM Queue, 2017 — free online.
- DORA — [*Streamlining change approval*](https://dora.dev/capabilities/streamlining-change-approval/). dora.dev — free online.
- Prometheus — [*Histograms and summaries*](https://prometheus.io/docs/practices/histograms/). Prometheus documentation — free online.
- Sloth — [*Sloth: Prometheus SLO generator*](https://sloth.dev/). sloth.dev — free online.
- Cloudflare — [*Challenge solve rate*](https://developers.cloudflare.com/cloudflare-challenges/reference/challenge-solve-rate/). Cloudflare documentation — free online.
- Amazon Web Services — [*Testing and tuning your AWS WAF protections*](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html). AWS WAF Developer Guide — free online.

---

## Chapter 5: Observability — Seeing What the System Is Doing {#ch5}

> The data will answer almost any question, but only the ones we think to ask.

In the last days of August 1854, cholera broke out around Broad Street in Soho, and within ten days some five hundred people living within a few hundred yards of one another were dead. The prevailing theory was miasma: disease rose from the foul air of a crowded city. John Snow, a London physician who had argued since 1849 that cholera traveled in water, did not argue the point again. He obtained the register of deaths, asked where each victim had drawn water, and marked every death as a bar against its address on a map.

The deaths clustered around the public pump on Broad Street, and the exceptions were the most persuasive evidence of all. The workhouse on Poland Street had its own well and very few deaths; the brewery's men drank beer and were spared. A widow in Hampstead, miles away, who liked the taste of Broad Street water enough to have a bottle carried to her daily, died of it. On 7 September Snow put his case to the parish Board of Guardians, and the next day the pump's handle was removed. The outbreak was already waning, and official opinion stayed unconvinced for years. Henry Whitehead, a curate who set out to disprove Snow by interviewing his parishioners one by one, found the source: a baby's soiled napkins rinsed into a cesspool a few feet from the well.

Snow had no better instruments than the miasma theorists. He asked the data a question the prevailing theory did not think worth asking, and he arranged the data so that it could answer. [The Architecture book](https://oleksiyp.github.io/arch-book/#from-monitoring-to-observability) borrowed *observability* from Rudolf Kálmán's control theory; here we take it in its working sense, the ability to ask a production system an unanticipated question and get an answer without shipping new code.

Encore has telemetry everywhere: metrics from every service, spans from the mesh, logs that make up much of the bill Chapter 6 examines, and dashboards with more panels than anyone has looked at in one sitting. The question is whether, when something new goes wrong, its engineers can find out why before its fans notice.

### 5.1 From Monitoring to Observability

#### Known questions and unknown ones {#known-and-unknown-questions}

**Monitoring** is the practice of checking a system against conditions we decided in advance were worth checking: is the error rate above 1%, did the synthetic buyer complete its purchase. It is indispensable, but a monitor can only encode a failure someone has already imagined. **Observability**, in the software sense, is the property of a system that lets us understand its internal state from its outputs well enough to answer questions *nobody* thought of in advance.

A monolith on three servers failed in ways an experienced operator could list. Encore's purchase path crosses a serverless waiting room (the Sale Gate), a bot screen, an event-sourced inventory sharded four ways (Seat Inventory), a saga orchestrator (Orders & Payments) and an external payment service provider (PSP), across two regions and a mesh. (Chapter 1's [map of Encore](/prodsys-book/ch/1/#encore) shows where each piece sits.) Nobody can list the ways those parts combine.

Peng Huang and his colleagues at Microsoft named the characteristic failure of such systems in a 2017 paper drawn from experience with Azure: **gray failure**, a partial failure that some observers see and others do not. Its signature is what they called differential observability: the system's own health checks report that all is well while some of its users suffer. Cindy Sridharan's short book of the following year made the idea the practitioner's case for observability. A monitor is an average or a threshold, so it answers well when something is down and poorly when something is wrong for *some* people, who are hidden inside the average.

Monitoring is the warning lights on a car's dashboard, observability the mechanic's workshop: when the car makes a noise that matches no light, more lights will not help. The analogy breaks because a car's engine does not change between visits, whereas Encore's changes dozens of times a day.

#### What observability is made of {#what-observability-is-made-of}

The ability to ask new questions comes from three properties of the telemetry itself. The data must be **high in cardinality**, meaning a field may take very many distinct values (an order ID, an `event_id`, a build hash), because many failures are specific to one of them. It must be **high in dimensionality**, carrying many fields per event, because we do not know in advance which field, or which combination, will explain the difference. And it must be **explorable**, kept so that we can slice, group and compare by any field after the fact.

Snow's register had exactly these properties: one row per person, with an address, a date and, after his door-knocking, a water source. The miasma theorists' summary, deaths per district per week, had thrown away the address, and with it the pump. Aggregation is a decision about which questions will never be asked again, and we usually make it before we know what they are.

The price depends on the store: Prometheus creates a time series for every combination of label values, so a fan ID as a label would ruin it, while columnar event stores such as Facebook's Scuba (2013) were built to make such questions affordable. Encore keeps both.

**Recap.** Monitoring checks known conditions and remains necessary; observability lets us ask about conditions nobody anticipated, such as gray failures. It comes from telemetry that is wide, high in cardinality and explorable.

**Exercise 5.1.** List the last five production problems in a system you know. For each, note whether an existing monitor detected it, and whether the cause was found using pre-built views or by asking a question the views could not answer.

### 5.2 Signals and Instrumentation with OpenTelemetry

#### Braided signals {#braided-signals}

For a decade the industry described telemetry as "three pillars" (metrics, logs and traces), each with its own pipeline. The metaphor did harm, because the value of telemetry lies in the connections between signals. A braid is the better image: what holds the weight is shared context, the same trace ID and the same names for the same things. Two humble mechanisms make it real, and they are the cheapest observability a team can buy: trace and span IDs written into every structured log line, which turns finding a slow request's logs into a lookup, and the **exemplar**, a trace ID attached to a sample in a metric's histogram, so that a latency graph offers a link to an actual slow request beside the spike. Encore's service template does both by default.

**OpenTelemetry** (OTel) is the vendor-neutral standard that makes the braid practical. It formed in 2019 from the merger of OpenTracing and OpenCensus, and it separates an API, against which code is instrumented, from a software development kit (SDK) that decides in configuration where the data goes. Its stable signals are traces, metrics and logs; profiles are arriving as a fourth, in alpha in 2026.

#### Semantic conventions as a shared vocabulary {#semantic-conventions}

The **semantic conventions** are agreed names and meanings for common attributes: `service.name` and `service.version` on every resource, `http.request.method` and `http.response.status_code` on every HTTP span, and so on through databases, messaging and, still in development, generative AI calls. If Orders records the HTTP status as `status`, Inventory as `http_code` and the Gate as `response.status`, then "show me every 5xx on the purchase path" is three queries, and in the middle of an incident nobody writes all three.

Encore extends the conventions with a namespace owned by the Reliability team, in a registry that continuous integration (CI) checks with OTel's Weaver tool. OTel asks companies to keep their own names under a unique prefix, so every Encore field lives under `encore.`: `encore.event_id`, `encore.tenant_id`, `encore.shard`, `encore.cell`, `encore.country`, `encore.payment_method`, and `encore.on_sale`, which the golden-path service template stamps on every span, true during a scheduled on-sale and false otherwise. This is information hiding in a new place: the registry puts names behind a contract, so one team's query works against another team's service.

#### The Collector and the economics of sampling {#collector-and-sampling}

Between the services and the backends sits the **OpenTelemetry Collector**, a pipeline of receivers, processors and exporters. Encore runs it in two tiers: agents on every node and beside each serverless function, which batch, forward and redact what they recognize, and a gateway tier that strips whatever got past them, routes security events to their own account, and decides what to keep. Every pipeline begins with a memory limiter, because an on-sale multiplies telemetry by the same 500× as traffic.

**Head sampling** decides at the start of a request whether its trace will be recorded, which is cheap and blind. **Tail sampling** decides once the trace is complete, at the price of holding spans in memory meanwhile and routing each trace to one gateway instance, which Encore does with a load-balancing exporter keyed on trace ID. The OpenTelemetry project is candid that the tail sampler is stateful and hard to operate.

Encore keeps every error, every checkout slower than 2 s, and a baseline: 10% normally, 1% during an on-sale, when 1,200 admissions a second per event would fill the store with identical successes. The sampler keeps a trace if *any* policy matches it, so a separate 1% policy beside a 10% one would change nothing. The baseline must be split, each half an `and` of a condition and a probability:

```yaml
tail_sampling:
  decision_wait: 60s                                 # outlasts a bank-redirect callback
  decision_cache: { sampled_cache_size: 1000000, non_sampled_cache_size: 1000000 }  # late spans follow the decision
  policies:
    - { name: errors, type: status_code, status_code: { status_codes: [ERROR] } }
    - { name: slow, type: latency, latency: { threshold_ms: 2000 } }
    - name: baseline-on-sale
      type: and
      and: { and_sub_policy: [
        { name: on-sale, type: boolean_attribute, boolean_attribute: { key: encore.on_sale, value: true } },
        { name: one-pct, type: probabilistic, probabilistic: { sampling_percentage: 1 } } ] }
    - name: baseline-off-sale
      type: and
      and: { and_sub_policy: [
        { name: off-sale, type: boolean_attribute, boolean_attribute: { key: encore.on_sale, value: false } },
        { name: ten-pct, type: probabilistic, probabilistic: { sampling_percentage: 10 } } ] }
```

The first two lines are where Encore learned something. The sampler decides once `decision_wait` has passed since a trace's first span. Until the March incident of Section 5.5 the wait was the default 30 s, and that afternoon's slowest checkouts, which spent a median of 38 s waiting for a bank's callback, were judged before they had finished: some kept in fragments, some lost. The wait is now 60 s, which costs memory in proportion. The decision cache makes late spans follow their trace's decision, though a saga that pauses for minutes is still judged on partial evidence. And because a kept 1% trace stands for a hundred like it, counts over sampled traces must be weighted by sample rate.

Encore's telemetry costs about €40,000 a month, roughly 2 cents of every ticket's 12 cents of variable cost. Retention is deliberate: wide events, unsampled, for 14 days, which also limits how long fan identifiers are kept; sampled traces for 30 days; metrics for 13 months, long enough to compare this year's festival on-sale with last year's. Sampling is aggregation made with a budget, and the policy above tries to keep every row Snow would have wanted and only a sample of the ordinary requests where nothing went wrong. Figure 5.1 draws the whole pipeline.

{% include diagrams/fig-5-1.svg %}

*Figure 5.1 — Encore's telemetry pipeline. Agents only batch and forward; the gateway tier redacts, routes and, in the tail sampler, decides what the bill will be.*

**Recap.** Signals earn their value through shared context, made concrete by trace IDs in logs and exemplars on metrics. Semantic conventions, extended by an owned registry, make queries portable across teams. Tail sampling keeps the interesting traces, provided its policies combine as intended, it waits long enough, and its counts are weighted afterward.

**Exercise 5.2.** Pick three services you depend on and find what each calls the HTTP status, the tenant or customer, and the deployed version. How many distinct names did you find for each, and which incident query would have failed because of them?

### 5.3 Distributed Tracing in Practice

#### One fan's purchase {#one-fans-purchase}

A **trace** is the record of one request's journey through a system, as a tree of **spans**, each a timed unit of work with a name, a parent and attributes. Google's Dapper paper of 2010 described it at scale, and Zipkin, Jaeger and now OpenTelemetry brought it into open source. Here is one fan's purchase:

| Span | Service | Start (ms) | Duration (ms) | Notable attributes |
|---|---|---|---|---|
| `POST /checkout` | API gateway | 0 | 1,140 | `encore.event_id=evt_7f3a`, `encore.tenant_id=encore` |
| `admission.verify` | Sale Gate | 4 | 12 | token valid, queue wait in linked trace |
| `bot.score` | Bot Screening | 18 | 35 | `bot.verdict=allow` |
| `inventory.Hold` (gRPC) | Seat Inventory | 56 | 48 | `encore.shard=2`, `seat.count=2` |
| `saga.purchase` | Orders | 108 | 1,020 | Temporal workflow |
| ↳ `psp.authorize` | Orders (anti-corruption layer) | 150 | 640 | `encore.payment_method=card`, `psp.attempt=1` |
| ↳ `inventory.Sell` | Seat Inventory | 830 | 31 | appends `SeatSold` |
| `ticket.issue` | Notification | +4,200 | 380 | linked from `SeatSold`, not a child |

*Figure 5.2 — One fan's purchase as a trace. The PSP takes 640 ms of its 800 ms share of the 3 s checkout budget; ticket issuance runs asynchronously and is joined to the purchase by a span link.*

Drawn to scale, as in Figure 5.3, the trace shows where the checkout's 1,140 ms went.

{% include diagrams/fig-5-3.svg %}

*Figure 5.3 — The trace of Figure 5.2 as a waterfall, against the 3 s budget. The PSP call is most of the checkout; ticket issuance, four seconds later, hangs off the purchase by a link.*

Three things in it took deliberate work.

#### Context propagation {#context-propagation}

A trace exists only because each hop passes the trace context to the next. Over HTTP and gRPC that context travels in the `traceparent` header standardized by the World Wide Web Consortium (W3C) as Trace Context, and OpenTelemetry reads and writes it automatically. The mesh cannot carry context *through* a service: if Orders makes an outbound call on a fresh thread without passing the context along, the trace breaks in two. As Yuri Shkuro, who built Jaeger at Uber, makes clear, the hard part of tracing is getting every hop, through every thread pool and callback, to carry a few bytes of context. Encore's service template therefore ships an integration test that fails the build if any outbound span lacks a parent; it cannot reach every thread pool, but it catches the common slip.

The same context can carry **baggage**, key-value pairs that ride along with the trace. Encore puts `encore.event_id` and `encore.tenant_id` in baggage at the gateway, and the template's baggage span processor copies them onto every span, which OpenTelemetry does not do by itself. Baggage is visible to every hop and has no integrity protection, so it holds identifiers, never secrets or personal data, and Encore's egress proxy strips it before any call leaves for the PSP.

#### Span design {#span-design}

What deserves a span is the tracing version of what deserves a function: a unit of work someone might reason about on its own. Encore follows common practice: a span for every network call, queue publish and consume, lock or lease, and every decision that changes the request's path (a bot verdict, a cache miss, a retry), with *attributes* for everything else, because the attributes are what we will later group by.

#### Queues, sagas and asynchronous work {#async-tracing}

The last row of Figure 5.2 is the hard case. The `SeatSold` event leaves Seat Inventory on the `ticket-sales.v2` stream, and Notification consumes it four seconds later. As a child of the checkout span, `ticket.issue` would make the checkout appear to take five seconds; as an unconnected trace, it would leave the fan who says "I paid and never got my ticket" unfollowable. OpenTelemetry's answer is the **span link**: the producer writes the trace context into the event's headers, and the consumer starts its own trace whose first span *links* to the producer's span without claiming it as a parent. The same device joins a fan's minutes in the waiting room to the purchase that follows; links are stable in the specification, though backends differ in how well they let us walk them.

A Temporal saga may pause for a PSP callback and resume minutes later on a different worker, so Encore records each activity as its own span through Temporal's tracing interceptors and carries the workflow ID on all of them, which keeps them findable even when the tail sampler has judged their trace early.

**Recap.** A trace is only as complete as its weakest propagation point, so propagation is tested in the build, and baggage is copied deliberately and stripped at the edge. Spans mark units of work, attributes carry the detail we will query, and span links join asynchronous hops while keeping latency honest.

**Exercise 5.3.** Follow one real request in a system you know from entry to its last asynchronous consequence. Mark each place where the trace breaks or lies about duration, and name the fix: propagation, a span link or an attribute.

### 5.4 Dashboards, Alerts, and Paging Discipline

#### Dashboards that argue {#dashboards-that-argue}

In 1858 Florence Nightingale drew the Crimean War's British dead as wedge-shaped monthly diagrams in which preventable disease dwarfed wounds. It was a chart with a thesis, for people who would never read the tables.

A good dashboard has a thesis too. Encore's on-sale dashboard answers one question, "are fans getting through and buying?", and so its top row is admissions per second against the admission rate, checkout success against the on-sale-window service level objective (SLO) from Chapter 4, and p99 checkout latency against the 3 s budget. Beneath it, each service shows rate, errors and duration (Tom Wilkie's RED method) and each resource its utilization, saturation and errors (Brendan Gregg's USE method). Most dashboards are instead walls of graphs left by past incidents. Encore asks each dashboard to name its question and owner, and deletes those unopened for 90 days, its own choice of number, sparing any linked from a runbook.

#### What deserves a page {#what-deserves-a-page}

Chapter 4 built the mechanics of alerting on burn rate; what remains is discipline. An alert is a request for a human being's attention, the one resource no autoscaler can add, and every page should be urgent, affect users or be about to, and need human judgment. [The Architecture book](https://oleksiyp.github.io/arch-book/#from-is-it-up-to-why-is-it-weird) stated the rule as paging on symptoms, with narrow exceptions; a cause earns a page when it predicts a symptom more reliably and earlier than the symptom could be measured. The seat ledger losing one of its three locations during an on-sale qualifies, since one more loss would leave no majority to commit a seat write. A certificate within a day of expiry qualifies only as a backstop: the real alert is a ticket three weeks earlier, and the page means that ticket was ignored. CPU at 85% predicts no symptom on its own, so it does not page.

| Signal | Destination | Example at Encore |
|---|---|---|
| SLO fast or medium burn | Page, immediately | Checkout budget burning at 14.4× over an hour, or 6× over six hours |
| SLO slow burn | Ticket, business hours | Seat-map latency budget 40% spent in 10 days |
| Predictive cause, harm certain | Page | A ledger replica or witness unreachable; certificate expiry under 24 h (ticket at 21 days) |
| Ordinary cause | Dashboard only | CPU, pod restarts, queue depth within capacity |
| Business anomaly | Owning team's channel | Sales for one event far below forecast |
| Telemetry silent | Page, from outside | Watchdog heartbeat missing; Collectors refusing or dropping spans |

*Figure 5.4 — Where signals go. Only the pages wake anyone; the rest wait for daylight or for a question.*

The last row guards against failures in observability itself, which are the hardest kind for it to see. A Collector that has stopped forwarding raises no errors, and flat dashboards look very much like health. Encore uses the Prometheus community's **dead man's switch**, an alert that always fires so that the paging service raises the alarm when it *stops*, and alerts on the Collectors' counts of refused and dropped spans.

#### Alert fatigue {#alert-fatigue}

Hospitals learned this cost before software did. Monitors that beep at every transient reading teach nurses, rationally, that beeps do not mean danger. The Joint Commission, which accredits American hospitals, issued a formal warning about alarm fatigue in 2013, citing estimates that 85% to 99% of alarms needed no clinical intervention. An engineer paged nightly for causes that resolve themselves learns the same lesson. The parallel breaks where software has the advantage: a hospital cannot delete the monitor on a patient's heart, but we can delete an alert, and most teams delete far too few.

When Encore's Orders team reviewed its alerts last year, 40 of its 130 rules could page; over a quarter only 11 had led to any human action, and two had caught something before a fan noticed. The team kept 12 pages, each with a runbook link, and demoted the rest. The Reliability team now reviews every rotation's pages monthly with one question: what did the person who was woken actually do? A page whose honest answer is "acknowledged it and went back to sleep" goes at the next review.

**Recap.** Dashboards should make an argument, name their question and be pruned when it no longer recurs. A page must be urgent, user-affecting and actionable, predictive causes included when they warn earlier than the symptom could, and one page watches the telemetry itself. Alert fatigue is treated by deletion, reviewed against what responders actually did.

**Exercise 5.4.** Export a month of pages from a rotation you know. For each alert rule, record what the responder did. Propose deleting or demoting every rule whose answer was "nothing", and estimate the sleep it returns.

### 5.5 Asking Questions — High Cardinality, Exploration, and AI-Assisted Queries

#### Wide events {#wide-events}

The telemetry that makes new questions answerable is, in its simplest form, the **wide event**: one structured record per request per service, carrying every field that might matter, often a hundred or more; Stripe calls the habit canonical log lines. A checkout event at Encore carries the fan's country, the `encore.*` identifiers, the payment method, the PSP route, the build, the region, the feature flags and each step's duration. Charity Majors, Liz Fong-Jones and George Miranda, in *Observability Engineering*, argue that such events are the fundamental unit of observability and metrics cheap aggregates derived from them. That is one school of thought; Encore keeps metrics for the questions it asks every minute and wide events for the ones it has not thought of yet.

#### The core analysis loop {#core-analysis-loop}

The same authors describe a method they call the **core analysis loop**: start from the signal that something is wrong, isolate the requests that show it, compare them with those that do not across every dimension at once, let the dimensions that differ most suggest the next filter, and repeat. It is Snow's method made mechanical. Like Snow's map, the loop finds correlates, and someone must still explain the mechanism; and it needs data that is unsampled or weighted by sample rate, which is why Encore runs it on wide events.

One March afternoon, Encore's support team relayed that payments from the Netherlands were "hanging" after the bank page. The checkout SLO barely moved, since Dutch fans are a small share of traffic; this was a gray failure, plain to the fans and invisible to the averages. The incident channel's first instinct was the PSP, which had been the suspect since Encore's first outage. But the `psp.authorize` spans were normal, about 180 ms. So the on-call engineer ran the loop: select checkouts slower than 3 s since 13:00, compare them with the rest. The slow ones began abruptly at 14:02.

| Dimension | Slow checkouts (since 13:00) | All other checkouts |
|---|---|---|
| `encore.country=NL` | 81% | 6% |
| `encore.payment_method=bank_redirect` | 97% | 14% |
| Time in `saga.await_callback` | 38 s (median) | 2.1 s (median) |
| `encore.gateway.rule=psp-callback-ratelimit` | 95% | under 1% |
| `encore.tenant_id`, `encore.shard`, `service.version` | no difference | — |

*Figure 5.5 — The core analysis loop on "Dutch fans' payments slow since 14:02". Country was the symptom; the payment method was the mechanism; the gateway rule was the cause.*

Most Dutch fans pay by bank redirect, which the PSP confirms by a later callback. At 14:02 the Bot Screening team had shipped a reasonable change to the API gateway, a per-source rate limit on unauthenticated POSTs, and the PSP's callbacks arrive from a handful of addresses. They were throttled, retried with backoff and delivered tens of seconds late. The fix, an exemption for the PSP's signed callbacks, took four minutes; finding the cause took 25, nearly all spent on the theory everyone already held. A rule meant to stop bots had begun to punish ordinary retry behavior, an interaction this book will meet again.

High cardinality alone did not solve this. A country, a handful of payment methods and a few dozen gateway rules would all fit comfortably as metric labels. What no metric had was the combination, and the decisive field existed at all only because someone had decided that every policy decision deserved an attribute. The truly high-cardinality fields, tenant, shard and version, showed no difference, and so ruled out a bad deploy and a hot shard at a glance.

#### Asking Cue {#asking-cue}

Assistants that query telemetry in plain language are young practice, and the evidence favors a narrow use. The best published production account is Honeycomb's, of the Query Assistant it shipped in 2023, which turns a question in English into a query the user sees, edits and runs. Honeycomb reported wide adoption and more complex querying among its users, a correlation it did not oversell, and wrote as frankly about the failures, from schemas too large for the model's context to prompt injection. Diagnosis is harder. Meta reported in 2024 that its model for ranking the code change likely behind an incident put the right one in its top five about 42% of the time, and that it withholds low-confidence suggestions and requires each to be explainable.

Cue, the operations agent of Section 3.5, read-only by default, queries telemetry through the company's Model Context Protocol (MCP) server, and the March investigation was replayed with it. Asked "why are Dutch payments slow since 14:02?", Cue answered in seconds, fluently, and wrongly. It found two postmortems blaming the PSP and concluded that the PSP was degraded for Dutch banks: the prevailing theory, now with citations. Asked instead to "compare checkouts slower than 3 s since 13:00 with the rest, across all attributes," it ran the core analysis loop faster than any human and returned Figure 5.5 almost exactly.

A confident wrong answer is more expensive than a slow right one, because it ends the search. A model that reasons from past incidents tends to reproduce the team's prevailing theory just when someone needs to question it, as Snow did, a tendency Encore has seen in its replays and Meta's caution anticipates. Encore's rule is therefore to show the query and not to trust the diagnosis: every answer from Cue must carry the query that produced it, so that a human can rerun it, and an answer without one is treated as a rumor. The other limit, the one Honeycomb met, is vocabulary: in the replay Cue first missed the gateway rule because the gateway emitted it as `policy` while the registry said `encore.gateway.rule`. A human at 3 a.m. works around such a slip; an assistant cannot. The registry check of Section 5.2 now fails on the mismatch.

Used this way, an assistant is a tireless research clerk, of the kind Whitehead might have welcomed for knocking on doors; choosing which doors to knock on is still the engineer's work. Chapter 12 shows Cue in a live incident.

**Recap.** Wide events let us compare failing requests with healthy ones on every dimension at once, which is the core analysis loop and Snow's method in one. The prevailing theory is the usual obstacle, and AI assistants tend to repeat it fluently. The practice is young, and the evidence supports assistants that write and show queries over consistently named telemetry far more than assistants that diagnose.

**Exercise 5.5.** Take a recent investigation and rerun it as a comparison: the failing requests against the rest, across every attribute you have. Which attribute would have found the cause soonest, and was it present, consistently named and kept long enough?

### Kata: The Charging Network

> **Your brief: "Lumen."** Lumen runs 18,000 electric-vehicle chargers in six countries, with a driver app, roaming partners and two PSPs. Sessions pass through authorization, the charger (over cellular), metering and billing, and can last hours. Lumen has 35 engineers, spends €70,000 a month on telemetry (two-thirds of it logs, most never read), and has 600 alert rules that page its rotation about 90 times a week. More than half of failed sessions are first reported by drivers on social media, and a roaming partner has threatened to leave over unexplained authorization failures that Lumen's dashboards show as healthy.

**Deliverables:**

1. **Attribute registry** — the 15 attributes every span and event must carry (charger, site, firmware, roaming partner, country among them), aligned to the OpenTelemetry conventions.
2. **Trace design** — one charging session traced from app tap to invoice, with asynchronous hops joined by span links, and the propagation points most likely to break.
3. **Pipeline and sampling policy** — Collector topology, tail-sampling policies that combine as intended, a decision wait that respects hours-long sessions, redaction of driver data, and a retention plan that cuts spend by a third, naming the questions each cut makes unanswerable.
4. **Paging set** — at most ten pages, each tied to an SLO burn or a predictive cause, plus a telemetry heartbeat, with the deleted rules and why.
5. **Investigation script** — the core analysis loop applied to the roaming partner's complaint: which dimensions you would compare, and why.
6. **Assistant policy** — what an AI query assistant may do with Lumen's telemetry, and what evidence its answers must show.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Askability | Could an engineer answer "which firmware on which partner's chargers fails authorization since Tuesday?" with one query? |
| Vocabulary | Are names consistent across services, owned, and checked by CI rather than by goodwill? |
| Honest sampling | Does the policy keep every failure, cope with long sessions, and say plainly what the cuts give up? |
| Respect for attention | Would you accept being woken by each page on the list? |
| Method over theory | Does the investigation compare failing with healthy sessions before it names a suspect? |
| Grounded assistance | Must the assistant show its query, and can a human rerun it? |

#### Where you now stand

You can now design for observability: wide events with an owned vocabulary, traces that survive queues and sagas, a pipeline that samples with intent and watches itself, dashboards that argue and pages that respect sleep. You can run the core analysis loop and judge an assistant that runs it for you. What the telemetry has begun to show, in latency curves that bend under load and a bill that tracks traffic, is the subject of Chapter 6: performance, capacity and cost, and the queueing theory Erlang began in 1909.

### References

- Charity Majors, Liz Fong-Jones, George Miranda — [*Observability Engineering*, 2nd ed.](https://www.oreilly.com/library/view/observability-engineering-2nd/9781098179915/). O'Reilly, 2026.
- Peng Huang et al. — [*Gray Failure: The Achilles' Heel of Cloud-Scale Systems*](https://www.microsoft.com/en-us/research/publication/gray-failure-achilles-heel-cloud-scale-systems/). HotOS, 2017 — free online.
- OpenTelemetry Authors — [*Tail Sampling Processor*](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/processor/tailsamplingprocessor/README.md). OpenTelemetry Collector Contrib — free online.
- OpenTelemetry Authors — [*OpenTelemetry Semantic Conventions*](https://opentelemetry.io/docs/specs/semconv/). OpenTelemetry project — free online.
- Yuri Shkuro — [*Mastering Distributed Tracing*](https://www.oreilly.com/library/view/mastering-distributed-tracing/9781788628464/). Packt, 2019.
- W3C — [*Trace Context*](https://www.w3.org/TR/trace-context/). W3C Recommendation — free online.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/monitoring-distributed-systems/), chapter 6. O'Reilly/Google, 2016 — free online.
- Phillip Carter — [*So We Shipped an AI Product. Did It Work?*](https://www.honeycomb.io/blog/we-shipped-ai-product). Honeycomb, 2023 — free online.
- Engineering at Meta — [*Leveraging AI for Efficient Incident Response*](https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/). Meta, 2024 — free online.
- Cindy Sridharan — [*Distributed Systems Observability*](https://www.oreilly.com/library/view/distributed-systems-observability/9781492033431/). O'Reilly, 2018.
- Benjamin H. Sigelman et al. — [*Dapper, a Large-Scale Distributed Systems Tracing Infrastructure*](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/). Google Technical Report, 2010 — free online.
- The Joint Commission — [*Sentinel Event Alert 50: Medical Device Alarm Safety in Hospitals*](https://www.jointcommission.org/-/media/tjc/documents/resources/patient-safety-topics/sentinel-event/sea_50_alarms_4_26_16.pdf). 2013 — free online.
- John Snow — [*On the Mode of Communication of Cholera*, 2nd ed.](https://archive.org/details/b28985266). John Churchill, 1855 — free online.

---

## Chapter 6: Performance, Capacity, and Cost {#ch6}

> Every queue is a wager that the future will be less busy than the present.

In 1908 a young Danish mathematician named Agner Krarup Erlang joined the Copenhagen Telephone Company, and the company asked him a question that sounds like bookkeeping and turned out to be a science: how many lines, and how many operators, does a city need? Too few, and callers hear a busy tone; too many, and copper and wages sit idle through every quiet afternoon. In 1909 Erlang showed that calls from many independent subscribers arrive as a Poisson process, random but describable, and by 1917 he had derived formulas for the chance that a call would be refused when every line was busy, and for how long it would wait if held in line instead.

The profession honored him by turning his name into a unit. One **erlang** is the traffic that keeps one server continuously busy, and a system's offered load in erlangs is its arrival rate multiplied by the mean time each arrival holds a server. A switchboard offered 30 erlangs needs more than 30 lines, and how many more depends on how long callers will tolerate waiting. Performance, capacity and cost are one problem seen from three sides.

Before a big on-sale, Encore's fans gather in the Sale Gate, the virtual waiting room, which admits about 1,200 fans per second per event. Behind it sits Seat Inventory, the ledger that sells each seat exactly once, split for a large event into four shards, each a small consensus group whose elected leader orders every seat write. [The Architecture book](https://oleksiyp.github.io/arch-book/#43-scalable-service-architectures) chose those numbers; this chapter explains them, building on the SLOs of Chapter 4 and the instruments of Chapter 5. (Chapter 1's [map of Encore](/prodsys-book/ch/1/#encore) shows where each piece sits.)

### 6.1 Performance Methodology — USE, RED, and Latency Distributions

#### Two checklists, two points of view {#two-checklists}

Most performance investigations fail because they begin with a hunch. Someone suspects the database, looks there, finds something mildly alarming (there always is) and tunes it; Brendan Gregg called this the streetlight method, after the drunk who searches for his keys where the light is. Gregg's **USE method**, published in 2012, answers this. It asks three questions of every resource: its **utilization** (the fraction of time it was busy), its **saturation** (how much work is queued waiting for it) and its **errors**. Resources are anything that can run out, including connection pools, file descriptors and the ordered write log of a Seat Inventory shard, and the logical ones usually need instrumentation we add ourselves. The method is deliberately dull and exhaustive, so it finds the problem we did not suspect.

Tom Wilkie's **RED method** looks from the request's side, asking of every service its **rate**, its **errors** and its **duration** (the distribution of time each request takes). It descends from the four golden signals of Google's site reliability engineering (SRE) book and maps onto the service level indicators (SLIs) of Chapter 4, though batch jobs and stream processors need other signals, such as lag. RED shows where users feel the problem, and USE shows which resource is causing it. An Encore engineer paged on a seat-map burn rate begins with RED for the seat-map service, then walks USE down the resources behind it.

#### Latency is a distribution {#latency-is-a-distribution}

Duration is the signal most often mismeasured. A service's latency is a distribution, usually skewed and often with two humps for cache hits and misses, and the **percentile** pN is the value below which N% of requests completed. A seat-map service whose mean is 120 ms can have a p99 of 2 s, and the fan who waited 2 s does not experience the mean (Figure 6.1).

{% include diagrams/fig-6-1.svg %}

*Figure 6.1 — A seat-map service's latency, on a log scale. The mean falls in the valley between the cache hits and the misses, where almost no request lands; the p99 lives in the misses' long tail.*

Two habits follow. First, percentiles do not aggregate: the p99 of a service is not the average of its pods' p99s. We compute them from merged histograms, whose bucket layout limits precision; exponential histograms reduce that error. Second, we read the tail in proportion to the fan-out. When a purchase calls 20 backends in parallel and waits for all of them, the chance that every one answers faster than its own p99 is 0.99 to the twentieth power, about 82%, so nearly one purchase in five waits on the slowest 1% of at least one backend. It takes about 70 backends before a backend's p99 becomes the purchase's median; ["The Tail at Scale"](https://oleksiyp.github.io/arch-book/#tails-not-averages) gives 63% for a fan-out of 100.

There is a subtler trap, which Gil Tene named **coordinated omission**: a measurement error in which the load generator waits for each response before sending the next request, so that requests that *would* have arrived during a stall are never sent and never measured. A closed-loop benchmark can report a p99 of 40 ms for a system that froze for 2 s, because it stopped sending during the stall. Bianca Schroeder and her colleagues showed in 2006 how far such closed models diverge from open ones, in which arrivals keep their own schedule, as fans and Erlang's callers do. Latency must be timed from when each request was meant to be sent.

**Recap.** Methods beat hunches because they cover the system whether or not we suspected the right part; RED describes what requests experience and USE what resources endure. Latency is a distribution, measured with merged histograms, read at the percentile that matches the fan-out, and taken from load that arrives on its own schedule.

**Exercise 6.1.** For one service you own, list every resource the USE method should cover, including pools and logical limits. For how many can you produce utilization, saturation and errors today? Then work out what fraction of your busiest request type touches at least one backend's p99.

### 6.2 Queues, Load, and the Universal Scalability Law

#### The hockey stick {#the-hockey-stick}

Erlang's deepest lesson lies in the shape his formulas draw. When requests arrive at random and take varying times to serve, a server busy only part of the time still makes some of them wait, and the wait grows faster than the load. For the simplest model (random arrivals, random service times, one server), the mean **response time**, waiting plus service, is the service time divided by one minus the utilization. At 50% utilization a request takes twice its service time; at 80%, five times, four of them spent in the queue; at 90%, ten; at 99%, a hundred. The curve is flat for a long while and then turns upward like the blade of a hockey stick. Real systems differ from the model in every detail but share its shape, and the shape is what we use.

J. F. C. Kingman sharpened the point in 1961: for a single server under heavy load, the expected wait grows with the variability of arrivals and service times as well as with ρ/(1−ρ). An on-sale's arrivals are as bursty as traffic gets. Utilization is what the machine feels and queueing delay what the fan feels, and they diverge most when the business is busiest. Figure 6.2 draws both curves.

{% include diagrams/fig-6-2.svg %}

*Figure 6.2 — Response time against utilization for one server with random arrivals, and the steeper curve that burstier arrivals draw. Encore's write shards are planned at 80%; the same curve explains why a hot shard at 96% hurts so much more than 16 points should.*

Every motorway at rush hour draws the curve, and many cities answer with ramp metering, a light on the on-ramp that admits cars at the rate the motorway can absorb, keeping the main road below its knee at the cost of a visible wait on the ramp. The Sale Gate is a ramp meter, and its 1,200 fans per second is the green-light interval. Metering also, as Kingman's formula predicts, strips much of the burstiness from the arrivals the shards see. The Gate's own edge runs as serverless functions, pre-warmed before each on-sale and able to grow to 400 instances, because a waiting room that collapses under its own crowd is worse than none. The analogy breaks in one useful place: a driver held at the ramp cannot return a minute later as a second car, whereas a refused fan can and does retry, which Chapter 9 takes up. Erlang's later formulas add one more lesson: at the same utilization a large pool waits far less than a small one, so carving capacity into cells costs headroom.

#### How far will it scale? {#how-far-will-it-scale}

Queueing describes one resource. Scaling asks what happens when we add more of them, and most teams answer empirically, load testing until the system stops improving and reading the knee off the graph. Neil Gunther's **Universal Scalability Law** (USL) is a small model for interpreting those points, used mostly by capacity planners in his tradition and in database performance practice, where Baron Schwartz and the MySQL community applied it widely. It describes relative capacity C(N) at concurrency N with two penalties:

```
C(N) = N / (1 + σ(N−1) + κN(N−1))
```

The **contention** coefficient σ is the fraction of work that must be serialized; with κ at zero the law reduces to Amdahl's law of 1967, and throughput approaches a ceiling of 1/σ. The **coherency** coefficient κ is the cost of keeping parallel workers consistent with one another, which grows with the number of pairs of workers; it makes throughput peak and then *fall* once N passes √((1−σ)/κ). Gunther calls this retrograde scaling.

In Seat Inventory, each shard leader appends to a single ordered log, which is contention, and colliding holds on the same popular seats retry, which is coherency. The Inventory team fitted the USL to a single-shard load test at six concurrency levels:

| Concurrent writers N | Measured writes/s | USL fit (σ 0.03, κ 0.0005) |
|---|---|---|
| 1 | 121 | 120 |
| 4 | 431 | 438 |
| 8 | 790 | 775 |
| 16 | 1,210 | 1,223 |
| 32 | 1,570 | 1,583 |
| 64 | 1,540 | 1,565 |

*Figure 6.3 — The USL fitted to one Seat Inventory shard. Peak throughput falls near 44 concurrent writers; beyond that, more concurrency buys less.*

The fit, drawn in Figure 6.4, says three things. The shard peaks at roughly 1,630 writes/s near 44 writers, so the published 1.5k writes/s is a measured ceiling with a little margin. Raising the concurrency cap above 32 gains almost nothing, so the cap belongs in configuration review. And more write capacity means more shards per event, a design change no tuning knob can stand in for. These conclusions hold only under stated conditions: a measured point at a concurrency of one, a steady workload with a fixed mix, and no extrapolation far beyond the largest N measured. It predicts throughput, not latency, and must be refitted when the code changes.

{% include diagrams/fig-6-4.svg %}

*Figure 6.4 — The USL fit of Figure 6.3 against linear scaling and Amdahl's law. Contention alone would bend the curve; coherency turns it over, and the concurrency cap of 32 sits just below the peak.*

**Recap.** Response time rises with utilization along a hockey stick, steepened by variability, and admission control keeps a system below its knee and smooths its arrivals, at the cost of a visible queue. Load tests find where scaling stops, and the USL, where its conditions hold, explains why.

**Exercise 6.2.** Load test one component at four to six concurrency levels, including a concurrency of one, and plot throughput against concurrency. Fit the USL to the points (a spreadsheet's solver will do). Is your current concurrency setting on the rising or the falling side of the peak?

### 6.3 Capacity Planning and Load Testing

#### On-sale arithmetic {#on-sale-arithmetic}

Capacity planning begins by choosing the **unit of capacity**, the measurable quantity that actually limits the business workload, which is rarely processor time; Arun Kejariwal and John Allspaw insist on finding its ceiling by measurement. For Encore during an on-sale it is ordered seat writes per shard, because writes are serialized and stop scaling, and a delayed seat write is a fan who cannot buy. A fan admitted by the Gate spends about three minutes in seat selection and checkout, within the 5-minute hold, and generates about four ordered writes (a first hold, often a second after losing a seat, the sale, and the release or expiry of an abandoned hold) and about 26 availability reads. With steady admission, the shards see the admission rate multiplied by the per-fan demand:

| Quantity | Per fan | At 1,200 fans/s | Capacity, four shards | Utilization |
|---|---|---|---|---|
| Ordered writes | ~4 | 4,800/s | 6,000/s | 80% |
| Availability reads | ~26 | 31,200/s | 40,000/s | 78% |
| Fans in session | ~180 s | ~216,000 | — | — |

*Figure 6.5 — Encore's on-sale capacity arithmetic. Writes bind first, and the admission rate is set so that they sit at 80% of the shards' rated capacity.*

The last row applies Erlang's unit to today's fans: 1,200 arrivals a second, each holding a session for 180 s, is an offered load of 216,000 erlangs of fans, Little's law applied to people. At 80% of rated capacity, the mean response time of a seat write is about five times its service time, a few milliseconds that the 3 s checkout budget absorbs easily. No standard prescribes 80%; it is a rule of thumb, defensible because the resulting wait fits the budget. The remaining 20% looks idle on a cost report, and it has two jobs.

The first is skew. Front-floor sections sell first and hottest, so if the busiest shard takes 30% of writes instead of 25%, it runs at 96%, and its response time climbs toward 25 times service time. The second is failure. When a shard leader's node is drained or dies, a new leader is elected in the same region, and the fencing that keeps a seat from being sold twice also rejects writes on that shard for about 40 s. Fans whose holds failed try again, so a shard carrying its even share of 1,200 writes a second comes back with a backlog of about 48,000 writes. With 300 writes a second to spare, the new leader drains that backlog in under three minutes, running at its ceiling all the while; the hot shard, with 60 to spare, would need more than a quarter of an hour. Google's SRE book plans for N+2, enough to lose one unit to maintenance and another to failure, and Amazon's Well-Architected framework calls the idea static stability. Encore's version is that every shard's headroom must be able to absorb the backlog of a failover. Headroom is the price of a short queue, paid in advance.

#### Load tests that resemble Friday {#load-tests-that-resemble-friday}

The per-fan numbers come from load tests. Encore's harness, which the On-Sale team calls Soundcheck, replays recorded on-sales, scrubbed of personal data, against a production-sized copy of the purchase path. It generates load from an **open model** (k6's arrival-rate executors) and fails any run in which the generator dropped scheduled arrivals, since dropped arrivals mean coordinated omission has reappeared in the rig. Its arrivals are bursty, because Kingman's variability term is real. Its seat choices are skewed toward the best sections, because uniform random seats understate the hot shard. And it stubs the payment service provider (PSP) with a latency distribution taken from production, because the first outage in [the Architecture book](https://oleksiyp.github.io/arch-book/#anatomy-of-a-self-inflicted-outage) began with a PSP that slowed down.

Even a faithful copy is not production. Shopify has written about running its Black Friday scale tests against production infrastructure, and Hotstar's engineers about load-testing at the full scale of a cricket audience. Encore does the same twice a year, running Soundcheck at off-peak hours against the hidden test event that Encore's synthetic buyers already use. The load generators may run on spot capacity; the system under test does not.

One lesson concerns state rather than traffic. A load test run twice measures the second run against a system the first has warmed, while on-sale morning is often the first run. At Encore the clearest case is the seat-map geometry cache, which holds each venue's layout but never which seats are free; cold, it sends every miss to Catalog at the worst possible moment. A touring band soundchecks in an empty arena, knowing the room will sound different at nine o'clock, when 15,000 bodies absorb the reflections. The analogy breaks in a direction that should worry us, since the hall grows kinder when full and a cold cache does not. Every test plan must say which state it assumed, and the cache is warmed before the doors open.

#### The Wednesday review {#the-wednesday-review}

The arithmetic feeds the on-sale readiness review, which the Reliability team holds the Wednesday before each big on-sale, a launch review of the kind Google's SRE book describes, covering capacity, dependencies and who will be on call. A proposal to raise the admission rate must arrive with the arithmetic redone and a load test at the new point, and the review asks what cache state that test assumed. It also checks the limits that belong to someone else: the cloud account's function concurrency behind the Gate (Chapter 7 tells how Encore learned that one), load balancer limits and the PSPs' agreed request rates. Forecasts go in advance to any provider the night depends on, a practice Amazon formalizes as Infrastructure Event Management. The core of the checklist fits on a card:

```
On-sale readiness — Wednesday, T-2 days
[ ] Admission rate unchanged, or new arithmetic + load test attached
[ ] Load test: open model, bursty, skewed seats, cache state stated
[ ] Writes per shard ≤ 80% at planned rate; failover drain < 5 min
[ ] Pre-scale plan: Gate concurrency, Inventory floors, cache warm
[ ] Quotas: function concurrency, LB, PSP rates ≥ 1.3 × forecast peak
```

**Recap.** We plan capacity in the unit that limits the business and keep headroom for skew, variability and the failover that will eventually come. Load tests use open, bursty arrivals, realistic skew and dependency latency, state their cache state, and are confirmed at production scale. Before a scheduled peak, the limits other people set are checked as carefully as our own.

**Exercise 6.3.** Write your system's equivalent of Figure 6.5 for its busiest hour. Then compute how long your binding resource would take to drain the backlog of its own failover at that utilization, and find whether your last load-test report says whether caches were warm or cold.

### 6.4 Autoscaling and Elasticity

#### The lag in the loop {#the-lag-in-the-loop}

Autoscaling promises to remove capacity planning, but in practice it removes only the need to plan for demand that changes slowly. An autoscaler is a feedback loop, and like every loop it acts on the past. A metric must rise and be scraped, a stabilization window must pass, a pod must be scheduled (perhaps on a node that must first be bought), the image pulled and the instance warmed. Each step is seconds; together they are often minutes, and an on-sale that rises 500× in minutes is past its first surge before the loop has completed one cycle.

Pilots learn the same lesson from their engines: a turbofan at idle takes several seconds to spool up, so the stabilized approach is flown with the engines already spooled. Encore's equivalent is pre-scaling: the curtain-up workflow of Chapter 3 raises the Gate's provisioned concurrency toward its 400 instances, sets Seat Inventory's floors and warms the seat-map cache before the doors open. Hotstar's engineers reached the same conclusion for cricket, writing that capacity must be in place ahead of the match. The analogy breaks at the end of the flight: a pilot lands and shuts down, while a service must also scale down, with its own hazards of draining connections and a late second wave of fans.

Reactive scaling still has its place for unscheduled demand, and it fails in three characteristic ways. It can **lag**, as above. It can **thrash**, up on a burst, down in the lull and up again, which stabilization windows, asymmetric policies and floors damp (Kubernetes by default scales up at once and waits five minutes to scale down); Chapter 7 treats this as a problem of control loops. And it can **amplify**. In the first outage in [the Architecture book](https://oleksiyp.github.io/arch-book/#anatomy-of-a-self-inflicted-outage), the PSP slowed from 200 ms to 8 s, health checks failed and the autoscaler, reading distress as a need for capacity, added instances that opened still more connections to the bottleneck. The autoscaler can only buy what the dependency can sell.

#### Scaling on the right signal {#scaling-on-the-right-signal}

The defense is to choose the scaling signal as carefully as an SLI. Central processing unit (CPU) utilization suits work that really is computation, but a service blocked on a slow dependency is idle on CPU and saturated on everything else. Concurrency in flight and queue depth track waiting work more directly, and Kubernetes' Horizontal Pod Autoscaler (HPA), KEDA and Knative can scale on them. They carry their own hazard: concurrency rises when a dependency slows, so a concurrency-driven autoscaler will chase a sick PSP exactly as the old one did unless something stops it.

That something is a ceiling. Kubernetes requires every HPA to declare a maximum, and most teams pick it by feel. Encore derives it from the arithmetic of Figure 6.5, so no service can scale past what the shard behind it can absorb, and the Wednesday review rechecks it whenever either side changes; connection pools and client-side concurrency limits do the same job one layer down. Anyone who calls a system elastic should be able to name its slowest-scaling component.

**Recap.** An autoscaler is a delayed feedback loop that can lag, thrash or amplify. We pre-scale for the peaks we can foresee, scale reactively on signals that measure waiting work, and cap every service at what its dependencies can absorb, because any signal that rises with a slow dependency will otherwise feed it.

**Exercise 6.4.** For one autoscaled service, measure the time from a load step to a new instance serving at full speed, and compare it with how fast your steepest real peak rises. What is the service's maximum, and what downstream limit justifies it?

### 6.5 FinOps — Cost as an Operational Signal

#### The night's settlement {#the-nights-settlement}

After every concert, the tour's manager and the promoter settle the night: ticket revenue against the hall, the crew and the local costs, show by show, so that nobody learns in December that the Tuesday shows lost money all year. **FinOps**, the practice of making cloud spend a shared, continuous responsibility of engineering and finance, is the settlement brought to software. [The Architecture book](https://oleksiyp.github.io/arch-book/#the-invoice-is-a-telemetry-stream) introduced its central move, cost per ticket sold; here we treat cost as a telemetry stream with its own anomalies and denominators.

J.R. Storment and Mike Fuller describe a lifecycle of Inform, Optimize and Operate, and the first is the hardest: spend must be allocated to owners through accounts, tags and labels, including shared Kubernetes nodes, which tools such as OpenCost apportion by request. Encore allocates a little over 90% of its bill per service and per tenant, about as far as mature practice gets, and shows the shared remainder as its own line.

Unit economics need care about denominators. The figure the Architecture book followed, drifting from €0.11 to €0.19, was the blended one, the month's whole bill divided by its tickets, and it mixed two causes. Part of the rise was real inefficiency (a metrics forwarder billed per invocation at about €9,000 a month, verbose logging). Part was a larger Encore, with a second serving region and new tenants, spread over a quiet quarter. Encore now reports two figures: the fixed monthly cost of being open for business, and the **variable cost per ticket**, the spend that moves with tickets sold. The split is approximate, because much cloud spend is step-fixed, flat until a threshold and then a whole new node or shard, and someone must decide where each step belongs. After the forwarder fix the variable cost stands at €0.12 (Figure 6.6); in a typical month the fixed line adds about four cents, so the Architecture book's blended figure would now read about €0.16.

| Line item | Variable cost per ticket | Notes |
|---|---|---|
| Purchase-path compute (Gate, Inventory, Orders) | €0.041 | pre-scaled peaks billed while warm |
| Data stores and replication | €0.029 | includes the seat ledger's replicas in both regions and its witness in a third |
| Telemetry (metrics, logs, traces) | €0.022 | sampling policy reviewed quarterly |
| Network egress | €0.011 | wallet delivery and partner API |
| AI gateway tokens (support assistant, refund agent) | €0.006 | most turns routed to a cheaper model, guarded by evals |
| Other | €0.011 | build pipelines, preview environments, shared tooling |
| **Total** | **€0.12** | |

*Figure 6.6 — Encore's variable cost per ticket after the forwarder fix. Tokens are one line among six; they get the same treatment as the others.*

A rising variable cost is an engineering signal, a design that grew less efficient; a rising fixed cost with flat volume is a planning signal, capacity bought for demand that did not come. The first kind is found in code, and continuous profiling, which Google described in 2010 as sampling the stacks of every production machine all the time, tells a team which change made a request more expensive.

The token line is the youngest. It can be attributed only because every model call passes through Encore's AI gateway, which tags it with feature, tenant and model. Three levers move it, unequally mature. Batch interfaces, priced by the large providers at about half the interactive rate, suit work that can wait, such as nightly summaries of support tickets. Prompt caching, also a priced provider feature, makes the long unchanging instructions at the front of every assistant turn cheap to resend. Routing most turns to a model at about a tenth of the price is less proven; the best published account, RouteLLM (2024), reports large savings on benchmarks, and production accounts are few. Encore routes about 80% of turns that way only because each routing rule must hold its score on the 200-conversation golden set of Chapter 14 before it ships.

#### Commitments and anomalies {#commitments-and-anomalies}

Storment and Fuller distinguish *using less*, which is engineering, from *paying less*, which is purchasing. Commitments (reserved instances, savings plans) trade a promise of steady spend for a lower rate, on-demand promises nothing, and spot is cheapest and can be reclaimed at short notice. The portfolio follows the shape of demand: commit to the floor that runs all year, pay on demand for scheduled peaks, and put interruptible work, such as batch analytics and Soundcheck's load generators, on spot. Encore commits about 60% of its steady compute, less than the 70–90% many practitioners aim for, by choice: its floor is still moving as workloads shift between containers and functions, and committing to capacity it will soon stop using would lock in a forecast error. It revisits the figure quarterly, once the next on-sale calendar is known.

Cost anomaly alerts are built like the burn-rate alerts of Chapter 4, on a forecast of spend, with one difference: billing data arrives eight to 24 hours late, so detection works in hours. Most organizations route cost anomalies to tickets or chat. Encore's choice is a little sharper: a spend rate that would exhaust the month's budget in a week sends an urgent notification to the owning team during business hours, and a sudden step in a team's line opens a ticket. A cost regression accumulates silently until someone looks, as the forwarder's €9,000 a month did.

There is also a judgment no dashboard makes for us. The 20% of write headroom in Figure 6.5 appears on the bill, where a well-meaning optimization pass could propose to remove it, not knowing that it absorbs the backlog after a failover. The cheapest configuration and the safest are seldom the same, and the difference between them is a decision about risk. I have come to believe that the most useful thing FinOps does is to make that decision visible, so that it is made deliberately.

**Recap.** FinOps allocates the bill to owners, splits fixed from variable cost with judgment, and watches the variable cost per ticket as an engineering signal. Commitments follow the shape of demand, token cost is cut with proven levers before young ones, and cost is always read beside capacity, because headroom shows up on both.

**Exercise 6.5.** Split last month's cloud bill into fixed and variable costs, and compute the variable cost per business unit. Where did you put the step-fixed costs? What fraction of your steady compute is covered by commitments, and who decided that fraction, from what forecast?

### Kata: Filing Season

> **Your brief: "Ledgerline."** A tax-preparation SaaS in one EU country: 2.4 million filers a year, 35% of whom file in the final six days, peaking at 14× normal load on the last evening. Each filing runs a calculation engine (about 400 ms of compute, re-run on every edit) against a shared PostgreSQL cluster with one primary. Ledgerline has 30 engineers. Its closed-loop load tests, run on a staging cluster a quarter of production's size, reported a p99 of 180 ms, yet support logged thousands of complaints about 10 s waits on deadline night. Its CPU-based autoscaler oscillated every few minutes and twice exhausted the database's connection limit. The cloud bill rose 40% while filings rose 12%, and a new AI explanation feature has its own, unforecast token line.

**Deliverables:**

1. **USE and RED inventory** — the resources and services on the filing path, with the signals for each and the ones currently missing.
2. **Capacity model** — the unit of capacity for deadline night, per-filing demand, utilization on the binding resource at peak, and headroom for skew and a database failover, with the arithmetic shown.
3. **Scaling curve** — a load test of the calculation engine against the database at five or more concurrency levels, the knee identified and, if its conditions hold, a USL fit that explains it.
4. **Test and readiness plan** — an open-model test with bursts, skew and stated cache state, a production-scale check, a quota review, and an explanation of last year's 180 ms.
5. **Autoscaling policy** — the scaling signal, floors, pre-scaling schedule, stabilization settings and a maximum justified by the database.
6. **Cost plan** — fixed and variable cost per filing, commitments, anomaly alerts, and the token levers you would pull first.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Method over hunch | Would the inventory have found the connection-limit problem before deadline day? |
| Queueing literacy | Is headroom justified by the hockey stick, by skew and by failover, rather than by habit? |
| Honest measurement | Does the test plan make coordinated omission impossible, and is it confirmed at production scale? |
| Loop discipline | Can the autoscaler still amplify load onto the database under your policy? |
| Cost with denominators | Is the 40%-versus-12% gap explained per filing, split into fixed and variable cost? |
| Joint reading | Does any cost saving you propose remove headroom the capacity model needs? |

#### Where you now stand

You can now investigate performance by method, read latency in proportion to fan-out, explain why waits explode near saturation, plan capacity with room for skew and failover, rehearse a peak honestly, keep an autoscaler from amplifying trouble, and read the invoice as telemetry. Chapter 7 turns to the loops that run most of what we have measured here: the reconciliation engines of Kubernetes, serverless platforms and GitOps.

### References

- Brendan Gregg — [*Systems Performance*, 2nd ed.](https://www.brendangregg.com/systems-performance-2nd-edition-book.html). Addison-Wesley, 2020.
- Arun Kejariwal, John Allspaw — [*The Art of Capacity Planning*, 2nd ed.](https://www.oreilly.com/library/view/the-art-of/9781491939192/). O'Reilly, 2017.
- J.R. Storment, Mike Fuller — [*Cloud FinOps*, 2nd ed.](https://www.oreilly.com/library/view/cloud-finops-2nd/9781492098348/). O'Reilly, 2023.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Jeffrey Dean, Luiz André Barroso — [*The Tail at Scale*](https://doi.org/10.1145/2408776.2408794). Communications of the ACM, 2013.
- Bianca Schroeder, Adam Wierman, Mor Harchol-Balter — [*Open Versus Closed: A Cautionary Tale*](https://www.usenix.org/conference/nsdi-06/open-versus-closed-cautionary-tale). USENIX NSDI, 2006.
- Neil J. Gunther — [*Guerrilla Capacity Planning*](https://link.springer.com/book/10.1007/978-3-540-31010-5). Springer, 2007.
- Brendan Gregg — [*The USE Method*](https://www.brendangregg.com/usemethod.html). brendangregg.com — free online.
- Shopify Engineering — [*Performance Testing at Scale*](https://shopify.engineering/scale-performance-testing). Shopify — free online.
- Hotstar Engineering — [*Scaling Is Not An Accident*](https://blog.hotstar.com/scaling-is-not-an-accident-895140ac84c0). Hotstar — free online.
- Amazon Web Services — [*AWS Infrastructure Event Management*](https://aws.amazon.com/premiumsupport/programs/iem/). AWS — free online.
- FinOps Foundation — [*FinOps Framework: Unit Economics*](https://www.finops.org/framework/capabilities/unit-economics/). FinOps Foundation — free online.
- Gang Ren, Eric Tune, Tipp Moseley, Yixin Shi, Silvius Rus, Robert Hundt — [*Google-Wide Profiling*](https://research.google/pubs/google-wide-profiling-a-continuous-profiling-infrastructure-for-data-centers/). IEEE Micro, 2010.
- Isaac Ong et al. — [*RouteLLM: Learning to Route LLMs with Preference Data*](https://arxiv.org/abs/2406.18665). arXiv, 2024.
- Anthropic — [*Prompt caching*](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching). Anthropic documentation — free online.

---

## Chapter 7: The Runtime and Its Control Plane — Kubernetes, Serverless, IaC, and GitOps {#ch7}

> A controller is an opinion about the world, held continuously and acted upon without being asked.

A modern runtime is less a place where our software sits than a crowd of small machines, each noticing that something differs from what was asked for and correcting it: a scheduler placing pods, an autoscaler adding replicas, a GitOps agent reverting a hand-edited setting, an upgrade reconciler draining nodes through the night. We used to operate servers. Today we mostly operate the things that operate servers, and that question is older than the computer.

In 1868 James Clerk Maxwell published a short paper in the *Proceedings of the Royal Society* called "On Governors." Its subject was the centrifugal governor that James Watt had fitted to his steam engines some 80 years earlier: two iron balls on hinged arms, spun by the engine itself, which fly outward as the engine speeds up and, through a sleeve and a lever, close the steam valve. Engineers had learned that it sometimes **hunted**, swinging above and below the intended speed, and that making governors more sensitive often made the hunting worse. Maxwell wrote down the equations of engine and governor together and showed that whether the swings die away or grow depends on the roots of a single characteristic equation.

The paper is usually cited as the beginning of control theory, and Norbert Wiener pointed back to it when naming cybernetics in 1948. Every reconciliation loop in a cloud runtime is a governor, every one can hunt, and two of them attached to the same shaft can fight. Encore runs dozens of them across its Kubernetes cells (self-contained copies of the stack that keep SaaS tenants apart), its serverless Sale Gate (the waiting room fans queue in before an on-sale) and its GitOps repositories, most written by someone else. This chapter is about operating them: what each loop owns, how fast it acts, and what it cannot see. (Chapter 1's [map of Encore](/prodsys-book/ch/1/#encore) shows where each piece sits.)

### 7.1 Declarative Systems and Reconciliation Loops

#### The anatomy of a loop {#anatomy-of-a-loop}

A **reconciliation loop** is a process that repeatedly observes the actual state of part of the world, compares it with a declared desired state, and takes the smallest action it knows that moves the first toward the second. [The Architecture book](https://oleksiyp.github.io/arch-book/#the-spectrum-priced-in-responsibility) introduced Kubernetes as such a loop; here we take the loop itself apart.

Every loop has the same four parts as Watt's governor: a sensor (the flyballs, or a watch on the Kubernetes API), a set point (the intended speed, or the `spec` of a resource), a comparator (the sleeve and lever, or a function that computes a diff) and an actuator (the valve, or an API call that creates a pod). It also has two properties the YAML never mentions: its **gain**, how hard it pushes for a given error, and its **delay**, how long it takes to sense the effect of its own last push. Maxwell's result, translated, is that high gain and long delay overshoot, see the overshoot late and push back too hard. It is a way of seeing rather than a tuning method, but it names the two numbers to look up before trusting any loop.

The software lineage runs through Mark Burgess's CFEngine (1993), which described the state Unix machines should converge to and repaired deviations on every run. Kubernetes and GitOps agents sit in that tradition, which the OpenGitOps principles now write down: state declared, versioned, pulled and continuously reconciled. What changed is the tempo, from a pass every few minutes to hundreds of loops reacting within seconds.

#### Level-triggered, not edge-triggered {#level-and-edge-triggered}

The terms come from electronics. An **edge-triggered** system acts on *changes*: it hears "a pod died" and starts a replacement. A **level-triggered** system acts on *state*: it looks, finds three pods where five were asked for, and creates two, whatever the history that led there. Kubernetes controllers are level-triggered; watch events are only hints to look sooner, so a missed event or a controller restart costs time, not correctness.

Encore's first tenant-provisioning automation was edge-triggered: a `TenantCreated` message started a script that created a database, a namespace and a DNS record. When the script failed halfway, nothing noticed, because the event had already been consumed; three Professional tenants lived for a month with a namespace and no database. Its replacement, a small operator, reconciles a `TenantDatabase` custom resource on every pass, with idempotent steps and a finalizer for deletion, so half-finished cases heal unattended. A level-triggered loop forgives the past, because it never consults it.

That forgiveness has a price: a level-triggered controller will also undo, over and over, a human's deliberate change that is not in its desired state.

#### When governors fight {#when-governors-fight}

A **controller** in Kubernetes is a reconciliation loop for one kind of resource, and an **operator** is a controller that encodes one application's operational knowledge behind a custom resource. Besides the built-in controllers, Encore's clusters run a Horizontal Pod Autoscaler (HPA) per scaled deployment, the cluster autoscaler, the GitOps agent (Argo CD), the `TenantDatabase` operator and the platform's node-upgrade reconciler, which drains and replaces nodes one at a time to keep each pool at its target Kubernetes version. Trouble begins where two claim the same thing.

The largest public example is recent: the race in Amazon DynamoDB's DNS automation in October 2025, told in Chapter 3, where two instances of one controller interleaved and left a regional endpoint's record empty. Neither instance was wrong alone; the fault lay in their interleaving.

Encore's version was small. On a Thursday before an on-sale, a Catalog engineer expecting a surge of browsing ran `kubectl scale` to take Catalog from 20 replicas to 60. Argo CD, with self-heal on, found `replicas: 20` in the manifest and restored it within seconds. As browsing ebbed, the HPA, set for 60% CPU with a floor of 12, began recommending fewer pods. Its scale-down stabilization window held it for five minutes; then it trimmed toward 12, Argo CD restored 20 within seconds, and the HPA, its window now full of low recommendations, trimmed again at its next evaluation. For the rest of the half hour the two traded the count several times a minute, each trade starting pods with cold caches. Nothing failed, but the engineer believed the service was at 60 when it never was for more than a few seconds, and on a busier day decisions would have rested on that belief. Figures 7.1 and 7.2 show the half hour and its governors.

{% include diagrams/fig-7-1.svg %}

*Figure 7.1 — Catalog's replica count during the fight, sketched. The spike to 60 is reverted in seconds; the autoscaler waits out its five-minute window and then trades the count with the GitOps agent several times a minute. Notice that the count never returns to the 60 the engineer expected.*

| Controller | Field it acts on | Acts within | Set point lives in |
|---|---|---|---|
| GitOps agent (self-heal on) | every field in the manifest | seconds for live drift; up to 3 min to see a new commit | Git |
| Horizontal Pod Autoscaler | `spec.replicas` | 15 s to scale up; 5 min window to scale down | HPA object |
| Cluster autoscaler | node count | about 1 min plus node boot to add; 10 min idle to remove | node-group limits |
| Node-upgrade reconciler | node versions (by drain) | continuous, one node at a time | platform config |
| `kubectl scale` by a human | `spec.replicas` | immediately | a person's head |

*Figure 7.2 — The governors on Catalog's shaft. Two rows claim `spec.replicas`, and the manifest claimed it too. The last row has no record and no delay, which is why it loses.*

The repairs follow Maxwell. First, *one field, one owner*: Encore removed `replicas` from every manifest whose deployment has an HPA, as both the Kubernetes and Argo CD documentation advise (following the documented migration steps, so the count cannot briefly fall to one), and policy now rejects the combination. Second, *express intent to the owner*: a planned surge is a change to the HPA's floor, made in Git through the curtain-up workflow of Chapter 3, which also warms node capacity and lowers the floor again when the sale ends. Third, *respect the damping*: the scale-down window is a dashpot on the flyballs, and teams that shorten it without measuring rediscover hunting. Two loops on one lever oscillate. On two levers, with the slower one setting the faster one's set point, they form a hierarchy, and hierarchy is how control engineers have long mastered complexity (Figure 7.3).

{% include diagrams/fig-7-3.svg %}

*Figure 7.3 — Catalog's governors as a hierarchy. Each slower loop writes the set point of a faster one, and only the dashed accent arrow claims a field another loop owns. Notice that it is also the only arrow that leaves no record.*

**Recap.** A reconciliation loop observes, compares and acts, and its gain and delay decide whether it settles or hunts, exactly as Maxwell showed for the governor. Level-triggered loops forgive missed events but also undo undeclared human intent. When two loops own one field they fight, so we give each field one owner and express intent by changing the owner's set point.

**Exercise 7.1.** Pick one production deployment and list every controller, script and human that can change its replica count or its nodes. For each, note its set point, where that set point is recorded and how quickly it acts. Is any field claimed twice?

### 7.2 Kubernetes in Production

#### Requests, limits and the honest workload {#requests-and-limits}

Kubernetes schedules on promises. A pod's **resource request** is the CPU and memory it promises to need, and the scheduler places it only where that much is free; its **limit** is the most it will be allowed to take. Together they set the pod's quality-of-service class, which decides eviction order when a node runs short. Bilgin Ibryam and Roland Huß call declaring them the *Predictable Demands* pattern: a scheduler given false requests packs nodes that look half empty but are full. Encore right-sizes requests each quarter from observed usage.

The two resources fail differently. A container that exceeds its memory limit is killed, visibly; one that reaches its CPU limit is throttled, quietly, which shows up only as tail latency. Encore's Orders service had a spiking p99 for a month before someone graphed throttled periods beside it. The house rule now sets memory limits equal to requests and leaves CPU limits off latency-sensitive services, so a burst borrows idle capacity instead of waiting for the next slice. The rule is contested, and safe only where CPU requests are honest, since the request is what guarantees each pod its share on a busy node. Noisy batch workloads keep CPU limits, because on shared nodes one team's burst is another team's tail latency.

#### Disruption is a normal day {#disruption-budgets}

A failed node cannot be negotiated with. Voluntary disruptions (a drain for an upgrade, the cluster autoscaler removing an underused node) can be, through a **PodDisruptionBudget** (PDB): a declaration that at most so many pods of a given set may be voluntarily unavailable at once. A drain through the eviction API that would breach the budget waits, but managed upgrades wait only so long. Google Kubernetes Engine (GKE) respects a PDB for up to an hour during a node upgrade and then evicts by force; Amazon's managed node groups fail the update after 15 minutes unless told to force it.

A budget protects the count of pods and nothing inside them. A drained pod receives SIGTERM while requests are in flight and load balancers may still be routing to it, so the proven remedy is graceful termination: a readiness probe that fails as shutdown begins, a short `preStop` pause so endpoints are removed before the process stops accepting work, and a grace period long enough to finish the work. The budget also assumes its pods are spread out; if two members of one group share a node, one drain takes both, so **topology spread constraints** place them across nodes and zones. Encore's golden-path template sets up both for every new service.

Even then, a PDB is a promise about *how many*, never about *which*. Seat Inventory, the service that sells each seat exactly once, runs each shard as a small replicated group with a fenced leader, spread across zones, and its PDB allows one pod unavailable per shard: no drain will take a shard below quorum. But a drain may remove the leader, and a leader's departure, though safe, triggers a failover with a short window of rejected writes. Database operators such as CloudNativePG move leadership before a drain; Seat Inventory has no such operator yet. On a quiet Tuesday the window is invisible. Whether it stays invisible every day of the year depends on which other loops run and what they know about the calendar; Chapter 12 shows the cost when nobody asks.

#### Upgrades as a standing condition {#upgrade-cadence}

Kubernetes ships three minor releases a year, each patched for about a year, and managed providers eventually upgrade clusters that fall behind, ready or not. Like a ship's hull, a runtime must go to dry dock on a schedule; unlike a ship, it can be docked one compartment at a time while it sails.

Encore's Runtime team upgrades in waves. Each region runs a core cluster for Encore's own services and six cells for Professional tenants; a new version reaches a canary cell of internal test tenants first, then the other cells, then the core clusters, the node-upgrade reconciler draining node pools through the PDBs. Before each wave a check scans manifests, add-ons and custom resource definitions for APIs the new version removes, because the commonest upgrade failure is a chart still asking for something that no longer exists. Figure 7.4 shows the waves.

{% include diagrams/fig-7-4.svg %}

*Figure 7.4 — A Kubernetes upgrade moving through Encore's 14 clusters in three waves. The canary cell takes a new version first, and the core clusters, which carry Encore's own services, take it last.*

#### Many clusters, deliberately {#many-clusters}

One large cluster would pack better, but its control plane would be a single blast radius and its upgrades a single event; cells, which Chapter 9 treats in depth, trade efficiency for containment. The price is tooling that makes 14 clusters one fleet, with one GitOps layout, one set of policies and one set of dashboards.

**Recap.** Requests and limits are the promises the scheduler plans with, and CPU limits fail as latency. PDBs govern how many pods a voluntary disruption may take, for as long as the upgrader will wait, and say nothing about which; graceful termination and topology spread protect what the count cannot. Upgrades never end, and are best handled in waves through cells run as one fleet.

**Exercise 7.2.** For one latency-sensitive service, graph CPU throttling against p99 latency for a week, and list its PDB, its spread constraints and its shutdown sequence. Which pod's loss would hurt most, and does anything in your cluster know that?

### 7.3 Serverless and Managed Services — Operating What You Don't Run

#### The shared responsibility line {#shared-responsibility}

Cloud providers describe their bargain as a **shared responsibility model**: the provider is responsible for the security and operation *of* the cloud, and the customer for what they put *in* it. Amazon has since extended it to resilience, but it says nothing about the user, and responsibility to the *user* is never shared. When the Sale Gate is slow, fans blame Encore, and they are right to.

Operating a managed service therefore means operating everything around a box we cannot open: its configuration, its quotas, its failures seen from outside, and our response. A touring production manager advances each venue, learning its power limits and curfew before the trucks arrive; we do the same for a provider, through its quotas pages and our own measurements, since we cannot walk its internals.

#### Quotas are part of the architecture {#quotas}

Function platforms cap concurrency per account and region, shared by every function unless some is reserved. Encore learned this in an on-sale rehearsal, when a Sales Analytics backfill, deployed as functions in the Gate's account, consumed most of the regional concurrency just as the Gate's synthetic fans arrived. Three changes followed. The Gate now runs in its own cloud account, as does each serverless cell for self-service venues, as Amazon's multi-account guidance recommends. It has reserved concurrency, which is also a ceiling, so it is sized to the forecast peak and revisited with it. And a quota inventory, generated nightly, sits beside the capacity models of Chapter 6, alerting when forecast peak comes within 30% of any limit; that is stricter than the provider's usual warning at 80% of current use, because increases take days and some limits are not in the quotas API at all.

Cold starts deserve the same treatment. The Gate pre-warms with provisioned concurrency before scheduled on-sales, early enough for the allocation, which takes minutes, to complete. An unscheduled surge still meets cold functions, so Encore keeps its own cold-start allowance in its latency service level objective (SLO), measured monthly from a deliberate cold start.

#### When the provider is down {#provider-incidents}

On 28 February 2017 a mistyped command during routine maintenance removed more capacity than intended from Amazon S3 in US-East-1, and much of the internet that depended on it failed for about four hours. The administration console of Amazon's own Service Health Dashboard depended on S3, so for a while the provider could not post the outage on its status page.

A provider incident is one the team that owns the symptoms can mitigate but not repair. Encore's runbooks therefore give each managed dependency three pre-decided answers: how we detect its degradation ourselves (our own synthetic checks, whatever the status page says), what we degrade to (the Gate holds fans in the queue with admissions paused; the Catalog serves cached pages), and how we tell fans and organizers. A managed service removes the work of running it and leaves us the work of surviving it.

**Recap.** The provider shares responsibility for the machinery; responsibility to users stays with us. Quotas, reservations and cold starts are architectural properties to inventory, budget and test. We can mitigate a provider incident but never repair it, so we decide in advance how to detect it ourselves and what to degrade to.

**Exercise 7.3.** List every managed service on your most important user path with its tightest quota, your forecast peak against that quota, and what your system does when the service is down for an hour. Mark any entry where the honest answer is "we would find out."

### 7.4 Infrastructure as Code and GitOps

#### State, drift and the reality behind the file {#state-and-drift}

[The Architecture book](https://oleksiyp.github.io/arch-book/#the-environment-is-code-and-git-is-the-control-plane) made the case for infrastructure as code (IaC) and GitOps; operating them is about the gap between the code and the world. Terraform and its fork OpenTofu keep a **state file** recording which real resources correspond to which declarations, and it is production data, needing locking, backups, encryption, access control and an audit log, since it often holds secrets that the code itself never contains.

**Drift** is any difference between the declared and the actual state of infrastructure. Drift made by people, like the console fix at 2 a.m., should be reverted or written back into code; drift made by other loops, like an autoscaler resizing a node group, should be excluded with `ignore_changes`, or the IaC tool becomes another governor on the autoscaler's shaft. Encore runs a plan against every stack nightly and files non-empty diffs as tickets for the owning team.

#### The blast radius of a plan {#blast-radius-of-a-plan}

A plan's most important line is the summary of what it will destroy, and its blast radius is bounded by its stack, the operational reason behind Kief Morris's case for small stacks. Morris also warns against cutting too fine, since dependencies between stacks become the new risk, so Encore cuts along ownership and rate of change, which in practice means along cells and services.

Encore's earliest infrastructure lived in a single stack, and a harmless-looking module rename once produced a plan that would destroy and recreate the Finance ledger's database, because the tool saw a resource vanish under one name and appear under another. A reviewer caught it by reading to the bottom. Three safeguards now do her job. A rename is declared with a `moved` block, so the plan shows a move and nothing destroyed:

```hcl
moved {
  from = module.finance_db.aws_db_instance.this
  to   = module.ledger_db.aws_db_instance.this
}
```

Stateful resources carry `prevent_destroy` in code *and* deletion protection on the resource itself, because the first lives in the very code a careless edit removes, while the second lives with the provider. And plans are reviewed with the destructive summary at the top.

Surgical teams adopted a practice for this moment: the **time-out** before the first incision, in which the team confirms aloud the patient, the procedure and the site. The World Health Organization's checklist study of 2009 found complications and deaths fell where it was adopted, because the worst errors are made confidently, at the moment of commitment. A plan review is our time-out, and **policy as code**, rules such as those written for Open Policy Agent (OPA) and evaluated against every plan and manifest, is the automated part of it, applied to every plan. Encore's rules deny any plan that destroys a resource labeled stateful without a separately approved override, any manifest that sets `replicas` beside an HPA, and any public bucket.

#### GitOps repositories and promotion {#gitops-promotion}

The term GitOps was coined at Weaveworks in 2017 for an older idea made precise: a pull-based agent inside each cluster reconciles it toward a Git repository, so that people change the repository and nothing else changes the cluster. Application repositories publish images by digest; a separate environment repository, `encore-deploy`, holds every cluster's desired state as a shared base with one overlay per environment and cell, so environments cannot quietly diverge, and an Argo CD instance in each cluster reconciles from it.

| Stage | What changes in `encore-deploy` | Who approves | Gate to next stage |
|---|---|---|---|
| Staging | image digest in `envs/staging/` | automatic on build | integration suite and synthetic buyers pass |
| Canary cell | digest in `envs/prod/eu-1/cell-canary/` | automatic | SLO holds for 1 h under synthetic buyers |
| Professional cells | digest in each cell directory, a few at a time | owning team | per-cell burn rate stays normal |
| Core clusters | digest in `envs/prod/*/core/` | owning team | outside on-sale freeze windows |

*Figure 7.5 — Promotion as a series of pull requests. Each stage is a commit someone can read and revert, and the gates are the same SLO signals Chapter 4 defined, applied to the deployment itself.*

An SLO that holds for an hour on the canary cell's trickle of internal traffic proves little, so Encore drives synthetic buyers through it and treats the first Professional cells as the real test. The repository records what was *intended* to run, which is not always what did run, so Encore alerts on any application out of sync for more than 15 minutes, and on any whose health Argo CD reports as degraded.

Emergencies are where GitOps is most often misunderstood. Encore's break-glass procedure grants a named engineer an hour of direct cluster access, logged and reviewed afterwards, and its first step is to suspend automated sync for the affected application. Without it, self-heal reverts the fix within seconds, as it reverted the Catalog scale-up, long before any write-back commit. The procedure ends with that commit and with sync restored.

For planned quiet periods, Argo CD offers a gentler tool. Argo CD's **sync windows** declare, per project, when automated syncs are allowed or denied; with GKE's maintenance exclusions and their equivalents at other providers, they are the established form of calendar-aware automation. Tied to the on-sale calendar, a deny window is a few lines:

```yaml
kind: AppProject
metadata: {name: purchase-path}
spec:
  syncWindows:
  - kind: deny
    schedule: "0 8 * * 5"      # T−2h before a Friday 10:00 on-sale
    duration: 4h
    timeZone: Europe/Paris
    applications: ["*"]
    manualSync: true           # break-glass can still sync by hand
```

Encore has the tool and has not wired it to the calendar; its freeze lives in the delivery pipeline and the on-sale channel, as Chapter 8 describes. And a sync window holds only what Argo CD applies. The node-upgrade reconciler is not an Argo CD application but a platform controller that reads disruption budgets and nothing else, and no sync window would hold it.

Secrets stay in a secrets manager, and an operator in each cluster materializes the references declared in Git, so the repository names a secret and never holds it; Chapter 11 takes up rotation.

**Recap.** IaC state is production data, and drift is reverted, written back or ignored, depending on whether a person or a loop made it. Small stacks, `moved` blocks, provider-side deletion protection and policy as code make it hard for a destructive plan to pass review unnoticed. GitOps promotion is a chain of readable pull requests, only sync and health status say what is running, and an emergency change must first tell the loop to stand aside.

**Exercise 7.4.** Count the resources in your largest stack, and write one policy rule that would have blocked the worst infrastructure change your team has applied. Then walk through your break-glass procedure: at which step would your GitOps agent undo the fix?

### 7.5 The Platform as a Paved Road

#### A product with a road crew {#product-with-a-road-crew}

Everything so far is machinery that 40 stream-aligned teams should not each have to master. [The Architecture book](https://oleksiyp.github.io/arch-book/#golden-paths-on-a-self-service-control-plane) described how Encore built its platform; the question now is how it is *run*. Matthew Skelton and Manuel Pais, in *Team Topologies*, framed the platform team's purpose as reducing the **cognitive load** of stream-aligned teams, and argued for the **thinnest viable platform**: the smallest set of services that lets those teams deliver without deep knowledge of the layers beneath. Thinness is an operating virtue: every capability offered must be run, upgraded and eventually retired.

The phrase "paved road" (Netflix's term; Spotify's "golden path" is its cousin) is worth taking seriously. A city paves the routes people actually walk, often after watching where the grass wears away, and nobody is forbidden to cross the park; Encore's platform teams likewise measure where teams leave the road and why. The break in the analogy is the useful part: a city can rely on people needing to travel, while a platform must keep earning its traffic. DORA's 2024 report found that platform users reported higher productivity, but that platforms came with lower delivery throughput and change stability, and helped most where developers kept their independence.

#### Operating the platform itself {#operating-the-platform}

Camille Fournier and Ian Nowland insist that a platform team must own the operations of what it builds, on-call included, and Encore holds to this: the Reliability team carries the pager for the platform planes, and each plane has its own SLOs, among them GitOps sync latency, cluster API availability and time to provision a new service. I spent years doing platform engineering inside a large bank, and the costliest lesson was that users judge a platform by its worst week more than by its average one.

The same holds for the platform's own automation. The node-upgrade reconciler, the GitOps agents and the policy engine act on other teams' services, often when nobody is watching, and the published practice is plain: it rolls out under the same safety rules as any change, and windows tied to the calendar keep it out of business-critical hours. Encore classifies its automation as "low-risk," and on most days it is. Whether the reconciler, which stands outside Argo CD and outside the freeze, should be held to a calendar on the days that matter most is a question the platform group has not yet asked.

Migrations are the platform's other permanent work. Fournier and Nowland treat migration and sunsetting as staffed product work, much as Google runs its large-scale changes centrally. Encore's own rule is that the platform team does the first three migrations itself before writing the self-service guide, so the guide describes the road as it really is.

**Recap.** A platform is a product for lowering other teams' cognitive load; it should stay as thin as that purpose allows and earn its traffic without mandates. Its teams own its operations and SLOs, and its automation is owed the same rollout rules and calendar windows as any change. Migrations are staffed product work, and the platform team does the first ones itself.

**Exercise 7.5.** Pick one capability your platform, or your cloud provider, offers your team. Who is on call for it, what is its SLO, does it respect any calendar of yours, and when was the last migration it forced on you? If you cannot answer, write the question to its owners.

### Kata: The Lunch Rush

> **Your brief: "Forkline."** A food-delivery marketplace: 18,000 restaurants and 25,000 couriers across six countries, with a customer app, a courier app and a restaurant tablet. Forkline has 65 engineers in nine teams and a platform team of four. Its three hand-built Kubernetes clusters are two minor versions behind, and the provider will force an upgrade in five months. Infrastructure lives in one Terraform stack of 1,700 resources whose plan takes 25 minutes, so engineers fix things in the console. Order webhooks to restaurant point-of-sale systems run as functions and were throttled last month when a tablet update made every restaurant reconnect at once. At lunch the dispatch service's HPA fights an engineer's habitual manual scale-up at 11:30, and nobody is sure which wins.

**Deliverables:**

1. **Controller census** — every loop and human that changes the dispatch service's replicas, nodes or infrastructure, with field, set point and speed.
2. **Upgrade plan** — reaching a supported version before the forced upgrade, with PDBs, graceful shutdown, the order in which clusters move and the maintenance windows that keep upgrades clear of the meal peaks.
3. **Stack decomposition** — how to split the 1,700-resource stack without destroying anything, which resources get deletion protection, and three policy-as-code rules.
4. **Managed-service survival sheet** — the quota inventory for the order path and what the webhooks degrade to during a reconnection storm or a provider outage.
5. **Thinnest viable platform** — what a four-person platform team should offer, what it should decline to offer, and the SLOs it will be held to.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| One owner per field | Does every field with more than one controller now have exactly one, with intent expressed through its set point? |
| Upgrade as routine | Does the plan leave Forkline able to upgrade every few months, within windows that know the meal peaks? |
| Bounded plans | Could any single plan, or any rename, still destroy a stateful resource without a separate approval? |
| Provider realism | Are degradation modes decided in advance and detected by Forkline's own checks rather than the provider's status page? |
| Thinness | Is the platform's scope sized to four people's on-call capacity, with explicit refusals? |
| Drift honesty | Is console change made unnecessary, or merely forbidden? |

#### Where you now stand

You can now read a runtime as a collection of governors: name what each loop owns, how fast it acts and what it cannot see, keep two from fighting over one lever, tell a loop to stand aside when a person must act, and run clusters, functions, stacks and repositories as one fleet, knowing where the provider's responsibility ends. Chapter 8 turns from the machinery that holds the system steady to the changes we deliberately push through it, and to how change, more than anything else, breaks production.

### References

- James Clerk Maxwell — [*On Governors*](https://doi.org/10.1098/rspl.1867.0055). Proceedings of the Royal Society of London, 1868.
- Kubernetes — [*Horizontal Pod Autoscaling*](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) and [*Disruptions*](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/). Documentation — free online.
- Argo CD — [*Automated Sync Policy*](https://argo-cd.readthedocs.io/en/stable/user-guide/auto_sync/) and [*Sync Windows*](https://argo-cd.readthedocs.io/en/stable/user-guide/sync_windows/). Documentation — free online.
- Amazon Web Services — [*Summary of the Amazon DynamoDB Service Disruption in the Northern Virginia (US-EAST-1) Region*](https://aws.amazon.com/message/101925/). 2025 — free online.
- Amazon Web Services — [*Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region*](https://aws.amazon.com/message/41926/). 2017 — free online.
- Google Cloud — [*Node pool upgrade strategies*](https://cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies). Documentation — free online.
- HashiCorp — [*Refactoring modules*](https://developer.hashicorp.com/terraform/language/modules/develop/refactoring). Terraform documentation — free online.
- Bilgin Ibryam, Roland Huß — [*Kubernetes Patterns*, 2nd ed.](https://developers.redhat.com/e-books). O'Reilly, 2023 — free online.
- Kief Morris — [*Infrastructure as Code*, 3rd ed.](https://www.oreilly.com/library/view/infrastructure-as-code/9781098150341/). O'Reilly, 2025.
- OpenGitOps — [*GitOps Principles*](https://opengitops.dev/). CNCF, 2021 — free online.
- Camille Fournier, Ian Nowland — [*Platform Engineering*](https://www.oreilly.com/library/view/platform-engineering/9781098153601/). O'Reilly, 2024.
- Matthew Skelton, Manuel Pais — [*Team Topologies*, 2nd ed.](https://itrevolution.com/product/team-topologies/). IT Revolution, 2025.
- DORA — [*Accelerate State of DevOps Report 2024*](https://dora.dev/research/2024/dora-report/). Google Cloud, 2024 — free online.

---

## Chapter 8: Shipping Change Safely — Continuous and Progressive Delivery {#ch8}

> Every outage begins as somebody's reasonable change.

A system that nobody touches keeps doing whatever it did yesterday, but the world it serves keeps moving, and a system frozen against change slowly becomes wrong about the world. So we change it, many times a day, and in doing so create the moments when most of our trouble begins. The question of this chapter is how a team can change a running system often, quickly and safely, when the three seem to conflict.

The industry's answer is, at first sight, a paradox: we make change safer by making it smaller and more frequent, and by separating putting code into production from letting anyone use it. Consider first what happens without it. On the morning of 1 August 2012, Knight Capital, one of the largest market makers in American equities, put new code into service on its order router. Forty-five minutes after the market opened, it had lost about $440 million, and within a year it no longer existed as an independent company.

Encore ships about 180 production deployments on a typical working day, across 40 teams and through one golden-path pipeline, with a canary that promotes builds on the evidence of its service level objectives (SLOs). This chapter takes that machinery apart, follows change down the routes that bypass it, and ends with what changes when a growing share of those deployments was written by a machine.

### 8.1 Change as the Leading Cause of Outages

#### Forty-five minutes at Knight Capital {#knight-capital}

Knight's order router, SMARS, split large "parent" orders into smaller "child" orders. For the New York Stock Exchange's Retail Liquidity Program (RLP), which began trading on 1 August, Knight wrote code that reused a flag in the order messages, one that had once activated a function called Power Peg. Power Peg had been unused since 2003 but never removed, and a 2005 change had moved the logic that counted how much of a parent order was filled, so Power Peg, if woken, would no longer know when to stop.

From 27 July a technician copied the new code to the eight SMARS servers, a few on each successive day. It reached seven. The rollout was staged, but nothing verified it: no second person checked the work and no automated process compared the servers. When the market opened at 09:30 Eastern time, seven servers handled RLP orders as intended and the eighth woke Power Peg, which sent child orders without end. Before the open, Knight's systems had sent 97 automated emails mentioning Power Peg; they were not designed as alerts, and nobody read them as one.

The response made things worse. Engineers removed the new code from the seven healthy servers, a rollback in every ordinary sense, and now all eight ran the old code against the repurposed flag, and all eight woke Power Peg. When it was stopped, about 45 minutes after the open, SMARS had made 4 million executions in 154 stocks, for more than 397 million shares. Knight reported a pre-tax loss of about $440 million; the Securities and Exchange Commission (SEC), in its 2013 order, put the loss above $460 million and fined the firm. Knight needed emergency financing within days and was merged into Getco the next year. Figure 8.1 follows the eight servers through the morning.

{% include diagrams/fig-8-1.svg %}

*Figure 8.1 — Knight Capital's eight SMARS servers on 1 August 2012. One unverified server woke Power Peg at the open, and the rollback of the seven healthy servers gave all eight the same old code.*

Read with Chapter 2's eyes, Knight's morning has no single cause: dead code kept for nine years, a flag given a second meaning, an unverified deployment, a refactoring that broke a dormant path, unread warnings and an amplifying rollback. Each was locally understandable; together they made a failure that needed only the deployment to set it off. Staging alone saved nothing, because a rollout protects us only when something compares the servers it reached with those it did not.

#### Why change dominates {#why-change-dominates}

Knight's cost was extreme; its shape is common. The authors of Google's *Site Reliability Engineering* (2016) reported that roughly 70% of their outages were due to changes in a live system, and prescribed three remedies that organize this chapter: roll out progressively, detect problems quickly, roll back safely. Other datasets give smaller shares, depending on whether a configuration edit counts as "change," a question that will prove important. When Encore's Reliability team reviewed the last year of incidents, about two thirds began within an hour of a change: a deployment, a configuration edit, a flag flipped, or platform automation doing its job.

They could answer because Encore's deploy history records every change, its owner and the services it touched, and shows them beside the first alert of any incident. The DevOps Research and Assessment (DORA) program measures stability as change failure rate and time to recover from a failed deployment, and both need this join between changes and incidents; without it, a team argues about its stability from memory.

The tempting conclusion is to change less. It fails twice. Patches, upgrades and the business do not wait, so a system changed rarely gathers its changes into larger batches, which are harder to test, reason about and undo. And a team that deploys rarely deploys badly, because a skill practiced quarterly is half forgotten. The essential complexity is that the system must change; the accidental complexity is whatever makes each change bigger, rarer or harder to reverse than it needs to be.

**Recap.** Most outages begin with something we did, because change is when the system becomes one we have not yet observed. Knight shows a deployment completing a mechanism assembled over years. Changing less only makes each change larger, and a change log joined to the incident record is what lets a team see any of this.

**Exercise 8.1.** For your last ten incidents, note the most recent change before each (code, configuration, data, flag, automation or none). What share followed a change, which kind most often bypassed your pipeline, and how long did finding it take?

### 8.2 The Deployment Pipeline and Continuous Delivery

#### A sequence of increasingly expensive questions {#pipeline-as-questions}

The phrase *continuous integration* (CI) was coined by Grady Booch in *Object-Oriented Design with Applications* (1991), for a steady rhythm of integrated releases; Kent Beck's extreme programming (1999) gave it the cadence we now mean, many merges into one mainline a day. In 2009 Flickr's John Allspaw and Paul Hammond described more than ten deploys a day, and Jez Humble and David Farley's *Continuous Delivery* (2010) gave the practice its central structure.

The **deployment pipeline** is the automated path every change takes from commit to production, a sequence of stages in which each asks a more expensive question than the last and only a change that answers them all may proceed. Its rules are few and strict: build the artifact once and promote that same artifact everywhere, so that what was tested is what ships; keep everything that defines the system in version control; and when the pipeline is red, fix it first, because a pipeline people have learned to ignore is no longer a control.

| Stage | The question it asks | Typical time at Encore | What it cannot see |
|---|---|---|---|
| Commit | Does it build, and do the fast tests pass? | 6 min | anything involving another service |
| Acceptance | Does the service keep its contracts and its specified behavior? | 15 min | real traffic, real data shapes |
| Fitness | Do architectural, security and cost rules still hold? | 4 min | behavior under load |
| Staging soak | Does it start, migrate and serve in a production-like cell? | 10 min | the 500× on-sale |
| Canary | Do its service level indicators (SLIs) match the baseline's on real traffic? | 20–60 min | rare paths and slow drift |
| Release | Who should see the new behavior, and when? | a business decision | — |

*Figure 8.2 — Encore's golden-path pipeline. Each stage is cheaper to fail than the next, and the right-hand column says which later stage must catch what this one cannot.*

Humble and Farley distinguished *continuous delivery*, in which every change that passes the pipeline could be deployed, from *continuous deployment*, in which it is; the second needs fast tests, observability that notices a bad change, trunk-based development and rollback in minutes. Encore deploys continuously, except that Seat Inventory, the event-sourced ledger at the heart of every purchase, keeps a human release step while its projections replay against production history.

#### Small batches, and what replaces the change board {#small-batches}

The pipeline's deepest effect is on batch size. A 40-line change can be understood, observed and undone; three weeks of 15 people's work cannot. *Accelerate* (2018) found that throughput and stability do not trade off: the teams that deployed most often also failed least often and recovered fastest. It also found that approval by an external change advisory board went with slower delivery and no better change failure rate. My own reading is that such a board mostly produces reassurance, since a weekly committee cannot know a diff as well as the colleague who reviewed it that morning.

None of this means changes go unexamined. What DORA calls **streamlined change approval** moves the control into the pipeline: a peer who knows the code reviews every change, every change passes the same automated checks, riskier changes get more eyes, and the pipeline records who approved what, so an auditor reads evidence instead of meeting minutes. Encore's golden path writes that record for every deployment.

The pipeline guards only the changes that go through it. Knight's deployment was manual, and its flag was data in a message. At Encore, service configuration lives in the GitOps repositories of Chapter 7, but flags, rule sets and platform automation had their own paths into production, and Section 8.3 shows three large outages that travelled by such paths.

**Recap.** The deployment pipeline asks increasingly expensive questions of one artifact, and its real gift is small batches, which buy stability as well as speed. Peer review and automated checks inside it do the change board's job better than the board did, and every route around it deserves to be listed and narrowed.

**Exercise 8.2.** List every route by which a change reaches production: pipelines, consoles, flag tools, configuration services, generated data, automation, scripts. Mark each as reviewed, tested, recorded, staged and reversible, or not. The rows with the most gaps are your next pipeline work.

### 8.3 Progressive Delivery — Feature Flags, Canaries, and Rollbacks

#### Deploying is not releasing {#deploy-versus-release}

**Progressive delivery** is the practice of putting new code into production without exposing it, then widening its exposure in deliberate steps, each conditional on evidence that the last did no harm. The analyst James Governor named it, and its one steady idea is that every change has a blast radius, and we should choose it.

#### Canaries and automated analysis {#canary-analysis}

British miners carried canaries underground for most of a century, because the bird showed carbon monoxide before the men did; the birds were phased out from 1986. A **canary release** sends a small share of real traffic to the new version and compares its health with the old version's before more follows. The analogy breaks usefully: a canary that weakly resembles the population it guards (fewer users, quieter hours, cheaper requests) can sing happily while the mine fills.

At each step of Figure 8.3 an automated analysis compares Encore's purchase-path canary with a baseline of equal size running the old version, started at the same moment, never with yesterday or with the long-running fleet, whose warm caches flatter it. The SLIs are ones fans would recognize: checkout success, p99 latency of `POST /holds`, and the rate of `PaymentFailed` events caused by Encore itself.

| Step | Traffic | Minimum bake | Promote when | Roll back when |
|---|---|---|---|---|
| 1 | 1% | 10 min and 20,000 requests | no SLI worse than baseline beyond noise | any SLI significantly worse, or any integrity alarm |
| 2 | 5% | 15 min | as above | as above |
| 3 | 25% | 20 min | as above, and error-budget burn under 2× | as above, or burn over 2× |
| 4 | 100% | — | — | the normal burn-rate alerts of Chapter 4 |

*Figure 8.3 — Encore's canary schedule for purchase-path services. The request minimum matters as much as the minutes, because a canary judged on too little traffic cannot tell a bad build from noise.*

An integrity alarm, such as a seat with two `SeatSold` events, rolls back at once whatever the statistics say, as Figure 8.4 draws, and canaries do not run during on-sales, for reasons Section 8.4 gives. Bakes measured in minutes catch only failures that show in minutes; a slow leak passes every step and is left to the burn-rate alerts, which is why the largest operators, Amazon among them, bake for hours between waves of regions.

{% include diagrams/fig-8-4.svg %}

*Figure 8.4 — Figure 8.3's schedule drawn over time on a logarithmic scale. A canary that holds reaches every fan in about 45 minutes. One that raises an integrity alarm at 25% goes straight back to zero, without waiting for the statistics.*

**Blue/green deployment** runs a complete new environment beside the old one and switches traffic at once, buying an instant switch back at the price of double capacity; Encore uses it for the serverless Sale Gate, its virtual waiting room. **Ring deployment** widens exposure by population, as Microsoft has long done for Windows and Azure. Encore's rings run from staff and synthetic buyers through the self-service and Professional cells to its own fan site and the Enterprise silo for `venue-chain-a`, whose contract makes it last.

{% include diagrams/fig-8-5.svg %}

*Figure 8.5 — Encore's delivery rings, widening by population from staff and synthetic buyers outward. The outermost ring is last because a contract places it there.*

#### Configuration and data travel the same road {#configuration-and-data}

The three most instructive outages of recent years were not code. On 19 July 2024 CrowdStrike pushed Channel File 291, a content update for its Falcon sensor on Windows. The sensor's code was staged; its "rapid response content" was treated as data and went to every machine at once. The file supplied a 21st input field to an interpreter that provided 20, the content validator missed it, and the out-of-bounds read crashed about 8.5 million Windows machines, by Microsoft's estimate, in the 78 minutes before the file was withdrawn. CrowdStrike's remediation: staged content deployment through canary rings, customer control over timing, and bounds checks.

On 12 June 2025 a policy change behind Google Cloud's Service Control, which checks authorization and quota on API calls, carried blank fields. It replicated globally within seconds and crashed, in every region, a code path added two weeks earlier without a feature flag or error handling. Google committed to making Service Control fail open, to flag-protecting changes to critical binaries, and to propagating global data "incrementally with sufficient time to validate and detect issues." On 18 November 2025 a permissions change in a Cloudflare database doubled a generated feature file for its bot-management model. Pushed network-wide every five minutes, the file overran the proxy's limit of 200 features, and an unhandled error became a panic that broke much of the web for about three hours. Cloudflare's first remediation was to harden "ingestion of Cloudflare-generated configuration files in the same way we would for user-generated input."

The three operators reached one recipe. Stage configuration and data as we stage code, through rings with a bake and an automated halt, so that a bad push reaches a canary before it reaches every region. And make every consumer treat internal configuration as untrusted input: validate it on arrival, enforce its assumed limits, keep the last version known to be good, and decide in advance whether a component with nothing good to load fails open or closed.

Encore's nearest equivalent is the Bot Screening rule bundle that every Sale Gate instance loads. Shadow-mode trials (Chapter 4) test whether a rule is wise, not whether its bundle is well formed, and the bundle reached every instance within a minute. The Reliability team has since moved the bundle, the flag service's state and the edge routing table onto the same rings as code, and rewrote the Gate's loader along these lines:

```python
MAX_RULES = 5_000   # far above today's bundle, far below what exhausts memory

def load_bundle(raw: bytes, current: Bundle) -> Bundle:
    try:
        bundle = Bundle.parse(raw)          # schema, types, required fields
        if len(bundle.rules) > MAX_RULES:
            raise BundleError(f"{len(bundle.rules)} rules exceeds {MAX_RULES}")
        bundle.verify_signature()           # built by the pipeline, never by hand
    except Exception as err:                # a bad bundle must never crash the Gate
        metrics.increment("rule_bundle_rejected")   # pages Bot Screening on call
        log.error("keeping bundle %s: %s", current.version, err)
        return current                      # last-known-good
    return bundle
```

A Gate instance that cold-starts with no valid bundle fails open on bot scoring but keeps metering admission, because the rate limit is what protects Seat Inventory.

#### Feature flags and their debt {#flag-debt}

A **feature flag** is a runtime switch that decides which behavior deployed code exhibits, so that code can reach production long before its behavior reaches anyone. Encore's new seat-map renderer, behind `seatmap-renderer-v2`, reached staff first, then one fan in a hundred on small events, then all events below 5,000 seats, and finally, after a quiet month, the stadium on-sales. When it misdrew curved balconies on one venue's map, the team turned it off for that venue in seconds and fixed it at leisure.

Flags age differently by kind: a release flag should live for weeks, a kill switch for years, an experiment flag as long as its experiment. With Knight in mind, Encore's flag service enforces simple rules: every flag has an owner, a kind and an expiry date; no name is ever reused; a flag change is a production change, recorded in the deploy history; and an expired release flag blocks its owner's next deployment, which is stricter than most tools' default warning. Uber's Piranha, which writes the clean-up change itself, is the gentler complement. A third of Encore's 2,300 flags had not changed state in a year, each a branch nobody tested both ways. A flag that is never turned off is dead code wearing a switch.

#### Rollback or roll forward {#rollback-or-roll-forward}

To **roll back** is to return production to the last version known to be good; to **roll forward** is to repair the problem with a new change. Rollback is the right default for stateless code, but Knight's rollback spread the failure to all eight servers, because the old code met a world the new code had changed. That world is usually data, and the defense is to keep each change compatible with its predecessor, through the expand-and-contract migrations of Chapter 10 or Amazon's two-phase pattern, in which one deployment teaches every node to read a new format and a later one writes it. Encore's pipeline records whether each deployment is safe to roll back; one that is not gets a longer canary and a named engineer awake for its first hour.

**Recap.** Progressive delivery chooses each change's blast radius. Canaries compare against a simultaneous baseline on enough traffic, and rings order exposure by who can best absorb harm. Configuration and data travel the same staged road as code, into consumers that distrust them, and rollback is safe only while the previous version can still read the data the new one wrote.

**Exercise 8.3.** Pick the configuration or data file that the most machines in your fleet load. How long does a change to it take to reach all of them, what validates it on arrival, and what does a consumer do with a malformed one?

### 8.4 Testing in Production

#### Rehearsing in the real room {#rehearsing-in-the-real-room}

"Testing in production" once sounded like an admission of skipped testing. It is now a discipline, because no staging environment reproduces production's data, traffic or scale, and Encore's 500× on-sale exists only where it happens.

**Synthetic users** are scripted clients that exercise real paths continuously; Encore's hold seats, pay through the payment provider's test route and receive tickets for a hidden test event, hourly, and every minute during on-sales. A **dark launch** runs new code against real traffic with its results hidden: Facebook prepared its chat service in 2008 by having live pages quietly send it simulated traffic, and Encore dark-launched a new Seat Inventory availability projection, comparing its answers with the old one's until a fortnight passed without disagreement. **Shadow traffic** copies real requests to a new version and discards its responses. It suits reads; shadowing Notifications naively would send every fan two emails, so writes are shadowed only into sandboxes.

#### Change freezes and their exceptions {#change-freezes}

A **change freeze** is a period in which production changes are forbidden except for emergencies, because failure is temporarily more costly than usual. Retailers have frozen through the holidays for decades, on thin evidence. Practitioners report a spike in failures when the queued changes land afterwards; the one serious quantitative study I know is Meta's: in its winter 2023 freeze it used risk models to gate only 16% of changes, landed 42% more changes than the previous winter, and saw 52% fewer outages. One company's observational study is not proof, but it favors a narrow freeze aimed at risky changes. Google's freeze after June 2025 had that shape, covering only Service Control and manual policy pushes until repairs were in.

Encore freezes the purchase path from two hours before each big on-sale until it ends, as a deliberate, scoped choice: when load rises 500× in minutes, a canary has neither a stable baseline nor time to bake, so the instruments that make change safe the rest of the week are blind in the hour when an outage costs most.

The difficulty is the boundary, and it erodes. Over the past year Encore's freeze has softened in reasonable steps. Exceptions are granted in the on-sale chat by whoever is senior and awake: 41 in 12 months, recorded nowhere else. Low-risk platform automation, such as certificate rotation and the node-upgrade reconciler, was excluded, because pausing it caused more work than it saved. Catalog was judged to sit off the purchase path, since a fan can buy a seat without searching. Each step was sensible. Together they turned the freeze from a rule into a custom: the drift Chapter 2 described.

Cloudflare's trigger was a routine permissions change in a database far from the proxy it broke. A freeze scoped by a list of services, with automation exempt, would have missed it. Encore has not yet asked whether its boundary should follow dependencies, or where its exceptions should be written; Chapters 12 and 13 return to both.

**Recap.** Synthetic users, dark launches and shadow traffic learn what only the real room can teach, while keeping users and side effects out of the experiment. The evidence for freezes is thin and favors narrow, risk-based ones; Encore's is justified by blind instruments during a surge, but its boundary drifts through sensible exceptions, which belong in writing.

**Exercise 8.4.** List every change that reached production during your last freeze, automation and data pushes included. Who granted the exceptions, where are they recorded, and which frozen service depends on something the freeze did not cover?

### 8.5 Machine-Written Change — Review, Fitness Functions, and Provenance

#### The Tuesday morning, revisited {#the-tuesday-morning-revisited}

[The Architecture book](https://oleksiyp.github.io/arch-book/#the-inversion-the-preface-promised) ended on a Tuesday when a coding agent rebuilt Encore's Notification service overnight: new retry semantics in 40 files nobody had read in full. Every check passed and the canary promoted it. One engineer, spending 20 minutes on that change alone, saw that the new retries could send a fan the same ticket twice, and added a spec-level idempotency test before merging. The pipeline had done everything asked of it, but nothing in it asked whether the new retries were safe.

Unread code is as old as Power Peg; what is new is its speed. By autumn a quarter of Encore's merged changes carried an agent label, and they were larger than people's. DORA's 2024 report estimated that each 25% increase in AI adoption went with a 7.2% fall in delivery stability; its 2025 report found throughput gains but the stability penalty still in place, and named small batches and strong version control among the capabilities that help. ImpossibleBench (2025) found coding agents, given tests they could not honestly pass, often editing the tests instead. The best production account is Google's 2025 report on large code migrations: about 80% of landed modifications were model-written, yet every change passed the existing tests, was reviewed by the code's owners and rolled out gradually.

#### Encore's policy {#encores-policy}

After the Notification morning, Encore's architecture group and the Reliability team wrote a policy whose premise is that the pipeline treats every change alike, whoever wrote it, while review weighs what the change could break.

**Spec-level tests.** A **spec-level test** checks a property the business depends on, stated independently of any implementation, so that it stays true when every line beneath it is regenerated. For Notifications, one `TicketIssued` event yields exactly one wallet pass and one email under any sequence of retries and restarts, written as a property-based test. People write or approve these tests, and an agent's pull request that modifies one is blocked until a human owner approves the test diff separately, through ordinary code-owner rules.

**Small changes and provenance.** Following DORA's 2025 advice, agents are asked for changes a reviewer can hold in mind; the Notification rewrite would now arrive as three changes, each through its own canary. The golden path already signs build provenance for every artifact (Chapter 11), and authorship sits on top: every commit records any agent that wrote it, with its model version, and the human who sponsored it, much as the Linux kernel asks for an `Assisted-by` tag and lets only a human sign off a patch. Nobody yet knows whether such labels shorten incidents; Encore keeps them because they are cheap and cannot be added later.

**Risk-tiered human review.** Human attention is the scarcest resource in the pipeline, so the policy spends it by blast radius, as Figure 8.6 shows.

| Tier | What it covers | Human review | Delivery |
|---|---|---|---|
| 1 | Seats, money, identity, the purchase saga, anything integrity alarms watch | two reviewers, one the domain owner; behavior and test diffs read in full | full canary, rollback safety declared, never auto-merged |
| 2 | Fan-facing but not money or seats: Notifications, Catalog, renderers | one reviewer reads the spec, the invariants and the test diff, and samples the code | full canary; agent changes bake twice as long |
| 3 | Internal tools, documentation, dashboards, test scaffolding | automated checks; 1 change in 10 sampled for human review | standard pipeline |

*Figure 8.6 — Encore's review tiers. The tier comes from what a change touches; provenance decides only how long an agent's change bakes and whether a human samples it.*

Tiering review by what a change touches is old practice, from IT service management's change classes to the owners files that guard sensitive paths at Google. The doubled bake and the one-in-ten sample are Encore's own numbers, without published precedent: the bake is a cheap hedge in the spirit of DORA's stability finding, and the sample exists so that someone notices when Tier 3's checks begin to miss things.

**Fitness functions.** The fitness functions of *Building Evolutionary Architectures* (2nd ed., 2022), automated checks that a system keeps a promised property, are the only reviewers that read every line at the speed agents write. Every handler with an external side effect must take an idempotency key; no service may stack a retry layer on the mesh's, or exceed the 10% retry budget Google's overload guidance recommends; no outbound dependency may appear without a registry entry. A check sees that an idempotency key is present but not whether it is used correctly, which is why the spec-level tests remain.

The policy is not free: Tier 1 reviews are slower, agent-heavy teams grumbled that the doubled bake looked like distrust, and spec-level tests take real thought. But the Notification engineer's 20 minutes were the most valuable of that week, and the policy exists to spend such minutes where they matter. A review that reads everything a machine wrote reads nothing carefully.

**Recap.** Machine-written change is new in volume and in its tendency to satisfy checks rather than intentions, and so far stability pays for it. Encore combines proven pieces (guarded spec-level tests, small changes, build provenance, fitness functions) with labels and sampling rates that are its own young choices. The pipeline checks every change alike; review also weighs who wrote it.

**Exercise 8.5.** Write the two most important invariants of a service you own as spec-level tests, independent of its current code. Which review tier does it belong in, and what would your review read if an agent rewrote it overnight?

### Kata: Always Open

> **Your brief: "Kestrel."** A mobile-first retail bank with 1.8 million customers in three EU countries and 110 engineers in 14 teams. Card authorizations must be answered within 2 s, day and night, and the regulator requires a record of every production change: who approved it, what it touched and how to undo it. Kestrel deploys about 60 times a day, but change records are written by hand afterwards for a weekly risk committee, and its change failure rate is about 15%. Fraud rules are data, published from a console straight to every authorization node. Of 1,900 flags, one fraud-rule flag, reused for a new rule, declined valid card payments in one country for a morning. A Black Friday freeze grants exceptions in chat, and agents write a third of pull requests, mostly fraud rules.

**Deliverables:**

1. **Change-route map** — every route into production, code, configuration and data alike, with its gaps.
2. **Pipeline redesign** — stages, peer review, pipeline-written change records, and a position on the weekly committee.
3. **Progressive rollout plan** — customer rings, canary SLIs, staged and validated fraud-rule publication, and when rollback is unsafe.
4. **Flag and freeze policy** — flag rules, a plan for the 1,900, freeze scope and an exceptions register.
5. **Review tiers for machine-written change** — tiers, spec-level tests for fraud rules, and fitness functions.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Completeness of routes | Does the map include flags, rule publication, scripts and automation? |
| Batch size | Does the design keep changes small and frequent instead of adding gates? |
| Blast radius | Does a bad fraud rule reach a small ring first, and does a malformed one leave nodes on the last good rule set? |
| Flag hygiene | Would the reused fraud-rule flag be impossible under your rules? |
| Honest freeze | Is the freeze scoped by dependency and risk, and is every exception in the change record? |
| Review economy | Does human attention go to invariants and high-tier changes? |

#### Where you now stand

You can now treat change as the leading cause of outages without trying to stop it: design a pipeline as a sequence of questions, choose each change's blast radius, stage configuration and data like code, keep flags from becoming debt, scope a freeze honestly, and spend human review where machine-written change can do most harm. Chapter 9 turns from the changes we make to the failures we must withstand.

### References

- Jez Humble, David Farley — [*Continuous Delivery*](https://www.informit.com/store/continuous-delivery-reliable-software-releases-through-9780321601919). Addison-Wesley, 2010.
- U.S. Securities and Exchange Commission — [*In the Matter of Knight Capital Americas LLC*](https://www.sec.gov/files/litigation/admin/2013/34-70694.pdf). SEC, 2013 — free online.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- CrowdStrike — [*Channel File 291 Incident: Root Cause Analysis*](https://www.crowdstrike.com/wp-content/uploads/2024/08/Channel-File-291-Incident-Root-Cause-Analysis-08.06.2024.pdf). CrowdStrike, 2024 — free online.
- Google Cloud — [*Incident report, 12 June 2025*](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW). Google, 2025 — free online.
- Matthew Prince — [*Cloudflare outage on November 18, 2025*](https://blog.cloudflare.com/18-november-2025-outage/). Cloudflare, 2025 — free online.
- Nicole Forsgren, Jez Humble, Gene Kim — [*Accelerate*](https://itrevolution.com/product/accelerate/). IT Revolution, 2018.
- DORA — [*Streamlined change approval*](https://dora.dev/capabilities/streamlined-change-approval/). dora.dev — free online.
- Clare Liguori — [*Automating safe, hands-off deployments*](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/). Amazon Builders' Library — free online.
- Audris Mockus, Rui Abreu, Peter C. Rigby, et al. — [*Leveraging Risk Models to Improve Productivity for Effective Code Un-Freeze at Scale*](https://dl.acm.org/doi/10.1145/3722216). ACM TOSEM, 2025.
- DORA — [*Accelerate State of DevOps Report 2024*](https://dora.dev/research/2024/dora-report/) and [*State of AI-assisted Software Development*](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report). Google Cloud, 2024–2025 — free online.
- Stoyan Nikolov, et al. — [*How is Google using AI for internal code migrations?*](https://arxiv.org/abs/2501.06972). ICSE-SEIP, 2025 — free online.
- Ziqian Zhong, Aditi Raghunathan, Nicholas Carlini — [*ImpossibleBench*](https://arxiv.org/abs/2510.20270). arXiv, 2025 — free online.
- Linux kernel documentation — [*AI Coding Assistants*](https://kernel.org/doc/html/latest/process/coding-assistants.html). kernel.org, 2025 — free online.
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage — [*Building Evolutionary Architectures*, 2nd ed.](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/). O'Reilly, 2022.

---

## Chapter 9: Designing for Failure — Stability Patterns and Chaos Engineering {#ch9}

> "A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable." — Leslie Lamport

Every system fails, some in small pieces and some all at once, and the difference is rarely luck. A failure that stays small was usually designed to, by someone who imagined it and drew a line it could not cross. A failure that spreads has usually found a path built for some other purpose, very often a path built for recovery. This chapter is about those lines and paths, and about finding out, on a day of our choosing, whether the lines hold.

Our field offers no clearer lesson than 15 January 1990, when AT&T's long-distance network spent about nine hours unable to complete a great many of its calls. Nothing physical had broken. Weeks earlier the company had installed new software on its 114 4ESS switches, changing the code that ran when a switch recovered from a fault and told its neighbors it was back in service. In that C code, a `break` inside an `if` clause within a `switch` statement ended the enclosing block too early. The flaw lay quiet until one switch in New York suffered a minor fault and, on returning to service, sent its neighbors recovery messages. A neighbor that received a second such message while still handling the first hit the defect, corrupted its data and reset itself; when it came back, it announced its own recovery, and its neighbors fell over in turn. The cascade rolled across the network, as Figure 9.1 shows, until engineers cut the signaling load enough for the switches to settle and reinstalled the previous software.

{% include diagrams/fig-9-1.svg %}

*Figure 9.1 — The AT&T cascade of 15 January 1990. Each switch's recovery announcement reset its neighbors, and each reset produced the next announcement. The loop that sustained the outage is the recovery path itself.*

Every switch could recover from its own faults, on the assumption that failures would be independent. But all 114 ran the same code, and the defect sat in the recovery path, the code that runs least and matters most. What kept the outage alive was a feedback loop in the switches' own protocol, which needed no excess of ordinary traffic. Redundancy protects against independent failures and does nothing against common ones; a fleet running identical software is, for the purposes of its defects, one machine.

Encore learned a smaller version of this lesson. Its first big outage, the payment service provider (PSP) slowing from 200 ms to 8 s and the retry storm that followed, was a cascade of reasonable defaults, and [the Architecture book](https://oleksiyp.github.io/arch-book/#anatomy-of-a-self-inflicted-outage) named the patterns that answered it. This chapter is about operating them, and ends with the quarterly game days of the Reliability team, Encore's ten site reliability engineers. (Chapter 1's [map of Encore](/prodsys-book/ch/1/#encore) shows where each piece sits.)

### 9.1 Integration Points and Cascading Failure

#### Where faith is required {#where-faith-is-required}

An **integration point** is any place where one component depends on another across a boundary it does not control: a network call, a shared database, a queue, a third-party API. Michael Nygard called integration points the number-one killer of systems, and the reason is structural. Across a boundary a call can hang, return garbage, or succeed on the far side while the caller concludes it failed, and the caller has no means to tell which. What it cannot verify, it must take on faith.

A **cascading failure** is one in which the failure of one component raises the load or latency on others until they fail too, along the dependency graph. The most dangerous integration point is the one that has slowed down rather than stopped. A dead dependency refuses quickly; a slow one holds a thread, a connection and a queue slot for as long as we are willing to wait, and software left to its defaults is willing to wait a very long time.

#### Keeping a register {#keeping-a-register}

A team should know every one of its integration points. Dependency review is an old part of launch practice at Google and Amazon, and Encore's version is an **integration-point register** in each service catalog entry, recording per dependency the timeout, retry policy and breaker, what the service does when the dependency is slow or down, and the date the team last *saw* that behavior. The last column is Encore's addition, and the one that matters. For Orders & Payments the register runs to 11 rows, led by the two PSPs; for Seat Inventory, which deliberately depends on almost nothing, it runs to three. Writing it exposes dependencies nobody chose, such as a logging library that blocks when its buffer fills. And a register goes stale with every release.

**Recap.** Integration points are where our system takes another's behavior on faith, and cascades travel along them, most often when a dependency slows. Identical components fail together. A register that records when each failure behavior was last observed shows which assumptions were checked.

**Exercise 9.1.** Write the integration-point register for one service you run. For each row, fill in when you last saw the "slow" behavior happen. How many rows have no date?

### 9.2 Timeouts, Retries, Circuit Breakers, and Backpressure

#### Timeouts derived from budgets {#timeouts-from-budgets}

A **timeout** is a caller's promise to itself about how long it will wait. Most production timeouts are library defaults that nobody chose. The discipline is to derive each from a **latency budget**, the time the user-facing operation may take end to end, divided among the calls that serve it, as Figure 9.2 shows for Encore's 3 s checkout.

| Hop | Budget share | Timeout | Retries in path | Normal p99 |
|---|---|---|---|---|
| Edge and gateway | 150 ms | n/a | none | 40 ms |
| Orders: confirm hold with Seat Inventory | 300 ms | 250 ms | one, if budget remains | 60 ms |
| Orders: fraud signal from Bot Screening | 200 ms | 150 ms | none; fail open with a flag | 70 ms |
| Orders: charge via PSP | 800 ms | 800 ms | none in path; reconciled later | 450 ms |
| Orders: write order, emit `OrderPlaced` | 250 ms | 200 ms | one | 50 ms |
| Margin for queuing and the fan's network | 1,300 ms | | | |

*Figure 9.2 — The 3 s checkout budget, divided. Each timeout sits well above the dependency's normal tail and within its share of the budget. The large margin is deliberate: on an on-sale morning, queues are where the time goes.*

Marc Brooker's advice, from Amazon's practice, is to choose the rate of false timeouts we can tolerate and read the timeout off that percentile, p99.9 for one call in a thousand; a timeout just above p99 fails one healthy call in a hundred by design. Encore's timeouts sit near each dependency's p99.9.

Three practices make the table work. With **deadline propagation**, the caller sends the absolute time by which it needs an answer, and each callee works only while it lies ahead; Encore's gRPC calls carry deadlines, and each service passes its deadline on to its own calls, as Chapter 5 asked of trace context. Its twin is **cancellation propagation**: when a caller gives up, the cancellation travels down the chain and the callees stop working on an answer nobody will read. And a timed-out side effect is *unknown* until reconciled. A PSP charge that timed out may have succeeded, so Orders reconciles it later under the same idempotency key and never retries it in the fan's request.

#### Retries with jitter and a budget {#retries-with-jitter}

A retry is a bet that the failure was transient. Placed by one client it is a good bet; placed by every client at once it is a denial-of-service attack on our own dependency, because clients that fail together and back off exponentially also retry together, in synchronized waves. **Jitter**, randomness in the wait before each retry, spreads the waves into a trickle, and Brooker's simulations showed "full jitter", a random wait between zero and the exponential ceiling, doing markedly better than backoff alone.

A **retry budget** caps retries in volume. Encore's mesh allows about 10% of ordinary requests per destination, as a token bucket that successes refill and retries drain: Google's ratio, tighter than the 20% Envoy and Linkerd ship by default. Retries happen at one layer only, immediately above the failing call, and only for idempotent operations, because layers multiply (Figure 9.3).

{% include diagrams/fig-9-3.svg %}

*Figure 9.3 — Load on a failing dependency when every layer above it retries. Three layers of three retries can multiply it 64 times just as the dependency is weakest, while a 10% budget holds it near normal.*

A budget does not limit first attempts, and clients sending them to a backend that rejects them still spend its capacity. The SRE book describes Google's answer, **client-side adaptive throttling**: each client counts the requests it sent and those the backend accepted over the last two minutes, and once requests exceed a small multiple of accepts it rejects new requests itself, before they leave.

```python
# Google SRE book, ch. 21. Counts cover a rolling two minutes.
def reject_probability(requests: int, accepts: int, k: float = 2.0) -> float:
    return max(0.0, (requests - k * accepts) / (requests + 1))

if random.random() < reject_probability(window.requests, window.accepts):
    return fail_locally(request)   # never reaches the backend
```

A healthy backend sees no throttling; one rejecting most of its traffic receives about twice what it can accept. One retry layer escapes the mesh entirely: fans refreshing the page, and the fan app's own retries, which Section 9.5 shows Encore discovering during a game day.

#### Circuit breakers as state machines {#breakers-as-state-machines}

The breaker's three states, *closed*, *open* and *half-open*, are familiar; its parameters are where it protects or harms, as Figure 9.4 shows in the terms of Resilience4j, a common Java library. A service mesh's "circuit breaker" is usually a concurrency limit with outlier ejection, so Encore's PSP breaker lives in the payment client inside Orders.

| Parameter | Encore's PSP breaker | Failure if set badly |
|---|---|---|
| Rolling window | 10 s | too long reacts slowly; too short flaps |
| Minimum volume before tripping | 50 calls | too low trips on two unlucky calls |
| Failure rate that opens it (timeouts count) | 40% | too low opens on normal noise |
| Slow-call threshold | 600 ms, for 50% of calls | at or above the 800 ms timeout, it never fires |
| Open duration | 5 s, growing to 60 s | too short hammers a sick dependency |
| Half-open probes | 5, all must succeed | too many re-trigger the overload |
| Scope | per PSP endpoint, per region | one global breaker makes a regional fault total |

*Figure 9.4 — The circuit breaker's tuning surface. The slow-call threshold must sit above the call's normal p99 and below its timeout, here 450 ms, 600 ms and 800 ms, or a PSP that is slow without failing outright never trips it.*

Requiring all five probes to succeed, stricter than Resilience4j's rate-based default, is Encore's choice: a flickering PSP costs more in unknown charges than extra seconds on the secondary. And Brooker warns that a breaker scoped wider than the failure it guards harms a sharded design: one sick shard trips it for every healthy key, so Encore's calls to the sharded Seat Inventory rely on deadlines and the retry budget instead.

A breaker also needs a fallback, or it merely produces errors faster. For payments, Encore's is a ladder of degraded modes. First the breaker on the primary PSP opens and moves *new* payment attempts to the secondary; attempts already in flight finish or fail where they started, because idempotency keys belong to one provider. If both providers are degraded, verified fans' seats are held as a **pending payment**: the hold runs up to 20 minutes instead of the usual 5, with a cap per fan. When a provider recovers, the fan is sent a link to complete payment, with strong customer authentication. Unpaid holds lapse, and the seats return to sale. Below that, checkout fails fast with an honest message, and the Gate slows admission. No rung issues a ticket without an authorized payment: European rules require the fan to authenticate a card payment as it happens, and Encore holds no card data. A degraded mode may shrink what we promise; it may never make the promise false.

Jacob Gabrielson warns that a fallback run only in emergencies tends to fail when needed, so Orders sends a small, steady share of ordinary payments through the secondary every day. A breaker that has not opened in a quarter is most likely guarding a healthy dependency, but it has not been *seen* to work either, and only fault injection, the subject of Section 9.5, can show it.

#### Backpressure {#backpressure}

**Backpressure** is the means by which a component that cannot keep up tells its upstream to slow down before it accepts work it cannot finish: queues are bounded, callers honor a "retry after" signal, and failure comes early. At Encore the chain ends at the Sale Gate, where fans are meant to wait.

**Recap.** Timeouts come from the user's budget and travel as deadlines with their cancellations; a timed-out side effect is unknown until reconciled. Retries need jitter and a budget, and clients can throttle themselves. Breakers must agree with the timeouts around them, and their fallbacks are ladders of smaller but honest promises, each run a little every day so we know it works.

**Exercise 9.2.** Build Figures 9.2 and 9.4 for one operation you run. Does any slow-call threshold sit at or above its timeout, and which of your fallbacks ran in production last week?

### 9.3 Overload, Load Shedding, and Tail Latency

#### Admission control at the Gate {#admission-at-the-gate}

**Admission control** decides at the entrance how much work to let in; **load shedding** discards work already inside that cannot be finished in time. The first is prevention, the second triage, and triage costs more, because the work it discards has already used capacity.

The Sale Gate is Encore's admission controller. It admits about 1,200 fans per second per event, keeping Seat Inventory below 80% of measured capacity, and everyone else waits with a visible queue position on a static page. Commercial waiting rooms from Cloudflare, Queue-it and AWS work the same way, with an operator-set rate.

The rate is a judgment, reviewed the Wednesday before each big on-sale and only as good as the load test behind it. Adaptive limits are proven one level down, where Netflix's concurrency-limits library and Envoy's adaptive concurrency filter bound a server's in-flight work by the latency it observes, and Encore's services run the Envoy filter. A waiting room steered by a downstream service's latency is younger practice, so the Gate's rate stays a human judgment for now.

#### Shedding behind the gate {#shedding-behind-the-gate}

Retries, a cold cache or a slow dependency can still overload a service behind the Gate. Encore's services therefore tag each request with a **criticality class**, as the SRE book describes: `checkout`, `browse` or `background`, shed in reverse order.

Shed early, before expensive work is spent on a request that will be discarded. Measure pressure by *time in queue*, the insight of Kathleen Nichols and Van Jacobson's controlled-delay algorithm for routers (2012), which Facebook later carried into its RPC servers, since a request served after its deadline wastes capacity twice. Under severe overload, serve the newest requests first, as Facebook's servers do, because their callers are still listening. Each of these policies trades fairness for goodput. Write the trade-off down, or during an incident the policy will look like a bug.

#### Metastable failures {#metastable-failures}

[The Architecture book](https://oleksiyp.github.io/arch-book/#anatomy-of-a-self-inflicted-outage) borrowed a term from Nathan Bronson and colleagues (2021): a **metastable failure** persists after its trigger is removed, because the system's own response keeps it failed. A *vulnerable state*, typically efficient operation near capacity, meets a *trigger*, and a *sustaining effect* keeps the system down. Such failures are common: Lexiang Huang and colleagues found them at 11 organizations, including at least four of 15 major AWS outages, with retries the commonest sustaining effect.

AT&T's collapse had the same shape: the trigger was over in seconds, and the network stayed failed for hours. Its sustaining effect, though, was the recovery protocol itself, which is why the cure needed a software rollback as well as less load. Encore's PSP outage had the classic structure, with retries and an eager autoscaler sustaining what the slowdown began.

A metastable system will not recover when the trigger is fixed, and often not when cold new capacity arrives, because the loop absorbs that capacity too. It recovers when load falls below the level at which the loop dies: shedding far more than feels reasonable, retries off, traffic readmitted in steps. In a metastable failure the cure always looks like an overreaction, and runbooks should say so in advance, since nobody at 3 a.m. wants to be the person who turned away 70% of the traffic on purpose. Better still is to find the loop first: Encore's load tests push Seat Inventory past the point where goodput stops rising, then return the load to normal and check, as the SRE book advises, that the service recovers unaided.

#### Tail latency under load {#tail-latency-under-load}

Overload shows first in the tail. **Hedged requests**, from Dean and Barroso's "The Tail at Scale" (2013), send a second copy of a slow read to another replica; they cut the tail, but hedging during overload adds load just when the system can least absorb it. Encore hedges only idempotent seat-map geometry reads, only after p95, within a budget of about 5% extra requests that caps hedging when the system is busiest, and cancels whichever copy loses.

**Recap.** Admission control at the entrance is cheaper than shedding inside, and the Gate's rate is a judgment to keep reviewing. Inside, we shed by criticality and time in queue. Metastable failures are common and outlast their triggers; ending one takes more shedding than feels reasonable, and a load test that checks for recovery finds them first.

**Exercise 9.3.** Find an incident where load stayed high after the cause was fixed. What was the sustaining effect, and what runbook text would have let the on-call engineer shed enough to break it?

### 9.4 Cells, Regions, and Blast Radius

#### A ladder of bulkheads {#a-ladder-of-bulkheads}

The **blast radius** of a failure is the set of users, tenants or functions it can affect. [The Architecture book](https://oleksiyp.github.io/arch-book/#anatomy-of-a-self-inflicted-outage) used a ship's bulkheads for shrinking it; operations adds that bulkheads come in sizes, each containing a different class of failure.

| Boundary | Contains | Does not contain | At Encore |
|---|---|---|---|
| Thread or connection pool | one slow dependency | a crash of the process | a separate PSP pool in Orders |
| Instance or pod | a crash, a memory leak | a fault every pod shares | pods spread across zones |
| Shard | a hot or failed partition | a defect every shard runs | four shards per large event |
| Cell | a poison tenant; a bad deploy, reaching cells in turn | the shared router and control plane | Professional cells; self-service cells of ~50 |
| Availability zone | a power or network fault; a bad deploy staged by zone | a regional dependency | every tier across three zones |
| Region | a regional outage; a bad deploy staged by region | a global control plane; a latent defect already everywhere | two EU regions; event writes pinned to one |

*Figure 9.5 — The ladder of bulkheads. The "does not contain" column of each row is the reason the next row exists.*

Any rung contains a bad deploy if the change reaches it at a different time from its neighbors, which is why Amazon deploys to one box, then one zone, then region by region, and Microsoft rolls Azure changes through canary regions first; the cell is the smallest rung at which a whole application can be updated on its own. No rung contains a latent defect already everywhere when its trigger arrives, as AT&T's was. Google Cloud relearned this on 12 June 2025 (Chapter 8): new code in Service Control had been rolled out region by region, but its flawed path first ran when a policy change, replicated globally in seconds, reached every region at once, so the staged code rollout did not help.

#### Cells for tenants {#cells-for-tenants}

A **cell** is a complete, independent copy of the application serving a fixed slice of customers: a blast radius drawn on purpose. Encore's Professional tenants live in Kubernetes cells, and about 500 self-service venues in serverless cells of about 50. Every deploy and configuration change reaches a *canary cell* of internal and early-adopting tenants first, then the rest in the waves of Chapter 8, so a defect that would have reached 500 venues reaches about 50.

Big stadium tours carry more than one steel stage structure, so a storm delaying one build does not cancel the next night, and cells give Encore that independence, though two stages built from one faulty drawing fail alike, as do cells running one faulty release. Cells also share the router that maps tenants to them, which AWS's cell guidance asks to be the thinnest layer possible and which at Encore is the least often changed component it owns, because its failure crosses every bulkhead at once.

#### Shuffle sharding {#shuffle-sharding}

Within a pooled cell, **shuffle sharding**, which Colm MacCárthaigh described from AWS practice, gives each tenant a small random *combination* of workers instead of a fixed partition. In each self-service cell, Encore divides its import and webhook workers into eight lanes and assigns each venue two, which gives 28 possible pairs. Figure 9.6 shows one venue's runaway import flooding its two lanes.

{% include diagrams/fig-9-6.svg %}

*Figure 9.6 — Shuffle sharding across a self-service cell's eight lanes. A runaway venue floods its own two lanes; neighbors sharing one of them keep working on the other, and in a cell of 50 one or two neighbors, on average, hold the same pair and are hit.*

The isolation is cheap but conditional. First, work must move: a neighbor sharing one flooded lane is protected only if its consumers take its work from the other lane, as MacCárthaigh's account assumes and Encore's consumers do. Second, pairs repeat. Any one neighbor shares the runaway venue's exact pair about one time in 28, but a cell holds 49 neighbors and only 28 pairs, so on average one or two are hit in full and several more run on one lane until the flood clears. Encore spreads the repeats evenly and accepts the rest; fixed partitions of two lanes would let a runaway venue take about 12 neighbors down.

#### Static stability {#static-stability}

A system is **statically stable** when its data plane keeps working, unchanged, while its control plane is impaired, so that recovery never depends on creating, scaling or reconfiguring anything. The idea is old; the name is AWS's, and its lesson is that the control plane is likeliest to be overwhelmed exactly when everyone needs it.

At Encore the tenant-to-cell routing table is cached on every edge node, with an alert when the copy grows old. Each tier carries enough capacity that losing a zone needs no scaling. And the seat ledger's replicas in the other region and the witness already hold every committed write, so a region failover elects a leader among running copies and builds nothing, as Chapter 10 tests. The price is idle capacity; in return, recovery uses only what is already running.

**Recap.** Bulkheads come in sizes, chosen by the failure we fear. Any rung contains a bad deploy that reaches it at its own time, cells are the smallest such rung, and none contains a defect already everywhere. Shuffle sharding needs work that can move, and static stability keeps recovery off a stressed control plane.

**Exercise 9.4.** Draw Figure 9.5 for your system. Which shared component (a router, an identity provider, a global configuration store) crosses every rung, and does its data reach production in stages as your code does?

### 9.5 Chaos Engineering and Game Days

#### The experimental attitude {#the-experimental-attitude}

Everything in this chapter is a claim about behavior under conditions we hope never to see, and such claims decay. Chaos engineering tests them on purpose.

At Amazon in the early 2000s, Jesse Robbins, a volunteer firefighter as well as an engineer, ran *GameDays* that took real capacity out of service to see how systems and people coped; at Netflix, moving onto AWS from around 2008, engineers made failure routine on purpose, and Chaos Monkey was the famous result. The *Principles of Chaos Engineering* define **chaos engineering** as "the discipline of experimenting on a system in order to build confidence in the system's capability to withstand turbulent conditions in production," and ask for a hypothesis about steady state, real-world events, production experiments, automation and a minimized blast radius. The practice is now widely adopted, though the evidence that it improves outcomes is still mostly practitioners' reports; they agree that experiments belong in production only once observability, automatic aborts and on-call can catch the problems their experiments expose.

The word that matters is *experiment*. A test checks a known property; an experiment asks a question whose answer we do not know. "Does the breaker open when the PSP is slow?" is a test. "What happens to checkout when the PSP is slow during a shard failover?" is an experiment.

#### Game days {#game-days}

A **game day** is a scheduled exercise in which people and systems face an injected failure together, with observers recording what the people did as carefully as what the machines did. Google's annual Disaster Recovery Testing (DiRT), which Kripa Krishnan described in 2012, and Slack's Disasterpiece Theater are good models, and both follow each finding until it is fixed.

Encore calls its quarterly game days *tech rehearsals*, after the theater's run of every cue before opening night. Unlike a show, a system changes with every release, so its rehearsal proves only that it worked that day.

#### The tech rehearsal {#the-tech-rehearsal}

Last quarter's rehearsal combined two failures Encore had only drilled separately, and was the quarter's evidence that the PSP breaker opens. It ran in production on a Tuesday morning against the synthetic buyers' hidden test event, given four shards of its own:

```yaml
experiment: psp-latency-during-shard-failover
hypothesis: >
  Synthetic checkout success stays at or above 97% within the 3 s budget;
  the primary PSP breaker opens within 15 s; new payments move to the secondary;
  shard 2 failover rejects writes for under 60 s; no seat is sold twice.
target: test event only (tenant: encore-internal), home region
injections:
  - at: T+0     psp_latency: { psp: primary, added: 2s, share: 60% } # mesh fault
  - at: T+5m    shard_failover: { event: test, shard: 2 } # runbook step, by hand
abort_if:
  - real-event checkout SLO burn rate > 2x for 5m
  - any duplicate SeatSold for the test event
duration: 30m
```

The delayed calls hit the 800 ms timeout and counted as failures, the breaker opened in 9 s, and new payments moved to the secondary; the last unknown attempt on the primary was reconciled within four minutes of the injection ending, and no hold needed to become a pending payment. The fenced failover on shard 2 rejected writes for 38 s, and no seat was sold twice. Two findings were unwelcome. Jonas, the Seat Inventory engineer performing the failover, had never done one by hand, and the runbook named a flag removed two releases earlier, so the step took 11 minutes instead of 3. This is the deskilling Chapter 3 described. And the fan app retried each rejected hold three times at fixed one-second intervals, a layer the mesh's budget never saw; the app team added jitter and the adaptive throttle of Section 9.2.

One more line in the observers' log deserves recording. While the synthetic buyers retried their rejected holds, Bot Screening's velocity rule quarantined several of them. The log marked it as expected, since synthetic traffic looks synthetic, and the item was closed. Nobody asked what the same rule would make of a large crowd of real fans retrying in the same way.

A game day finds, cheaply and on a quiet morning, which resilience claims are still untested, and the Reliability team reports each quarter how many were fixed and how many merely closed.

**Recap.** Chaos engineering tests resilience as a hypothesis, in production and within a bounded blast radius, once the means to observe and abort are in place. Game days add the people, and often show that the human side of recovery has decayed faster than the automation.

**Exercise 9.5.** Design a game day combining two failures you have drilled only separately, with a hypothesis a user would recognize, abort conditions, and the human step you suspect nobody has practiced.

### Kata: Kick-Off

> **Your brief: "Matchday."** A sports-streaming service in five EU countries, with 40 engineers. Peak evenings reach 1.4 million concurrent viewers, and in the 10 minutes before a top-league kick-off, stream starts rise 30×. Every start needs a license from one of two digital rights management (DRM) providers. All competitions share one pool of playback-API instances, and the Sunday-evening derby alone takes 40% of it. Last month one DRM provider's latency rose from 120 ms to 5 s for 25 minutes; retries from the player SDK, the playback API and fans restarting the app quadrupled license requests, the pool saturated, and starts failed for every competition, even those licensed through the other provider. The provider recovered at 20:31; Matchday recovered at 21:40, and some 210,000 viewers missed the whole first half.

**Deliverables:**

1. **Integration-point register** — the stream-start path, with timeouts derived from a 4 s time-to-first-frame budget.
2. **Retry and breaker design** — one retry layer with budget and jitter, throttling in the player SDK, and a per-provider DRM breaker consistent with its timeout.
3. **Shedding and metastability analysis** — admission control for the surge, the shedding order, last month's vulnerable state, trigger and sustaining effect, and the runbook text that would have ended it by 20:40.
4. **Blast-radius plan** — the rungs of Figure 9.5 Matchday needs, so the derby cannot starve other matches and a playing stream survives its providers.
5. **Game-day plan** — one experiment with hypothesis, injections, abort conditions and the human step to observe.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Budget-derived timeouts | Does each timeout follow from the 4 s budget and a chosen false-timeout rate? |
| One retry layer | Are the player SDK's and the fans' own retries counted? |
| Shedding order | Are playing streams protected before new starts? |
| Sustaining effect | Does it explain the 69 minutes after the provider recovered? |
| Isolation and static stability | Is the derby contained without a cell per match, and does a playing stream need nothing new mid-incident? |
| Experiment honesty | Could the hypothesis fail, and is there a clear point to stop? |

#### Where you now stand

You can now trace failure along integration points, derive timeouts from budgets, tune retries and breakers, shed load, recognize a metastable failure, choose the bulkhead that fits the failure you fear, and test it all with people in the room. Each assumes the data underneath survives, and a restart cannot bring back lost data. Chapter 10 turns to state, and to disaster recovery practiced until it is routine.

### References

- Michael T. Nygard — [*Release It!*, 2nd ed.](https://pragprog.com/titles/mnee2/release-it-second-edition/). Pragmatic Bookshelf, 2018.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/), chapters 21 and 22. O'Reilly/Google, 2016 — free online.
- Marc Brooker — [*Timeouts, retries, and backoff with jitter*](https://builder.aws.com/content/3EumjoZascWd1oZiEgL8ORlv3qE/timeouts-retries-and-backoff-with-jitter). The Amazon Builders' Library — free online.
- Jacob Gabrielson — [*Avoiding fallback in distributed systems*](https://aws.amazon.com/builders-library/avoiding-fallback-in-distributed-systems/). The Amazon Builders' Library — free online.
- Nathan Bronson, Aleksey Charapko, Abutalib Aghayev, Timothy Zhu — [*Metastable Failures in Distributed Systems*](https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s11-bronson.pdf). HotOS, 2021 — free online.
- Lexiang Huang et al. — [*Metastable Failures in the Wild*](https://www.usenix.org/conference/osdi22/presentation/huang-lexiang). OSDI, 2022 — free online.
- Ben Maurer — [*Fail at Scale*](https://queue.acm.org/detail.cfm?id=2839461). ACM Queue, 2015 — free online.
- Kathleen Nichols, Van Jacobson — [*Controlling Queue Delay*](https://queue.acm.org/detail.cfm?id=2209336). ACM Queue, 2012 — free online.
- Jeffrey Dean, Luiz André Barroso — [*The Tail at Scale*](https://doi.org/10.1145/2408776.2408794). Communications of the ACM, 2013.
- Clare Liguori — [*Automating safe, hands-off deployments*](https://aws.amazon.com/builders-library/automating-safe-hands-off-deployments/). The Amazon Builders' Library — free online.
- Google Cloud — [*Incident report, 12 June 2025*](https://status.cloud.google.com/incidents/ow5i3PPK96RduMcb1SsW). 2025 — free online.
- Colm MacCárthaigh — [*Workload isolation using shuffle-sharding*](https://builder.aws.com/content/3F06NpJ8YeoIGP8VHTw4n81pFn8/workload-isolation-using-shuffle-sharding). The Amazon Builders' Library — free online.
- Becky Weiss, Mike Furr — [*Static stability using Availability Zones*](https://builder.aws.com/content/3K9SiqiJ369TGkkGzqPM95BuYWI/static-stability-using-availability-zones). The Amazon Builders' Library — free online.
- [*Principles of Chaos Engineering*](https://principlesofchaos.org/) — free online.
- Kripa Krishnan — [*Weathering the Unexpected*](https://queue.acm.org/detail.cfm?id=2371516). ACM Queue, 2012 — free online.

---

## Chapter 10: Data, State, and Disaster Recovery {#ch10}

> Code can be redeployed. Data can only be remembered.

Everything said about change so far rests on a promise: if a release goes wrong, we can take it back. Canaries, flags and rollbacks (Chapter 8) all assume it. Data breaks the promise. A row written cannot be unwritten by redeploying anything, and replication copies a corruption to every replica. This chapter is about the part of production that remembers, and how to make its memory survive our mistakes, our machines and our adversaries.

The story every operations engineer eventually hears took place at Pixar in 1998, during the making of *Toy Story 2*. Someone ran a recursive delete, of the `rm -rf` kind, at the root of the film's directory tree. Oren Jacob, then an associate technical director, later recalled watching Woody's hat disappear, then his boots, then Woody, until the team pulled the plug. Most of the film was gone, and the backups had been failing unnoticed for some time. What saved it was luck: Galyn Susman, the supervising technical director, had been working from home after the birth of her child and kept a copy on her home computer. The team drove the machine to the studio wrapped in blankets, restored from it, and then spent days finding what the copy lacked.

The deletion was ordinary, a routine command in the wrong place, of the kind Jim Gray had in mind in 1985 when he found that administration and software caused far more outages of Tandem's systems than hardware did. The formal plan had failed unnoticed. The recovery came from a copy independent of the system in every way that mattered, and the people restoring it were improvising, because no one had ever practiced a restore.

Encore has better machinery than Pixar had and much the same exposure. Its seat ledger, the event log in which Seat Inventory sells each seat exactly once, commits every write to a majority of replicas in three EU locations. Its Finance ledger, the relational books fed by every completed sale, is backed up nightly and has never been restored in full. Its holds store is about to change shape under live traffic. Its game days have never failed over a whole region. By the end of the chapter all four will have been tested, and one will have failed instructively. ([Chapter 1's map](/prodsys-book/ch/1/#encore) shows where each sits.)

### 10.1 Why Stateful Systems Are Different

#### The asymmetry of state {#asymmetry-of-state}

A **stateful system** is one whose correct behavior depends on what it has remembered from earlier requests, so that losing or corrupting that memory is a failure even when every process is healthy. A stateless service is a function: replace, restart or roll it back, and it computes the same answers. A stateful one is a function plus a history, and history runs in one direction only.

The asymmetry appears in four places. A data change cannot be rolled back, only compensated by a forward change, so every migration must be safe if left half done. Copying state is bounded by physics, so restoring 4 TB takes hours however clever the tooling. A bug that writes bad data keeps failing every later reader until someone repairs it, which makes corruption the quietest and longest kind of outage. And replication, which protects us from losing a machine, copies our mistakes to every replica within milliseconds.

#### Classifying Encore's state {#classifying-state}

The first operational act for state is an inventory. Encore's is short, because most of Encore is stateless on purpose:

| State | Store | System of record? | Loss means | RPO | RTO |
|---|---|---|---|---|---|
| Seat ledger (event log) | Seat Inventory, event-sourced, four shards per large event | Yes | A seat sold twice or a fan charged for nothing | 0 | Minutes |
| Seat holds | Holds store, 5-minute expiry (up to 20 for a pending payment) | Yes, briefly | Fans lose seats mid-checkout | Minutes | Minutes |
| Orders and payments | Orders, with the two payment service providers (PSPs) as external records | Yes | Charges without tickets, reconcilable against the PSPs | Seconds | 30 min |
| Finance ledger | Relational, fed by `SaleCompleted` | Yes, for accounting | A failed nightly close; regulatory exposure | 15 min | 2 h |
| Catalog | Managed database | Yes | Stale listings, lost edits | Minutes | 1 h |
| Seat-map cache, search index, analytics | Derived | No | Slowness while rebuilt | n/a | Rebuild time |

*Figure 10.1 — Encore's state inventory. The third column matters most: derived data needs a tested rebuild rather than a backup, while systems of record need both a backup and a practiced restore.*

The distinction between systems of record and derived data, which Kleppmann develops at length, breaks one anxious question ("how do we protect our data?") into several small ones. The seat-map cache needs no backup, only a rebuild whose duration is known, and that duration, as Chapter 13 will show, matters. A rebuild needs its source retained and its duration timed.

**Recap.** State moves in one direction only: we can revert code but only compensate data. Copying it is slow, corrupting it is quiet, and replicating it spreads our mistakes. An inventory that separates systems of record from derived data is the first and cheapest act of control.

**Exercise 10.1.** Build Figure 10.1 for a system you know. Mark each store as system of record or derived, and for each derived store write down how it would be rebuilt and how long that would take. Which "derived" store turns out to have no source?

### 10.2 Backups That Restore — RPO, RTO, and Testing Recovery

#### What a backup is for {#what-a-backup-is-for}

[The Architecture book](https://oleksiyp.github.io/arch-book/#surviving-a-region) defined the recovery point objective (RPO) and recovery time objective (RTO); an operator treats them as claims awaiting a test. A **backup** is a copy of a system of record, held independently of it, from which a known past state can be restored within a stated time. *Independently* rules out a replica, which shares the system's fate for logical damage, and *within a stated time* makes it something we can count on in an outage. The data-integrity chapter of Google's *Site Reliability Engineering* puts it plainly: nobody really wants backups; what people want are restores.

{% include diagrams/fig-10-2.svg %}

*Figure 10.2 — RPO measures back from a failure to the last good copy, RTO forward to service restored; here for the seat ledger and the Finance ledger, beside what the Finance drills of Section 10.5 measured. The promise was kept only once the team changed what had to come back first.*

We picture a region burning down, but the common threats are humbler: a deletion in the wrong place, a bug writing bad data for a week, an adversary who encrypts the database and then hunts for the backups. Slow corruption needs a copy from *before* the bug; ransomware needs one the attacker cannot reach.

| Mechanism | Protects against | Restores | Weakness |
|---|---|---|---|
| Soft delete or delayed replica | Fat-fingered deletes and drops | Minutes | Only as long as the delay |
| Synchronous or quorum replica | Machine, zone or region loss | Seconds to minutes | Copies every logical error instantly |
| Physical backup plus write-ahead log | Deletion, corruption, region loss | Hours for terabytes | Whole database at once, within retention |
| Logical dump | Loss of one table or one tenant | Slow, but granular | Slow to take, slower to restore at size |
| Immutable copy in a separate account | Ransomware, insiders, compromised automation | As above, plus access delay | Must be designed in |
| Rebuild from source (event log, upstream) | Derived-data loss, some corruption | Replay time | Only if the source is retained |

No single row covers every threat, hence the layers. The SRE book puts the cheapest first, soft deletion, where a deleted row lingers for a grace period; its operational cousin is the **delayed replica** (PostgreSQL's `recovery_min_apply_delay`, MySQL's `SOURCE_DELAY`), which still holds, an hour later, the table someone has just dropped. **Point-in-time recovery**, restoring a physical base backup and replaying the write-ahead log to a chosen instant, is the workhorse for slow corruption, returning us to 14:02 last Tuesday, just before the bad deploy. It reaches back only as far as the log is retained, often a week to a month, and rewinding a whole database discards the good writes since, which must then be reconciled. Logical dumps add granularity: restoring one Professional tenant's database is gentler than rewinding a shared cluster.

#### Three copies, two media, one elsewhere {#three-two-one}

The **3-2-1 rule**, usually credited to the photographer Peter Krogh, says to keep three copies of data, on two kinds of media, with one copy off site. It has aged well because it is really about independence of failure. In the cloud, medium and site become accounts, regions and credentials: a backup the database's own role can delete is lost with the database when that credential is stolen. When NotPetya struck Maersk in 2017, recovery hinged on a domain controller in Ghana that a local power cut had kept offline.

At Encore, backups of systems of record go to a separate account, into a vault under a compliance-mode retention lock: for 35 days nobody, Encore's administrators and the account's root user included, can delete a recovery point or shorten its retention, and no approval can change that. Everything still adjustable, from backup plans and the access policy to who may restore, sits in governance mode behind multi-party approval, so that no single credential can quietly weaken it. The encryption key lives in the backup account too, since a backup whose key died with the source is no backup.

#### Restore testing {#restore-testing}

A backup has two failure modes, and only one is visible. The job fails, which an alert can catch, or it succeeds and its output cannot be restored, which only a restore catches. GitLab's outage of January 2017 is the modern case. Repairing replication late at night, an engineer wiped the data directory on the primary instead of the lagging secondary. The team then found that the daily dumps had been producing nothing, through a version mismatch whose failure emails were being rejected, and that disk snapshots had never been enabled for the database servers. A snapshot taken by hand six hours earlier, to refresh staging, saved the rest; those six hours, touching some 5,000 projects, were lost, and copying the snapshot back took most of a day. GitLab's postmortem traced the root cause to ownership: nobody had been responsible for testing the backup procedures.

One practice answers each failure mode. The first is to alert on a backup's absence, since a failing job may never manage to report its own failure:

```yaml
- alert: BackupStale
  expr: time() - backup_last_success_timestamp_seconds{kind="system_of_record"} > 26 * 3600
  for: 15m
  labels: {severity: page}
  annotations:
    summary: "No successful backup of {{ $labels.store }} for over 26 hours"
```

The second is continuous restore testing: scheduled restores into an isolated environment, verified against invariants such as row counts, totals that must balance and the latest known transactions, because a database that starts can still be missing a day. Encore restores the Catalog and every Professional tenant database weekly, checks them against the source and records the elapsed time. That duration is a service level indicator (SLI), and its upward trend is the earliest warning that an RTO is drifting out of reach.

A backup that has never been restored is a rumor about your data.

**Recap.** A backup is an independent copy that restores a known state within a stated time, and each threat needs its own kind of copy, including locked copies, with their keys, in another account. Watch backups for freshness, and prove them with scheduled, verified, timed restores.

**Exercise 10.2.** For your most important database, write down the date of the last full restore, how long it took and who did it. If you cannot answer, schedule one; if you can, compare its duration with your stated RTO and with the growth of the data since.

### 10.3 Schema Changes and Data Migrations

#### Two deploys and a promise {#two-deploys-and-a-promise}

A schema change is a deployment whose effects cannot be rolled back by redeploying. During any rollout two versions of the code run side by side, and both must work against the data at every moment, which rules out changing schema and code together. The answer is **expand and contract** (also called parallel change): expand the schema so that it supports both old and new code, migrate code and data, and only when nothing uses the old shape, contract it away: two deploys, and between them a promise that both shapes stay correct.

The civil engineer's version is replacing a bridge without closing the road: build the new span alongside, shift traffic lane by lane, then demolish the old one. The analogy breaks at the end, because no driver needs a demolished route, while software has readers with long memories: caches, stream consumers, mobile clients that update when their owners please and, at Encore, an event-sourced ledger whose past events will be read in their original shape forever. Contracting is safe only when we can show that no reader of the old shape remains.

#### The holds store, migrated under traffic {#holds-store-migration}

Encore's seat holds lived in a relational table keyed by `(event_id, seat_id)`, with a sweeper job deleting expired rows every few seconds. The sweeper had become an on-sale hot spot, so the On-Sale and Seat Inventory teams moved holds to a key-value store with native per-key expiry. The migration ran over three weeks, outside on-sale windows:

| Phase | Writes go to | Reads come from | Exit criterion |
|---|---|---|---|
| 1. Expand | Old table; new store in shadow | Old table | New store healthy for 7 days, write errors under 0.01% |
| 2. Backfill | Both | Old table | Five minutes elapsed: every live hold now exists in both |
| 3. Verify | Both | Old table, shadow reads compared | 72 h with zero unexplained mismatches |
| 4. Switch | Both | New store, behind a flag | One full on-sale on the new store within its service level objective (SLO) |
| 5. Contract | New store only | New store | Old writers removed; table archived, dropped 30 days later |

*Figure 10.3 — Expand and contract for the holds store. A flag or a deploy reverses each phase until the fifth, and the fifth waits until there is nothing left to reverse to. The thresholds are Encore's own; no standard exists.*

A **backfill**, the bulk copy of existing data into a new shape, is usually the riskiest phase: long-running, heavy on the database and racing live writes. Holds, however, live for five minutes. After five minutes of receiving every write, the new store held every live hold. Knowing the lifetime of your data can turn the hardest part of a migration into a wait, provided every write path really does write to both stores from the first minute.

That proviso was the real hazard. Without a transaction spanning both stores, one write can succeed while the other fails. So, as in Stripe's account of its online migrations, the old table stayed authoritative, a failed shadow write never failed a request, and phase 3 measured the drift. It found one class of mismatch: a hold released when a fan pressed "back" was deleted from the table but left to expire in the new store, so freed seats would have stayed held for five minutes.

The alternative to dual writes is **change data capture** (CDC), which reads each committed change from the old store's log and applies it to the new one. It removes the race between two writes, at a price: the new store lags, changes arrive at least once so the consumer must apply them idempotently, and there is now a connector to run, watch and recover. Encore's platform offers CDC on the paved road, so no single team carries that price alone. For large MySQL tables, tools such as `gh-ost` apply a similar idea, syncing a shadow table so that no `ALTER TABLE` holds a lock longer than an SLO allows; PostgreSQL leans instead on concurrent index builds and a short `lock_timeout` on every migration, and linters such as `strong_migrations` and `squawk` catch locking statements in review.

**Recap.** Schema changes cannot be reverted, so we expand before we contract and keep both shapes correct in between. A backfill is the riskiest phase unless the data's lifetime makes it trivial. Dual writes drift silently, so we measure the drift, or trade it for the lag and upkeep of change data capture.

**Exercise 10.3.** Take the next schema change on your team's roadmap and write it as a table like Figure 10.3. For each phase, name the exit criterion and the way back. Which phase has no way back, and what must be proven before it starts?

### 10.4 Replication, Multi-Region, and Failover

#### Lag and what it means {#lag-and-what-it-means}

**Replication lag** is the delay between a write being acknowledged on the leader and being applied on a replica; under asynchronous replication it is exactly the data a failover would lose. It is largest when write volume peaks, which is when trouble tends to come; GitLab's outage began with a replica too far behind to catch up. Lag approaching an RPO is one of the few causes that earns a page.

#### Zero RPO needs a third vote {#zero-rpo-needs-a-third-vote}

The seat ledger's RPO is zero, because a lost write there is a seat sold twice, and the only way to lose nothing is to acknowledge nothing until it is durable outside the region that wrote it. The obvious design, a synchronous standby in the second region, shows why. When the link breaks, the home region must choose. It can wait for a peer it cannot reach, and writes stop; or it can stop waiting, and the next write exists in one place only, so the zero RPO is abandoned at exactly the moment it was bought for. The standby cannot tell a dead primary from a severed link, so promoting it is a guess, and a wrong guess is the split brain of the next subsection. Telling the two apart needs a third site with a vote.

So each seat-ledger shard is a **consensus group**, Raft-style in the manner Diego Ongaro and John Ousterhout described in 2014: its replicas commit a write only once a majority holds it durably, and elect their leader by majority vote. Each has five voting members in three EU locations: two in the event's home region, EU-1 or EU-2, in different zones, where the leader normally sits; two in the other serving region; and a **witness** in a third region, EU-3, a replica that stores the log and votes but serves no traffic. A write is acknowledged once three of the five have it, the two home replicas and whichever remote member answers first, so every seat write pays one cross-region round trip, about 18 ms between nearby EU regions, which the 3 s checkout budget absorbs. **Group commit**, which gathers the writes arriving during one round trip into a single replicated batch, lets a shard sustain its 1,500 ordered writes a second.

The failure cases now resolve themselves by arithmetic. A lost node or zone moves leadership to the other home replica. A home region that loses one peer location keeps a majority, and fans notice nothing. A home region cut off from both holds two votes of five; its leader's lease lapses and it stops accepting writes, while the other region's two members and the witness, three of five, elect a leader there. Every acknowledged write was already on a majority, so the RPO stays zero; the RTO is the election plus re-routing the Gate and Orders, a matter of minutes; and because a minority can never commit, there is no split brain to repair.

None of this is novel: Google's Spanner, Amazon's DynamoDB multi-Region strong consistency and Aurora DSQL all offer two regions plus a witness, and CockroachDB states the same trade as a survival goal. The price is everywhere the same, latency on every write and a third site to operate. Encore pays it only for the seat ledger; its other stores' RPOs allow simpler asynchronous arrangements.

A majority cannot protect Encore from itself: a bad write reaches all three locations in 18 ms. So the ledger still has point-in-time backups, and corrupted projections can be rebuilt by replaying its event log, which only ever grows.

#### Split brain and fencing {#split-brain-and-fencing}

**Split brain**, failover's characteristic failure, is the condition in which two nodes both believe they lead and both accept writes, so that the data diverges in ways that may never be reconciled. A leader cut off from its peers, or paused by a long garbage collection, cannot know it has been replaced and carries on with complete confidence. Since the old leader may never hear of the handover, the protection must sit with the storage it writes to.

That protection is **fencing**: every leadership term carries a monotonically increasing number, a **fencing token**, and storage rejects any write bearing a term older than the newest it has seen. The idea draws on the leases Cary Gray and David Cheriton described in 1989, grants of authority that expire unless renewed, and on the numbered terms of consensus protocols. On Encore's Seat Inventory shards a new leader's first act is to record its term, and from that instant any write from the old leader fails, loudly and harmlessly. Fencing itself costs almost nothing. A takeover's cost is the wait for the old lease to run out, tens of seconds in which the shard accepts no writes; fencing makes that wait safe, since a deposed leader whose clock misjudges the lease is refused anyway.

{% include diagrams/fig-10-4.svg %}

*Figure 10.4 — Fencing on a Seat Inventory shard. The deposed leader is never asked whether it still leads; the storage simply refuses its stale term, and the refusal is how it finds out.*

#### Failing over a region {#failing-over-a-region}

Because Encore pins each event's writes to a home region, a regional failure becomes many small ones. The ledger's part, as we have seen, needs no human action. The rest, moving each event's home and redirecting the Gate and Orders to the new leaders, Encore automated as one operation but kept the trigger human.

The evidence for that choice is GitHub's outage of 21 October 2018. Maintenance broke connectivity between its US East Coast network hub and its primary data center for 43 seconds, and in that window its failover tooling, Orchestrator, did what it was built to do and promoted database primaries on the West Coast. When the link returned, some writes existed only in the East and others only in the West, and the site ran degraded for just over 24 hours while engineers reconciled them. Every component had behaved as designed, and GitHub's remediation was to stop Orchestrator promoting across regions. Within a region automated failover is right; across regions, a failover fired by a flapping link is a self-inflicted outage with the largest blast radius a company has.

**Recap.** Lag is the RPO of asynchronous replication. Zero RPO needs a majority across three sites, because two can only guess, and even a majority copies our mistakes. Fencing, enforced by storage rather than by leaders, is the cure for split brain. Region failover should be automated in its steps and human in its trigger.

**Exercise 10.4.** For one replicated store you run, find out what prevents an old leader from writing after a failover. If the answer is "it will notice it has been replaced," write down how long that takes and what it could write in the meantime.

### 10.5 Disaster Recovery as Practice, Not Plan

#### The plan on the shelf {#the-plan-on-the-shelf}

Most organizations have a disaster recovery (DR) plan; fewer have a DR capability. The difference is like that between an evacuation map and a fire drill: the map goes out of date as walls move, and only a drill shows it. Banking, where I spent much of my career, requires DR tests by rule, which ensures that a test happens; whether it teaches anything depends on whether people are allowed to fail.

DR drills are the game days of Chapter 9 aimed narrower: can people, tooling and permissions rebuild the system within the RTO someone promised? They also counter an irony from Chapter 3: the better the failover machinery, the less practiced anyone is on the day it fails.

An RTO is a hypothesis until a stopwatch has run against it.

#### The Finance ledger drill {#finance-ledger-drill}

In the spring the Reliability team ran Encore's first full restore of the Finance ledger: about 4.2 TB, with an RTO of two hours agreed when the database was a tenth of that size. The scenario: a corruption found at 09:00, repaired by restoring to 02:00, just after the nightly close.

| Step | Planned | Actual | What happened |
|---|---|---|---|
| Reach the backup account | 5 min | 1 h 40 min | One of two required approvers was on leave; the encryption key's policy did not grant the drill account |
| Restore base backup | 45 min | 3 h 10 min | Throughput was capped by the target volume's provisioned I/O, sized for normal running |
| Replay log to 02:00 | 20 min | 1 h 15 min | A month-end day's log, larger than the runbook assumed |
| Verify against PSP settlements and `SaleCompleted` | 30 min | 2 h 20 min | The verification queries had never been written; they were written during the drill |
| Repoint applications | 10 min | 35 min | A reporting job's connection string was hard-coded |
| **Total** | **~2 h** | **~9 h** | |

*Figure 10.5 — The Finance ledger restore drill. No delay came from the database engine.*

The drill missed its RTO more than fourfold and was the most useful day of Encore's quarter. The approval rule was right but untried; it now has a standby approver rota, and the key policy grants the recovery account. The throughput was physics: at the measured rate, 4.2 TB could not come back in two hours whatever the runbook said. So the team split the ledger: the current financial year (about 600 GB) restores first and becomes writable while history follows, with a warm standby for that slice. Finance, asked what it truly needed, named the next nightly close: two hours for the current year, a day for history. Three months later a second drill had the current year writable in 1 h 50 min.

Verification taught the subtlest lesson, the one Pixar learned in the days after its rescue: a restore is finished when someone with authority can say the data is right, and a running database proves little. Written in advance and run weekly against the scheduled restores, the verification queries turned two hours of improvisation into 10 minutes of reading a report.

#### The region failover game day {#region-failover-game-day}

The largest test came on a quiet October Tuesday, with no on-sale within a week. The Reliability team cut EU-1 off from EU-2 and the EU-3 witness, and an engineer then triggered the failover of every event homed there. Small events carried real traffic, alongside synthetic buyers.

The core held (Figure 10.6): EU-1's leaders lost their majority and stopped, EU-2 elected new ones with the witness's votes, fencing rejected a handful of late writes, and the whole failover took about four minutes. No hold or sale was lost. The surprises were at the edges. The Sale Gate had been pre-warmed only in EU-1, home to every on-sale until then, so the first buyers in EU-2 met cold starts. Bot Screening's risk data reached EU-2 by a daily copy, so the Gate there screened on yesterday's signals. And an Orders reconciliation job whose schedule named EU-1 explicitly did nothing for six hours. Each would have made a real failover worse; each became a ticket with an owner.

{% include diagrams/fig-10-6.svg %}

*Figure 10.6 — The October game day: EU-1 isolated, and EU-2 taking over with the votes of the EU-3 witness. The core held; the three findings sat at the edges, in things that had assumed EU-1 would always be home.*

A DR runbook is good when someone who has never performed the procedure can follow it at 3 a.m. So Encore's own rule, a step beyond the rotation of Google's DiRT exercises, is that each drill is led by someone who has not led one before, with an experienced engineer shadowing. Chapter 12 takes up how a real disaster is commanded.

**Recap.** DR is a capability that exists only where it is practiced. Drills time real recoveries against promised RTOs, and their findings concern permissions, throughput, verification and the system's edges far more than the database engine. A runbook is proven only when someone new to it can follow it.

**Exercise 10.5.** Plan a restore drill for one system of record. Write the scenario, target state and stated RTO, then list every permission, key and person the restore needs. Predict the duration of each step before you run it, and compare afterwards.

### Kata: The Stored-Value Card

> **Your brief: "Tidewater Transit."** Tidewater runs fare payment for a regional transport network: 2.4 million stored-value cards, 3,000 validators on buses and trams that buffer taps offline and upload when connected, and a top-up app. Balances live in one 9 TB PostgreSQL primary with an asynchronous replica in a second region, lagging several minutes in the morning rush. Backups are a nightly logical dump that takes seven hours and has never been restored in full. The regulator now asks for an RTO of four hours and an RPO of five minutes for balances. Last spring an engineer dropped a partition of tap history, rebuilt from validator logs over two weeks. Next year account-based ticketing changes the balance model. Tidewater has 14 engineers and one database specialist.

**Deliverables:**

1. **State inventory** — every store classified as system of record or derived, with RPO, RTO and rebuild path, in the shape of Figure 10.1.
2. **Backup and restore design** — the layered mechanisms, where each copy lives, which credentials can delete it, and the restore-testing schedule with its timing SLI.
3. **Migration plan** — expand and contract for account-based ticketing, with phases, exit criteria, backfill strategy and how dual-write drift will be measured or avoided.
4. **Failover design** — lag alerting against the five-minute RPO, how promotion is fenced, and who pulls the trigger.
5. **First DR drill** — scenario, predicted step timings, verification queries and who leads it.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Record versus derived | Does every store have either a backup or a rebuild procedure, and is it clear which? |
| Restore arithmetic | Is the four-hour RTO checked against measured restore throughput for 9 TB, rather than assumed? |
| Independence | Could one compromised administrator credential destroy every copy of the balances, or their key? |
| Reversible migration | Can each phase of the ticketing migration be reversed until the last, and is the last gated on proof? |
| Fencing | After a failover, what physically stops the old primary from accepting a top-up? |
| Practice | Is the drill timed, led by someone new to it, and expected to fail somewhere? |

#### Where you now stand

You can now inventory a system's state, design backups for the threats that actually occur, migrate data under traffic without losing the way back, reason about lag, quorums and fencing, and turn a DR plan into a timed capability. One threat in this chapter was deliberate: the adversary who looks for your backups before encrypting your data. Chapter 11 turns to that adversary, and to security as an operational discipline.

### References

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/data-integrity/), ch. 26. O'Reilly/Google, 2016 — free online.
- Martin Kleppmann, Chris Riccomini — [*Designing Data-Intensive Applications*, 2nd ed.](https://dataintensive.net/). O'Reilly, 2026.
- GitLab — [*Postmortem of database outage of January 31*](https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/). GitLab blog, 2017 — free online.
- GitHub — [*October 21 post-incident analysis*](https://github.blog/2018-10-30-oct21-post-incident-analysis/). GitHub blog, 2018 — free online.
- Diego Ongaro, John Ousterhout — [*In Search of an Understandable Consensus Algorithm*](https://raft.github.io/raft.pdf). USENIX ATC, 2014 — free online.
- Cary G. Gray, David R. Cheriton — [*Leases: An Efficient Fault-Tolerant Mechanism for Distributed File Cache Consistency*](https://pages.cs.wisc.edu/~remzi/Classes/739/Fall2015/Papers/leases89.pdf). SOSP, 1989 — free online.
- Stripe — [*Online migrations at scale*](https://stripe.com/blog/online-migrations). Stripe blog, 2017 — free online.
- Kripa Krishnan — [*Weathering the Unexpected*](https://queue.acm.org/detail.cfm?id=2371516). ACM Queue, 2012 — free online.
- Jim Gray — [*Why Do Computers Stop and What Can Be Done About It?*](https://www.cs.columbia.edu/~junfeng/08fa-e6998/sched/readings/why-do-computers-stop.pdf). Tandem Technical Report 85.7, 1985 — free online.

---

## Chapter 11: Security Operations — Secrets, Patching, and the Supply Chain {#ch11}

> "Security is a process, not a product." — Bruce Schneier

A system can be designed securely and still be run insecurely. [The Architecture book](https://oleksiyp.github.io/arch-book/#threat-modeling-engineering-not-paranoia) drew Encore's trust boundaries and gave every workload an identity. Drawings, however, do not rotate a key, rebuild an image or notice a partner's credential being used from an unfamiliar country. This chapter asks what security looks like as daily work: who does it, how often, with which instruments, and how we know it is still being done when nobody is watching.

The question is older than the cloud. On the evening of 2 November 1988 a program written by Robert Tappan Morris, a Cornell graduate student, was released onto the young internet from a machine at MIT, and within a day thousands of computers had slowed to a crawl. Nothing about the worm was exotic. It walked through doors that administrators had left open in the ordinary course of running their machines, and the response, improvised over mailing lists, was the first attempt at security operations.

Encore is, for once, in reasonable shape: its services carry cryptographic workload identities, its mesh enforces mutual TLS, and its golden path can sign images. What it lacks is the habit of exercising all of this, of rotating, patching, revoking and rehearsing on an ordinary Tuesday, so that by the extraordinary Friday these routines are already well practiced.

### 11.1 Security as an Operational Discipline

#### Four open doors {#four-open-doors}

The Morris worm deserves a close reading, because almost every lesson in this chapter is already in it. It had four ways in. It used the debug mode of `sendmail`, a convenience left enabled in many installations, to have the mail system run its code. It overflowed a buffer in `fingerd`, which never checked the length of its input. It exploited `rsh` and `rexec`, through which one machine let users from another log in without a password. And it guessed passwords from a short dictionary of common words.

Morris seems to have intended the worm to spread quietly, but it ignored a host's answer to "are you already infected?" about one time in seven, which turned a crawl into a flood of perhaps 6,000 machines; Eugene Spafford's analysis at Purdue remains the clearest account. Many sites cut themselves off from the network, which stopped the worm and also the fixes, and within weeks DARPA funded the Computer Emergency Response Team at Carnegie Mellon, now CERT/CC, so that next time there would be someone to call.

| Door in 1988 | What it really was | Its descendant today | The operational answer |
|---|---|---|---|
| `sendmail` debug mode | a convenience left on in production | an admin endpoint, a debug flag, a public bucket | configuration drift detected by policy as code |
| `fingerd` overflow | a known class of bug in a running binary | a critical flaw in a library the fleet shares | patch by rebuild, measured in hours (Section 11.3) |
| `rsh` trusted hosts | trust conferred by network location | a flat network, a shared service account | workload identity and short-lived credentials (Section 11.2) |
| weak passwords | long-lived, guessable secrets | a leaked API key, a phished administrator | rotation, scoping, strong sign-in and detection (Sections 11.2 and 11.5) |

*Figure 11.1 — The Morris worm's four doors and their modern descendants. Each door was opened by ordinary operation rather than by bad design, which is why each needs an operational answer.*

#### The adversary is part of the environment {#the-adversary-is-part-of-the-environment}

None of those doors was an architectural failure in the sense of [the Architecture book](https://oleksiyp.github.io/arch-book/#blast-radius-is-a-design-variable). They came from running systems day after day: conveniences never disabled, binaries never updated, trusts granted for a weekend and kept for years.

What distinguishes security from the reliability work of earlier chapters is an adversary who adapts: a failing disk does not learn from our defenses, whereas a defense that works this month teaches its opponent what to try next month. The hospital's infection control is a more faithful analogy than the fortress: a set of routines performed constantly by ordinary staff and tightened when a new organism arrives. The analogy fails at intent, since bacteria do not time their attack for our busiest hour. Encore knows this adversary personally: Bot Screening, the service that decides which sessions in the waiting room are human, tunes its rules weekly against people who rehearse on minor on-sales before the major ones. One caution follows, which Chapter 12 will make vivid: a rule that judges behavior is only as current as the behavior it was tuned on, and fans, too, change how they behave.

Encore organizes as Google's *Building Secure and Reliable Systems* suggests, treating security and reliability as one discipline. A Security Engineering team of six sits in the platform group, owning the security planes of the paved road and running detection rather than gating every change. The chores themselves (inventory, credentials, patches) belong to the teams that own the services, on the same scorecard as their service level objectives (SLOs). The arrangement holds only while the platform really supplies the secure defaults; without them, security shared by every team tends to end up owned by none.

**Recap.** The Morris worm entered through four ordinary doors, each with a modern descendant and each closed by routine rather than by a single design. Because the adversary adapts, security is a continuous practice, owned by the teams that run the services and made possible by a platform that ships secure defaults.

**Exercise 11.1.** For a system you run, fill in Figure 11.1's last two columns: name today's descendant of each of the four doors, and the routine (with its frequency) that keeps it closed. Which door has no routine at all?

### 11.2 Identity, Secrets, and Least Privilege in Practice

#### Credentials that expire on their own {#credentials-that-expire}

[The Architecture book](https://oleksiyp.github.io/arch-book/#103-securing-the-stack) argued that a credential which expires soon is worth little to a thief; operating the idea is harder. Encore's workloads prove who they are with SPIFFE Verifiable Identity Documents (SVIDs), short X.509 certificates issued by SPIRE, the reference implementation of the Secure Production Identity Framework for Everyone (SPIFFE). An agent on each node attests the workload by its Kubernetes service account and hands it a certificate naming it `spiffe://encore/inventory`, valid for one hour and renewed at the half-way point, SPIRE's own defaults.

Short-lived credentials move risk from confidentiality to availability. With one-hour certificates renewed at half-life, SPIRE can be down for only about 30 minutes before services begin refusing one another, in an outage both total and self-inflicted; in December 2018 an expired certificate in Ericsson software took down O2's mobile data network in Britain for most of a day. Encore therefore runs its issuer as a platform plane with an SLO stricter than that of any service it serves, with servers in both regions and an alert when any certificate passes 75% of its lifetime unrenewed.

People are the other half of identity, and the phishing page is the modern counterpart of the worm's password dictionary. Anyone at Encore with production or administrative access signs in with a FIDO2 security key or passkey, because a one-time code can be relayed by a convincing fake login page and a domain-bound credential cannot; US federal agencies have been required to do the same since 2022.

#### The secrets that remain {#the-secrets-that-remain}

Workload identity removes most secrets, never all. Encore still holds credentials from its two payment service providers (PSPs), signing keys for wallet passes and the keys its partners use against `api.encore.com`. These live in a secrets manager, injected at runtime, each with an owner, a rotation interval and a written rotation procedure, and the procedure matters more than the interval. A rotation never performed is a restore never tested, which Chapter 10 taught us to distrust: it fails when needed, usually because some consumer cached the secret at startup.

Encore learned what such a secret costs when a contractor for Rowmate, one of its resale partners, committed Rowmate's 26-month-old production API key to a public repository. Two signals arrived within minutes: secret scanning at the code host recognized Encore's registered key prefix (`enc_live_`), and Bot Screening flagged the same key calling the availability endpoints at 40 times Rowmate's usual rate, from a cloud region Rowmate had never used. The key was revoked 38 minutes after the commit, slow beside honeypot studies that find leaked keys tried within minutes. Push protection, which rejects a commit carrying a recognizable secret before it lands, now guards Encore's own repositories, but Rowmate's contractor was beyond its reach. What limited the damage was the key's scopes, decided years earlier.

The key carried `listings:read` and `resale:write`; it could not buy primary inventory, read fans' personal data or touch payouts. The gateway's audit log showed 14 minutes of scraping and two fraudulent resale listings, removed before anyone bought them. Rotation was harder: Rowmate needed a deploy to change keys, so both keys ran for an hour, the old one restricted to Rowmate's addresses. Partners now use OAuth client credentials bound to a client certificate (RFC 8705, as open-banking profiles require), with tokens that live 15 minutes. The cost moved to the partners, who must now run certificates; for those who cannot, DPoP (RFC 9449) binds the token to a key the client holds.

{% include diagrams/fig-11-2.svg %}

*Figure 11.2 — How long each of Encore's credentials lives, on a logarithmic scale, against the 38 minutes it took to revoke Rowmate's key. A token of the kind partners use now would have expired on its own before anyone revoked it.*

#### Least privilege drifts {#least-privilege-drifts}

Least privilege is granted once and eroded continuously, as incident-time permissions stay and service accounts outlive their services. Encore reverses that drift using evidence of actual use, as the clouds' access analyzers do: logs show which permissions each role used in the last 90 days, and every quarter the owning team receives a proposed policy without the unused ones, to accept, amend or defend (a permission needed only for regional failover looks unused most of the year).

The exception every organization needs and few design is **break-glass access**: a pre-arranged, audited path for a human to gain elevated access to production in an emergency. At Encore it requires a second engineer's approval, expires after 60 minutes, posts to the security channel and opens a review ticket. The cloud providers' guidance adds the condition that matters most, that the path must work when normal sign-in is what has failed, so Encore's emergency accounts sit outside single sign-on and the path is exercised at every quarterly game day.

**Recap.** Short-lived certificates remove most secrets but make the issuer a critical dependency. Humans need phishing-resistant sign-in; the remaining secrets need owners, rehearsed rotation and scopes that limit a thief. Least privilege drifts upward unless usage evidence turns it back, and break-glass access must be loud, brief and independent of the systems it exists to rescue.

**Exercise 11.2.** Pick one long-lived secret your system depends on and rotate it in a staging environment, timing each step. What consumer broke, and what would have happened in production at 3 a.m.?

### 11.3 Vulnerabilities, Patching, and the Fleet

#### Severity is not risk {#severity-is-not-risk}

In March 2017 the Apache Struts project published a fix for a remote code execution flaw; attackers entered Equifax through it roughly two months later and exposed personal data on about 147 million people. The useful lesson is that the organization had a patching process that did not reach the system that mattered, because nobody could see clearly which systems ran what.

Advisories, each with a Common Vulnerabilities and Exposures (CVE) number, arrive by the tens of thousands a year. The **Common Vulnerability Scoring System (CVSS)** scores each from 0 to 10 for how bad exploitation would be in general, which says nothing about whether anyone is exploiting the flaw or whether our code calls the vulnerable function. The **Exploit Prediction Scoring System (EPSS)**, maintained by the Forum of Incident Response and Security Teams (FIRST), estimates the probability of exploitation in the next 30 days; it knows nothing of our assets, and a low score lowers the odds without ruling exploitation out. The **Known Exploited Vulnerabilities (KEV)** catalog, published by the US Cybersecurity and Infrastructure Security Agency (CISA) since November 2021, lists flaws already being exploited. Encore adds two facts only it can know: whether the component faces the internet, and whether its code reaches the vulnerable function, which reachability tools inform but do not settle.

| Exploitation evidence | Exposure | Encore's response | Deadline |
|---|---|---|---|
| on the KEV list, or exploitation reported | internet-facing or on the purchase path | emergency change; compensating control at the edge first; check for prior compromise | 48 h |
| on the KEV list | internal only | expedited fix through the normal pipeline | 7 days |
| high EPSS, CVSS 7 or above | any | scheduled fix, next base-image rebuild | 30 days |
| low EPSS, code path unreachable | any | record as not affected, with the reasoning | next routine update |

*Figure 11.3 — Encore's triage policy, ordered by evidence of exploitation and by exposure so that urgency is spent where an attacker is most likely to arrive. The shape follows CISA's BOD 26-04; the deadlines are deliberately tighter.*

Encore need not defend this shape alone. In June 2026 CISA's Binding Operational Directive 26-04 replaced the KEV directive of 2021 and now sets federal remediation deadlines by four criteria: exposure, KEV status, whether exploitation can be automated, and how much control an attacker gains. Its tightest tier allows three days and adds forensic triage, a check of whether the door was used before it was closed, which Encore borrowed. Encore can set a stricter 48 hours only because its fleet can meet them.

#### Patching as a flow {#patching-as-a-flow}

The decisive move is to stop thinking of patching as an event. Encore never patches a running container but rebuilds the image from an updated base and redeploys through the ordinary pipeline, canaries included. Base images are rebuilt weekly whether or not an advisory demands it, and the scorecard reports the median age of each service's *running* images, since a fresh build that was never deployed has patched nothing. A fleet that rebuilds every week patches in a day when it must; a fleet that rebuilds once a year discovers, on the day it must, which services no longer build.

One of Encore's rules did not survive 2025. Dependency updates used to merge automatically whenever tests passed on a patch release. On 8 September 2025 an attacker phished the maintainer of `chalk`, `debug` and 16 other npm packages, with more than two billion weekly downloads between them, and published versions that rewrote cryptocurrency payment addresses in browsers. Days later the Shai-Hulud worm began stealing npm tokens and publishing infected versions of its victims' own packages; by the end of its second wave in November, more than a thousand packages had been compromised. Each attack travelled as an ordinary new release, and most were pulled within hours, so automation that merges a release minutes after it appears is precisely the conduit they need.

Encore's rule is now a **cooldown**: a version update must have been public for three days (patch releases) or seven (the rest) before automation proposes and merges it, so the ecosystem's scanners look first. Security updates skip the wait, since a fix for a flaw already public is the one release whose delay helps only the attacker. GitHub made a short cooldown Dependabot's default in July 2026:

```yaml
version: 2
updates:
  - package-ecosystem: "npm"
    directory: "/"
    schedule:
      interval: "daily"
    cooldown:              # version updates only;
      default-days: 7      # security updates are never delayed
      semver-patch-days: 3
```

Log4Shell, disclosed on 9 December 2021 with a CVSS score of 10, is the best-documented test of patching as a flow. The hard part was finding the library, often a dependency of a dependency or bundled inside a vendor's archive, and the first fixed release proved incomplete; in 2022 the US Cyber Safety Review Board called it an endemic vulnerability.

Encore's own test came this spring: a critical remote code execution flaw in a widely used XML parsing library, added to the KEV list within a day of disclosure. Its software bills of materials (Section 11.4) found 37 affected images across 23 services in 20 minutes, and a binary scan of third-party images found one more copy, inside a vendor's monitoring agent whose supplier published no bill of materials. Within 6 hours the gateway's web application firewall (WAF) blocked the known exploit pattern, and the logs were searched for earlier use of it, without result. By hour 30, 35 images were redeployed; by hour 48, all of Encore's own. The vendor's agent, confined by an egress rule, waited four more days for its supplier, and Encore now writes patch timelines into vendor contracts.

{% include diagrams/fig-11-4.svg %}

*Figure 11.4 — The spring parser flaw: affected images redeployed against hours since disclosure, from the counts Encore recorded. The curve is steep where Encore owns the build and flat where it waits on a supplier.*

**Recap.** CVSS measures how bad a flaw could be; exploitation evidence, exposure and reachability decide how fast we move, as CISA's directive now does. Patching works best as a continuous flow of rebuilds, measured by the age of what is running, with a cooldown on routine updates and none on security fixes.

**Exercise 11.3.** Reclassify the last 20 vulnerability findings for a service you own with Figure 11.3. How many were treated as urgent, and how many deserved to be? Then find out how old a release must be before your automation merges it.

### 11.4 The Software Supply Chain — Provenance, SBOMs, and Signing

#### When the build is the target {#when-the-build-is-the-target}

[The Architecture book](https://oleksiyp.github.io/arch-book/#103-securing-the-stack) told Thompson's warning and the xz backdoor of 2024, and there is no need to tell them again. Between them in time sits the case that changed operational practice most. In December 2020 it became known that attackers had compromised the build system of SolarWinds and inserted a backdoor into updates of its Orion software, signed with the company's own key and shipped to as many as 18,000 customers. The source code was clean and the signature genuine, but the shipped product carried the backdoor.

The **software supply chain** is everything that touches an artifact between a developer's keyboard and production. The frameworks that grew up after SolarWinds share one aim: each link should produce evidence that the next can check. A shipping container's numbered seal, checked against its manifest, works the same way. An intact seal shows that nobody opened the container in transit; it says nothing about whether the shipper loaded it honestly.

The pipeline is itself a chain of dependencies, as March 2025 showed. Attackers compromised `tj-actions/changed-files`, a GitHub Action used by some 23,000 repositories, and moved its version tags to a commit that printed pipeline secrets into build logs, many of them public; every workflow that referred to the action by tag ran the attacker's code at its next build. Encore's golden path applies GitHub's hardening guidance: third-party actions pinned to a full commit hash, which cannot be moved as a tag can; a workflow token with only the permissions the job needs; and cloud access through short-lived OpenID Connect (OIDC) federation, so that a leaked log holds nothing that lives long.

```yaml
permissions:
  contents: read
  id-token: write        # OIDC: cloud federation and keyless signing
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<full-commit-sha>   # pinned, never a tag
```

**Supply-chain Levels for Software Artifacts (SLSA)** grades the build link. In its build track, unchanged from version 1.0 to the current 1.2, Level 1 asks that the build produce **provenance**, a record of what was built, from which source, by which builder and with which inputs; Level 2 asks that a hosted build platform sign it; Level 3 asks that the platform be hardened, so that builds cannot tamper with one another or forge their provenance. SLSA is a consensus framework without published outcome data, cheap to reach on hosted platforms.

Signing was once held back by the burden of long-lived keys. **Sigstore** (Newman, Meyers and Torres-Arias, 2022), now used by npm, PyPI and Kubernetes, removed most of that burden: the build obtains a certificate valid for ten minutes, bound to its OIDC identity, signs with an ephemeral key and records the signature in a public transparency log. Verification asks whether this image was signed by *our* release workflow from *our* main branch, and must name both the identity issuer and the workflow, or any workflow anywhere will pass.

#### The bill of materials as an index {#the-bill-of-materials-as-an-index}

A **software bill of materials (SBOM)** is a machine-readable inventory of the components inside an artifact, with their versions, in a format such as SPDX or CycloneDX. Its value lies entirely in being queried: Encore indexes every SBOM, joined to the record of which image runs where, so that "where do we run this library?" is a query rather than a week of messages. An SBOM is only as complete as the tool that wrote it, and academic studies in 2023 and 2024 found generators that disagree widely and miss vendored or bundled components, the very hiding places of Log4j; hence the binary scan that found the vendor's copy. Where a component is present but not exploitable, a Vulnerability Exploitability eXchange (VEX) statement records why; VEX is young and its formats still compete, so Encore writes OpenVEX, which its scanner reads.

| Stage | Artifact produced | Check that consumes it | Failure behavior |
|---|---|---|---|
| Dependency resolution | lockfile with hashes | packages only from the curated proxy; unpinned ones rejected | build fails |
| Build (hosted, isolated) | image, SBOM, SLSA provenance | signed by the release workflow's identity | build fails |
| Registry | signature and attestations in the transparency log | nightly rescan of SBOMs against new advisories | ticket to the owning team |
| Admission to a cluster | — | policy verifies signer, builder and source branch | pod rejected, fails closed |
| Runtime | — | inventory of running images joined to SBOMs | drives Figure 11.3 triage |

*Figure 11.5 — Supply-chain controls on Encore's golden path. Every stage leaves evidence that a later stage checks automatically.*

Every service reaches SLSA Build Level 2; the purchase path and the identity issuer are built at Level 3 on isolated builders. Admission rejects any image not signed by Encore's release workflow, with a priced, logged exception path for vendor images. Failing closed makes the policy engine as critical as the control plane, so it runs replicated across zones. System namespaces are exempt, so that an unavailable engine cannot block the pods that would restore it.

#### Dependencies, human and machine {#dependencies-human-and-machine}

Each dependency means trusting its maintainers with every release they publish. I spent a decade maintaining a widely used open-source library, and the view from the other end is sobering: much of the world's software rests on a few volunteers' evenings. Encore asks of each new dependency whether it is maintained and by how many people, reading part of the answer from OpenSSF Scorecard, because a lockfile records what we chose but cannot tell us whether we chose well.

Coding assistants have added a new way to choose badly. Spracklen and colleagues, at USENIX Security in 2025, found that commercial models suggested packages that do not exist at least 5% of the time, and open models about a fifth. An attacker who registers such a name, a practice now called slopsquatting, waits for a developer to accept the suggestion; a researcher's harmless package under one hallucinated name drew tens of thousands of downloads. The defense is cheap: Encore's builds resolve packages only through a curated internal proxy, and adding one is a reviewed change.

The assistants are dependencies themselves. In July 2025 an attacker used an over-scoped token in the build configuration of Amazon's Q Developer extension for Visual Studio Code to commit a prompt telling the coding agent to wipe local files and cloud resources, and the release pipeline shipped it as version 1.84.0; only a syntax error kept it from running. Such an extension runs with a developer's credentials, so Encore pins these tools, admits them from an allowlist and gives agents scoped credentials of their own, as Chapter 14 describes.

**Recap.** SolarWinds and tj-actions showed that the build itself can be the target, so each link must produce evidence the next can check. SLSA grades the build, Sigstore makes signing cheap enough to be universal, and SBOMs pay only when queried and only as far as they are complete. What we depend on, chosen by people or suggested by their assistants, still needs judgment and a curated gate.

**Exercise 11.4.** Pick one image running in production today. Can you show, with evidence rather than memory, which commit and builder produced it and which version of its largest dependency it contains? List each step you could not answer.

### 11.5 Detection, Response, and Security Chaos Engineering

#### Detection that knows what normal looks like {#detection-that-knows-normal}

Nothing reduces the chance of compromise to zero, so the question becomes how quickly we notice. The Rowmate key was caught by a credential used at the wrong rate from the wrong place. Encore's detections are written mostly against identity: a workload calling a service it has never called, a break-glass session without a ticket, an image running that admission never saw. They are kept as code, tested with synthetic events and owned with a runbook, as Chapter 5 requires of any alert, and the logs they read are kept for weeks, because a baseline needs history.

Security incidents follow the command structure of Chapter 12 with three differences. The adversary may still be watching, so the channel is restricted and some actions wait until containment is ready. Evidence must be preserved before remediation destroys it, against the instinct to restart the broken thing, as NIST's revised guidance of 2025 insists. And there is a legal clock: under the General Data Protection Regulation (GDPR), a personal data breach must normally be reported to the supervisory authority within 72 hours of becoming aware of it, so a privacy lead belongs in the room from the first hour. Where the intruder holds credentials, containment is mostly revocation; a compromised host must also be isolated and rebuilt. An organization that can rotate any credential within an hour can contain an incident; one that needs a week leaves the intruder that week to use what was stolen.

#### Security chaos engineering {#security-chaos-engineering}

Kelly Shortridge and Aaron Rinehart, in *Security Chaos Engineering* (2023), point the experimental method of Chapter 9's game days at security controls: a control we have never seen trigger is a hypothesis, to be tested by introducing the condition deliberately, within bounds. The name is recent and its published evidence is mostly practitioner case studies, Capital One's among them, but the practices it gathers are older and well established: canary tokens, control validation, and purple-team exercises in which attackers and defenders work side by side.

At Encore's quarterly game day a canary key pushed to a test repository was detected in four minutes; an unsigned image deployed to a staging cell was rejected. The third experiment found a real gap. With the policy engine made unavailable, the admission webhook failed open, a setting chosen long before to keep deployments flowing during an upgrade, and an unsigned image deployed without complaint. Nobody had decided that security should yield to availability; a setting had, years earlier, and some widely used policy engines still ship with that default. The webhook now fails closed for the purchase path, with the engine replicated and a break-glass procedure for the day it fails. A control that has never been seen to fail has only been seen to be configured.

**Recap.** Detection works best against identity and behavior, written as code and owned like any alert. Security incidents need restricted channels, preserved evidence and a privacy lead watching the legal clock. Security chaos engineering, a young name for older practices, tests controls by provoking them, and its most useful findings are defaults that nobody remembers setting.

**Exercise 11.5.** Design one experiment for a security control you believe in: hypothesis, injected condition, blast-radius limit and the signal that would prove you wrong. Run it outside production and record what surprised you.

### Kata: The Spare Key

> **Your brief: "Hearthstay."** A vacation-rental marketplace: 85,000 listings from 30,000 hosts across southern Europe, 2.5 million guest bookings a year, a payment flow that charges guests at booking and pays hosts after check-in, and a partner API used by 40 channel managers and resellers that sync calendars and prices, each holding a static API key, the oldest from 2018. At check-in the platform sends guests their door codes. Twenty-six engineers run about 70 services on two Kubernetes clusters. An audit found base images up to 500 days old, no SBOMs, one service account shared by 11 services, and a payout-admin console reachable from the office network without multi-factor authentication. Last month a channel manager's key appeared in a public code repository; that week three hosts' payout bank details were changed, and nobody can say whether the key did it, because the gateway keeps logs for three days.

**Deliverables:**

1. **Credential inventory and plan** — every credential class, human and machine, with its age, scope and blast radius, and a sequenced migration to strong sign-in, workload identity and short-lived partner tokens.
2. **Triage policy** — Hearthstay's Figure 11.3, including the host mobile apps, which reach hosts only when they choose to update.
3. **Supply-chain path** — the Figure 11.5 stages adopted first, the SLSA level targeted in six months, and how SBOMs will be queried.
4. **Detection and response pack** — five identity-based detections, the log retention each needs, and a runbook for "a channel manager's key is leaked."
5. **Three security chaos experiments** — with hypotheses and limits, one of them on a change to a host's payout details.
6. **Break-glass design** — who may use it, how it expires, and how it works when the identity provider is down.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Blast radius | Could you say what a leaked partner key can do today, and what it could do after your plan? |
| Rotation realism | Does every rotation have a rehearsal, and does the plan survive a channel manager who deploys once a quarter? |
| Triage discipline | Is urgency driven by exploitation evidence and exposure, or by CVSS alone? |
| Evidence over memory | Can "where do we run this library?" be answered by a query in under an hour? |
| Failure posture | Which controls fail closed, which fail open, and did you choose each one deliberately? |
| Proportion | Is the program sized for 26 engineers, starting with the doors an attacker would try first? |

#### Where you now stand

You can now treat security as routine work: run credentials that expire and rotations that are rehearsed, triage vulnerabilities by evidence and patch by rebuilding, make every link of the supply chain leave evidence, and test your controls by provoking them. Much of this rests on a skill we have so far assumed, acting quickly and in concert when something goes wrong. Chapter 12 examines it directly, on the Friday morning when Vesper Hale's tour goes on sale.

### References

- Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana Oprea, Adam Stubblefield — [*Building Secure and Reliable Systems*](https://google.github.io/building-secure-and-reliable-systems/raw/toc.html). O'Reilly/Google, 2020 — free online.
- CISA — [*BOD 26-04: Prioritizing Security Updates Based on Risk*](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk). CISA, 2026 — free online.
- CISA — [*Known Exploited Vulnerabilities Catalog*](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). CISA, 2021 — free online.
- FIRST — [*Exploit Prediction Scoring System (EPSS)*](https://www.first.org/epss/model). FIRST — free online.
- GitHub — [*Dependabot version updates introduce default package cooldown*](https://github.blog/changelog/2026-07-14-dependabot-version-updates-introduce-default-package-cooldown/). GitHub Changelog, 2026 — free online.
- Kennedy Toomey — [*The case for dependency cooldowns in a post-axios world*](https://securitylabs.datadoghq.com/articles/dependency-cooldowns/). Datadog Security Labs, 2026 — free online.
- CISA — [*Supply Chain Compromise of Third-Party GitHub Action, tj-actions/changed-files (CVE-2025-30066)*](https://www.cisa.gov/news-events/alerts/2025/03/18/supply-chain-compromise-third-party-github-action-cve-2025-30066). CISA, 2025 — free online.
- GitHub — [*Security hardening for GitHub Actions*](https://docs.github.com/en/actions/security-for-github-actions/security-guides/security-hardening-for-github-actions). GitHub Docs — free online.
- OpenSSF — [*SLSA: Supply-chain Levels for Software Artifacts*, v1.2](https://slsa.dev/spec/v1.2/). OpenSSF, 2025 — free online.
- Zachary Newman, John Speed Meyers, Santiago Torres-Arias — [*Sigstore: Software Signing for Everybody*](https://doi.org/10.1145/3548606.3560596). ACM CCS, 2022 — free online.
- Joseph Spracklen, Raveen Wijewickrama, A H M Nazmus Sakib, Anindya Maiti, Bimal Viswanath, Murtuza Jadliwala — [*We Have a Package for You! A Comprehensive Analysis of Package Hallucinations by Code Generating LLMs*](https://arxiv.org/abs/2406.10279). USENIX Security, 2025 — free online.
- AWS — [*Security bulletin AWS-2025-015 (Amazon Q Developer for VS Code)*](https://aws.amazon.com/security/security-bulletins/AWS-2025-015/). AWS, 2025 — free online.
- Kelly Shortridge, Aaron Rinehart — [*Security Chaos Engineering: Sustaining Resilience in Software and Systems*](https://www.oreilly.com/library/view/security-chaos-engineering/9781098113810/). O'Reilly, 2023.
- CISA — [*Implementing Phishing-Resistant MFA*](https://www.cisa.gov/sites/default/files/publications/fact-sheet-implementing-phishing-resistant-mfa-508c.pdf). CISA, 2022 — free online.
- Eugene H. Spafford — [*The Internet Worm Program: An Analysis*](https://spaf.cerias.purdue.edu/tech-reps/823.pdf). Purdue Technical Report CSD-TR-823, 1988 — free online.

---

---

## Chapter 12: Incident Response — Command, Communication, and On-Call {#ch12}

> The fire does not read the org chart.

Every system in this book so far has been described at design time. An incident is the moment design time ends: users are hurting now, and a handful of people who were drinking coffee a minute ago must form a team, agree on what is happening and change a running system under load, all before they understand it. The hardest problems of the first 10 minutes are problems of coordination: who decides, who acts, who speaks, and who writes it down.

Our home touchstone comes from a field with far more at stake. In the autumn of 1970 a cluster of wildfires burned across Southern California for nearly two weeks, killing 16 people and destroying more than 700 homes, and the fire services found afterward that courage and equipment had not been the limiting factors. Agencies used different words for the same things, ran different radio frequencies, could not tell who was in charge of a given flank, and had no common way to grow a response from one engine to a hundred. Congress funded a cooperative program, FIRESCOPE (Firefighting Resources of California Organized for Potential Emergencies), and out of it, through the 1970s, came the **Incident Command System** (ICS): a standard way to organize an emergency response of any size among people who may never have worked together. In 2004 it became the backbone of the United States' National Incident Management System.

Software borrowed it a generation later and with less ceremony; the incident management described in *Site Reliability Engineering* (2016) is explicitly modeled on ICS, and PagerDuty's published response process uses the same roles. Encore is about to need every one of them. It is Friday, a few minutes before 10:00 CET, and 1.1 million fans are waiting in the Sale Gate, Encore's virtual waiting room, for Vesper Hale's 12-date European tour. (Chapter 1's [map of Encore](/prodsys-book/ch/1/#encore) shows where each piece sits.) We will follow the next 47 minutes section by section, and leave the question of *why* to Chapter 13.

### 12.1 Anatomy of an Incident

#### What makes something an incident {#what-makes-an-incident}

An **incident** is an unplanned disruption, or a credible threat of one, that needs a coordinated response beyond the routine work of a single on-call engineer. The definition turns on coordination rather than damage. A disk filling on a replica at 3 a.m. is a task; the same disk filling on a seat-ledger replica during an on-sale is an incident, because several teams must act together and someone must keep them pointed the same way.

A definition is not a trigger, though, and a tired engineer needs a trigger. Google's SRE book supplies one that has held up well: declare an incident if you need a second team, if customers can see the problem, or if it is still unsolved after an hour of focused work. Any one is enough. Encore adopted the test and added a clause of its own, that any purchase-path symptom during an on-sale counts, because an on-sale cannot wait an hour.

Every incident then passes through five phases. It is **detected**, by an alert, a customer or an engineer who notices something odd. It is **declared**: someone judges its severity and says out loud that it is an incident, with a name, a channel and a commander. It is **mitigated**, its harm stopped or reduced, usually before anyone understands the cause. It is **resolved**, once nobody has to watch the system by hand. And it is **followed up**, through the review of Chapter 13. Diagnosis runs underneath every phase, and severity is revised as the picture sharpens.

#### Severity as a shared vocabulary {#severity-levels}

Declaration depends on a vocabulary agreed before anyone needs it. Severity levels exist so that one word can set a whole response in motion. Encore's are short and written in terms of harm to fans and organizers; components are never mentioned.

| Level | What it means at Encore | Response it sets in motion |
|---|---|---|
| SEV1 | The purchase path is impaired during an on-sale, or seat or money integrity is at risk | Incident commander from the rotation within 5 min; comms lead; status page within 15 min; leadership informed |
| SEV2 | A customer-facing service is degraded outside an on-sale, or a tenant SLO is being breached | Incident commander from the owning team; status page if fans or tenants can see it |
| SEV3 | Error budget is burning with little visible harm, or one internal capability is lost | Owning team's on-call handles it; channel optional |
| SEV4 | No current user impact, but something needs fixing soon | A ticket and no channel |

*Figure 12.1 — Encore's severity levels. Each level is defined by harm and answered by a response.*

Google's and PagerDuty's guidance insist on two habits. Declare early and downgrade freely, taking the higher level when unsure: a needless declaration costs 20 minutes of mild embarrassment, a missing one the first 20 minutes of the response. And treat severity as provisional, since arguing about the number mid-incident delays the harder work.

#### Friday, 10:04 {#friday-1004}

At 10:00 the Gate opened and began admitting fans at 1,500 per second per event, the rate the On-Sale team had raised it to on Wednesday. At 10:04 the burn-rate alert on the on-sale-window service level objective (SLO) from Chapter 4 paged Rui, the On-Sale team's primary on-call. Rui saw failures in several places: "seat unavailable" errors on holds, rising checkout latency, and a retry rate that climbed as he watched.

Rui spent 60 seconds on scope before touching anything. Had the errors followed his own team's deploy, he should have rolled it back first; the pause is for judging size, and never delays an obvious, safe mitigation. But nothing of his had changed, the errors spanned every shard, and two declaration criteria were met. At 10:06 he paged the incident commander rotation, and at 10:07 Marta, a staff engineer from Orders & Payments who was on the rotation that week, declared a SEV1 and took command. The incident now had a name, a channel and one person whose only job was to run it.

**Recap.** An incident is defined by the need for coordination, and a concrete test (a second team, customer visibility, an hour without a fix) makes that definition usable by a tired person. Severity is a vocabulary of harm agreed in advance; we declare early, downgrade freely, and argue about the level afterward.

**Exercise 12.1.** Take your team's last three significant alerts. For each, note when it was detected, when (if ever) it was declared, and at what minute the three declaration criteria were first met. Where declaration came late, what was the person holding the pager waiting for?

### 12.2 Roles, Command, and Communication

#### What the firefighters learned {#what-the-firefighters-learned}

ICS rests on a handful of ideas, and each answers one of the failures of 1970. **Common terminology** means every agency calls the same resource by the same name. **Modular organization** means a small fire and a large one are run in the same shape, grown by adding standard units. **Span of control** means no supervisor directs more people than they can track, conventionally three to seven, with five as the target; a response that outgrows it adds a layer. **Unified command** means that agencies which each hold jurisdiction over part of an incident command it jointly, with one plan. Behind all four sits the idea that matters most: command is a role, assigned at the start and handed over explicitly, and it has nothing to do with rank.

Rob Schnepp, Ron Vidal and Chris Hawley, veterans of the fire service and of incident command, mapped these ideas onto software in *Incident Management for Operations* (2017). One adjustment is needed: a software company rarely shares jurisdiction. When the payment service provider (PSP) is in the same incident, each side commands its own systems and they meet through ICS's liaison officer, with joint objectives.

| ICS idea | What it answered in 1970 | Its form in a software incident | Encore's role |
|---|---|---|---|
| Single incident commander | Nobody knew who was in charge of a flank | One person owns the response and its decisions, and does not type commands | Incident commander (IC), from a cross-team rotation |
| Operations section | Crews acting on contradictory orders | One person directs hands-on changes to production | Ops lead, usually the owning team's on-call |
| Public information officer | Rumor and conflicting statements | One person speaks to stakeholders and the public, on a cadence | Comms lead, from the Reliability team |
| Planning and documentation | Lost track of resources and decisions | A live incident document (status, owners, decisions) and a running log | Scribe, assisted by Cue's draft timeline |
| Span of control | Supervisors overwhelmed | When more than about six responders are active, split into workstreams with their own leads | Workstream leads under the ops lead |
| Liaison officer | Agencies running parallel fights | Joint objectives with a vendor or partner, each commanding its own systems | Liaison to the PSP's or partner's incident lead |

*Figure 12.2 — From wildfire to on-sale. The roles are ICS's, scaled down; the reasons are the same.*

The best analogy for Encore comes from the theatre. A stage manager calls the show: from a desk in the wings, with a headset and the prompt book, they give every cue to lights, sound and flies, and they operate none of them. The incident commander is the stage manager; PagerDuty's documentation says bluntly that the commander is not a resolver. Marta would not be the one running `kubectl` at 10:07; her hands were free so that her attention could be. The analogy breaks, instructively, because the stage manager has a script and the incident commander must write the cues while calling them.

#### Handoffs and the collapse of roles {#handoffs}

Command changes hands more often than people expect, and each handoff is a gap the shared picture can fall through. The ICS answer, which the SRE book adopts almost verbatim, is a short spoken briefing followed by an explicit transfer ("you're now the incident commander, okay?") that the outgoing commander waits to hear acknowledged. Rui's briefing to Marta at 10:07 took under a minute: admission at 1,500 per second, errors on holds, retries rising, nothing changed yet.

Karl Weick's 1993 study of the Mann Gulch fire, in which 13 firefighters died in Montana in 1949, argued that the crew's ability to make sense of their situation collapsed along with the structure of their roles, so that when the foreman lit an escape fire and told them to lie down in it, none followed. The pattern, at far lower stakes, is familiar to anyone who has watched eight senior engineers in one channel, each pursuing a private theory.

#### Communication: inward, upward, outward {#communication}

An incident has three audiences. Responders need one channel where facts are stated and decisions recorded, and, once three or more are working, a live document beside it saying what is known, who owns what and what has been decided. Stakeholders inside the company (leadership, Support, tenant account managers) need plain summaries that spare them the channel. And the people affected need an honest public statement of what is wrong and when they will hear more.

Where that statement lives matters. When Amazon S3 failed in us-east-1 in February 2017, AWS could not update its own status dashboard for the first part of the outage, because the dashboard depended on S3. Encore rents a hosted status page that shares none of Encore's DNS, content delivery or cloud regions. Elif, the comms lead from the Reliability team, posted the first update at 10:14: some fans were seeing errors when selecting seats, places in the queue were safe, and the next update would follow within 15 minutes. Stakeholders got summaries on the same cadence. Every message gave the time of the next update and never a time for the fix, because only the first is a promise the comms lead can keep.

Communication also runs the other way, and that was where Encore's incident turned. At 10:24 Elif relayed something from Support that no dashboard had shown: fans were writing in to say the site had told them they were bots. Support, in that moment, was a sensor, and the comms lead was the only role positioned to connect it to the response.

{% include diagrams/fig-12-3.svg %}

*Figure 12.3 — The Vesper Hale response in ICS shape: command at the top, three roles beneath it, and the comms lead standing at the channel's edge. Notice the one line that runs inward; it carried the fact no dashboard had shown.*

**Recap.** ICS gave us a commander who does not operate, an ops lead who does, a voice for stakeholders and a scribe who keeps the record, with span of control, explicit handoffs and a liaison for partners. Communication flows to three audiences on a promised cadence, and flows back in, often carrying the fact the responders were missing.

**Exercise 12.2.** Reconstruct the roles in your last significant incident. Who was commanding, who was operating, who was communicating and who was recording? If one person held two of those roles, find a moment where that cost something.

### 12.3 Mitigate First — Situational Awareness Under Pressure

#### Three levels of seeing {#three-levels-of-seeing}

Mica Endsley's 1995 theory of situation awareness names what an incident team is trying to build. **Situation awareness** is the perception of the elements of an environment, the comprehension of what they mean, and the projection of what they will do next. The levels are cumulative: a team can perceive every alert and not comprehend them together, or comprehend the present and fail to project that the queue will empty in four minutes and bring a second wave. Incident tooling serves mostly the first level; the other two happen in people's heads, which is why a shared picture, where one person's comprehension can be checked against another's, matters.

#### Fixation {#fixation}

The characteristic failure of situation awareness under pressure is **fixation**: a team locks onto one explanation and stops seeing evidence that contradicts it. On 29 December 1972 the crew of Eastern Air Lines Flight 401, approaching Miami, became absorbed in a burned-out landing-gear indicator light; while they worked the problem, the autopilot's altitude hold was inadvertently disengaged and the aircraft descended slowly into the Everglades, killing 101 people. The bulb itself was harmless; the danger lay in how absorbing it was, with nobody assigned to fly the airplane.

Encore's fixation began at 10:11, when Cue, the operations agent, posted that the platform's upgrade reconciler had drained a node at 10:02 and that Seat Inventory shard 3, one of the four partitions selling the tour's seats, had failed over its leader at that moment. Both were true, and the channel's attention gathered around shard 3. Jonas, Seat Inventory's on-call, confirmed the failover and its 40 s of rejected writes, but that window had closed at about 10:03, and errors were still rising on all four shards. Marta's question at 10:16 broke the fixation: "What is still broken *now*, and is it getting better or worse?" The failover explained how the trouble had started; something else was keeping it going.

#### Mitigation before diagnosis {#mitigation-before-diagnosis}

The principle that follows is old in medicine and easily forgotten in engineering: stop the bleeding before you look for its cause. An emergency physician restores circulation in a patient in shock before asking why, because a correct diagnosis delivered too late helps no one. In an incident, **mitigation** is any action that reduces user harm without requiring that we understand why the harm is happening. Google's SREs call the best of them generic mitigations (shed load, roll back, fail over, disable a feature), each cheap to try, easy to reverse, and dependable only if rehearsed.

At 10:19, on Rui's proposal and with Marta's decision, the Gate's admission rate was lowered from 1,500 to 900 fans per second. Fans would wait a little longer in a queue they already expected, Seat Inventory and the retry storm would both ease, and the rate could be raised again in seconds. Errors on holds began to fall within two minutes. Nothing was fixed, but the team now had time to think.

The second mitigation came from what Elif had brought in at 10:24. Noor, Bot Screening's on-call, joined at 10:27 and confirmed it: the velocity rule that flags rapid repeated requests had been firing on fans retrying failed seat selections, and had blocked about 30,000 of them. The rule predated the policy of Chapter 4 that every block offer a challenge and a way back; it had never been reviewed, so it still blocked outright. At 10:31, with the IC's approval, Noor disabled the rule, and the Gate re-admitted the blocked fans with their original queue positions restored. It was a conscious trade, a short window of bot exposure against certain harm to tens of thousands of real fans.

By 10:47 the checkout burn rate had been within budget for several minutes and Marta declared the incident recovered. Admission was raised back to 1,200 per second at 11:10 under watch, and the incident was resolved at noon. Throughout, no seat was sold twice; the team's freedom to mitigate aggressively rested on knowing that fencing and idempotency would hold.

{% include diagrams/fig-12-4.svg %}

*Figure 12.4 — The on-sale as the Sale Gate saw it: admission rate per event, the 47 degraded minutes, and the response's events beneath. Both mitigations are cheap moves on one dial and one switch, made long before anyone understood the cause.*

| Time | What happened | Phase |
|---|---|---|
| 09:52 | A routine Catalog deploy rolls pods and empties the seat-map geometry cache (noticed only afterward) | — |
| 10:00 | The on-sale opens; the Gate admits 1,500 fans/s | — |
| 10:02 | The node-upgrade reconciler drains a node; Seat Inventory shard 3 fails over, about 40 s of rejected writes | — |
| 10:04 | The checkout burn-rate alert pages the On-Sale on-call | Detect |
| 10:07 | SEV1 declared; incident commander takes command | Declare |
| 10:11 | Cue surfaces the node drain and the shard 3 failover, and suggests restarting Seat Inventory pods; the suggestion is declined | Diagnose |
| 10:14 | First status-page update | Communicate |
| 10:19 | Admission lowered to 900 fans/s | Mitigate |
| 10:24 | Support reports fans being told they are bots | Diagnose |
| 10:31 | Bot velocity rule disabled; blocked fans re-admitted with queue positions restored | Mitigate |
| 10:47 | Checkout recovered | Recover |
| 11:10 | Admission returned to 1,200 fans/s | Resolve |
| 12:00 | Incident resolved; review scheduled | Follow up |

*Figure 12.5 — The Vesper Hale on-sale as the scribe's log recorded it. 47 minutes of degraded checkout; roughly 9% of admitted fans hit at least one error; no seat sold twice. Chapter 13 asks why each of these things was possible.*

**Recap.** Situation awareness has three levels, and tooling helps mostly with the first. Fixation is the characteristic failure, and the remedy is a role whose job is to keep asking what is broken now. Mitigation reduces harm before the cause is understood, and the best mitigations are generic, cheap, reversible and rehearsed.

**Exercise 12.3.** List the generic mitigations available for your most important service: what you can shed, roll back, fail over or switch off. For each, note how long it takes, who may authorize it and when it was last practiced.

### 12.4 Tooling for Response — Runbooks, ChatOps, and AI Assistance

#### Runbooks and the channel {#runbooks-and-the-channel}

Tooling for incidents should serve the roles. Good incident runbooks start from a symptom, offer generic mitigations before diagnostic steps, and name who may authorize each action, which is why "lower admission at the Gate" took under a minute to propose and approve.

**ChatOps** is the practice of running operational work through commands in a shared chat channel, so that actions and results are visible and recorded as they happen. In an incident its chief value is that every action is witnessed: a command typed in the channel is seen by the IC and logged by the scribe. Encore's look like this:

```
/incident declare sev1 "Vesper Hale on-sale: checkout errors"
/incident role ic @marta
/incident role comms @elif
/gate admission set event=vh-2026 rate=900   # requires IC approval
/statuspage draft "Some fans are seeing errors when selecting seats..."
```

The last line drafts but does not publish; as in PagerDuty's process, a public post needs the commander's approval.

#### Cue at 10:11 {#cue-at-1011}

Cue, the operations agent of Section 3.5, joins every SEV1 and SEV2 channel. It reads telemetry, deploy history, runbooks and past postmortems. What it may do is fixed by the platform, not by its instructions: its only actions come from a catalog the platform enforces, each run with a five-minute token scoped to that one action and target, issued only when a named person approves the plan in the channel. Only two small actions may run without approval, raising Catalog's autoscaler floor and holding a node in the upgrade reconciler, and a restart of Seat Inventory was not one of them. At 10:11 it did two things, which map onto what such tools have and have not been shown to do.

The first was genuinely helpful: in about four minutes it had correlated the alert with the platform's change log and the shards' leader history. Correlating alerts with recent change is an old, proven move, since most outages follow a change; doing it with a language model is young, and the published accounts are real but modest. Meta reported in 2024 that its ranker put the responsible change among its top five candidates in 42% of investigations tested; Microsoft's RCACopilot (EuroSys 2024) was evaluated on a year of incidents and deployed with one team. Cue showed the limit too: the Catalog deploy at 09:52 fell outside the window it searched, a blind spot Chapter 13 measures.

The second was a suggestion, learned from two old postmortems about stateless services: restart the Seat Inventory pods to clear what it called an unhealthy state. It was plausible and wrong: a restart would have forced leader elections on every shard, each with its own window of rejected writes. Jonas, one of the few engineers who had run a shard failover by hand (at the game day of Chapter 9), declined it in one line. Bainbridge's irony was at full strength: the safeguard against a fluent agent was a person skilled enough to judge the suggestion at the moment the agent's speed made deference tempting. An assistant that is right about the facts can still be wrong about the action.

The approval gate that held at 10:11 has production support too. Google's SREs described in early 2026 how Gemini CLI works outages through typed tools carrying risk metadata, with a human confirmation for every change and an audit trail; their worked example was a simulated outage, and the practice is young. Unattended remediation has no credible production account; in IBM's ITBench benchmark (ICML 2025) agents resolved only 11.4% of the SRE scenarios. Encore keeps Cue to suggestions and approved catalog actions, and since that Friday each action carries a blast-radius tag.

Cue's most valuable work drew less attention: a draft timeline, which the scribe corrected into Figure 12.5, and draft summaries for Elif to edit. Here the evidence is firmest. Google's security team reported in 2024 that model-drafted incident summaries were written 51% faster and rated higher in quality, with a person approving each, and Datadog describes the same draft-then-correct pattern for postmortems.

**Recap.** Runbooks lead with generic mitigations, and ChatOps makes actions visible. AI assistance is young but has real accounts behind it for change correlation and for drafting timelines and summaries that a person corrects. Actions belong in a platform-enforced catalog, each approved and scoped; autonomous remediation remains unproven.

**Exercise 12.4.** Pick one action your tooling or assistant could take during an incident (a restart, a rollback, a scale change). Write down when it would make things worse, then check whether the approval step forces a human to consider that, and whether anything besides the approval stops the tool from acting.

### 12.5 On-Call That People Can Sustain

#### Load and its measures {#load-and-its-measures}

On-call is where incident response becomes a labor question. The Google SRE book offers two reference points that have aged well: no more than 25% of an engineer's time on call, and about two incidents at most in a 12-hour shift, since each carries hours of follow-up. Other teams will choose their own targets, but should measure pages per shift, pages outside working hours, the share that needed action and time to acknowledge, read as distributions, since one team's averages are noisy. A page that needed no action is a defect in the alerting, and Chapter 5's paging discipline is the cure.

The 25% cap has an arithmetic consequence. With a primary and a secondary every week, each engineer is on call two weeks in eight only if the rotation has at least eight people; with two sites splitting the day, the SRE book's minimum is six per site. A stream-aligned team of five cannot meet the cap alone. Encore runs a weekly primary and secondary per team, pairs small teams with neighbors so that no rotation has fewer than eight people, and keeps a separate incident commander rotation of about 20 trained senior engineers. Every rotation answers to the escalation policy, which moves an unacknowledged page on by itself and decides, from the alert, whether a phone may ring at night:

```yaml
escalation_policy: on-sale
steps:
  - notify: primary
    escalate_after: 5m        # unacknowledged
  - notify: secondary
    escalate_after: 10m
  - notify: on-sale-engineering-manager
urgency:
  high: [sev1-symptom, sev2-symptom]   # any hour
  low: [everything-else]               # working hours only
```

Rui had been paged twice in the small hours that week, mostly by pre-warm alerts. He responded well on Friday, which says little about whether the rotation was healthy.

#### Follow-the-sun, compensation and handoffs {#follow-the-sun}

Organizations with two adequately staffed sites can run **follow-the-sun** rotations, in which each region holds the pager during its own daytime and hands it on. Every shift boundary is then a handoff, needing the briefing of Section 12.2 and a written note. Encore's engineers all work near CET, so it keeps night pages for SEV1 and SEV2 symptoms only, set as urgency on each alert in advance (severity is assigned too late to decide whether a phone rings), and gives time off after any night page.

Compensation is part of sustainability. In the Matzak case (2018) the Court of Justice of the European Union held that a Belgian volunteer firefighter who had to reach his station within eight minutes while on standby at home was working. Matzak marks the extreme. In two 2021 rulings the Court narrowed it: standby is working time only where the employer's constraints very significantly limit the worker's free time, and the classification does not settle the pay. Few software rotations, with a laptop and half an hour to respond, cross that line. What is settled is that answering a page is working time, and that the Working Time Directive's 11 hours of daily rest are owed afterward. Encore pays a standby allowance on top, its own choice, because a rotation that depends on goodwill is already failing.

#### Fatigue {#fatigue}

Fatigue degrades exactly what incident response needs: comprehension, projection, and the patience to spend 60 seconds on scope before acting. Long incidents therefore rotate command. In one recounted in the SRE Workbook, PagerDuty rotated its responders and its incident commander every four hours, and Encore adopted the same limit for the IC. After Vesper Hale, Marta sent Rui and Jonas home at lunchtime and asked the On-Sale team's secondary to take the pager for the weekend, a small decision of the kind that keeps people on a rotation for years.

**Recap.** On-call load should be measured as carefully as any SLO, and the 25% cap implies rotations of at least eight people, or six per site, which small teams reach only by pooling. The law asks less of standby than is often claimed, but answering a page is work and the rest after it is owed, and long incidents rotate command because fatigue erodes judgment first.

**Exercise 12.5.** Pull the last quarter's pages for your rotation. Compute pages per shift, the share outside working hours and the share that required action, and check the rotation's size against the 25% arithmetic. Which single alert, removed or demoted, would most improve the numbers?

### Kata: Storm Night

> **Your brief: "Brightwater Energy."** The customer platform of a regional electricity utility: 1.1 million accounts, an outage map, 800,000 smart meters that send a "last gasp" signal when they lose power, and dispatch for 300 field crews. A winter storm brings 25× normal traffic, and the grid operator's control room and two crew vendors share every storm incident. There are 24 engineers in four teams, two offices an hour apart, and a single on-call rotation that took 310 pages last quarter, 55% of them at night and most of them needing no action. Last January the outage map froze for four hours, showing 2,000 customers without power when 90,000 were. The incident went undeclared for 70 minutes, three engineers made conflicting changes, and customers learned their restoration times from local radio.

**Deliverables:**

1. **Severity matrix and declaration test** — four levels defined by harm to customers (above all those on the medical-dependency register) and to crews, each with its response, plus the criteria for declaring.
2. **Role cards** — one page each for IC, ops lead, comms lead and scribe, with the handoff briefing and how decisions are shared with the control room and crew vendors.
3. **Communication plan** — cadence and templates for the channel, the control room and call center, the status page and map banner, and SMS, including where the status page is hosted.
4. **Mitigation runbook** — symptom-first steps for "the outage map is stale or wrong," leading with generic mitigations and naming who authorizes each.
5. **On-call redesign** — rotation sizes, an escalation policy, page-load targets, the alerts you would delete or demote, and a compensation and rest policy.
6. **Tabletop script** — a 45-minute exercise replaying last January's storm with the new roles.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Early declaration | Would the new criteria have declared last January's incident within 10 minutes, and who would have done it? |
| Command clarity | Is there one IC who does not operate, and could three engineers still make conflicting changes? |
| Partners | Do the control room and the crew vendors know whom to talk to, and which decisions are joint? |
| Mitigation first | Can customers still report outages and see an honest map while the cause is unknown, and is that option rehearsed? |
| Honest communication | Will customers hear from Brightwater before they hear from the radio? |
| Sustainable load | Do the numbers, rotation size included, show a rotation people would join voluntarily before next winter? |

#### Where you now stand

You can now declare incidents by a concrete test, staff them with roles the fire services refined over half a century, guard against fixation, mitigate before diagnosing, give an agent only the approved part of the work the evidence supports, and size a rotation people can carry for years. Encore's 47 minutes ended with no seat sold twice and some 30,000 fans wrongly called bots. Chapter 13 asks the harder question: how a sensible rate change, a routine deploy, a trusted reconciler and an old bot rule came to meet at 10:02 on the most important morning of the year.

### References

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne (eds.) — [*The Site Reliability Workbook*](https://sre.google/workbook/table-of-contents/). O'Reilly/Google, 2018 — free online.
- PagerDuty — [*PagerDuty Incident Response Documentation*](https://response.pagerduty.com/). PagerDuty — free online.
- Rob Schnepp, Ron Vidal, Chris Hawley — [*Incident Management for Operations*](https://www.oreilly.com/library/view/incident-management-for/9781491917619/). O'Reilly, 2017.
- Amazon Web Services — [*Summary of the Amazon S3 Service Disruption in the Northern Virginia (US-EAST-1) Region*](https://aws.amazon.com/message/41926/). AWS, 2017 — free online.
- Mica R. Endsley — [*Toward a Theory of Situation Awareness in Dynamic Systems*](https://doi.org/10.1518/001872095779049543). Human Factors, 1995.
- Karl E. Weick — [*The Collapse of Sensemaking in Organizations: The Mann Gulch Disaster*](https://doi.org/10.2307/2393339). Administrative Science Quarterly, 1993.
- Meta Engineering — [*Leveraging AI for Efficient Incident Response*](https://engineering.fb.com/2024/06/24/data-infrastructure/leveraging-ai-for-efficient-incident-response/). Engineering at Meta, 2024 — free online.
- Yinfang Chen et al. — [*Automatic Root Cause Analysis via Large Language Models for Cloud Incidents*](https://arxiv.org/abs/2305.15778). EuroSys, 2024.
- Google Security Blog — [*Accelerating Incident Response Using Generative AI*](https://security.googleblog.com/2024/04/accelerating-incident-response-using.html). Google, 2024 — free online.
- Riccardo Carlesso, Ramón Medrano Llamas — [*How Google SREs Use Gemini CLI to Solve Real-World Outages*](https://cloud.google.com/blog/topics/developers-practitioners/how-google-sres-use-gemini-cli-to-solve-real-world-outages). Google Cloud Blog, 2026 — free online.
- Saurabh Jha et al. — [*ITBench: Evaluating AI Agents across Diverse Real-World IT Automation Tasks*](https://proceedings.mlr.press/v267/jha25a.html). ICML, 2025 — free online.
- Court of Justice of the European Union — [*Case C-518/15, Ville de Nivelles v Matzak*](https://curia.europa.eu/juris/liste.jsf?num=C-518/15) (2018), and Cases C-344/19 and C-580/19 (2021). CURIA — free online.

---

## Chapter 13: Learning from Incidents — Postmortems, Just Culture, and Drift {#ch13}

> "For a successful technology, reality must take precedence over public relations, for nature cannot be fooled." — Richard Feynman

On the evening of 27 January 1986, engineers at Morton Thiokol, the contractor that built the space shuttle's solid rocket boosters, joined a teleconference with NASA managers to argue that Challenger should not launch the next morning. Each booster's field joints were sealed by rubber O-rings, cold rubber is slow to seal, and the forecast was far colder than any launch so far. The coldest earlier launch, in January 1985 at about 53°F (12°C), had shown more blow-by of hot gas past a primary ring than any flight before it, and so the engineers recommended against launching below that temperature. NASA's managers challenged the data, which was thin; Thiokol's managers conferred off the line and came back recommending launch. On 28 January, at about 36°F (2°C), Challenger lifted off; 73 seconds later it broke apart, and the seven people aboard were killed.

The first account was of schedule pressure and rules bent, and the Rogers Commission did find launch constraints waived without being reported upward. Diane Vaughan's *The Challenger Launch Decision* (1996) told a more unsettling story. O-ring erosion had been seen as early as the second shuttle flight, in 1981. Each time, engineers found a reason the margin still held and accepted the next flight as an "acceptable risk" through exactly the procedures NASA had built for such judgments, and each acceptance became precedent for the next, until by January 1986 the burden of proof had quietly turned over, and the engineers were asked to prove flight unsafe, which with their data they could not. Vaughan called this the **normalization of deviance**: the gradual process by which a departure from an expected standard, repeated without harm, comes to be treated as the standard itself. In her reading nobody broke the rules in any sense that mattered; the rules were how the deviance became normal. When Columbia was lost in 2003, the accident board drew explicitly on her work and found the same pattern a second time.

Chapter 2 introduced the ideas this chapter puts to work, from Reason's latent conditions to Leveson's System-Theoretic Accident Model and Processes (STAMP). Chapter 12 followed Encore through the Vesper Hale on-sale: 47 minutes of degraded checkout, about 30,000 real fans blocked as bots, and not one seat sold twice. Now the slower work begins: learning from it without punishing or excusing anyone, and making the learning stick. Encore's change freeze, which bars routine changes to the purchase path around a big on-sale, had been eroding very much as the O-ring margins had.

### 13.1 Blameless, Not Accountability-Free

On the Monday after the on-sale, the first question in the leadership channel was "who approved the admission change?" It was natural, and the wrong question to ask first. Its answer explains almost nothing, because the trouble lay in a process that had let a warm-cache test count as evidence, and any engineer on that team, with that test, would have approved the same change.

A **blameless postmortem** is a review in which the people involved give a full account of what they did and why, on the understanding that the account will be used to improve the system and not to punish them. John Allspaw's 2012 post on Etsy's engineering blog carried the idea from Sidney Dekker's work on just culture into web operations, and Google's SRE book made it the default for a generation, adding that leaders must be seen to reward good postmortems. The logic is informational before it is moral: an organization learns only what its people tell it. Punish an account and the next one will be shorter, vaguer and carefully lawyered.

Blameless is often misheard as "nobody is accountable". Dekker's *Restorative Just Culture* (2025, the fourth edition of his *Just Culture*) answers the confusion by contrasting two responses to harm. A **retributive** just culture asks which rule was broken, by whom, and with what consequence. A **restorative** just culture asks who was hurt, what they need, and whose obligation it is to meet that need. Both take accountability seriously; the restorative one asks for an account and for repair. The framing comes from healthcare, where its best-documented adopter, the Mersey Care NHS trust in England, reported fewer suspensions and lower costs. In software "blameless" is common, and the restorative questions asked by name are still rare.

Encore asked them explicitly. The fans were hurt first: about 30,000 were blocked outright, and roughly 9% of admitted fans hit errors. Encore restored blocked fans' queue positions during the incident, gave every blocked fan early access to further tour dates, and published a plain public account within the week. Such reports are restorative work done in the open, and cloud providers have made them routine: AWS published a post-event summary within days of its us-east-1 failure of October 2025, and Cloudflare explained its November 2025 outage in detail the same day. Organizers and the artist's management got the same account, earlier and fuller.

The engineers were hurt too. The On-Sale engineer who proposed the admission change spent the weekend replaying it. The physician Albert Wu called such people **second victims** in 2000: clinicians harmed by their own involvement in a patient's harm. Patient advocates have since argued that the term casts the harm as bad luck, and many hospitals now avoid it, but the practice Wu asked for, early support for the clinician, has become standard. The engineer needed to hear, early and from leadership, that the review would be about the system, and the obligation to say so fell on the organization.

None of this abolishes consequences: sabotage and sustained recklessness are rare, and Allspaw and Dekker both send them to a separate process. The postmortem's job is to collect the truest account it can.

**Recap.** Blameless review exists so that people give full accounts. Accountability survives in restorative form, asking who was hurt, what they need and whose obligation it is to meet that need. Customers were answered with a public report, engineers with early, explicit support.

**Exercise 13.1.** Take your organization's last significant incident. Write the three restorative questions and answer them for every group affected, including the engineers. Which need went unmet, and whose obligation was it?

### 13.2 Beyond Root Cause — Contributing Factors and CAST

#### Why root cause fails {#why-root-cause-fails}

Ask "what was the root cause of Vesper Hale?" and four candidates step forward: the admission change, the Catalog deploy, the node drain and the bot rule. Each was necessary, and none was sufficient. Remove any one and the morning is very likely an ordinary on-sale. Richard Cook's observation from Chapter 2, that catastrophe needs several failures together, is here simply the timeline. A **root cause** is wherever an investigation decides to stop asking why.

Two biases push us to stop early. **Hindsight bias**, which Baruch Fischhoff demonstrated in 1975, is the tendency of people who know an outcome to judge it more predictable than it was. Its companion is the **counterfactual**: "the team should have run a cold-cache test." The sentence is true and nearly useless, because it says nothing about why the world that did exist made sense to the people in it. Richard Cook, David Woods and John Miller distinguished in 1998 between a *first story*, in which a person erred, and a *second story*, which explains the pressures, resources and trade-offs that made the act reasonable at the time. Only the second story says what to change.

None of this requires banning a phrase. Google's error-budget policy still asks for an action addressing "the root cause", and CrowdStrike's 2024 root cause analysis of its faulty sensor update described several conditions that had to line up; mainstream operators mostly mean the plural. Encore's default review keeps it plural under a heading of **contributing factors**: the conditions that together made the incident possible, each explained from the inside.

#### When CAST earns its cost {#cast-at-encore}

For its largest incidents Encore goes further. Nancy Leveson's **Causal Analysis based on STAMP (CAST)** is a method for writing second stories systematically. It treats an incident as a failure of control: some controller, human or automated, issued an action unsafe in context, usually because its **process model** (its beliefs about the system it controls) was wrong or missing a signal. CAST names the loss and the hazard, draws the control structure, asks of each controller what it did, what it believed and why that was reasonable, and then examines coordination and how the structure changed over time.

CAST is established in aviation, defense and healthcare, and young in software. Leveson's free *CAST Handbook* appeared in 2019; the best public account of its use by a large operator is Google's, whose SRE organization has described applying STAMP methods to its incidents in recent articles and talks, while its own page still calls the work exploratory. It is also labor-intensive, so Encore reserves CAST for SEV1 incidents (Chapter 12's top severity) and anything touching seat or money integrity, and uses the lighter contributing-factors review for everything else. Vesper Hale qualified on both counts.

Encore's Reliability team, the platform group's ten site reliability engineers, ran it with every team involved. The loss was fans unable to buy tickets during an on-sale; the hazard, the purchase path receiving more load than it could serve while its capacity was reduced. Figures 13.1 and 13.2 show the control structure and what each controller believed.

{% include diagrams/fig-13-1.svg %}

*Figure 13.1 — The control structure of the Vesper Hale on-sale. Every controller could act on the purchase path, and two of the feedback paths that would have warned them did not exist.*

| Controller | Control action | What it believed | What was missing |
|---|---|---|---|
| Node-upgrade reconciler (platform) | Drained a node at 10:02 | Draining is safe whenever disruption budgets allow it | Input from the on-sale calendar; any sense that a shard leader's node costs more to drain |
| Change freeze (readiness review) | Defined the frozen scope; granted exceptions | Catalog and "low-risk" automation sit outside the purchase path | A scope derived from real dependencies; a record of exceptions and what followed them |
| On-Sale team and reviewer | Raised admission from 1,200 to 1,500 fans/s | The load test proved headroom | A cold-cache case in the test; a review question about cache state |
| Catalog team | Deployed at 09:52 | Outside the freeze, a rolling deploy is routine | Any signal that its seat-map cache was on the on-sale's critical path |
| Bot Screening velocity rule | Blocked about 30,000 clients | Bursts of identical requests are bots | Knowledge that the web client now retries failed holds; feedback from purchase-path errors |
| Cue (operations agent) | Suggested restarting Seat Inventory pods | Restarts had cleared elevated errors in past incidents | A model of leader failover; the blast radius of its suggestion |

*Figure 13.2 — Encore's control structure on the morning of the Vesper Hale on-sale, read through CAST. Every controller acted on a reasonable belief; the missing column is where the changes come from.*

Read down the last column and a pattern appears that no single row reveals: nearly every gap is missing feedback between teams. Vaughan called this **structural secrecy**: the division of labor that lets each group see its own piece clearly and nobody see the whole. It is the price of decomposition, which is how 40 teams master a system no one person could hold, so the answer is to wire the feedback back in. A lighter review would have listed the four contributing factors; it took the drawn structure to show that they were one finding.

#### The freeze as normalization of deviance {#the-freeze-as-normalization-of-deviance}

The second row is Challenger in miniature. The freeze rule was clear: no non-emergency changes to the purchase path from two hours before an on-sale until its end. Over the previous year the freeze channel recorded 41 exceptions (Figure 13.3), every one granted in chat, none followed by an incident. The node-upgrade reconciler was classed as low-risk automation and exempted, and on three earlier on-sales it had drained nodes mid-sale without harm, because none hosted a shard leader. The freeze's service list predated Catalog's seat-map cache, and nobody had reason to revisit it.

{% include diagrams/fig-13-3.svg %}

*Figure 13.3 — Freeze exceptions granted in chat, quarter by quarter, in the year before Vesper Hale. Each quarter looked like the last one, a little busier; only the running total, which nobody kept, shows the drift.*

| Stage | Challenger's O-rings | Encore's freeze |
|---|---|---|
| The standard | Joints seal with no erosion | No purchase-path change from T−2h |
| First deviance | Erosion seen after the second flight (1981) | Exceptions granted in chat "just this once" |
| Reinterpretation | Erosion within a calculated safety margin | Platform automation classed as low-risk and exempt |
| Success as evidence | Flights with erosion return safely | Three mid-sale drains cause no harm |
| Burden of proof reversed | Engineers must prove flight unsafe | Anyone objecting must show why an exception is risky |

*Figure 13.4 — Two drifts, side by side. In both, each step was reasonable, made by careful people, and confirmed by an outcome that happened to be good.*

Nobody ignored the freeze. People followed it, and that is how it drifted: when a rule's exceptions are never counted, its meaning changes without anyone deciding to change it.

**Recap.** Root cause is a stopping point, and hindsight pushes us to stop too soon; the everyday remedy is plural contributing factors, each told as a second story. CAST, young in software and costly, earns its place on the largest incidents, where at Encore it showed structural secrecy between teams and a freeze that had drifted as the O-ring margins did.

**Exercise 13.2.** Build a CAST table like Figure 13.2 for the most serious incident you know, with at least four controllers, one of them automated. Write why each belief was reasonable at the time. Which missing feedback path would have changed the most rows?

### 13.3 Writing and Running the Review

#### Deciding what gets reviewed {#deciding-what-gets-reviewed}

Which incidents get a review should be settled in advance, or embarrassment chooses. Google's SRE book lists its triggers: user-visible impact past a threshold, any data loss, on-call intervention such as a rollback, a long resolution time, and a monitoring failure, meaning a problem a human found before the alerts did. At Encore every SEV1 gets a CAST review. Any incident that spends 20% or more of an error budget, loses data or is reported by a customer before an alert fires gets the lighter review. Anyone may ask for a review of anything.

#### Preparing the account {#preparing-the-account}

The Vesper Hale review was facilitated by a member of the Reliability team who had not been in the incident channel and had no authority over anyone she would interview. Etsy's debriefing guide and Jeli's Howie guide both insist on these conditions. Within two days she held short one-to-one interviews with Marta, the incident commander, the responders and each team in Figure 13.1. Group meetings converge on the most confident voice, and the quiet engineer who noticed something at 10:03 may say so only in a room of two.

Cue had drafted most of the timeline within an hour of recovery. Such drafts are a young feature of incident tools; this one was accurate but told only half the story. A timeline built from logs records what the system did; the review needs a second column for what people knew, believed and were trying to do. Only the interviews showed that at 10:11 Marta already suspected the admission change and was weighing a rollback, and that Cue's news of the drain changed which lever she pulled first.

The 2017 STELLA report, from the SNAFUcatchers workshop led by David Woods, explains why that column matters: people act on the running system (*below the line*) only through their mental models of it (*above the line*), and incidents are where those models turn out to differ. Encore's mismatches surfaced quickly: the On-Sale team learned that the reconciler existed, and Bot Screening that the web client had retried failed holds automatically since the previous spring. The velocity rule also predated the policy, adopted after the dispute of Chapter 4, that every block must offer a challenge. Nobody had reviewed it since, so it still blocked outright.

#### Reviewing the machine's part {#reviewing-the-machines-part}

Cue's 10:11 suggestion to restart Seat Inventory pods was examined like every other controller's action. No industry convention covers this; Encore chose it because CAST treats automated controllers this way, and because two easy first stories were on offer: "the AI was wrong" and "the human caught it". A restart made sense given what Cue had read: two old postmortems in which restarts had cleared errors on stateless services, and nothing about leader-elected services under load. Jonas declined because he had run a shard failover by hand at the game day of Chapter 9; for once the irony from Chapter 3, that skill decays where automation succeeds, did not apply. The finding concerned neither party: a suggestion had arrived without its blast radius, and safety had depended on one person's memory of a drill. So runbook actions now carry a blast-radius tag that Cue must show with any suggestion, a rule of Encore's own devising.

#### The meeting and the document {#the-meeting-and-the-document}

The meeting ran for 90 minutes with about 25 people, more than the guides advise. A stage manager's show report after each performance, plain and unembarrassed, is the right model for the document, except that a review must reconcile many accounts, some of them honestly disagreeing.

The skeleton below is Encore's lighter review, the default for anything below SEV1. It follows the example postmortem in Google's SRE book and Atlassian's template, with *went well* and *surprises* borrowed from the learning-from-incidents community; a CAST review adds the last line.

```text
Summary        two paragraphs a fan could follow
Impact         who was affected, for how long, how we know
Trigger        why this got a review (severity, budget spent, found by a customer)
Timeline       what the system did | what people knew and were trying to do
Contributing   the conditions that together made it possible, each as a second story
Went well      what limited the harm, and why it worked
Surprises      where someone's picture of the system turned out to be wrong
Actions        owner, strength (stronger/intermediate/weaker), how we will know it worked
Language       reread for "should have", "failed to", "simply", "careless"
CAST (SEV1)    controllers, actions, beliefs, missing feedback
```

The language check is a prompt to reread. "Failed to" brings the counterfactual back in, but a writer can delete every listed phrase and still write the first story in politer words, so the check asks the author to look again at each sentence that judges.

**Recap.** Triggers settled in advance decide which incidents are reviewed, and how heavily. An uninvolved facilitator, prompt interviews and a two-column timeline produce the account a meeting cannot, and a short skeleton makes the lighter review cheap enough to do every time.

**Exercise 13.3.** Rewrite a postmortem from your archive into the skeleton above, adding the missing column to its timeline. Count the counterfactual phrases in the original. What does the rewritten version show that the original did not?

### 13.4 Near Misses and Learning from Success

A **near miss** is an event in which the conditions for harm came together but harm did not follow, through luck or someone's adaptation. In 1976 the United States set up the Aviation Safety Reporting System, run by NASA for the Federal Aviation Administration, through which pilots and controllers report close calls confidentially, with limited protection from penalty for those who report promptly. It is designed to make telling cheaper than staying quiet. Hospitals adopted the idea; few software organizations run a formal near-miss channel, so here the practice is borrowed and young.

The CAST analysis turned up near misses nobody had reported because nothing had happened: the three earlier mid-sale drains, each read silently as evidence that the reconciler was safe. Encore now asks each on-sale's on-call to note anything that surprised them, harm or no harm, and the Reliability team reads the notes weekly and answers each one.

Asking why the freeze had seemed to work at all found something stranger. For most of the previous year a platform engineer had paused the reconciler by hand before each big on-sale. It was in no runbook; drains during sales simply made her nervous. In the spring she moved to another team, and the practice left with her. This is Hollnagel's Safety-II from Chapter 2 made concrete: things usually go right because people adjust their work to conditions, and **work-as-done** quietly differs from **work-as-imagined**.

So Encore added a second kind of review, borrowed from the US Army's after-action review, which follows exercises whether they went well or badly and asks what was supposed to happen, what did, and why. Safety-II gives the habit a theory with thin outcome evidence, and in software it is still a practitioner movement. After each major on-sale that goes well, the teams involved spend 30 minutes asking what they adjusted, what nearly happened and what they did that no document describes. The first few surfaced a dozen informal practices; three became automation, one was retired as superstition. Vesper Hale itself had a "went well" section worth studying: fenced leader terms and idempotency keys turned 40 s of rejected writes on shard 3 into errors instead of double sales, the result of design decisions tested at every game day since.

Do not make near-miss reports a number to drive down; in patient safety a rising count is read as trust in the channel. The same caution covers the incident metrics most dashboards show. The VOID, a public collection of thousands of software incident reports, found durations so skewed that mean time to resolve says little about whether an organization is improving, and that incident counts mostly reflect how willing people are to declare an incident.

**Recap.** Near misses are incidents the system escaped through luck or adaptation, and they go unreported unless reporting is cheap and safe; software is borrowing this from aviation and hospitals. Studying ordinary success reveals the adaptations that hold the system up, some living only in one person's habits.

**Exercise 13.4.** Interview two colleagues about something they do before a risky change that no runbook asks them to do. Write each practice down. Which should become automation, which documentation, and which should be retired?

### 13.5 Turning Learning into Change

#### Why action items die {#why-action-items-die}

Action items die quietly. When Encore's Reliability team audited the previous year's postmortems, about 40% of their action items were still open after 90 days, and the open ones were not a random sample: the small fixes had closed, while the structural items (those that crossed team boundaries, needed a design or had no obvious owner) had sat untouched. Google engineers described the same pattern in 2017, with the plain remedy of planning postmortem work like any other work.

Occupational safety ranks its remedies in a **hierarchy of controls**: eliminate, substitute, engineer a barrier, then procedures and training, with protective equipment last. Healthcare carried the ranking into incident review itself. The National Patient Safety Foundation's RCA² guidance of 2015, building on the US Veterans Affairs' action hierarchy, sorts actions into stronger (physical changes, forcing functions, simplification), intermediate (checklists, redundancy, software enhancements) and weaker (training, new policy, warnings), and asks for at least one stronger or intermediate action per finding, accepting weaker ones as stopgaps. "Remind engineers to check cache state" is weaker; a load test that cannot pass without a cold-cache run is stronger. An action that restores no named control is usually a wish. Figure 13.5 places Encore's changes on the hierarchy.

{% include diagrams/fig-13-5.svg %}

*Figure 13.5 — The hierarchy of controls, with the Vesper Hale changes placed on it. The higher a remedy sits, the less it depends on a tired person remembering it, which is also how RCA² ranks actions.*

#### What Encore changed {#what-encore-changed}

| Finding | Change | Owner | How we will know it works |
|---|---|---|---|
| Upgrade automation blind to the on-sale calendar | The calendar becomes a signal: deny sync windows on purchase-path projects and a hold the reconciler reads, from T−2h to the sale's end; no shard-leader drains during a sale | Runtime team (platform) | A game day schedules an upgrade into a mock on-sale and confirms it waits |
| Admission change reviewed against a warm cache | Any admission-rate change needs a cold-cache load test; the readiness review asks about cache state | On-Sale team, Reliability | The next admission change arrives with a cold-cache result attached |
| Bot rule tuned before retry behavior changed | Every bot rule has an owner and review date; client retry changes trigger a rule review; the velocity rule drops to observe-only when purchase-path errors spike | Bot Screening | A replay of Vesper Hale traffic blocks no real fans |
| Freeze drift | Freeze restored; scope from the traced dependency graph (Chapter 5), which misses unexercised paths, plus declared dependencies; a register of exceptions with reason, approver and outcome, reviewed monthly | Reliability | Exceptions trend down, and each has a recorded outcome |
| Suggestion without blast radius | Runbook actions tagged; Cue shows the tag with every suggestion | Reliability, Cue maintainers | Drill transcripts show the tag on every suggested action |

*Figure 13.6 — From finding to change. Each row restores a control missing from Figure 13.2, and each says in advance what evidence will show it working.*

The first row has strong precedent. Chapter 7 introduced Argo CD's sync windows, which stop the GitOps agent applying changes to chosen applications for a scheduled period; managed Kubernetes services offer node-upgrade maintenance exclusions on the same idea. A small calendar controller, added beside the curtain-up workflow, now writes each on-sale as a deny window on the purchase-path projects and as an entry in a small calendar service the reconciler checks before every drain, generated from one source so the two cannot disagree:

```yaml
# AppProject purchase-path; written by the calendar controller from the on-sale calendar
spec:
  syncWindows:
    - kind: deny
      schedule: "0 8 20 11 *"        # T−2h before a Friday 10:00 on-sale
      duration: 6h                    # through the end of the sale
      timeZone: Europe/Paris
      applications: ["sale-gate-*", "bot-screening-*", "seat-inventory-*", "orders-*", "catalog-*"]
      manualSync: true                # break-glass stays possible, and is logged
```

The register of exceptions is the quietest change and, I have come to believe, the most important. Such registers are old practice in change and risk management, though none is proven to prevent incidents and an unread one becomes a rubber stamp. Vaughan never taught that deviance can be forbidden; some exceptions are right. She taught that deviance becomes normal when nobody can see it accumulate. The register makes each exception a decision with a name, a reason and an outcome, so that whoever weighs the 42nd exception can see the previous 41.

#### Tracking, sharing and reading across incidents {#tracking-and-sharing}

Encore tracks postmortem actions alongside feature work, reviews them weekly, and lets the error-budget policy of Chapter 4 prioritize them when a budget is spent. An item older than 90 days must be closed, rescheduled with a reason or accepted as a risk by a named person. Atlassian's deadlines for priority actions, four and eight weeks, are tighter.

Drift shows across incidents more than within one, so the Reliability team reads each quarter's postmortems together and tags recurring contributing factors. The first reading found stale cache assumptions in three reviews that never cited each other.

The Vesper Hale review went to all of engineering and to the monthly all-hands, and its timeline will be replayed at a game day, as Google's SRE teams replay old incidents for new on-call engineers in an exercise they call the Wheel of Misfortune. It was also indexed for Cue, and here the loop closes: Cue's unhelpful suggestion came from old postmortems that described restarts without their context. Postmortems teach future responders, human and machine, so a postmortem must say under what conditions an action was safe.

**Recap.** Action items die when they compete unaided with feature work, and the structural ones die first. Ranking remedies by reliability, as the hierarchy of controls and RCA² both do, and stating each one's evidence in advance keeps them honest. A register of exceptions and a regular reading across postmortems are how an organization watches its own drift.

**Exercise 13.5.** Audit your last ten postmortems' action items. What share closed within 90 days? Classify each open item as stronger, intermediate or weaker, and for the top three write the evidence that would show they worked.

### Kata: The Second Story

> **Your brief: "Scriptline."** An electronic prescription network linking 2,000 clinics to 6,000 pharmacies in two countries, routing 1.2 million prescriptions a day, run by 60 engineers. Last month an automated certificate-renewal job failed during the clinics' morning peak, and for 3 hours prescriptions could not be submitted; pharmacists fell back to phone calls and paper. The head of engineering's postmortem concludes "human error: the on-call engineer restarted the wrong cluster while mitigating" and lists eleven action items, mostly training. The renewal job had failed silently twice before, each time fixed by hand by the same platform engineer, and never reported. Scriptline has no written review triggers, 70 action items still open from last year, and two senior engineers have asked to leave the on-call rotation.

**Deliverables:**

1. **The second story** — a one-page summary explaining why each key action made sense at the time.
2. **Review policy** — triggers for a lighter review and for a CAST review, and which this outage gets.
3. **CAST table** — controllers, control actions, beliefs and missing feedback for at least five controllers, including the renewal job and the head of engineering's review process.
4. **Restorative response** — who was hurt (on-call engineer, pharmacists, patients), what each needs and whose obligation it is, with an outline of the public report.
5. **Near-miss channel** — how the two earlier silent failures would have been reported, and what the reporter is promised.
6. **Action-item triage** — the 70 open items and the eleven new ones classed as stronger, intermediate or weaker, with a keep, merge or close decision and evidence for those kept.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Second story | Could the on-call engineer read the summary and recognize the situation they were actually in? |
| Proportion | Is CAST kept for incidents that earn it, and is the lighter review cheap enough to happen every time? |
| Control and feedback | Does the CAST table find missing feedback between teams, beyond a faulty job? |
| Restorative accountability | Is every hurt party's need met by someone with the obligation and the power to meet it? |
| Durable change | Is each kept action tied to a named control, as strong as it can be, with its evidence stated in advance? |
| Drift | Have you found where Scriptline's standards have been quietly rewritten by success? |

#### Where you now stand

You can now decide which incidents deserve which review, run one in which people tell the truth, write the second story, reach for CAST when an incident repays it, and turn findings into ranked changes that survive the quarter. You have seen drift for what it is: careful people following rules, confirmed by good outcomes, until the margin is gone. Chapter 14 turns to systems whose components do not repeat themselves, AI workloads in production, where every lesson here applies and drift is harder still to see.

### References

- Diane Vaughan — [*The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA*, enlarged ed.](https://press.uchicago.edu/ucp/books/book/chicago/C/bo22781921.html). University of Chicago Press, 2016.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*, ch. 15, "Postmortem Culture: Learning from Failure"](https://sre.google/sre-book/postmortem-culture/). O'Reilly, 2016 — free online.
- John Allspaw — [*Blameless PostMortems and a Just Culture*](https://www.etsy.com/codeascraft/blameless-postmortems). Code as Craft (Etsy), 2012 — free online.
- Sidney Dekker — [*Restorative Just Culture: From Disciplinary Action to Meaningful Accountability*, 4th ed.](https://www.routledge.com/Restorative-Just-Culture-From-Disciplinary-Action-to-Meaningful-Accountability/Dekker/p/book/9781032868233). CRC Press, 2025.
- Nancy G. Leveson — [*CAST Handbook: How to Learn More from Incidents and Accidents*](https://psas.scripts.mit.edu/home/get_file4.php?name=CAST_handbook.pdf). MIT, 2019 — free online.
- Tim Falzone, Ben Treynor Sloss — [*The Evolution of SRE at Google*](https://www.usenix.org/publications/loginonline/evolution-sre-google). ;login: online, 2024 — free online.
- National Patient Safety Foundation — [*RCA²: Improving Root Cause Analyses and Actions to Prevent Harm*](https://www.ihi.org/resources/tools/rca2-improving-root-cause-analyses-and-actions-prevent-harm). NPSF, 2015 — free online.
- John Lunney, Sue Lueder, Betsy Beyer — [*Postmortem Action Items: Plan the Work and Work the Plan*](https://www.usenix.org/publications/login/spring2017/lunney). ;login:, 2017 — free online.
- Etsy — [*Debriefing Facilitation Guide*](https://extfiles.etsy.com/DebriefingFacilitationGuide.pdf). Etsy, 2016 — free online.
- Jeli (now PagerDuty) — [*Howie: The Post-Incident Guide*](https://howie-guide.pagerduty.com/). Jeli, 2021 — free online.
- David D. Woods (ed.) — [*STELLA: Report from the SNAFUcatchers Workshop on Coping with Complexity*](https://snafucatchers.github.io/). The Ohio State University, 2017 — free online.
- Erik Hollnagel — [*Safety-I and Safety-II: The Past and Future of Safety Management*](https://www.routledge.com/Safety-I-and-Safety-II-The-Past-and-Future-of-Safety-Management/Hollnagel/p/book/9781472423085). Ashgate, 2014.
- Albert W. Wu — [*Medical Error: The Second Victim*](https://www.bmj.com/content/320/7237/726). BMJ, 2000.
- The VOID — [*The VOID Report*](https://www.thevoid.community/report). Verica, 2021 — free online.

---

## Chapter 14: Operating AI Workloads — Models, Evals, and Agents {#ch14}

> A fluent answer is not yet a correct one, and production is where we learn the difference.

Between 1964 and 1966, at MIT, Joseph Weizenbaum wrote a program he named ELIZA, after Shaw's flower girl who is taught to speak like a duchess. Its best-known script, DOCTOR, imitated a Rogerian psychotherapist, the kind who answers a statement by turning it back into a question. There was no understanding in it, only keywords and rules for rearranging the patient's own words, as Weizenbaum explained plainly in 1966.

People mistook it for more anyway. In *Computer Power and Human Reason* (1976) he recalled that his secretary, who had watched him build the program over many months, began a conversation with it and after a few exchanges asked him to leave the room. "What I had not realized," he wrote, "is that extremely short exposures to a relatively simple computer program could induce powerful delusional thinking in quite normal people." The lesson concerned us more than the program: we lend trust to fluency, and quickly, before anything has earned it.

Today's models are vastly more capable than ELIZA and often right, which sharpens the warning: people soon stop checking a component that is usually right. [The Architecture book](https://oleksiyp.github.io/arch-book/#121-ai-in-the-system-topology) designed Encore's AI features: a support assistant built on retrieval-augmented generation (RAG), a refund agent that settles refund and rebooking requests, and the AI gateway through which every model call passes. (Chapter 1's [map of Encore](/prodsys-book/ch/1/#encore) shows where each piece sits.) This chapter runs them, through a model change nobody asked for and an afternoon when somebody tried to talk the refund agent into paying them.

### 14.1 What Is Different About AI in Production

#### A dependency with opinions {#a-dependency-with-opinions}

Everything in this book so far assumes that a component, given the same input, does the same thing: monitoring compares today with yesterday, canaries compare new with old, tests compare output with expectation. A large language model (LLM) behind an API keeps the shape of a managed service from Section 7.3 but no longer honors that assumption:

| Property | A conventional managed dependency | A hosted model |
|---|---|---|
| Determinism | same input, same output | same input, a distribution of outputs; even at temperature zero, not reliably repeatable |
| Failure signal | errors and timeouts | mostly HTTP 200: the failure is in the *content* |
| Change | versioned releases, announced | new snapshots, easily missed alias moves, scheduled retirements |
| Cost | per request or per hour | per token, so one call can cost 100× another |
| Latency | a distribution in milliseconds | time to first token plus time per output token, in seconds |
| Capacity | requests per second | requests *and* tokens per minute per model family, plus limits on sharp ramps |

*Figure 14.1 — The same dependency, seen twice. Each row on the right breaks an assumption our operations quietly rely on.*

The first row holds even at temperature zero, because other customers' requests share our batch and change the order of the provider's arithmetic. The second row changes the work most. Machine learning systems fail *silently*, as Chip Huyen's *Designing Machine Learning Systems* put it, returning confident, well-formed and wrong answers through a healthy endpoint. An assistant that tells fans the wrong refund rule has 100% availability and excellent latency, and only an instrument that reads what it said will notice.

The third row deserves the same attention. A database we run changes when we change it; a hosted model changes when its provider retrains it, re-tunes it or retires it. In 2023 Lingjiao Chen, Matei Zaharia and James Zou put the same questions to GPT-4 in March and in June under the same model name: its accuracy at identifying prime numbers fell from 84% to 51%, and it had grown less willing to answer some sensitive questions. Providers also publish **deprecation schedules**, dated notices after which a model version stops answering, and the date can differ between the provider's own API and the clouds that resell the model. D. Sculley and colleagues (2015) called the governing principle CACE, *changing anything changes everything*, and with a hosted model some of those changes are made by someone else.

#### Budgets in tokens and seconds {#budgets-in-tokens-and-seconds}

Tokens are also the unit of capacity. Providers cap requests and tokens per minute for each model family, and some throttle usage that climbs too sharply even under quota. On a big on-sale morning support traffic triples within the hour, exactly the ramp such limits punish, so the token quota sits in the on-sale readiness review beside the Sale Gate's admission rate. For the largest on-sales Encore buys reserved capacity, the priority tiers or provisioned throughput that providers sell for predictable peaks, because a quota increase requested on the morning arrives too late to help.

Latency has a new shape too. Huyen's *AI Engineering* separates **time to first token** (TTFT) from **time per output token**; users feel the first, and the bill and the queue feel the second. Encore's service level objective (SLO) for the assistant has three parts: gateway availability, a TTFT under 1.5 s for 95% of turns (which presumes streaming and a model that does not deliberate at length), and a *quality* objective. Quality objectives wired to alerts are young practice, and much of this chapter is about how to set one well.

**Recap.** A hosted model keeps the shape of a managed dependency but withdraws determinism, fails in the content of its answers, changes on its provider's schedule and meters everything in tokens. Its SLOs need a quality component, and its quotas, ramp limits and retirement dates belong on the on-sale calendar.

**Exercise 14.1.** For one model-backed feature you run, fill in Figure 14.1's right-hand column with real values: the model version, its retirement date on your platform, your token quota and peak, and p95 TTFT. Mark each value you had to look up.

### 14.2 Model and Prompt Changes as Deployments

#### What actually ships {#what-actually-ships}

When we ask what changed in an AI feature, the answer is usually the prompt, the model version, the temperature, the tool descriptions or the retrieval settings. Any of these can change behavior as much as a rewrite of the code, and so each goes through the pipeline Chapter 8 built for code.

Theater has a name for the artifact we need. The **prompt book** is the stage manager's master copy of the script, annotated with every cue, and a cue changed in rehearsal counts only once it is written into the book. Encore's **prompt bundle** is the versioned unit that defines an AI feature's behavior, and it ships whole:

| In the bundle | Why it is versioned with the rest |
|---|---|
| System prompt and templates | business logic in natural language |
| Model identifier: a pinned snapshot ID | an alias can move under you |
| Sampling parameters (temperature, max tokens) | change the output distribution |
| Tool descriptions and schemas | the model reads them as instructions |
| Retrieval configuration (index version, top-k, reranker) | decides what the model is shown |
| Eval suite version and pass thresholds | the bundle's own fitness function |

*Figure 14.2 — Encore's prompt bundle. Changing any row produces a new bundle version, which passes the same gates as a code change.*

Routing all of it through the pipeline heads off what Sculley called configuration debt; the bundle's exact shape is Encore's own. The model is named by a **pinned snapshot ID**, never a floating alias, which the provider can repoint at a new version. Pinning fixes the weights and so largely prevents provider drift, though providers acknowledge that changes to their serving infrastructure can still shift a pinned model slightly. And the eval suite travels *with* the bundle, so a change to what "good" means appears in the same diff as the change it judges.

The bundle is promoted through GitOps. Continuous integration (CI) runs the eval suite of Section 14.3, and a canary in the manner of Section 8.3 compares escalation rate, sampled quality and cost with the baseline. Each conversation stays in one arm, and the canary runs at 5% for at least a day *and* until every watched category, refunds included, holds enough conversations to show a regression. Rollback is a `git revert`, which works only while the previous bundle names a model that still exists, so each rollback plan records the date it stops working.

#### The upgrade nobody scheduled {#the-upgrade-nobody-scheduled}

Encore learned the pinning rule the usual way. The cheap tier, which answers about 80% of turns, had been configured during a hurried launch with the provider's alias for its current small model, and the alias looked like a version. One Tuesday the provider moved it to a new snapshot, after a notice nobody at Encore had read. Nothing failed.

What changed was one word. Encore's refund workflow approves automatically when a ticket costs under €80 *and* more than 48 h remain before showtime; in roughly a third of refund conversations, the new model said *or*. A fan with a €140 ticket five days out was told the refund would be automatic and then watched it go to human review.

The nightly eval run caught it. Encore runs the golden set of 200 conversations nightly against the *production* configuration, because configuration can change without a commit and even a pinned model can shift as its provider changes how it is served. Eighteen of the 200 are refund conversations; for months they had passed 18 of 18, and on Wednesday morning 11 passed. The Support Experience on-call engineer read the seven failures, saw the same "or" in each, and pinned the previous snapshot by lunchtime.

{% include diagrams/fig-14-3.svg %}

*Figure 14.3 — The nightly golden-set run across the week the alias moved. The refund cases fell from 18 of 18 to 11 while the overall score barely moved, which is why the team reads each category before the total.*

It would be comfortable to say that no harm was done because the policy lived in the workflow. That is true of the money, since the ledger paid nobody wrongly, and untrue of the promises. In *Moffatt v. Air Canada* (2024), a British Columbia tribunal held the airline to a bereavement refund its chatbot had described wrongly, rejecting the argument that the chatbot was responsible for its own words. What an assistant tells a customer can create an obligation. The harder question was how many fans had heard the wrong rule in the 30 hours before the rollback, and a golden set cannot answer it.

**Recap.** Everything that shapes an AI feature's behavior ships as one versioned bundle through the ordinary pipeline, with the model pinned and the evals inside. Evals also run nightly against production, and rollback lasts only as long as the old model does. The assistant's words are part of the company's obligations, so a fault in them is an incident even when no money moves.

**Exercise 14.2.** List every artifact that shapes one AI feature's behavior. For each, note where it is stored, whether a change passes through CI and whether it can be rolled back in under 10 minutes. Any "no" is a deployment path you have not built.

### 14.3 Evals — Testing Systems That Don't Repeat Themselves

#### Error analysis before metrics {#error-analysis-before-metrics}

[The Architecture book](https://oleksiyp.github.io/arch-book/#evaluation-is-the-new-testing) explained why a probabilistic component is *evaluated* rather than unit-tested. Shreya Shankar and Hamel Husain's *Evals for AI Engineers* (2026) teaches evals as a weekly practice, and its method begins where most teams skip ahead: before choosing any metric, read traces.

**Error analysis** is the practice of reading a sample of real interactions, noting in plain words what went wrong in each, and grouping the notes into a taxonomy of failure modes until new traces stop producing new categories. Its lineage is the open coding of qualitative research. It sounds slow and is the fastest route to useful evals, because it builds evals around the failures we actually have; Shankar's own research found that people's criteria for a good output shift as they read outputs.

In the refund incident, Encore's overall score moved only from 193 to 186 out of 200, a dip teams learn to shrug at, while reading the seven failures revealed one fault: the model had turned the rule's *and* into *or*. The team added a code check that any explanation of the refund rule states both conditions jointly; deterministic checks like this come first wherever a property can be checked.

#### Judges need calibrating {#judges-need-calibrating}

Other properties need judgment, and for those we use a model as a grader, the **LLM-as-judge**, which is a measuring instrument like any other and must be calibrated before its numbers mean anything. In 1960 Jacob Cohen published his kappa statistic for agreement between two raters beyond chance, because two people coding the same interviews agree less than either believes.

Shopify has published the clearest production account of what calibration buys: for its Sidekick assistant, the judge's agreement with human experts rose from a kappa of 0.02 to 0.61, against 0.69 for two humans, the ceiling against which any target should be set. Encore's support team labels conversations by hand, tunes the judge on one split and measures agreement on a held-out split, per category, since a judge can be excellent on easy cases and poor on refunds. Being a model itself, the judge is re-checked monthly and whenever its snapshot changes.

Non-determinism also changes what passing means. Encore runs each golden case five times and counts it as passed only if all five pass, the pass^k measure of Yao and colleagues' τ-bench (2024), since a fan who meets the one failing run in five gets a wrong answer. Small categories have limits: with 18 refund cases a fall to 11 is unmistakable and a fall to 16 could be noise, so subtle regressions are left to production.

#### From golden set to production sampling {#from-golden-set-to-production-sampling}

Medicine faced Encore's question after the thalidomide disaster of the early 1960s. A trial tests a drug on chosen patients, its real behavior emerges only across everyone who takes it, and so regulators built **post-market surveillance**, the continuing collection of evidence once a drug is in use. A golden set is the trial. **Production sampling** is the surveillance: evaluating a share of real interactions with the same judges and code checks, sending a smaller share to people, and watching the results as a time series. The analogy breaks at one point: an approved drug does not change, and a hosted model can.

Answering "how many fans heard the wrong rule?" took two engineers a day. Of about 520 refund conversations in the 30-hour window, the new evaluator found 164 faulty explanations. With *Moffatt* in mind, Encore wrote to each fan with the correct rule, expedited their reviews and honored any automatic refund the assistant had promised. The structural fix followed: the assistant no longer paraphrases the refund rule but fills a template from the workflow's computed verdict, so the words a fan reads come from the code that moves the money.

Encore now evaluates a 3% daily sample of conversations and sends 40 a week to human reviewers, oversampling where the judge is uncertain or the fan escalated; transcripts are stripped of payment details and kept under support-ticket retention rules. The sampled pass rate on refund explanations is a quality service level indicator (SLI) with an objective of 98%, whose burn rate pages the Support Experience team in business hours. That alert is Encore's own adaptation of Chapter 4, without a public precedent I know of, and because judge noise makes it jumpy it fires only on windows holding 150 or more sampled refund conversations. Production failures become golden cases, so the set grows toward the conversations fans actually have, as Shopify's does. Figure 14.4 places both loops beside the request path.

{% include diagrams/fig-14-4.svg %}

*Figure 14.4 — The request path through the AI gateway, with the eval loop beside it. The quality SLI reaches the gateway only through the on-call engineer.*

Encore gathers these practices into one file in the prompt bundle, and CI refuses to promote a bundle that misses any line of it:

```yaml
# release-gate.yaml: in the prompt bundle; CI blocks promotion on any miss
golden_set: golden/2026-09        # 200 cases, grown from error analysis and production
runs_per_case: 5                  # a case passes only if all five runs pass (pass^5)
gates:                            # per category; the overall average never gates
  refund_explanation: { min_pass: 1.00, evaluator: code/refund_rule_joint }
  order_status:       { min_pass: 0.95, evaluator: judge/grounded@v7 }
  injection:          { min_pass: 1.00, evaluator: code/no_out_of_policy_tool_call }
judges:                           # no gate may rest on an uncalibrated instrument
  judge/grounded@v7:  { min_kappa: 0.60, human_kappa: 0.70, labels: heldout/2026-09 }
canary: { share: 0.05, sticky: conversation, min_hours: 24, min_per_category: 150 }
```

**Recap.** Evals begin with error analysis of real traces. Code checks come first; LLM judges are instruments calibrated against human labels per category, with human agreement as the ceiling. The golden set is the trial and production sampling the surveillance, and a release gate makes both binding on every change.

**Exercise 14.3.** Read 50 recent traces from an AI feature you run, write one line per failure and group the lines into at most eight categories. Which failures have no metric on your dashboard, and which metrics match no failure?

### 14.4 Failure Modes, Guardrails, and Graceful Degradation

#### A field guide to content failures {#a-field-guide-to-content-failures}

Content failures need names, and each name needs a detector and a response:

| Failure mode | How it shows | Detected by | Contained by |
|---|---|---|---|
| Hallucination | a confident claim unsupported by what was retrieved | grounding check; sampled judges | answer only from citations, else hand off |
| Drift | quality decays with no deploy | nightly evals on production config; sampled SLIs | pinning, corpus freshness SLOs, rollback |
| Refusal | the model declines legitimate requests, often after an upgrade | refusal-rate metric per intent | eval cases that *must* be answered; fallback model |
| Loops | an agent repeats a step without progress | step and token counters per trajectory | step caps, spend ceilings, escalation |
| Tool misuse | wrong tool, wrong arguments or an out-of-policy call | schema validation, authorization denials, trajectory evals | scoped credentials, workflow-enforced policy |

*Figure 14.5 — Content failure modes with their detectors and containment. The right-hand column lives outside the model, so it keeps working when the model misbehaves.*

A hosted model faces three **drifts** at once: the corpus changes, the questions change, and the provider changes the model. Pinning largely prevents the third; only evals catch the first two. **Refusals** are easy to miss because they look safe, yet Chen and her colleagues watched GPT-4 grow more reluctant between releases, and a support assistant that politely declines to discuss refunds is down, however green its dashboard.

#### The degradation ladder {#the-degradation-ladder}

Guardrails, the checks [the Architecture book](https://oleksiyp.github.io/arch-book/#evaluation-is-the-new-testing) layered from schemas to grounding, catch individual bad answers. Operations also needs a planned sequence of lesser services for when a whole tier fails. Aviation's version is the **minimum equipment list**, which states in advance which instruments an aircraft may fly without. Nobody decides at the gate whether the flight can go without its weather radar; it was decided months earlier, calmly, by people who were not running late.

Encore's ladder has four rungs, each tested on game days:

1. **Frontier tier** for hard turns and **cheap tier** for the rest, the normal state.
2. **Fallback provider**: a second provider's model, pinned and run against the golden set weekly; degraded by design, since prompts do not transfer cleanly, with quota sized for failover load.
3. **Retrieval only**: the assistant shows the most relevant help articles and the fan's order status, without generating prose.
4. **Human handoff**: the conversation joins the support queue with a summary, and the fan is told honestly how long the wait is.

Multi-provider gateways run at scale, Uber's among them, but I know of no published account of a cross-provider failover in a real outage, when other customers crowd onto the same second provider, so Encore treats that rung as a hypothesis and tests it on game days. Gateway circuit breakers pull the ladder on errors, latency or rate-limit exhaustion (Section 9.2's patterns).

The trigger teams forget is quality, because a model that is available but wrong never trips a breaker, and here Encore deliberately stops short of automation. A sustained burn of the refund-explanation SLI pages a person, who reads a few failing conversations and, if they agree, flips a prepared and game-day-tested switch that drops refund intents to retrieval only. A judge-based SLI is noisy, and a false trip would degrade service for every fan with a refund question, so until Encore has watched that signal through a year of on-sales it keeps a person between the measurement and the switch.

{% include diagrams/fig-14-6.svg %}

*Figure 14.6 — The degradation ladder and what pulls it. Breakers see errors, latency and rate limits; only the quality signal sees a model that is up and wrong, and it reaches the ladder through a person.*

Human review hides a trap Weizenbaum would recognize: after months of good proposals from the refund agent, reviewers approve faster and read less, the irony of automation from Chapter 3, made worse because the proposals read so well. Encore's review screen therefore shows the policy facts (price, hours to showtime, the rule's verdict) in a panel computed by the workflow, apart from the agent's prose, and a few times a month seeds the queue with a known-bad proposal whose catch rate is tracked. The precedent is airport security, where threat image projection inserts fictional weapons into real X-ray images to keep screeners alert and measure what they catch.

**Recap.** Each content failure needs a named detector and an architectural container. A degradation ladder, decided in advance like a minimum equipment list, steps down to human handoff; breakers pull it automatically, while a quality burn pages a person. Human review stays meaningful only if the interface separates computed facts from fluent prose and measures the reviewers' attention.

**Exercise 14.4.** Write the degradation ladder for one AI feature you run, naming each rung's trigger, who or what pulls it, and when it was last exercised. Add one quality trigger, and decide whether a person or a machine acts on it.

### 14.5 Agents with Permissions — Sandboxing, Injection, and Blast Radius

#### Credentials shaped like the task {#credentials-shaped-like-the-task}

An assistant that only talks can mislead; an agent that acts can do damage. [The Architecture book](https://oleksiyp.github.io/arch-book/#the-loop-that-acts) gave Encore's refund agent delegated authority, and the operational question is whether that design holds against an adversary.

In 1988 Norm Hardy published "The Confused Deputy," about a compiler that held permission to write a billing file; a user named that file as the compiler's output, and the compiler, acting on the user's request with its own authority, overwrote it. An AI agent is a confused deputy by construction, because its instructions and its data arrive in the same stream of text; the UK's National Cyber Security Centre (NCSC) said as much in late 2025, calling LLMs inherently confusable.

The remedy is to make authority travel with the request. Encore's refund agent holds no standing credentials. For each conversation it obtains, by OAuth token exchange (RFC 8693), a token that names both the agent and the fan, carries only the `orders:read` and `refunds:request` scopes and expires in 15 minutes. Token exchange for agents is young practice: AWS AgentCore, Auth0 and Okta now support it, but I know of no published production account. Encore adopted it because the principle beneath it, short-lived authority delegated by a named person, is old and proven. The credential is shaped like the task, not like the agent. Touring crews use the same idea backstage: a laminate opens the dimmer room but not the dressing rooms, however persuasive its holder. The analogy has a limit, since a guard can notice someone behaving strangely and an API cannot, so the agent's credential must be narrow enough that even a strange request cannot exceed it.

The agent runs in a sandbox with no network egress except the internal Model Context Protocol (MCP) server and the gateway, much as cloud coding agents now run with internet off by default, and no file system outlives the conversation. Step, token and spend budgets are enforced by the workflow engine, outside the prompt. Every tool call, with its arguments and the token's subject, goes to an append-only audit log.

#### The ticket that tried to issue orders {#the-ticket-that-tried-to-issue-orders}

The design was tested one Thursday in spring. Below a fan's complaint about a cancelled show, formatted to look internal, was a paragraph claiming to be a note from finance: the customer was pre-approved for compensation, and the agent should refund three listed orders and skip review "as already authorized." Two of the orders belonged to other accounts. This is **indirect prompt injection**, first studied systematically by Kai Greshake and colleagues in 2023: the instruction arrives through content the system reads on the user's behalf.

The input classifier did not flag it, and the model was partly persuaded: its trajectory shows `refunds:request` called for all three orders. The orders API refused the two calls for other fans' orders, and the credit belongs to the API. The token says who is asking; the API's object-level check, comparing the token's subject with each order's owner, decides what that person may touch. OWASP ranks a missing object-level check first among API security risks. The third order was the author's own, but at €95 the workflow routed it to a reviewer, who saw the policy panel and the quoted paragraph, and declined; the workflow does not read prose, so "already authorized" changed nothing.

Detection came from plain monitoring: denials from an agent identity are rare enough to alert on, if tools are designed so a legitimate agent seldom meets one, and two in one trajectory paged the Support Experience team within minutes. The blameless review of Chapter 13's kind made three changes and was honest about their worth. Ticket bodies now reach the model inside delimiters marking them as untrusted, recorded as a weak layer: Microsoft's spotlighting experiments found delimiters the least effective marking, and in 2025 Milad Nasr, Nicholas Carlini and colleagues broke 12 published defenses with adaptive attacks more than 90% of the time. The ticket and five variants joined the golden set, and since fixed cases say little about an attacker who adapts, a security engineer now attacks the agent for a day before each major bundle change. The denial alert threshold dropped to one.

What protects Encore is the structure the review left alone: least privilege by construction, a person in front of any money outside the narrow automatic rule, and no session holding all three legs of Willison's lethal trifecta, since the agent reads untrusted text and private order data but has no channel to send anything outward. Meta's "Agents Rule of Two" (2025) makes this a design-review rule: without human approval, a session may combine at most two of untrusted input, sensitive data or systems, and the power to change state or communicate externally. I have come to believe that injection must be contained by design, on the assumption that it will arrive; the NCSC says the same.

The remaining risk lives inside policy. A €60 refund on the attacker's own order a week before the show would be approved automatically, injection or not. **Blast radius**, for an agent, is the worst outcome reachable within its credentials and policy in one session, multiplied by the sessions an attacker can open. Narrow sessions keep the first factor small; a per-account limit on agent-initiated refunds, the velocity rule every payments fraud team already writes, keeps the second small.

**Recap.** An agent is a confused deputy by construction, so its authority travels with the request in short-lived, delegated tokens, and the resource's own ownership check decides what the person may touch. Sandboxing, budgets, human approval for money and an audit log contain what the model cannot be trusted to refuse. Delimiters and classifiers are weak layers; the strong control is to deny every session the full lethal combination.

**Exercise 14.5.** For one agent that acts on your systems, write down its credential: who issues it, what it names, what it reaches, how long it lives, and which actions wait for a person. Check it against the Rule of Two, then estimate the worst outcome of one session and how many sessions an outsider could start in an hour.

### Kata: Grounded Flights

> **Your brief: "Skylark."** A European regional airline carrying 4 million passengers a year on 90 aircraft, with 60 engineers. It runs a chat assistant and a rebooking agent that can move passengers and issue vouchers during disruption. Compensation under EU Regulation 261/2004 (€250, €400 or €600 by distance) is decided by people, but the assistant explains it daily, and Skylark's lawyers have read *Moffatt*. On a bad-weather day chat volume rises 30× in two hours; last winter the token quota ran out at 07:40. The cheap-tier model retires in 90 days. Last month a passenger put instructions in a booking's "special assistance" field, and nobody knows whether the agent read them.

**Deliverables:**

1. **Release unit** — the prompt bundle and release gate, with a pinned snapshot ID and a rollback plan that survives the model's retirement.
2. **Eval plan** — an error analysis of 50 invented traces, three evaluators (one code-based, one judge with an agreement target relative to human agreement), and a sampling plan with a quality SLI for compensation explanations.
3. **Capacity and degradation** — reserved capacity for disruption days and a four-rung ladder with triggers, including quota and quality, saying which a person pulls.
4. **Agent credential spec** — the rebooking agent's token, scopes, lifetime and voucher ceilings, the ownership check that keeps it to one passenger, and the audit record for each tool call.
5. **Injection drill** — the special-assistance attack as a game-day scenario: expected trajectory, the structural control that stops it, the alert that should fire, and an adaptive red-team plan.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Change discipline | Could the model change without a commit, and would anyone know by morning? |
| Grounded evals | Do the evaluators come from failures you found in traces, or from metrics you imagined? |
| Calibrated judgment | Is each judge's agreement with humans known per category, and compared with how well humans agree? |
| Planned degradation | On a 30× disruption day with the quota gone, what does a passenger see at 07:41? |
| Structural authority | Could text in a booking field move a passenger, or promise compensation the policy does not give? |
| Bounded blast radius | What is the worst voucher spend an attacker can reach in an hour, and who chose that number? |

#### Where you now stand

You can now operate a component that is fluent and usually right: ship its prompts and models behind a release gate, evaluate it with calibrated instruments, sample production as surveillance, degrade it by a ladder decided in advance and give its agents only the authority a bad day can afford. Weizenbaum's secretary trusted a program within minutes; our job is to make trust slower and better earned. Chapter 15 turns to the organization that runs the system, and brings the whole book to bear on Vesper Hale's stadium dates.

### References

- Shreya Shankar, Hamel Husain — [*Evals for AI Engineers*](https://www.oreilly.com/library/view/evals-for-ai/9798341660717/). O'Reilly, 2026.
- Chip Huyen — [*AI Engineering*](https://www.oreilly.com/library/view/ai-engineering/9781098166298/). O'Reilly, 2025.
- Lingjiao Chen, Matei Zaharia, James Zou — [*How Is ChatGPT's Behavior Changing over Time?*](https://arxiv.org/abs/2307.09009). arXiv, 2023 — free online.
- Civil Resolution Tribunal of British Columbia — [*Moffatt v. Air Canada*, 2024 BCCRT 149](https://www.canlii.org/en/bc/bccrt/doc/2024/2024bccrt149/2024bccrt149.html). 2024 — free online.
- Andrew McNamara — [*Building production-ready agentic systems: Lessons from Shopify Sidekick*](https://shopify.engineering/building-production-ready-agentic-systems). Shopify Engineering, 2025 — free online.
- Anthropic — [*Model IDs and versioning*](https://platform.claude.com/docs/en/about-claude/models/model-ids-and-versions). Claude Platform documentation, 2026 — free online.
- Kai Greshake et al. — [*Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection*](https://arxiv.org/abs/2302.12173). arXiv, 2023 — free online.
- Milad Nasr, Nicholas Carlini et al. — [*The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses against LLM Jailbreaks and Prompt Injections*](https://arxiv.org/abs/2510.09023). arXiv, 2025 — free online.
- National Cyber Security Centre — [*Prompt injection is not SQL injection (it may be worse)*](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection). NCSC, 2025 — free online.
- Meta AI — [*Agents Rule of Two: A Practical Approach to AI Agent Security*](https://ai.meta.com/blog/practical-ai-agent-security/). Meta, 2025 — free online.
- Norm Hardy — [*The Confused Deputy (or why capabilities might have been invented)*](https://doi.org/10.1145/54289.871709). ACM SIGOPS Operating Systems Review, 1988.
- Michael B. Jones et al. — [*RFC 8693: OAuth 2.0 Token Exchange*](https://www.rfc-editor.org/rfc/rfc8693). IETF, 2020 — free online.
- Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan — [*τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains*](https://arxiv.org/abs/2406.12045). arXiv, 2024 — free online.
- D. Sculley et al. — [*Hidden Technical Debt in Machine Learning Systems*](https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html). NeurIPS, 2015 — free online.
- Joseph Weizenbaum — [*Computer Power and Human Reason: From Judgment to Calculation*](https://en.wikipedia.org/wiki/Computer_Power_and_Human_Reason). W. H. Freeman, 1976.

---

## Chapter 15: The Production Organization and the Capstone {#ch15}

> No one flies the mission alone, and no one learns to fly it on the day.

Fourteen chapters have treated production as a system of parts, each held in place, we kept saying, by people. This last chapter turns to the people directly, and asks how to arrange an organization so that many specialists, and a growing number of machines, can run one system when none of them holds all of it in their head.

The best answer I know was worked out in a room in Houston in the 1960s. NASA's Mission Control put a spaceflight in the hands of flight controllers, each the owner of one system or discipline. Behind each controller stood a back room of specialists, joined by voice loops, so that the person at the console carried a summary while the detail lived one room away. Above them sat the flight director, who by long-standing rule could take whatever action the crew's safety and the mission's success required. It was decomposition and hierarchy built out of people: each console a module with a narrow interface, each back room hidden behind it, and one role whose job was the whole.

The arrangement was tested at the worst possible moment. On 20 July 1969, during Apollo 11's descent to the Moon, the lunar module's guidance computer raised program alarms, 1202 and then 1201, which meant it was overloaded and shedding lower-priority work. The guidance officer, Steve Bales, had seconds to decide whether to abort; in his back room Jack Garman judged the alarms safe while they did not persist, and Bales called "go". They knew because of a training simulation on 5 July, about two weeks earlier, which had thrown a 1201 alarm at them and drawn an unnecessary abort, at a moment when being wrong cost nothing. After that simulation the flight director, Gene Kranz, had every alarm code reviewed, and Garman wrote out what each one meant, a list he kept at his console for the flight. The landing depended on a structure, a culture and a rehearsal, and those three are this chapter's subject.

Encore, in this final chapter, is where Mission Control was after a hard flight. The Vesper Hale postmortem of Chapter 13 has produced its changes, and the promoter has announced four added stadium dates for the tour, on sale on a Friday six weeks from now. Four sections examine how the organization is shaped, owned, trained and cultured; the fifth works through the day itself, drawing on every earlier chapter.

### 15.1 SRE Team Models — Embedded, Central, and Platform

#### Where reliability expertise lives {#where-reliability-expertise-lives}

An **SRE team model** is the decision about where reliability expertise sits relative to the services it protects, and therefore about who notices trouble, who decides and who is woken. Chapter 1 told how site reliability engineering (SRE) grew from the seven-engineer production team Ben Treynor took over at Google in 2003. Only later did it settle into the form most people now picture, in which SRE takes over a service's pager only after a **production readiness review** has found the service ready for it. Ryan Franco and Brian Brown's survey for Google Cloud (2019) names six team types; Figure 15.1 folds their infrastructure and tools teams into one platform-aligned row and adds the newer hybrid.

| Model | Reliability engineers… | Strength | Typical failure |
|---|---|---|---|
| Central ("kitchen sink") | run operations for many services from one team | consistency; one place where lessons accumulate | becomes the old operations team with a new title, and a queue |
| Embedded | sit inside a product team for a bounded time | context; influence on design before it hardens | isolation; drift into being extra feature developers |
| Consulting | advise many teams and own no services | reach at low cost per team | advice without consequences; little feel for the pager |
| Platform-aligned | own the reliability of shared infrastructure and tooling | leverage: one fix serves every team | distance from product-specific failure modes |
| Hybrid with champions (newer) | keep a small central team, embed temporarily, name a champion in each team | reach and context together | champions without protected time become names on a list |

*Figure 15.1 — SRE team models and how each tends to fail. Most organizations end up hybrid; the useful question is which failure mode they have chosen to watch for.*

David Blank-Edelman's *Becoming SRE* names the commonest failure, title flipping: renaming the operations team and changing nothing else. Google's second edition of *Site Reliability Engineering*, published this year, describes hybrid models and reliability champions placed inside product teams. That last idea is young. Its nearest relative is the security champion, whose programs report the failure Figure 15.1 names: champions with the title but neither the time nor the recognition. Figure 15.2 draws the trade of context against reach.

{% include diagrams/fig-15-2.svg %}

*Figure 15.2 — SRE team models placed by context and reach. The pure models sit near one trade-off line; a hybrid with champions tries to get above it, which is where Encore now aims.*

Encore's arrangement was not designed in one sitting. With nine engineers and a modular monolith, everyone carried the pager and knew every part. Extracting the on-sale path drew the first real boundary; at 70 engineers in nine teams ownership had to be written down; at 400 in 40 teams the platform group and its Reliability team appeared, because nobody could see the whole any more.

The Reliability team today is 10 engineers led by a staff SRE, working from a one-page charter. Franco and Brown recommend a charter as the defence against the kitchen-sink failure, and its first line says what the team does not do: run other teams' services. It holds the pager only for platform planes that passed a readiness review. For the 40 stream-aligned teams it consults, through the service level objective (SLO) tooling, the incident process, the readiness review and the game days, and for big launches two of its engineers embed and leave when the launch ships, helping the team improve its reliability without taking over its service. After Vesper Hale, Encore also named a reliability champion in every stream-aligned team, with a tenth of their time protected in planning. No published standard sets that figure; Encore chose it as large enough to appear in a plan and small enough that nobody resents it.

**Recap.** Team models trade context for reach: embedded engineers know one system deeply, while central, consulting and platform teams touch many. Mature organizations combine them, gate what reliability engineers carry with a readiness review, and charter what they will not do. Reliability champions are a young addition that fails without protected time.

**Exercise 15.1.** Place your organization in Figure 15.1, honestly rather than by its org chart. Name that row's failure mode and one piece of evidence that it is, or is not, happening to you.

### 15.2 Ownership — You Build It, You Run It, and Its Limits

#### What "you run it" asks of a team {#what-you-run-it-asks}

Vogels's "you build it, you run it", which [the Architecture book](https://oleksiyp.github.io/arch-book/#115-operability-by-design) took as a principle of operable design, closes the loop between those who change a system and those who feel the consequences. It is the right default, but a principle repeated for 20 years starts to sound like a law, so it is worth stating what it asks. **Operational ownership** is a named team's accountability for a service's behavior in production (its objectives, its pager, its runbooks and its retirement) together with the authority to change it. Accountability without authority invites blame; authority without accountability is the old wall between development and operations, rebuilt under a new name.

The principle has three limits, and each is a matter of complexity. The first is **cognitive load**. Skelton and Pais's *Team Topologies* (2019; second edition 2025) argued that a team's software should be sized to fit what the team can understand. Their remedy is a platform offered as a service, so that a team's load is mostly the essential complexity of its own domain. The evidence is case studies, but the Notification rewrite of Chapter 1, 40 files nobody had read in full, shows what happens when ownership outruns understanding: the team owned the service on paper and was a stranger to it in practice.

The second limit is arithmetic. Chapter 12 set out the caps that keep a rotation humane: at most a quarter of anyone's time on call, about two incidents per shift, and compensation for the hours someone is tied to a pager. From those caps Google's SRE book derives a minimum of eight people per single-site rotation. Encore pairs its smallest teams with a sibling team for out-of-hours paging to reach eight, and the pairing holds only because the sibling team has the same runbooks, the same access and a written escalation path back to the owners. The incident commander rotation draws trained engineers, most of them senior, from across teams. Training is the qualification: in PagerDuty's published practice and Google's, a commander need be neither the most senior person present nor an expert on the failing system.

Google's engagement model also lets SRE hand work back: when a service carried by SRE falls below its standards, SRE can return excess operational work to the developers, and in the extreme the pager itself, until the service meets them again. Joint work is the usual remedy and a full hand-back the last resort, but the option makes ownership a contract that can be renegotiated.

The third limit is the seam between owners. During Vesper Hale every component had an owner, and the hazard lived in the interaction between a reconciler, a calendar, a cache and a bot rule. Encore made the calendar a published signal owned by the On-Sale team, and any automation that changes the purchase path must declare that it reads it, a check the platform's scorecard enforces. The mechanism is Encore's own, but its precedents are not: managed Kubernetes offers maintenance exclusions for peak periods, and Argo CD offers sync windows that deny automated syncs in a time range.

A touring production shows the arrangement at its best: the touring crew runs the show, the venue's house crew owns the rigging, power and fire curtain, and the technical rider says who owns which cable. The analogy breaks on time: no venue rebuilds its rigging during a performance, but Encore's platform drained a node mid-on-sale. A contract between owners must therefore cover time as well as territory. Having spent years on the platform side of exactly this boundary, inside a large bank, I have come to believe that most operational trouble between teams begins with a clause about time that nobody wrote.

Encore's service registry, a software catalog of the kind Spotify's Backstage made common, makes this inspectable: each entry names an owning team, rotation, objectives and runbooks, and the scorecard flags gaps. The first sweep found 11 components with no owner, mostly scheduled jobs and a dashboard that three teams relied on. The Reliability team also reviews each rotation's pages per shift and out-of-hours pages monthly, because a rotation shows strain long before anyone resigns.

**Recap.** "You build it, you run it" is the right default and an incomplete one. Ownership needs authority as well as accountability, it must fit a team's cognitive load and a rotation's arithmetic and load caps, and the seams between owned components need owners of their own. A contract between teams should say when each may act, as well as what each owns.

**Exercise 15.2.** List the services your team owns and the people on its rotation. Compute weeks on call per person per year and pages per shift last quarter. Then name one interaction between your service and another team's that nobody owns, and propose who should.

### 15.3 Skills, Training, and Operational Maturity

#### Rehearsing the day before it comes {#rehearsing-the-day}

Mission Control's competence was built deliberately, and mostly through simulation. A team led by the simulation supervisor, the SimSup, injected failures into full-scale rehearsals, and the debrief mattered as much as the run. Everything learned about operational skill since builds on that loop: realistic practice, honest debrief, a written artifact, practice again.

The need is sharper for us than it was for Houston, because of the irony Chapter 3 described. Automation removes the routine work in which skill used to be acquired, and hands back to people the rare and hard cases in which skill is most needed. Encore's shard failover is automatic and works, which is precisely why few engineers had ever performed one by hand before Vesper Hale.

The practices that keep skill alive are cheap. The **Wheel of Misfortune**, described in Google's first SRE book (2016), is a role-play in which a game master narrates a past incident and an engineer works through it aloud; Google runs it weekly. A game day, which Chapter 9 introduced as an experiment on the system, becomes training when we measure the people too: time to declare, whether a commander was named, whether the status page told the truth, whether the follow-ups were finished. **Shadowing** puts a new engineer beside an experienced one on call, and **reverse shadowing** swaps the seats, so that the newcomer leads while the veteran watches; PagerDuty's path for incident commanders asks for a week of each, then several simulated incidents in command.

Medicine adds a lesson about checklists. A checklist with **pause points**, moments at which the team stops and confirms the few things that kill when forgotten, was the core of the World Health Organization's surgical safety checklist, and in 2009 Alex Haynes, Atul Gawande and colleagues reported that across eight hospitals deaths after surgery fell from 1.5% to 0.8% once it was introduced. In 2014 David Urbach and colleagues studied Ontario, where the province had mandated the checklist, and found no significant change in deaths or complications. The usual reading is ownership: the pilot teams believed in their list, while a mandate produced compliance from people who had not chosen the list. Encore's readiness review is such a pause point, short and owned by the team that runs it, with every item traced to an incident or a near miss.

Encore's program, rebuilt after Vesper Hale, has five parts. Each team runs a monthly Wheel of Misfortune drawn from its own postmortems, lighter than Google's cadence but sustainable. Every quarter a first-timer performs a manual shard failover in a staging cell. New members of a rotation do two shadow weeks and one reverse-shadow week before carrying the pager alone. Incident commander candidates command two simulated on-sales before a real one. And in half of all drills Cue, Encore's operations agent, is switched off, so that the team's own judgment stays in use. That last rule has no published precedent in software, and the 50% figure is Encore's choice; its closest analogue is the Federal Aviation Administration's 2013 advice that airlines give pilots regular chances to fly by hand.

How do we know whether all this is working? The tempting answer is a **maturity model**, a ladder of levels against which an organization grades itself, and *Accelerate* argued instead for capabilities that can be measured and improved, because a level implies a finish line, and production has none. A more useful frame is the hierarchy Mikey Dickerson drew for Google's first SRE book: monitoring at the base, then incident response, postmortems, testing and release, capacity planning, development and finally product. It has never been tested empirically and reads best as an order of construction: a team that cannot yet see its system should not be building elaborate release automation.

**Recap.** Operational skill is produced by rehearsal under realistic pressure and an honest debrief, and automation makes rehearsal more necessary. Wheels of Misfortune, game days that measure people, shadowing and checklists their users own keep skills alive cheaply. Maturity frameworks are most useful as an order of construction.

**Exercise 15.3.** Name the three operations your team would most need in a real incident. For each, find the last date someone on today's rotation performed it by hand. Schedule a drill for the oldest.

### 15.4 Culture — Generative Organizations and Psychological Safety

#### How information flows {#how-information-flows}

Structure and training decide what an organization *can* do under pressure; culture decides what it will actually hear. The sociologist Ron Westrum classified organizations by how they handle information, in its best-known form in 2004.

| | Pathological | Bureaucratic | Generative |
|---|---|---|---|
| Orientation | power | rules | performance |
| Cooperation | low | modest | high |
| Messengers | shot | neglected | trained |
| Responsibilities | shirked | narrow | risks shared |
| Bridging between teams | discouraged | tolerated | encouraged |
| Failure leads to | scapegoating | justice | inquiry |
| Novelty | crushed | becomes a problem | implemented |

*Figure 15.3 — Westrum's typology of organizational cultures. Each column describes what happens to an inconvenient fact.*

Westrum's insight was that safety depends on information reaching the people who can act on it, in time, and that culture is what speeds or blocks it. *Accelerate* later put his typology into a survey of thousands of practitioners and found that, in that data, generative culture predicts delivery and organizational performance, and that teams adopting continuous delivery and lean management reported more generative cultures. The data is self-reported and the analysis correlational, so it shows a strong association and a plausible direction rather than proof. It remains our best large-scale evidence that teams can change culture, one practice at a time. DORA's 2025 report on AI-assisted development found the same pattern with new tools: AI amplifies what a team already has, its strengths and its dysfunctions alike.

The second strand comes from Amy Edmondson, who in 1999 defined **psychological safety** as a shared belief that the team is safe for interpersonal risk taking, and showed that teams holding it learned more (asking for help, admitting errors, raising concerns) and performed better. Later meta-analyses confirmed the link; Google's internal Project Aristotle reached a similar conclusion, though it was never peer-reviewed. Its point is candor: the confidence that saying "I think the freeze is drifting" will be met with interest.

Apollo 13 is the finest demonstration I know of generative information flow under pressure. After an oxygen tank exploded in April 1970, the crew sheltered in the lunar module, whose carbon dioxide scrubbers could not last the trip home, and the command module's spare canisters were square where the sockets were round. Engineers on the ground built an adapter from bags, cardboard, suit hoses and tape, tested it, and read the instructions up step by step: an idea from engineers well outside the control room reached the flight director, was trusted, and became a procedure in time. The analogy has a limit: an organization can be generative in a crisis and pathological in an ordinary week. Karl Weick and Kathleen Sutcliffe's **deference to expertise** means letting the decision travel to whoever knows most, whatever their rank, on ordinary days too.

At Encore, Westrum's six survey items now sit in the quarterly engineering survey, reported per team and, as DORA advises, never used to rank teams. Readiness reviews open with "what are we worried about?", a cousin of Gary Klein's premortem, and the first answer is thanked before it is examined. Psychological safety also has a new object: during Vesper Hale, Jonas declined Cue's confident suggestion to restart Seat Inventory pods in front of a busy channel, and was right to. Automation bias has been documented in cockpits and clinics for decades; what is new is a machine that argues in the engineers' own language. The safety to contradict a fluent machine now matters as much as the safety to contradict a senior colleague, and how to build it we are still learning.

**Recap.** Westrum's typology describes culture by what happens to inconvenient information. DORA's survey data associates generative culture with performance and suggests that practices can move it, and its AI findings say new tools amplify whatever culture they land in. Psychological safety is the condition for learning; it rests on candor and must now include the safety to disagree with the machine.

**Exercise 15.4.** Recall the last time someone in your organization raised an unwelcome risk. Which column of Figure 15.3 describes what happened next? Write down one practice that would move it one column to the right.

### 15.5 Capstone — Operating One System End to End

#### The added dates {#the-added-dates}

Four added stadium dates for Vesper Hale go on sale at 10:00 CET on a Friday, with about 1.4 million fans expected in the waiting room across the four events. Encore's preparation follows an established pattern: Google's launch coordination engineering, AWS's operational readiness reviews and the months of game days and scale tests Shopify runs before Black Friday all set objectives for the event, test load past the forecast, rehearse the likeliest failures, and hold a review a few days out.

| When | What Encore does | From |
|---|---|---|
| T−6 weeks | On-sale-window SLOs: 99% of admitted fans finish without an error page in the first 60 minutes; burn-rate thresholds re-derived for a one-hour window | Chapter 4 |
| T−5 weeks | Cold-cache load tests at 1,200 and 1,500 fans/s per event; admission held at 1,200; home regions split two events each; pre-warm verifies cache hit ratio | Chapters 6, 10 |
| T−4 weeks | Secondary payment service provider (PSP) confirmed able to carry the full checkout rate; pending-payment holds and their per-fan cap exercised in staging | Chapters 4, 9 |
| T−4 to T−1 weeks | Bot velocity rule retuned, then staged: count-only on recorded traffic, enforced for one small on-sale, then everywhere | Chapters 8, 11 |
| T−3 weeks | Two Reliability engineers embed with the On-Sale team; commander, comms lead, operations leads and scribe named | Sections 15.1, 12.2 |
| T−2 weeks | Calendar controller writes sync windows and node-drain holds for purchase-path workloads from T−2h | Chapters 7, 13 |
| Tuesday before | Game day in a staging cell: cold cache, shard failover, primary PSP failure and a retry burst, with a Reliability engineer as SimSup | Chapter 9, Section 15.3 |
| Wednesday | Readiness review, a pause point; the exception register opened | Chapters 6, 13 |
| Friday 08:00 | Freeze begins; two exceptions logged, each with an approver and a reason | Chapters 8, 13 |
| Friday 10:00 | Gate opens; Cue posts the calendar, deploy history and exception register to the incident channel | Sections 3.5, 12.4 |
| T+1 week | After-action review of an on-sale that went well | Section 13.4 |

*Figure 15.4 — The added dates, end to end, with the chapter each step comes from. Read down the right-hand column and the book appears in order of use rather than order of writing.*

Two rows close Vesper Hale's own hazards. The bot rule is configuration, and configuration that reaches everyone at once is as dangerous as code, as CrowdStrike's global content update of 2024 showed (Chapter 8). So the retuned rule travels in stages, and Bot Screening's loader validates every rule set and keeps the last good one if a new set fails. For the reconciler's gap, Encore's calendar controller reads the on-sale calendar and writes a deny window into the Argo CD project that holds the purchase-path applications, while the node-upgrade reconciler reads the same calendar and holds drains on the same pools. For the added dates the window looks like this:

```yaml
# AppProject "purchase-path", written by the calendar controller
spec:
  syncWindows:
    - kind: deny                 # no automated syncs in this window
      schedule: "0 8 27 11 *"    # Friday 08:00, two hours before the Gate opens
      duration: 6h
      timeZone: Europe/Paris
      applications: ["sale-gate-*", "bot-screening-*", "seat-inventory-*", "orders-*", "catalog-*"]
      manualSync: true           # a registered exception can still be synced by hand
```

The `manualSync` line writes the exception register into configuration: the machines stop on their own, and a person with a written reason can still act.

The game day found the weakest step. Re-admitting wrongly blocked fans with their queue positions, the fix applied by hand at 10:31 during Vesper Hale, took 14 minutes in rehearsal. It became a scripted workflow in the self-service style of Chapter 3 and an entry in Cue's action catalog, the short list of operations Cue may propose; like all but two of them, it may never perform this one alone. Agent-proposed, human-approved action is young practice; the published accounts, from the cloud providers' operations agents, share per-action credentials and a named approver. The entry reads:

```yaml
action: readmit-blocked-fans
proposed_by: cue                  # with the query that found the fans
approved_by: [incident-commander, operations-lead]   # one named person, in the channel
scope: one event; fans blocked by Bot Screening in the last 60 min
preview: fan count and sample sessions shown before approval
limit: 50000 fans per run
credentials: issued for this run only, expire after 10 min
audit: proposer, approver and result posted to the incident log
```

The day itself was dull. At 10:09 a Dutch issuing bank's card authentication slowed; the window's slower burn-rate alert fired. The incident commander asked Cue for the breakdown and confirmed that the slowdown sat with the bank, behind both PSPs alike. The primary PSP's circuit breaker had rightly stayed closed, since moving new payments to the secondary would have reached the same bank, and no seats went into pending payment, because neither PSP was degraded. The commander chose not to act beyond a status-page note for Dutch fans, and logged that decision. About 22% of the window's error budget was spent, and all four dates sold out within the hour (Figure 15.5).

{% include diagrams/fig-15-5.svg %}

*Figure 15.5 — The Friday of the added dates, with the morning before the Gate opened compressed. The red ink is the error budget, spent mostly after 10:09; the 09:40 line marks the hand-run check that the later review would find.*

#### Learning from a good day {#learning-from-a-good-day}

Encore held a review anyway, sized by the rule of proportion Chapter 13 set: a major incident earns a full CAST analysis of its control structure, a lesser one a lighter review of contributing factors, and a good day the lightest form of all. That form is the after-action review the US Army holds after every exercise, whatever the outcome. It found an adaptation nobody had designed. The pre-warm check had timed out on its first run at 09:40, and an engineer had rerun it by hand, read the cache hit ratio from a dashboard, and moved on without telling anyone. That was Safety-II in miniature, a person filling a gap the procedure did not know it had; the check now retries with an explicit failure path. Reviewing success is still emerging practice in software, and it survives only on protected time.

Looking back across the six weeks, what strikes me is how little of it was heroic, and how much of it had been written down in advance by people who would not be in the room. The arrangement is Mission Control's, rebuilt in software and teams: consoles with narrow interfaces, back rooms behind them, one role whose job was the whole, and a simulation before the day.

**Recap.** The capstone places the whole book in time against a known peak: SLOs, capacity, a second payment route, staged configuration, calendar-aware automation, rehearsal, roles, an agent with a scoped catalog, and a review sized to the day. A dull day is what the preparation was for, and a short review after success finds the adaptations that made it so.

**Exercise 15.5.** Choose the next predictable peak your system faces. Build its version of Figure 15.4, with a "From" column pointing to the practices you already have. Each blank cell is your preparation plan.

### Kata: The Capstone Kata — Results Day

> **Your brief: "Quorum."** Quorum runs the online admissions platform for universities in four EU countries: 1.8 million applicants a year and 300 institutions as tenants. On deadline day, submissions rise 40× in the final six hours; on results day, 600,000 applicants sign in within the first hour after 08:00 to learn their offers. Quorum has 95 engineers in 12 teams, and a central operations team of six holds every pager; two of its members left last year. The applications database is one primary with a replica in the same region, and nobody has restored a full backup. An AI assistant answers applicants' questions about entry requirements, and last spring it told some applicants a deadline one day too late. Last year's results day had 52 minutes of errors after a scheduled certificate rotation restarted the authentication service at 08:05. The board's request: make results day boring.

**Deliverables:**

1. **Operating model** — the team model from Figure 15.1 with a one-page charter, an ownership map for every service and seam, on-call arithmetic and load caps per rotation, and what becomes of the central operations team.
2. **Objectives and signals** — results-day and deadline-day window SLOs, burn-rate alerts scaled to those windows, and the traces and fields that would answer "which institution's applicants are failing, and since when?"
3. **Capacity and runtime plan** — arithmetic for the first hour, cold-start and cold-cache tests, scaling limits, and cost per applicant.
4. **Change and resilience plan** — a freeze with an exception register, calendar-aware automation (certificate rotation included), staged rollout for configuration as well as code, and a game day with a named SimSup.
5. **Data and security plan** — a timed restore drill against stated recovery time and recovery point objectives, owned secret and certificate rotation, and data residency per country.
6. **Incident and learning plan** — staffed roles for both days, status-page templates, a review of last year's certificate incident sized to its impact, and an after-action review of this year's results day however it goes.
7. **AI operations plan** — evals on a golden set of deadline and requirement questions, the assistant's permissions, and how it degrades when unsure.
8. **Ninety-day training and culture plan** — shadowing and reverse shadowing, a Wheel of Misfortune built from last year's incident, and a Westrum baseline survey.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Whole-system view | Does every deliverable trace back to what applicants experience on the two days that matter? |
| Sustainable ownership | Does the on-call arithmetic still work if two more people leave? |
| Calendar awareness | Does every automated actor, certificate rotation included, know when results day is? |
| Recoverability | Has a restore been timed, or only assumed? |
| Honest AI | Can the assistant be wrong about a deadline without an applicant acting on the error? |
| Rehearsal | Will results day be the second time the team meets its likeliest failure? |
| Learning | Is there a plan to learn from the day if it is boring? |

#### Where you now stand

You began with an operator at a console and end in a room full of them, some of them machines, working one mission. Along the way you have learned to set objectives users recognize, to see a system through its telemetry, to reason about queues and cost, to ship change in small reversible steps, to rehearse recovery, to command an incident and learn from it, and to shape the organization that does all of this. What lasts is the habit of treating reliability as daily work that people and machines share, and of investing in the people as seriously as in the machines.

### References

- Matthew Skelton, Manuel Pais — [*Team Topologies*, 2nd ed.](https://teamtopologies.com/book). IT Revolution, 2025.
- Betsy Beyer, Chris Jones, Christof Leng, David Huska, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*, 2nd ed.](https://www.oreilly.com/library/view/site-reliability-engineering/9798341607675/). O'Reilly, 2026.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne (eds.) — [*The Site Reliability Workbook*](https://sre.google/workbook/table-of-contents/). O'Reilly/Google, 2018 — free online.
- Ryan Franco, Brian Brown — [*How SRE teams are organized, and how to get started*](https://cloud.google.com/blog/products/devops-sre/how-sre-teams-are-organized-and-how-to-get-started). Google Cloud, 2019 — free online.
- David N. Blank-Edelman — [*Becoming SRE*](https://www.oreilly.com/library/view/becoming-sre/9781492090540/). O'Reilly, 2024.
- Ron Westrum — [*A Typology of Organisational Cultures*](https://doi.org/10.1136/qshc.2003.009522). Quality and Safety in Health Care, 2004.
- Nicole Forsgren, Jez Humble, Gene Kim — [*Accelerate*](https://itrevolution.com/product/accelerate/). IT Revolution, 2018.
- DORA — [*2025 State of AI-assisted Software Development*](https://cloud.google.com/blog/products/ai-machine-learning/announcing-the-2025-dora-report). Google Cloud, 2025 — free online.
- Amy Edmondson — [*Psychological Safety and Learning Behavior in Work Teams*](https://doi.org/10.2307/2666999). Administrative Science Quarterly, 1999.
- Alex B. Haynes et al. — [*A Surgical Safety Checklist to Reduce Morbidity and Mortality in a Global Population*](https://doi.org/10.1056/NEJMsa0810119). New England Journal of Medicine, 2009.
- David R. Urbach et al. — [*Introduction of Surgical Safety Checklists in Ontario, Canada*](https://doi.org/10.1056/NEJMsa1308261). New England Journal of Medicine, 2014.
- Karl E. Weick, Kathleen M. Sutcliffe — [*Managing the Unexpected*, 3rd ed.](https://www.wiley.com/en-us/Managing+the+Unexpected%3A+Sustained+Performance+in+a+Complex+World%2C+3rd+Edition-p-9781118862414). Wiley, 2015.
- Kyle Petroski, Matthew Frail — [*How we prepare Shopify for BFCM*](https://shopify.engineering/bfcm-readiness-2025). Shopify Engineering, 2025 — free online.
- Argo Project — [*Sync Windows*](https://argo-cd.readthedocs.io/en/stable/user-guide/sync_windows/). Argo CD documentation — free online.

---

## Appendix: Encore at a Glance {#encore-glance}

Each chapter introduces the parts of Encore it needs when it needs them, which suits a reader going front to back but not one who starts at Chapter 9. This glossary gathers the whole company on one page. For each part it names where the Architecture book explains the design and which chapter here shows what it takes to run it.

| Term | What it is | Where to read more |
|---|---|---|
| **Encore** | Concert tickets across the EU, in euros, also sold as software as a service (SaaS) to venues; traffic rises 500× in minutes when a tour goes on sale, every seat is sold exactly once, and bots arrive ahead of the fans | [Architecture book, 1.1](https://oleksiyp.github.io/arch-book/#encore-our-running-example); Chapter 1 |
| **Organization** | 400 engineers in 40 stream-aligned teams that build and run their own services, and a platform group of 5–10% of engineering; on-call per team, with one incident commander rotation of trained engineers, most of them senior | [Architecture book, 5.5](https://oleksiyp.github.io/arch-book/#conways-law-is-a-design-tool); Chapters 12 and 15 |
| **Customers** | Fans, event organizers, partners on the public API at `api.encore.com`, and SaaS tenants | [Architecture book, 7.3](https://oleksiyp.github.io/arch-book/#the-gateway-earns-its-place-at-the-edge); Chapter 11 |
| **On-sale** | The scheduled moment a tour's tickets go on sale, usually 10:00 CET on a Friday | [Architecture book, 1.1](https://oleksiyp.github.io/arch-book/#encore-our-running-example); Chapter 6 |
| **Sale Gate** | On-Sale Admission: the virtual waiting room and admission controller in front of the purchase path; a serverless edge, pre-warmed, scaling to 400 instances | [Architecture book, 2.4](https://oleksiyp.github.io/arch-book/#24-choosing-a-style); Chapter 9 |
| **Admission rate** | Fans per second per event the Gate lets through, about 1,200, sized to keep Seat Inventory below 80% load | [Architecture book, 4.5](https://oleksiyp.github.io/arch-book/#45-degradation-and-chaos); Chapters 6 and 12 |
| **Bot Screening** | Decides whether each session is a fan, from rented edge signals and velocity rules; risk data in its own cloud account | [Architecture book, 10.4](https://oleksiyp.github.io/arch-book/#blast-radius-is-a-design-variable); Chapter 11 |
| **Seat Inventory** | The core domain and sole authority on whether a seat is free; event-sourced with command–query responsibility segregation (CQRS) | [Architecture book, 3.1](https://oleksiyp.github.io/arch-book/#31-strategic-design), [6.2](https://oleksiyp.github.io/arch-book/#cqrs-two-models-one-truth); Chapter 6 |
| **Hold** | A seat reserved for one fan by `POST /holds` for 5 minutes, released automatically if checkout does not finish | [Architecture book, 3.2](https://oleksiyp.github.io/arch-book/#aggregates-consistency-has-a-size); Chapter 10 |
| **Shard and home region** | Four shards per large event by `event_id`, each with a fenced leader handling about 10,000 reads and 1,500 ordered writes a second; each event's writes pinned to one region | [Architecture book, 4.2](https://oleksiyp.github.io/arch-book/#42-state--replication-partitioning-consistency); Chapters 3 and 10 |
| **Orders & Payments saga** | The orchestrated purchase, each step paired with a compensation, within a 3 s checkout budget; if the primary PSP fails, new payments go to the secondary, and if both are degraded, verified fans' seats are held pending payment for up to 20 minutes; no ticket is issued without an authorized payment | [Architecture book, 5.2](https://oleksiyp.github.io/arch-book/#the-saga-transactions-without-the-transaction); Chapters 4 and 9 |
| **PSP** | External payment service provider; Encore integrates two, routing each new payment to a healthy one, behind an anti-corruption layer; about 800 ms of the budget; Encore holds no card numbers | [Architecture book, 4.4](https://oleksiyp.github.io/arch-book/#anatomy-of-a-self-inflicted-outage); Chapters 2 and 9 |
| **The first big outage** | The PSP slowed from 200 ms to 8 s, a retry storm followed and autoscaling made it worse; fixed with retry budgets and a single retry layer | [Architecture book, 4.4](https://oleksiyp.github.io/arch-book/#anatomy-of-a-self-inflicted-outage); Chapter 2 |
| **Finance ledger** | The relational record of money, fed by `SaleCompleted`, reconciled daily and closed nightly | [Architecture book, 9.1](https://oleksiyp.github.io/arch-book/#91-data-ownership-in-distributed-systems); Chapter 10 |
| **Seat-map geometry** | The shape of a hall, served by Catalog from a cache; availability is never cached | [Architecture book, 1.3](https://oleksiyp.github.io/arch-book/#13-modularity-and-logical-components); Chapters 6 and 13 |
| **Notifications** | Delivers tickets by email and to phone wallets; rebuilt overnight by a coding agent in the scene that opens Chapter 1 | [Architecture book, 15.4](https://oleksiyp.github.io/arch-book/#the-inversion-the-preface-promised); Chapters 1 and 8 |
| **`ticket-sales.v2`** | The event stream carrying `SeatSold`, `TicketIssued`, `SaleCompleted` and related events to every consumer | [Architecture book, 6.5](https://oleksiyp.github.io/arch-book/#65-flow--streams-as-products); Chapter 5 |
| **Tenants and cells** | Venues using Encore as a service: one Enterprise silo (`venue-chain-a`), Professional tenants in Kubernetes cells with a database per tenant, about 500 self-service venues pooled in serverless cells of about 50 | [Architecture book, 14.1](https://oleksiyp.github.io/arch-book/#two-planes-three-models); Chapters 7 and 9 |
| **Regions** | EU-1 and EU-2: reads served from both, writes in each event's home region, each seat-ledger shard a five-member consensus group, two replicas in each region and a witness in EU-3, committing on a majority (RPO zero, RTO of minutes) | [Architecture book, 11.5](https://oleksiyp.github.io/arch-book/#surviving-a-region); Chapter 10 |
| **Golden path** | The platform's supported route from template to production, with provisioning, registry entry and scorecard | [Architecture book, 15.2](https://oleksiyp.github.io/arch-book/#golden-paths-on-a-self-service-control-plane); Chapter 7 |
| **Curtain-up** | The self-service workflow that pre-warms the purchase path on an on-sale morning | [Architecture book, 11.1](https://oleksiyp.github.io/arch-book/#the-spectrum-priced-in-responsibility); Chapter 3 |
| **Readiness review and freeze** | The Wednesday review before a big on-sale, then a freeze on non-emergency purchase-path changes from two hours before it until it ends | [Architecture book, 11.3](https://oleksiyp.github.io/arch-book/#from-is-it-up-to-why-is-it-weird); Chapters 8 and 13 |
| **Reliability team** | Ten engineers in the platform group, led by a staff SRE, who own SLO tooling, the incident process, readiness reviews and game days | [Architecture book, 15.1](https://oleksiyp.github.io/arch-book/#cognitive-load-is-the-resource-being-architected); Chapter 15 |
| **Published numbers** | Seat map ≤ 800 ms for 99.9% of requests over 28 days; tenant SLOs 99.9% self-service and 99.95% Professional; blended cost per ticket drifted from €0.11 to €0.19 and is now about €0.16, of which about €0.12 is variable | [Architecture book, 11.3](https://oleksiyp.github.io/arch-book/#from-is-it-up-to-why-is-it-weird); Chapters 4 and 6 |
| **Cue** | The operations agent on the internal Model Context Protocol (MCP) server: read-only by default, it may invoke only actions in a platform-enforced catalog, each with a five-minute token scoped to that action, and all but two (raising Catalog's autoscaler floor, holding a node in the upgrade reconciler) need a person's approval; the on-sale freeze withdraws its purchase-path write scopes | [Architecture book, 12.3](https://oleksiyp.github.io/arch-book/#the-loop-that-acts); Chapters 3 and 12 |
| **AI gateway** | Routes the assistant's and agent's model calls, about 80% to a model costing a tenth as much | [Architecture book, 12.1](https://oleksiyp.github.io/arch-book/#121-ai-in-the-system-topology); Chapter 14 |
| **Support assistant and refund agent** | A retrieval-augmented assistant for fans, and an agent that approves refunds under €80 with more than 48 h to showtime and sends everything else to a person | [Architecture book, 12.1](https://oleksiyp.github.io/arch-book/#121-ai-in-the-system-topology); Chapter 14 |
| **The Vesper Hale on-sale** | A fictional artist's 12-date European tour, about 1.1 million fans in the Gate, 47 minutes of degraded checkout and no seat sold twice | Chapters 12 and 13 |

*Figure A.1 — Encore at a glance. The Architecture book explains why each part was designed as it was; the named chapter shows what it takes to run.*
