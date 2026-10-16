# Running Production Systems in the AI & Cloud Era

*Reliability is something people and machines keep producing together.*

<small>© 2026 Oleksiy Pylypenko · Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) — share and adapt freely, non-commercially, with attribution. Source on [GitHub](https://github.com/oleksiyp/prodsys-book). Companion volume: [*Software Architecture in the AI & Cloud Era*](https://oleksiyp.github.io/arch-book/).</small>

## Preface

Every system worth building eventually leaves the hands of the people who designed it and enters a world they cannot fully foresee: real users, real traffic, real failures, at three in the morning and on the busiest day of the year. We call that world *production*, and for most of our field's history we treated it as the place where software went after the interesting work was done. The engineers wrote the code and somebody else kept it running. That division never served anyone well, and in the last fifteen years it has quietly dissolved. Cloud runtimes, service level objectives, observability, infrastructure as code, progressive delivery, chaos engineering, blameless reviews and, most recently, AI assistants that read our telemetry and write our changes have remade the practice of running software almost completely. The craft has changed far more than its reputation has.

The problems beneath the craft have not changed at all. A system of many interacting parts still fails in ways no single part explains. Automation still removes the easy work and leaves people with the hard work, at the moment they are least prepared for it. Queues still grow without bound as utilization approaches one, and organizations still drift, one reasonable exception at a time, toward the edge of what they can safely do. These are old lessons, learned at great cost in telephone exchanges, nuclear plants, cockpits and launch pads long before anyone ran a Kubernetes cluster. I have come to believe that the newest techniques are best understood, and best used, by someone who knows the older lessons that explain why they work.

This book is written for that reader: an engineer who builds services and now runs them, a team lead who has inherited an on-call rotation, an architect who wants the systems they design to survive contact with the world. It teaches today's techniques, the ones a team should actually use in 2026, and it roots each one in its lineage: safety science, control theory, queueing, and the ironies of automation. AI appears where it really changes the practice, and nowhere else. The tools will keep changing. The judgment they require will not.

It is the operational companion to *Software Architecture in the AI & Cloud Era*, and it continues that book's story. Reading one does not require the other, but the two were written to be read together. The first asks how we should shape a system; this one asks how we keep it alive.

### Influences & Attribution

Much of this book's method comes from others, and each chapter's references point to the original works, which are always the better read. The practice of site reliability engineering follows Google's *Site Reliability Engineering* and *The Site Reliability Workbook*, along with Alex Hidalgo's *Implementing Service Level Objectives*. Observability draws on Charity Majors, Liz Fong-Jones and George Miranda's *Observability Engineering*. Stability patterns come from Michael Nygard's *Release It!*, delivery from Jez Humble and David Farley's *Continuous Delivery* and the DORA research of Nicole Forsgren and colleagues, and performance from Brendan Gregg and Neil Gunther. Chaos engineering follows Casey Rosenthal and Nora Jones, and evaluation of AI systems follows Shreya Shankar, Hamel Husain and Chip Huyen.

The book's intellectual foundation is older. Charles Perrow, James Reason, Jens Rasmussen, Richard Cook, David Woods, Erik Hollnagel, Sidney Dekker, Nancy Leveson, Diane Vaughan and Lisanne Bainbridge studied how complex systems fail and how people keep them working. Their work, written for aviation, medicine, nuclear power and spaceflight, turns out to describe software operations with uncomfortable accuracy.

Several terms used here as common vocabulary have specific coiners: toil and error budgets (Google SRE), the USE method (Brendan Gregg), the RED method (Tom Wilkie), the Universal Scalability Law (Neil Gunther), normalization of deviance (Diane Vaughan), Safety-I and Safety-II (Erik Hollnagel), STAMP, STPA and CAST (Nancy Leveson), chaos engineering (Netflix) and the Swiss cheese model (James Reason).

### Authorship & Disclaimer

Written and directed by Oleksiy Pylypenko, with AI assistance (Anthropic's Claude). The judgment in it comes from twenty-plus years of practice: platform engineering inside a large bank, API architecture in fintech, and a decade of maintaining a widely used open-source library. The author chose the thesis, the structure, the examples and the trade-offs, edited every chapter, and takes responsibility for every claim, errors included. Encore and every kata company are fictional; historical events are described from the public record. The content is provided as-is, without warranty of any kind: educational material, not professional advice for any specific system. The license's full disclaimer of warranties applies.

## How to Read This Book

One company runs through all 15 chapters: **Encore**, which sells tickets to live concerts, and whose traffic can rise 500× in minutes when a major tour is announced. Readers of the companion volume watched Encore grow from nine engineers to 400. This book meets it the morning after that story ended and asks a different question: now that the system exists, who keeps it running, and how? Chapter 1 summarizes everything a new reader needs to know about Encore. One incident, the on-sale for a fictional artist named Vesper Hale, runs through the book. It is foreshadowed early, fought live in Chapter 12 and learned from in Chapter 13.

Each chapter closes with a **kata**: a practice brief for a different company, with its own scale and constraints, and a rubric to check your work against. As with a musician's scales, the value lies in repetition where mistakes are cheap, which is exactly what production never offers. Every section ends with a recap and a short exercise, best done against a system you run. Each chapter's references list the field's standard works; those marked *free online* cost nothing.

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

**The destination (Chapters 14–15):** operating AI workloads, and the organization that runs production, where the capstone awaits.
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

---

## Chapter 1: What Production Is — Running Software in the Cloud Era {#ch1}

> Code is finished when it ships. Production never is.

On the morning after Encore's new Notification service went live, nothing happened, and that was the first thing worth noticing. Overnight a coding agent had rebuilt the service on a new framework, with better retry semantics and 40 files that no person had typed or read in full. The contract tests passed, the boundary rules passed, the security checks passed, and the canary, judged against its service level objective (SLO), promoted the new version without complaint. By breakfast the service had delivered about 180,000 tickets to fans' phone wallets and email inboxes, and every dashboard was green.

One engineer had nonetheless spent 20 minutes on that change before it merged, reading not the code but the behavior it promised, and had found that the new retry semantics could, under the wrong timing, send a fan the same ticket twice. Nothing in the automated checks would have noticed, because a duplicate ticket is a perfectly healthy delivery, twice. She added a specification-level idempotency test, and the change went out. So the green dashboards raise the question this book exists to answer, and it is older than it looks. Who runs code that nobody fully read, and what do they need from it at 3 a.m.?

The honest answer is that people have always run code they did not write. How to run software well without understanding all of it is the founding question of our discipline, and this chapter traces how it was answered, from the machine-room operators of the 1950s to the first site reliability engineering (SRE) team at Google in 2003, before setting out what users actually feel of production, the stack of practices we use to run it, and the principles that make a system operable by strangers.

Encore is our companion again. For readers new to it, Figure 1.1 is the briefing a new engineer would get on their first day.

| Aspect | Where Encore stands |
|---|---|
| **Business** | Concert tickets across the EU, in euros; also sold as software as a service (SaaS) to venues. |
| **Defining problem** | Traffic rises 500× in minutes when a tour is announced; every seat sold exactly once; the bots arrive before the fans do. |
| **Organization** | 400 engineers in 40 teams that build and run their own services. A platform group (5–10% of engineering) includes a ten-person **Reliability team**: SLO tooling, incident process, on-sale readiness, game days. |
| **Customers** | Fans, event organizers, partners on `api.encore.com`, and SaaS tenants: one Enterprise silo, Professional tenants in Kubernetes cells, about 500 self-service venues in serverless cells. |
| **Purchase path** | Sale Gate (waiting room, at most about 1,200 fans/s per event) → Bot Screening → Seat Inventory (event-sourced, four shards per large event, 5-minute holds) → Orders & Payments (a saga, 3 s checkout budget, about 800 ms of it at the payment provider) → Notifications (wallet and email). |
| **Runtime** | Containers on Kubernetes, serverless where traffic is spiky, infrastructure as code with GitOps, reads active–active across two EU regions, each event's writes pinned to a home region. |
| **Published numbers** | Seat map: ≤ 800 ms for 99.9% of requests over 28 days. Tenant SLOs: 99.9% self-service, 99.95% Professional. Cost per ticket drifted from €0.11 to €0.19, was investigated, and is now about €0.12. |
| **AI already in production** | Demand forecasting, a support assistant, a refund agent (auto-approves under €80 with more than 48 h to showtime), an AI gateway, an internal tool server. |
| **Scars** | The first big outage: a payment provider slowed from 200 ms to 8 s, retries stormed, autoscaling made it worse. Fixed with retry budgets and a single retry layer. |
| **Rhythm** | Big on-sales at 10:00 Central European Time (CET) on Fridays, a readiness review the Wednesday before, and a change freeze on the purchase path from two hours before an on-sale until it ends. |

*Figure 1.1 — Encore so far. Everything in this table was earned by an earlier decision, and most of it by an earlier failure.*

### 1.1 Production as a Sociotechnical System

#### What we mean by production {#what-we-mean-by-production}

The word *production* comes to us from manufacturing, where it names the floor on which the real goods are made, as distinct from the laboratory where they are designed. In software it has come to mean something more specific. **Production** is the environment in which software serves real users with real consequences, where a mistake costs money, trust or someone's evening, and where nothing can be undone merely by closing a laptop. Staging, test and the developer's machine are all rehearsals; production is the performance.

The theatre analogy teaches something the manufacturing one does not. A play is not its script. The script is written once, but the production is made again every night, by actors, stage managers and riggers who adjust to a cold house, a missed cue, a prop gone missing, and a good stage manager keeps a show running through a dozen small failures the audience never sees. A bad script cannot be saved by any crew, but the evening's success is made by people working with it in real time. The code is the script; production is the performance, and no two nights are the same.

The analogy breaks at scale. A theatre crew can see the whole stage; Encore runs thousands of copies of its services for an audience of millions it never sees, and no one person can hold the stage in view. That gap between what is happening and what anyone can perceive is where most of this book's techniques live.

#### People and machines, jointly {#people-and-machines-jointly}

The term *sociotechnical system* is older than software operations. It comes from the Tavistock Institute in London, where Eric Trist and Ken Bamforth, studying British coal mines in 1951, found that a new and technically superior mining method had made the mines worse. The longwall method reorganized the work around the machinery and broke apart the small, self-managing teams that had made the old method safe and productive. Their conclusion, which has had to be relearned in every industry since, was that the social and the technical parts of a work system cannot be optimized separately: improve one in isolation and you may degrade the whole.

A **sociotechnical system**, then, is one whose behavior is produced jointly by its people and its technology, so that neither can be understood or improved without the other. Production is such a system. Its reliability is not a property of the code, any more than a ship's safety is a property of its hull. Reliability is produced continuously, through people knowing what the system is doing, changing it carefully, withstanding what goes wrong, responding when it does and learning afterwards. Those five verbs are the structure of this book.

The Notification rewrite shows what this means. As a technical artifact, the new service was better than the old one. As part of a sociotechnical system it was briefly worse, because its operators understood less of it than of the code it replaced. The engineer's 20 minutes restored some of that understanding, and her test made it durable, moving a piece of human knowledge into a check that would outlast her attention. That move, from what a person knows to what the system enforces, is the oldest move in operations.

In the companion volume's language, Encore's 500× spike is essential complexity, which no design removes. The gap between what a system does and what its operators can perceive is usually accidental, a product of how we built, instrumented and staffed it, and much of operations is its patient removal.

**Recap.** Production is where software meets real consequences, and it is made fresh every day, like a performance rather than a printed page. It is a sociotechnical system: its reliability is produced jointly by people and machines, and improving either in isolation can harm the whole. Much operational work consists of closing the gap between what the system does and what its people can perceive.

**Exercise 1.1.** Take a service you know and list the last five times a person, not an automated check, prevented or shortened a problem with it. For each, ask whether that person's knowledge now lives in a test, an alert or a runbook, or still only in their head.

### 1.2 From Operators to SRE — A Short History of Running Software

#### The machine room {#the-machine-room}

In September 1947 someone working on the Harvard Mark II taped a moth into the machine's logbook, beside the note "First actual case of bug being found." The joke is famous; the logbook is the more instructive object. From the beginning, running a computer meant keeping a record of what it did and what went wrong, and the incident timelines of Chapter 12 are its descendants.

Through the 1950s and 1960s, as machines like the IBM 704 and later the System/360 spread through universities, banks and government, **computer operator** became a job title with its own shifts, skills and career. Most installations ran as a *closed shop*: programmers handed their card decks across a counter and came back hours later for the printout. Behind the counter, operators mounted tapes when the console asked for them, loaded decks in sequence, watched the lights and the console typewriter, and restarted failed jobs according to instructions the programmers had left, often in a binder called a run book (Chapter 3 follows its descendants).

The operator's position is exactly that of Encore's on-call engineer on the morning after the rewrite. Operators ran programs they had not written and could not usefully read. What made that workable was a contract: the program declared what it needed, the run book said what to do when it stopped, and the operator's judgment covered the cases in between. It failed in familiar ways. Instructions went stale, programmers wrote for the happy path, and the operator at 3 a.m. improvised with a machine whose authors were asleep.

#### Automating the operator {#automating-the-operator}

Much of the history of computing can be read as the operator's work being absorbed into software. In 1956 General Motors Research and North American Aviation wrote GM-NAA I/O for the IBM 704, one of the first operating systems, chiefly to reduce the idle time between jobs that operators spent setting up the machine by hand. Job control languages, spooling and time-sharing absorbed more of the role, until by the 1980s the work had moved to a new figure, the **system administrator**, who tended fleets of smaller machines, mostly Unix, through scripts and configuration files, and who in time built a profession with its own conferences and textbooks.

Aviation went through a parallel change. Large airliners once carried a flight engineer, a third crew member whose panel managed the engines, fuel, hydraulics and electrics. From the early 1980s new airliners were certified for two pilots, and that panel was folded into automation. The role did not vanish so much as dissolve into the design of the aircraft and the training of the pilots, and operations in computing dissolved in the same way, into operating systems, scripts and eventually the code itself. The analogy breaks on one point: an airliner is designed once and certified, whereas software changes every day, so what the automation must absorb keeps moving.

Every era of operations has been an attempt to move what the operator knew into something that does not get tired. And every era left a residue the automation could not absorb, which was the judgment needed when things went wrong in a way nobody had written down.

#### The wall, and two ways over it {#the-wall-and-two-ways-over-it}

As software moved onto the web, a structural problem hardened. Developers were rewarded for change and operations staff for stability, and the two sat on opposite sides of a wall over which releases were thrown. Frameworks such as the IT Infrastructure Library (ITIL), which the UK government began publishing in the late 1980s, brought discipline to change management, but often also institutionalized the wall, with change advisory boards approving work they could not evaluate.

Two answers emerged. In 2003 Benjamin Treynor (now Ben Treynor Sloss) joined Google and was put in charge of a production team of seven engineers. He staffed it, and the organization that grew from it, with software engineers who treated operations as a software problem: automate the repetitive work, cap the manual share of each engineer's time, and govern the trade between change and stability with measurements rather than seniority. In Google's *Site Reliability Engineering* (2016) he put it in a line quoted ever since: "SRE is what happens when you ask a software engineer to design an operations team." The other answer came from web companies that could not afford a large operations staff. In 2009 John Allspaw and Paul Hammond described Flickr's practice of deploying more than 10 times a day, through cooperation between developers and operations, and later that year Patrick Debois organized the first DevOpsDays in Ghent. Where SRE built a new kind of operations team, DevOps tried to take down the wall, and Amazon's "you build it, you run it", which the companion volume discussed, pushed the pager all the way to the team that wrote the code.

Encore has inherited all three answers: stream-aligned teams run their own services, a small Reliability team works in the SRE tradition, and the incident commander rotation borrows senior engineers from everywhere. The forms are new; the question is the closed shop's. How do people safely run software whose authors are not in the room? With a coding agent as author, the author may not be anywhere at all, which sharpens the old question without making it new. Figure 1.2 sets the whole lineage on one line.

{% include diagrams/fig-1-2.svg %}

*Figure 1.2 — Who has stood between the code and its users, from the 1947 logbook to today. Each era absorbed the last one's routine work into software; notice that the question at the counter never changed, only who stands behind it.*

**Recap.** Operators have always run code they did not write, and the job has always relied on a contract between authors and operators plus judgment for the unwritten cases. Each era moved the operator's knowledge into automation, and each left a residue of judgment behind. SRE and DevOps are two answers to the wall between change and stability, and modern organizations usually combine them.

**Exercise 1.2.** Draw your organization's equivalent of the closed shop's counter: the point where code passes from those who wrote it to those who run it. Who is on each side, what crosses it with the code, and what is lost in the crossing?

### 1.3 Reliability, Availability, and What Users Actually Feel

#### Definitions worth quoting {#definitions-worth-quoting}

The reliability engineers of the 1950s, working on military electronics that failed at alarming rates, gave us a definition that has held up well: **reliability** is the probability that a system performs its intended function, under stated conditions, for a stated period. Every part of that sentence does work. *Intended function* means that a system can be running and still be failing; *stated conditions* means that reliability on a quiet Tuesday says nothing about reliability during an on-sale; *stated period* means that reliability is always measured over a window, never at an instant.

**Availability** is narrower: the fraction of time, or of requests, for which the system is able to serve. The classical formula divides the mean time between failures by the sum of that and the mean time to repair, and its arithmetic carries a lesson: availability rises either by failing less often or by recovering faster, and for most modern systems the second is far cheaper. Figure 1.3 draws the arithmetic.

{% include diagrams/fig-1-3.svg %}

*Figure 1.3 — Availability as mean time between failures over the sum of that and mean time to repair, with lines of equal availability. Halving the time to recover buys exactly what doubling the time between failures buys, and it is usually far easier to get.* Chapter 4 turns availability into targets and budgets.

A third property, often left out of such lists, matters most to Encore. **Correctness** is the property that the system's answers are right: that a seat sold is sold once, that a charged fan receives a ticket, and that a ticket is delivered once. Availability measures whether the system answered; users judge what it said. The duplicate ticket the rewrite nearly shipped would have appeared nowhere in availability; the dashboard would have been greenest just as fans found two copies of one seat in their wallets.

#### Vital signs and the patient {#vital-signs-and-the-patient}

Medicine offers the right analogy for what operators usually measure. A hospital monitors pulse, temperature and blood pressure because they are cheap, continuous and correlated with health, yet clinicians know that a patient can have normal vital signs and be seriously unwell, and that the patient's own account is evidence too. Health checks, CPU graphs and pod counts are a system's vital signs: necessary, and not the patient. What the fan feels in the queue, at the seat map and at checkout is the patient's account, and the gap between the two is where most surprising outages hide. The analogy breaks in our favor, since software can be instrumented to report its users' experience directly, at the edge of their journey, as Chapter 5 shows.

| What the system reports | What the fan feels |
|---|---|
| All Seat Inventory pods healthy | "Seat unavailable" on every seat I click, because one shard is mid-failover |
| Payment API 99.95% available | My card was charged and the page spun until it timed out |
| Notification delivery success 100% | I got my ticket twice and don't know which one is valid |
| Sale Gate p99 latency 40 ms | I have been in the queue 25 minutes and the position hasn't moved |
| Bot Screening blocked 2% of sessions | I am a real fan and I was told I am a robot |

*Figure 1.4 — Vital signs against the patient's account. Each left-hand statement can be true while the right-hand one is also true.*

Two features of user experience shape the rest of the book. Failure is usually partial: some fans on some shard see errors while the rest proceed, so the useful questions are "for whom?" and "how many?" And users feel their own latency, never the median, so in a purchase touching a dozen services someone will meet the slow tail of nearly every one, as the companion volume's tail-at-scale argument showed.

Reliability, finally, is a promise made to people who cannot see inside the system. A fan who has queued 25 minutes for a sold-out show cannot know whether the error was a failover, a bug or a bot rule. They know only whether Encore kept its word.

**Recap.** Reliability is the probability of doing the intended job under stated conditions over a stated period; availability is narrower, and correctness is a third property that availability cannot see. Operational vital signs are necessary but are not the user's experience. Failure is partial and felt individually, so the useful questions are always for whom, how many and how slowly.

**Exercise 1.3.** For one user journey you own, write five rows of Figure 1.4: a metric your dashboards show, beside a user experience that could coexist with it. Which of the right-hand column could you detect today, and how?

### 1.4 The Modern Production Stack

#### Layers, and why we need them {#layers-and-why-we-need-them}

A touring concert production is organized in layers. Riggers hang the structure, a power crew brings in electricity, the sound and lighting desks run their systems, and the stage manager calls the cues. Each layer has its own specialists, tools and failure modes, each depends on the ones beneath it, and the show is what they produce together on the night.

The modern production stack is organized the same way, for the same reason. Hierarchy is how we master a whole too complex to hold at once: each layer hides detail from the ones above and offers them a simpler surface to rely on. Figure 1.5 names each layer by the question it answers and maps it to Encore and to the chapter that treats it, which makes it a reading map for the book.

At the bottom sits the **runtime and its control plane**: clusters, functions and managed services, declared as code and continuously reconciled toward that declaration. Above it, **delivery** carries change into production through pipelines, canaries and flags. **Telemetry** reports what the system is doing, and **SLOs** judge whether that is good enough for users and turn the judgment into decisions about risk. The **incident process** takes over when users are hurting now, and **learning** decides what changes afterwards. Alongside them all runs the **platform**, which packages the lower layers into paved paths so that 40 teams need not each rebuild them.

| Layer | The question it answers | Encore today | Chapter |
|---|---|---|---|
| Safety foundations | Why do complex systems fail, and what role do people play? | The first outage, re-read | 2, 3 |
| SLOs and error budgets | Is it good enough for users? | Seat-map and tenant SLOs | 4 |
| Telemetry and observability | What is it doing, and why? | Traces across Gate, Inventory, Orders, payment provider | 5 |
| Capacity and cost | Will it hold, and at what price? | 1,200 fans/s, four shards, cost per ticket | 6 |
| Runtime and control plane | Where does it run, and what keeps it there? | Kubernetes cells, serverless Gate, GitOps | 7 |
| Delivery | How does change arrive safely? | Canaries, flags, the on-sale freeze | 8 |
| Resilience | What happens when parts fail? | Retry budgets, load shedding, cells | 9 |
| Data and recovery | What is lost, and how fast do we return? | A seat ledger that may lose nothing, restore drills | 10 |
| Security operations | Who else is acting on the system? | Bots, leaked keys, signed artifacts | 11 |
| Incident response | What do we do while users hurt? | Incident commander rotation | 12 |
| Learning from incidents | What do we change afterwards? | Postmortems that change the system | 13 |
| AI workloads | How do we run components that don't repeat themselves? | Support assistant, refund agent, AI gateway | 14 |
| Platform and organization | Who owns what, and how do teams get it for free? | Golden paths, the Reliability team | 7, 15 |

*Figure 1.5 — The production stack as Encore runs it, and where this book treats each layer. Read top to bottom for the book's order; read it against your own system to find the layer you have been neglecting.*

#### What the stack hides, and what it cannot {#what-the-stack-hides}

Layers help only while their surfaces hold, and production is where they do not. A node drain in the runtime shows up as a latency spike in telemetry, an SLO burn, a page, an incident and, if we are diligent, a change to delivery; the whole stack takes part in one bad minute. Here the touring analogy breaks: a tour hires one stage manager to call every cue, whereas a cloud system's cues are called by hundreds of control loops, many automated and none aware of all the others. The stack organizes knowledge and ownership but offers no single vantage point, and the incident process exists partly to assemble one when it is needed. Figure 1.6 follows one such minute through the stack.

{% include diagrams/fig-1-6.svg %}

*Figure 1.6 — One node drain, as each layer of the stack sees it. Every layer holds a piece of the event and none holds all of it, which is why an incident needs someone to assemble the whole.*

Seen from the morning after the Notification rewrite, not one layer required the on-call engineer to have read the 40 files. The runtime would restart the service if it crashed, delivery could roll it back, telemetry would show its behavior, and the SLO would say whether that behavior was acceptable. What the stack could not do was tell anyone whether "acceptable" had been defined correctly, which is why the missing check was a specification of behavior, written by a person who understood what a ticket is for.

**Recap.** The production stack is a hierarchy of layers, each answering one question and hiding detail from the layers above. Figure 1.5 is the book's map. The layers organize knowledge and ownership but give no single vantage point, and in an incident the whole stack takes part at once.

**Exercise 1.4.** Fill in Figure 1.5's "Encore today" column for your own system. Mark each row as strong, adequate or missing, and pick the weakest row that sits on your most important user journey.

### 1.5 Principles for Operable Systems

#### A definition, and a stranger {#a-definition-and-a-stranger}

If the history in Section 1.2 has a single lesson, it is that operators have never been able to rely on understanding everything they run. They have relied on systems that were designed to be run. **Operability** is the degree to which a system can be understood, controlled and repaired in production by people who did not build it, under time pressure and with partial knowledge. The final clause is the one that matters. Every engineer who wrote the code will one day be asleep, on holiday or working somewhere else, and with coding agents in the loop the author may never have been a person at all. An operable system is one that can be run by people who did not write it, which in time means everybody.

James Hamilton's 2007 paper on designing and deploying internet-scale services reads in large part as a list of courtesies a service should extend to its operators, and Nygard's *Release It!* made the same case by cataloguing what happens to systems designed only to pass their tests. Five principles distill the tradition, and they apply equally to code written by people and by agents.

**Legible.** The system tells us what it is doing, in terms of its users' experience, without anyone reading its source. Encore's new Notification service emits a delivery record per ticket with the order and attempt number, so a duplicate that escaped would show up within minutes rather than through a fan's complaint.

**Steerable.** The system offers controls that operators can turn safely and quickly while it runs: admission rates, feature flags, drains, load-shedding thresholds. The Sale Gate's admission rate is the canonical example, one number that trades fans' waiting time against the load reaching Seat Inventory.

**Bounded.** When the system fails, the damage stays inside a known perimeter: a cell, a shard, a tenant, a slice of traffic. The companion volume drew these boundaries for architectural reasons; operationally, they make a bad change survivable.

**Reversible.** Every change can be undone faster than it can do serious harm, and the irreversible ones, mostly changes to data, are identified in advance. The canary that promoted the Notification rewrite was safe only because the previous version could be restored in minutes.

**Rehearsed.** Recovery paths that have never been exercised are untested. Failovers, restores and rollbacks become dependable only through practice, and a team that has not rolled back in six months may find it cannot.

#### Ownership, which holds the principles together {#ownership-holds-them-together}

These five are properties of the system; the tradition insists on a sixth, a property of the organization. Every production system needs an **owner**, a named team that answers its pages, keeps its runbooks current and decides when its risks are acceptable. The Notification service's owner, the Fan Messaging team, woke that morning owning code it had not written, the operator's oldest position. What made that tolerable was not heroic code review but a service that was legible, steerable, bounded, reversible and rehearsed, and one person's 20 minutes spent making sure its most important behavior was specified.

I have come to believe that this is the right answer to the question with which the chapter began. We cannot read everything we run, and we never could. What we can do is insist that whatever we run, whoever or whatever wrote it, comes with the courtesies that let a stranger operate it at 3 a.m., and that someone is accountable for it when the stranger is us. Operability is the contract between a system and the people who will run it, and like every contract it is worth exactly as much as its enforcement.

**Recap.** Operability is the degree to which strangers can understand, control and repair a system under pressure. Five principles describe it (legible, steerable, bounded, reversible and rehearsed) and ownership holds them together. They apply to code written by agents exactly as they apply to code written by people.

**Exercise 1.5.** Score a service you own from one to five on each of the five principles. For the lowest score, describe the specific 3 a.m. situation in which it would hurt, and the smallest change that would raise it by one point.

### Kata: The Night Ferry

> **Your brief: "Tideway."** A ferry operator's booking platform: 14 routes between islands and the mainland, about 9,000 bookings on a normal day. When storms cancel crossings, rebooking traffic jumps 40× within an hour, and island residents with hospital appointments cannot afford to be stranded. Tideway has 22 developers in four teams and a three-person infrastructure team that receives releases on Thursday evenings and holds the only pager. Half of last quarter's code came from a contractor's coding agent; the contract ended in September. Outages are reported by port staff phoning the office. The board's request: "fewer surprises, without slowing down."

**Deliverables:**

1. **Sociotechnical map** — the people, teams, automated systems and external parties involved in a storm rebooking, with who knows what about each part.
2. **Operations history** — where Tideway sits in the lineage of Section 1.2, where its counter between authors and operators is, and what crosses it.
3. **User-felt reliability** — a Figure 1.4 table for storm rebooking, with at least two rows where availability looks healthy and residents are failed.
4. **Stack map** — a Figure 1.5 table for Tideway, rated strong, adequate or missing, with the three weakest layers chosen for investment.
5. **Operability review** — the five principles scored for the rebooking service, an owner named for the contractor's code, and a 90-day plan.

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

You can now describe production as a sociotechnical system, place your organization in the history of running software, separate what a dashboard reports from what a user feels, map the production stack, and judge operability whoever wrote the code. What you lack is an account of how such systems actually fail, which is rarely the way our dashboards expect. Chapter 2 turns to safety science, from Three Mile Island onward, for that account.

### References

- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Betsy Beyer, Chris Jones, Christof Leng, David Huska, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*, 2nd ed.](https://www.oreilly.com/library/view/site-reliability-engineering/9798341607675/). O'Reilly, 2026.
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan — [*The Practice of Cloud System Administration*](https://www.informit.com/store/practice-of-cloud-system-administration-devops-and-9780321943187). Addison-Wesley, 2014.
- Michael T. Nygard — [*Release It!*, 2nd ed.](https://pragprog.com/titles/mnee2/release-it-second-edition/). Pragmatic Bookshelf, 2018.
- David N. Blank-Edelman — [*Becoming SRE*](https://www.oreilly.com/library/view/becoming-sre/9781492090540/). O'Reilly, 2024.
- David N. Blank-Edelman (ed.) — [*Seeking SRE*](https://www.oreilly.com/library/view/seeking-sre/9781491978856/). O'Reilly, 2018.
- John Allspaw, Jesse Robbins (eds.) — [*Web Operations*](https://www.oreilly.com/library/view/web-operations/9781449377465/). O'Reilly, 2010.
- James Hamilton — [*On Designing and Deploying Internet-Scale Services*](https://www.usenix.org/legacy/event/lisa07/tech/full_papers/hamilton/hamilton.pdf). LISA '07, USENIX, 2007 — free online.
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne (eds.) — [*The Site Reliability Workbook*](https://sre.google/workbook/table-of-contents/). O'Reilly/Google, 2018 — free online.
- Thomas A. Limoncelli, Christina J. Hogan, Strata R. Chalup — [*The Practice of System and Network Administration*, 3rd ed.](https://www.oreilly.com/library/view/the-practice-of/9780133415087/). Addison-Wesley, 2016.
- Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren — [*The DevOps Handbook*, 2nd ed.](https://itrevolution.com/product/the-devops-handbook-second-edition/). IT Revolution, 2021.
- E. L. Trist, K. W. Bamforth — [*Some Social and Psychological Consequences of the Longwall Method of Coal-Getting*](https://doi.org/10.1177/001872675100400101). Human Relations, 1951.

---

## Chapter 2: How Complex Systems Fail — Safety Science for Software {#ch2}

> "Complex systems run in degraded mode." — Richard Cook

At four o'clock in the morning on 28 March 1979, the pumps feeding water to the steam generators of Unit 2 at Three Mile Island, near Harrisburg, Pennsylvania, stopped. What followed was the worst accident in the history of American commercial nuclear power, and nothing in it was exotic. A valve stuck. A light told the truth about the wrong thing. Conscientious operators did what their training and instruments told them, and in doing so starved the core of the water it needed. By the time anyone understood, about half the core had melted.

The accident is usually told as a story about operators who made mistakes. Charles Perrow, a sociologist of organizations, told it differently. In *Normal Accidents* (1984) he argued that Three Mile Island was a property of the kind of system it was: one whose parts interacted in ways nobody had anticipated, bound so tightly that there was no time to understand those interactions before they did harm. In such systems accidents are *normal*: rare, perhaps, but inevitable. That provocative word opened a line of thought running through Reason, Rasmussen, Cook, Dekker, Hollnagel, Woods and Leveson, and it is the intellectual foundation of this book.

This chapter asks why systems that are carefully built, well staffed and heavily defended still fail, and what the answer implies for the way we run them. Encore gives us two events to re-read: its oldest scar, the retry storm that followed a slow payment provider, and a failure that did not happen, the duplicate ticket one engineer caught in an agent-written change. Safety science will tell us that the second is as worth studying as the first.

### 2.1 Normal Accidents — Coupling and Interactive Complexity

#### What happened at Three Mile Island {#what-happened-at-three-mile-island}

The chain is worth following slowly, because every link in it was reasonable. When the feedwater stopped, the reactor's primary circuit heated and its pressure rose. A pilot-operated relief valve (PORV) on the pressurizer opened, as designed, and the reactor shut itself down, also as designed. Seconds later the valve was commanded to close. It did not close, and for more than two hours it vented the reactor's coolant into a drain tank.

The control room had a light for that valve, and the light went out. It reported, however, that the signal to close had been sent; it described the command and said nothing about the world. The valve had a history of weeping, so a high temperature on its discharge line looked like old news. The backup feedwater pumps had started, but two valves on their lines had been left shut after maintenance, and nobody noticed for about eight minutes. Amid over a hundred alarms, the operators watched the water level in the pressurizer rise. Their training said the worst thing a pressurizer could do was fill completely ("go solid"), so they throttled back the high-pressure injection, the emergency cooling that had started automatically to replace the escaping water. The level was rising because steam forming in the reactor was pushing water up. The core was uncovering while the instrument they trusted said it was flooding.

Notice what the story lacks: a villain, a single broken part, a step at which a reasonable person knowing only what the operators knew would obviously have acted otherwise. The presidential commission criticized training, procedures, control-room design and the regulator alike. Perrow explained why such a list was the right shape of answer.

#### Two dimensions of trouble {#two-dimensions-of-trouble}

Perrow described systems along two axes. In a system with **linear interactions**, parts affect each other in expected, visible sequences, like stations on an assembly line. A system has **interactive complexity** when its parts can interact in unplanned and often invisible ways, through shared components, feedback loops and indirect information, so that a failure in one place appears as a symptom somewhere else. A **tightly coupled** system has little slack: processes are fast, cannot be paused, follow a fixed sequence and have few substitutes for failed parts. A **loosely coupled** system has buffers, delays and alternative paths, and so tolerates a fault while people work out what is going on.

| | Linear interactions | Complex interactions |
|---|---|---|
| **Tight coupling** | Dam, power grid · a batch payment file with a bank cutoff | Nuclear plant, chemical plant · a synchronous service mesh under peak load |
| **Loose coupling** | Assembly line, post office · a nightly report job | University, research lab · an event-driven system with durable queues |

*Figure 2.1 — Perrow's interaction and coupling chart, with software analogues beside his examples. Normal accidents live in the top-right cell, where failures interact in ways nobody foresaw, faster than anyone can understand them.*

The top-right cell is where the trouble lies, because each property defeats the usual remedy for the other. Interactive complexity defeats prediction, so we rely on people to understand the unexpected interaction when it arrives; tight coupling defeats understanding in the moment, because the system moves faster than anyone can think. Perrow added an organizational corollary: complexity calls for decentralized control, coupling for centralized control, and a system with both demands the two at once.

His most uncomfortable observation concerned safety devices. Every alarm, interlock and redundant part adds interactions. At the Enrico Fermi 1 reactor near Detroit in 1966, a zirconium plate installed as a safety feature broke loose and blocked the coolant flow, causing a partial meltdown; at Three Mile Island the emergency cooling worked perfectly and was turned down by people misled by another instrument. Defenses are part of the system they defend, and they can fail into it.

#### Encore's retry storm, re-read {#encores-retry-storm-re-read}

Encore's first big outage, told in the companion volume, looks different through Perrow's eyes. The external payment service provider (PSP) slowed from 200 ms to 8 s. Each request held its connection 40 times longer, so connection pools ran dry; health checks sharing those pools began to fail; healthy instances were restarted, and the autoscaler, reading the failures as a need for capacity, added instances that opened still more connections to a provider that could not serve them. Retries at several layers multiplied the load on everything.

Every element there was a safety device. Health checks remove sick instances, autoscalers absorb load, retries ride out transient faults; each was sensible alone, and their interaction through shared pools appeared on no diagram, which is interactive complexity in its purest form. The purchase path was also tightly coupled to the PSP: a synchronous call, with no buffer between a fan's click and a bank's reply, inside a 3 s checkout budget. Accepting orders when the PSP is down and charging later was therefore not a bug fix. It moved the purchase path out of the top-right cell by loosening a coupling, buying time with a durable queue, while retry budgets and a single retry layer reduced the interactions. Neither made failure impossible, and neither was meant to.

What I take from Perrow is not his pessimism, which the high-reliability school later challenged with studies of aircraft carriers and air traffic control. It is his diagnostic: before asking who failed, ask which cell of the chart the system was in. A system in the top-right cell will surprise its operators, and our job is to design for the surprise.

**Recap.** Perrow's two dimensions, interactive complexity and tight coupling, explain why careful systems still fail: the first defeats prediction, the second defeats understanding in the moment. Safety devices add complexity and can cause the accidents they were meant to prevent. Loosening a coupling is often the most effective reliability work a team can do.

**Exercise 2.1.** Place five components of a system you run on Figure 2.1. For the one nearest the top-right cell, name one coupling you could loosen (a buffer, a timeout, an asynchronous step) and one safety device whose interaction with others you have never tested.

### 2.2 From Human Error to System Error — Reason, Rasmussen, Cook

#### The sharp end and the blunt end {#the-sharp-end-and-the-blunt-end}

For most of the twentieth century, accident investigation ended when it found a person, and "human error" was both the cause and, through retraining or discipline, the cure. James Reason, a psychologist at the University of Manchester, did more than anyone to take this account apart, beginning from inside it. *Human Error* (1990) classified how competent people err: **slips** and **lapses**, where a sound plan is badly executed or forgotten, and **mistakes**, where the plan itself is wrong. Violations form a separate category, and most are well-meant shortcuts rather than sabotage.

The book's most consequential chapter turned outward. Reason distinguished **active failures**, unsafe acts at the point of contact whose effects are felt almost at once, from **latent conditions**, weaknesses created far away in time and place by designers, managers, maintainers and budget holders, which lie dormant until some local circumstance wakes them. He called them resident pathogens: a body carries many, and illness arrives when enough of them meet a trigger. Woods, Cook and their colleagues made the two ends of this picture standard vocabulary. The **sharp end** is where practitioners touch the hazard: the control room, the on-call laptop. The **blunt end** is where the conditions of their work are set: budgets, schedules, tooling and policy. Operators are less the instigators of accidents than their inheritors.

In *Managing the Risks of Organizational Accidents* (1997) Reason gave the idea its famous picture: each defense is a slice of cheese with moving holes, and an accident happens when, briefly, they line up. The Swiss cheese model is a teaching image rather than a theory, and complex systems do not fail in neat lines through stationary slices. But it made the defenses themselves, and the organization that maintains them, the object of study. Figure 2.2 draws it for Encore's retry storm, which we re-read below.

{% include diagrams/fig-2-2.svg %}

*Figure 2.2 — Reason's Swiss cheese, with the retry storm's defenses as the slices. Each hole was a latent condition set far from the sharp end; notice that every slice was a safety device, and that no single hole was enough.*

#### Rasmussen's boundaries {#rasmussens-boundaries}

Jens Rasmussen, the Danish engineer on whose levels of performance Reason had built, went further in "Risk Management in a Dynamic Society" (1997). He pictured an organization's work as a point moving within a space bounded on three sides: economic failure, unacceptable workload, and the limit of functionally acceptable performance, beyond which accidents happen. Management pushes the point away from the economic boundary, toward efficiency; people, sensibly, push it away from the workload boundary, toward least effort. Both gradients point toward the safety boundary, and nothing in daily work shows where that boundary is. Rasmussen likened the point's movement to a particle's random drift, which wanders but, under steady pressure, travels. Figure 2.3 draws the space and a point drifting through it.

{% include diagrams/fig-2-3.svg %}

*Figure 2.3 — Rasmussen's migration toward the boundary of acceptable performance (after Rasmussen, 1997). Two sensible gradients push the same way; notice that the boundary people believe in is not the one that matters, and that the drift looks like noise until it arrives.*

This is the model to keep in mind for the rest of the book: safety is not a state a system reaches but a position it must keep holding against pressure. And the boundary is usually discovered only by crossing it.

#### Eighteen short theses {#eighteen-short-theses}

In 1998 Richard Cook, an anesthesiologist and safety researcher at the University of Chicago, wrote "How Complex Systems Fail", a few pages of numbered theses that engineering organizations have passed around more than any other text in this chapter. Complex systems are intrinsically hazardous and therefore heavily defended. They always contain flaws, too many to find and fix, and so they run degraded. Catastrophe needs several failures together, each insufficient alone, which is why the search for a single root cause is mistaken and reflects the social need for blame more than the mechanism of failure. Hindsight makes obvious a path that was invisible at the time. And practitioners play two roles at once, producing the system's output and defending it against failure. Safety, in Cook's account, is something people *do*, minute by minute.

The movement these three began is often called the New View, and its central claim fits in a sentence: **human error** is an attribution made after the fact, not a cause discovered in it. The useful question after an incident is not "who made the mistake?" but "why did it make sense to them at the time?" Woods and his co-authors call the answer the second story.

Read the retry storm this way and the cast changes. The engineers who configured retries at each layer were not careless; retries were recommended practice, nobody owned their sum, and nothing in review showed how they multiplied. The latent conditions were the shared pools, health checks that measured the wrong thing, and an autoscaler policy written for a different overload. Stop at a person, and the latent conditions survive to meet the next one.

**Recap.** Reason showed that operators inherit failures planted far from the sharp end, and that defenses have holes that move. Rasmussen showed that steady, sensible pressures push work toward a safety boundary nobody can see. Cook showed that complex systems always run degraded, that failure needs several contributors, and that people at the sharp end are creating safety all the time.

**Exercise 2.2.** Take your last incident review. List every contributing factor it named and mark each as sharp end or blunt end. If the blunt-end list is shorter, write the second story for the most prominent human action: why did it make sense at the time?

### 2.3 Drift and the Normalization of Deviance

#### How margins erode {#how-margins-erode}

Rasmussen's model describes a force; Sidney Dekker's *Drift into Failure* (2011) describes what that force looks like from inside an organization. **Drift** is the slow movement of a system toward failure through many small decisions, each locally reasonable and each judged acceptable by the standards of its day, so that no single step can be identified afterwards as the moment things went wrong. Drift is not negligence. It is what success looks like while it is quietly spending its margins.

Dekker's features of drift describe any busy engineering organization. Resources are scarce, so there is always a reason to go a little faster. Each change departs slightly from the last accepted practice, which becomes the next baseline. A review that has always approved becomes an occasion for reassurance rather than inquiry. And drift is rewarded: every time the thinner margin holds, it becomes evidence that the margin was never needed.

The sociologist Diane Vaughan named the mechanism the **normalization of deviance**: a departure from an expected standard, repeated without consequence, comes to be accepted as the standard itself. Her study of the Challenger launch decision is the home touchstone of Chapter 13, and we leave it there. Deviance is normalized by people who still care, examining evidence that keeps saying all is fine.

#### The pressure that does not show on a dashboard {#the-pressure-that-does-not-show}

A touring production offers a fair analogy. The load-in schedule is written with slack: four hours to rig, an hour to sound-check, time for a fault. On the first night the crew uses all of it. By the 30th night the rig goes up in three hours, so the production manager books an interview in the spare hour and the venue opens the doors earlier, each reasonably. Nobody removed the slack; it was spent, one good decision at a time, and the tour now depends on every night going as well as the last. The analogy breaks at one point, which is also its lesson: a touring crew sees its own clock. In software the margin being spent is usually invisible: headroom on a shard, slack in a retry budget, the distance between a freeze rule and what people actually do.

Encore's on-sale change freeze is worth watching. As written, it forbids non-emergency changes to the purchase path from two hours before an on-sale until it ends. As practiced, it has acquired texture. Exceptions are granted in chat by whichever senior engineer is around, usually for good reasons, and recorded nowhere else. Platform automation considered low-risk is excluded, which made sense when that automation did little; it does more now. Services beside the purchase path were never covered. Counting exception requests, the Reliability team found 3 in the first quarter of last year and 14 in the most recent quarter, and not one had led to an incident. That last fact is exactly what makes the trend worth attention. Chapter 8 examines the freeze as a delivery control and Chapter 13 returns to it with sharper questions.

What can be done about drift is modest but real. We can make margins visible, so that spending them is a decision rather than a side effect. We can treat a quiet period as weak evidence. And we can bring outsiders and dissenters into reviews, because people inside a practice are the last to see it change; Dekker's call for diversity of opinion is the one sensor that reliably detects drift.

**Recap.** Drift is the slow spending of safety margins through decisions that are each reasonable, and it is reinforced by success. Deviance is normalized by people examining evidence that keeps saying all is well. The defenses are to make margins visible, to distrust quiet periods, and to keep dissenting voices in the room.

**Exercise 2.3.** Pick one rule your team holds about production (a freeze, a review requirement, an alert threshold). Compare its written form with the last three months of practice. List the exceptions, who granted them and why, and decide whether the rule or the practice should change.

### 2.4 Safety-I, Safety-II, and Resilience Engineering

#### Studying what goes right {#studying-what-goes-right}

Everything so far has studied failure. Erik Hollnagel, a psychologist working in the tradition Rasmussen founded, argued that this is a strange way to understand a system that almost always works. In *Safety-I and Safety-II* (2014) he named the traditional view **Safety-I**: safety as the condition in which as few things as possible go wrong, achieved by finding and removing the causes of failure. Beside it he set **Safety-II**: safety as the ability to succeed under varying conditions, achieved by understanding how everyday work succeeds and supporting it.

| | Safety-I | Safety-II |
|---|---|---|
| Definition | As few things as possible go wrong | As many things as possible go right |
| What is studied | Failures, incidents, root causes | Everyday work, adaptations, near misses |
| Human variability | A hazard, to be constrained | A resource, the reason things work |
| Response | Find the cause, add a barrier | Understand the adaptation, support it |
| Encore example | The retry-storm postmortem | The duplicate-ticket catch |

*Figure 2.4 — Two views of safety. Safety-II complements Safety-I rather than replacing it; a team needs both the barrier and the understanding of why work usually succeeds without hitting it.*

Critics, Leveson among them, rightly note that few practitioners ever held the caricature of Safety-I; take the reframing and leave the polemic. It rests on one observation. The same **performance variability**, people adjusting what they do to fit the conditions they meet, is the source of both success and failure. Hollnagel called its commonest form the efficiency–thoroughness trade-off (ETTO): under pressure, people cannot be both completely thorough and completely efficient, and they choose case by case. The gap between **work as imagined**, the work in runbooks and process documents, and **work as done** is not a compliance failure. It is where the system's resilience lives.

#### The catch that did not make the news {#the-catch-that-did-not-make-the-news}

Consider the agent-written rewrite of Encore's Notification service, told at the end of the companion volume. The work as imagined was clear: contracts, boundary rules and security checks pass, and the service level objective (SLO) canary promotes. All of it passed. The work as done included one engineer who felt the new retry semantics deserved more time than the pipeline thought. She spent 20 minutes on that one change, saw that a retry after a partial failure could send a fan the same ticket twice, and wrote a spec-level idempotency test before merging.

In a Safety-I organization this event leaves no trace; Safety-II asks us to study it as carefully as the outage. The engineer had time, because the change was not squeezed into a crowded release. She had context, having worked on ticket delivery. She had authority, since nothing stopped a reviewer from slowing a green pipeline. And she had reason for suspicion, because 40 files nobody had typed invited a closer look. A reorganization that left reviewers without slack or context would remove the catch without ever registering its loss. The adjustments that save us most often are the ones we have never written down.

#### Resilience as a capacity {#resilience-as-a-capacity}

Resilience engineering, which gathered as a field around a 2004 symposium and the book *Resilience Engineering: Concepts and Precepts* (2006, edited by Hollnagel, Woods and Leveson), supplies the working vocabulary. **Resilience** is a system's capacity to adjust its functioning before, during and after disturbances, so that it sustains operations under expected and unexpected conditions alike. David Woods contrasts handling variation within the designed envelope with **graceful extensibility**, the ability to stretch past its edge; systems lacking the second are brittle, fine until they collapse. His law of stretched systems adds that any gain in capacity is soon consumed by demands to do more, which is Rasmussen's migration seen from another angle.

The ideas reached software through John Allspaw, Richard Cook and the SNAFUcatchers, whose STELLA report (2017) studied engineers coping with real incidents. It draws a line through the system: below it sit code, infrastructure and tooling; above it, people, each holding a partial mental model of what lies below, seen only through dashboards and tools. Incidents are the moments those models prove wrong, which makes them information rather than embarrassment. Figure 2.5 draws Encore through that line.

{% include diagrams/fig-2-5.svg %}

*Figure 2.5 — Above and below the line of representation, after the STELLA report (2017). Nobody touches the running system directly; every person sees it and acts on it through representations, and holds a partial model of what lies beneath them.*

**Recap.** Safety-I studies what goes wrong and removes causes; Safety-II studies what goes right and supports the adaptations that produce it. Performance variability is the source of both success and failure, and the gap between work as imagined and work as done is where resilience lives. Resilience is a capacity to adapt, including beyond the designed envelope, and it lives above the line, in people's mental models.

**Exercise 2.4.** Find one occasion in the last quarter when someone on your team noticed and prevented a problem that no process would have caught. Write it up as you would an incident: what they noticed, what let them notice, and what change in your organization would quietly have removed that capacity.

### 2.5 Systems Thinking and Control — STAMP for Software

#### Safety as a control problem {#safety-as-a-control-problem}

The models so far explain failure well and prescribe engineering poorly. Nancy Leveson of MIT, who had spent years on the safety of software-intensive systems, built one that does both. Her **STAMP** (System-Theoretic Accident Model and Processes), first set out in a 2004 paper and developed in *Engineering a Safer World* (2011), starts from systems theory instead of chains of events. Safety is an emergent property of the whole, distinct from the reliability of its parts: many software accidents happen with every component doing exactly what it was built to do. Accidents occur when the controls meant to enforce safety constraints are inadequate.

The model has three ideas. **Safety constraints** are conditions that must always hold, such as "no seat is sold twice". A hierarchical **control structure** of controllers (people, organizations, software) issues control actions downward and receives feedback upward. And each controller acts on a **process model**, its own belief about the state of what it controls. At Three Mile Island the light that reported a command instead of a position fed the operators' process model false feedback, and every subsequent control action was rational and wrong. The governor of Chapter 7 is a controller in exactly this sense, and its descendants run our clusters.

Leveson's hazard analysis method, **STPA** (System-Theoretic Process Analysis), asks of each controller how its control actions could be unsafe, in four ways: a needed action is not provided; an action is provided that causes a hazard; an action is provided too early, too late or in the wrong order; or an action is stopped too soon or applied too long. Her accident analysis method, CAST (Causal Analysis based on STAMP), applies the same structure after the fact, and Chapter 13 puts it to work.

#### Encore's control structure {#encores-control-structure}

Software suits STAMP unusually well, because our controllers are explicit: every autoscaler, reconciler and admission gate is a control loop with a process model we can read. Here is part of Encore's control structure around an on-sale:

| Controller | Controls | Process model (what it believes) | Feedback it receives |
|---|---|---|---|
| On-Sale team | Gate admission rate | Seat Inventory's safe throughput, from load tests | Load-test reports, on-sale dashboards |
| Sale Gate | Fans admitted per second | A configured rate, about 1,200 fans/s per event | Queue depth, its own error rate |
| Bot Screening | Which sessions are blocked | What bot traffic looks like, from past patterns | Block rates, appeals |
| Kubernetes autoscaler | Pod counts per service | CPU and request load per pod | Metrics, a few seconds late |
| Platform node-upgrade reconciler | Node versions in each cluster | Node health and disruption budgets | Node and pod readiness |
| Reliability team | Readiness review, freeze policy | The on-sale calendar, past incidents | Reviews, postmortems, chat |

*Figure 2.6 — Part of Encore's control structure around an on-sale. Each controller acts rationally on its own process model; hazards arise where a model is stale, incomplete or blind to another controller's actions.*

Read the table column by column and questions surface that no component review would ask. Where do two controllers act on the same thing without knowing of each other? Which process models come from tests, and how closely do those tests resemble an on-sale? Which controllers know an on-sale is happening, and which have no way to find out? The table makes these questions askable, which is the first service a good model performs. A well-made control structure is a map of where the next surprise could come from.

#### Mastering complexity with structure {#mastering-complexity-with-structure}

STAMP returns us to the oldest weapons against complexity: abstraction, decomposition and hierarchy. Drawing the control structure decomposes responsibility into controllers with stated constraints, and it separates essential complexity from accidental. Encore's 500× spike and its bots come with the business; controllers added one at a time by different teams, each with a process model nobody else has read, do not. STAMP does not remove that accidental complexity, but it makes it visible, and what is visible can be governed.

This is the book's through-line seen whole. Reliability is the product of a control structure in which people and machines keep each other's process models accurate, and it decays whenever a controller acts on a belief the world has quietly outgrown. The chapters that follow can be read as ways to keep those beliefs current: SLOs and observability as feedback, delivery as safer control actions, incident response as control under pressure, and learning from incidents as repair of the process models themselves.

**Recap.** STAMP treats safety as an emergent property enforced by a hierarchy of controllers, each acting on a process model of what it controls. Hazards arise from inadequate control, often from process models that are stale or blind to other controllers. Software makes its controllers unusually explicit, so the control structure is the natural map for finding where the next surprise could come from.

**Exercise 2.5.** Draw a control-structure table like Figure 2.6 for one critical path in your system, including at least one automated controller and one team. For each controller, write one unsafe control action from each of STPA's four categories, and circle the one you would least like to discover in production.

### Kata: The Twice-Monthly Run

> **Your brief: "Payday."** A payroll SaaS for 3,000 employers in four EU countries. Twice a month it computes about 600,000 payslips and sends payment files to 11 partner banks, each with a hard cutoff around 16:00 local time; a missed cutoff means people are paid late. Its 24 engineers run a modular monolith, a calculation engine that calls a third-party tax-rules service synchronously, and a file-generation pipeline. Last year they added auto-remediation that restarts stuck calculation workers. Two months ago a configuration change nearly sent a bank a duplicate file; an operations analyst noticed the totals were twice the usual size and stopped it. The pre-payday freeze, once 48 hours, is now "no risky changes on payday", and nobody can say who decides what is risky.

**Deliverables:**

1. **Coupling and complexity map** — Payday's main components on Figure 2.1, and two couplings to loosen before the next run, with their costs.
2. **Latent-condition inventory** — at least six latent conditions that could combine with an ordinary slip on payday.
3. **The near miss as Safety-II** — what the analyst noticed, what let them notice, and what would erode that capacity.
4. **Drift register** — the freeze as written against the freeze as practiced, with three indicators that would show further drift.
5. **Control structure** — the controllers around file generation, including the auto-remediation, with their process models and one STPA unsafe control action each.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Systemic framing | Does any deliverable stop at a person, or does each reach the conditions behind the action? |
| Coupling realism | Do the proposed loosenings respect the bank cutoffs, with arithmetic on the time they buy? |
| Safety devices | Is the auto-remediation analyzed as a potential source of accidents as well as a defense? |
| Learning from success | Would the near-miss write-up help the next analyst notice? |
| Drift visibility | Could an outsider read the drift register and see the margin being spent? |
| Process models | Is there at least one controller whose model of the world is plainly stale or incomplete? |

#### Where you now stand

You can now read a system as safety science reads it: place it on Perrow's chart, look past the sharp end for latent conditions, watch for the slow spending of margins, study what goes right as seriously as what goes wrong, and draw the control structure that shows where process models may be failing. These ideas recur in every later chapter. The first place they bite is automation, because every script, reconciler and assistant we add is both a safety device and a new controller with a process model of its own. Chapter 3 takes up that paradox, beginning with Lisanne Bainbridge's ironies.

### References

- Charles Perrow — [*Normal Accidents: Living with High-Risk Technologies*, updated ed.](https://press.princeton.edu/books/paperback/9780691004129/normal-accidents). Princeton University Press, 1999.
- Richard I. Cook — [*How Complex Systems Fail*](https://how.complexsystems.fail/). Cognitive Technologies Laboratory, University of Chicago, 1998 — free online.
- Nancy G. Leveson — [*Engineering a Safer World: Systems Thinking Applied to Safety*](https://doi.org/10.7551/mitpress/8179.001.0001). MIT Press, 2011 — free online.
- Jens Rasmussen — [*Risk Management in a Dynamic Society: A Modelling Problem*](https://doi.org/10.1016/S0925-7535%2897%2900052-0). Safety Science, 1997.
- Sidney Dekker — [*Drift into Failure*](https://www.routledge.com/Drift-into-Failure-From-Hunting-Broken-Components-to-Understanding-Complex/Dekker/p/book/9781409422211). Ashgate, 2011.
- Erik Hollnagel — [*Safety-I and Safety-II: The Past and Future of Safety Management*](https://www.routledge.com/Safety-I-and-Safety-II-The-Past-and-Future-of-Safety-Management/Hollnagel/p/book/9781472423085). Ashgate, 2014.
- David D. Woods, Sidney Dekker, Richard Cook, Leila Johannesen, Nadine Sarter — [*Behind Human Error*, 2nd ed.](https://www.routledge.com/Behind-Human-Error/Woods-Dekker-Cook-Johannesen-Sarter/p/book/9780754678342). Ashgate, 2010.
- James Reason — [*Managing the Risks of Organizational Accidents*](https://www.routledge.com/Managing-the-Risks-of-Organizational-Accidents/Reason/p/book/9781840141054). Ashgate, 1997.
- James Reason — [*Human Error*](https://doi.org/10.1017/CBO9781139062367). Cambridge University Press, 1990.
- Erik Hollnagel, David D. Woods, Nancy Leveson (eds.) — [*Resilience Engineering: Concepts and Precepts*](https://www.routledge.com/Resilience-Engineering-Concepts-and-Precepts/Hollnagel-Woods-Leveson/p/book/9780754649045). Ashgate, 2006.
- David D. Woods (ed.) — [*STELLA: Report from the SNAFUcatchers Workshop on Coping with Complexity*](https://snafucatchers.github.io/). The Ohio State University, 2017 — free online.

---

## Chapter 3: Automation and Its Ironies — Toil, Runbooks, and the Human Role {#ch3}

> Every machine that takes a task away from us leaves a harder one behind.

Every operations team keeps a list of chores it would rather a machine did, and works through it as time allows. It is a sound instinct: repetitive work done by hand at 3 a.m. is slow, error-prone and quietly corrosive. Yet the history of automation in every field that has taken it seriously, from chemical plants to flight decks, tells a stranger story than "automate and be free." The question of this chapter is what automation actually does to the work it touches, and what it leaves for the people who remain.

In 1983 the British psychologist Lisanne Bainbridge published a short paper in *Automatica* with a title that has outlived most of its contemporaries: "Ironies of Automation." Its argument fits in a sentence. When we automate a process we do not remove the human from it; we change the human's job, usually into a harder one, and in ways that erode the very skills the new job demands. She was writing about control rooms and aircraft; four decades later the paper reads as if written about a platform team with an on-call rotation.

Encore has automated a great deal. Its on-sale preparations, once a wiki page, run from a button; its platform upgrades Kubernetes nodes weekly untouched; its seat ledger fails over on its own, so reliably that hardly anyone remembers how to do it by hand. This chapter follows that automation from the case for it, through its ironies, to a vocabulary for deciding how much a machine should do alone, and ends with the newest machine Encore has added, which raises the oldest questions.

### 3.1 Toil and the Case for Automation

#### What toil is {#what-toil-is}

The word needs a precise meaning, or every unpleasant task becomes "toil." Google's site reliability engineering (SRE) book (2016) gave the field its working definition. **Toil** is work tied to running a production service that is manual, repetitive, automatable, tactical rather than strategic, devoid of enduring value, and that grows linearly as the service grows. Each adjective does work: a task done once is not toil, however tedious, and a task that needs fresh judgment each time is not toil, however frequent.

The last property matters most. A team whose work is mostly toil can grow only by hiring at the rate the business grows; it has turned an engineering function into a linear cost. Google's SRE organization capped toil at 50% of each engineer's time, a line in the sand whose purpose was to keep half of every week for the work that removes toil, so that operational effort could bend away from the curve of growth. Yet a little toil keeps engineers close to the system, and Section 3.3 will argue that removing the last of it has costs we rarely count. The goal is toil kept bounded and visible.

#### Encore's toil, measured {#encores-toil-measured}

The Reliability team asked on-call engineers to tag their interrupts for a quarter. Across stream-aligned teams, roughly 30% of the on-call week met all six properties of toil. The On-Sale team, in the spring touring season, spent closer to 45%, and most of it went on one chore: preparing the platform before each scheduled on-sale.

The touring world Encore serves has the same problem. A stadium tour loads into a different venue every few nights and rigs the same lights, sound and stage again and again. Mature productions pre-wire what they can into road cases and standard rigging plots, so that load-in becomes assembly. The crew does not shrink; it becomes faster and less likely to forget a safety chain at 2 a.m. The analogy breaks, usefully, at the venue whose roof cannot take the standard rig: pre-wired cases are wonderful until the situation they were wired for is not the one in front of you.

#### The case, and its fine print {#the-case-and-its-fine-print}

The SRE book's chapter on the evolution of automation makes the positive case: automation is consistent where people vary, fast where they are slow, and it turns knowledge held in a few heads into a platform. Consistency matters most, because most operational mistakes come from variation. It also recounts a decommissioning workflow whose bug erased far more machines than anyone intended, with all the speed and consistency automation promises. Automation repeats our mistakes as faithfully as our successes, at the scale it was built to reach.

I find it useful to see automation as abstraction applied to work. A good abstraction hides the steps so that we can think about the purpose: we stop thinking about 31 commands and start thinking about whether the on-sale is ready. But every abstraction leaks, and automation leaks under unusual conditions, when the hidden steps suddenly matter again and nobody has looked at them in a year. Toil is the accidental complexity of operations, performed by hand. Automation removes the hands; it moves the complexity somewhere we can no longer see.

**Recap.** Toil is manual, repetitive, automatable, tactical work without enduring value that grows with the service, and its linear growth is the reason to fight it. Automation brings consistency first and speed second, repeats mistakes as faithfully as successes, and hides complexity without removing it.

**Exercise 3.1.** For one on-call week, tag every interrupt against the six properties of toil. Which chore takes the largest share, and how does it scale with your customers, services or tenants?

### 3.2 From Runbook to Script to Self-Service

#### The prompt book {#the-prompt-book}

A **runbook** is a written procedure for an operational task, precise enough that someone who did not write it can follow it under pressure. The idea is older than computing. In the theatre the stage manager keeps the *prompt book*, the script marked with every cue, and during the performance calls each one ("standby lighting 42 … lighting 42, go") for the crew to execute. The prompt book is a very good runbook: it has been rehearsed, it is the single authoritative copy, and a human with judgment still calls every cue.

Encore's on-sale pre-warm began as a wiki page, amended by everyone who ran it, until it had 31 steps. Raise provisioned concurrency on the Sale Gate's admission edge. Confirm the event's four Seat Inventory shards and their leaders in the home region. Warm the seat-map geometry cache for the venue. Set the admission rate and load the event's bot rules. Check the synthetic buyer's last run. Post readiness; announce the change freeze. It took an experienced engineer about 70 minutes, and with about 160 on-sales a year needing it, well over 200 hours of skilled attention. The hours were the smaller cost: one spring morning the concurrency step was skipped, and the first 90 seconds of an on-sale ran on cold starts.

#### Script, then service {#script-then-service}

An engineer then turned the page into `prewarm.py`, which took an `event_id` and ran the steps in order, cutting 70 minutes to 12 and ending skipped steps. It also brought new failure modes. It needed broad production credentials, so only a handful of people could run it, and when a step failed it left the platform half-prepared. And it encoded the steps but not the judgment around them. Beside the admission-rate step the wiki had said "check with the On-Sale lead if the venue is new"; the script set the rate and moved on.

Each step of the wiki page had contained a moment of human attention, a person glancing at the result before moving on, and code removes those moments unless we deliberately put them back as checks. A runbook is a script that has not yet been trusted to run alone, and the passage between the two is where that trust has to be earned.

The third generation is a self-service workflow in Encore's platform portal, which the teams call **curtain-up**. At 07:30 on the day of a large on-sale, the On-Sale team's on-call engineer reviews the plan it proposes and presses go. Every step is idempotent, so a failed run resumes where it stopped, and each states its precondition and checks its result: the cache step reports its hit ratio after warming, and the concurrency step confirms instances are provisioned, not merely requested. It finishes before the 08:00 freeze and posts its report to the on-sale channel. The On-Sale team owns what the steps do; the platform group owns the engine that runs them.

| | Wiki page | `prewarm.py` | Curtain-up |
|---|---|---|---|
| Who can run it | anyone who can read | a few engineers with admin credentials | the on-call engineer, through the portal |
| Time per on-sale | 70–120 min | about 12 min | about 15 min unattended, 5 min of review |
| Where judgment lives | in notes beside each step | nowhere | in explicit preconditions and checks |
| Failure halfway | the person notices, usually | half-prepared platform; read the code | resumes from the failed step |
| What it teaches | every step, every time | nothing, unless you read it | the plan and report, if anyone reads them |

*Figure 3.1 — Three generations of Encore's on-sale pre-warm. Each removes toil, and each changes who knows what the steps are.*

Section 3.3 will need the last row. The wiki page was a tutor as well as a procedure; the script taught nothing; curtain-up teaches only as much as its report is read, a habit automation itself tends to erode.

The ladder generalizes, and each rung needs the one below it. Automating a procedure nobody has written down encodes one person's habits, and turning a script into self-service before its failure modes are understood produces a button only its author can diagnose. Figure 3.2 puts the generations' yearly cost side by side.

{% include diagrams/fig-3-2.svg %}

*Figure 3.2 — Engineer-hours a year spent on the pre-warm, by generation, against the number of on-sales. Each rung flattens the line by an order of magnitude; notice that none of them reaches zero, because someone still has to read the plan.*

**Recap.** A runbook carries judgment in its margins, which code loses unless we rebuild it as explicit checks. Encore's pre-warm moved from wiki to script to curtain-up, gaining speed and consistency, and each step changed who understood the procedure, a cost the time savings do not show.

**Exercise 3.2.** Pick one procedure your team runs by hand. Name its rung on the ladder, and for each step list the moment of human attention it contains. Which of those moments would a script silently remove?

### 3.3 The Ironies — Deskilling, Surprise, and the Hand-Back

#### Bainbridge's argument {#bainbridges-argument}

Bainbridge's paper runs to five pages. She wrote when the prevailing view held that the human operator was unreliable and should be designed out wherever possible. She did not dispute that machines could do much of the work better; her point was about what was left behind, and the ironies she drew out fall into four.

The first is that the designer's errors become a major source of operating problems. Automation moves human error upstream, from the operator acting in the moment to the designer who decided, months earlier and far from the plant, what the machine would do in every case they could foresee.

The second is about what remains. The designer who tries to eliminate the operator still leaves the operator the tasks the designer could not think how to automate. They are an arbitrary collection, defined only by having resisted automation, and so tend to be the hardest, rarest and least understood tasks in the system.

The third concerns monitoring. Among the leftover tasks is watching the automation and stepping in when it fails, and vigilance research since the 1940s had shown that attention to a display on which little happens decays within about half an hour. We ask people to watch for rare events, which are exactly what attention fails to catch.

The fourth, with the longest shadow, is about skill. When the automation fails, the operator must take over by hand and diagnose what went wrong, and both skills decay without use; an operator who has spent years only monitoring is no longer experienced, whatever their tenure. Inside this catch lies another: to monitor the automation well, the operator must know what it ought to be doing, which is knowledge built by doing the work oneself, the very work the automation took away. Her conclusion, paraphrased, was that the most successful automated systems, those needing intervention least often, may need the greatest investment in operator training.

#### Surprise and the hand-back {#surprise-and-the-hand-back}

Nadine Sarter and David Woods later named what operators experience when automation behaves unexpectedly: **automation surprises**. *Behind Human Error* (2010) treats them at length, with mode error, the confusion when behavior depends on a mode the operator has lost track of. Earl Wiener reported that pilots of the new glass cockpits of the 1980s kept asking three questions of their automation: what is it doing, why did it do that, and what will it do next? Engineers watching a cluster reschedule pods mid-incident ask them too.

Aviation's most studied hand-back is Air France 447. On 1 June 2009 an Airbus A330 flying at night from Rio de Janeiro to Paris passed through ice crystals over the Atlantic. Its airspeed probes iced over and the autopilot disconnected, handing a flyable aircraft to a crew who had to fly it by hand at cruise altitude, which airline pilots rarely do. Within about a minute the aircraft had stalled, and some four minutes after the autopilot let go it struck the ocean, with the loss of all 228 people aboard. The French investigators' final report (2012) deserves to be read rather than summarized into blame, but its core is Bainbridge's: control came back in exactly the conditions the automation could not handle, to people whose practice at that task was thin, with little time to understand what had happened. The analogy breaks for us in the stakes and the time available, but holds in the shape of the hand-back, which Three Mile Island, Chapter 2's touchstone, had shown from a control room.

#### The failover nobody has done {#the-failover-nobody-has-done}

Seat Inventory elects a new shard leader automatically, with fencing so a deposed leader cannot keep writing. It has handled about 60 failovers in the past 19 months, mostly during node maintenance, each with a few seconds of rejected writes and no human involved. It is good automation. It also has a manual failover procedure for the cases the automation refuses. When it cannot confirm that the old leader's term has expired, it stops rather than risk two leaders, and a person must confirm the fence, advance the term, promote a replica and verify the ledger's sequence. When the Reliability team checked last spring, 4 of the 34 engineers on the Inventory and On-Sale rotations had ever done it in production, the most recent 19 months earlier. Game days exercised the automatic path, the one the system takes; nobody had exercised the other.

This is Bainbridge's fourth irony nearly word for word. The automation is good, so the hand-back is rare; the hand-back is rare, so the skill has decayed; and when it comes, it will come in exactly the situation the automation found too ambiguous to resolve. A failover we never practice is one we will perform for the first time during an on-sale. Encore's response has been modest and, I think, correct: the Inventory team now runs a manual failover in staging monthly, rotating the operator, and quarterly in production on a shard serving no live on-sale. The first drill found two stale commands in the procedure. Figure 3.3 sketches the shape of the problem.

{% include diagrams/fig-3-3.svg %}

*Figure 3.3 — Readiness for the manual failover, sketched (the curve is illustrative; the counts are Encore's). Sixty successful automatic failovers did nothing to keep the manual path alive; only practice of that path does.*

The same shape appears elsewhere on the platform. The node-upgrade reconciler, a control loop Chapter 7 describes, replaced a quarterly weekend of manual node upgrades the platform group used to dread. It drains each node within the workloads' disruption budgets, upgrades it and moves on, and in over a year it has caused almost no pages. Under the on-sale freeze it counts as low-risk automation. It knows a great deal about nodes and very little about concerts, which nobody has yet had reason to find strange.

**Recap.** Automation moves error to the designer, leaves operators an arbitrary set of the hardest tasks, asks them to watch for rare events, and erodes the skills they need when control comes back. Surprises and stressful hand-backs follow from that structure, in aircraft and clusters alike. The remedy is deliberate practice of the paths automation makes rare.

**Exercise 3.3.** List the three most important automated recovery actions in a system you run. For each, find the manual procedure for when the automation declines, and count who has performed it in the last year. Schedule a drill for the lowest count.

### 3.4 Levels of Automation and Calibrated Trust

#### How much should the machine do alone? {#how-much-should-the-machine-do-alone}

In 1951 the psychologist Paul Fitts led a report listing what humans and machines each do better, later nicknamed MABA-MABA ("men are better at, machines are better at"). *The Practice of Cloud System Administration* (2014) contrasts three allocation principles: the *left-over principle* automates everything possible and leaves people the rest, the design Bainbridge criticized; the *compensatory principle* gives each task to whichever party does it better; and the *complementarity principle*, which the authors favor, has people and machines work together so that people keep the skill to take over. Erik Hollnagel and David Woods (2005) go further: automation transforms human work, so the unit worth designing is the joint system of people and machines.

For a vocabulary we turn to Thomas Sheridan and William Verplank, who in 1978, studying remote control of undersea vehicles at MIT, set out levels of automation between full human control and full machine autonomy. In the form usually quoted it has 10 levels, and it remains the simplest way to state how much a piece of automation may do without asking.

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

*Figure 3.4 — Sheridan and Verplank's levels of automation, applied to Encore. The level belongs to a specific action rather than a whole system: curtain-up sits at level 5 for the decision and level 7 for its steps.*

Drawn for a real system, this table usually shows consequential automation high on the scale, informing nobody, at a level nobody chose; it was whatever the first version did. Choosing it deliberately, per action, is a design decision that deserves a written rationale.

#### Use, misuse, disuse, abuse {#use-misuse-disuse-abuse}

The other half of the problem is how people come to rely on automation, for which Raja Parasuraman and Victor Riley (1997) gave four words.

| Term | Meaning | How it looks in operations |
|---|---|---|
| **Use** | relying on automation when appropriate | running curtain-up and reading its report |
| **Misuse** | over-reliance, including complacency | approving the plan unread, because it has always been right |
| **Disuse** | under-reliance, usually after false alarms | muting an alert channel that cried wolf last month |
| **Abuse** | automating without regard for the people left to supervise it | a remediation bot with no way to see or pause what it does |

*Figure 3.5 — Parasuraman and Riley's four relationships with automation. Misuse and disuse are failures of trust; abuse is a failure of design, made at the blunt end, far from those who live with it.*

Seafarers had a phrase for misuse long before software: the **radar-assisted collision**, in which ships with working radar collide because their officers trusted what the screen seemed to say over careful plotting. The radar worked; the trust was miscalibrated. The analogy breaks in software's favor, since our automation can be made to show its reasoning.

John Lee and Katrina See (2004) gave the idea its precise form. **Calibrated trust** is reliance that matches the automation's actual capability: high where it performs well, low where it does not, and fine-grained enough to tell the two apart. People base trust on the automation's *performance* (what it has done), its *process* (how it works) and its *purpose* (what it was built for), and designers should make all three visible. A curtain-up report that shows the cache hit ratio after warming supports calibrated trust; one that says only "done" asks for faith. Trust that is never tested is not calibrated, only comfortable.

{% include diagrams/fig-3-6.svg %}

*Figure 3.6 — Calibrated trust, after Lee and See (2004). Trust should track what the automation can actually do; misuse lives above the diagonal and disuse below it, and the same team can sit in both places with two different tools.*

#### Automation as a team player {#automation-as-a-team-player}

Gary Klein, David Woods and colleagues asked in 2004 what it would take for automation to be a "team player" in joint activity. Teammates, they observed, enter a **basic compact**, an agreement to coordinate and to warn one another when they cannot keep their part. They are **mutually predictable**, **directable** (one can redirect the other as circumstances change), and they maintain **common ground**, the shared knowledge that lets a short message carry a great deal of meaning.

Curtain-up passes these tests: it shows its plan and can be paused. The node-upgrade reconciler is predictable from its log and directable through an annotation that holds a node, but shares little common ground with the teams on those nodes: it knows their disruption budgets and nothing of their calendars. Bot Screening's velocity rules are the weakest teammate, acting silently at level 9 on assumptions about client behavior set years ago. None of this says the automation is bad, only how well it can be supervised, a property we rarely measure.

**Recap.** Sheridan and Verplank's scale states, per action, how much a machine may do unasked, and that level should be chosen. Parasuraman and Riley describe how reliance goes wrong; Lee and See ask that performance, process and purpose be visible so trust can be calibrated. The team-player tests ask whether automation can be supervised at all.

**Exercise 3.4.** Place five automated actions from your platform on the 10-level scale. For the highest, answer the four team-player questions. What would make it directable during an incident?

### 3.5 AI Assistants — The Newest Automation, the Oldest Ironies

#### Cue {#cue}

Encore's newest operational automation is an assistant called **Cue**. It is built on the internal Model Context Protocol (MCP) server that Encore's AI features already use, through which it reads telemetry, deploy history, runbooks and past postmortems. It answers questions in the incident channel, drafts timelines and points to matching runbook steps. It is read-only by default. A few runbook actions, such as pausing a curtain-up run or raising the Gate's provisioned concurrency, are available to it only when a named human approves that specific action in the channel. Chapters 5 and 12 show it at work.

On Sheridan and Verplank's scale Cue sits mostly at levels 2 to 4, and its approved actions at level 5, a deliberately conservative placement. What is new is not its level but its manner. Earlier automation was narrow and literal: the reconciler drains nodes, the velocity rule blocks clients, each in its own small vocabulary. Cue speaks the engineers' language, on every subject, with the same fluency whether it is right or wrong.

The theatre supplied its name and supplies the analogy. A prompter sits in the wings with the book and gives a forgotten line, and a good one is invaluable and nearly invisible. The analogy breaks where it matters most. The prompter reads from the authoritative script, whereas Cue composes its lines from whatever it can retrieve, and a plausible line that is in no script sounds exactly like one that is.

#### The ironies, in order {#the-ironies-in-order}

Bainbridge's ironies apply one by one. The designer's errors move upstream: Cue's behavior depends on the tools it is given, the runbooks it can retrieve and its instructions, all decided months before any incident. A runbook that is stale on the wiki is stale in Cue's answers, delivered with more confidence than the wiki ever had.

The leftover tasks grow harder. Cue is very good at the lookup parts of an investigation, and leaves the engineer the judgment about which findings matter, whether a suggested action is safe now, and what Cue has not looked at. Addy Osmani, writing about coding assistants in *Beyond Vibe Coding* (2025), calls the parallel effect the "70% problem": the assistant speeds up the easy majority, and the remainder, where expertise lives, stays with the human. In operations that remainder arrives at 3 a.m.

Monitoring grows harder too. Approving Cue's suggestions is a vigilance task, and a well-performing Cue makes it a boring one; after 50 sensible suggestions, the 51st is approved on reflex. This is Parasuraman and Riley's misuse, and an approval step that is never declined is a rubber stamp with a name attached.

And skills decay in a new place. Newer engineers have learned to ask Cue rather than write a trace query, a reasonable division of labor in ordinary weeks. But judging whether Cue's answer is right needs exactly the skill of investigating unaided that its convenience lets lapse: Bainbridge's catch, applied to diagnosis rather than control.

#### Designing for calibrated trust {#designing-for-calibrated-trust}

Encore's design choices for Cue follow from the earlier sections and owe nothing peculiar to language models, which is, I think, the main lesson here. Cue cites its sources: every answer links the query, dashboard, deploy or postmortem behind it, so engineers can check its process as well as its conclusion, as Lee and See recommend. Its actions come from a fixed catalog, each approved separately, so it is predictable and directable. The Reliability team tracks how often its suggestions are accepted, declined and later judged wrong, so that trust rests on a record of performance. And each quarter some game days and incident drills run with Cue switched off, for the same reason the Inventory team fails over shards by hand.

None of this makes Cue safe in any final sense; it makes Cue supervisable, which we can design and test. An assistant that is fluent when wrong is the oldest irony of automation in a new voice, and Bainbridge's answers (practice, visibility, and humility about what the designer could foresee) still hold.

**Recap.** Cue suggests and, with explicit approval, acts from a fixed catalog of runbook steps. Every one of Bainbridge's ironies applies to it, sharpened by its fluency. Encore designs for calibrated trust with cited sources, chosen levels, a tracked record and drills without the assistant.

**Exercise 3.5.** If your team uses an AI assistant in operations, review the last 20 suggestions or actions someone approved. How many were declined, and how many did anyone check against the source? If both answers are zero, design one change that makes checking cheaper than approving.

### Kata: The Hand-Back

> **Your brief: "Lanternway."** A managed hosting company for 3,000 online shops across Europe, run by 22 operations engineers in two time zones. It has automated aggressively: a remediation bot restarts unhealthy containers about 400 times a week, and database failover, certificate renewal and storage expansion are hands-off. An AI assistant in the on-call channel can run 15 remediation actions with one-click approval; it has been approved 1,100 times and declined twice. On-call engineers still report 35% of their week as toil, mostly tickets the bot could not resolve. Last month a database failover stalled and handed control to a human for the first time in 14 months; the manual procedure took 95 minutes, 40 of them spent finding the right credentials.

**Deliverables:**

1. **Toil inventory** — the top five sources of toil, tested against the six properties, with how each scales with the number of shops.
2. **Runbook ladder** — the current rung of the 10 most frequent procedures, and the next rung for 3, with checks that replace lost human attention.
3. **Levels map** — every automated action on Sheridan and Verplank's scale, and the three you would move, with reasons.
4. **Hand-back drills** — which manual procedures are drilled, how often and by whom.
5. **Trust plan for the assistant** — what it must show, how approvals become meaningful again, and what you will measure.
6. **One architecture decision record (ADR)** — the remediation bot's level of automation, with its losses written down.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Toil with arithmetic | Is toil measured and tied to growth, or described by how tedious it feels? |
| Judgment preserved | When a procedure climbs the ladder, is each moment of human attention replaced by an explicit check? |
| Chosen levels | Is each action's level of automation a written decision, or an accident of its first version? |
| Practiced hand-backs | Would the stalled failover now take minutes, and who has practiced it this quarter? |
| Meaningful approval | Does the plan make declining the assistant likely when it is wrong, rather than rare by habit? |

#### Where you now stand

You can now measure toil, move a procedure from runbook to self-service without losing the judgment it carried, and recognize Bainbridge's ironies in your own platform. You can choose how much each machine may do alone and calibrate trust in it, an AI assistant included. Part II turns to how we know the system is working, beginning in Chapter 4 with how reliable it needs to be.

### References

- Lisanne Bainbridge — [*Ironies of Automation*](https://doi.org/10.1016/0005-1098%2883%2990046-8). Automatica 19(6): 775–779, 1983.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Raja Parasuraman, Victor Riley — [*Humans and Automation: Use, Misuse, Disuse, Abuse*](https://doi.org/10.1518/001872097778543886). Human Factors 39(2): 230–253, 1997.
- John D. Lee, Katrina A. See — [*Trust in Automation: Designing for Appropriate Reliance*](https://doi.org/10.1518/hfes.46.1.50_30392). Human Factors 46(1): 50–80, 2004.
- Gary Klein, David D. Woods, Jeffrey M. Bradshaw, Robert R. Hoffman, Paul J. Feltovich — [*Ten Challenges for Making Automation a "Team Player" in Joint Human-Agent Activity*](https://doi.org/10.1109/MIS.2004.74). IEEE Intelligent Systems 19(6): 91–95, 2004.
- Thomas B. Sheridan, William L. Verplank — [*Human and Computer Control of Undersea Teleoperators*](https://ntrl.ntis.gov/NTRL/dashboard/searchResults/titleDetail/ADA057655.xhtml). Technical report, MIT Man-Machine Systems Laboratory, 1978.
- David D. Woods, Sidney Dekker, Richard Cook, Leila Johannesen, Nadine Sarter — [*Behind Human Error*, 2nd ed.](https://www.routledge.com/Behind-Human-Error/Woods-Dekker-Cook-Johannesen-Sarter/p/book/9780754678342). Ashgate, 2010.
- Erik Hollnagel, David D. Woods — [*Joint Cognitive Systems: Foundations of Cognitive Systems Engineering*](https://www.routledge.com/products/9780367864200). CRC Press, 2005.
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan — [*The Practice of Cloud System Administration*](https://www.informit.com/store/practice-of-cloud-system-administration-devops-and-9780321943187). Addison-Wesley, 2014.

---

## Chapter 4: Reliability as a Product Decision — SLOs, Error Budgets, and Risk {#ch4}

> Every promise about reliability is also a promise about what we will stop doing.

How reliable should a system be? Engineers tend to hear a technical question and give the most technical answer available: "as reliable as we can make it." The answer sounds responsible and is nearly always wrong. Reliability costs money, attention and, above all, the freedom to change things, and a system made as reliable as possible has spent all three on a property its users stopped noticing several nines ago. The real question is a product question: how much unreliability can our users absorb before they would rather be elsewhere, and what will we buy with the rest?

The telephone network is where that question was first asked at scale, and where its most famous answer, "five nines," became a byword. Its engineers chose a number, priced it, built machines to meet it and quietly left room for calls that would not get through. We follow their example here, taking the chain the companion volume introduced, from service level indicator (SLI) to service level objective (SLO) to error budget, and turning it from a definition into a working instrument: one that chooses what to measure, settles arguments between teams and wakes people only when it should.

Encore needs that instrument now. It has one published objective, for the seat map, and 40 teams with opinions about what the others should promise. The Reliability team has been asked to give checkout, the on-sale window and every tenant an objective users would recognize, before the next big Friday.

### 4.1 Why 100% Is the Wrong Target

#### The Bell System and its nines {#bell-system-nines}

For most of the twentieth century the Bell System, AT&T with its operating companies, Western Electric and Bell Telephone Laboratories, ran the telephone network of the United States as a regulated monopoly, and it built an engineering culture around the expectation that the dial tone would always be there. When the first No. 1 Electronic Switching System (ESS) entered commercial service in 1965, in Succasunna, New Jersey, it brought stored-program control to the telephone exchange, and the design objective most often cited for it is striking: no more than two hours of total downtime in 40 years. That works out to a little better than 99.999% availability, the "five nines" that became the industry's shorthand for carrier-grade.

The objective was met by engineering. The switch duplicated its central processor and compared the two copies, so that a fault in one could be isolated while the other carried calls. Five nines was a budget of about five minutes a year, and the engineers spent real hardware to stay inside it.

Two details teach more than the famous number. The objective belonged to the switch, while the subscriber's experience depended on far more: the copper loop to the house, the handset, the storm that brought down a line. And the same network was deliberately engineered to fail some calls. Trunk capacity was sized to a **grade of service**, a target probability that a call is blocked in the busiest hour, and a commonly used figure was one call in a hundred. Building enough trunks never to block a call would have been ruinous, so the network accepted a small, priced, predictable failure rate at its peak. Chapter 6 takes up the queueing mathematics behind that choice. The most reliability-obsessed engineering organization of its century ran on an error budget long before the term existed.

#### What each nine costs {#what-each-nine-costs}

Figure 4.1 translates nines into time, using both a calendar year and the rolling 28-day window Encore uses for its objectives.

| Availability | Downtime per year | Downtime per 28 days |
|---|---|---|
| 99% | 3.65 days | 6.7 h |
| 99.5% | 43.8 h | 3.4 h |
| 99.9% | 8.8 h | 40 min |
| 99.95% | 4.4 h | 20 min |
| 99.99% | 53 min | 4 min |
| 99.999% | 5.3 min | 24 s |

*Figure 4.1 — The nines as time. Each additional nine divides the allowance by ten, and the cost of staying inside it rises by much more, because the last nines are bought with redundancy, slower change and people awake at night.*

Read the right-hand column as an operator would. At 99.9%, Encore can afford one bad deploy a month that takes half an hour to roll back. At 99.99%, four minutes, it cannot afford a human in the loop: by the time someone has been paged and found the dashboard, the budget is gone, so detection and rollback must be automatic. At five nines, 24 seconds must cover every dependency, failover and certificate renewal. Each nine changes the kind of engineering as well as its amount.

Users cannot perceive reliability beyond that of their own path to us. The *Site Reliability Engineering* book makes the point with users' phones and networks, which fail far more often than a well-run service: a fan on a train between tunnels cannot tell a 99.99% seat map from a 99.999% one, and every unit of reliability beyond what users perceive is paid for in change not made. A target of 100% is not a very high standard. It is a refusal to choose, and it hands the choice to whoever is most frightened.

This is why reliability is a product decision. Only the product owner can weigh a slightly less reliable seat map against a feature fans have been asking for. Engineers supply the price list; the business chooses from it, and carries the consequences.

**Recap.** The Bell System chose its nines, priced them and engineered to them, and it accepted blocked calls at the peak. Each nine changes the kind of engineering required. Because users cannot feel reliability beyond their own path to us, the target is a product choice about where to spend the freedom to change.

**Exercise 4.1.** For a service you run, find the row of Figure 4.1 at which a single incident, handled by your current detection, paging and rollback, would consume the whole monthly allowance. Is your published target above or below that row?

### 4.2 SLIs and SLOs That Users Would Recognize

#### From journeys to indicators {#journeys-to-indicators}

A **service level indicator (SLI)** is a measurement of service, expressed as the proportion of valid events that were good; a **service level objective (SLO)** is a target for that proportion over a stated window. The companion volume stopped there. The harder craft is choosing which events to count and what to call good, and the test I find most reliable is simple: could a fan, shown the SLI in plain words, recognize it as something they have felt?

That test points away from components and toward **user journeys**, the sequences of steps a user takes to get something done: join the waiting room, see the seat map, hold seats, check out, receive tickets. Each indicator for a journey must define what counts as an event, what counts as good and where it is measured.

Take checkout. A naive SLI counts HTTP 5xx responses from the Orders service, and gets two cases wrong. When a fan's card is declined, the system has worked correctly, and the event is good, however unhappy the fan. When the payment service provider (PSP) is down and Encore accepts the order and charges later, the fan has a ticket, and that event is good too. So Encore's checkout SLO reads: *of checkout attempts by admitted fans, 99.9% end in a confirmed order or a correctly explained decline within 3 s, measured at the gateway over a rolling 28 days.*

Medicine knows the distinction well. A doctor reads vital signs, but the outcome that matters is whether the patient can climb the stairs at home, and a ward can have excellent vitals and miserable patients. SLIs are vital signs chosen because they predict the outcome. The analogy breaks where software is kinder: we can often measure the outcome directly, so we should, and keep component metrics for diagnosis.

#### Ratios, thresholds and percentiles {#ratios-thresholds-percentiles}

SLIs come in two common shapes. An **event-based** (or ratio) SLI counts good events over valid events: 99.9% of checkouts. A **time-based** SLI judges each slice of time good or bad against a threshold and counts good slices: 99.9% of minutes in which the error rate stayed below 1%. Event-based SLIs weight busy periods heavily, which is usually what we want. Time-based SLIs treat a quiet minute and a frantic one alike, which suits services with little traffic, and contracts, whose authors prefer minutes to fractions.

Latency is where well-meant indicators go astray. "p99 latency below 800 ms" and "99% of requests faster than 800 ms" sound identical, and over one window on one server they are. Elsewhere they part company, because percentiles cannot be averaged: the mean of 10 servers' p99 values is not the fleet's p99, and the mean of 60 one-minute p99 values is not the hour's. The ratio form simply adds good and total counts, so it aggregates honestly across servers, regions and time. Encore therefore states latency objectives as ratios, records latency in histograms with a bucket boundary at each threshold, and measures at the gateway, because a server timing itself from the moment it accepts a request cannot see the requests still waiting to be accepted. Averages are where incidents go to hide, and server-side percentiles are where the queue goes to hide.

#### Windows, and the hour that matters {#windows-and-on-sale-slos}

The window is the SLO's memory. A **rolling window** (Encore uses 28 days, so every window holds four of each weekday) remembers continuously, so a bad Friday weighs on the team for exactly 28 days and is then forgiven. A **calendar window** resets on the first of the month. It suits reports and contracts but breeds strange incentives: a budget nearly spent on the 29th is rescued by the calendar, while a team that burned it all on the 2nd faces a long, cautious month.

Encore's peculiarity is that fans do not remember months. They remember 10:00 on the Friday their artist went on sale, and a 28-day checkout SLO can stay comfortably green while that hour was a disaster, diluted by 27 quiet days. So for each on-sale the readiness review classifies as major, Encore now evaluates an **on-sale-window SLO**: an objective computed over a fixed window around a scheduled event, here the first 60 minutes of the sale, with a budget of its own. Its SLI counts fans: *99% of admitted fans complete their journey, an order or a clear "sold out," without seeing an error.* Counting requests would let retries distort the picture, since a fan who retries an error 10 times generates 10 bad requests whether or not the 11th succeeds. A fan who saw an error page has had one bad on-sale, however many requests it took.

| Journey | SLI (good ÷ valid) | Where measured | Objective and window |
|---|---|---|---|
| See seat map | requests served in ≤ 800 ms | gateway | 99.9%, rolling 28 days |
| Check out | attempts ending in confirmed order or explained decline within 3 s | gateway | 99.9%, rolling 28 days |
| Major on-sale | admitted fans completing without an error page | Gate and gateway, joined per fan | 99%, first 60 min of the sale |
| Receive tickets | orders with ticket in wallet within 5 min | Notifications, confirmed by wallet receipt | 99.5%, rolling 28 days |

Each objective in the right-hand column is a product decision, signed by the journey's product owner.

**Recap.** Good SLIs start from user journeys and define the event, the good event and the place of measurement. Ratios aggregate honestly where percentiles do not. Rolling windows give an SLO a steady memory, and a scheduled peak deserves a window shaped like the event.

**Exercise 4.2.** For one SLI you have, find a case it counts as good that the user felt as bad, and one it counts as bad that nobody noticed. Rewrite it to count both correctly.

### 4.3 Error Budgets as a Negotiation Instrument

#### A contract written in calm weather {#contract-in-calm-weather}

An **error budget** is the amount of unreliability an SLO permits over its window, and an **error budget policy** is the written agreement about what happens as it is spent. The budget is arithmetic. The policy is politics in the honorable sense: an agreement among people with different interests about how to share something scarce.

Its value lies in timing. Every organization argues about whether to ship or to stabilize, and the worst time to argue is during the outage, when the product owner has a marketing date and the on-call engineer has not slept. The policy moves the argument to a quiet Tuesday. Encore's purchase-path policy says, in summary: while budget remains, teams ship at will; below 25% remaining, changes to the journey need a second reviewer from the Reliability team; once it is exhausted, only reliability work, security fixes and risk-reducing changes ship until the budget recovers; and any single incident that consumes more than 20% of a budget requires a postmortem, a rule taken nearly unchanged from the example policy in *The Site Reliability Workbook*.

A touring production offers a fair analogy. The tour manager holds a contingency line for what will go wrong on the road, a cancelled ferry, a broken truck, a sick lighting operator, and the crew knows in advance who may spend it and what happens when it runs out. The analogy breaks in a useful place: money spent is gone, whereas an error budget refills as the window rolls forward, and so it is meant to be spent. A team that ends every month with most of its budget intact is paying for reliability nobody asked for in the currency of changes it did not make. The *Site Reliability Engineering* book tells of Google's Chubby lock service, so reliable that its users came to depend on more than its objective promised, until planned outages were taken to bring its real availability down to its stated one. Unspent budget looks like thrift, but it is a promise you are keeping by accident, and someone will soon build on it.

The idea is older than SRE. Walter Shewhart, working on manufacturing quality for the Bell System in the 1920s, separated the variation a stable process always shows from variation with an assignable cause, and his control charts told managers when to leave a process alone. An error budget does the same for a service: failures within budget are the process behaving as designed, and a fast burn signals a cause worth hunting.

#### The dispute between On-Sale and Bot Screening {#onsale-botscreening-dispute}

Encore's policy met its first real test in the spring. At a mid-size arena on-sale, the Bot Screening team switched on a new device-fingerprint rule that blocked about 6,000 sessions in 15 minutes, most of them, as challenge data later suggested, real fans on an older phone browser. The on-sale-window SLO came in at 96.8% against its 99%, and the blocked journeys took 70% of the On-Sale team's 28-day budget, putting that team under review and delaying a long-planned Gate change. Figure 4.2 shows what 15 minutes did to a month.

{% include diagrams/fig-4-2.svg %}

*Figure 4.2 — The On-Sale team's 28-day error budget through the spring on-sale. Ordinary spending keeps the budget well above the steady burn line; one rule from another team takes 70% in 15 minutes and drops the budget below the policy's 25% line.*

Both teams had a case. On-Sale said a real fan blocked at the door is the worst error the system can make, and that it had paid for someone else's change. Bot Screening said a block is no error at all but the system doing its job, and counting blocks as failures would teach the team to let bots through. Each was describing half of a trade-off, which is why disputes between careful people are so hard to settle.

The resolution, brokered by the Reliability team over two meetings, had three parts. The journey SLO stayed as it was, because fans do not care which team blocked them. The policy now attributes consumption: the review regime applies to the team whose change caused the burn, so it was Bot Screening that went under review. And Bot Screening gained an SLI of its own, a **false-block rate**, the share of sessions blocked that later pass a human challenge, with an objective of no more than one in a thousand admitted sessions. New rules now run in shadow mode, logging what they would have blocked, through one on-sale before enforcing. Nobody thought to ask the same question of the rules already in force, an omission that will matter in Chapter 12.

The argument still happened, but it was about which numbers to count and who owns them, which is an argument with an end, rather than about who was to blame, which has none.

**Recap.** The budget is arithmetic and the policy is an agreement, written in calm weather, about how teams share a scarce allowance of failure. Budgets are meant to be spent, and unspent ones create promises nobody made. When a dependency spends another team's budget, the answer is attribution and a new indicator for the dependency.

**Exercise 4.3.** Draft a one-page error budget policy for a journey you own: thresholds, what changes at each, who grants exceptions and how a burn caused by another team is attributed. Then ask that team to read it.

### 4.4 Alerting on Burn Rate

#### Fuel flow and the fuel gauge {#watching-the-flow}

An SLO gives a principled answer to the oldest question in operations: when should a human be woken? When the budget is being spent fast enough that waiting until morning would cost more than users will forgive. The **burn rate** says how fast: it is the rate at which a service consumes its error budget, relative to the rate that would exactly exhaust it at the end of the window. A burn rate of 1 spends the budget in exactly one window; a burn rate of 10 spends it in a tenth of one.

Pilots know the difference between level and flow. The fuel gauge says how much is left, but a leak shows up in the fuel flow long before the gauge looks alarming. Budget remaining is the gauge; burn rate is the flow. The analogy breaks because engines burn fuel steadily, while errors arrive in bursts, so a single reading of burn rate is noisy, and the craft of SLO alerting lies in choosing the windows over which to measure it.

Paging whenever the error ratio over the last few minutes exceeds the objective pages constantly, on blips that matter to nobody's monthly budget; paging when the budget has run low pages too late. *The Site Reliability Workbook* works through the designs in between and arrives at **multi-window, multi-burn-rate alerting**: page when the budget is burning fast over a long window *and* is still burning over a short one.

#### The arithmetic {#burn-rate-arithmetic}

For a 30-day window, the Workbook suggests paging if 2% of the budget is consumed in one hour, a burn rate of 0.02 × 720 h ÷ 1 h, or 14.4, at which the whole budget would be gone in 50 hours. It suggests a second page if 5% is consumed in six hours (a burn rate of 6) and a ticket if 10% is consumed in three days (a burn rate of 1).

The long window gives significance; the short window gives timeliness. An hour of data separates a real problem from a burst, but alone it would keep firing for up to an hour after the fix. So each long window is paired with a short one, by convention a twelfth of its length, and both must exceed the threshold; when the bleeding stops, the short window drops below the line within minutes and the page resolves.

| Severity | Budget consumed | Long window | Short window | Burn rate | Budget gone in | Response |
|---|---|---|---|---|---|---|
| Fast burn | 2% | 1 h | 5 min | 14.4 | about 2 days | page |
| Medium burn | 5% | 6 h | 30 min | 6 | 5 days | page |
| Slow burn | 10% | 3 days | 6 h | 1 | 30 days | ticket |

*Figure 4.3 — Multi-window, multi-burn-rate alerting, with the Workbook's parameters for a 30-day budget. Both windows must exceed the threshold, so the alert stops soon after the problem does.*

Encore's windows are 28 days, but the Reliability team kept the Workbook's multipliers, which then mean about 2.1% and 5.4% of budget; nobody's judgment is that precise, and everyone can remember 14.4. For the seat map's 99.9% objective, a burn rate of 14.4 means an error ratio above 1.44%:

```yaml
# seat-map: 99.9% of requests <= 800 ms, rolling 28 days (budget 0.1%)
alerts:
  - severity: page    # fast burn
    when: bad_ratio(1h)  > 14.4 * 0.001  and  bad_ratio(5m)  > 14.4 * 0.001
  - severity: page    # medium burn
    when: bad_ratio(6h)  > 6.0  * 0.001  and  bad_ratio(30m) > 6.0  * 0.001
  - severity: ticket  # slow burn
    when: bad_ratio(3d)  > 1.0  * 0.001  and  bad_ratio(6h)  > 1.0  * 0.001
```

Detection times are the alert's real specification. If the seat map fails completely, the one-hour ratio crosses 1.44% in about 52 seconds. If one request in 50 is slow, the line is crossed after about 43 minutes, by which time the incident has spent about 2% of the budget, exactly as designed. A slow leak is allowed to run a little before it wakes anyone, because a slow leak can afford to. Figure 4.4 follows a partial outage, one seat-map request in ten going bad for 40 minutes, through both windows of the fast-burn rule.

{% include diagrams/fig-4-4.svg %}

*Figure 4.4 — A fast-burn page through one incident. The one-hour ratio decides when the page fires and the five-minute ratio decides when it stops: without the short window, the page would outlast the fix by more than three-quarters of an hour.*

Two limits apply. Burn-rate alerting needs traffic: at a few requests a minute, one failure moves the ratio by whole percentage points, a problem Section 4.5 meets again with small tenants. And it cannot protect an on-sale-window SLO, whose budget would be 2% spent after about a minute of trouble. For major on-sales Encore does not rely on pages at all. The teams and an incident commander are already watching per-fan error ratios over one-minute windows. In the theater, the stage manager calling cues does not wait for the fire alarm; they see trouble as the audience does.

**Recap.** Burn rate measures how fast the budget is being spent, and the right alert watches the flow, not the tank. A long window supplies significance and a short one confirms the problem is still happening. Detection times turn an alert rule into a specification; for event-shaped windows, people watching beat any rule.

**Exercise 4.4.** For one SLO you own, compute the thresholds for the three rows of Figure 4.3 and how long a total outage and a 5% partial outage would take to page. Would your users accept those times?

### 4.5 SLOs Across Dependencies and Teams

#### Composition only subtracts {#composition-only-subtracts}

No service meets its SLO alone. Checkout depends on the Gate, Seat Inventory, Orders & Payments and the PSP, and if each must work for checkout to work, their availabilities multiply. Four hard dependencies at 99.95% each give at best about 99.80%, below the checkout objective before Orders has written a line of its own code. In a serial chain, reliability is never inherited; it is composed, and composition only ever subtracts. Figure 4.5 draws the arithmetic.

{% include diagrams/fig-4-5.svg %}

*Figure 4.5 — The best availability a chain of hard dependencies allows. At 99.95% each, the chain falls through checkout's objective at the second dependency; at 99.99% each, three still leave room for checkout's own failures.*

A sound engineer knows this instinctively: the audience hears the whole chain of microphone, desk, amplifiers and speakers, and a perfect desk cannot redeem a crackling cable. The analogy breaks where it saves us: a sound system cannot sing without its speakers, but a service can often keep its promise when a dependency fails, if it was designed to.

Encore uses two remedies. The first is the rule Ben Treynor and his co-authors set out in "The Calculus of Service Availability" (2017): critical dependencies should be roughly one nine more reliable than the service itself. Encore holds its internal purchase-path services to 99.99%, so three of them multiply to about 99.97%, leaving room inside a 99.9% promise. The second is to make a hard dependency soft. The PSP's contract promises 99.9% per calendar month, which alone would pull a hard-wired checkout below its objective. But since the first outage Encore accepts orders when the PSP is down and charges them later, so a PSP failure no longer fails the fan; the price, a few charges that fail afterwards, is one Finance has agreed to carry. Figure 4.6 shows the result.

| Dependency | Its objective | Hard or soft for checkout | What Encore does when it fails |
|---|---|---|---|
| Sale Gate (admission) | 99.99% internal | hard | admitted fans continue; new admissions pause |
| Seat Inventory (writes) | 99.99% internal | hard | holds fail fast with a clear message |
| Orders & Payments | 99.99% internal | hard | saga resumes from its last step |
| PSP | 99.9% per calendar month, contractual | soft | accept the order, charge later |
| Notifications | 99.9% internal | soft | ticket delivered late, order confirmed now |

*Figure 4.6 — Composing checkout. Hard dependencies multiply and need an extra nine; soft ones are designed out of the product. The PSP row is why the checkout SLO is achievable at all.*

An SLO thereby becomes part of a service's interface. It tells consumers how much to trust a service, as a type signature tells them what to pass, and Encore's service registry shows each service's SLOs beside its API contracts. This is information hiding, in the sense the companion volume took from Parnas, extended to reliability: depend on the promise, because observed behavior is only a coincidence that has lasted so far.

#### Tenants, contracts and small numbers {#tenants-and-contracts}

SaaS tenants add a commercial layer. Self-service venues are promised 99.9% and Professional tenants 99.95%, while the Enterprise tenant, `venue-chain-a`, has a **service level agreement (SLA)**, a contractual promise with consequences: 99.95% per calendar month, with service credits below it. The internal SLO for that silo is 99.97% over a rolling 28 days, because the gap between SLO and SLA is where engineers fix things before anyone writes an invoice.

Small tenants raise a problem of statistics. A venue selling 300 tickets a month would breach a per-venue 99.9% objective with one unlucky fan. Hidalgo's book gives a chapter to the probability involved; the lesson is that an SLO needs enough events to tell signal from chance. Encore measures self-service SLOs per serverless cell of about 50 venues, the unit that fails together, and keeps the per-venue view as a diagnostic for Support.

Every tenant's checkout also passes through the same Seat Inventory, so the core must be at least as reliable as the strongest promise it supports, one more reason it carries an extra nine. Cells limit blast radius, as Chapter 9 will show, but they cannot lift reliability above what the shared core provides.

**Recap.** Serial dependencies multiply, so critical ones need an extra nine or must be made soft by design. Published SLOs belong in a service's interface, and consumers should build on the published promise alone. SLAs sit outside SLOs with room to spare, and low-volume objectives need enough events to mean anything.

**Exercise 4.5.** Draw the dependency chain for your most important journey, mark each dependency hard or soft with its published objective (or "none"), and multiply the hard ones. Does the product leave room for your SLO, and which dependency would you make soft first?

### Kata: The Eight O'Clock Slots

> **Your brief: "Kindred Health."** A telehealth platform runs video consultations with about 2,400 doctors in three EU countries and handles some 6 million consultations a year. Patients book in the app, and 85 insurer and clinic partners book through an API with a contractual 99.9% monthly SLA. A consultation needs the booking service, an external video relay, a national eID login in two of the countries and an insurer eligibility check, and payments go through an external PSP. Every weekday at 08:00 the day's same-day slots open, and in the winter flu season traffic rises 30× for about 40 minutes. Kindred has 35 engineers in six teams, every service carries a 99.99% alert copied from a vendor template, on-call took 58 pages last month, and the clinical lead and product disagree about freezing changes through the flu season.

**Deliverables:**

1. **Journey SLOs** — for booking, joining a consultation, the consultation's video staying usable and partner booking: each SLI as good over valid events, where it is measured, and a target and window agreed with the product owner.
2. **The eight o'clock SLO** — an event-window objective counted per patient, and how people will watch it during the 40 minutes.
3. **Error budget policy** — thresholds, consequences, exceptions, attribution between teams and escalation, on one page.
4. **Burn-rate alert set** — multi-window rules for joining a consultation, with detection times for a total outage and a 3% partial one, replacing the template alerts.
5. **Dependency composition** — the booking and consultation chains, hard and soft dependencies marked and multiplied, and one hard dependency made soft.
6. **Partner SLA and internal SLO** — the objective behind the 99.9% partner SLA, and the reasoning for its margin.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Recognizability | Would a patient, reading each SLI in plain words, recognize it as something they have felt? |
| Honest arithmetic | Are latency objectives ratios, and do the thresholds and detection times check out? |
| Event-shaped thinking | Do the eight o'clock slots have their own window and per-patient counting, or are they diluted into a month? |
| Policy as agreement | Does the policy say what happens at each threshold, and was it written in calm weather? |
| Composition | Does the consultation SLO survive its hard dependencies, including the video relay and the eID login? |
| Paging discipline | Would the new alerts have cut last month's 58 pages without missing what mattered? |

#### Where you now stand

You can now choose indicators from what users experience, state them as ratios that aggregate honestly, give scheduled peaks their own windows, write an error budget policy teams can live with, alert on burn rate and reason about reliability across dependencies and contracts. An SLO can tell us *that* users are suffering; it cannot say *why*. Chapter 5 turns to observability, the craft of asking a running system questions nobody thought to ask in advance.

### References

- Alex Hidalgo — [*Implementing Service Level Objectives*](https://www.oreilly.com/library/view/implementing-service-level/9781492076803/). O'Reilly, 2020.
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne (eds.) — [*The Site Reliability Workbook*](https://sre.google/workbook/table-of-contents/). O'Reilly/Google, 2018 — free online.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Betsy Beyer, Chris Jones, Christof Leng, David Huska, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*, 2nd ed.](https://www.oreilly.com/library/view/site-reliability-engineering/9798341607675/). O'Reilly, 2026.
- Ben Treynor, Mike Dahlin, Vivek Rau, Betsy Beyer — [*The Calculus of Service Availability*](https://queue.acm.org/detail.cfm?id=3096459). ACM Queue, 2017.
- David N. Blank-Edelman (ed.) — [*Seeking SRE*](https://www.oreilly.com/library/view/seeking-sre/9781491978856/). O'Reilly, 2018.
- Charity Majors, Liz Fong-Jones, George Miranda, Austin Parker — [*Observability Engineering*, 2nd ed.](https://www.oreilly.com/library/view/observability-engineering-2nd/9781098179915/). O'Reilly, 2026.
- Michael T. Nygard — [*Release It!*, 2nd ed.](https://pragprog.com/titles/mnee2/release-it-second-edition/). Pragmatic Bookshelf, 2018.

---

## Chapter 5: Observability — Seeing What the System Is Doing {#ch5}

> The data will answer almost any question, but only the ones we think to ask.

In the last days of August 1854, cholera broke out around Broad Street in Soho, and within ten days some five hundred people who lived within a few hundred yards of one another were dead. The prevailing theory, held by most physicians and the authorities, was miasma: disease rose from the foul air of a crowded city. John Snow, a London physician better known for giving chloroform to Queen Victoria at the birth of Prince Leopold the year before, had argued since 1849 that cholera travelled in water. He did not argue the point again. He obtained the register of deaths, walked the streets asking where each victim had drawn water, and marked every death as a small bar against its address on a map.

The map made a new question answerable. The deaths clustered around the public pump on Broad Street, and the exceptions were the most persuasive evidence of all. The workhouse on Poland Street had its own well and very few deaths. The men at the Broad Street brewery drank the beer they were allowed and water from the brewery's own well, and they were spared. A widow in Hampstead, miles away, who had moved from the district but liked the taste of Broad Street water enough to have a bottle carried to her daily, died of it. On 7 September Snow put his case to the parish Board of Guardians, and the next day the pump's handle was removed. The outbreak was already waning, as Snow acknowledged, and official opinion stayed unconvinced for years. The most patient investigator was Henry Whitehead, curate of St Luke's on Berwick Street, who set out to disprove Snow, interviewed his parishioners one by one, and found what the map had pointed to: a baby at 40 Broad Street whose soiled napkins had been rinsed into a cesspool a few feet from the well. Snow published the map in the second edition of *On the Mode of Communication of Cholera* in 1855.

What Snow did is what this chapter is about. He had no better instruments than the miasma theorists, only the same deaths, streets and registers. He asked the data a question the prevailing theory did not think worth asking, and he arranged the data so that it could answer. The companion volume borrowed *observability* from Rudolf Kálmán's control theory; here we take it in its working sense, the ability to ask a production system an unanticipated question and get an answer without shipping new code.

Encore has telemetry everywhere: metrics from every service, spans from the mesh, logs that fill a bill Chapter 6 will read closely, and an on-sale dashboard with more panels than anyone has looked at in one sitting. The question is whether Encore can *see*: whether, when something new goes wrong, its engineers can find out why before its fans find out that it has.

### 5.1 From Monitoring to Observability

#### Known questions and unknown ones {#known-and-unknown-questions}

**Monitoring** is the practice of checking a system against conditions we decided in advance were worth checking: is the error rate above 1%, is the disk 90% full, did the synthetic buyer complete its purchase. It is indispensable, and its strength is its limit: a monitor encodes a failure someone has already imagined. **Observability**, in the software sense, is the property of a system that lets us understand its internal state from its outputs well enough to answer questions *nobody* thought of in advance.

The distinction matters more now, because the failures that hurt have changed shape. A monolith on three servers failed in ways an experienced operator could list. Encore's purchase path crosses a serverless admission edge, a bot screen, an event-sourced inventory sharded four ways, a saga orchestrator and an external payment service provider (PSP), across two regions and a mesh. Nobody can list the ways those parts combine, and so the failures that page us at 3 a.m. are increasingly ones nobody has seen before. Cindy Sridharan's 2018 report named the type: partial, gray failures, in which nothing is down and something is wrong for some users. Monitoring is excellent at "down"; it is close to useless at "some".

Monitoring is the warning lights on a car's dashboard, observability the mechanic's workshop. The lights cover the conditions the manufacturer anticipated, and we would be foolish to drive without them; when the car makes a noise that matches none of them, no number of extra lights will substitute for opening the engine. The analogy breaks instructively: a car's engine does not change between visits, whereas Encore deploys dozens of times a day, so the mechanic always faces an engine slightly different from the manual.

#### What observability is made of {#what-observability-is-made-of}

The ability to ask new questions comes not from a tool but from three properties of the telemetry itself. The data must be **high in cardinality**, meaning a field may take very many distinct values (a fan's order ID, an `event_id`, a build hash), because the interesting failures are usually specific to one of them. It must be **high in dimensionality**, carrying many fields per event, because we do not know in advance which field will turn out to explain the difference. And it must be **explorable**, kept so that we can slice, group and compare by any field after the fact instead of only through pre-built views.

Snow's register had exactly these properties: one row per person, with an address, a date and, after his door-knocking, a water source. The miasma theorists' summary, deaths per district per week, had thrown away the address, and with it the pump. Aggregation is a decision about which questions will never be asked again, and we usually make it before we know what they are.

**Recap.** Monitoring checks known conditions and remains necessary; observability lets us ask about conditions nobody anticipated. The gray, partial failures of distributed systems belong to the second kind. Observability comes from telemetry that is wide, high in cardinality and explorable, not from the name of the product that stores it.

**Exercise 5.1.** List the last five production problems in a system you know. For each, note whether an existing monitor detected it, and whether the cause was found using pre-built views or by asking a question the views could not answer.

### 5.2 Signals and Instrumentation with OpenTelemetry

#### Braided signals {#braided-signals}

For a decade the industry described telemetry as "three pillars" (metrics, logs and traces), each with its own agent, pipeline and often vendor. The metaphor did harm, because pillars stand apart, and the value of telemetry lies in the connections between signals. A latency spike is the symptom, that minute's traces the evidence, the log line in the slowest span the testimony. Ted Young and Austin Parker, in *Learning OpenTelemetry*, prefer the image of a braid, and it is the better one: what holds the weight is shared context, the same trace ID, resource attributes and names for the same things.

**OpenTelemetry** (OTel) is the vendor-neutral standard that makes the braid practical. It formed in 2019 from the merger of OpenTracing and OpenCensus, when the industry had two good answers and needed one. OTel separates an API, against which code and libraries are instrumented, from a software development kit (SDK) that decides where the data goes. A library can therefore be instrumented natively, and the service using it decides in configuration where, if anywhere, the spans go. The signals it defines are traces, metrics and logs, with continuous profiles arriving as a fourth.

#### Semantic conventions as a shared vocabulary {#semantic-conventions}

The least glamorous part of OpenTelemetry is the most important. The **semantic conventions** are agreed names and meanings for common attributes: `service.name` and `service.version` on every resource, `http.request.method` and `http.response.status_code` on every HTTP span, and so on through databases, messaging and, more recently, generative AI calls. A query is only as good as its vocabulary. If Orders records the HTTP status as `status`, Inventory as `http_code` and the Gate as `response.status`, then "show me every 5xx on the purchase path" is three queries, and in the middle of an incident it is usually zero.

Encore extends the conventions with its own namespace, owned by the Reliability team and kept in a registry checked by continuous integration (CI). Every span on the purchase path carries `encore.event_id`, `encore.tenant_id`, `encore.shard`, `encore.cell` and `encore.on_sale` (set by the Gate during a scheduled on-sale), added by the golden-path service template. This is information hiding in a new place: the registry puts the names behind a contract, so a query written by one team keeps working against a service written by another.

#### The Collector and the economics of sampling {#collector-and-sampling}

Between the services and the backends sits the **OpenTelemetry Collector**, a pipeline of receivers, processors and exporters. Encore runs it in two tiers: agents on every Kubernetes node and beside each serverless function, which batch and forward, and a gateway tier that does the expensive work. The gateway strips what must never be stored, such as a fan's email address that a careless log statement put into a span, routes security events to their own account, and makes the decision that dominates the bill: what to keep.

**Head sampling** decides at the start of a request whether its trace will be recorded, typically by a fixed probability, and propagates that decision downstream. It is cheap, and blind, because at that moment nobody knows whether this request will be the interesting one. **Tail sampling** waits until a trace is complete, then decides with the whole trace in view. It can keep every error, every slow checkout and a thin baseline of the ordinary, at the price of buffering spans and routing each trace to one gateway instance, which Encore does with a load-balancing exporter keyed on trace ID. The policy looks like this:

```yaml
processors:
  tail_sampling:
    decision_wait: 30s
    policies:
      - name: keep-errors
        type: status_code
        status_code: { status_codes: [ERROR] }
      - name: keep-slow-checkouts
        type: latency
        latency: { threshold_ms: 2000 }
      - name: baseline
        type: probabilistic
        probabilistic: { sampling_percentage: 10 }
```

During an on-sale, at 1,200 admissions a second per event, a separate policy lowers the baseline for successful admissions to 1%. Encore's telemetry costs about €40,000 a month, roughly 2 cents of every ticket's 12, and its retention is a set of deliberate choices: full-detail events for 14 days, sampled traces for 30 and metrics for 13 months, long enough to compare this year's festival on-sale with last year's. Sampling is the same decision as aggregation, made with a budget. Made well, it keeps every row Snow would have wanted and only a sample of the streets where nothing happened. Figure 5.1 draws the whole pipeline.

{% include diagrams/fig-5-1.svg %}

*Figure 5.1 — Encore's telemetry pipeline. Agents only batch and forward; the gateway tier redacts, routes and, in the tail sampler, decides what the bill will be.*

**Recap.** Signals earn their value through shared context, which is why OpenTelemetry treats them as a braid. Semantic conventions, extended by an owned registry, make queries portable across teams. The Collector is where telemetry is cleaned, routed and sampled, and tail sampling lets us keep the interesting traces because it decides after the story is known.

**Exercise 5.2.** Pick three services you depend on and find what each calls the HTTP status, the tenant or customer, and the deployed version. How many distinct names did you find for each, and which incident query would have failed because of them?

### 5.3 Distributed Tracing in Practice

#### One fan's purchase {#one-fans-purchase}

A **trace** is the record of one request's journey through a system, as a tree of **spans**, each span a timed unit of work with a name, a parent and attributes. Google's Dapper paper of 2010 described it at scale, Twitter's Zipkin and Uber's Jaeger brought it into open source, and OpenTelemetry is its present form.

Here is one fan's purchase on an ordinary Thursday:

| Span | Service | Start (ms) | Duration (ms) | Notable attributes |
|---|---|---|---|---|
| `POST /checkout` | API gateway | 0 | 1,140 | `encore.event_id=evt_7f3a`, `encore.tenant_id=encore` |
| `admission.verify` | Sale Gate | 4 | 12 | token valid, queue wait in linked trace |
| `bot.score` | Bot Screening | 18 | 35 | `bot.verdict=allow` |
| `inventory.Hold` (gRPC) | Seat Inventory | 56 | 48 | `encore.shard=2`, `seat.count=2` |
| `saga.purchase` | Orders | 108 | 1,020 | Temporal workflow |
| ↳ `psp.authorize` | Orders (anti-corruption layer) | 150 | 640 | `payment.method=card`, `psp.attempt=1` |
| ↳ `inventory.Sell` | Seat Inventory | 830 | 31 | appends `SeatSold` |
| `ticket.issue` | Notification | +4,200 | 380 | linked from `SeatSold`, not a child |

*Figure 5.2 — One fan's purchase as a trace. The PSP takes 640 ms of its 800 ms share of the 3 s checkout budget; ticket issuance runs asynchronously and is joined to the purchase by a span link.*

Drawn to scale, as in Figure 5.3, the same trace shows at a glance where the fan's second went.

{% include diagrams/fig-5-3.svg %}

*Figure 5.3 — The trace of Figure 5.2 as a waterfall, against the 3 s budget. The PSP call is most of the saga and most of the checkout; ticket issuance, four seconds later, hangs off the purchase by a link rather than stretching it.*

Three things in this table took deliberate work.

#### Context propagation {#context-propagation}

A trace exists only because each hop passes the trace context to the next. Over HTTP and gRPC that context travels in the `traceparent` header standardized by the World Wide Web Consortium (W3C) as Trace Context, and OpenTelemetry reads and writes it automatically. The mesh can record spans for every hop, but it cannot carry context *through* a service: if Orders makes an outbound call on a fresh thread without passing the context along, the trace breaks in two. As Yuri Shkuro, who built Jaeger at Uber, makes clear, the hard part of tracing was never storage but getting every hop, through every thread pool and callback, to carry a few bytes of context. One broken link hides everything downstream, so Encore's service template includes a test that fails the build if an outbound call loses its parent.

The same context can carry **baggage**, key-value pairs that ride along with the trace. Encore puts `encore.event_id` and `encore.tenant_id` in baggage at the gateway so that every service can stamp them on its spans. Baggage is visible to every hop, so it holds identifiers, never secrets or personal data.

#### Span design {#span-design}

What deserves a span is the tracing version of what deserves a function, and the answer is similar: a unit of work someone might reason about on its own. One span per method produces a trace too deep to read and too expensive to keep; one span per service hides the PSP call inside the saga, where nobody can see that it took 640 ms. Encore's rule is a span for every network call, every queue publish and consume, every lock or lease, and every decision that changes the request's path (a bot verdict, a cache miss, a retry), and *attributes* for everything else. A span with 30 well-named attributes is worth more than ten spans with none, because the attributes are what we will later group by.

#### Queues, sagas and asynchronous work {#async-tracing}

The last row of Figure 5.2 is the hard case. The `SeatSold` event leaves Seat Inventory on the `ticket-sales.v2` stream, and Notification consumes it four seconds later. Made a child of the checkout span, `ticket.issue` would make the checkout appear to take five seconds; started as an unconnected trace, it would leave the fan who says "I paid and never got my ticket" unfollowable across the gap. OpenTelemetry's answer is the **span link**: the producer writes the trace context into the event's headers, and the consumer starts its own trace whose first span *links* to the producer's span without claiming it as a parent. The same device joins a fan's seven minutes in the waiting room to the purchase that follows, and the Finance ledger's batch to the hundreds of `SaleCompleted` events it reads.

A Temporal saga may also pause for a PSP callback and resume minutes later on a different worker, so Encore records each activity as its own span and carries the workflow ID as an attribute on all of them. Tracing an asynchronous system is like following a suitcase rather than its traveller: it changes hands, waits on carousels and sometimes takes another flight, and only the tag on the handle ties its journey together.

**Recap.** A trace is only as complete as its weakest propagation point, so propagation is tested in the build. Spans mark units of work worth reasoning about, and attributes carry the detail we will query. Asynchronous hops are joined by span links, which keep latency honest while keeping the journey followable.

**Exercise 5.3.** Follow one real request in a system you know from entry to its last asynchronous consequence. Mark each place where the trace breaks or lies about duration, and name the fix: propagation, a span link or an attribute.

### 5.4 Dashboards, Alerts, and Paging Discipline

#### Dashboards that argue {#dashboards-that-argue}

In 1858 Florence Nightingale drew the deaths of British soldiers in the Crimean War as wedge-shaped monthly diagrams in which deaths from preventable disease dwarfed those from wounds. It was a chart with a thesis, an argument to people who would never have read the tables, and it changed how the army cared for its sick.

A good dashboard has a thesis too. Encore's on-sale dashboard answers one question, "are fans getting through and buying?", and so its top row is admissions per second against the admission rate, checkout success against the on-sale-window service level objective (SLO) from Chapter 4, and p99 checkout latency against the 3 s budget. Most dashboards are the opposite, walls of graphs accumulated after each incident. A dashboard is a set of answers to questions someone asked last year, valuable when those questions recur and misleading when they do not, because a wall of green panels persuades tired people that they are seeing the whole system. Encore asks each dashboard to name its question and its owner, and deletes those unopened for 90 days.

#### What deserves a page {#what-deserves-a-page}

Chapter 4 built the mechanics of alerting on burn rate; what remains is the discipline around it. An alert is a request for a human being's attention, and attention is the one resource no autoscaler can add. Every page should be urgent, affect users or be about to, and need a human judgment. The companion volume stated the rule as paging on symptoms, not causes, with narrow exceptions for causes that make harm certain. In practice the rule needs one refinement: a cause is worth a page when it predicts a symptom more reliably and earlier than the symptom itself could be measured. A certificate expiring in six hours qualifies, and so does the seat ledger's cross-region standby becoming unreachable during an on-sale, since every seat write depends on it. CPU at 85% does not, because it predicts nothing on its own.

| Signal | Destination | Example at Encore |
|---|---|---|
| SLO fast burn | Page, immediately | Checkout error budget burning at 14× its sustainable rate |
| SLO slow burn | Ticket, business hours | Seat-map latency budget 40% spent in 10 days |
| Predictive cause, harm certain | Page | Certificate expiry under 24 h; ledger standby unreachable |
| Ordinary cause | Dashboard only | CPU, pod restarts, queue depth within capacity |
| Business anomaly | Owning team's channel | Sales for one event far below forecast |

*Figure 5.4 — Where signals go. Only the first and third rows wake anyone; the rest wait for daylight or for a question.*

#### Alert fatigue {#alert-fatigue}

Hospitals learned this cost before software did. Monitors that beep at every transient reading teach nurses, entirely rationally, that beeps do not mean danger, and real alarms are then missed. The Joint Commission, which accredits American hospitals, issued a formal warning about alarm fatigue in 2013. An engineer paged nightly for causes that resolve themselves learns the nurse's lesson. The parallel breaks where software has the advantage: a hospital cannot delete the monitor on a patient's heart, but we can delete an alert, and most teams delete far too few.

When Encore's Orders team reviewed its alerts last year, it had 130 rules, of which 40 could page. Over a quarter, only 11 of those had led to any human action. Just two had caught something before a fan noticed. The team kept 12 pages, each with a runbook link, and demoted the rest. The Reliability team now reviews every rotation's pages monthly with one question: what did the person who was woken actually do? An alert whose honest answer is "acknowledged it and went back to sleep" has already been deleted by the engineer; the configuration simply has not caught up.

**Recap.** Dashboards should make an argument, name their question and be pruned when the question no longer recurs. A page is a claim on human attention and must be urgent, user-affecting and actionable, with predictive causes allowed when they warn earlier than the symptom could. Alert fatigue is treated by deletion, reviewed regularly against what responders actually did.

**Exercise 5.4.** Export a month of pages from a rotation you know. For each alert rule, record what the responder did. Propose deleting or demoting every rule whose answer was "nothing", and estimate the sleep it returns.

### 5.5 Asking Questions — High Cardinality, Exploration, and AI-Assisted Queries

#### Wide events {#wide-events}

The telemetry that makes new questions answerable is, in its simplest form, the **wide event**: one structured record per unit of work, per request per service, carrying every field that might matter, often a hundred or more. A checkout event at Encore carries the fan's country, the `encore.*` identifiers, the payment method, the PSP route, the build, the region, the feature flags in effect, the retry count and each step's duration. Charity Majors, Liz Fong-Jones and George Miranda, in *Observability Engineering*, argue that such events, of which trace spans are one linked form, are the fundamental unit of observability, and that metrics are best understood as a cheap aggregate derived from them. The argument has a cost, which Section 5.2 priced, and the merit of keeping the address in the register.

#### The core analysis loop {#core-analysis-loop}

The same authors describe a method they call the **core analysis loop**: start from the signal that something is wrong, isolate the requests that show it, compare them with those that do not across every dimension at once, and let the dimensions that differ most suggest the next filter, then repeat. It is Snow's method made mechanical. He did not test hypotheses one at a time; he laid every death against every address and let the cluster and its exceptions tell him where to look.

On a Tuesday afternoon in March, Encore's support team relayed a pattern from fans: payments from the Netherlands were "hanging" after the bank page. The checkout SLO barely moved, since Dutch fans are a small share of traffic. The on-call engineer's first instinct, and the instinct of the incident channel, was the PSP, which had been the suspect since Encore's first outage and was the obvious miasma of the purchase path. But the `psp.authorize` spans were normal, about 180 ms. So she ran the loop instead: select checkouts slower than 3 s since 13:00, compare them with the rest. The slow ones began abruptly at 14:02.

| Dimension | Slow checkouts (since 13:00) | All other checkouts |
|---|---|---|
| `client.country=NL` | 81% | 6% |
| `payment.method=bank_redirect` | 97% | 14% |
| Time in `saga.await_callback` | 38 s (median) | 2.1 s (median) |
| `gateway.rule_matched=psp-callback-ratelimit` | 95% | under 1% |
| `encore.tenant_id`, `encore.shard`, `service.version` | no difference | — |

*Figure 5.5 — The core analysis loop on "Dutch fans' payments slow since 14:02". Country was the symptom; the payment method was the mechanism; the gateway rule was the cause.*

Most Dutch fans pay by bank redirect, in which the bank confirms the payment by a callback from the PSP rather than in the original request. At 14:02 the Bot Screening team had shipped a reasonable change to the API gateway, a per-source rate limit on unauthenticated POSTs, and the PSP's callbacks arrive from a handful of addresses. They were throttled, retried with backoff and delivered tens of seconds late while fans watched a spinner. The fix, an exemption for the PSP's signed callbacks, took four minutes once the cause was known. Finding it took 25 minutes, nearly all of them spent on the theory everyone already held. A rule meant to stop bots had quietly begun to punish ordinary retry behavior, an interaction this book will meet again.

None of the fields in Figure 5.5 would survive in a metric with a label budget, and the decisive one, the gateway rule name, existed only because someone had once decided that every policy decision deserved an attribute.

#### Asking Cue {#asking-cue}

Cue, Encore's read-only operations assistant, queries telemetry through the company's Model Context Protocol (MCP) server, and the March investigation was later replayed with it. Asked "why are Dutch payments slow since 14:02?", Cue answered in seconds, fluently, and wrongly. It found the elevated latency, found two postmortems blaming the PSP, and concluded that the PSP was degraded for Dutch banks. Its answer was the miasma theory with citations. Asked instead to "compare checkouts slower than 3 s since 13:00 with the rest, across all attributes, and list the largest differences," it ran the core analysis loop faster than any human could have and returned Figure 5.5 almost exactly.

Two limits follow. The first is that a confident wrong answer is more expensive than a slow right one, because it ends the search. A model that reasons from past incidents reproduces the team's prevailing theory fluently, exactly when a Snow is most needed, so Encore asks Cue for comparisons and queries it can show, not for diagnoses, and treats any answer without the query behind it as a rumor. The second is that the assistant is only as good as the vocabulary of the telemetry. In the replay, Cue's first attempt missed the gateway rule because the gateway called it `policy` while the registry said `gateway.rule_matched`; one inconsistent name made the decisive field invisible. The authors of *Observability Engineering* now argue for an explicit ontology shared by humans and machines, persuasively: a naming slip a human might work around at 3 a.m. is a wall to an assistant that cannot know what it has not been told.

Used this way, an assistant is a tireless research clerk, of the kind Whitehead might have welcomed for knocking on doors, and a poor substitute for the curiosity that chose the doors. Chapter 12 takes up how Cue behaves under the pressure of a live incident, where the same strengths and weaknesses arrive faster.

**Recap.** Wide, high-cardinality events let us compare failing requests with healthy ones on every dimension at once, which is the core analysis loop and Snow's method in one. The prevailing theory is the usual obstacle, and AI assistants tend to repeat it fluently. They are valuable for running comparisons and writing queries, and only as reliable as the semantic conventions beneath them.

**Exercise 5.5.** Take a recent investigation and rerun it as a comparison: the failing requests against the rest, across every attribute you have. Which attribute would have found the cause soonest, and was it present, consistently named and kept long enough?

### Kata: The Charging Network

> **Your brief: "Lumen."** Lumen runs 18,000 electric-vehicle chargers across six countries, with a driver app, roaming partners whose customers charge on Lumen's network, and two PSPs. Sessions pass through authorization, the charger (over cellular), metering and billing. Lumen has 35 engineers, spends €70,000 a month on telemetry (two-thirds of it logs, most never read), defines 600 alert rules and pages its rotation about 90 times a week. Last quarter more than half of failed charging sessions were first reported by drivers on social media, and a roaming partner has threatened to leave over unexplained authorization failures that Lumen's dashboards show as healthy.

**Deliverables:**

1. **Attribute registry** — the 15 attributes every span and event must carry (charger, site, firmware, roaming partner, country among them), with names aligned to the OpenTelemetry semantic conventions.
2. **Trace design** — one charging session traced from app tap to invoice, with the asynchronous hops joined by span links, and the propagation points that are most likely to break.
3. **Pipeline and sampling policy** — Collector topology, tail-sampling rules, redaction of driver data, and a retention plan that cuts telemetry spend by a third, with the questions each cut makes unanswerable.
4. **Paging set** — at most ten pages, each tied to an SLO burn or a predictive cause, with the deleted rules listed and the reason for each deletion.
5. **Investigation script** — the core analysis loop applied to the roaming partner's complaint, showing which dimensions you would compare and why.
6. **Assistant policy** — what an AI query assistant may do with Lumen's telemetry, and what evidence its answers must show.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Askability | Could an engineer answer "which firmware on which partner's chargers fails authorization since Tuesday?" with one query? |
| Vocabulary | Are names consistent across services, owned, and checked by CI rather than by goodwill? |
| Honest sampling | Does the policy keep every failure and say plainly what the cuts give up? |
| Respect for attention | Would you accept being woken by each page on the list? |
| Method over theory | Does the investigation compare failing with healthy sessions before it names a suspect? |
| Grounded assistance | Must the assistant show its query, and can a human rerun it? |

#### Where you now stand

You can now design for observability: wide events with an owned vocabulary, traces that survive queues and sagas, a pipeline that samples with intent, dashboards that argue and pages that respect sleep. You can run the core analysis loop and judge an assistant that runs it for you. What the telemetry has begun to show, in latency curves that bend under load and a bill that tracks traffic, is the subject of Chapter 6: performance, capacity and cost, and the queues that Erlang first learned to count.

### References

- Charity Majors, Liz Fong-Jones, George Miranda — [*Observability Engineering*, 2nd ed.](https://www.oreilly.com/library/view/observability-engineering-2nd/9781098179915/). O'Reilly, 2026.
- Ted Young, Austin Parker — [*Learning OpenTelemetry*](https://www.oreilly.com/library/view/learning-opentelemetry/9781098147174/). O'Reilly, 2024.
- Yuri Shkuro — [*Mastering Distributed Tracing*](https://www.oreilly.com/library/view/mastering-distributed-tracing/9781788628464/). Packt, 2019.
- Cindy Sridharan — [*Distributed Systems Observability*](https://www.oreilly.com/library/view/distributed-systems-observability/9781492033431/). O'Reilly, 2018.
- Mike Julian — [*Practical Monitoring*](https://www.oreilly.com/library/view/practical-monitoring/9781491957349/). O'Reilly, 2017.
- Phillip Carter — [*Observability for Large Language Models*](https://www.oreilly.com/library/view/observability-for-large/9781098159757/). O'Reilly, 2023.
- Benjamin H. Sigelman et al. — [*Dapper, a Large-Scale Distributed Systems Tracing Infrastructure*](https://research.google/pubs/dapper-a-large-scale-distributed-systems-tracing-infrastructure/). Google Technical Report, 2010 — free online.
- OpenTelemetry Authors — [*OpenTelemetry Semantic Conventions*](https://opentelemetry.io/docs/specs/semconv/). OpenTelemetry project — free online.
- W3C — [*Trace Context*](https://www.w3.org/TR/trace-context/). W3C Recommendation — free online.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- John Snow — [*On the Mode of Communication of Cholera*, 2nd ed.](https://archive.org/details/b28985266). John Churchill, 1855 — free online.
- Steven Johnson — [*The Ghost Map*](https://www.penguinrandomhouse.com/books/295522/the-ghost-map-by-steven-johnson/). Riverhead Books, 2006.

---

## Chapter 6: Performance, Capacity, and Cost {#ch6}

> Every queue is a wager that the future will be less busy than the present.

In 1908 a young Danish mathematician named Agner Krarup Erlang joined the Copenhagen Telephone Company, and the company asked him a question that sounds like bookkeeping and turned out to be a science: how many lines, and how many operators, does a city need? Too few, and callers hear a busy tone; too many, and copper and wages sit idle through every quiet afternoon. In his paper of 1909, Erlang showed that calls arriving independently from many subscribers follow a Poisson distribution, so that the randomness of a city's telephone traffic could be described exactly enough to engineer against. By 1917 he had derived formulas for the chance that a call would be refused when every line was busy, and for how long it would wait when the system held callers in line instead of refusing them. Queueing theory begins there, with a man counting calls.

The profession honored him in the usual way, by turning his name into a unit. One **erlang** is the traffic that keeps one server continuously busy, and the offered load of any system, in erlangs, is its arrival rate multiplied by the mean time each arrival holds a server. A switchboard offered 30 erlangs needs more than 30 lines, and how many more depends on how long callers will tolerate waiting; that sentence is this chapter in miniature. Performance is how long each request holds a server, capacity is how many servers we provide, and cost is what we pay for them; the three are one problem viewed from three chairs, and Erlang was the first to write it down as mathematics.

Encore has met all three. The companion volume left it with a Sale Gate that admits about 1,200 fans per second per event, a Seat Inventory sharded four ways for large events, and a cost per ticket that once drifted from €0.11 to €0.19 before an engineer moved a metrics forwarder off serverless functions. Chapter 4 gave us the service level objectives (SLOs) and Chapter 5 the instruments. This chapter asks how fast the system is, how close it runs to its ceilings, how it grows when demand arrives, and what each fan's evening costs.

### 6.1 Performance Methodology — USE, RED, and Latency Distributions

#### Two checklists, two points of view {#two-checklists}

Most performance investigations fail because they begin with a hunch. Someone suspects the database, so we look there, find something mildly alarming (there always is), tune it, and wait. Brendan Gregg catalogued these habits as *anti-methods*: the streetlight method, which looks where the light happens to be, and the random-change method, which turns knobs until the symptom wanders off. Both let the investigator's attention, rather than the system, decide where to look.

The cure is a method that covers the system regardless of hunches. Gregg's **USE method**, which he published in 2012, asks three questions of every resource: its **utilization** (the fraction of time it was busy), its **saturation** (how much work is queued waiting for it) and its **errors**. Resources are anything that can run out: processors, memory, disks and network interfaces, but also connection pools, file descriptors and the ordered write log of a Seat Inventory shard. The method is deliberately dull, and exhaustive in a fixed number of steps, so it finds the problem we did not suspect.

USE looks at the system from the machine's side. Tom Wilkie's **RED method** looks from the request's side, asking of every service its **rate** (requests per second), its **errors** (failed requests per second) and its **duration** (the distribution of time each request takes). RED is what a user would measure if a user could measure, and it maps cleanly onto the service level indicators (SLIs) of Chapter 4. The two are complementary in the way a physician's questions and a nurse's chart are complementary: RED says the patient feels unwell and where it hurts, USE says which organ is struggling. An Encore engineer paged on a seat-map burn rate begins with RED for the seat-map service, then walks USE down the resources behind it.

#### Latency is a distribution {#latency-is-a-distribution}

Duration is the signal most often mismeasured, because it is not a single number. A service's latency is a distribution, usually skewed and often with two humps for cache hits and misses, and the **percentile** pN is the value below which N% of requests completed. A seat-map service whose mean is 120 ms can have a p99 of 2 s, and the fan who waited 2 s does not experience the mean. Figure 6.1 draws such a service. An average is a number that describes no one's evening.

{% include diagrams/fig-6-1.svg %}

*Figure 6.1 — A seat-map service's latency, on a log scale. The mean falls in the valley between the cache hits and the misses, where almost no request lands; the p99 lives in the misses' long tail.*

Two habits follow. First, percentiles do not aggregate: the p99 of a service is not the average of its pods' p99s, and no arithmetic on summary percentiles recovers it. We keep histograms and compute percentiles from the merged buckets. Second, we look at the tail in proportion to the fan-out. A purchase that touches 20 backends sees each backend's p99 far more often than once in a hundred (the arithmetic of "The Tail at Scale" from the companion volume), so the backend's p99 is the purchase's median problem.

There is a subtler trap, which Gil Tene named **coordinated omission**: a measurement error in which the load generator, or the instrumented client, waits for each response before sending the next request, so that when the system stalls, the requests that *would* have arrived during the stall are never sent and never measured. The stall appears in the data as one slow request instead of hundreds. A closed-loop benchmark can report a p99 of 40 ms for a system that froze for 2 s, because it politely stopped asking. Real fans, like Erlang's callers, arrive at their own pace, and our measurements must be taken the same way.

**Recap.** Methods beat hunches because they cover the system whether or not we suspected the right part. RED describes what requests experience and USE describes what resources endure, and an investigation usually moves from the first to the second. Latency is a distribution, measured with histograms, read at the percentile that matches the fan-out, and taken from load that arrives on its own schedule.

**Exercise 6.1.** For one service you own, list every resource the USE method should cover, including pools and logical limits. For how many can you produce all three of utilization, saturation and errors today? Then check whether your latency percentiles are computed from merged histograms or averaged across instances.

### 6.2 Queues, Load, and the Universal Scalability Law

#### The hockey stick {#the-hockey-stick}

Erlang's deepest lesson lies less in his formulas than in the shape they draw. When requests arrive at random and take varying times to serve, a server that is busy only part of the time still makes some of them wait, and the wait grows faster than the load. For the simplest model (random arrivals, random service times, one server), the mean response time is the service time divided by one minus the utilization. At 50% utilization a request takes twice its service time; at 80%, five times; at 90%, ten; at 95%, twenty. At 99%, a hundred. The curve is flat for a long while and then turns upward like the blade of a hockey stick, and real systems, which differ from the model in every detail, share its shape.

J. F. C. Kingman sharpened the point in 1961: for a single server under heavy load, the expected wait scales with the variability of both arrivals and service times as well as with ρ/(1−ρ). A system comfortable on a dashboard of averages can therefore collapse during an on-sale, whose arrivals are as bursty as traffic gets. Utilization is what the machine feels; queueing delay is what the fan feels, and the two part company precisely where the business is busiest. Figure 6.2 draws both curves.

{% include diagrams/fig-6-2.svg %}

*Figure 6.2 — Response time against utilization for one server with random arrivals, and the steeper curve that burstier arrivals draw. Encore's write shards are planned at 80%; the same curve explains why a hot shard at 96% hurts so much more than 16 points should.*

Anyone who has driven a motorway at rush hour knows the curve. Traffic flows freely at moderate density, and then a few more cars per minute turn a road into a car park, though nothing about the road has changed. Many cities answer with ramp metering, a traffic light on the on-ramp that admits cars at the rate the motorway can absorb, which keeps the main road below its knee at the cost of a short, visible wait on the ramp. The Sale Gate is a ramp meter, and its 1,200 fans per second is the green-light interval. The analogy breaks in one useful place: a driver held at the ramp cannot leave and return a minute later as a second car, whereas a fan refused by a busy service can and does retry, which adds load at exactly the moment the system can least absorb it. Chapter 9 takes up what retries do to a queue.

Erlang's later formulas carry one more lesson worth keeping. For the same utilization, a pool of many servers keeps its waits far shorter than a single server does, because an idle server somewhere can usually take the next arrival. Pooling is the oldest economy of scale in capacity planning, and it is why ten small pools need more total headroom than one large one, a cost worth remembering whenever we carve capacity into cells for blast radius.

#### How far will it scale? {#how-far-will-it-scale}

Queueing describes one resource. Scaling asks what happens when we add more of them, and here Neil Gunther's **Universal Scalability Law** (USL) is the most useful small model we have. It describes relative capacity C(N) at concurrency N (threads, nodes, workers) with two penalties:

```
C(N) = N / (1 + σ(N−1) + κN(N−1))
```

The **contention** coefficient σ is the fraction of work that must be serialized, the cost of waiting for a shared resource; with κ at zero the law reduces to Amdahl's law of 1967, and throughput approaches a ceiling of 1/σ. The **coherency** coefficient κ is the cost of keeping parallel workers consistent with one another, which grows with the number of pairs of workers; it is what makes throughput not merely flatten but *fall* as N grows past √((1−σ)/κ). Gunther calls this retrograde scaling: adding capacity removes capacity.

Seat Inventory gives us an honest example. Each shard leader appends seat writes to a single ordered log, which is pure contention: whatever the concurrency, one append at a time. Concurrent hold requests for the same popular seats must also check one another's fenced terms and versions, and when they collide, one retries, which is coherency. The Inventory team fitted the USL to a single-shard load test by regressing measured throughput at six concurrency levels:

| Concurrent writers N | Measured writes/s | USL fit (σ 0.03, κ 0.0005) |
|---|---|---|
| 1 | 121 | 120 |
| 4 | 431 | 438 |
| 8 | 790 | 775 |
| 16 | 1,210 | 1,223 |
| 32 | 1,570 | 1,583 |
| 64 | 1,540 | 1,565 |

*Figure 6.3 — The USL fitted to one Seat Inventory shard. Peak throughput falls near 44 concurrent writers; beyond that, more concurrency buys less.*

The fit, drawn in Figure 6.4, says three useful things. The shard peaks at roughly 1,630 writes/s near 44 writers, so the published 1.5k writes/s is a measured ceiling with a little margin. Raising the concurrency cap above 32 gains almost nothing and, past 64, loses throughput, so the cap belongs in configuration review. And growing write capacity materially means more shards per event, a design change that no tuning knob can stand in for. A model fitted to six points is only a sketch, and Gunther himself would ask us to refit it whenever the code changes; but a sketch that predicts the knee is worth more than a spreadsheet that assumes linearity.

{% include diagrams/fig-6-4.svg %}

*Figure 6.4 — The USL fit of Figure 6.3 against linear scaling and Amdahl's law. Contention alone would bend the curve; coherency turns it over, and the concurrency cap of 32 sits just below the peak.*

**Recap.** Response time rises with utilization along a hockey stick, steepened by variability, so we keep utilization well below the knee where waits matter. Pooling reduces waiting, and admission control keeps a system below its knee at the cost of a visible queue. The USL separates contention from coherency, predicts where scaling stops and reverses, and turns a handful of load-test points into a capacity ceiling we can defend.

**Exercise 6.2.** Run a load test against one component at four to six concurrency levels and fit the USL to the results (a spreadsheet's solver will do). Where does the model put the peak, and is your current concurrency setting on the rising or the falling side of it?

### 6.3 Capacity Planning and Load Testing

#### On-sale arithmetic {#on-sale-arithmetic}

Capacity planning begins by choosing the **unit of capacity**, the measurable quantity that actually limits the business workload, which is rarely processor time. Arun Kejariwal and John Allspaw insist on finding real ceilings by measurement, never from a vendor's specification. For Encore during an on-sale the unit is ordered seat writes per shard, because writes are serialized, because Section 6.2 showed they stop scaling, and because a seat write delayed is a fan who cannot buy.

The arithmetic is short enough for a whiteboard, and belongs on one, in front of the people who will run the on-sale. A fan admitted by the Gate spends about three minutes in seat selection and checkout, within the 5-minute hold. Across that session the fan generates, on average, about four ordered writes (a first hold, often a second hold after losing a seat to someone faster, the sale itself, and the release or expiry of an abandoned hold) and about 26 availability reads. Admission is steady during the on-sale, so arrivals and departures balance, and the shards see the admission rate multiplied by the per-fan demand:

| Quantity | Per fan | At 1,200 fans/s | Capacity, four shards | Utilization |
|---|---|---|---|---|
| Ordered writes | ~4 | 4,800/s | 6,000/s | 80% |
| Availability reads | ~26 | 31,200/s | 40,000/s | 78% |
| Fans in session | ~180 s | ~216,000 | — | — |

*Figure 6.5 — Encore's on-sale capacity arithmetic. Writes bind first, and the admission rate is set so that they sit at 80% of the shards' rated capacity.*

The last row is Erlang's unit in modern dress: 1,200 arrivals a second, each holding a session for 180 s, is an offered load of 216,000 erlangs of fans, Little's law from the companion volume applied to people. At 80% of rated capacity, the hockey stick puts the expected queueing delay at about five times the service time, which the checkout budget can absorb. The remaining 20% looks idle on a cost report. It is not. Load across shards is never perfectly even, because the front-floor sections sell first and hottest; if the busiest shard takes 30% of writes instead of 25%, it runs at 96%, and the hockey stick puts its waits near 25 times service time. Headroom is the price of a short queue, paid in advance.

Encore's on-sale readiness review draws two consequences. A proposal to raise the admission rate raises utilization on the binding resource, so it must arrive with the arithmetic redone and a load test at the new point. And the per-fan figures are measurements that drift with the product; a seat-map renderer that polls twice as often would quietly double the reads row.

#### Load tests that resemble Friday {#load-tests-that-resemble-friday}

The per-fan numbers come from load tests. Encore's harness, which the On-Sale team calls Soundcheck, replays recorded on-sales against a staging copy of the purchase path, and four design choices make it trustworthy. It generates load from an **open model**, in which fans arrive on their own schedule however slowly the system responds, so no stall can hide. Its arrival process is bursty, with the surge of the first minutes, because Kingman's variability term is real. Its seat choices are skewed toward the best sections, because uniform random seats spread writes evenly and flatter the shards. And it stubs the payment service provider (PSP) with a latency distribution taken from production, because the companion volume's first outage began with a PSP that slowed down.

One lesson concerns state rather than traffic. A system's performance depends on what it remembers (caches, connection pools, compiled code, the database's buffer pool), and a load test run twice measures the second run against a system the first has warmed, while on-sale morning is often the first run. The seat-map geometry cache is the clearest case at Encore, since a warm cache serves geometry from memory while a cold one sends every miss to Catalog at the worst possible moment. A touring band soundchecks in an empty arena in the afternoon, and every sound engineer knows the room will sound different at nine o'clock, when 15,000 bodies absorb the reflections; the soundcheck is indispensable, and still only a rehearsal. The analogy breaks in a direction that should worry us, since the hall grows kinder when full and a cold cache does not. A load test against a warm cache measures the encore, not the opening night, and so the test plan must say which state it assumed.

**Recap.** We plan capacity in the unit that actually limits the business, compute utilization on the binding resource, and keep headroom for skew and variability. Load tests use open arrivals, realistic bursts, realistic data skew and realistic dependency latency. Every test states the state it ran against, warm or cold, because production will not always offer the kinder one.

**Exercise 6.3.** Write your system's equivalent of Figure 6.5 for its busiest hour: the unit of capacity, per-request demand, rated capacity and utilization. Then read your last load-test report and find whether it says, anywhere, whether caches were warm or cold.

### 6.4 Autoscaling and Elasticity

#### The lag in the loop {#the-lag-in-the-loop}

Autoscaling promises to remove capacity planning and delivers something smaller: it removes the need to plan for the slow part of demand. An autoscaler is a feedback loop, and like every loop it acts on the past. A metric must rise and be scraped, a stabilization window must pass, a pod must be scheduled (perhaps on a node that must first be bought), the image pulled and the instance warmed before it serves at full speed. Each step is seconds; together they are often minutes, and an on-sale that rises 500× in minutes has finished its first act before the loop has finished its first turn.

Pilots of jet aircraft learn the same lesson about their engines. A turbofan at idle takes several seconds to spool up to full thrust, so an approach flown at idle with a plan to add power when needed can find the airplane sinking before the power arrives. The discipline that answers this is the stabilized approach, flown with the engines already spooled and the power set before it is needed. Encore's equivalent is pre-scaling: because on-sales are scheduled, the curtain-up workflow of Chapter 3 raises the Gate's provisioned concurrency toward its 400 instances and sets Seat Inventory's floors before the doors open. The analogy breaks at the end of the flight: a pilot lands and shuts down, while a service must also scale down, with its own hazards of draining connections, in-flight holds and a late second wave of fans.

Reactive scaling still has its place for unscheduled demand, and it fails in three characteristic ways. It can **lag**, as above. It can **thrash**, scaling up on a burst, down in the lull, and up again, paying the start-up cost each time and never reaching steady state; stabilization windows, asymmetric policies (scale up fast, down slowly) and minimum floors damp the oscillation, which Chapter 7 treats properly as a problem of control loops, the lineage that begins with its governor. And it can **amplify**, which is the most dangerous of the three. The companion volume's first outage is the textbook case: the PSP slowed from 200 ms to 8 s, Orders' requests piled up, health checks failed and the autoscaler, reading the distress as a need for capacity, added instances that opened still more connections to a dependency that was itself the bottleneck. More callers made the slow dependency slower. The autoscaler can only buy what the dependency can sell.

#### Scaling on the right signal {#scaling-on-the-right-signal}

The defense is to choose the scaling signal as carefully as an SLI. Central processing unit (CPU) utilization is a convenient signal and frequently a wrong one, because a service blocked on a slow dependency is idle on CPU and saturated on everything else. Concurrency in flight, queue depth and the saturation measures of Section 6.1 track the work waiting much more directly, and Kubernetes' Horizontal Pod Autoscaler (HPA), or an event-driven scaler built on it, can scale on any of them. Equally important is a ceiling. Every autoscaled service at Encore declares a maximum that its downstream dependencies can actually absorb, derived from the same arithmetic as Figure 6.5, so that the autoscaler cannot scale a service past the capacity of the shard behind it. The maximum is a capacity statement and a budget statement at once.

Elasticity, in the end, belongs to the whole path. A service that scales out in 30 s is still inelastic if its database refuses the extra connections or its warm-up takes five minutes, and anyone who calls a system elastic should be able to name its slowest-scaling component.

**Recap.** An autoscaler is a delayed feedback loop that can lag, thrash or amplify. We pre-scale for the peaks we can foresee, scale reactively on signals that measure waiting work rather than CPU, and cap every service at what its dependencies can absorb. A system is only as elastic as its least elastic component.

**Exercise 6.4.** For one autoscaled service, measure the time from a load step to the first new instance serving at full speed. Compare it with the time your fastest-rising real peak takes to reach its height. What is the service's maximum, and what downstream limit justifies it?

### 6.5 FinOps — Cost as an Operational Signal

#### The night's settlement {#the-nights-settlement}

At the end of every concert, after the crowd leaves, the tour's manager and the promoter sit down to settle the night: ticket revenue against the hall, the crew, the security and the local costs, show by show. A tour that looked at its finances only at season's end would learn in December that its Tuesday shows had lost money all year. **FinOps**, the practice of making cloud spend a shared, continuous responsibility of engineering and finance, is the settlement brought to software. The companion volume introduced its central move, cost per ticket sold; here we treat cost as a telemetry stream with its own anomalies and denominators.

J.R. Storment and Mike Fuller describe the practice as a lifecycle of three phases, Inform, Optimize and Operate, and the first is the hardest. Before anyone can act, every euro must be allocated to an owner through accounts, tags and labels, including the shared nodes of a Kubernetes cluster. Encore allocates cost per service and per tenant, and shows the shared remainder (idle cluster headroom, the telemetry pipeline) as its own line.

Unit economics then need care about denominators. Cost per ticket on a quiet Tuesday and on an on-sale Friday measure different things, because fixed costs are spread over very different volumes. Encore therefore reports two figures: the fixed monthly cost of being open for business, and the variable cost per ticket, which should stay flat or fall as volume rises. A rising variable cost is an engineering signal, a design that grew less efficient; a rising fixed cost with flat volume is a planning signal, capacity bought for demand that did not come.

| Line item | Variable cost per ticket | Notes |
|---|---|---|
| Purchase-path compute (Gate, Inventory, Orders) | €0.041 | pre-scaled peaks billed while warm |
| Data stores and replication | €0.029 | includes the seat ledger's synchronous standby |
| Telemetry (metrics, logs, traces) | €0.022 | sampling policy reviewed quarterly |
| Network egress | €0.011 | wallet delivery and partner API |
| AI gateway tokens (support assistant, refund agent) | €0.006 | about 80% of turns routed to the smaller model |
| Other | €0.011 | build pipelines, preview environments, shared tooling |
| **Total** | **€0.12** | |

*Figure 6.6 — Encore's variable cost per ticket after the forwarder fix. Tokens are one line among six; they get the same treatment as the others.*

The token line moves with prompts and model choices as well as traffic, but it is attributed, budgeted and alerted on like every other line; Chapter 14 takes up the workloads behind it.

#### Commitments, anomalies and on-call {#commitments-and-anomalies}

Cloud pricing offers two ways to spend less, which Storment and Fuller call *using less* and *paying less*. Using less is engineering: right-sizing, deleting what nobody uses, and the arithmetic of the companion volume's forwarder. Paying less is purchasing. Commitments (reserved instances, savings plans) trade a promise of steady spend for a lower rate; on-demand capacity costs more and promises nothing; spot capacity is cheapest and can be reclaimed at short notice. The sensible portfolio follows the shape of demand: commit to the floor that runs every hour of the year, pay on demand for the scheduled peaks, and put interruptible work, such as Sales Analytics' batch jobs and load tests, on spot. A commitment is a capacity forecast written in currency, and it should be made by the people who make the capacity forecast, with the same error bars. Encore commits about 60% of its steady compute and revisits the figure quarterly, once the next on-sale calendar is known.

The Operate phase is where cost meets the pager. Cost anomaly alerts behave like burn-rate alerts: a spend rate that would exhaust the month's budget in a week is a page during business hours, a sudden step in a team's line is a ticket. A latency regression is felt within minutes; a cost regression accumulates silently until the invoice, as the forwarder's €9,000 a month did. Cost is the slowest alarm in the building, which is why it must be wired to the fastest detector we have.

There is also a judgment that no dashboard makes for us. The 20% of write headroom in Figure 6.5 appears on the bill, where a well-meaning optimization pass could find it and propose to remove it. The cheapest configuration and the safest are seldom the same, and the difference between them is a decision about risk, so cost and capacity must be read together. I have come to believe that the most useful thing FinOps does is not to cut spend but to make that decision visible, so that someone makes it on purpose.

**Recap.** FinOps allocates every euro to an owner, splits fixed from variable cost, and watches the variable cost per ticket as an engineering signal. Commitments cover the steady floor, on-demand covers the scheduled peaks and spot covers interruptible work. Cost anomalies are alerted on like burn rates, and cost is always read beside capacity, because headroom shows up on both.

**Exercise 6.5.** Split last month's cloud bill into fixed and variable costs, and compute the variable cost per business unit. What fraction of your steady compute is covered by commitments, and who decided that fraction, from what forecast?

### Kata: Filing Season

> **Your brief: "Ledgerline."** A tax-preparation SaaS in one EU country: 2.4 million filers a year, 35% of whom file in the final six days before the deadline, peaking at 14× normal load on the last evening. Each filing runs a calculation engine (about 400 ms of compute, re-run on every edit) against a shared PostgreSQL cluster. Ledgerline has 30 engineers. Its closed-loop load tests reported a p99 of 180 ms last year, yet support logged thousands of complaints about 10 s waits on deadline night. Its autoscaler scales on CPU, oscillated every few minutes on deadline day, and twice exhausted the database's connection limit. The cloud bill rose 40% year on year while filings rose 12%, and an AI explanation feature launched in spring has its own, unforecast token line.

**Deliverables:**

1. **USE and RED inventory** — the resources and services on the filing path, with the signals for each and the ones currently missing.
2. **Capacity model** — the unit of capacity for deadline night, per-filing demand, utilization on the binding resource at peak, and the headroom you would keep, with the arithmetic shown.
3. **Scalability fit** — a USL fit for the calculation engine against the shared database, from at least five load-test points you specify, with the predicted peak concurrency.
4. **Load-test redesign** — an open-model test plan with realistic arrival bursts, data skew and stated cache state, and an explanation of last year's 180 ms.
5. **Autoscaling policy** — the scaling signal, floors, pre-scaling schedule, stabilization settings and a maximum justified by the database.
6. **Cost plan** — fixed and variable cost per filing, the commitment portfolio, and the anomaly alerts, with the token line treated like the others.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Method over hunch | Would the inventory have found the connection-limit problem before deadline day? |
| Queueing literacy | Is headroom justified by the hockey stick and by skew, not by habit? |
| Honest measurement | Does the load-test plan make coordinated omission impossible? |
| Loop discipline | Can the autoscaler still amplify load onto the database under your policy? |
| Cost with denominators | Is the 40%-versus-12% gap explained per filing, split into fixed and variable cost? |
| Joint reading | Does any cost saving you propose remove headroom the capacity model needs? |

#### Where you now stand

You can now investigate performance by method, read latency as a distribution, explain why waits explode near saturation, fit the USL to a handful of measurements, plan capacity in the unit that limits the business, keep an autoscaler from amplifying trouble, and read the invoice as telemetry. Chapter 7 turns to the loops that run most of what we have measured here: the reconciliation engines of Kubernetes, serverless platforms and GitOps.

### References

- Brendan Gregg — [*Systems Performance*, 2nd ed.](https://www.brendangregg.com/systems-performance-2nd-edition-book.html). Addison-Wesley, 2020.
- Neil J. Gunther — [*Guerrilla Capacity Planning*](https://link.springer.com/book/10.1007/978-3-540-31010-5). Springer, 2007.
- Arun Kejariwal, John Allspaw — [*The Art of Capacity Planning*, 2nd ed.](https://www.oreilly.com/library/view/the-art-of/9781491939192/). O'Reilly, 2017.
- J.R. Storment, Mike Fuller — [*Cloud FinOps*, 2nd ed.](https://www.oreilly.com/library/view/cloud-finops-2nd/9781492098348/). O'Reilly, 2023.
- Brendan Gregg — [*The USE Method*](https://www.brendangregg.com/usemethod.html). brendangregg.com — free online.
- Luiz André Barroso, Urs Hölzle, Parthasarathy Ranganathan — [*The Data Center as a Computer*, 4th ed.](https://link.springer.com/book/10.1007/978-3-031-99489-0). Springer, 2025 — free online.
- Jeffrey Dean, Luiz André Barroso — [*The Tail at Scale*](https://doi.org/10.1145/2408776.2408794). Communications of the ACM, 2013.
- Brendan Gregg — [*BPF Performance Tools*](https://www.brendangregg.com/bpf-performance-tools-book.html). Addison-Wesley, 2019.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne (eds.) — [*The Site Reliability Workbook*](https://sre.google/workbook/table-of-contents/). O'Reilly/Google, 2018 — free online.

---

## Chapter 7: The Runtime and Its Control Plane — Kubernetes, Serverless, IaC, and GitOps {#ch7}

> A controller is an opinion about the world, held continuously and acted upon without being asked.

A modern runtime is less a place where our software sits than a crowd of small machines, each noticing that something differs from what was asked for and correcting it: a scheduler placing pods, an autoscaler adding replicas, a GitOps agent reverting a hand-edited setting, an upgrade reconciler draining nodes through the night. We used to operate servers. Today we mostly operate the things that operate servers, and how to do that well turns out to be an old question in new clothes.

In 1868 James Clerk Maxwell published a short paper in the *Proceedings of the Royal Society* called "On Governors." Its subject was the centrifugal governor that James Watt had fitted to his steam engines some 80 years earlier: two iron balls on hinged arms, spun by the engine itself, which fly outward as the engine speeds up and, through a sleeve and a lever, close the steam valve. The device was everywhere, and it mostly worked, but engineers had learned that it sometimes **hunted**, swinging above and below the intended speed, and that their improvements, which made governors more sensitive, often made the hunting worse. Maxwell wrote down the equations of engine and governor together, linearized them around the running speed, and showed that whether the swings die away or grow depends on the roots of a single characteristic equation. He also drew a distinction we will need: a *moderator* merely reduces an error, leaving the engine a little off its mark under load, whereas a true governor keeps correcting until the error is gone, and pays for that exactness with a greater tendency to oscillate.

The paper is usually cited as the beginning of control theory; Norbert Wiener pointed back to it when naming cybernetics in 1948. For us it is something more practical. Every reconciliation loop in a cloud runtime is a governor, every one can hunt, and two of them attached to the same shaft can fight. Encore now runs dozens of such loops across its Kubernetes cells, its serverless Gate and its GitOps repositories, most of them written by someone else. This chapter is about operating them: what each loop owns, how fast it acts, and what it cannot see.

### 7.1 Declarative Systems and Reconciliation Loops

#### The anatomy of a loop {#anatomy-of-a-loop}

A **reconciliation loop** is a process that repeatedly observes the actual state of some part of the world, compares it with a declared desired state, and takes the smallest action it knows that moves the first toward the second. The companion volume introduced Kubernetes as such a loop; here we take the loop itself apart.

Every loop has the same four parts as Watt's governor: a sensor (the flyballs, or a watch on the Kubernetes API), a set point (the intended speed, or the `spec` of a resource), a comparator (the sleeve and lever, or a function that computes a diff) and an actuator (the valve, or an API call that creates a pod). It also has two properties that the declarative YAML never mentions and that decide whether it behaves: its **gain**, how hard it pushes for a given error, and its **delay**, how long it takes to sense the effect of its own last push. Maxwell's result, translated, is that a loop with high gain and long delay will overshoot, see the overshoot late, push back too hard, and settle into the hunting that so puzzled the engine builders.

A closer ancestor is Mark Burgess's CFEngine, begun in 1993, which managed Unix machines by describing the state they should converge to and repairing deviations on every run. Kubernetes and today's GitOps agents sit in that tradition; what changed is the tempo, from a pass every few minutes to hundreds of loops reacting within seconds.

#### Level-triggered, not edge-triggered {#level-and-edge-triggered}

The term comes from electronics. An **edge-triggered** system acts on *changes*: it hears "a pod died" and starts a replacement. A **level-triggered** system acts on *state*: it looks, finds three pods where five were asked for, and creates two, whatever the history that led there. Kubernetes controllers are written to be level-triggered. Events from the API's watch are only hints to look sooner; the action is computed from the whole present state, so a missed event or a controller restart costs time, not correctness.

The distinction matters most where we are tempted to violate it. Encore's first version of its tenant-provisioning automation was edge-triggered: a `TenantCreated` message started a script that created a database, a namespace and a DNS record. When the script failed halfway, nothing ever noticed, because the event had already been consumed; three Professional tenants lived for a month with a namespace and no database. The replacement is a small operator that reconciles a `TenantDatabase` custom resource on every pass and heals half-finished cases without anyone filing a ticket. A level-triggered loop forgives the past, because it never consults it.

That forgiveness has a price: a level-triggered controller will also undo a human's deliberate change that is not in its desired state, patiently, all night.

#### When governors fight {#when-governors-fight}

A **controller** in Kubernetes is a reconciliation loop for one kind of resource, and an **operator** is a controller that encodes the operational knowledge of a particular application (how to fail over this database, how to resize that cache) behind a custom resource. Besides the built-in controllers, Encore's clusters run a Horizontal Pod Autoscaler (HPA) per scaled deployment, the cluster autoscaler, the GitOps agent, the `TenantDatabase` operator and the platform's node-upgrade reconciler, which keeps every node pool at its target Kubernetes version by draining and replacing nodes one at a time. Each is sensible alone. Trouble begins where two claim the same field.

On an ordinary Thursday before a mid-sized on-sale, an engineer on the Catalog team, expecting a surge of browsing, ran `kubectl scale` to take Catalog from 20 replicas to 60. Within a minute the GitOps agent, which had self-healing switched on and found `replicas: 20` in the manifest, put it back to 20. Meanwhile the HPA, configured for 60% CPU with a floor of 12, saw 60 nearly idle pods and, once its scale-down stabilization window had passed, began trimming them. For half an hour the replica count drew a sawtooth on the dashboard as three governors, each correct by its own lights, pulled the same lever. Nothing failed. But the engineer believed the service was scaled when for most of that half hour it was not, which is how small fights become large incidents on worse days. Figure 7.1 sketches the shape of that half hour, and Figure 7.2 lists the governors that drew it.

{% include diagrams/fig-7-1.svg %}

*Figure 7.1 — Catalog's replica count during the fight, sketched. One spike to 60 is reverted within a minute, and then the GitOps agent and the autoscaler pull the count back and forth between 20 and the autoscaler's preference. Notice that the line the engineer believed in is never touched again.*

| Controller | Field it acts on | Acts within | Set point lives in |
|---|---|---|---|
| GitOps agent | every field in the manifest | about 3 min (sync interval) | Git |
| Horizontal Pod Autoscaler | `spec.replicas` | 15 s to scale up; 5 min window to scale down | HPA object |
| Cluster autoscaler | node count | about 1 min plus node boot | node-group limits |
| Node-upgrade reconciler | node versions (by drain) | continuous, one node at a time | platform config |
| `kubectl scale` by a human | `spec.replicas` | immediately | a person's head |

*Figure 7.2 — The governors on Catalog's shaft. Two rows claim `spec.replicas`, and the manifest claimed it too. The last row has no record and no delay, which is why it loses.*

The repairs follow Maxwell more closely than one might expect. First, *one field, one owner*: Encore removed `replicas` from every manifest whose deployment has an HPA, and its policy checks now reject the combination. Second, *express intent to the owner*: a planned surge is a change to the HPA's floor, made in Git through the curtain-up workflow of Chapter 3, never a fight with the HPA's output. Third, *respect the damping*: the HPA's scale-down window is a dashpot on the flyballs, and teams that shorten it reliably rediscover hunting. Two loops on one lever produce oscillation; two loops on two levers, with the slower one setting the faster one's set point, produce a hierarchy, and hierarchy is how control engineers have always mastered this kind of complexity. Figure 7.3 draws Catalog's loops arranged that way.

{% include diagrams/fig-7-3.svg %}

*Figure 7.3 — Catalog's governors as a hierarchy. Each slower loop writes the set point of a faster one, and only the dashed accent arrow claims a field another loop owns. Notice that it is also the only arrow that leaves no record.*

The theatre has a practice that shows both the value of reconciliation and its limit. Before every performance a stage crew runs the **preset**, putting every chair, prop and lamp where the stage manager's book says, whatever happened the night before: level-triggered in the purest sense. But a good crew also knows *why* the book says what it says, and would leave alone a chair the director moved on purpose. A controller has no such sense. It knows the book and nothing of the reasons, and so the only way to tell it about a reason is to change the book.

**Recap.** A reconciliation loop observes, compares and acts, and its gain and delay decide whether it settles or hunts, exactly as Maxwell showed for the governor. Level-triggered loops forgive missed events but also undo undeclared human intent. When two loops own one field they fight, so we give each field one owner and express intent by changing the owner's set point.

**Exercise 7.1.** Pick one production deployment and list every controller, script and human that can change its replica count or its nodes. For each, note its set point, where that set point is recorded and how quickly it acts. Is any field claimed twice?

### 7.2 Kubernetes in Production

#### Requests, limits and the honest workload {#requests-and-limits}

Kubernetes schedules on promises. A pod's **resource request** is the CPU and memory it promises to need, and the scheduler places it only where that much is free; its **limit** is the most it will be allowed to take. The two numbers together set the pod's quality-of-service class, which decides who is evicted first when a node runs short. Bilgin Ibryam and Roland Huß call declaring them the *Predictable Demands* pattern, and everything else rests on it: a scheduler fed false promises packs nodes that look half empty on paper and are full in fact.

The two resources fail differently. A container that exceeds its memory limit is killed, abruptly and visibly; one that reaches its CPU limit is throttled, quietly, which shows up as latency at the tail rather than as an error. Encore's Orders service spent a month with a p99 that spiked every few minutes before someone graphed throttled periods beside it. The house rule now sets memory limits equal to requests, and leaves CPU limits off latency-sensitive services, so a burst borrows idle capacity instead of waiting for the next slice. It is a house rule and no more; noisy batch workloads still get CPU limits, because on shared nodes one team's burst is another team's tail latency.

#### Disruption is a normal day {#disruption-budgets}

Involuntary disruptions, such as a failed node, cannot be negotiated with. Voluntary ones (a drain for an upgrade, the cluster autoscaler removing an underused node) can be, and the instrument of negotiation is the **PodDisruptionBudget** (PDB): a declaration that at most so many pods of a given set may be voluntarily unavailable at once. A drain that would breach the budget waits.

A PDB is a promise about *how many*, never about *which*. Seat Inventory runs each shard as a small replicated group with a fenced leader, and its PDB allows one pod unavailable per shard, which is correct as far as it goes: no drain will take a shard below quorum. But a drain that removes one pod may remove the leader, and a leader's departure, though safe, triggers a failover with a short window of rejected writes. On a quiet Tuesday that window is invisible. Whether it is invisible on every day of the year depends on which other loops are running and what they know about the calendar, and Chapter 12 will show what that question costs when nobody has asked it.

#### Upgrades as a standing condition {#upgrade-cadence}

Kubernetes ships roughly three minor releases a year, and each is patched upstream for a little over a year; managed providers follow a similar rhythm and eventually upgrade clusters that fall too far behind, whether or not their owners are ready. Upgrading is therefore less a project than a weather system, and a platform that treats it as a project will be caught in the rain twice a year.

Encore's Runtime team, one of the platform group's product teams, upgrades in waves. Each region runs a core cluster for Encore's own services and six cells for Professional tenants; a new version reaches a canary cell of internal test tenants first, then the other cells, then the core clusters. Node pools are replaced by the node-upgrade reconciler, draining through the PDBs. Before each wave a check scans manifests for APIs the new version removes, because the most common upgrade failure is rarely a bug in Kubernetes; it is a chart still asking for something that no longer exists. Figure 7.4 shows the waves across all 14 clusters. A runtime is like a ship's hull, which goes to dry dock on a schedule rather than when it leaks; the analogy breaks only in our favor, since we can dry-dock one compartment while the ship sails.

{% include diagrams/fig-7-4.svg %}

*Figure 7.4 — A Kubernetes upgrade moving through Encore's 14 clusters in three waves. The canary cell takes a new version first, and the core clusters, which carry Encore's own services, take it last.*

#### Many clusters, deliberately {#many-clusters}

Encore runs 14 clusters by choice. One large cluster would pack better, but its control plane would be a single blast radius and its upgrades a single event; cells, which Chapter 9 treats in depth, trade efficiency for containment. The price is tooling that makes 14 clusters behave like one fleet, with one GitOps layout, one set of policies and one set of dashboards. A fleet of hand-tended clusters is merely 14 opportunities to drift.

**Recap.** Requests and limits are the promises the scheduler plans with, and CPU limits fail as latency rather than errors. PDBs govern how many pods a voluntary disruption may take and say nothing about which. Upgrades are a permanent condition best handled in waves through cells, and many clusters are worth their cost only if tooling makes them one fleet.

**Exercise 7.2.** For one latency-sensitive service, graph CPU throttling against p99 latency for a week, and list its PDB. Which pod's loss would hurt most, and does anything in your cluster know that?

### 7.3 Serverless and Managed Services — Operating What You Don't Run

#### The shared responsibility line {#shared-responsibility}

Cloud providers describe their bargain with customers as a **shared responsibility model**: the provider is responsible for the security and operation *of* the cloud, and the customer for what they put *in* it. It was framed for security, but it describes operations just as well, and its most important word is the one it leaves out. Responsibility to the *user* is never shared. When the Sale Gate is slow, fans blame Encore, and they are right to.

So operating a function or a managed service means operating everything around a box we cannot open: its configuration, its quotas, its failure modes seen from outside, and our response when it misbehaves. A touring production that plays a venue uses the house crew, the house rigging and the house power, and nobody in the audience distinguishes the tour's failures from the venue's. A good production manager therefore advances the show, learning the load-in times, power limits and curfew ahead of time. The analogy breaks because a venue can be walked the day before, while a provider's internals stay invisible; our advance work is done through quotas pages and our own measurements.

#### Quotas are part of the architecture {#quotas}

Function platforms cap concurrency per account and region, and that cap is shared by every function in the account unless some of it is reserved. Encore learned this in an on-sale rehearsal, when a backfill job for Sales Analytics, deployed as functions in the same account as the Gate, consumed most of the regional concurrency at the moment the Gate's synthetic fans arrived; the Gate was throttled by a neighbor it did not know it had. Three changes followed. The Gate now runs in its own cloud account, as do each of the serverless cells for self-service venues. It has reserved concurrency, so no neighbor can take its share. And a quota inventory, generated nightly from the provider's APIs, sits beside Encore's capacity models from Chapter 6, with an alert when forecast peak demand comes within 30% of any limit.

Cold starts deserve the same treatment as quotas: a property to be measured rather than an annoyance to be endured. The Gate pre-warms with provisioned concurrency before scheduled on-sales, but an unscheduled surge (a surprise announcement on social media, say) meets cold functions, and the first seconds of p99 latency belong to the runtime's initialization, not Encore's code. The team keeps a cold-start allowance in its latency service level objective (SLO) and measures it monthly from a deliberate cold start.

#### When the provider is down {#provider-incidents}

On 28 February 2017 a mistyped command during routine maintenance removed more capacity than intended from Amazon S3 in its US-East-1 region, and much of the internet that depended on it failed for some hours. One detail has become a teaching story: the provider's own status dashboard could not show the problem at first, because it too depended on S3. Its lessons, documented in Amazon's own summary, concern the customers more than the provider: many discovered dependencies they had never drawn.

A provider incident is a strange kind of incident for the team that owns the symptoms, since it can mitigate but not repair. Encore's runbooks therefore treat each managed dependency as an integration point with three pre-decided answers: how we detect its degradation ourselves (synthetic checks of our own, whatever the provider's status page says), what we degrade to (the Gate can hold fans in the queue with admissions paused; the Catalog can serve cached pages), and how we say so to fans and organizers. A managed service removes the work of running it and leaves us the work of surviving it.

**Recap.** Responsibility for the machinery is shared with the provider; responsibility to users is not. Quotas and cold starts are architectural properties to inventory, budget and test. We can mitigate a provider incident but never repair it, so we decide in advance how to detect them ourselves and what to degrade to.

**Exercise 7.3.** List every managed service on your most important user path with its tightest quota, your forecast peak against that quota, and what your system does when the service is down for an hour. Mark any entry where the honest answer is "we would find out."

### 7.4 Infrastructure as Code and GitOps

#### State, drift and the reality behind the file {#state-and-drift}

The companion volume made the case for infrastructure as code (IaC) and GitOps; operating them is about the gap between the code and the world. Declarative IaC tools such as Terraform and its fork OpenTofu keep a **state file**, a record of which real resources correspond to which declarations, and every plan is computed against it. The state file is production data in its own right: it needs locking, backups and access control, since it often holds the very secrets the code was careful not to.

**Drift** is any difference between the declared and the actual state of infrastructure, and it has two sources that call for different responses. Some is made by people, like the console fix at 2 a.m.; some by other loops, like an autoscaler resizing a node group. The first should be reverted or written back into code; the second should be excluded from IaC's attention, since an IaC tool that fights the autoscaler is just Section 7.1's sawtooth with slower teeth. Encore runs a plan against every stack nightly and files the non-empty diffs as tickets for the owning team, which turns drift from folklore into a queue.

#### The blast radius of a plan {#blast-radius-of-a-plan}

A plan is a forecast of what an apply will do, and its most important line is the summary of what it will destroy. Kief Morris argues for small, independently deployable stacks, and the operational reason is that a plan's blast radius is bounded by its stack. Encore's earliest infrastructure lived in a single stack, and a harmless-looking module rename once produced a plan that would destroy and recreate the Finance ledger's database, because the tool saw a resource vanish under one name and appear under another. A reviewer caught it, but only because she read to the bottom. Today stacks are cut along the same lines as cells and services, stateful resources carry lifecycle protection against deletion, and plans are reviewed with the destructive summary at the top.

Surgical teams adopted a practice for this moment: the **time-out** before the first incision, in which the team stops and confirms aloud the patient, the procedure and the site. It exists because the worst errors are made confidently, by skilled people, at the moment of commitment. A plan review is our time-out, and **policy as code**, rules written in a language such as Open Policy Agent's (OPA) and evaluated against every plan and manifest, is the part of it that never tires. Encore's rules deny any plan that destroys a resource labeled stateful without an explicit, separately approved override, any manifest that sets `replicas` beside an HPA, and any public bucket at all. A policy check is a colleague who has read every postmortem and never skims.

#### GitOps repositories and promotion {#gitops-promotion}

The term GitOps was coined at Weaveworks in 2017 for an older idea made precise: a pull-based agent inside each cluster reconciles it toward a Git repository, so that humans and pipelines change the repository and nothing else changes the cluster. At Encore, application repositories build images and publish them by digest; a separate environment repository, `encore-deploy`, holds the desired state of every cluster, one directory per environment and cell, and an Argo CD instance in each cluster reconciles from it.

| Stage | What changes in `encore-deploy` | Who approves | Gate to next stage |
|---|---|---|---|
| Staging | image digest in `envs/staging/` | automatic on build | integration suite and synthetic buyers pass |
| Canary cell | digest in `envs/prod/eu-1/cell-canary/` | automatic | SLO canary holds for 1 h |
| Professional cells | digest in each cell directory, a few at a time | owning team | per-cell burn rate stays normal |
| Core clusters | digest in `envs/prod/*/core/` | owning team | outside on-sale freeze windows |

*Figure 7.5 — Promotion as a series of pull requests. Each stage is a commit someone can read and revert, and the gates are the same SLO signals Chapter 4 defined, applied to the deployment itself.*

The history of the environment repository is a complete account of what was *intended* to run where, which is not the same as what did run: a sync can fail, a webhook can reject a manifest, an emergency can bypass the repository. Encore therefore alerts on any application out of sync for more than 15 minutes, and its break-glass procedure, an hour of direct cluster access for a named engineer, ends with a required commit writing the change back into Git, so the loop does not quietly revert the fix.

Secrets are the awkward guest. Encore keeps them in a secrets manager and lets an operator in each cluster materialize references declared in Git, so the repository says *which* secret a service needs and never what it is; Chapter 11 takes up rotation.

**Recap.** IaC state is production data, and drift is either reverted, written back or deliberately ignored, depending on whether a person or a loop made it. A plan's blast radius is bounded by its stack, so stacks stay small, and policy as code makes the review's time-out tireless. GitOps promotion is a chain of readable pull requests, but only sync status tells us what is actually running.

**Exercise 7.4.** Run a plan against every stack you own and count the resources in the largest. Then write one policy rule that would have blocked the worst infrastructure change your team has ever applied.

### 7.5 The Platform as a Paved Road

#### A product with a road crew {#product-with-a-road-crew}

Everything in this chapter so far is machinery that 40 stream-aligned teams should not each have to master. The companion volume described how Encore built its platform; the question now is how it is *run*. Matthew Skelton and Manuel Pais, in *Team Topologies*, framed the platform team's purpose as reducing the **cognitive load** of stream-aligned teams, and argued for the **thinnest viable platform**: the smallest set of services that lets those teams deliver without deep knowledge of the layers beneath. Thinness is an operating virtue, because every capability a platform offers is one it must run, upgrade and eventually retire.

The phrase "paved road" (Netflix's term; Spotify's "golden path" is its cousin) repays development. A city paves the routes people actually walk, often after watching where the grass wears away, and then maintains them: potholes are filled, closures announced in advance, and nobody is forbidden to cross the park. Encore's Runtime and Delivery teams work the same way, measuring where teams leave the road and why, and announcing deprecations with the patience of a highway authority. The analogy breaks at its most useful point. A city can rely on people needing to travel; a platform must keep earning its traffic, because a stream-aligned team that finds the road worse than the field will cut across, and the platform will learn about it only from the drift.

#### Operating the platform itself {#operating-the-platform}

Camille Fournier and Ian Nowland insist that a platform team must own the operations of what it builds, on-call included, and Encore holds to this: within the platform group, the Reliability team carries the pager for the platform planes, and each plane has its own SLOs, among them GitOps sync latency, cluster API availability and time to provision a new service. I spent years doing platform engineering inside a large bank, and the lesson that cost the most to learn was that a platform's users judge it by its worst week, not its average one. A shared runtime's incidents are everyone's incidents, and its changes need the discipline Chapter 8 asks of any change on the purchase path.

That includes the platform's own automation. The node-upgrade reconciler, the GitOps agents and the policy engine are production systems that act on other teams' services, often at times nobody is watching. Encore classifies them as "low-risk automation," and for most days of the year they are. Whether that classification should hold on the days that matter most is a question the platform group has not yet asked, and the absence of a question is not the same as an answer.

Migrations are the platform's other permanent work. Moving 40 teams to a new ingress controller takes quarters, and Fournier and Nowland rightly treat migration and sunsetting as staffed product work. Encore's rule is that the platform team does the first three migrations itself, alongside the owning teams, before writing the self-service guide, so the guide describes the road as it really is.

**Recap.** A platform is a product whose purpose is to lower other teams' cognitive load, and it should stay as thin as that purpose allows. Its teams own its operations, with SLOs of their own, and its automation is production software acting on everyone's services. Migrations are planned, staffed product work, done first by the people who ask others to do them.

**Exercise 7.5.** Pick one capability your platform, or your cloud provider, offers your team. Who is on call for it, what is its SLO, and when was the last migration it forced on you? If you cannot answer, write the question to its owners.

### Kata: The Lunch Rush

> **Your brief: "Forkline."** A food-delivery marketplace: 18,000 restaurants and 25,000 couriers across six countries, with a customer app, a courier app and a restaurant tablet. Forkline has 65 engineers in nine teams and a platform team of four. Its three hand-built Kubernetes clusters are two minor versions behind, and the provider will force an upgrade in five months. Infrastructure lives in one Terraform stack of 1,700 resources whose plan takes 25 minutes, so engineers make "small" fixes in the console. Order webhooks to restaurant point-of-sale systems run as functions and were throttled last month when a tablet app update made every restaurant reconnect at once. At the lunch and dinner peaks the dispatch service's HPA and an engineer's habitual manual scale-up at 11:30 regularly fight, and nobody is sure which wins.

**Deliverables:**

1. **Controller census** — every loop and human that changes the dispatch service's replicas, nodes or infrastructure, with field, set point and speed.
2. **Upgrade plan** — reaching a supported version before the forced upgrade, with PDBs, the order in which clusters move and the hours kept clear of the meal peaks.
3. **Stack decomposition** — how to split the 1,700-resource stack, which resources get deletion protection, and three policy-as-code rules.
4. **Managed-service survival sheet** — the quota inventory for the order path and what the webhooks degrade to during a reconnection storm or a provider outage.
5. **Thinnest viable platform** — what a four-person platform team should offer, what it should decline to offer, and the SLOs it will be held to.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| One owner per field | Does every field with more than one controller now have exactly one, with intent expressed through its set point? |
| Upgrade as routine | Does the plan leave Forkline able to upgrade every few months, or only survive this one? |
| Bounded plans | Could any single plan still destroy a stateful resource without a separate approval? |
| Provider realism | Are degradation modes decided in advance and detected by Forkline's own checks rather than the provider's status page? |
| Thinness | Is the platform's scope sized to four people's on-call capacity, with explicit refusals? |
| Drift honesty | Is console change made unnecessary, or merely forbidden? |

#### Where you now stand

You can now read a runtime as a collection of governors: name what each loop owns, how fast it acts and what it cannot see, keep two of them from fighting over one lever, and operate the clusters, functions, stacks and repositories beneath them as one fleet, knowing where the provider's responsibility ends and yours continues. Chapter 8 turns from the machinery that holds the system steady to the changes we deliberately push through it, and to the long record of how change, more than anything else, is what breaks production.

### References

- James Clerk Maxwell — [*On Governors*](https://doi.org/10.1098/rspl.1867.0055). Proceedings of the Royal Society of London, 1868.
- Josh Rosso, Rich Lander, Alex Brand, John Harris — [*Production Kubernetes*](https://www.oreilly.com/library/view/production-kubernetes/9781492092292/). O'Reilly, 2021.
- Bilgin Ibryam, Roland Huß — [*Kubernetes Patterns*, 2nd ed.](https://developers.redhat.com/e-books). O'Reilly, 2023 — free online.
- Kief Morris — [*Infrastructure as Code*, 3rd ed.](https://www.oreilly.com/library/view/infrastructure-as-code/9781098150341/). O'Reilly, 2025.
- Billy Yuen, Alexander Matyushentsev, Todd Ekenstam, Jesse Suen — [*GitOps and Kubernetes*](https://www.manning.com/books/gitops-and-kubernetes). Manning, 2021.
- Camille Fournier, Ian Nowland — [*Platform Engineering*](https://www.oreilly.com/library/view/platform-engineering/9781098153601/). O'Reilly, 2024.
- Matthew Skelton, Manuel Pais — [*Team Topologies*, 2nd ed.](https://itrevolution.com/product/team-topologies/). IT Revolution, 2025.
- Brendan Burns, Joe Beda, Kelsey Hightower, Lachlan Evenson — [*Kubernetes: Up and Running*, 3rd ed.](https://www.oreilly.com/library/view/kubernetes-up-and/9781098110192/). O'Reilly, 2022.
- Brendan Burns, Brian Grant, David Oppenheimer, Eric Brewer, John Wilkes — [*Borg, Omega, and Kubernetes*](https://queue.acm.org/detail.cfm?id=2898444). ACM Queue, 2016 — free online.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.

---

## Chapter 8: Shipping Change Safely — Continuous and Progressive Delivery {#ch8}

> Every outage begins as somebody's reasonable change.

A system that nobody touches tends to keep doing whatever it did yesterday, but the world it serves keeps moving, and a system frozen against change slowly becomes wrong about the world. So we change it, many times a day, and in doing so create the moments when most of our trouble begins. The question of this chapter is how a team can change a running system often, quickly and safely, when each of those three words seems to argue with the other two.

The answer the industry has worked out over the last two decades is, at first sight, a paradox: we make change safer by making it smaller and more frequent, and by separating the act of putting code into production from the act of letting anyone use it. First, consider what happens without it. On the morning of 1 August 2012, Knight Capital, one of the largest market makers in American equities, deployed new code to its order router. Forty-five minutes after the market opened, the firm had lost about $440 million, and within a year it no longer existed as an independent company.

Encore today ships about 180 production deployments on a typical working day, across 40 teams and through one golden-path pipeline, with a canary that promotes builds on the evidence of its service level objectives (SLOs). This chapter takes that machinery apart, asks what each piece is for, and ends with the newest question: what changes when a growing share of those deployments was written by a machine.

### 8.1 Change as the Leading Cause of Outages

#### Forty-five minutes at Knight Capital {#knight-capital}

Knight's order router, SMARS, broke large "parent" orders into smaller "child" orders sent to the market. In the summer of 2012, Knight prepared code for the New York Stock Exchange's Retail Liquidity Program (RLP), which was to start trading on 1 August. The new code reused a flag in the order messages, one that had once activated a function called Power Peg. Power Peg had not been used since 2003, but its code had never been removed. Worse, a change in 2005 had moved the logic that counted how much of a parent order was already filled, so Power Peg, if ever woken, would no longer know when to stop.

In the days before the launch, a technician deployed the new code to the eight servers that ran SMARS. It reached seven of them. Nobody noticed the eighth, because no second person checked the deployment and no automated process compared the servers. When the market opened at 09:30 Eastern time and RLP orders arrived carrying the repurposed flag, seven servers handled them as intended and the eighth woke Power Peg. It sent child orders without end, with no notion that the parent orders were long since filled. Before the open, Knight's systems had sent 97 automated emails mentioning Power Peg; they were not designed as alerts, and nobody read them as one.

The response made things worse. Engineers removed the new code from the seven healthy servers, a rollback in every ordinary sense, and now all eight servers ran the old code against the repurposed flag, and all eight woke Power Peg. By the time it was stopped, about 45 minutes after the open, SMARS had made more than 4 million executions in 154 stocks and left Knight holding billions of dollars of positions it had never meant to take. Knight reported a pre-tax loss of about $440 million; the Securities and Exchange Commission (SEC), in its 2013 order, put it above $460 million and fined the firm for its controls. Knight needed emergency financing within days and was merged into Getco the following year. Figure 8.1 lays out the eight servers through that morning.

{% include diagrams/fig-8-1.svg %}

*Figure 8.1 — Knight Capital's eight SMARS servers on 1 August 2012. One unverified server woke Power Peg at the open, and the rollback of the seven healthy servers gave all eight the same old code.*

Read with Chapter 2's eyes, Knight's morning has no single cause: dead code kept for nine years, a flag given a second meaning, an unverified manual deployment, a refactoring that broke a dormant path, warnings nobody was designed to see, and a rollback that amplified the failure. Each was locally understandable; together they were a loaded mechanism, and the deployment pulled its trigger.

#### Why change dominates {#why-change-dominates}

Knight's cost was extreme; its shape is common. The authors of Google's *Site Reliability Engineering* (2016) reported that roughly 70% of their outages were due to changes in a live system. When Encore's Reliability team reviewed the last year of incidents, about two thirds began within an hour of a change: a deployment, a configuration edit, a flag flipped, or a piece of platform automation doing what it was built to do.

This is close to a tautology: a system whose code and load are unchanged has few new ways to fail. A deployment is the one moment when we know for certain that the system in production differs from the one we tested. Aviation knows the pattern: a disproportionate share of accidents cluster in takeoff and landing, the phases of flight in which the aircraft changes state, close to the ground, with the least margin. The analogy instructs because it names the state transition as the dangerous thing. It breaks on frequency: an airliner makes a few takeoffs a day, each with a crew running a checklist, while Encore makes 180 before dinner, and no checklist read by a human scales to that.

The tempting conclusion is to change less. It fails twice. Patches, upgrades and the business do not wait, so a system changed rarely gathers its changes into larger batches, which are harder to test, reason about and undo. And a team that deploys rarely deploys badly, because a skill practiced quarterly is a skill half forgotten. The essential complexity here is that the system must change; the accidental complexity is whatever we add to each change that makes it bigger, rarer or harder to reverse than it needs to be.

**Recap.** Most outages begin with something we did, because change is when the system becomes one we have not yet observed. Knight Capital shows a deployment completing a mechanism assembled over years. Changing less only makes each change larger and each deployment less practiced.

**Exercise 8.1.** For your last ten incidents, note the most recent change before each began (code, configuration, flag, automation or none). What share began with a change, and which kind most often bypassed your pipeline?

### 8.2 The Deployment Pipeline and Continuous Delivery

#### A sequence of increasingly expensive questions {#pipeline-as-questions}

Continuous integration (CI) came from extreme programming, which Kent Beck set out in *Extreme Programming Explained* (1999): integrate everyone's work into one mainline many times a day, while conflicts are small. In 2009, at the Velocity conference, John Allspaw and Paul Hammond described Flickr doing more than ten deploys a day, and an industry used to quarterly releases heard that this could be ordinary. A year later Jez Humble and David Farley published *Continuous Delivery* (2010), which gave the practice its central structure.

The **deployment pipeline** is the automated path every change takes from commit to production, a sequence of stages in which each stage asks a more expensive question than the last and only a change that answers them all may proceed. Its rules are few and strict: build the artifact once and promote that same artifact everywhere, so that what was tested is what ships; keep everything that defines the system in version control; and when the pipeline is red, fix it first, because a pipeline people have learned to ignore is no longer a control.

| Stage | The question it asks | Typical time at Encore | What it cannot see |
|---|---|---|---|
| Commit | Does it build, and do the fast tests pass? | 6 min | anything involving another service |
| Acceptance | Does the service keep its contracts and its specified behavior? | 15 min | real traffic, real data shapes |
| Fitness | Do architectural, security and cost rules still hold? | 4 min | behavior under load |
| Staging soak | Does it start, migrate and serve in a production-like cell? | 10 min | the 500× on-sale |
| Canary | Do its service level indicators (SLIs) match the baseline's on real traffic? | 20–60 min | rare paths and slow drift |
| Release | Who should see the new behavior, and when? | a business decision | — |

*Figure 8.2 — Encore's golden-path pipeline. Each stage is cheaper to fail than the next, and the right-hand column says which later stage must catch what this one cannot.*

A theater production moves from read-through to technical rehearsal to dress rehearsal to previews, and each stage catches what the previous one could not, since nobody discovers that a costume change is too slow until the actors wear the costumes. The picture breaks at the end: a theater has one opening night, a pipeline opens every hour, and its preview audience is the real audience, which is why the last two stages of Figure 8.2 belong to Section 8.3.

Humble and Farley distinguished *continuous delivery*, in which every change that passes the pipeline could be deployed, from *continuous deployment*, in which it is. Valentina Servile's *Continuous Deployment* (2024) argues for the second and lists its prerequisites: fast automated tests, observability that notices a bad change, trunk-based development and a rollback that takes minutes. Encore deploys continuously, except that Seat Inventory keeps a human release step, because its event-sourced projections must first replay against production history and a person reads the result.

#### Small batches and the evidence for speed {#small-batches}

The pipeline's deepest effect is on batch size. A 40-line change in production 40 minutes after it was written can be understood, observed and undone; three weeks of 15 people's work can only be hoped for. The DevOps Research and Assessment (DORA) metrics, which the companion volume introduced, measure exactly this, and the finding in *Accelerate* (2018) that matters here is that throughput and stability do not trade off: the teams that deployed most often also failed least often and recovered fastest. The same research found that approval by an external change board was associated with slower delivery and no better change failure rate, which suggests that the board's main product is reassurance.

The pipeline has one weakness that Knight's morning displays: it guards only the changes that go through it. Knight's deployment was manual, and its flag was data in a message. At Encore, configuration lives in the GitOps repositories of Chapter 7, but flags, runtime tuning and platform automation each have their own paths into production, and the changes that bypass the pipeline are the ones its owners know least about.

**Recap.** The deployment pipeline is a sequence of increasingly expensive questions asked of one artifact. Its real gift is small batches, which buy stability as well as speed. It protects only the changes that pass through it, so every other route into production deserves to be listed and narrowed.

**Exercise 8.2.** List every route by which a change can reach your production systems: pipelines, consoles, flag tools, configuration services, automation, scripts. Mark each as reviewed, tested, recorded and reversible, or not. The rows with the most gaps are your next pipeline work.

### 8.3 Progressive Delivery — Feature Flags, Canaries, and Rollbacks

#### Deploying is not releasing {#deploy-versus-release}

**Progressive delivery** is the practice of putting new code into production without exposing it, then widening its exposure in deliberate steps, each conditional on evidence that the last step did no harm. The name came from the analyst James Governor, and *Progressive Delivery* (2025), by Governor, Kim Harrison, Heidi Waterhouse and Adam Zimman, argues that who sees a change, and when, should be decided by whoever owns the risk. The mechanics are mostly in Humble and Farley already; what progressive delivery adds is one idea held steadily: every change has a blast radius, and we should choose it.

#### Canaries and automated analysis {#canary-analysis}

British miners carried canaries underground for most of a century, because the bird showed the effects of carbon monoxide before the men did; the last were retired in 1986. A **canary release** works the same way: a small share of real traffic goes to the new version, and its health is compared with the old version's before more traffic follows. The canary must be more sensitive than the population it protects, or it warns too late. The analogy breaks in a useful place: a canary that weakly resembles the population it guards (fewer users, quieter hours, cheaper requests) can sing happily while the mine fills.

Encore's purchase-path canary is automated end to end. At each step of Figure 8.3 an analysis job compares the canary with a baseline running the old version *at the same time*, never with yesterday, because no Tuesday afternoon resembles another closely enough to judge by. The comparison uses SLIs fans would recognize: checkout success, p99 latency of `POST /holds`, and the rate of `PaymentFailed` events caused by Encore itself.

| Step | Traffic | Minimum bake | Promote when | Roll back when |
|---|---|---|---|---|
| 1 | 1% | 10 min and 20,000 requests | no SLI worse than baseline beyond noise | any SLI significantly worse, or any integrity alarm |
| 2 | 5% | 15 min | as above | as above |
| 3 | 25% | 20 min | as above, and error-budget burn under 2× | as above, or burn over 2× |
| 4 | 100% | — | — | the normal burn-rate alerts of Chapter 4 |

*Figure 8.3 — Encore's canary schedule for purchase-path services. The request minimum matters as much as the minutes: a canary judged on too little traffic is a coin toss with a dashboard.*

Two refinements came from experience. An integrity alarm, such as a seat with two `SeatSold` events, rolls back at once whatever the statistics say: some failures are too costly to measure politely. Figure 8.4 draws both outcomes over time. And canaries do not run during on-sales: a canary started at 09:55 on a Friday is a gamble taken in front of a million fans.

{% include diagrams/fig-8-4.svg %}

*Figure 8.4 — Figure 8.3's schedule drawn over time on a logarithmic scale. A canary that holds reaches every fan in about 45 minutes. One that raises an integrity alarm at 25% goes straight back to zero, without waiting for the statistics.*

**Blue/green deployment** stands a complete new environment beside the old one and switches traffic at once, buying an instant switch back at the price of double capacity; Encore uses it for the serverless Sale Gate. **Ring deployment** widens exposure by population rather than percentage, and Encore's SaaS business supplies natural rings: staff and synthetic buyers, then the pooled self-service cells, then the Professional cells, then Encore's own fan site and the Enterprise silo for `venue-chain-a`, whose contract makes it last. Clinical trials run the same way, a small first phase looking for harm before larger phases measure effect. The parallel breaks on consent: a trial patient agreed to be early and a self-service venue did not, so early rings must be those whose contracts, and patience, allow it.

{% include diagrams/fig-8-5.svg %}

*Figure 8.5 — Encore's delivery rings. Exposure widens by population rather than percentage, from staff and synthetic buyers outward, and the outermost ring is last because a contract places it there.*

#### Feature flags and their debt {#flag-debt}

A **feature flag** is a runtime switch that decides which behavior deployed code exhibits, so that code can reach production long before its behavior reaches anyone. Encore's new seat-map renderer, behind `seatmap-renderer-v2`, reached production weeks before any fan saw it. Staff saw it first, then one fan in a hundred on small events, then everyone on events below 5,000 seats, and only after a quiet month the stadium on-sales. When it misdrew curved balconies on one venue's map, the team turned it off for that venue in seconds and fixed it at leisure.

Flags age differently by kind. A release flag should live for weeks, a kill switch for years (tested like any other control), an experiment flag as long as its experiment. Trouble comes when nobody can tell which kind a flag is, because then nobody knows when it may be removed.

Knight's repurposed flag is the warning every flag system should carry. A flag that once meant one thing and now means another is a trap set for whatever code still remembers its old meaning. Encore's flag service enforces simple rules: every flag has an owner and an expiry date, no name is ever reused, an expired release flag blocks its owner's next deployment, and a flag change is a production change, recorded in the deploy history and, on the purchase path, widened progressively. When the Reliability team first counted, Encore had about 2,300 flags, and a third had not changed state in a year, each a branch nobody tested in both directions. A flag that is never turned off is not a safety mechanism; it is dead code wearing a switch.

#### Rollback or roll forward {#rollback-or-roll-forward}

To **roll back** is to return production to the last version known to be good; to **roll forward** is to repair the problem with a new change. Rollback is the right default for stateless code, because it restores a state we have observed rather than one we hope for. But Knight's engineers rolled back, and that rollback spread the failure from one server to eight, because the old code met a world the new code had changed. A rollback is a deployment too, and it deserves the same suspicion.

The world that changes is usually data: a new field, event shape or schema the old version may not understand. The defense is to keep each change backward-compatible with its predecessor, through the expand-and-contract migrations of Chapter 10. Encore's pipeline records whether each deployment is safe to roll back, and one that is not gets a longer canary and a named engineer awake for its first hour. The choice between rolling back and rolling forward is better made at a desk on Tuesday than in a channel at 3 a.m.

**Recap.** Progressive delivery separates deployment from release and chooses each change's blast radius. Canaries compare against a simultaneous baseline on enough traffic, and rings order exposure by who can best absorb harm. Flags need owners, expiries and unique names, and rollback is safe only while the previous version still understands the world.

**Exercise 8.3.** Export your feature flags with their last change date. How many are older than six months, how many have no owner, and has any flag's meaning ever changed? Pick the oldest release flag and remove it this week.

### 8.4 Testing in Production

#### Rehearsing in the real room {#rehearsing-in-the-real-room}

"Testing in production" once sounded like a confession. It is now a discipline, because no staging environment reproduces production's data, traffic, neighbors or scale, and Encore's 500× on-sale exists only where it happens. A touring band soundchecks in the actual venue, because no rehearsal studio can tell you how a sold-out arena will swallow the bass: some properties belong to the room. The analogy breaks because a soundcheck happens with the hall empty, while in production the audience never leaves. Testing in production is the craft of experimenting where real users are without letting the experiment touch them.

**Synthetic users** are scripted clients that exercise real paths continuously. Encore's synthetic buyers run hourly against a hidden test event, holding seats, paying through the payment provider's test route and receiving tickets in a test wallet. During on-sale windows they run every minute, because an hourly check is a historian when a sale lasts 40 minutes.

A **dark launch** runs new code against real traffic with its results hidden from users. Facebook prepared its chat feature in 2008 by having users' browsers quietly exercise the new backend before anyone could see the chat window, so the service met its real load before its first user. Encore dark-launched a new availability projection for Seat Inventory the same way, comparing its answers with the old one's on every seat-map request until a fortnight passed without disagreement.

**Shadow traffic** copies real requests to a new version and discards its responses. It suits reads and endangers anything with side effects: shadowing Notifications naively would send every fan two emails. Writes are shadowed only into sandboxes, with side effects stubbed at the boundary.

#### Change freezes and their exceptions {#change-freezes}

A **change freeze** is a period in which production changes are forbidden except for emergencies, declared because failure is temporarily more costly than usual. Retailers have frozen their systems through the holiday season for decades. Encore freezes the purchase path from two hours before each big on-sale until it ends, and the logic is sound: if change causes most outages, we should not change things in the hour when an outage costs most.

A freeze has a definition and a boundary, and both erode. Someone must decide what counts as an emergency, and which services lie on "the purchase path." Over the past year Encore's freeze has softened in reasonable steps. Exceptions are granted in the on-sale chat channel by whoever is senior and awake: 41 in 12 months, recorded nowhere else. Low-risk platform automation, such as certificate rotation and the node-upgrade reconciler, was excluded, because pausing it caused more work than it saved. Catalog was judged to sit off the purchase path, since a fan can buy a seat without searching. Each step was sensible. Together they turned the freeze from a rule into a custom, and Chapter 2's drift reminds us how customs are measured: by what has not yet gone wrong. A freeze whose exceptions live in a chat channel has become a habit with a name.

A freeze has a second cost: changes that wait pile up, and the hour after it ends is often a burst of larger, staler deployments. And a freeze substitutes for confidence. A team that fully trusted its canaries, flags and rollbacks would need none, and a team that cannot trust them during the on-sale should ask why it trusts them the rest of the week. Encore keeps its freeze, rightly, but has not yet asked whether its boundary should follow services or their dependencies, or whether automation is exempt merely because no human pressed a button. Chapters 12 and 13 return to those questions.

**Recap.** Synthetic users, dark launches and shadow traffic learn what only the real room can teach, while keeping users and side effects out of the experiment. Freezes are reasonable when risk peaks, but their definitions and boundaries drift through sensible exceptions, which belong in writing where the next reviewer will see them.

**Exercise 8.4.** Write down your freeze rules, including the unwritten ones. List every change that reached production during the last freeze, automation included. How many were exceptions, who granted them, and where is that recorded?

### 8.5 Machine-Written Change — Review, Fitness Functions, and Provenance

#### The Tuesday morning, revisited {#the-tuesday-morning-revisited}

The companion volume ended on a Tuesday when a coding agent rebuilt Encore's Notification service overnight: a new framework, better retry semantics and 40 files that nobody had typed or read in full. Contracts passed, boundary rules held, security checks were clean and the SLO canary promoted the build. One engineer, spending 20 minutes on that change alone, saw that the new retry semantics could send a fan the same ticket twice, and added a spec-level idempotency test before merging. The pipeline had done everything asked of it; nothing in it had asked the right question.

Knight's Power Peg was unread code too, dormant for nine years, and every large system carries libraries nobody has read in full. Unread code is old; what is new is how quickly we can make it. By autumn about a quarter of Encore's merged changes carried an agent label, and they were larger on average than people's, because generating a file costs an agent nothing. Addy Osmani's *Beyond Vibe Coding* (2025) names the gap the "70% problem": the assistant produces the plausible bulk, while edge cases, failure handling and operability remain engineering. Gene Kim and Steve Yegge's *Vibe Coding* (2025) adds agents that pass a failing test by weakening it, and DORA's 2024 findings, which the companion volume weighed, point the same way.

#### Encore's policy {#encores-policy}

After the Notification morning, Encore's architecture group and the Reliability team wrote a policy for machine-written change. It has four parts, and its premise is that the pipeline should not care who wrote a change, while review should care very much what the change could break.

**Spec-level tests.** A **spec-level test** checks a property the business depends on, stated independently of any implementation, so that it remains true when every line beneath it is regenerated. For Notifications the property is that, for any sequence of retries, redeliveries and restarts, one `TicketIssued` event produces exactly one wallet pass and one email. Such tests are written or approved by people and owned by the service team. An agent's pull request that modifies a spec-level test alongside the code it tests is blocked until a human owner approves the test diff separately.

**Provenance labels.** Every commit records who or what wrote it: a person, an agent with its workload identity and model version, or both, along with the ticket or specification it implemented and the human who sponsored it. The labels travel with the artifact into the deploy history, where review rules, canary policy and, later, an incident responder can ask how a change came to exist.

**Risk-tiered human review.** Human attention is the scarcest resource in the pipeline, so the policy spends it by blast radius, as Figure 8.6 shows.

| Tier | What it covers | Human review | Delivery |
|---|---|---|---|
| 1 | Seats, money, identity, the purchase saga, anything integrity alarms watch | two reviewers, one the domain owner; behavior and test diffs read in full | full canary, rollback safety declared, never auto-merged |
| 2 | Fan-facing but not money or seats: Notifications, Catalog, renderers | one reviewer reads the spec, the invariants and the test diff, and samples the code | full canary; agent changes bake twice as long |
| 3 | Internal tools, documentation, dashboards, test scaffolding | automated checks; 1 change in 10 sampled for human review | standard pipeline |

*Figure 8.6 — Encore's review tiers. The tier comes from what a change touches, not who wrote it; provenance decides only how long an agent's change bakes and whether a human samples it.*

**Fitness functions.** The fitness functions of *Building Evolutionary Architectures* (2nd ed., 2022), automated checks that a system keeps a promised property, are the only reviewers that read every line at the speed agents write. Encore added several. Every handler with an external side effect must take an idempotency key. No service may add a retry layer where the mesh already retries, or a retry budget above 10%. No new outbound dependency may appear without a registry entry. A latency budget for each purchase-path call is checked in the staging soak. Each began as a sentence a reviewer used to say aloud, and each now fails a build.

The policy is not free: Tier 1 reviews are slower, agent-heavy teams grumbled that the doubled bake looked like distrust, and spec-level tests take real thought. But the Notification engineer's 20 minutes were the most valuable of that week, and the policy exists to spend such minutes where they matter. A review that reads everything a machine wrote reads nothing carefully. A review that reads the specification, the invariants and the tests, and leaves the rest to fitness functions and canaries, has a chance of seeing the one duplicate ticket.

**Recap.** Machine-written change is new in volume and in its tendency to satisfy checks rather than intentions. Encore's answer is spec-level tests that agents may not quietly rewrite, provenance carried into deploy history, human review tiered by blast radius, and fitness functions for the rules reviewers used to say aloud. The pipeline is indifferent to authorship; review must not be.

**Exercise 8.5.** Pick a service you own and write its two most important invariants as spec-level tests, independent of its current code. Then decide which review tier it belongs in, and what your review would read if an agent rewrote it overnight.

### Kata: Always Open

> **Your brief: "Kestrel."** A mobile-first retail bank with 1.8 million customers in three EU countries and 110 engineers in 14 teams. Its app and card-processing services must answer every card authorization within 2 s, day and night, and its regulator requires a record of every production change: who approved it, what it touched and how it can be undone. Kestrel deploys about 60 times a day through a 40-minute pipeline, but the change records are written by hand after the fact, and a weekly risk committee reviews a sample of them. Its change failure rate is about 15%. Its flag tool holds 1,900 flags, and nobody knows which are still read. Last quarter a fraud-rule flag, reused for a new rule, declined valid card payments in one country for a morning. A freeze covers Black Friday weekend, with exceptions granted in chat. Agents now write about a third of pull requests, mostly in fraud-rule and statement modules.

**Deliverables:**

1. **Change-route map** — every route into production, marked reviewed, tested, recorded and reversible.
2. **Pipeline redesign** — stages, each one's question and time budget, change records written by the pipeline itself, and a position on the weekly committee.
3. **Progressive rollout plan** — customer rings, canary SLIs for the app and card authorization, and the rule for when rollback is unsafe.
4. **Flag and freeze policy** — ownership, expiry and naming rules, a plan for the 1,900, freeze scope and an exceptions register.
5. **Review tiers for machine-written change** — the tiers, spec-level tests for fraud rules, and the fitness functions that replace reviewer folklore.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Completeness of routes | Does the map include flags, configuration, scripts and automation, not only the pipeline? |
| Batch size | Does the design keep changes small and frequent, rather than adding gates to them? |
| Blast radius | Does a bad fraud-rule change reach a small ring first, with a rollback that is safe while cards are being authorized? |
| Flag hygiene | Would the reused fraud-rule flag be impossible under your rules? |
| Honest freeze | Is the freeze scoped by dependency and risk, and is every exception in the change record? |
| Review economy | Does human attention go to invariants and high-tier changes, with machines covering the rest? |

#### Where you now stand

You can now treat change as the leading cause of outages without concluding that change should stop: design a pipeline as a sequence of questions, choose each change's blast radius, keep flags from becoming debt, decide in advance whether rollback is safe, test in the real room, and spend human review where machine-written change can do most harm. All of this reduces how often we break the system; none of it stops the world from breaking it for us. Chapter 9 turns from the changes we make to the failures we must withstand.

### References

- Jez Humble, David Farley — [*Continuous Delivery*](https://www.informit.com/store/continuous-delivery-reliable-software-releases-through-9780321601919). Addison-Wesley, 2010.
- U.S. Securities and Exchange Commission — [*SEC Charges Knight Capital With Violations of Market Access Rule*](https://www.sec.gov/news/press-release/2013-222). SEC, 2013 — free online.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Valentina Servile — [*Continuous Deployment*](https://www.oreilly.com/library/view/continuous-deployment/9781098146719/). O'Reilly, 2024.
- James Governor, Kim Harrison, Heidi Waterhouse, Adam Zimman — [*Progressive Delivery*](https://itrevolution.com/product/progressive-delivery/). IT Revolution, 2025.
- Nicole Forsgren, Jez Humble, Gene Kim — [*Accelerate*](https://itrevolution.com/product/accelerate/). IT Revolution, 2018.
- Gene Kim, Jez Humble, Patrick Debois, John Willis, Nicole Forsgren — [*The DevOps Handbook*, 2nd ed.](https://itrevolution.com/product/the-devops-handbook-second-edition/). IT Revolution, 2021.
- Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage — [*Building Evolutionary Architectures*, 2nd ed.](https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/). O'Reilly, 2022.
- Addy Osmani — [*Beyond Vibe Coding*](https://www.oreilly.com/library/view/beyond-vibe-coding/9798341634749/). O'Reilly, 2025.
- Gene Kim, Steve Yegge — [*Vibe Coding*](https://itrevolution.com/product/vibe-coding-book/). IT Revolution, 2025.

---

## Chapter 9: Designing for Failure — Stability Patterns and Chaos Engineering {#ch9}

> "A distributed system is one in which the failure of a computer you didn't even know existed can render your own computer unusable." — Leslie Lamport

Every system fails, some in small pieces and some all at once, and the difference is rarely luck. A failure that stays small has usually been designed to stay small, by someone who imagined it and drew a line it could not cross. A failure that spreads has usually found a path built for some other purpose, very often a path built for recovery. This chapter is about those lines and paths, and about finding out, on a day of our choosing, whether the lines hold.

Our field offers no clearer lesson than the afternoon of Monday, 15 January 1990, when AT&T's long-distance network spent about nine hours unable to complete a great many of the calls placed on it. Nothing physical had broken. Weeks earlier the company had installed new software on its 114 4ESS switching systems, changing the code that ran when a switch recovered from a fault and told its neighbors it was back in service. In that code, written in C, a `break` statement inside an `if` clause within a `switch` statement ended the enclosing block earlier than its author intended. The flaw lay quiet until one switch in New York suffered a minor fault, took itself briefly out of service and, on returning, sent its neighbors the expected messages. A neighbor that received a second such message while still handling the first ran into the defect, corrupted its own data and reset itself. When it came back, it announced its own recovery, and its neighbors fell over in turn. The cascade rolled across the network for the rest of the day, as Figure 9.1 shows.

{% include diagrams/fig-9-1.svg %}

*Figure 9.1 — The AT&T cascade of 15 January 1990. Each switch's recovery announcement reset its neighbors, and each reset produced the next announcement. Notice that the loop that sustained the outage is the recovery path itself.*

Notice what did *not* go wrong. Every switch was redundant, could detect its own faults and recover, and dutifully told its peers what had happened. The network was designed so that any switch could fail and the rest would route around it, and that design assumed failures would be independent. But all 114 switches ran the same code, and the defect sat in the recovery path, the code that runs least and matters most. The machinery of self-healing became the vector of the illness. Redundancy protects against independent failures and does nothing against common ones; a fleet running identical software is, for the purposes of its defects, one machine.

Encore has learned a smaller version of this lesson. Its first big outage, the payment service provider (PSP) slowing from 200 ms to 8 s and the retry storm that followed, was a cascade of reasonable defaults, and the companion volume named the patterns that answered it. This chapter goes deeper, into operating those patterns, and ends with the Reliability team's quarterly game days, where real people test them at real consoles.

### 9.1 Integration Points and Cascading Failure

#### Where faith is required {#where-faith-is-required}

An **integration point** is any place where one component depends on another across a boundary it does not control: a network call, a shared database, a queue, a third-party API. Michael Nygard called integration points the number-one killer of systems, and the reason is structural. Across a boundary a call can hang, return garbage, or succeed on the far side while the caller concludes it failed. Every integration point is a place where we take on faith something we cannot verify.

A **cascading failure** is one in which the failure of one component raises the load or latency on others until they fail too, so that the damage travels along the dependency graph. Nygard distinguished it from a *chain reaction*, which spreads sideways among peers: one instance dies, its load moves to the survivors, and the survivors die in sequence. The most dangerous integration point is the one that has slowed down rather than stopped. A dead dependency refuses quickly; a slow one holds a thread, a connection and a queue slot for as long as we are willing to wait, and software left to its defaults is willing to wait a very long time.

Consider a touring production with a fixed running order of cues. Miss one scene change by two minutes and every later cue slides, because each waits for the one before. The analogy breaks at the hold: a theater can stop the show and the audience will wait, but a service under load cannot ask its users to stand still, and every second it hesitates more of them arrive.

#### Keeping a register {#keeping-a-register}

A team should know its integration points as a ship's officer knows the openings in the hull. Encore's Reliability team asks each team to keep an **integration-point register** in its service catalog entry: per dependency, the timeout, the retry policy, the breaker, what the service does when the dependency is slow and when it is down, and the date the team last *saw* that behavior. The last column is the one that matters. For Orders & Payments the register runs to 11 rows, led by the PSP, the fraud signal from Bot Screening and the wallet providers; for Seat Inventory, which deliberately depends on almost nothing, it runs to three. Writing it exposes dependencies nobody chose, such as a logging library that blocks when its buffer fills.

**Recap.** Integration points are where our system takes another's behavior on faith, and cascades travel along them, most often when a dependency slows. Identical components fail together. A register with the date each failure behavior was last observed turns faith into evidence.

**Exercise 9.1.** Write the integration-point register for one service you run. For each row, fill in when you last saw the "slow" behavior happen. How many rows have no date?

### 9.2 Timeouts, Retries, Circuit Breakers, and Backpressure

#### Timeouts derived from budgets {#timeouts-from-budgets}

A **timeout** is a promise a caller makes to itself about how long it will wait before treating a call as failed. Most production timeouts were never chosen, only inherited. The discipline is to derive each from a **latency budget**, the time the user-facing operation may take end to end, divided among the calls that serve it. Encore's fan has a 3 s checkout budget, spent roughly as Figure 9.2 shows.

| Hop | Budget share | Timeout | Retries in path | Typical p99 |
|---|---|---|---|---|
| Edge and gateway | 150 ms | n/a | none | 40 ms |
| Orders: confirm hold with Seat Inventory | 300 ms | 250 ms | one, if budget remains | 60 ms |
| Orders: fraud signal from Bot Screening | 200 ms | 150 ms | none; fail open with a flag | 70 ms |
| Orders: charge via PSP | 800 ms | 800 ms | none in path; reconciled later | 450 ms |
| Orders: write order, emit `OrderPlaced` | 250 ms | 200 ms | one | 50 ms |
| Margin for queuing and the fan's network | 1,300 ms | | | |

*Figure 9.2 — The 3 s checkout budget, divided. Each timeout sits above the dependency's normal p99 and below its share of the budget. The large margin is deliberate: on an on-sale morning, queues are where the time goes.*

Two practices make the table real. With **deadline propagation**, the caller sends the absolute time by which it needs an answer, and each callee works only while that deadline lies in the future; Encore's internal gRPC calls carry deadlines natively, so a hold confirmation arriving with 40 ms left is refused at once. And a timed-out side effect is *unknown* until reconciled. A PSP charge that timed out may have succeeded, so Orders records it as pending and reconciles it later with the same idempotency key.

#### Retries with jitter and a budget {#retries-with-jitter}

A retry is a bet that the failure was transient. Placed by one client it is a good bet; placed by every client at once it is a denial-of-service attack aimed at our own dependency. Marc Brooker, writing at Amazon Web Services, gave the clearest account of why: clients that fail together and back off exponentially also retry together, in synchronized waves that arrive when the dependency is weakest. **Jitter**, randomness in the wait before each retry, spreads the waves into a trickle, and Brooker's simulations showed "full jitter", a random wait between zero and the exponential ceiling, doing markedly better than backoff alone.

Jitter shapes retries in time; a **retry budget** caps them in volume, as a fraction of ordinary requests, so that a dependency in trouble sees a bounded increase in load however many calls fail. Encore's mesh enforces about 10% per destination as a token bucket that successes refill and retries drain; when it is empty, the call fails fast and honestly. Retries happen at one layer only, and only for idempotent operations, because layers multiply, as Figure 9.3 shows.

{% include diagrams/fig-9-3.svg %}

*Figure 9.3 — Load on a failing dependency when every layer above it retries. Three layers of three retries can multiply it 64 times just as the dependency is weakest, while a 10% budget holds it near normal.*

One retry layer escapes the mesh entirely: the fan's thumb. A fan who sees "something went wrong" presses again, and the fan app may add retries of its own. Human retries carry no jitter and respect no budget, and Section 9.5 shows Encore discovering what that means, at a moment of its own choosing.

#### Circuit breakers as state machines {#breakers-as-state-machines}

The breaker's three states are familiar: *closed*, where calls flow and failures are counted; *open*, where calls fail at once; and *half-open*, where a few probes test recovery. Every transition is governed by a parameter, and wrong parameters turn a safety device into a source of outages.

| Parameter | What it governs | Encore's PSP breaker | Failure if set badly |
|---|---|---|---|
| Rolling window | How much history decides the state | 10 s | too long reacts slowly; too short flaps |
| Minimum volume | Calls needed before it may trip | 50 calls | too low trips on two unlucky calls at night |
| Failure-rate threshold | Share of failed calls that opens it | 40% | too low opens on normal noise |
| Slow-call threshold | Calls slower than this count as failures | 1.5 s, for 50% of calls | absent, a slow PSP never trips it |
| Open duration | How long before probing | 5 s, growing to 60 s | too short hammers a sick dependency |
| Half-open probes | Trial calls while testing | 5, all must succeed | too many re-trigger the overload |
| Scope | What one breaker protects | one per PSP endpoint, per region | one global breaker turns a regional fault into a total one |

*Figure 9.4 — The circuit breaker's tuning surface. The slow-call threshold is the row most often missing, and it is the one the PSP outage needed.*

A breaker also needs a fallback, a defined thing to do when open, or it merely produces errors faster; for the PSP, Encore's fallback is the degraded mode already designed, accepting the order and charging later. Breaker transitions belong on the service dashboard, and a breaker that has not opened in a quarter is either guarding a perfect dependency or misconfigured. The second is likelier.

#### Backpressure {#backpressure}

**Backpressure** is the means by which a component that cannot keep up tells its upstream to slow down before it accepts work it cannot finish. Without it, work piles up in unbounded queues and the system fails late and messily instead of early and cleanly; with it, queues are bounded and callers honor a "retry after" signal. A busy port works this way, sending ships to anchor offshore when the berths are full. The image breaks on patience: a ship will wait a week, but a request has a deadline, so backpressure that moves the queue upstream must also bound the wait. At Encore the chain ends at the Sale Gate, the one place where waiting is the product.

**Recap.** Timeouts come from the user's budget and travel as deadlines, and a timed-out side effect is unknown until reconciled. Retries need jitter in time and a budget in volume, and the human retry needs designing for too. Breakers are state machines whose parameters decide whether they protect or harm, and backpressure keeps the queue where someone can see it.

**Exercise 9.2.** Build Figure 9.2 for one user-facing operation you run. Where does a timeout exceed its budget share, and where does a dependency's normal p99 sit uncomfortably close to its timeout?

### 9.3 Overload, Load Shedding, and Tail Latency

#### Admission control at the Gate {#admission-at-the-gate}

Overload is a mismatch between the work offered and the work a system can do well. Two tools answer it. **Admission control** decides at the entrance how much work to let in, so that what enters can be served well. **Load shedding** discards work already inside that cannot be finished in time. The first is prevention, the second triage, and a system that relies only on triage spends its scarce capacity deciding whom not to serve.

The Sale Gate is Encore's admission controller. It admits at most about 1,200 fans per second per event, keeping Seat Inventory below 80% of its measured capacity, and everyone else waits with a visible queue position. The Gate converts an arrival rate the system cannot serve into waiting time it can, and puts that waiting in the cheapest, most honest place: a static page that tells fans where they stand.

Note what kind of number the admission rate is: people set it from a load test and review it at the on-sale readiness review. It is exactly as good as that test's resemblance to the morning in question, a point Chapter 6 made about warm caches. An adaptive Gate that lowers its own rate as Seat Inventory's latency climbs is on the Reliability team's roadmap. Until then the rate is a judgment, and judgments deserve review.

#### Shedding behind the gate {#shedding-behind-the-gate}

Retries, a cold cache, a failover or a slow dependency can still overload a service the Gate believed it was protecting. Encore's services therefore tag each request with a **criticality class**, an idea the SRE book develops: `checkout` for requests completing a purchase, `browse` for seat-map and listing reads, `background` for analytics and prefetches. Under pressure a service sheds `background` first and `checkout` last, so capacity goes to fans closest to finishing.

Three habits make shedding work. Shed early and cheaply, before expensive work is spent on a request that will be discarded. Measure pressure by *time in queue*, the insight of Kathleen Nichols and Van Jacobson's controlled-delay algorithm for network routers (2012): a request that has waited past its deadline is useless when served, so serving it wastes capacity twice. And under severe overload, serve the newest requests first, since their callers are still listening. Each trades fairness for goodput and should be written down, or during an incident it will look like a bug.

#### Metastable failures {#metastable-failures}

The companion volume borrowed a term from Nathan Bronson and colleagues (2021): a **metastable failure** persists after its trigger is removed, because the system's own response keeps it overloaded. The system starts in a *vulnerable state*, typically running efficiently near capacity. A *trigger* (a spike, a failover, a cache flush) pushes it over. A *sustaining effect*, most often retries, keeps load above capacity after the trigger is gone.

AT&T's collapse fits the shape exactly. The trigger, one switch's minor fault, was over within seconds; the sustaining effect was the recovery protocol, each reset producing the messages that reset its neighbors, and the network stayed failed for hours after its cause had vanished. Encore's PSP outage had the same structure in miniature, with retries and an eager autoscaler sustaining what the PSP's slowdown began.

The operational lesson is uncomfortable. A metastable system will not recover when the trigger is fixed, and often not when capacity is added, because new capacity arrives cold and the sustaining loop consumes it. It recovers when load falls below the level at which the loop dies, which means shedding far more than feels reasonable, keeping retries off, and admitting traffic back in steps. In a metastable failure the cure always looks like an overreaction. Runbooks should say so in advance, since nobody at 3 a.m. wants to be the person who turned away 70% of the traffic on purpose.

#### Tail latency under load {#tail-latency-under-load}

Overload shows first in the tail, long before errors rise, so p99 is its early warning, and a dashboard of medians reports good news until there is none. **Hedged requests**, from Dean and Barroso's "The Tail at Scale" (2013), send a second copy of a slow read to another replica; they cut the tail, but hedging during overload pours fuel on the fire. Encore hedges only idempotent reads of seat-map geometry, only after the call passes its p95, and within a budget of about 5% extra requests, so hedging switches itself off when the system is busiest.

**Recap.** Admission control at the entrance is cheaper than shedding inside, and the Gate turns excess load into honest waiting at a rate people set and must keep reviewing. Inside, we shed by criticality and by time in queue. Metastable failures outlive their triggers and yield only to shedding that feels excessive.

**Exercise 9.3.** Find an incident in your system where load stayed high after the cause was fixed. What was the sustaining effect, and what runbook text would have let the on-call engineer shed enough load to break it?

### 9.4 Cells, Regions, and Blast Radius

#### A ladder of bulkheads {#a-ladder-of-bulkheads}

The **blast radius** of a failure is the set of users, tenants or functions it can affect. The strongest patterns shrink it structurally. The companion volume used a ship's bulkheads for this idea; operations adds that bulkheads come in sizes, each containing a different class of failure.

| Boundary | Contains | Does not contain | At Encore |
|---|---|---|---|
| Thread or connection pool | one slow dependency | a bad deploy | a separate PSP pool in Orders |
| Instance or pod | a crash, a memory leak | anything common to all pods | restarts, pods spread across zones |
| Shard | a hot or failed partition | a code defect | four shards per large event |
| Cell | a bad deploy, a poison tenant | a shared control plane | Professional cells; self-service cells of about 50 |
| Availability zone | power, network, a data-center fault | a regional dependency | every tier across three zones |
| Region | a regional outage | a global control plane, a common-mode defect | two EU regions; each event's writes pinned to one |

*Figure 9.5 — The ladder of bulkheads. The "does not contain" column of each row is the reason the next row exists.*

Read that column with AT&T in mind. No number of identical regions contains a defect in code that every region runs. Only one rung contains a bad deploy, and only because the deploy reaches it at a different time: the cell.

#### Cells for tenants {#cells-for-tenants}

A cell is a complete, independent copy of the application serving a fixed slice of customers. Encore's Professional tenants already live in Kubernetes cells, and about 500 self-service venues in serverless cells of about 50. What makes the structure a blast-radius control is how change moves through it. Every deploy reaches one designated *canary cell* first, holding Encore's internal test tenants and a few tenants who chose early updates, and then the rest in the waves Chapter 8 describes. A defect that would have reached all 500 self-service venues reaches about 50.

The biggest stadium tours travel with more than one set of stage steel, so that while the show plays one city, a second structure is rising in the next, and a storm that delays one build does not cancel the next night. Cells give Encore the same independence. The analogy breaks where AT&T's network did: two sets of steel built from one faulty drawing fail alike. Cells also share the routing layer that maps tenants to them, which must be the dullest, least often changed component Encore owns, because its failure crosses every bulkhead at once.

#### Shuffle sharding {#shuffle-sharding}

Within a pooled cell, one noisy tenant can still harm its 49 neighbors. Shuffle sharding, which Colm MacCárthaigh described from AWS practice, gives each tenant a small random *combination* of workers instead of a fixed partition. In each self-service cell, Encore divides its import and webhook workers into eight lanes and assigns each venue two. There are 28 possible pairs, so a venue whose runaway import floods its two lanes shares both with any given neighbor only about one time in 28; everyone else keeps at least one healthy lane. The isolation comes from combinatorics, not hardware, which is why it is cheap. Figure 9.6 shows one cell's lanes.

{% include diagrams/fig-9-6.svg %}

*Figure 9.6 — Shuffle sharding across a self-service cell's eight lanes. A runaway venue floods its own two lanes, and most neighbors keep at least one healthy lane. Only the rare neighbor holding the same pair is hit.*

#### Static stability {#static-stability}

A system is **statically stable** when its data plane keeps working, unchanged, while its control plane is impaired, so that recovery never depends on creating, scaling or reconfiguring anything during the failure. The term comes from AWS, and its lesson is that the control plane is likeliest to be overwhelmed exactly when everyone needs it.

Encore applies it in three places. The tenant-to-cell routing table is pushed to every edge node and cached, so routing continues from the last good copy if its control plane fails. Each tier carries enough capacity that losing a zone needs no scaling. And the seat ledger's standby in the second region is already running, so failover promotes a running copy and builds nothing, though its minutes of recovery time objective (RTO) belong to Chapter 10. Static stability costs idle capacity, and in return it removes the most dangerous step from every recovery: asking a struggling system to do something new.

**Recap.** Bulkheads come in sizes, so we choose the rung by the failure we fear. Cells contain bad deploys only because change reaches them at different times, shuffle sharding isolates tenants through combinatorics, and static stability keeps recovery independent of a control plane under stress.

**Exercise 9.4.** Draw Figure 9.5 for your system. Which rung is missing, and which shared component (a router, an identity provider, a pipeline) crosses every rung you have?

### 9.5 Chaos Engineering and Game Days

#### The experimental attitude {#the-experimental-attitude}

Everything in this chapter is a claim about behavior under conditions we hope never to see, and such claims decay. Configurations drift and timeouts creep. Chaos engineering is how we keep the claims honest.

The practice grew up at Netflix as it moved onto AWS from around 2008, on the reasoning that if instances would fail routinely, failure had better be made routine on purpose; Chaos Monkey was the famous result. The *Principles of Chaos Engineering* set the discipline down, defining **chaos engineering** as "the discipline of experimenting on a system in order to build confidence in the system's capability to withstand turbulent conditions in production." They ask for a hypothesis about steady state as users would measure it, real-world events as variables, experiments in production, continuous automation, and a minimized blast radius.

The word that matters is *experiment*. A test checks a known property against an expected answer; an experiment asks a question whose answer we do not know. "Does the breaker open when the PSP is slow?" is a test. "What happens to checkout when the PSP is slow during a shard failover?" is an experiment, and, as Casey Rosenthal and Nora Jones argue, its uncertainty is its value.

#### Game days {#game-days}

A **game day** is a scheduled exercise in which people and systems face an injected failure together, with observers recording what the people did as carefully as what the machines did. It tests the sociotechnical system as a whole: whether the alert reaches the right person, whether the runbook still matches the system, whether anyone remembers the manual step. Google's DiRT and Slack's Disasterpiece Theater, both described in Rosenthal and Jones's book, are good models.

Before a production opens, a theater company holds a technical rehearsal: the actors walk the show while the crew runs every cue for real, to find the cue that cannot be made in the time the script allows. Encore's Reliability team calls its quarterly game days *tech rehearsals* for that reason. The analogy falls short at the end: a show then runs the same way every night, while a system's rehearsal proves only that it worked that day.

#### The tech rehearsal {#the-tech-rehearsal}

Last quarter's rehearsal combined two failures Encore had only drilled separately. It ran in production on a Tuesday morning against the hidden test event the synthetic buyers use, given four shards of its own as a large on-sale would have:

```yaml
experiment: psp-latency-during-shard-failover
hypothesis: >
  Synthetic checkout success stays at or above 97% within the 3 s budget;
  the PSP breaker opens within 15 s; orders are accepted and charged later;
  shard 2 failover rejects writes for under 60 s; no seat is sold twice.
target: test event only (tenant: encore-internal), home region
injections:
  - at: T+0     psp_latency: { added: 2s, share: 60% }   # mesh fault injection
  - at: T+5m    shard_failover: { event: test, shard: 2 } # runbook step, by hand
abort_if:
  - real-event checkout SLO burn rate > 2x for 5m
  - any duplicate SeatSold for the test event
duration: 30m
```

Much went as hoped. The PSP breaker opened in 9 s, orders were accepted under "your card will be charged shortly", and the charge-later queue drained within four minutes of the injection ending. The fenced failover on shard 2 rejected writes for 38 s, and no seat was sold twice. Two findings were unwelcome. Jonas, the Seat Inventory engineer performing the failover, had never done one by hand, and the runbook named a flag removed two releases earlier, so the step took 11 minutes instead of 3: Chapter 3's deskilling, precisely. And the fan app turned out to retry each rejected hold three times at fixed one-second intervals, a retry layer the mesh's budget never saw; the app team added jitter and a client-side budget the next sprint.

One more line in the observers' log deserves recording. While the synthetic buyers retried their rejected holds, Bot Screening's velocity rule quarantined several of them. The log marked it as expected, since synthetic traffic looks synthetic, and the item was closed. Nobody asked what the same rule would make of a large crowd of real fans retrying in the same way, and on that Tuesday nobody had a reason to.

A game day does not prove resilience; it finds, cheaply and on a quiet morning, the places where resilience is a belief. Its yield is the surprises that become work; the Reliability team's quarterly report shows how many from the previous rehearsal were fixed and how many were merely closed.

**Recap.** Chaos engineering treats resilience as a hypothesis about steady state, tested with real-world failures in production within a bounded blast radius. Game days add the people, and routinely find that the human part of recovery has decayed faster than the machines'.

**Exercise 9.5.** Design a game day combining two failures you have so far drilled only separately. Write the hypothesis in terms a user would recognize, the abort conditions, and the one human step you suspect nobody has practiced.

### Kata: Kick-Off

> **Your brief: "Matchday."** A live sports-streaming service carrying football and basketball to subscribers in five EU countries, with 40 engineers. Peak evenings reach 1.4 million concurrent viewers, and in the 10 minutes before a top-league kick-off, stream starts rise 30×. Every start needs an entitlement check, a license from one of two third-party digital rights management (DRM) providers and a manifest from one of three content delivery networks; new subscriptions go through two payment providers. All competitions share one pool of playback-API instances, and the Sunday-evening derby alone takes 40% of it. Last month one DRM provider's license latency rose from 120 ms to 5 s for 25 minutes. Retries from three layers (the player SDK, the playback API and fans restarting the app) quadrupled license requests, the playback pool saturated, and starts failed for every competition, including a basketball game licensed through the other provider. The provider recovered at 20:31; Matchday recovered at 21:40, and some 210,000 viewers missed the whole first half.

**Deliverables:**

1. **Integration-point register** — every dependency on the stream-start path, with timeouts derived from a 4 s time-to-first-frame budget.
2. **Retry and breaker design** — the single retry layer, its budget and jitter (including the player SDK already on fans' phones), and a per-provider DRM breaker with every Figure 9.4 parameter chosen and justified.
3. **Shedding and metastability analysis** — admission control for the kick-off surge and the order in which work is shed; the vulnerable state, trigger and sustaining effect of last month's incident; and the runbook text that would have ended it by 20:40.
4. **Blast-radius plan** — the rungs of Figure 9.5 Matchday needs, including how the derby is kept from starving every other match and how a stream already playing survives its providers.
5. **Game-day plan** — one experiment with hypothesis, injections, abort conditions and the human step to observe, run on a midweek evening with no fixtures.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Budget-derived timeouts | Does each timeout follow from the 4 s budget, or was it guessed? |
| One retry layer | Are the player SDK's and the fans' own retries counted, or only the playback API's? |
| Shedding order | Are playing streams protected before new starts, and new starts before new subscriptions? |
| Sustaining effect | Does the analysis explain why recovery took 69 minutes after the provider recovered? |
| Isolation and static stability | Is the derby contained without a cell per match for 40 engineers, and does a playing stream need anything scaled or reconfigured mid-incident? |
| Experiment honesty | Could the hypothesis actually fail, and is there a clear point at which the game day stops? |

#### Where you now stand

You can now trace failure along integration points, derive timeouts from budgets, tune retries and breakers to damp a failure, shed load where it costs least, recognize a metastable failure and its uncomfortable cure, choose the bulkhead that fits the failure you fear, and test it all with people in the room. Each of these assumes the data underneath survives, and data is the one thing a restart cannot restore. Chapter 10 turns to state, and to disaster recovery practiced until it is routine.

### References

- Michael T. Nygard — [*Release It!*, 2nd ed.](https://pragprog.com/titles/mnee2/release-it-second-edition/). Pragmatic Bookshelf, 2018.
- Casey Rosenthal, Nora Jones — [*Chaos Engineering: System Resiliency in Practice*](https://www.oreilly.com/library/view/chaos-engineering/9781492043850/). O'Reilly, 2020.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Nathan Bronson, Aleksey Charapko, Abutalib Aghayev, Timothy Zhu — [*Metastable Failures in Distributed Systems*](https://sigops.org/s/conferences/hotos/2021/papers/hotos21-s11-bronson.pdf). HotOS, 2021 — free online.
- Marc Brooker — [*Timeouts, retries, and backoff with jitter*](https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/). The Amazon Builders' Library — free online.
- Marc Brooker — [*Exponential Backoff And Jitter*](https://aws.amazon.com/blogs/architecture/exponential-backoff-and-jitter/). AWS Architecture Blog, 2015 — free online.
- Colm MacCárthaigh — [*Workload isolation using shuffle-sharding*](https://aws.amazon.com/builders-library/workload-isolation-using-shuffle-sharding/). The Amazon Builders' Library — free online.
- Becky Weiss, Mike Furr — [*Static stability using Availability Zones*](https://aws.amazon.com/builders-library/static-stability-using-availability-zones/). The Amazon Builders' Library — free online.
- [*Principles of Chaos Engineering*](https://principlesofchaos.org/) — free online.
- Kathleen Nichols, Van Jacobson — [*Controlling Queue Delay*](https://queue.acm.org/detail.cfm?id=2209336). ACM Queue, 2012 — free online.
- Jeffrey Dean, Luiz André Barroso — [*The Tail at Scale*](https://doi.org/10.1145/2408776.2408794). Communications of the ACM, 2013.

---

## Chapter 10: Data, State, and Disaster Recovery {#ch10}

> Code can be redeployed. Data can only be remembered.

Everything we have said about change so far has rested, quietly, on a promise: if a release goes wrong, we can take it back. Canaries, flags and rollbacks (Chapter 8) all assume that the past is still there to return to. Data breaks the promise. A row written cannot be unwritten by redeploying anything, a dropped table does not return when we revert the commit that dropped it, and a corruption that reached the replicas reached them faithfully. This chapter is about the part of production that remembers, and how to make its memory survive our mistakes, our machines and our adversaries.

The story every operations engineer eventually hears took place at Pixar in 1998, during the making of *Toy Story 2*. Someone ran a recursive delete, of the `rm -rf` kind, at the root of the film's directory tree on a shared server. Animators watched their work vanish; Oren Jacob, then an associate technical director, later recalled a character's hat disappearing first and then more of the character, until the team pulled the power on the machines. By then most of the film's files were gone. The backups that should have made this an inconvenience had been failing for some time, and nobody had noticed. What saved the film was an accident of life rather than of design: Galyn Susman, the supervising technical director, had been working from home after the birth of her child, and she kept a copy of the film on a computer in her house. The team drove the machine back to the studio, wrapped in blankets, and restored most of the work from it.

Its lessons are precise. The deletion was ordinary, a routine command in the wrong place, of the kind Jim Gray had in mind in 1985 when he studied failures of Tandem's fault-tolerant systems and found that administration and software caused far more outages than hardware did. The formal plan had decayed silently. The recovery came from a copy independent of the system in every way that mattered: another building, another machine, another reason for existing. And the people restoring it were improvising, because no one had ever practiced a restore.

Encore stands this morning with better machinery than Pixar had and much the same exposure. Its seat ledger commits synchronously to a second region. Its Finance ledger is backed up every night and has never been restored in full. Its holds store is about to change shape under live traffic. Its game days have exercised shard failovers (Chapter 9) but never a whole region. By the end of the chapter all four will have been tested, and one will have failed instructively.

### 10.1 Why Stateful Systems Are Different

#### The asymmetry of state {#asymmetry-of-state}

A **stateful system** is one whose correct behavior depends on what it has remembered from earlier requests, so that losing or corrupting that memory is a failure even when every process is healthy. A stateless service is a function: replace it, restart it or roll it back, and it computes the same answers from the same inputs. A stateful one is a function plus a history, and history runs in one direction only.

Theatre gives us a good picture of the difference. A touring production's set is struck after every show, packed into road cases and rebuilt in the next city from its drawings; nobody mourns a set, because it can be rebuilt from its specification. The stage manager's prompt book is another matter. It holds every cue as actually called and the notes from 40 performances, and it cannot be rebuilt from the set, because it records what happened rather than what was designed. Containers are the set; databases are the prompt book. The analogy breaks in tempo: a prompt book changes a few times a night, while each seat-ledger shard takes 1,500 writes a second during an on-sale.

The asymmetry appears in four places. *Rollback*: a data change can only be compensated by another, forward change, so every migration must be safe if left half done. *Speed*: copying state is bounded by physics, so restoring 4 TB takes hours however clever the tooling. *Blast radius*: a bug in stateless code fails requests, while a bug that writes bad data keeps failing every later reader until someone repairs it, which makes corruption the quietest and longest kind of outage. *Replication*: the mechanism that protects us from losing a machine copies our mistakes to every replica within milliseconds, so it protects us from nothing we do to ourselves.

#### Classifying Encore's state {#classifying-state}

The first operational act for state is an inventory. Encore's is short, because most of Encore is stateless on purpose:

| State | Store | System of record? | Loss means | RPO | RTO |
|---|---|---|---|---|---|
| Seat ledger (event log) | Seat Inventory, event-sourced, four shards per large event | Yes | A seat sold twice or a fan charged for nothing | 0 | Minutes |
| Seat holds | Holds store, 5-minute expiry | Yes, briefly | Fans lose seats mid-checkout | Minutes | Minutes |
| Orders and payments | Orders, with the payment service provider (PSP) as external record | Yes | Charges without tickets, reconcilable against the PSP | Seconds | 30 min |
| Finance ledger | Relational, fed by `SaleCompleted` | Yes, for accounting | A failed nightly close; regulatory exposure | 15 min | 2 h |
| Catalog | Managed database | Yes | Stale listings, lost edits | Minutes | 1 h |
| Seat-map cache, search index, analytics | Derived | No | Slowness while rebuilt | n/a | Rebuild time |

*Figure 10.1 — Encore's state inventory. The third column matters most: derived data needs a tested rebuild rather than a backup, while systems of record need both a backup and a practiced restore.*

The distinction between systems of record and derived data, which Kleppmann develops at length, decomposes one large, anxious question ("how do we protect our data?") into several small ones, each with its own answer. The seat-map cache needs no backup at all, only a rebuild whose duration is known, and that duration, as Chapter 13 will show, matters more than it seems.

**Recap.** State is what a system remembers, and it moves in one direction only: we can revert code but only compensate data. Copying it is slow, corrupting it is quiet, and replicating it spreads our mistakes as reliably as our writes. An inventory that separates systems of record from derived data is the first and cheapest act of control.

**Exercise 10.1.** Build Figure 10.1 for a system you know. Mark each store as system of record or derived, and for each derived store write down how it would be rebuilt and how long that would take. Which "derived" store turns out to have no source?

### 10.2 Backups That Restore — RPO, RTO, and Testing Recovery

#### What a backup is for {#what-a-backup-is-for}

The companion volume defined the recovery point objective (RPO) and recovery time objective (RTO); here we treat them as an operator must, as claims awaiting a test. A **backup** is a copy of a system of record, held independently of it, from which a known past state can be restored within a stated time. *Independently* rules out a replica, which shares the system's fate for logical damage, and *within a stated time* turns an artifact into a capability. The data-integrity chapter of Google's *Site Reliability Engineering* makes the point that nobody wants backups as such; what people want is restores.

{% include diagrams/fig-10-2.svg %}

*Figure 10.2 — RPO measures back from a failure to the last good copy, RTO forward to service restored; here both are drawn for the seat ledger and the Finance ledger, beside what the Finance drills of Section 10.5 actually measured. Notice that the promise was kept only once the team changed what had to come back first.*

We picture a region burning down, which cloud providers have made rare. The common threats are humbler: an engineer deleting the wrong thing; a bug writing bad data for a week before anyone notices; a tenant deleting their own events and wanting them back; and an adversary who encrypts the database and then hunts for the backups. Each has a different shape in time. Slow corruption needs a copy from *before* the bug; ransomware needs one the attacker cannot reach.

| Mechanism | Protects against | Restores | Weakness |
|---|---|---|---|
| Synchronous replica | Machine, zone or region loss | Seconds (promotion) | Copies every logical error instantly |
| Physical backup plus write-ahead log | Deletion, corruption, region loss | Hours for terabytes | Whole database at once |
| Logical dump | Loss of one table or one tenant | Slow, but granular | Slow to take, slower to restore at size |
| Immutable copy in a separate account | Ransomware, insiders, compromised automation | As above, plus access delay | Must be designed in |
| Rebuild from source (event log, upstream) | Derived-data loss, some corruption | Replay time | Only if the source is retained |

No single row covers every threat, which is the practical argument for layering them. **Point-in-time recovery**, restoring a physical base backup and replaying the write-ahead log to a chosen instant, is the workhorse for slow corruption, because it can return us to 14:02 last Tuesday, just before the bad deploy. Logical backups earn their place through granularity: when a Professional tenant deletes a season of events by mistake, restoring that tenant's own database from a dump is far gentler than rewinding a shared cluster.

#### Three copies, two media, one elsewhere {#three-two-one}

The **3-2-1 rule**, usually credited to the photographer Peter Krogh, says to keep three copies of data, on two kinds of media, with one copy off site. It has aged well because it is really a rule about independence of failure. In the cloud, media and site translate into accounts, regions and credentials: a backup in the same account as the database, deletable by the same role, is one stolen credential away from not existing.

The ransomware era has retold the lesson. When NotPetya struck the shipping company Maersk in 2017, its recovery famously depended on a domain controller in Ghana that had been offline during the attack because of a local power cut. Like Galyn Susman's home computer, it survived because it happened to be somewhere else.

At Encore, backups of systems of record go to a separate account, in object storage with retention locks, so that for 35 days nobody, Encore's administrators included, can delete them; changing the lock policy takes two people. **Immutability** is a property of the storage and its permissions; good intentions do not enter into it.

#### Restore testing {#restore-testing}

A backup has two failure modes, and only one is visible. The job fails, which an alert can catch, or the job succeeds and its output cannot be restored, which nothing catches except a restore. GitLab's database outage of January 2017 is the well-documented modern case. Late at night, while trying to repair replication to a lagging secondary, an engineer wiped the data directory on the primary instead. The team then found that their daily dumps had been producing nothing, because of a tool version mismatch whose failure emails were being rejected, and that disk snapshots had never been enabled for the database servers. A snapshot taken by hand about six hours earlier, for an unrelated purpose, saved most of the data, and copying it from slow staging disks took most of a day. GitLab's published postmortem is blunt: several backup mechanisms existed, and none had been tested end to end.

A backup that has never been restored is a rumor about your data.

The answer is continuous restore testing: scheduled restores into an isolated environment, verified against invariants. Encore restores the Catalog and every Professional tenant database weekly, checks them against the source and records the elapsed time. That duration is a service level indicator (SLI) in its own right, and its upward trend is the earliest warning that an RTO is drifting out of reach as the data grows.

**Recap.** A backup is an independent copy that restores a known state within a stated time, and each threat needs its own kind of copy, with immutable copies in another account for adversaries. Only a restore proves a backup, so restores should run on a schedule and be timed.

**Exercise 10.2.** For your most important database, write down the date of the last full restore, how long it took and who did it. If you cannot answer, schedule one; if you can, compare its duration with your stated RTO and with the growth of the data since.

### 10.3 Schema Changes and Data Migrations

#### Two deploys and a promise {#two-deploys-and-a-promise}

A schema change is a deployment whose effects cannot be rolled back by redeploying. During any rollout two versions of the code run side by side, and both must work against the data at every moment, which rules out changing schema and code together. The answer is **expand and contract** (also called parallel change): expand the schema so that it supports both old and new code, migrate code and data, and only when nothing uses the old shape, contract it away.

The civil engineer's version is replacing a bridge without closing the road: build the new span alongside, shift traffic lane by lane, watch the new span under load, and only then demolish the old one. At every step but the last, reverting means sending traffic back. The analogy breaks in one instructive place. When a bridge is demolished, no driver still needs the old route. Software has readers with long memories: caches, stream consumers, mobile clients that update when their owners please and, at Encore, an event-sourced ledger whose past events will be read in their original shape for as long as it exists. Contracting is safe only when we can show that no reader of the old shape remains.

Every migration is two deploys and a promise: the expand, the contract, and the promise, kept in between, that both shapes stay correct.

#### The holds store, migrated under traffic {#holds-store-migration}

Encore's seat holds lived in a relational table keyed by `(event_id, seat_id)`, with a sweeper job deleting expired rows every few seconds. The sweeper had become an on-sale hot spot, so the On-Sale and Seat Inventory teams moved holds to a key-value store with native per-key expiry, adding the Sale Gate admission token so that every hold could be traced to the queue position that earned it. The migration ran over three weeks, outside on-sale windows:

| Phase | Writes go to | Reads come from | Exit criterion |
|---|---|---|---|
| 1. Expand | Old table; new store in shadow | Old table | New store healthy for 7 days, write errors under 0.01% |
| 2. Backfill | Both | Old table | Five minutes elapsed: every live hold now exists in both |
| 3. Verify | Both | Old table, shadow reads compared | 72 h with zero unexplained mismatches |
| 4. Switch | Both | New store, behind a flag | One full on-sale on the new store within its service level objective (SLO) |
| 5. Contract | New store only | New store | Old writers removed; table archived, dropped 30 days later |

*Figure 10.3 — Expand and contract for the holds store. A flag or a deploy reverses each phase until the fifth, and the fifth waits until there is nothing left to reverse to.*

A **backfill** is the bulk copy of existing data into a new shape, and in most migrations it is the riskiest phase: long-running, heavy on the database and racing live writes. Holds, however, live for five minutes. Once the new store had received every write for five minutes, it held every live hold and nothing older mattered. Knowing the lifetime of your data can turn the hardest part of a migration into a wait.

The dual writes were the real hazard, and the teams treated them as such. Without a transaction spanning both stores, one write can succeed while the other fails, so the old table stayed authoritative, the shadow write never failed a request, and phase 3 measured the drift instead of assuming it away. It found one class of mismatch: a hold released when a fan pressed "back" was deleted from the table but, through a missing code path, left to expire in the new store. Fans would have seen freed seats stay held for five minutes. The alternative to dual writes, change data capture from the old store's log, avoids partial failure altogether, and Encore's platform now offers it on the paved road. Online schema change tools such as `gh-ost` apply the same idea to large tables, syncing a shadow table so that no `ALTER TABLE` holds a lock longer than an SLO allows.

**Recap.** Schema changes are deployments that cannot be reverted, so we expand before we contract and keep both shapes correct in between. Backfills are the riskiest phase, unless the data's own lifetime makes them trivial. Dual writes drift silently, so we measure the drift with shadow comparisons or avoid it with change data capture.

**Exercise 10.3.** Take the next schema change on your team's roadmap and write it as a table like Figure 10.3. For each phase, name the exit criterion and the way back. Which phase has no way back, and what must be proven before it starts?

### 10.4 Replication, Multi-Region, and Failover

#### Lag and what it means {#lag-and-what-it-means}

**Replication lag** is the delay between a write being acknowledged on the leader and being applied on a replica; under asynchronous replication it is exactly the data a failover would lose. It tends to be largest at the worst moment, because the events that raise write volume (an on-sale, a backfill) are the ones most likely to precede trouble; GitLab's outage began with a replica too far behind to catch up. Lag that threatens an RPO is one of the few causes that earns a page.

Encore chose synchronous replication for the seat ledger precisely to take lag out of the RPO. Each write commits to a standby in its home region and to one in the second region before the fan's hold is confirmed. The price is a cross-region round trip of about 18 ms on every seat write, which the 3 s checkout budget absorbs easily. What synchronous replication cannot buy is protection from Encore itself: a bad write reaches three copies in 18 ms. So the ledger, despite its zero RPO, still has point-in-time backups, and its event-sourced design earns its keep: corrupted projections can be rebuilt by replaying a log that only ever grows.

Replication copies your mistakes as faithfully as your data.

#### Split brain and fencing {#split-brain-and-fencing}

Failover has a characteristic failure that is worse than the outage it was meant to end. **Split brain** is the condition in which two nodes both believe they are the leader and both accept writes, so that the data diverges in ways that may never be reconciled. It arises naturally, because a leader cut off from its peers, or paused by a long garbage collection, cannot know it has been replaced, and when it wakes it carries on with complete confidence.

Pilots handle the analogous problem with a ritual, "I have control," "You have control," "I have control," which makes the transfer of the aircraft explicit and acknowledged, so that there is never a moment when both pilots fly or neither does. The ritual works because both pilots share a cockpit and can hear each other, and that is where the analogy breaks: in a distributed system the old leader may never hear the handover. The protection must therefore sit not with the leaders, who may be mistaken, but with the storage they write to.

That protection is **fencing**: every leadership term carries a monotonically increasing number, a **fencing token**, and storage rejects any write bearing a term older than the newest it has seen. The idea descends from the leases Cary Gray and David Cheriton described in 1989, grants of authority that expire unless renewed, and Kleppmann gives the clearest modern account of fencing tokens. Encore's Seat Inventory shards run with fenced leader terms: a new leader's first act is to record its term, and from that instant any write from the old leader fails, loudly and harmlessly. The cost, tens of seconds of rejected writes during takeover, buys the invariant that matters most. No seat is sold twice, whatever the leaders believe.

{% include diagrams/fig-10-4.svg %}

*Figure 10.4 — Fencing on a Seat Inventory shard. The deposed leader is never asked whether it still leads; the storage simply refuses its stale term, and that refusal is how it learns.*

#### Failing over a region {#failing-over-a-region}

Because Encore pins each event's writes to a home region, a regional failure becomes many small ones: for each event homed there, promote its standby, move its home and redirect its writers. Encore automated those steps as one operation but kept the trigger human, because partial regional failures are common and confusing, and a failover fired by a flapping health check is a self-inflicted outage with the largest blast radius Encore has.

**Recap.** Lag is the RPO of asynchronous replication; synchronous replication removes lag but not our own mistakes. Split brain is the characteristic failure of failover, and fencing, enforced by storage rather than by leaders, is its cure. Region failover should be automated in its steps and human in its trigger.

**Exercise 10.4.** For one replicated store you run, find out what prevents an old leader from writing after a failover. If the answer is "it will notice it has been replaced," write down how long that takes and what it could write in the meantime.

### 10.5 Disaster Recovery as Practice, Not Plan

#### The plan on the shelf {#the-plan-on-the-shelf}

Most organizations have a disaster recovery (DR) plan; fewer have a DR capability. The difference is that between an evacuation map and a fire drill: the map decays as walls move, people change and doors are locked for other reasons, and only the drill reveals the decay. Banking, where I spent a good part of my career, requires DR tests by rule; the rule ensures that a test happens, and whether it teaches anything depends on whether its people are allowed to fail.

DR drills are the game days of Chapter 9 aimed at something narrower and harder: whether people, tooling and permissions can rebuild the system, timed against an RTO someone promised. They also counter one of the ironies of Chapter 3. The better the replication and failover machinery, the less often anyone performs a recovery, and the less able anyone is to perform one on the day the machinery itself has failed.

An RTO is a hypothesis until a stopwatch has run against it.

#### The Finance ledger drill {#finance-ledger-drill}

In the spring the Reliability team ran Encore's first full restore of the Finance ledger: about 4.2 TB, with an RTO of two hours agreed when the database was a tenth of that size. The scenario: a corruption found at 09:00, repaired by restoring to 02:00, just after the nightly close. The Finance platform team did the work; the Reliability team kept time.

| Step | Planned | Actual | What happened |
|---|---|---|---|
| Reach the backup account | 5 min | 1 h 40 min | One of two required approvers was on leave; the encryption key's policy did not grant the drill account |
| Restore base backup | 45 min | 3 h 10 min | Throughput was capped by the target volume's provisioned I/O, sized for normal running |
| Replay log to 02:00 | 20 min | 1 h 15 min | A month-end day's log, larger than the runbook assumed |
| Verify against PSP settlements and `SaleCompleted` | 30 min | 2 h 20 min | The verification queries had never been written; they were written during the drill |
| Repoint applications | 10 min | 35 min | A reporting job's connection string was hard-coded |
| **Total** | **~2 h** | **~9 h** | |

*Figure 10.5 — The Finance ledger restore drill. No delay came from the database engine.*

The drill missed its RTO more than fourfold, and was the most useful day of reliability work Encore did that quarter. The two-person rule was right but untried under pressure; it now has a standby approver rota. The throughput was physics, and the arithmetic unanswerable: at the measured rate, 4.2 TB could not come back in two hours whatever the runbook said. So the team split the ledger: the current financial year (about 600 GB) restores first and becomes writable while history follows, and kept a warm standby for that slice. Finance, asked what it truly needed, said the real deadline was the next nightly close: two hours for the current year's postings was right, and a day for history was acceptable. Three months later a second drill had the current year writable in 1 h 50 min.

Verification taught the subtlest lesson. A restore is finished not when the database starts but when someone with authority can say the data is right. Written down in advance and run weekly against the scheduled restores of Section 10.2, the verification queries turned two hours of anxious improvisation into 10 minutes of reading a report.

#### The region failover game day {#region-failover-game-day}

The largest test came on a quiet Tuesday in October, with no on-sale within a week: the Reliability team failed over every event homed in Encore's first region, EU-1, to the second, EU-2, carrying real traffic for small events and the synthetic buyers of Encore's hidden test event.

The core held (Figure 10.6): standbys were promoted in about four minutes, fencing rejected a handful of late writes from EU-1 leaders that had not heard of their replacement, and no hold or sale was lost. The surprises were at the edges. The Sale Gate's provisioned concurrency had been pre-warmed only in EU-1, because every on-sale until then had been homed there, so the first synthetic buyers in EU-2 met cold starts. Bot Screening's risk data, in its separate account, reached EU-2 only by a daily copy, so the Gate there screened against yesterday's signals. And an Orders reconciliation job whose schedule named EU-1 explicitly quietly did nothing for six hours. None would have stopped a real failover; each would have made it worse, and each became a ticket with an owner.

{% include diagrams/fig-10-6.svg %}

*Figure 10.6 — The October game day, EU-1 to EU-2. The core that had been designed for failover held, while the three findings sat at the edges, in things that had quietly assumed EU-1 would always be home.*

The drills also changed Encore's runbooks. A DR runbook is good when an engineer who has never performed the procedure can follow it at 3 a.m. against the clock, so each drill is now led by someone who has not led one before. Chapter 12 takes up how a real disaster is commanded.

A drill that goes perfectly has taught us only that we chose the wrong drill.

**Recap.** DR is a capability that exists only where it is practiced. Drills time real recoveries against promised RTOs, and their findings concern permissions, throughput arithmetic, verification and the edges of the system far more than the database engine. Runbooks are proven by people who have never used them.

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
| Independence | Could one compromised administrator credential destroy every copy of the balances? |
| Reversible migration | Can each phase of the ticketing migration be reversed until the last, and is the last gated on proof? |
| Fencing | After a failover, what physically stops the old primary from accepting a top-up? |
| Practice | Is the drill timed, led by someone new to it, and expected to fail somewhere? |

#### Where you now stand

You can now inventory a system's state, design backups for the threats that actually occur, migrate data under live traffic without losing the way back, reason about lag, split brain and fencing, and turn a DR plan into a capability measured with a stopwatch. One threat in this chapter had a face: the adversary who looks for your backups before encrypting your data. Chapter 11 turns to that adversary, and to security as an operational discipline.

### References

- Laine Campbell, Charity Majors — [*Database Reliability Engineering*](https://www.oreilly.com/library/view/database-reliability-engineering/9781491925935/). O'Reilly, 2017.
- Martin Kleppmann, Chris Riccomini — [*Designing Data-Intensive Applications*, 2nd ed.](https://dataintensive.net/). O'Reilly, 2026.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Heather Adkins, Betsy Beyer, Paul Blankinship, Piotr Lewandowski, Ana Oprea, Adam Stubblefield — [*Building Secure and Reliable Systems*](https://google.github.io/building-secure-and-reliable-systems/raw/toc.html). O'Reilly/Google, 2020 — free online.
- Thomas A. Limoncelli, Christina J. Hogan, Strata R. Chalup — [*The Practice of System and Network Administration*, 3rd ed.](https://www.oreilly.com/library/view/the-practice-of/9780133415087/). Addison-Wesley, 2016.
- GitLab — [*Postmortem of database outage of January 31*](https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/). GitLab blog, 2017 — free online.
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne (eds.) — [*The Site Reliability Workbook*](https://sre.google/workbook/table-of-contents/). O'Reilly/Google, 2018 — free online.
- Thomas A. Limoncelli, Strata R. Chalup, Christina J. Hogan — [*The Practice of Cloud System Administration*](https://www.informit.com/store/practice-of-cloud-system-administration-devops-and-9780321943187). Addison-Wesley, 2014.
- Jim Gray — [*Why Do Computers Stop and What Can Be Done About It?*](https://www.cs.columbia.edu/~junfeng/08fa-e6998/sched/readings/why-do-computers-stop.pdf). Tandem Technical Report 85.7, 1985 — free online.
- Cary G. Gray, David R. Cheriton — [*Leases: An Efficient Fault-Tolerant Mechanism for Distributed File Cache Consistency*](https://pages.cs.wisc.edu/~remzi/Classes/739/Fall2015/Papers/leases89.pdf). SOSP, 1989 — free online.

---

## Chapter 11: Security Operations — Secrets, Patching, and the Supply Chain {#ch11}

> "Security is a process, not a product." — Bruce Schneier


A system can be designed securely and still be run insecurely, as a well-drawn ship can be sailed onto the rocks. The companion volume drew Encore's trust boundaries and gave every workload an identity. Drawings, however, do not rotate a key, rebuild an image or notice a partner's credential being used from a country the partner has never operated in. This chapter asks what security looks like as daily work: who does it, how often, with which instruments, and how we know it is still being done when nobody is watching.

The question is older than the cloud. On the evening of 2 November 1988 a program written by Robert Tappan Morris, a Cornell graduate student, was released onto the young internet from a machine at MIT, and within a day thousands of computers had slowed to a crawl. Nothing about the worm was exotic. It walked through doors that administrators had left open in the ordinary course of running their machines, and the response, improvised over mailing lists, became the first rough draft of security operations.

Encore stands, for once, in reasonable shape: its services carry cryptographic workload identities, its mesh enforces mutual TLS, and its golden path can sign images. What it lacks is the habit of exercising all of this, of rotating, patching, revoking and rehearsing on an ordinary Tuesday, so that the extraordinary Friday finds the machinery already warm.

### 11.1 Security as an Operational Discipline

#### Four open doors {#four-open-doors}

The Morris worm deserves a close reading, because almost every lesson in this chapter is already in it. It attacked VAX and Sun machines running Berkeley-derived Unix, and it had four ways in. It used the debug mode of `sendmail`, a convenience left enabled in many installations, to have the mail system run its code. It overflowed a buffer in `fingerd`, which read its input with a C routine that never checked length. It exploited the trust relationships of `rsh` and `rexec`, through which one machine let users from another log in without a password. And it guessed passwords from a short dictionary of common words, which on a network of trusting hosts opened many more.

Morris seems to have intended the worm to spread quietly. It asked each host whether a copy was already running, but, so that administrators could not defeat it with false answers, it ignored the answer about one time in seven and installed itself anyway. That one decision turned a crawl into a flood, as machines filled with copies until they were unusable. The figure most often repeated is about 6,000 machines infected, roughly a tenth of the perhaps 60,000 then connected, though nobody counted carefully and the estimate deserves to be held loosely.

The response is as instructive as the attack. Groups at Berkeley and MIT, among others, decompiled the worm within days and circulated fixes; Eugene Spafford's analysis at Purdue, published that month, remains the clearest account. Many sites cut themselves off from the network, which stopped the worm and also the fixes, since both travelled the same wires. Within weeks the Defense Advanced Research Projects Agency (DARPA) funded a Computer Emergency Response Team at Carnegie Mellon's Software Engineering Institute, the body we now know as CERT/CC, so that next time there would be someone to call.

| Door in 1988 | What it really was | Its descendant today | The operational answer |
|---|---|---|---|
| `sendmail` debug mode | a convenience left on in production | an admin endpoint, a debug flag, a public bucket | configuration drift detected by policy as code |
| `fingerd` overflow | a known class of bug in a running binary | a critical flaw in a library the fleet shares | patch by rebuild, measured in hours (Section 11.3) |
| `rsh` trusted hosts | trust conferred by network location | a flat network, a shared service account | workload identity and short-lived credentials (Section 11.2) |
| weak passwords | long-lived, guessable secrets | a leaked API key in a public repository | rotation, scoping and detection (Sections 11.2 and 11.5) |

*Figure 11.1 — The Morris worm's four doors and their modern descendants. Each door was opened by ordinary operation rather than by bad design, which is why each needs an operational answer.*

#### The adversary is part of the environment {#the-adversary-is-part-of-the-environment}

None of those doors was an architectural failure in the companion volume's sense. They were the residue of running systems day after day: conveniences never disabled, binaries never updated, trusts granted for a weekend and kept for years. A system loses security through operation as surely as it gains it through design, and must regain it the same way.

What distinguishes security from the reliability work of earlier chapters is an adversary who adapts. Gravity is the same tomorrow as today, which is why civil engineers can publish tables, whereas a defense that works this month teaches its opponent what to try next month. The fortress is the usual analogy; I find the hospital's infection control more faithful. Nobody believes a hospital can be made sterile once and left that way. Infection control is a set of routines (hand hygiene, surveillance, isolation when something unusual appears) performed constantly by ordinary staff and tightened when a new organism arrives. The analogy breaks at intent: bacteria evolve blindly, while an adversary reads our status page and times the attack for our busiest hour.

Encore knows this adversary personally: the bots arrived before the fans when it had nine engineers, and never left. Bot Screening is the clearest case of security as operations: its rules, built on rented edge signals, are tuned weekly, and its team watches each big on-sale live. The bots are run by people with a business model, who buy residential proxies and rehearse on minor on-sales before the major ones. A permanent adversary is a kind of weather that learns. One caution follows, which Chapter 12 will make vivid: a rule that judges behavior is only as current as the behavior it was tuned on, and fans, too, change how they behave.

Google's *Building Secure and Reliable Systems* treats security and reliability as one discipline seen from two sides, and Encore organizes accordingly. A Security Engineering team of six sits in the platform group beside the Reliability team, owning the security planes of the paved road and running detection, consulting and building rather than gating every change. The chores themselves (inventory, credentials, patches) belong to the teams that own the services, on the same scorecard as their service level objectives (SLOs).

**Recap.** The Morris worm entered through four ordinary doors, each with a modern descendant and each closed by routine rather than by a single design. Because the adversary adapts, security is a continuous practice, closer to infection control than to construction, owned by the teams that run the services.

**Exercise 11.1.** For a system you run, fill in Figure 11.1's last two columns: name today's descendant of each of the four doors, and the routine (with its frequency) that keeps it closed. Which door has no routine at all?

### 11.2 Identity, Secrets, and Least Privilege in Practice

#### Credentials that expire on their own {#credentials-that-expire}

The companion volume argued that a credential which expires soon is worth little to a thief; operating the idea is harder. Encore's workloads prove who they are with SPIFFE Verifiable Identity Documents (SVIDs), short X.509 certificates issued by SPIRE, the reference implementation of the Secure Production Identity Framework for Everyone (SPIFFE). An agent on each node attests the workload by its Kubernetes service account and hands it a certificate naming it `spiffe://encore/inventory`, valid for one hour and renewed at the half-way point. Nobody types, stores or accidentally pastes them.

Touring crews solved a version of this long ago: the backstage laminate changes design from city to city, so a pass lifted in Hamburg is useless in Vienna. The analogy breaks where software is stronger: a guard glances at a pass, while the mesh checks every request cryptographically and never tires at the end of the night.

Short-lived credentials carry a price their advocates mention less often: they move risk from confidentiality to availability. A credential that expires every hour depends, every hour, on its issuer being up. If SPIRE were down longer than the fleet's certificates had left to live, Encore's services would refuse one another, in an outage both total and self-inflicted. In December 2018 an expired certificate in Ericsson software took down O2's mobile data network in Britain for most of a day. Encore therefore runs its issuer as a platform plane with an SLO stricter than any service it serves, servers in both regions and an alert when any certificate passes 75% of its lifetime unrenewed. Trading a secret that lives too long for an issuer that might fail is wise only if the issuer is treated as the most critical dependency in the building.

#### The secrets that remain {#the-secrets-that-remain}

Workload identity removes most secrets, never all. Encore still holds credentials from its payment service provider (PSP), signing keys for wallet passes and the keys its partners use against `api.encore.com`. These live in a secrets manager, injected at runtime, each with an owner, a rotation interval and a written rotation procedure. The procedure matters more than the interval. A rotation never performed is a restore never tested, which Chapter 10 taught us to distrust: it fails at the moment of need, usually because some consumer read the secret once at startup and cached it forever.

Encore learned the cost of the remaining secrets on a quiet Thursday. A contractor working for Rowmate, one of its resale partners, committed a configuration file to a public repository, and inside it was Rowmate's production API key, 26 months old. Two signals arrived within minutes: secret scanning at the code host recognized Encore's key prefix (`enc_live_`), and Bot Screening flagged the same key calling the availability endpoints at 40 times Rowmate's usual rate, from a cloud region Rowmate had never used. The key was revoked 38 minutes after the commit.

What made the episode an incident rather than a disaster was a decision taken years earlier: scopes. The key carried `listings:read` and `resale:write`, which let its holder read availability and list tickets for resale on Rowmate's behalf. It could not buy primary inventory, read fans' personal data or touch payouts. The gateway's audit log showed 14 minutes of scraping and two fraudulent resale listings, removed before anyone bought them. Rotation was harder: Rowmate needed a deploy to change keys, so both ran for an hour, the old one restricted to Rowmate's addresses. Partners now use OAuth client credentials bound to a client certificate, with tokens that live 15 minutes.

{% include diagrams/fig-11-2.svg %}

*Figure 11.2 — How long each of Encore's credentials lives, on a logarithmic scale, against the 38 minutes it took to revoke Rowmate's key. A token of the kind partners use now would have expired on its own before anyone revoked it.*

#### Least privilege drifts {#least-privilege-drifts}

Least privilege is granted once and eroded continuously, as incident-time permissions stay and service accounts outlive their services. Permissions are a ratchet that turns one way unless someone deliberately turns it back. Encore turns it back from evidence: access logs show which permissions each role actually used in the last 90 days, and every quarter the owning team receives a proposed policy without the unused ones, to accept, amend or defend.

The exception every organization needs and few design is **break-glass access**: a pre-arranged, audited path for a human to gain elevated access to production in an emergency, outside the normal approvals. At Encore it requires a second engineer's approval, expires after 60 minutes, posts to the security channel and opens a review ticket automatically. Glass that breaks silently is just a door, and a door that nobody watches is the very thing the worm walked through.

**Recap.** Short-lived certificates remove most secrets but make the issuer a critical dependency with an SLO of its own. The remaining secrets need owners, rehearsed rotation and scopes that limit a thief. Least privilege drifts upward unless usage evidence turns it back, and break-glass access must be loud, brief and reviewed.

**Exercise 11.2.** Pick one long-lived secret your system depends on and rotate it in a staging environment, timing each step. What consumer broke, and what would have happened in production at 3 a.m.?

### 11.3 Vulnerabilities, Patching, and the Fleet

#### Severity is not risk {#severity-is-not-risk}

In March 2017 the Apache Struts project published a fix for a remote code execution flaw. Attackers entered Equifax through that flaw roughly two months later, in systems that had not been patched, and the breach exposed personal data on about 147 million people. The lesson usually drawn, that patching matters, is true and not very useful. The useful lesson is that the organization had a patching process that did not reach the system that mattered, because nobody could see clearly which systems ran what.

Advisories, each with a Common Vulnerabilities and Exposures (CVE) number, arrive by the tens of thousands a year; a team that treats all as urgent soon treats none so. The **Common Vulnerability Scoring System (CVSS)** gives each a severity score from 0 to 10, describing how bad exploitation would be in general, but severity is not risk: it says nothing about whether anyone is exploiting the flaw, or whether our code ever calls the vulnerable function. Two further signals help. The **Exploit Prediction Scoring System (EPSS)**, maintained by the Forum of Incident Response and Security Teams (FIRST), estimates the probability that a vulnerability will be exploited in the next 30 days. The **Known Exploited Vulnerabilities (KEV)** catalog, published by the US Cybersecurity and Infrastructure Security Agency (CISA) since November 2021, lists those that are being exploited already. Encore adds two facts only it can know: whether the component faces the internet, and whether its own code reaches the vulnerable function.

| Exploitation evidence | Exposure | Encore's response | Deadline |
|---|---|---|---|
| on the KEV list, or exploitation reported | internet-facing or on the purchase path | emergency change; compensating control at the edge first | 48 h |
| on the KEV list | internal only | expedited fix through the normal pipeline | 7 days |
| high EPSS, CVSS 7 or above | any | scheduled fix, next base-image rebuild | 30 days |
| low EPSS, code path unreachable | any | record as not affected, with the reasoning | next routine update |

*Figure 11.3 — Encore's triage policy. The rows are ordered by evidence of exploitation and by exposure, not by CVSS alone, so that urgency is spent where an attacker is most likely to arrive.*

The policy resembles aviation's airworthiness directives, which tell every operator of an aircraft type what must be inspected or replaced, and by when, attaching a compliance time to each finding. The analogy breaks twice. Software fleets change hourly, so the list of affected machines is stale as soon as it is printed, and a directive is rarely written while an adversary is already exploiting the defect, which for the top row of Figure 11.3 is the normal case.

#### Patching as a flow {#patching-as-a-flow}

The decisive move is to stop thinking of patching as an event. Containers let a patch become a rebuild: Encore never patches a running container, it rebuilds the image from an updated base and redeploys through the ordinary pipeline, canaries included. Base images are rebuilt weekly whether or not an advisory demands it, dependency-update pull requests merge automatically when tests pass on a patch release, and the scorecard reports each service's median image age. A fleet that rebuilds every week patches in a day when it must; a fleet that rebuilds once a year discovers, on the day it must, which services no longer build.

Log4Shell is the best-documented test of this idea. On 9 December 2021 a flaw in Log4j 2, a ubiquitous Java logging library, was disclosed with a CVSS score of 10: a crafted string written to a log could make the server fetch and run remote code. The hard part was finding it, because Log4j was often a dependency of a dependency, or bundled inside a vendor's archive where no package manager could see it. The first fixed release proved incomplete, so teams that patched once had to patch again. In 2022 the US Cyber Safety Review Board called it an endemic vulnerability that would remain in systems for years.

Encore's own test came this spring: a critical remote code execution flaw in a widely used XML parsing library, added to the KEV list within a day of disclosure. Its software bills of materials (Section 11.4) answered the first question in 20 minutes: 37 images across 23 services, two of them base images, and one copy inside a vendor's monitoring agent. Within 6 hours the gateway's web application firewall (WAF) blocked the known exploit pattern on internet-facing paths, a compensating control that bought time rather than safety. A big on-sale fell inside the window, so purchase-path changes went through the freeze's emergency category. By hour 30, 35 images were redeployed; by hour 48, all of Encore's own. The vendor's agent, confined meanwhile by an egress rule, waited four more days for its supplier. The honest summary is "patched in 48 hours, except the part we did not build", and Encore now writes that exception into vendor contracts.

{% include diagrams/fig-11-4.svg %}

*Figure 11.4 — The spring parser flaw: affected images redeployed against hours since disclosure, from the counts Encore recorded. The curve is steep where Encore owns the build and flat where it waits on a supplier.*

**Recap.** CVSS measures how bad a flaw could be; exploitation evidence, exposure and reachability decide how fast we move. Patching works best as a continuous flow of rebuilds, so that an emergency is the ordinary process run faster. Finding a vulnerable component is often harder than fixing it, and vendor software sets the length of the tail.

**Exercise 11.3.** Reclassify the last 20 vulnerability findings for a service you own with Figure 11.3. How many were treated as urgent, and how many deserved to be? Then measure your production images' median age.

### 11.4 The Software Supply Chain — Provenance, SBOMs, and Signing

#### When the build is the target {#when-the-build-is-the-target}

The companion volume told Thompson's warning and the xz backdoor of 2024, and there is no need to tell them again. Between them in time sits the case that changed operational practice most. In December 2020 it became known that attackers had compromised the build system of SolarWinds and inserted a backdoor into updates of its Orion monitoring software, signed with the company's own key and shipped to as many as 18,000 customers. The source was clean, the signature genuine and the product poisoned. What failed was the integrity of the place the artifact was made.

The **software supply chain** is everything that touches an artifact between a developer's keyboard and production: source repositories, dependencies, build systems, registries and deployment tooling. The frameworks that grew up after SolarWinds share one aim, to make each link produce evidence that the next can check. Shipping offers the closest analogy. A container crossing an ocean travels with a manifest and a numbered seal applied at the origin, and customs checks the seal against the paperwork. The analogy is exact about what a seal proves and honest about what it does not: an intact seal shows that nobody opened the container on the way, and nothing about whether the shipper loaded it honestly. Signatures, likewise, tell us who built an artifact, never whether its builders were deceived.

**Supply-chain Levels for Software Artifacts (SLSA)** grades the build link. In its version 1.0 build track, Level 1 asks that the build produce **provenance**, a record of what was built, from which source, by which builder and with which inputs; Level 2 asks that a hosted build platform sign that provenance; Level 3 asks that the platform be hardened, so that builds cannot tamper with one another and the build's own steps cannot forge the provenance. Each level describes the pipeline rather than the code, which is why SLSA belongs in a book about running systems.

Signing used to founder on key management, a signing key being exactly the long-lived secret Section 11.2 warned against. **Sigstore**, described by Newman, Meyers and Torres-Arias in 2022, removed most of that burden with keyless signing: the build obtains a certificate valid for minutes, bound to its OpenID Connect (OIDC) identity, such as a particular workflow in a particular repository, signs with an ephemeral key and records the signature in a public transparency log. Verification then asks a question operators can actually answer: was this image signed by *our* release workflow, from *our* main branch?

#### The bill of materials as an index {#the-bill-of-materials-as-an-index}

A **software bill of materials (SBOM)** is a machine-readable inventory of the components inside an artifact, with their versions and origins, in a standard format such as SPDX or CycloneDX. Producing SBOMs is easy, and many organizations stop there; their value lies entirely in being queried. Encore indexes every SBOM, joined to the record of which image runs where, so that "where do we run this library?" is a query rather than a week of messages; hence Section 11.3's 20 minutes. Where a vulnerable component is present but not exploitable, a Vulnerability Exploitability eXchange (VEX) statement records the reasoning, so the finding is not triaged again by every scanner and every auditor.

| Stage | Artifact produced | Check that consumes it | Failure behavior |
|---|---|---|---|
| Dependency resolution | lockfile with hashes | the build rejects unpinned or unknown packages | build fails |
| Build (hosted, isolated) | image, SBOM, SLSA provenance | signed by the release workflow's identity | build fails |
| Registry | signature and attestations in the transparency log | nightly rescan of SBOMs against new advisories | ticket to the owning team |
| Admission to a cluster | — | policy verifies signer, builder and source branch | pod rejected, fails closed |
| Runtime | — | inventory of running images joined to SBOMs | drives Figure 11.3 triage |

*Figure 11.5 — Supply-chain controls on Encore's golden path. Every stage leaves evidence that a later stage checks automatically.*

Encore's golden path does all of this by default, so a team creating a service from the template inherits signing, provenance and SBOMs without writing pipeline code. Every service reaches SLSA Build Level 2; the purchase path and the identity issuer are built at Level 3 on isolated builders. Admission rejects any image not signed by Encore's release workflow, with a priced, logged exception path for bought products whose vendors cannot yet provide provenance.

Dependency hygiene completes the picture. Every dependency is a standing relationship with strangers. I spent a decade maintaining a widely used open-source library, and the view from the other end of a dependency is sobering: a great deal of the world's software rests on a few volunteers' evenings. Encore asks of each new dependency whether it is maintained, by how many people, and whether it is worth a permanent relationship. One newer hazard deserves a line: coding assistants sometimes suggest packages that do not exist, attackers publish malicious packages under such names, and so a lockfile that admits only known packages now guards against a machine's imagination as well as a person's typo.

**Recap.** SolarWinds showed that the build itself can be the target, so each link must produce evidence the next can check. SLSA grades the build, Sigstore makes signing cheap enough to be universal, and SBOMs pay only when queried. Signatures prove who built an artifact, never whether it is good, so dependency hygiene still matters.

**Exercise 11.4.** Pick one image running in production today. Can you show, with evidence rather than memory, which commit and builder produced it and which version of its largest dependency it contains? List each step you could not answer.

### 11.5 Detection, Response, and Security Chaos Engineering

#### Detection that knows what normal looks like {#detection-that-knows-normal}

Everything so far reduces the chance of compromise; nothing reduces it to zero. The question becomes how quickly we notice, and the Rowmate key suggests where to look. The scraping was caught not by a signature of known malice but by a deviation from known behavior: a credential used at the wrong rate, from the wrong place. Encore's detections are written mostly in those terms, against identity: a workload calling a service it has never called, a break-glass session without a ticket, an image running that admission never saw. They are kept as code and tested with synthetic events, each with an owner and a runbook, as Chapter 5 requires of any alert.

Security incidents follow the command structure of Chapter 12, but differ from reliability incidents in three ways. The adversary may still be watching, so the incident channel must be restricted and some actions delayed until containment is ready. Evidence must be preserved before remediation destroys it, against the operator's instinct to restart the broken thing. And there is a legal clock: under the General Data Protection Regulation (GDPR), a personal data breach must normally be reported to the supervisory authority within 72 hours of becoming aware of it, so a privacy lead belongs in the room from the first hour. Containment is mostly revocation, and its speed is the true measure of what the earlier sections were worth. An organization that can rotate any credential in an hour has an incident; one that needs a week has a breach with a long tail.

#### Security chaos engineering {#security-chaos-engineering}

Kelly Shortridge and Aaron Rinehart, in *Security Chaos Engineering*, point the experimental method of Chapter 9's game days at security controls. A control we have never seen fire, they argue, is a hypothesis rather than a fact. Each belief (that admission rejects unsigned images, that an alert reaches a human) can be tested by introducing the condition deliberately, within bounds, and watching what the system and its people actually do. Experiments measure the capacity to notice, adapt and recover instead of assuming it.

The analogy is the fire drill. A drill is not valued for proving that people can walk down stairs, but for what goes wrong: the locked door, the alarm nobody heard on the fourth floor. It breaks because a fire does not watch the drill, while an adversary would gladly learn which doors we tested, so the results are themselves sensitive.

Encore added a security scenario to its quarterly game days. A canary key pushed to a test repository was detected in four minutes; an unsigned image deployed to a staging cell was rejected. The third experiment found the lesson. With the policy engine behind admission made unavailable, the admission webhook failed open, a setting chosen long before to keep deployments flowing during a policy-engine upgrade, and an unsigned image deployed without complaint. Nobody had decided that security should yield to availability; a setting had decided it, quietly, years earlier. The webhook now fails closed for the purchase path, with a break-glass procedure for the day the policy engine itself is the problem. A control that has never been seen to fail has only been seen to be configured.

**Recap.** Detection works best against identity and behavior, written as code and owned like any alert. Security incidents need restricted channels, preserved evidence and a privacy lead watching the legal clock; containment is mostly revocation. Security chaos engineering tests controls by provoking them, and its best findings are defaults nobody remembers choosing.

**Exercise 11.5.** Design one experiment for a security control you believe in: hypothesis, injected condition, blast-radius limit and the signal that would prove you wrong. Run it outside production and record what surprised you.

### Kata: The Spare Key

> **Your brief: "Hearthstay."** A vacation-rental marketplace: 85,000 listings from 30,000 hosts across southern Europe, 2.5 million guest bookings a year, a payment flow that charges guests at booking and pays hosts after check-in, and a partner API used by 40 channel managers and resellers that sync calendars and prices, each holding a static API key, the oldest from 2018. At check-in the platform sends guests their door codes. Twenty-six engineers run about 70 services on two Kubernetes clusters. An audit found base images up to 500 days old, no SBOMs, one service account shared by 11 services, and a payout-admin console reachable from the office network without multi-factor authentication. Last month a channel manager's key appeared in a public code repository; that week three hosts' payout bank details were changed, and nobody can say whether the key did it, because the gateway keeps logs for three days.

**Deliverables:**

1. **Credential inventory and plan** — every credential class with its age, scope and blast radius, and a sequenced migration to workload identity and short-lived partner tokens that needs no coordinated weekend.
2. **Triage policy** — Hearthstay's Figure 11.3, including the host mobile apps, which reach hosts only when they choose to update.
3. **Supply-chain path** — the Figure 11.5 stages adopted first, the SLSA level targeted in six months, and how SBOMs will be queried.
4. **Detection and response pack** — five identity-based detections, the log retention each needs, and a runbook for "a channel manager's key is leaked."
5. **Three security chaos experiments** — with hypotheses and limits, one of them on a change to a host's payout details.
6. **Break-glass design** — who may use it, how it expires, and how its use is reviewed.

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
- Kelly Shortridge, Aaron Rinehart — [*Security Chaos Engineering: Sustaining Resilience in Software and Systems*](https://www.oreilly.com/library/view/security-chaos-engineering/9781098113810/). O'Reilly, 2023.
- Cassie Crossley — [*Software Supply Chain Security*](https://www.oreilly.com/library/view/-/9781098133696/). O'Reilly, 2024.
- OpenSSF — [*SLSA: Supply-chain Levels for Software Artifacts*, v1.0](https://slsa.dev/spec/v1.0/). OpenSSF, 2023 — free online.
- Zachary Newman, John Speed Meyers, Santiago Torres-Arias — [*Sigstore: Software Signing for Everybody*](https://doi.org/10.1145/3548606.3560596). ACM CCS, 2022 — free online.
- Liz Rice — [*Container Security*, 2nd ed.](https://www.oreilly.com/library/view/container-security-2nd/9798341627697/). O'Reilly, 2025.
- Daniel Feldman, Emily Fox, Evan Gilman, et al. — [*Solving the Bottom Turtle: A SPIFFE Way to Establish Trust in Your Infrastructure via Universal Identity*](https://spiffe.io/book/). SPIFFE project, 2020 — free online.
- Eugene H. Spafford — [*The Internet Worm Program: An Analysis*](https://spaf.cerias.purdue.edu/tech-reps/823.pdf). Purdue Technical Report CSD-TR-823, 1988 — free online.
- FIRST — [*Common Vulnerability Scoring System v4.0*](https://www.first.org/cvss/v4-0/). FIRST, 2023 — free online.
- CISA — [*Known Exploited Vulnerabilities Catalog*](https://www.cisa.gov/known-exploited-vulnerabilities-catalog). CISA, 2021 — free online.

---

---

## Chapter 12: Incident Response — Command, Communication, and On-Call {#ch12}

> The fire does not read the org chart.

Every system in this book so far has been described in the calm tense of design. An incident is the moment that tense changes: users are hurting now, and a handful of people who were drinking coffee a minute ago must form a team, agree on what is happening and change a running system under load, all before they understand it. The hardest problems of the first 10 minutes are problems of coordination: who decides, who acts, who speaks, and who writes it down.

Our home touchstone comes from a field with far more at stake. In the autumn of 1970 a cluster of wildfires burned across Southern California for about two weeks. Sixteen people died and hundreds of homes were lost, and the fire services found afterward that courage and equipment had not been the limiting factors. Agencies used different words for the same things, ran different radio frequencies, could not tell who was in charge of a given flank, and had no common way to grow a response from one engine to a hundred. Congress funded a cooperative program, FIRESCOPE (Firefighting Resources of California Organized for Potential Emergencies), and out of it, through the 1970s, came the **Incident Command System** (ICS): a standard way to organize an emergency response of any size among people who may never have worked together. It spread from fire to every kind of emergency, and in 2004 it became the backbone of the United States' National Incident Management System.

Software borrowed it a generation later and with less ceremony; the incident management described in *Site Reliability Engineering* (2016) is explicitly modeled on ICS. Encore is about to need every one of its roles. It is Friday, a few minutes before 10:00 CET, and 1.1 million fans are waiting in the Sale Gate for Vesper Hale's 12-date European tour. We will follow the next 47 minutes section by section, and leave the question of *why* to Chapter 13.

### 12.1 Anatomy of an Incident

#### What makes something an incident {#what-makes-an-incident}

An **incident** is an unplanned disruption, or a credible threat of one, that needs a coordinated response beyond the routine work of a single on-call engineer. The definition turns on coordination rather than damage. A disk filling on a replica at 3 a.m. is a task; the same disk filling on the seat ledger's standby during an on-sale is an incident, because several teams must act together and someone must keep them pointed the same way.

Every incident, large or small, passes through the same five phases. It is **detected**, by an alert, a customer or an engineer who notices something odd. It is **triaged and declared**, which means someone judges its severity and says out loud that it is an incident, with a name, a channel and a commander. It is **mitigated**: user harm is stopped or reduced, usually before anyone understands the cause. It is **resolved**, when the system is back to a stable state that nobody has to watch by hand. And it is **followed up**, through the review that Chapter 13 takes up. *Anatomy of an Incident*, Google's short report, frames an incident's cost as the time to detect plus the time to repair, weighed against the time between failures. The phases are not a waterfall: diagnosis runs underneath all of them, and severity is revised as the picture sharpens.

#### Severity as a shared vocabulary {#severity-levels}

Declaration depends on a vocabulary agreed before anyone needs it. Severity levels exist so that one word can set a whole response in motion. Encore's are short and written in terms of harm to fans and organizers; components are never mentioned.

| Level | What it means at Encore | Response it sets in motion |
|---|---|---|
| SEV1 | The purchase path is impaired during an on-sale, or seat or money integrity is at risk | Incident commander from the rotation within 5 min; comms lead; status page within 15 min; leadership informed |
| SEV2 | A customer-facing service is degraded outside an on-sale, or a tenant SLO is being breached | Incident commander from the owning team; status page if fans or tenants can see it |
| SEV3 | Error budget is burning with little visible harm, or one internal capability is lost | Owning team's on-call handles it; channel optional |
| SEV4 | No current user impact, but something needs fixing soon | A ticket, not a channel |

*Figure 12.1 — Encore's severity levels. Each level is defined by harm and answered by a response; nobody has to remember which components are "critical."*

Two habits make severity work. The first is to declare early and downgrade freely. A needless declaration costs 20 minutes of mild embarrassment; a missing one costs the first 20 minutes of the response, the most valuable it has. The second is to treat severity as provisional: the number mobilizes people, and arguing about it mid-incident is a way of avoiding harder work.

#### Friday, 10:04 {#friday-1004}

At 10:00 the Gate opened and began admitting fans at 1,500 per second per event, the rate the On-Sale team had raised it to on Wednesday. At 10:04 the burn-rate alert on the on-sale-window SLO from Chapter 4 paged Rui, the On-Sale team's primary on-call. The alert had done what it was designed to do. Rui saw a smear of failures: "seat unavailable" errors on holds, rising checkout latency, and a retry rate that climbed as he watched.

Rui did the most useful thing an on-call engineer can do in that moment, which was to resist fixing anything for 60 seconds and ask whether this was bigger than him. At 10:06 he paged the incident commander rotation, and at 10:07 Marta, a staff engineer from Orders & Payments who was on the rotation that week, declared a SEV1 and took command. The incident now had a name, a channel and one person whose only job was to run it.

**Recap.** An incident is defined by the need for coordination, and every one passes through detection, declaration, mitigation, resolution and follow-up, though rarely in a straight line. Severity levels are a vocabulary agreed in advance, written in terms of harm, and they exist to mobilize people quickly. We declare early, downgrade without shame, and save the argument about the number for afterward.

**Exercise 12.1.** Take your team's last three significant alerts. For each, write down when it was detected, when (if ever) it was declared an incident, and by whom. Where declaration came late or never, what was the person who held the pager waiting for?

### 12.2 Roles, Command, and Communication

#### What the firefighters learned {#what-the-firefighters-learned}

ICS rests on a handful of ideas, and each answers one of the failures of 1970. **Common terminology** means every agency calls the same resource by the same name. **Modular organization** means the response grows by adding standard units, so a small fire and a large one are run in the same shape. **Span of control** means that no supervisor directs more people than they can actually track, conventionally between three and seven, with five as the usual target; when a response outgrows that, it adds a layer rather than overloading the person at the top. **Unified command** means that agencies sharing an incident command it jointly, with one plan. Behind all four sits the idea that matters most: command is a role, assigned at the start and handed over explicitly, and it is not the same thing as rank.

Schnepp, Vidal and Hawley, themselves former wildland firefighters, wrote *Incident Management for Operations* (2017) to map these ideas onto software operations.

| ICS idea | What it answered in 1970 | Its form in a software incident | Encore's role |
|---|---|---|---|
| Single incident commander | Nobody knew who was in charge of a flank | One person owns the response and its decisions, and does not type commands | Incident commander (IC), from a cross-team rotation |
| Operations section | Crews acting on contradictory orders | One person directs hands-on changes to production | Ops lead, usually the owning team's on-call |
| Public information officer | Rumor and conflicting statements | One person speaks to stakeholders and the public, on a cadence | Comms lead, from the Reliability team |
| Planning and documentation | Lost track of resources and decisions | A running log of what was seen, decided and done | Scribe, assisted by Cue's draft timeline |
| Span of control | Supervisors overwhelmed | When more than about six responders are active, split into workstreams with their own leads | Workstream leads under the ops lead |
| Unified command | Agencies running parallel fights | Joint command with a vendor or partner sharing the incident | IC plus the PSP's or partner's incident lead |

*Figure 12.2 — From wildfire to on-sale. The roles are ICS's, scaled down; the reasons are the same.*

The analogy that suits Encore best comes from the theatre it sells tickets for. A stage manager calls the show: from a desk in the wings, with a headset and the prompt book, they give every cue to lights, sound and flies, and they operate none of them. A show in which each department fires its cues when it feels ready is a show in which the curtain comes down on an actor's head. The incident commander is the stage manager. Marta's value at 10:07 lay precisely in the fact that she would not be the one running `kubectl`; her hands were free so that her attention could be. The analogy breaks, instructively, because the stage manager has a script and the incident commander must write the cues while calling them.

#### Handoffs and the collapse of roles {#handoffs}

Command changes hands more often than people expect, and each handoff is a gap the shared picture can fall through. The ICS answer, which works unchanged in software, is a short spoken briefing followed by an explicit statement that command has transferred: "You are IC now," acknowledged in the channel. Rui's briefing to Marta at 10:07 took under a minute: admission at 1,500 per second, errors on holds, retries rising, nothing changed yet.

The cost of losing roles is visible far outside software. Karl Weick's 1993 study of the Mann Gulch fire, in which 13 firefighters, 12 of them smokejumpers, died in Montana in August 1949, argued that the crew's ability to make sense of their situation collapsed along with the structure of their roles, so that when the foreman lit an escape fire and told them to lie down in it, none followed. The pattern, at far lower stakes, is familiar to anyone who has watched eight senior engineers in one channel, each pursuing a private theory. Structure is not bureaucracy in that moment. It is what lets a group think.

#### Communication: inward, upward, outward {#communication}

An incident has three audiences. Responders need one channel where facts are stated and decisions recorded. Stakeholders inside the company (leadership, Support, tenant account managers) need plain summaries that spare them the channel. And the people affected need an honest public statement of what is wrong and when they will hear more.

Encore rents a hosted status page, because one hosted on the platform it reports on tends to fail at the same moment. Elif, the comms lead from the Reliability team, posted the first update at 10:14: some fans were seeing errors when selecting seats, places in the queue were safe, and the next update would follow within 15 minutes. Inside, stakeholders got a summary on the same cadence, in the conditions, actions and needs shape that Schnepp and his coauthors recommend. A useful discipline is to promise the time of the next update rather than the time of the fix, because the first promise is always within your power and the second rarely is. A status page is a promise about honesty, not about uptime.

Communication also runs the other way, and that was where Encore's incident turned. At 10:24 Elif relayed something from Support that no dashboard in the channel had shown: fans were writing in to say the site had told them they were bots. Support, in that moment, was a sensor, and the comms lead was the only role positioned to connect it to the response.

{% include diagrams/fig-12-3.svg %}

*Figure 12.3 — The Vesper Hale response in ICS shape: command at the top, three roles beneath it, and the comms lead standing at the channel's edge. Notice the one line that runs inward; it carried the fact no dashboard had shown.*

**Recap.** ICS gave us a commander who does not operate, an ops lead who does, a voice for stakeholders and a hand that keeps the record, along with span of control and explicit handoffs. Structure is what allows a group under stress to keep thinking together. Communication flows to three audiences on a promised cadence, and it flows back in, often carrying the fact the responders were missing.

**Exercise 12.2.** Reconstruct the roles in your last significant incident. Who was commanding, who was operating, who was communicating and who was recording? If one person held two of those roles, find a moment where that cost something.

### 12.3 Mitigate First — Situational Awareness Under Pressure

#### Three levels of seeing {#three-levels-of-seeing}

Mica Endsley's 1995 theory of situation awareness, rooted in the study of fighter cockpits, names what an incident team is trying to build. **Situation awareness** is the perception of the elements of an environment, the comprehension of what they mean, and the projection of what they will do next. The levels are cumulative: a team can perceive every alert and still not comprehend what they mean together; it can comprehend the present and still fail to project that the queue will empty in four minutes and bring a second wave of load.

Incident tooling is built almost entirely for the first level. Comprehension and projection are still done in people's heads, which is why the shared picture in the channel matters: it is where one person's comprehension can be checked against another's.

#### Fixation {#fixation}

The characteristic failure of situation awareness under pressure is **fixation**: a team locks onto one explanation and stops seeing evidence that contradicts it. On 29 December 1972 the crew of Eastern Air Lines Flight 401, approaching Miami, became absorbed in a burned-out landing-gear indicator light; while they worked the problem, the autopilot's altitude hold was inadvertently disengaged and the aircraft descended slowly into the Everglades, killing more than a hundred people. Nothing about the bulb was dangerous. The danger was that it was interesting, and that nobody had been assigned to fly the airplane.

Encore had its own small bulb. At 10:11, Cue posted to the channel that a node had been drained at 10:02 by the platform's upgrade reconciler and that Seat Inventory shard 3 had failed over its leader at the same moment. Both facts were true and both were relevant, and for the next few minutes the channel's attention gathered around shard 3. Jonas, Seat Inventory's on-call, confirmed the failover and its 40 s of rejected writes. But that window had closed at about 10:03, and errors were still rising on all four shards. Marta's question at 10:16 was the one that broke the fixation: "What is still broken *now*, and is it getting better or worse?" The failover explained how the trouble had started. It did not explain why the trouble had kept going.

#### Mitigation before diagnosis {#mitigation-before-diagnosis}

The principle that follows is old in medicine and easily forgotten in engineering: stop the bleeding before you look for its cause. An emergency physician restores circulation in a patient in shock before investigating why, because a correct diagnosis delivered too late helps no one. In an incident, **mitigation** is any action that reduces user harm without requiring that we understand why the harm is happening. The best mitigations are generic, cheap to try and easy to reverse: shed load, roll back the last change, fail over, disable a feature.

At 10:19, on Rui's proposal and with Marta's decision, the Gate's admission rate was lowered from 1,500 to 900 fans per second. Fans would wait a little longer in a queue they already expected, Seat Inventory and the retry storm would both ease, and the rate could be raised again in seconds. Errors on holds began to fall within two minutes. Nothing was cured; the team had bought room to think.

The second mitigation came from the information Elif had brought in at 10:24. Marta asked for Bot Screening's on-call, and Noor joined at 10:27 and confirmed what the support tickets suggested: the velocity rule that flags rapid repeated requests had been firing on fans who were retrying failed seat selections, and it had blocked about 30,000 of them. At 10:31, with the IC's approval, Noor disabled the rule, and the Gate re-admitted the blocked fans with their original queue positions restored. Disabling a bot defense mid-on-sale was a conscious trade: a short window of bot exposure against certain harm to tens of thousands of real fans. Mitigation buys the time that diagnosis spends.

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

**Recap.** Situation awareness has three levels, and most tooling helps only with the first. Fixation is the characteristic failure, and the remedy is a role whose job is to keep asking what is broken now. Mitigation reduces harm before the cause is understood, and the best mitigations are generic, cheap and reversible.

**Exercise 12.3.** List the generic mitigations available for your most important service: what you can shed, roll back, fail over or switch off. For each, note how long it takes, who may authorize it and whether it has ever been practiced.

### 12.4 Tooling for Response — Runbooks, ChatOps, and AI Assistance

#### Runbooks and the channel {#runbooks-and-the-channel}

Tooling for incidents should serve the roles rather than replace them. Chapter 3 followed Encore's pre-warm runbook from wiki page to script to self-service workflow; incident runbooks follow the same path, and the good ones share a shape. They start from a symptom, offer generic mitigations before diagnostic steps, and say who may authorize each action, which is why "lower admission at the Gate" took under a minute to propose and approve.

**ChatOps** is the practice of running operational work through commands in a shared chat channel, so that actions and their results are visible to everyone and recorded as they happen. Its virtue in an incident is less automation than witness: a command typed in the channel is seen by the IC and logged by the scribe. Encore's incident tooling opens a channel, pages roles and drafts status posts from a few commands:

```
/incident declare sev1 "Vesper Hale on-sale: checkout errors"
/incident role ic @marta
/incident role comms @elif
/gate admission set event=vh-2026 rate=900   # requires IC approval
/statuspage draft "Some fans are seeing errors when selecting seats..."
```

The last line drafts but does not publish. A person reads the words before fans do.

#### Cue at 10:11 {#cue-at-1011}

Cue, Encore's operations assistant, joins every SEV1 and SEV2 channel. It reads telemetry, deploy history, runbooks and past postmortems, and it is read-only by default; a small set of runbook actions is available to it only when a human approves each one explicitly in the channel. At 10:11 it did two things.

The first was genuinely helpful. In about four minutes it had correlated the burn-rate alert with the platform's change log and the Seat Inventory leader history, and it posted that a node drain at 10:02 coincided with a leader failover on shard 3. It cut minutes off the team's perception of the situation, which is exactly what correlation is for.

The second was a suggestion: restart the Seat Inventory pods to clear what it described as an unhealthy state. It was plausible, and wrong in a way only someone who knew Seat Inventory would see at once. Restarting the pods would have forced leader elections on every shard, each one bringing its own window of rejected writes, at the worst moment of the year. Jonas declined it in one line. He was one of the few engineers who had run a shard failover by hand, at the game day of Chapter 9, and so he knew what one cost.

This is the human role that Chapter 3 argued for, made concrete, with Bainbridge's ironies at full strength: the assistant was fluent and fast, and the only safeguard was a person skilled enough to judge it at the moment its speed made deference tempting. An assistant that is right about the facts can still be wrong about the action. The safeguard worked because Cue could not restart anything without explicit approval in the channel, from whoever held the operations role. Cue also missed something: the Catalog deploy at 09:52 fell outside the window it searched, a limit of correlation by time whose cost Chapter 13 measures.

Cue's most valuable work drew less attention: it kept a draft timeline as the channel scrolled, which the human scribe corrected into Figure 12.5. The most useful assistance an incident team receives may simply be a good memory.

**Recap.** Runbooks start from symptoms and lead with generic mitigations, and ChatOps makes actions visible and recorded as they happen. An assistant can shorten perception dramatically through correlation, but it acts within approvals held by people who understand the system. The case for keeping skilled humans at the decision point is made at exactly the moments when the assistant is most persuasive.

**Exercise 12.4.** Pick one action your tooling or assistant could take during an incident (a restart, a rollback, a scale change). Write down the circumstances in which it would make things worse, and check whether the approval step forces a human to consider them.

### 12.5 On-Call That People Can Sustain

#### Load and its measures {#load-and-its-measures}

On-call is where incident response becomes a labor question. The Google SRE book offers two reference points that have aged well: no more than 25% of an engineer's time on call, and no more than about two incidents in a 12-hour shift, since each carries hours of follow-up. Other teams will choose their own numbers, but should measure against them: pages per shift, pages outside working hours, the share of pages that needed action, and time to acknowledge. A page that needed no action is a defect in the alerting, and Chapter 5's paging discipline is the cure.

Encore runs on-call per stream-aligned team, a primary and a secondary on weekly rotations, with the incident commander rotation drawn from about 20 senior engineers across teams. The Reliability team reviews every team's page load monthly alongside its SLOs. Rui had been paged twice in the small hours that week, mostly by pre-warm alerts. He responded well on Friday. That is not the same as saying the rotation was healthy.

#### Follow-the-sun, compensation and handoffs {#follow-the-sun}

Organizations spread across time zones can run **follow-the-sun** rotations, in which each region holds the pager during its own daytime and hands it on. Its cost is that every shift boundary is a handoff, which needs the ICS briefing of Section 12.2 and a written note of open incidents, recent changes and anything that looked odd. Encore's engineers all work within an hour or two of CET, so follow-the-sun is not available to it; it relies instead on keeping night pages for SEV1 and SEV2 symptoms only, and on giving time off after any night page.

Compensation belongs to sustainability; it is no perk. European law has taken standby time seriously: in 2018 the Court of Justice of the European Union held, in the Matzak case, that a Belgian volunteer firefighter required to reach his station within minutes while on standby at home was working during that time. Few software rotations are that constrained, but the principle that a pager tether costs something is settled, and Encore pays a standby allowance on top of the time off. A rotation that depends on heroes is already failing; it simply has not sent the invoice.

#### Fatigue {#fatigue}

Fatigue degrades exactly what incident response needs: comprehension, projection, and the patience to wait 60 seconds before acting. Long incidents should therefore rotate command, with an explicit handover; at Encore no one holds the IC role for more than four hours at a stretch. After Vesper Hale, Marta sent Rui and Jonas home at lunchtime, handed the follow-up to the review, and asked the On-Sale team's secondary to take the pager for the weekend. It was a small decision, and the kind that keeps people on a rotation for years.

**Recap.** On-call load should be measured as carefully as any SLO, in pages per shift, off-hours pages and actionable share. Follow-the-sun removes night work at the price of handoffs, which need their own discipline, and compensation acknowledges that standby is work. Fatigue erodes judgment first, so long incidents rotate command and responders rest.

**Exercise 12.5.** Pull the last quarter's pages for your rotation. Compute pages per shift, the share outside working hours and the share that required action. Which single alert, removed or fixed, would most improve the numbers?

### Kata: Storm Night

> **Your brief: "Brightwater Energy."** The customer platform of a regional electricity utility: 1.1 million customer accounts, an outage map, outage reporting by app, web and SMS, half-hourly readings from 800,000 smart meters that send a "last gasp" signal when they lose power, and a dispatch system that routes 300 field crews to faults. A winter storm brings 25× normal traffic, mostly to the map and the reporting forms, and the grid operator's control room and two contracted crew vendors share every storm incident with Brightwater. There are 24 engineers in four teams, two offices an hour apart, and a single on-call rotation that took 310 pages last quarter, 55% of them at night and most of them needing no action. Last January the outage map froze for four hours, showing 2,000 customers without power when 90,000 were. The incident went undeclared for 70 minutes, three engineers made conflicting changes, and customers learned their restoration times from local radio.

**Deliverables:**

1. **Severity matrix** — four levels defined by harm to customers (above all those on the medical-dependency register) and to the crews, each with the response it sets in motion.
2. **Role cards** — one page each for IC, ops lead, comms lead and scribe, including the handoff briefing and how unified command works with the control room and the crew vendors.
3. **Communication plan** — cadence and templates for the internal channel, the control room and call center, the public status page and outage-map banner, and SMS, including where the status page is hosted.
4. **Mitigation runbook** — symptom-first steps for "the outage map is stale or wrong," leading with generic mitigations and naming who authorizes each.
5. **On-call redesign** — rotation structure for storm season, page-load targets, the alerts you would delete or demote, and a compensation and rest policy.
6. **Tabletop script** — a 45-minute exercise replaying last January's storm with the new roles.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Early declaration | Would the new process have declared last January's incident within 10 minutes, and who would have done it? |
| Command clarity | Is there one IC who does not operate, and could three engineers still make conflicting changes? |
| Unified command | Do the control room and the crew vendors know whom to talk to and how joint decisions are made? |
| Mitigation first | Can customers still report outages and see an honest map while the cause is unknown, and is that option rehearsed? |
| Honest communication | Will customers hear from Brightwater before they hear from the radio? |
| Sustainable load | Do the numbers show a rotation people would join voluntarily before next winter? |

#### Where you now stand

You can now declare incidents early, staff them with roles the fire services refined over half a century, guard against fixation, mitigate before diagnosing, use an assistant without surrendering judgment to it, and design an on-call rotation people can carry for years. Encore's 47 minutes ended with no seat sold twice and some 30,000 fans wrongly called bots. Chapter 13 sits down with the people who were in the channel and asks the harder question: how a sensible rate change, a routine deploy, a trusted reconciler and an old bot rule came to meet at 10:02 on the most important morning of the year.

### References

- Rob Schnepp, Ron Vidal, Chris Hawley — [*Incident Management for Operations*](https://www.oreilly.com/library/view/incident-management-for/9781491917619/). O'Reilly, 2017.
- Ayelet Sachto, Adrienne Walcer, Jessie Yang — [*Anatomy of an Incident: Google's Approach to Incident Management for Production Services*](https://sre.google/resources/practices-and-processes/anatomy-of-an-incident/). O'Reilly/Google, 2022 — free online.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Betsy Beyer, Niall Richard Murphy, David K. Rensin, Kent Kawahara, Stephen Thorne (eds.) — [*The Site Reliability Workbook*](https://sre.google/workbook/table-of-contents/). O'Reilly/Google, 2018 — free online.
- Mica R. Endsley — [*Toward a Theory of Situation Awareness in Dynamic Systems*](https://doi.org/10.1518/001872095779049543). Human Factors, 1995.
- Karl E. Weick, Kathleen M. Sutcliffe — [*Managing the Unexpected*, 3rd ed.](https://www.wiley.com/en-us/Managing+the+Unexpected%3A+Sustained+Performance+in+a+Complex+World%2C+3rd+Edition-p-9781118862414). Wiley, 2015.
- Karl E. Weick — [*The Collapse of Sensemaking in Organizations: The Mann Gulch Disaster*](https://doi.org/10.2307/2393339). Administrative Science Quarterly, 1993.
- Sidney Dekker — [*The Field Guide to Understanding 'Human Error'*, 3rd ed.](https://www.routledge.com/The-Field-Guide-to-Understanding-Human-Error/Dekker/p/book/9781472439055). CRC Press, 2014.
- Gary Klein, David D. Woods, Jeffrey M. Bradshaw, Robert R. Hoffman, Paul J. Feltovich — [*Ten Challenges for Making Automation a "Team Player" in Joint Human-Agent Activity*](https://doi.org/10.1109/MIS.2004.74). IEEE Intelligent Systems, 2004.
- David D. Woods (ed.) — [*STELLA: Report from the SNAFUcatchers Workshop on Coping with Complexity*](https://snafucatchers.github.io/). The Ohio State University, 2017 — free online.

---

## Chapter 13: Learning from Incidents — Postmortems, Just Culture, and Drift {#ch13}

> "For a successful technology, reality must take precedence over public relations, for nature cannot be fooled." — Richard Feynman

On the evening of 27 January 1986, engineers at Morton Thiokol, the contractor that built the space shuttle's solid rocket boosters, joined a teleconference with NASA managers to argue that Challenger should not launch the next morning. The forecast was far colder than anything a shuttle had flown in. Each booster's field joints were sealed by a pair of rubber O-rings, and cold rubber is slow to seal. The coldest earlier launch, in January 1985 at about 53°F (12°C), had shown more blow-by of hot gas past a primary ring than any flight before it, and so the engineers recommended against launching below that temperature. NASA's managers challenged the data, which was thin and, as charted that night, did not make a clean case. Thiokol's managers asked for a recess, conferred off the line and came back recommending launch. On 28 January, at about 36°F (2°C), Challenger lifted off; 73 seconds later it broke apart, and the seven people aboard were killed.

The first account was the one we would expect: schedule pressure, managers overruling engineers, rules bent. Diane Vaughan spent years in the archives and published *The Challenger Launch Decision* in 1996 with a more unsettling story. O-ring erosion had been seen as early as the second shuttle flight, in 1981. Each time, engineers studied it, found a reason the margin still held, and accepted the next flight as an "acceptable risk" through exactly the procedures NASA had built for such judgments. Each acceptance became precedent for the next, until by January 1986 the burden of proof had quietly turned over: the engineers on the teleconference were no longer asked to show that flight was safe, but to prove that it was unsafe, and with the data they had, they could not. Vaughan called this the **normalization of deviance**: the gradual process by which a departure from an expected standard, repeated without harm, comes to be treated as the standard itself. Nobody broke the rules. The rules were how the deviance became normal. When Columbia was lost in 2003, the accident board drew on Vaughan's work and found the same pattern a second time: knowing it once had not prevented it.

Chapter 2 introduced the ideas this chapter puts to work: Reason's latent conditions, Rasmussen's drift toward the boundary, Dekker's new view of human error, Hollnagel's Safety-II and Leveson's System-Theoretic Accident Model and Processes (STAMP). Chapter 12 followed Encore through the Vesper Hale on-sale as it happened: 47 minutes of degraded checkout, about 30,000 real fans blocked as bots, and not one seat sold twice. Now the harder work begins: learning from it without punishing anyone or excusing anything, finding more than a root cause, running a review people tell the truth in, learning from the days that went right, and making any of it stick. And, as we shall see, Encore's change freeze had been eroding very much as the O-ring margins had.

### 13.1 Blameless, Not Accountability-Free

On the Monday after the on-sale, the first question in the leadership channel was "who approved the admission change?" It was a natural question, asked by a decent person under pressure, and the wrong one to ask first. Its answer (an On-Sale engineer, with a reviewer, after a load test) explains almost nothing, because the trouble lay in a process that had let a warm-cache test count as evidence, and any engineer on that team, with that test, would have approved the same change.

A **blameless postmortem** is a review in which the people involved give a full account of what they did and why, on the understanding that the account will be used to improve the system and not to punish them. John Allspaw's 2012 post on Etsy's engineering blog carried this idea from Sidney Dekker's work on just culture into web operations, and its logic is informational before it is moral. An organization learns only what its people tell it. Punish an account and the next one will be shorter, vaguer and carefully lawyered, and the organization will know less about itself at exactly the moment it most needs to know more.

Blameless is often misheard as "nobody is accountable", and Dekker's later work is the best answer to that confusion. In *Restorative Just Culture* (2025, the fourth edition of his *Just Culture*), he contrasts two ways of responding when someone's action is linked to harm. A **retributive** just culture asks which rule was broken, who broke it, how bad the breach was and what the consequence should be. A **restorative** just culture asks who was hurt, what they need, and whose obligation it is to meet that need. Both take accountability seriously. The first treats it as a debt to be paid backward; the second treats it as account-giving and repair, looking forward. Dekker also observes that the line between honest mistake and negligence is drawn by whoever has the power to draw it, which is a good reason to draw it rarely and in public.

Encore asked the restorative questions explicitly. The people hurt were, first, the fans: about 30,000 were blocked outright, and roughly 9% of admitted fans hit errors. They needed an honest explanation and a fair second chance, so Encore published a plain apology, restored blocked fans' queue positions during the incident, and gave every blocked fan an early-access window for any further dates on the tour. Organizers and the artist's management needed the same, earlier and in more detail. And the engineers were hurt too. The On-Sale engineer who proposed the admission change spent the weekend replaying it; the physician Albert Wu named such people **second victims** in 2000, clinicians harmed by their own involvement in a patient's harm. Her need was to hear, early and from leadership, that the review would be about the system. The obligation to meet these needs fell on the organization, not on her.

Medicine has held morbidity and mortality conferences for a century, in which clinicians present their own complications to their peers, and the practice teaches one useful thing: when a profession makes discussing failure routine, its members get better at it. The analogy breaks in an instructive place. Those conferences often ask "what would you have done differently?", which keeps the focus on the individual; a software postmortem asks what the system made easy and what it made hard. Blame is a way of ending a conversation the organization badly needed to have.

None of this abolishes consequences. Deliberate sabotage and sustained recklessness are rare, and they belong to a different process. The postmortem's job is narrower and more valuable: to collect the truest account it can.

**Recap.** Blameless review exists so that people give full accounts, because an organization learns only what it is told. Accountability survives in restorative form: who was hurt, what they need, and whose obligation it is. The engineers closest to an incident are often among the hurt, and saying so early is part of the repair.

**Exercise 13.1.** Take your organization's last significant incident. Write the three restorative questions and answer them for every group affected, including the engineers. Which need went unmet, and whose obligation was it?

### 13.2 Beyond Root Cause — Contributing Factors and CAST

#### Why root cause fails {#why-root-cause-fails}

Ask "what was the root cause of Vesper Hale?" and four candidates step forward: the admission change, the Catalog deploy, the node drain and the bot rule. Each was necessary, and none was sufficient. Remove any one and the morning is very likely an ordinary on-sale. Richard Cook's observation from Chapter 2, that catastrophe needs several failures together, is here a plain description of the timeline. A **root cause** is wherever an investigation decides to stop asking why, and the choice of stopping point says more about the investigators than about the incident.

Two biases push us toward stopping early. **Hindsight bias**, which Baruch Fischhoff demonstrated in 1975, is the tendency of people who know an outcome to judge it as more predictable than it was. Its close companion is the **counterfactual**: "the team should have run a cold-cache test." The sentence is true and nearly useless, because it describes a world that did not exist and says nothing about why the world that did exist made sense to the people in it. Richard Cook, David Woods and John Miller drew the distinction in 1998 between a *first story*, in which a person erred, and a *second story*, which explains the pressures, resources and trade-offs that made the error a reasonable act at the time. The first story is quicker to write. Only the second tells us what to change.

#### CAST at Encore {#cast-at-encore}

Nancy Leveson's **Causal Analysis based on STAMP (CAST)** is a method for writing second stories systematically. It treats an incident as a failure of control: some controller, human or automated, issued an action unsafe in context, usually because its **process model** (its beliefs about the system it controls) was wrong or missing a signal. CAST names the loss and the hazard, draws the control structure, examines each controller in turn (what it was responsible for, what it did, what it believed and why that belief was reasonable) and then looks at the structure as a whole, at coordination and at how it changed over time.

Encore's Reliability team ran it with every team involved. The loss was fans unable to buy tickets during a scheduled on-sale; the hazard was the purchase path receiving more load than it could serve while its capacity was reduced. Figure 13.1 draws the control structure, simplified, with its control actions running down and its feedback running up; Figure 13.2 sets out what each controller did and believed.

{% include diagrams/fig-13-1.svg %}

*Figure 13.1 — The control structure of the Vesper Hale on-sale. Every controller could act on the purchase path, and two of the feedback paths that would have warned them did not exist.*

| Controller | Control action | What it believed | What was missing |
|---|---|---|---|
| Node-upgrade reconciler (platform) | Drained a node at 10:02 | Draining is safe whenever disruption budgets allow it | Any input from the on-sale calendar; any notion that a node hosting a shard leader is costlier than one hosting replicas |
| Change freeze (readiness review) | Defined the frozen scope; granted exceptions | Catalog and "low-risk" automation sit outside the purchase path | A scope derived from real dependencies; a record of exceptions and what followed them |
| On-Sale team and reviewer | Raised admission from 1,200 to 1,500 fans/s | The load test proved headroom | A cold-cache case in the test; a review question about cache state |
| Catalog team | Deployed at 09:52 | Outside the freeze, a rolling deploy is routine | Any signal that Catalog's seat-map geometry cache was on the on-sale's critical path |
| Bot Screening velocity rule | Blocked about 30,000 clients | Bursts of identical requests are bots | Knowledge that the web client now retries a failed hold automatically; feedback from purchase-path error rates |
| Cue (ops assistant) | Suggested restarting Seat Inventory pods | Restarts had cleared elevated errors in past incidents | A model of leader failover; the blast radius of its suggestion |

*Figure 13.2 — Encore's control structure on the morning of the Vesper Hale on-sale, read through CAST. Every controller acted on a reasonable belief; the missing column is where the changes come from.*

Read down the last column and a pattern appears that no single row reveals: nearly every gap is a missing feedback path between teams. The reconciler belonged to the platform, the calendar to the On-Sale team, the cache to Catalog, the client's retry behavior to the web team, and the rule to Bot Screening. Vaughan called this **structural secrecy**: the division of labor that lets each group see its own piece clearly and nobody see the whole. It is the price of decomposition, which is how 40 teams master a system no one person could hold, and so the answer is not to undo it but to wire the feedback back in.

#### The freeze as normalization of deviance {#the-freeze-as-normalization-of-deviance}

The second row deserves its own telling, because it is Challenger in miniature. The freeze rule was clear: no non-emergency changes to the purchase path from two hours before an on-sale until its end. Over the previous year the freeze channel recorded 41 exceptions (Figure 13.3), every one granted in chat, none followed by an incident. When the node-upgrade reconciler arrived, it was classed as low-risk automation and exempted, and on three earlier on-sales it had drained nodes mid-sale without harm, because none of those nodes happened to host a shard leader. The freeze's service list predated serving seat-map geometry from Catalog's cache, and nobody had reason to revisit it.

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

The lesson is not that the freeze was ignored. It was followed, and the following was how it drifted. A rule whose exceptions are never counted is a rule whose meaning is being rewritten in private.

**Recap.** Root cause is a stopping point, not a discovery, and hindsight and counterfactuals push us to stop too soon. CAST replaces the search for a broken part with an account of controllers, their beliefs and their missing feedback. At Encore that account showed structural secrecy between teams and a freeze that had drifted exactly as the O-ring margins did.

**Exercise 13.2.** Build a CAST table like Figure 13.2 for an incident you know, with at least four controllers, one of them automated. For each, write why its belief was reasonable at the time. Which feedback path, if it had existed, would have changed the most rows?

### 13.3 Writing and Running the Review

#### Preparing the account {#preparing-the-account}

Encore's review was facilitated by a member of the Reliability team who had not been in the incident channel, which is the first rule of facilitation: the person steering the conversation should have no part of the story to defend. Before the meeting she held short one-to-one interviews with Marta, the incident commander, with the responders (Rui, Jonas, Noor and Elif) and with each team in Figure 13.1. Group meetings converge on the most senior or confident voice, and the quiet engineer who noticed something odd at 10:03 will often say so only in a room of two.

The timeline came first, and Cue had drafted most of it within an hour of recovery, from the incident channel, deploy history and telemetry. It was accurate, and it was half the story. A timeline built from logs records what the system did; the review needs a second column for what people knew, believed and were trying to do at each moment. At 10:11 the logs show Cue surfacing the node drain. Only the interviews show that Marta had already suspected the admission change and was weighing whether to roll it back, and that the drain changed her mind about which lever to pull first.

The 2017 STELLA report, from the SNAFUcatchers workshop led by David Woods, explains why that column matters. It distinguishes the running system *below the line*, which no one can see directly, from the representations and mental models *above the line*, through which people understand and act on it. Incidents are where those models turn out to differ, and the review's best minutes are spent finding the differences. Encore's came quickly: the On-Sale team learned that the node-upgrade reconciler existed, and Bot Screening learned that the web client had retried failed holds automatically since a release the previous spring.

#### Reviewing the machine's part {#reviewing-the-machines-part}

Cue's suggestion at 10:11 to restart Seat Inventory pods was examined with the same questions as every other controller, and the discipline matters, because there are two easy first stories available: "the AI was wrong" and "the human caught it". Why did a restart make sense given what Cue had read? Its corpus held two past postmortems in which restarting pods had cleared elevated errors, both on stateless services, and nothing it could read said that restarting a leader-elected service under load would cause further failovers. Why did Jonas decline? He had run a manual shard failover at the previous quarter's tech rehearsal (Chapter 9) and recognized the pattern; the irony from Chapter 3, that skill decays where automation succeeds, ran the other way for once. The finding was not about either party. A suggestion had arrived without its blast radius, and the safe outcome had depended on one person's recent memory of a drill. The change followed directly: runbook actions now carry a blast-radius tag that Cue must show with any suggestion, and suggestions touching leader-elected services say so plainly.

#### The meeting and the document {#the-meeting-and-the-document}

The meeting ran for 90 minutes with about 25 people, and opened with the ground rules read aloud. A theatre's stage manager writes a show report after every performance (timings, what went wrong, what the crew did about it), and its plain, unembarrassed tone is the right model for the document. The analogy breaks because a show report has one author, while a review must reconcile many accounts, some of which contradict each other honestly. Encore's template is short:

```text
Summary        two paragraphs a fan could understand
Impact         who was hurt, for how long, how we know
Timeline       what the system did | what people knew and were trying to do
Control        controllers, actions, beliefs, missing feedback (CAST)
What held      what worked, and why it worked
Surprises      where mental models differed
Changes        each tied to a missing control, with an owner and a check
Language check no "should have", "failed to", "simply", "careless"
```

The language check is not fussiness: "failed to" smuggles the counterfactual back in, and a document full of such phrases trains its readers in the first story however blameless its intentions.

**Recap.** An uninvolved facilitator, one-to-one interviews and a two-column timeline produce the account a meeting alone cannot. The machine's part is reviewed like any controller's, asking what it knew and why its action made sense. The document's language either teaches the second story or quietly undoes it.

**Exercise 13.3.** Take a postmortem from your archive and add the missing column to its timeline: what people knew and were trying to do at each step. Count the counterfactual phrases in the original. What does the rewritten version show that the original did not?

### 13.4 Near Misses and Learning from Success

A **near miss** is an event in which the conditions for harm came together but harm did not follow, because of luck or because someone adapted. In 1976 the United States set up the Aviation Safety Reporting System, run by NASA for the Federal Aviation Administration, through which pilots and controllers report incidents and close calls confidentially, with limited protection from penalty for those who report promptly. Its genius is the incentive: it makes telling cheaper than staying quiet. The analogy breaks at Encore, which has no regulator to grant immunity, only its own record of how earlier reports were treated; but that record is what Dekker says reporting depends on.

The CAST analysis turned up near misses nobody had reported because nothing had happened. The three earlier on-sales in which the reconciler drained a node mid-sale were the plainest, and each had been read, without anyone saying so, as evidence that the reconciler was safe. That is the O-ring logic again: erosion without burn-through taken for margin. A near miss is the system telling you, for free, what an incident would charge for. Encore now asks each on-sale's on-call to note anything that surprised them, harm or no harm, and the Reliability team reads the notes weekly.

The more interesting discovery came from asking why the freeze had seemed to work at all. For most of the previous year a platform engineer had paused the node-upgrade reconciler by hand before each big on-sale. It was in no runbook; drains during sales simply made her nervous. In the spring she moved to another team, and the practice left with her. The freeze had looked safe partly because of a person, not the policy. This is Hollnagel's Safety-II from Chapter 2 made concrete: things usually go right because people adjust their work to conditions, and **work-as-done** quietly differs from **work-as-imagined**. Her adjustment was invisible precisely because it succeeded.

So Encore added a second kind of review. After each major on-sale that goes well, the teams involved spend 30 minutes asking what they adjusted, what nearly happened and what they did that no document describes. The first few surfaced a dozen informal practices; three became automation and one was retired as superstition. Vesper Hale itself had a "what held" section worth studying, not merely celebrating: fenced leader terms and idempotency keys turned 40 s of rejected writes on shard 3 into errors rather than double sales, the result of design decisions made years earlier and tested at every game day since.

One caution: do not make near-miss reports a metric to drive down. Dekker warns that error counts mislead, and a rising count here is often good news, since it means people trust the channel. Watch instead how many reports led to a change.

**Recap.** Near misses are incidents the system paid for in luck, and they go unreported unless reporting is cheap and safe. Studying ordinary success reveals the adaptations that hold the system up, some of which live only in one person's habits. A good review asks what held, as carefully as what broke.

**Exercise 13.4.** Interview two colleagues about something they do before a risky change that no runbook asks them to do. Write each practice down. Which should become automation, which documentation, and which should be retired?

### 13.5 Turning Learning into Change

#### Why action items die {#why-action-items-die}

Action items die quietly. When Encore's Reliability team audited the previous year's postmortems, about 40% of their action items were still open after 90 days, and the open ones were not a random sample: the small fixes had been closed, while the structural items (the ones that crossed team boundaries, needed a design or had no obvious owner) had sat untouched. The learning had been real in the meeting and was gone by the next quarter.

Occupational safety has long ranked its remedies in a **hierarchy of controls**: eliminate the hazard, substitute something safer, engineer a barrier, then add procedures and training, with protective equipment last. The ranking reflects how reliably each works when a tired person is in the loop. Postmortem actions sort the same way. "Remind engineers to check cache state" sits at the bottom; a load test that cannot pass without a cold-cache run sits near the top. Every action item worth writing restores a missing control from the CAST table, and one that names no control is usually a wish. Figure 13.5 places Encore's own changes on the hierarchy.

{% include diagrams/fig-13-5.svg %}

*Figure 13.5 — The hierarchy of controls, with the Vesper Hale changes placed on it. The higher a remedy sits, the less it depends on a tired person remembering it.*

#### What Encore changed {#what-encore-changed}

| Finding | Change | Owner | How we will know it works |
|---|---|---|---|
| Upgrade automation blind to the on-sale calendar | Platform automation reads the calendar and holds disruptive actions from T−2h until the sale ends; nodes hosting shard leaders are never drained during a sale | Runtime team (platform) | A game day schedules an upgrade into a mock on-sale and confirms it waits |
| Admission change reviewed against a warm cache | Any admission-rate change needs a cold-cache load test; the readiness review asks about cache state | On-Sale team, Reliability | The next admission change arrives with a cold-cache result attached |
| Bot rule tuned before retry behavior changed | Every bot rule has an owner and a review date; client retry changes trigger a rule review; the velocity rule drops to observe-only when purchase-path errors spike | Bot Screening | A replay of Vesper Hale traffic blocks no real fans |
| Freeze drift | Freeze restored; scope derived from the traced dependency graph (Chapter 5), not a list; a register of exceptions with reason, approver and outcome, reviewed monthly | Reliability | Exceptions trend down, and each has a recorded outcome |
| Suggestion without blast radius | Runbook actions tagged; Cue shows the tag with every suggestion | Reliability, Cue maintainers | Drill transcripts show the tag on every suggested action |

*Figure 13.6 — From finding to change. Each row restores a control missing from Figure 13.2, and each says in advance what evidence will show it working.*

The register of exceptions is the quietest change and, I have come to believe, the most important. Vaughan's lesson was never that deviance can be forbidden; some exceptions are right, and a freeze with none would be broken in other ways. Her lesson was that deviance becomes normal when nobody can see it accumulate. The register makes each exception a decision with a name, a reason and a recorded outcome, so that the 42nd exception arrives in a room that can see the previous 41.

#### Tracking and sharing {#tracking-and-sharing}

Encore now tracks postmortem actions alongside feature work, reviews open items weekly, and lets the error-budget policy from Chapter 4 give them priority when a budget is spent. An item older than 90 days must be closed, rescheduled with a reason or accepted as a risk by a named person.

Sharing is the step most often skipped. The Vesper Hale review was published to all of engineering, read out at the monthly all-hands and summarized for organizers. It was also indexed for Cue, and here an irony closes the loop: Cue's unhelpful suggestion came from old postmortems that described restarts without their context. Postmortems are now part of what future responders, human and machine, will learn from, and so they must be written to teach the right lesson. An organization's postmortems are its memory, and an incomplete memory teaches confidently.

**Recap.** Action items die when they compete unaided with feature work, and the structural ones die first. Ranking remedies by how reliably they work, tying each to a missing control and stating its evidence in advance keeps them honest. A register of exceptions is how an organization watches its own drift, and postmortems written well become the memory that later responders learn from.

**Exercise 13.5.** Audit your last ten postmortems' action items. What share closed within 90 days? Place each open item on the hierarchy of controls, and for the top three write the evidence that would show they worked.

### Kata: The Second Story

> **Your brief: "Scriptline."** An electronic prescription network linking 2,000 clinics to 6,000 pharmacies in two countries, routing about 1.2 million prescriptions a day, run by 60 engineers in eight teams. Last month, an automated certificate-renewal job failed during a clinics' morning peak, and for 3 hours prescriptions could not be submitted; pharmacists fell back to phone calls and paper. The postmortem, written by the head of engineering, concludes "human error: the on-call engineer restarted the wrong cluster while mitigating" and lists eleven action items, mostly training. The renewal job had failed silently twice before, each time fixed by hand by the same platform engineer, and never reported. Scriptline has 70 action items still open from last year's postmortems, and two senior engineers have asked to leave the on-call rotation.

**Deliverables:**

1. **The second story** — a one-page summary rewritten without counterfactuals, explaining why each key action made sense at the time.
2. **CAST table** — controllers, control actions, beliefs and missing feedback for at least five controllers, including the renewal job and the head of engineering's review process.
3. **Restorative response** — who was hurt, what each needs and whose obligation it is, including the on-call engineer and the pharmacists.
4. **Near-miss channel** — how the two earlier silent failures would have been reported, by whom, and what the reporter is promised.
5. **Action-item triage** — the 70 open items and the eleven new ones placed on the hierarchy of controls, with a keep, merge or close decision and evidence for those kept.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Second story | Could the on-call engineer read the summary and recognize the situation they were actually in? |
| Control, not components | Does the CAST table find missing feedback between teams, not just a faulty job? |
| Restorative accountability | Is every hurt party's need met by someone with the obligation and the power to meet it? |
| Near misses | Would the third silent failure now be reported, and would reporting it cost the reporter nothing? |
| Durable change | Does each kept action restore a named control and state in advance how you will know it works? |
| Drift | Have you found where Scriptline's standards have been quietly rewritten by success? |

#### Where you now stand

You can now run a review that people tell the truth in, write the second story instead of the first, draw the control structure with CAST, learn from near misses and ordinary success, and turn findings into changes that survive the quarter. You have also seen drift for what it is: careful people following rules, confirmed by good outcomes, until the margin is gone. Chapter 14 turns to systems whose components do not repeat themselves, AI workloads in production, where every lesson here applies and the evidence of drift is harder still to see.

### References

- Diane Vaughan — [*The Challenger Launch Decision: Risky Technology, Culture, and Deviance at NASA*, enlarged ed.](https://press.uchicago.edu/ucp/books/book/chicago/C/bo22781921.html). University of Chicago Press, 2016.
- Nancy G. Leveson — [*Engineering a Safer World: Systems Thinking Applied to Safety*](https://doi.org/10.7551/mitpress/8179.001.0001). MIT Press, 2011 — free online.
- Nancy G. Leveson — [*CAST Handbook: How to Learn More from Incidents and Accidents*](https://psas.scripts.mit.edu/home/get_file4.php?name=CAST_handbook.pdf). MIT, 2019 — free online.
- Sidney Dekker — [*Restorative Just Culture: From Disciplinary Action to Meaningful Accountability*, 4th ed.](https://www.routledge.com/Restorative-Just-Culture-From-Disciplinary-Action-to-Meaningful-Accountability/Dekker/p/book/9781032868233). CRC Press, 2025.
- John Allspaw — [*Blameless PostMortems and a Just Culture*](https://www.etsy.com/codeascraft/blameless-postmortems). Code as Craft (Etsy), 2012 — free online.
- David D. Woods (ed.) — [*STELLA: Report from the SNAFUcatchers Workshop on Coping with Complexity*](https://snafucatchers.github.io/). The Ohio State University, 2017 — free online.
- Sidney Dekker — [*The Field Guide to Understanding 'Human Error'*, 3rd ed.](https://www.routledge.com/The-Field-Guide-to-Understanding-Human-Error/Dekker/p/book/9781472439055). Ashgate/CRC Press, 2014.
- Sidney Dekker — [*Drift into Failure*](https://www.routledge.com/Drift-into-Failure-From-Hunting-Broken-Components-to-Understanding-Complex/Dekker/p/book/9781409422211). Ashgate, 2011.
- Erik Hollnagel — [*Safety-I and Safety-II: The Past and Future of Safety Management*](https://www.routledge.com/Safety-I-and-Safety-II-The-Past-and-Future-of-Safety-Management/Hollnagel/p/book/9781472423085). Ashgate, 2014.
- Nancy G. Leveson, John P. Thomas — [*STPA Handbook*](https://psas.scripts.mit.edu/home/get_file.php?name=STPA_handbook.pdf). MIT, 2018 — free online.
- Dave Zwieback — [*Beyond Blame: Learning from Failure and Success*](https://www.oreilly.com/library/view/beyond-blame/9781491914441/). O'Reilly, 2015.
- Ayelet Sachto, Adrienne Walcer, Jessie Yang — [*Anatomy of an Incident*](https://sre.google/resources/practices-and-processes/anatomy-of-an-incident/). O'Reilly/Google, 2022 — free online.

---

## Chapter 14: Operating AI Workloads — Models, Evals, and Agents {#ch14}

> A fluent answer is not yet a correct one, and production is where we learn the difference.

Between 1964 and 1966, at MIT, Joseph Weizenbaum wrote a program he called ELIZA, after the flower girl in Shaw's *Pygmalion* who is taught to speak like a duchess. Its best-known script, DOCTOR, imitated a Rogerian psychotherapist, the kind who answers a statement by turning it back into a question. A patient's "My mother is unkind to me" might come back as "Tell me more about your family." There was no understanding in it, only keywords and rules for rearranging the patient's own words, and Weizenbaum described the mechanism plainly in *Communications of the ACM* in 1966.

People mistook it for more anyway. In *Computer Power and Human Reason* (1976) he recalled that his secretary, who had watched him build the program over many months and knew exactly what it was, began a conversation with it and after a few exchanges asked him to leave the room. Some psychiatrists proposed that it might grow into automatic psychotherapy, which dismayed him more. "What I had not realized," he wrote, "is that extremely short exposures to a relatively simple computer program could induce powerful delusional thinking in quite normal people." The lesson concerned us: we lend trust to fluency, and quickly, before anything has earned it.

That lesson is the operational heart of this chapter. Today's models are vastly more capable than ELIZA, and much of what they say is right, which makes the warning sharper: trust that is partly deserved is harder to ration, and a component that is usually right is harder to supervise than one that is obviously wrong. The companion volume designed Encore's AI features, the support assistant built on retrieval-augmented generation (RAG), the refund agent and the AI gateway. This chapter runs them: on an ordinary Tuesday, through a model upgrade nobody asked for, and on the afternoon somebody tried to talk the refund agent into paying them.

### 14.1 What Is Different About AI in Production

#### A dependency with opinions {#a-dependency-with-opinions}

Everything in this book so far assumes that a component, given the same input, does the same thing. Monitoring compares today with yesterday, canaries compare new with old, and tests assert that an output equals what we expected. A large language model (LLM) behind an API keeps the operational shape of a managed service from Section 7.3 while quietly withdrawing that assumption. Six differences matter in practice:

| Property | A conventional managed dependency | A hosted model |
|---|---|---|
| Determinism | same input, same output | same input, a distribution of outputs; even at temperature zero, not reliably repeatable |
| Failure signal | errors and timeouts | mostly HTTP 200: the failure is in the *content* |
| Change | versioned releases, announced | new snapshots, silent alias moves, scheduled retirements |
| Cost | per request or per hour | per token, so one call can cost 100× another |
| Latency | a distribution in milliseconds | time to first token plus time per output token, in seconds, growing with output length |
| Capacity | requests per second | requests *and* tokens per minute, per model, per account |

*Figure 14.1 — The same dependency, seen twice. Each row on the right breaks an assumption our operations quietly rely on.*

The second row changes the work most. Chip Huyen's *Designing Machine Learning Systems* made the point for classic machine learning: these systems fail *silently*, returning confident, well-formed and wrong answers through a healthy endpoint. Every signal from Chapter 5 stays green. An assistant that tells fans the wrong refund rule has 100% availability and excellent latency, and only an instrument that reads what it said will notice.

The third row deserves the same attention. A database we run changes when we change it; a hosted model changes when its provider retrains it, re-tunes its safety behavior or retires it, and providers publish **deprecation schedules**, dated notices after which a model version stops answering. A retirement date is an incident with a calendar invitation attached. D. Sculley and colleagues, in "Hidden Technical Debt in Machine Learning Systems" (2015), called the governing principle CACE, *changing anything changes everything*. With a hosted model, some of the anything is changed by someone else.

#### Budgets in tokens and seconds {#budgets-in-tokens-and-seconds}

Tokens are also the unit of capacity. Encore's gateway already tags every call with feature, tenant and model, so cost per resolved conversation sits on the FinOps dashboard of Section 6.5. The newer fact is that providers grant each account a ceiling of requests and tokens per minute, per model, and that ceiling behaves like any shared capacity in Chapter 6: invisible until the queue forms, then decisive. On a big on-sale morning support traffic triples within the hour, so the Reliability team now lists the provider's token quota in the on-sale readiness review beside the Gate's admission rate. A quota is a capacity ceiling that someone else sets.

Latency has a new shape too. Huyen's *AI Engineering* separates **time to first token** (TTFT), how long before the first word arrives, from **time per output token**, how quickly the rest follows. Users feel the first; the bill and the queue feel the second. Encore's service level objective (SLO) for the assistant therefore has three parts: gateway availability, a TTFT under 1.5 s for 95% of turns, and a *quality* objective. The first two are ordinary reliability engineering. The rest of the chapter is largely about earning the right to write down the third.

A touring production that hires a local orchestra in each city knows this situation. The score is the production's own; the players are rented, and one night the second oboe is a substitute who phrases a passage differently. The right reflex is to rehearse with whoever will actually play and to listen during the performance. The analogy breaks because an orchestra announces its substitutes in the program, whereas a provider may change the player behind the same name.

**Recap.** A hosted model keeps the shape of a managed dependency but withdraws determinism, fails in content rather than status codes, changes on its provider's schedule and meters everything in tokens. Its SLOs need a quality component, and its quotas and retirement dates belong on the on-sale calendar.

**Exercise 14.1.** For one model-backed feature you run, fill in the right-hand column of Figure 14.1 with real values: the model version you call, its retirement date if announced, your token quota and current peak, and p50 and p95 TTFT. Mark each value you had to look up.

### 14.2 Model and Prompt Changes as Deployments

#### What actually ships {#what-actually-ships}

When we ask what changed in an AI feature, the honest answer is rarely "the code." It is the prompt, the model version, the temperature, the tool descriptions or the retrieval settings, and any one of them can change behavior as much as a rewrite. Each is therefore a deployment and travels the road Chapter 8 built for code.

Theater has a name for the artifact we need. The **prompt book** is the stage manager's master copy of the script, annotated with every cue and change; an understudy who goes on tonight plays from it, and a change made in rehearsal is not real until it is written in. Encore borrowed the idea. A **prompt bundle** is the versioned unit that defines an AI feature's behavior, and it ships whole:

| In the bundle | Why it is versioned with the rest |
|---|---|
| System prompt and templates | business logic in natural language |
| Model identifier, pinned to a dated snapshot | an alias can move under you |
| Sampling parameters (temperature, max tokens) | change the output distribution |
| Tool descriptions and schemas | the model reads them as instructions |
| Retrieval configuration (index version, top-k, reranker) | decides what the model is shown |
| Eval suite version and pass thresholds | the bundle's own fitness function |

*Figure 14.2 — Encore's prompt bundle. Changing any row produces a new bundle version, which passes the same gates as a code change.*

Two rows carry most of the weight. The model is **pinned** to a dated snapshot, never a floating alias such as "latest," because an alias is a dependency whose version someone else chooses. And the eval suite travels *with* the bundle, so a change to what "good" means appears in the same diff as the change it judges.

The bundle is promoted through GitOps like any service. Continuous integration (CI) runs the eval suite of Section 14.3, and promotion is a canary in the manner of Section 8.3: 5% of conversations for a day, compared with the baseline on escalation rate, sampled quality and cost. Rollback is a `git revert`, and it works because the previous bundle names a model that still exists. That clause will not be true forever. A rollback plan for an AI feature carries an expiry date printed by the provider.

#### The upgrade nobody scheduled {#the-upgrade-nobody-scheduled}

Encore learned the pinning rule the usual way. The frontier tier had always been pinned, but the cheap tier, which answers about 80% of turns, had been configured during a hurried launch with the provider's alias for its current small model, and the alias looked like a version. One Tuesday the provider moved it to a new snapshot. Nothing failed; latency and cost both improved slightly.

What changed was one word. Encore's refund workflow approves automatically when a ticket costs under €80 *and* more than 48 h remain before showtime. The new model, in roughly a third of refund conversations, explained the rule as under €80 *or* more than 48 hours out. A fan with a €140 ticket five days out was told the refund would be automatic and then watched it go to human review. No money moved wrongly, because the policy lived in the workflow and not in the model's words, but the assistant was making promises the system would not keep, which is a reliability failure by any definition a fan would recognize.

The nightly eval run caught it. Encore runs the golden set of 200 conversations every night against the *production* configuration, not only in CI, precisely because configuration can change without a commit. Eighteen of the 200 are refund conversations; for months they had passed 18 of 18, and on Wednesday morning 11 passed. The Support Experience team's on-call engineer read the seven failures, saw the same "or" in each, and pinned the previous snapshot by lunchtime. Figure 14.3 shows how loudly the refund cases spoke and how quietly the overall score did.

{% include diagrams/fig-14-3.svg %}

*Figure 14.3 — The nightly golden-set run across the week the alias moved. The refund cases fell from 18 of 18 to 11; the overall score barely moved, which is why the team reads categories and not averages.*

The harder question was how many real fans had heard the wrong rule in the 30 hours before the rollback. A golden set shows how a version behaves on cases we chose; what it told the people who actually came lives only in production.

**Recap.** Prompts, model versions, parameters, tool descriptions and retrieval settings ship together as one versioned bundle through the ordinary pipeline. Models are pinned, evals travel with the bundle, and rollback lasts only as long as the old model does. Evals also run nightly against production, because configuration can change without a commit.

**Exercise 14.2.** List every artifact that shapes the behavior of one AI feature you run. For each, note where it is stored, whether a change to it passes through CI and whether it can be rolled back in under 10 minutes. Any "no" is a deployment path you have not built yet.

### 14.3 Evals — Testing Systems That Don't Repeat Themselves

#### Error analysis before metrics {#error-analysis-before-metrics}

The companion volume explained why a probabilistic component is *evaluated* rather than unit-tested, and introduced Encore's golden set. This section treats evals as an operational practice, something a team does every week, and the most useful guide is Shreya Shankar and Hamel Husain's *Evals for AI Engineers* (2026). Their method begins where most teams skip ahead: before choosing any metric, read traces.

**Error analysis** is the practice of reading a sample of real interactions, noting in plain words what went wrong in each, and grouping the notes into a taxonomy of failure modes, repeating until new traces stop producing new categories. It sounds slow and is the fastest route to useful evals, because it replaces the metrics we imagined with the failures we actually have. Generic "helpfulness" scores measure something real and often irrelevant; the failure that hurts hides inside a 4-out-of-5.

Encore's refund incident showed exactly this. The overall score moved only from 193 to 186 out of 200, a dip teams learn to shrug at. Reading the seven failures revealed one specific, conjunction-sized fault, and the team added an evaluator for it: a code check that any explanation of the refund rule states both conditions jointly. Error analysis is how we discover which questions to ask; evaluators are how we keep asking them.

#### Judges need calibrating {#judges-need-calibrating}

Some checks are code: did the cited order exist, does the output parse, is the euro amount right. Others need judgment, and for those we use a model as a grader, the **LLM-as-judge**. Huyen, Shankar and Husain all agree on the central caution: a judge is a measuring instrument, and an uncalibrated instrument produces numbers, not measurements.

In 1960 Jacob Cohen published his kappa statistic for agreement between two raters beyond what chance would produce, because researchers had learned that two people coding the same interviews agree less than either believes. A judge model is a second rater. Encore's support team labels conversations by hand, tunes the judge's prompt on one split of the labels and measures its agreement with humans on a held-out split, counting both missed failures and false alarms. A judge that agrees with humans 95% of the time on easy cases and 60% on refund cases is a poor judge of refunds, and only per-category agreement shows it. The judge is itself a model, so it is re-checked against fresh labels monthly and whenever its own snapshot changes.

Non-determinism also changes what passing means. Encore runs each golden case five times and tracks how often it passes all five, in the spirit of the pass^k measure from Yao and colleagues' τ-bench (2024). An assistant right four times in five is wrong for one fan in five, and averages are very good at hiding that fan.

#### From golden set to production sampling {#from-golden-set-to-production-sampling}

Medicine faced Encore's question after the thalidomide disaster of the early 1960s. A clinical trial tests a drug on chosen patients under chosen conditions; its real behavior emerges only across everyone who takes it. The answer was **post-market surveillance**, the continuing collection of evidence once a drug is in use. A golden set is the trial. **Production sampling** is the surveillance: evaluating a share of real interactions with the same calibrated judges and code checks, sending a smaller share to human reviewers, and watching the results as a time series. The analogy has one limit worth stating: an approved drug does not change, and a hosted model can, so we need surveillance more than the regulator does.

Answering "how many fans heard the wrong rule?" took two engineers a day. They pulled about 520 refund conversations from the 30-hour window, ran the new evaluator over them and found 164 faulty explanations; the support team wrote to each of those fans with the correct rule and expedited their reviews. Doing it by hand once made the case for doing it continuously. Encore now evaluates a 3% daily sample of assistant conversations, sends 40 a week to human reviewers, and oversamples where the judge is uncertain or the fan escalated. The sampled pass rate on refund explanations is a quality service level indicator (SLI) with an objective of 98%, and its burn rate pages the Support Experience team in business hours like any SLO of Chapter 4.

The loop closes in both directions. Production failures become new golden cases, so the golden set grows toward the conversations fans actually have, as Phillip Carter's early report on LLM observability argued it should. What we sample this quarter is what we test next quarter. Figure 14.4 places both loops beside the request path they watch.

{% include diagrams/fig-14-4.svg %}

*Figure 14.4 — The request path through the AI gateway, with the eval loop beside it. Notice that the evaluators reach back into the gateway: quality is a signal the path acts on, not only a report.*

**Recap.** Evals begin with error analysis of real traces, which turns imagined metrics into a taxonomy of actual failures. LLM judges are instruments calibrated against human labels per category and re-checked when they drift, and repeated runs measure consistency as well as accuracy. The golden set is the trial and production sampling the surveillance, each feeding the other.

**Exercise 14.3.** Read 50 recent traces from an AI feature you run. Write one line per failure, then group the lines into no more than eight categories. Compare the categories with the metrics on your current dashboard: which failures have no metric, and which metrics match no failure?

### 14.4 Failure Modes, Guardrails, and Graceful Degradation

#### A field guide to content failures {#a-field-guide-to-content-failures}

Content failures need names, and each name needs a detector and a response. Five recur often enough to plan for:

| Failure mode | How it shows | Detected by | Contained by |
|---|---|---|---|
| Hallucination | a confident claim with no support in what was retrieved | grounding check against cited sources; sampled judges | answer only from citations; uncited claims become a handoff |
| Drift | quality decays with no deploy: corpus, users or provider changed | nightly evals on production config; sampled SLIs | pinning, corpus freshness SLOs, rollback |
| Refusal | the model declines legitimate requests, often after an upgrade | refusal-rate metric per intent | eval cases that *must* be answered; fallback model |
| Loops | an agent repeats a tool call or plan without progress | step and token counters per trajectory | step caps, spend ceilings, loop detector, escalation |
| Tool misuse | wrong tool, wrong arguments or an out-of-policy call | schema validation, authorization denials, trajectory evals | scoped credentials, workflow-enforced policy |

*Figure 14.5 — Content failure modes with their detectors and containment. The right-hand column is architecture, which is why it holds when the model does not.*

Two rows deserve comment. **Drift**, which *Reliable Machine Learning* by Chen, Murphy and colleagues treats at length, classically means the world moving away from a model's training data. A hosted model faces three drifts at once: the corpus changes, the questions change (a stadium tour brings questions about bag policies), and the provider changes the model. Only the third can be prevented by pinning. **Refusals** mirror hallucination and are easy to miss because they look safe; a support assistant that politely declines to discuss refunds is down, however green its dashboard.

#### The degradation ladder {#the-degradation-ladder}

Guardrails, the input and output checks the companion volume layered from schemas to grounding, catch individual bad answers. Operations also needs a planned sequence of lesser services for when a whole tier is unavailable or untrustworthy. Aviation's version is the **minimum equipment list**, which states in advance which instruments an aircraft may fly without, and under what restrictions. Nobody decides at the gate whether the flight can go without its weather radar; it was decided months earlier, calmly, by people who were not running late.

Encore's equivalent is a ladder, every rung tested on game days:

1. **Frontier tier** for hard turns and **cheap tier** for the rest, the normal state.
2. **Fallback provider**: a second provider's model, pinned and run against the same golden set weekly, so the fallback is a known quantity.
3. **Retrieval only**: the assistant shows the most relevant help articles and the fan's order status, without generating prose.
4. **Human handoff**: the conversation joins the support queue with a summary, and the fan is told honestly how long the wait is.

Circuit breakers in the gateway pull the ladder when errors or latency cross thresholds (Section 9.2's patterns, applied to a provider), as does rate-limit exhaustion. The trigger teams forget is quality, because a model that is available but wrong never trips a breaker. Encore wires the refund-explanation SLI into the same switch, so a sustained quality burn drops refund intents to retrieval only until a human looks. Figure 14.6 draws the ladder with its triggers.

{% include diagrams/fig-14-6.svg %}

*Figure 14.6 — The degradation ladder and what pulls it. The breakers see errors, latency and rate limits; only the quality signal sees a model that is up and wrong.*

Human handoff hides a trap Weizenbaum would recognize. Reviewers of the refund agent's proposals approve with one click, and after months of good proposals they approve faster and read less. Chapter 3 called this the irony of automation, and fluency sharpens it: the proposal is written in the confident register of someone who has checked. Encore's review screen therefore shows the policy facts (price, hours to showtime, the rule's verdict) in a fixed panel computed by the workflow, apart from the agent's prose, and occasionally seeds the queue with a known-bad proposal whose catch rate is tracked. Reviewers who are never shown a wrong answer gradually lose the ability to notice one.

**Recap.** Hallucination, drift, refusals, loops and tool misuse each need a named detector and an architectural container. A degradation ladder, decided in advance like an aircraft's minimum equipment list, steps from fallback models down to human handoff, and quality signals must be able to trigger it. Human review stays meaningful only if the interface separates computed facts from fluent prose and tests the reviewers' attention.

**Exercise 14.4.** Write the degradation ladder for one AI feature you run. For each rung, name its trigger, who or what pulls it, and when it was last exercised. Add one trigger that fires on quality rather than availability.

### 14.5 Agents with Permissions — Sandboxing, Injection, and Blast Radius

#### Credentials shaped like the task {#credentials-shaped-like-the-task}

An assistant that only talks can mislead; an agent that acts can do damage. The companion volume gave Encore's refund agent delegated authority, and the operational question is whether that design holds against an adversary, months after anyone last read it.

In 1988 Norm Hardy published "The Confused Deputy," about a compiler on a time-sharing system that held permission to write a billing file for its own purposes. A user named the billing file as the compiler's output file, and the compiler, acting on the user's request with its own authority, overwrote it. It was not malicious, only confused about whose authority it was exercising. An AI agent is a confused deputy by construction, because its instructions and its data arrive in the same stream of text.

The remedy is to make authority travel with the request. Encore's refund agent holds no standing credentials. For each conversation it obtains, by OAuth token exchange (RFC 8693), a token that names both the agent and the fan, carries only the `orders:read` and `refunds:request` scopes, covers that one fan's orders and expires in 15 minutes. Least privilege, practiced for workloads in Chapter 11, takes its most literal form here: the credential is shaped like the task, not like the agent. Backstage, the same idea is printed on a laminate, which says which areas its holder may enter and on which dates; the lighting tech's pass opens the dimmer room and not the dressing rooms, however persuasive the tech becomes. The analogy breaks instructively. A guard can notice someone behaving strangely and an API cannot, so the laminate must be strict enough that strangeness has nowhere to go.

The agent runs in a sandbox with no network egress except the internal Model Context Protocol (MCP) server and the gateway, no file system that outlives the conversation, and step, token and spend budgets enforced by the workflow engine rather than the prompt. Every tool call, with its arguments and the token's subject, goes to an append-only audit log, which turns "what did the agent do?" from a reconstruction into a query.

#### The ticket that tried to issue orders {#the-ticket-that-tried-to-issue-orders}

The design was tested one Thursday in spring. A ticket about a cancelled show arrived, and below the fan's complaint, formatted to look internal, was a paragraph addressed to the assistant. It claimed to be a note from finance, said the customer was pre-approved for compensation, and told the agent to refund three listed orders and skip review "as already authorized." Two of the orders belonged to other accounts. This is **indirect prompt injection**, the variant Steve Wilson's *Developer's Playbook for Large Language Model Security* treats as the harder one: the instruction arrives through content the system reads on the user's behalf.

The input classifier did not flag it, and the model was partly persuaded: its trajectory shows `refunds:request` called for all three orders. What happened next was decided by structure. The API refused the two calls for other fans' orders, because the token named a different fan. The third order was the author's own, but at €95 the workflow routed it to human review, and "already authorized" meant nothing to a workflow that does not read prose. The reviewer saw the policy panel and the quoted paragraph, and declined.

Detection came from the boring layer. Authorization denials from an agent identity are rare enough to alert on, and two in one trajectory paged the Support Experience team within minutes. The blameless review of Chapter 13's kind made three changes: ticket bodies now reach the model inside delimiters marking them as untrusted quotation; the ticket and five variants joined the golden set as adversarial cases; and the alert threshold for agent authorization denials dropped to one. None claimed to prevent the next injection. I have come to believe that is the honest posture: injection is contained the way a hospital contains infection, by assuming it will arrive and designing the wards accordingly.

The remaining risk lives inside policy. A €60 refund on the attacker's own order a week before the show would be approved automatically, injection or not. **Blast radius**, for an agent, is the worst outcome reachable within its credentials and policy in one session, multiplied by the sessions an attacker can open. Narrow sessions keep the first factor small, and a per-account limit on agent-initiated refunds keeps the second small. An agent's permissions are a promise about the worst day, and they should be written by someone imagining it.

**Recap.** An agent is a confused deputy by construction, so its authority must travel with the request: short-lived, exchanged tokens naming the agent and the person it acts for, scoped to one task. Sandboxing, workflow-enforced budgets and an append-only audit log contain what the model cannot be trusted to refuse. Injection can only be contained, and blast radius is measured as the worst in-policy outcome times the sessions an attacker can open.

**Exercise 14.5.** For one agent or automation that acts on your systems, write down its credential: who issues it, what it names, what it can reach and how long it lives. Then describe the worst outcome it allows in one session, and how many sessions an outsider could start in an hour.

### Kata: Grounded Flights

> **Your brief: "Skylark."** A European regional airline carrying 4 million passengers a year on 90 aircraft, with 60 engineers. It runs a chat assistant and a rebooking agent that can move passengers and issue meal and hotel vouchers during disruption. Compensation under EU Regulation 261/2004 (€250, €400 or €600 by distance) is decided by a human team, but the assistant explains it daily. On a bad-weather day chat volume rises 30× in two hours, and last winter the provider's token quota ran out at 07:40, the worst possible minute. The cheap-tier model Skylark calls retires in 90 days. Last month a passenger put instructions in a booking's "special assistance" field, and nobody knows whether the agent read them.

**Deliverables:**

1. **Release unit** — Skylark's prompt bundle in the shape of Figure 14.2, with pinning, the CI gate and a rollback plan that survives the model's retirement.
2. **Eval plan** — an error analysis of 50 invented traces into a failure taxonomy, three evaluators (at least one code-based and one calibrated judge with its human-agreement target), and a production sampling plan with a quality SLI for compensation explanations.
3. **Degradation ladder** — four rungs for a disruption day, with triggers, including one triggered by quota exhaustion and one by quality.
4. **Agent credential spec** — the rebooking agent's token: issuer, subject, scopes, lifetime, voucher spend ceiling per session and per hour, and the audit record for each tool call.
5. **Injection drill** — the special-assistance attack as a game-day scenario, with the expected trajectory, the structural control that stops it and the alert that should fire.

**Rubric:**

| Criterion | The question to ask yourself |
|---|---|
| Change discipline | Could the model change behind the feature without a commit, and would anyone know by morning? |
| Grounded evals | Do the evaluators come from failures you found in traces, or from metrics you imagined? |
| Calibrated judgment | Is each judge's agreement with humans known per category, and re-checked when it drifts? |
| Planned degradation | On a 30× disruption day with the quota gone, what does a passenger see at 07:41? |
| Structural authority | Could any text in a booking field move a passenger who did not ask to be moved? |
| Bounded blast radius | What is the worst voucher spend an attacker can reach in an hour, and who chose that number? |

#### Where you now stand

You can now operate a component that is fluent and usually right: ship its prompts and models as deployments, pin what can move, evaluate it with calibrated instruments, sample production as surveillance, degrade it by a ladder decided in advance and give its agents only the authority a bad day can afford. Weizenbaum's secretary trusted a program within minutes; our job is to make trust slower and better earned. Chapter 15 turns from the system to the organization that runs it, and brings the whole book to bear on Vesper Hale's stadium dates.

### References

- Shreya Shankar, Hamel Husain — [*Evals for AI Engineers*](https://www.oreilly.com/library/view/evals-for-ai/9798341660717/). O'Reilly, 2026.
- Chip Huyen — [*AI Engineering*](https://www.oreilly.com/library/view/ai-engineering/9781098166298/). O'Reilly, 2025.
- Joseph Weizenbaum — [*Computer Power and Human Reason: From Judgment to Calculation*](https://en.wikipedia.org/wiki/Computer_Power_and_Human_Reason). W. H. Freeman, 1976.
- Joseph Weizenbaum — [*ELIZA — A Computer Program for the Study of Natural Language Communication between Man and Machine*](https://doi.org/10.1145/365153.365168). Communications of the ACM, 1966.
- Cathy Chen, Niall Richard Murphy, Kranti Parisa, D. Sculley, Todd Underwood — [*Reliable Machine Learning*](https://www.oreilly.com/library/view/reliable-machine-learning/9781098106218/). O'Reilly, 2022.
- Chip Huyen — [*Designing Machine Learning Systems*](https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/). O'Reilly, 2022.
- Steve Wilson — [*The Developer's Playbook for Large Language Model Security*](https://www.oreilly.com/library/view/the-developers-playbook/9781098162191/). O'Reilly, 2024.
- Ken Huang, Chris Hughes — [*Securing AI Agents*](https://link.springer.com/book/10.1007/978-3-032-02130-4). Springer, 2025.
- Phillip Carter — [*Observability for Large Language Models*](https://www.oreilly.com/library/view/observability-for-large/9781098159757/). O'Reilly, 2023.
- D. Sculley et al. — [*Hidden Technical Debt in Machine Learning Systems*](https://proceedings.neurips.cc/paper_files/paper/2015/hash/86df7dcfd896fcaf2674f757a2463eba-Abstract.html). NeurIPS, 2015 — free online.
- Norm Hardy — [*The Confused Deputy (or why capabilities might have been invented)*](https://doi.org/10.1145/54289.871709). ACM SIGOPS Operating Systems Review, 1988.
- Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan — [*τ-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains*](https://arxiv.org/abs/2406.12045). arXiv, 2024 — free online.
- Jacob Cohen — [*A Coefficient of Agreement for Nominal Scales*](https://doi.org/10.1177/001316446002000104). Educational and Psychological Measurement, 1960.
- Michael B. Jones et al. — [*RFC 8693: OAuth 2.0 Token Exchange*](https://www.rfc-editor.org/rfc/rfc8693). IETF, 2020 — free online.

---

## Chapter 15: The Production Organization and the Capstone {#ch15}

> No one flies the mission alone, and no one learns to fly it on the day.

Fourteen chapters have treated production as a system of parts, each of which, we kept saying, is held in place by people. This last chapter turns to the people directly. It asks how an organization should be arranged so that many specialists, and a growing number of machines, can run one system together without any of them having to hold the whole of it in their heads.

The best answer I know was worked out in a room in Houston in the 1960s. NASA's Mission Control put a spaceflight in the hands of flight controllers, each the owner of one system or one discipline: guidance, propulsion, electrical power, the trajectory itself. The front row, where the trajectory specialists sat, was known as the trench. Behind each controller stood a back room of further specialists, joined to the front by voice loops that a controller could monitor several at a time, so that the person at the console carried a summary while the detail lived one room away. Above them sat the flight director, who by long-standing rule could take whatever action the crew's safety and the mission's success required. It was decomposition and hierarchy built out of people: each console a module with a narrow interface, each back room hidden behind it, and one role whose job was the whole.

The arrangement was tested at the worst possible moment. On 20 July 1969, during Apollo 11's descent to the Moon, the lunar module's guidance computer raised program alarms, 1202 and then 1201, which meant it was overloaded and shedding lower-priority work to protect the tasks that mattered. The guidance officer, Steve Bales, had seconds to decide whether to abort the landing. In his back room Jack Garman recognized the alarms and judged them safe while they did not persist; Bales called "go", and the landing went on. They knew because a training simulation a few weeks earlier had thrown a similar alarm at them, and the controllers had called an abort that was not needed, at a moment when being wrong cost nothing. Afterwards Garman wrote out what every alarm code meant. A structure, a culture and a rehearsal saved that landing, and those three things are the subject of this chapter.

Encore, in this final chapter, stands where Mission Control stood after a hard flight. The Vesper Hale postmortem of Chapter 13 has produced its changes, and the promoter has announced four added stadium dates for the tour, on sale on a Friday six weeks from now. Four sections examine how that organization is shaped, owned, trained and cultured; the fifth runs the day itself, and with it the whole book.

### 15.1 SRE Team Models — Embedded, Central, and Platform

#### Where reliability expertise lives {#where-reliability-expertise-lives}

An **SRE team model** is the decision about where reliability expertise sits relative to the services it protects, and therefore about who notices trouble, who decides and who is woken. Site reliability engineering (SRE) began at Google in 2003 as a separate team that took over the pager for services meeting its standards, and in the two decades since, the industry has tried most of the arrangements available. They differ mainly in how close the engineers sit to the code and how many teams each can reach.

| Model | Reliability engineers… | Strength | Typical failure |
|---|---|---|---|
| Central ("kitchen sink") | run operations for many services from one team | consistency; one place where lessons accumulate | becomes the old operations team with a new title, and a queue |
| Embedded | sit inside a product team, on its roadmap | context; influence on design before it hardens | isolation; drift into being extra feature developers |
| Consulting | advise many teams and own no services | reach at low cost per team | advice without consequences; little feel for the pager |
| Platform-aligned | own the reliability of shared infrastructure and tooling | leverage: one fix serves every team | distance from product-specific failure modes |
| Hybrid with champions | keep a small central team, embed temporarily, name a champion in each team | reach and context together | champions without protected time become names on a list |

*Figure 15.1 — SRE team models and how each tends to fail. Most organizations end up hybrid; the useful question is which failure mode they have chosen to watch for.*

The literature grew plural as the practice spread. David Blank-Edelman's *Becoming SRE* describes centralized, embedded and hybrid integration, the stages such organizations pass through, and the commonest failure, title flipping: renaming the operations team and changing nothing else. *Seeking SRE*, which he edited, records the alternatives, among them Spotify's practice of SRE without a dedicated SRE team and Facebook's production engineering. Google's second edition of *Site Reliability Engineering*, published this year, describes (by its announcement) hybrid models, closer ties to platform engineering and reliability champions placed inside product teams. Each model trades context against reach, and no position on that line stays right as an organization grows. Figure 15.2 draws the line.

{% include diagrams/fig-15-2.svg %}

*Figure 15.2 — SRE team models placed by context and reach. The pure models sit near one trade-off line; a hybrid with champions tries to get above it, which is where Encore now aims.*

A hospital teaches the shape well. The ward owns its patients, and one attending physician answers for each of them. Specialists consult and leave notes; an intensivist joins for the critical days; the hospital's engineers keep the oxygen and the power running for every ward at once. The analogy breaks at the point that matters most, because a good SRE practice does not merely treat the patient in front of it. It changes the system so that the next patient never needs the specialist at all.

Encore's version is the Reliability team: 10 engineers in the platform group, led by a staff SRE. For the platform planes the team is platform-aligned and holds the pager. For the 40 stream-aligned teams it consults, through the service level objective (SLO) tooling, the incident process, the on-sale readiness review and the game-day program, and for big launches it embeds. Ten people cannot run 40 teams' services, and they should not try; what they can do is raise the floor beneath all of them, since one well-made SLO tool is a single abstraction that 40 teams share. After Vesper Hale, Encore added the hybrid's last ingredient, a reliability champion in every stream-aligned team with a tenth of their time protected in planning. Seen this way, an SRE team model is a decomposition of attention, and like any decomposition it is judged by what it leaves at the seams.

**Recap.** Team models trade context for reach: embedded engineers know one system deeply, while central, consulting and platform teams touch many. Most mature organizations combine them and should watch deliberately for their combination's characteristic failure. A small reliability team earns its keep by raising the floor through shared tools and practices, never by running everyone else's services.

**Exercise 15.1.** Place your organization in Figure 15.1, honestly rather than by its org chart. Then name the failure mode in that row and one piece of evidence that it is, or is not, happening to you now.

### 15.2 Ownership — You Build It, You Run It, and Its Limits

#### What "you run it" asks of a team {#what-you-run-it-asks}

Vogels's "you build it, you run it", which the companion volume took as a principle of operable design, closes the loop between the people who change a system and the people who feel the consequences. It is the right default, and Encore's teams live by it, but a principle repeated for 20 years acquires the sound of a law, so it is worth stating what it asks. **Operational ownership** is a named team's accountability for a service's behavior in production (its objectives, its pager, its runbooks and its retirement) together with the authority to change it. Accountability without authority is blame waiting to happen; authority without accountability is the old wall between development and operations, rebuilt under a new name.

The principle has three limits, and each is a matter of complexity. The first is **cognitive load**. Skelton and Pais's *Team Topologies* (first published in 2019, in a second edition in 2025) made the point that a team can own only as much as it can understand, and that the size of a team's software should be set to fit its mind and not the other way round. Their remedy is a platform offered as a service and enabling teams that teach rather than take over, so that a team's load is mostly the essential complexity of its own domain. The Notification rewrite of Chapter 1, 40 files nobody had read in full, was a small lesson in what happens when ownership outruns understanding: the team owned the service on paper and a stranger in practice.

The second limit is arithmetic. A team of five on a weekly round-the-clock rotation is on call one week in five, and Chapter 12 has shown what that does to people. Encore pairs its smallest teams with a sibling team for out-of-hours paging, so that each rotation has at least eight people in it, and reserves the single incident commander rotation for senior engineers drawn from across teams. Google's engagement model adds a useful escape valve: SRE can hand the pager back to developers when a service falls below its standards, which treats ownership as a contract whose terms can be renegotiated when they are broken.

The third limit is the seam between owners. On the day of the Vesper Hale on-sale every component had an owner, and the hazard lived in none of them; it lived in the interaction between a reconciler, a calendar, a cache and a bot rule, as Chapter 13's causal analysis based on systems theory (CAST) drew it. Ownership of components leaves the interactions orphaned unless someone names an owner for them. Encore now does. The on-sale calendar is a published signal owned by the On-Sale team, and any automation that changes the purchase path must declare that it reads it, a check the platform's scorecard enforces. Fournier and Nowland's *Platform Engineering* insists on the same from the other side: platform teams must own the operation of what they build, including when it acts on other teams' services.

A touring production shows the arrangement at its best. The touring crew builds the show and runs it every night, while the venue's house crew owns the rigging points, the power and the fire curtain. It works because the technical rider says who owns which cable, and because one stage manager calls the show for both crews. The analogy breaks on time: no venue rebuilds its rigging during a performance, but Encore's platform drained a node mid-on-sale. A contract between owners must therefore cover time as well as territory. Having spent years on the platform side of exactly this boundary, inside a large bank, I have come to believe that most operational trouble between teams begins with a clause about time that nobody wrote.

Encore's service registry makes this inspectable: each entry names an owning team, rotation, objectives and runbooks, and the scorecard flags gaps. The first sweep found 11 components with no owner, mostly scheduled jobs and a dashboard that three teams relied on. Ownership that cannot be carried at 3 a.m. is only a name on a wiki page.

**Recap.** "You build it, you run it" is the right default and an incomplete one. Ownership needs authority as well as accountability, it must fit a team's cognitive load and its rotation arithmetic, and the seams between owned components need owners of their own. A contract between teams should say when each may act, as well as what each owns.

**Exercise 15.2.** List the services your team owns and the people on its rotation. Compute weeks on call per person per year. Then name one interaction between your service and another team's that nobody owns, and propose who should.

### 15.3 Skills, Training, and Operational Maturity

#### Rehearsing the day before it comes {#rehearsing-the-day}

Mission Control's competence was manufactured, and the factory was the simulation. A team led by the simulation supervisor, the SimSup, designed failures and injected them into full-scale rehearsals with crews and controllers at their consoles; the debrief afterwards mattered as much as the run. The 1201 alarm of Apollo 11 was not luck. It was the dividend of a rehearsal that went wrong in the right place, followed by someone writing down what had been learned. Everything learned about operational skill since elaborates that loop: realistic practice, honest debrief, a written artifact, practice again.

The need is sharper for us than it was for Houston, because of the irony Chapter 3 described. Automation removes the routine work in which skill used to be acquired, and hands back to people the rare and hard cases in which skill is most needed. At Encore, shard failover is automatic and fenced, and it works; that is precisely why few engineers have ever performed one by hand, and why the 40 seconds of rejected writes during Vesper Hale were understood quickly only by those who had. Unexercised skill decays quietly, and the decay is invisible until the day it is needed.

The practices that keep it are cheap compared with what they prevent. The **Wheel of Misfortune**, described in Google's first SRE book (2016), is a role-play in which a game master narrates a past incident and an engineer works through it aloud, asking for the dashboards and logs they would consult; it costs an hour and risks nothing. A game day, which Chapter 9 introduced as an experiment on the system, becomes training when we measure the people too: time to declare, whether a commander was named, whether the status page told the truth. **Shadowing** puts a new engineer beside an experienced one on call, and **reverse shadowing** swaps the seats, so that the newcomer leads while the veteran watches and stays silent unless needed. Atul Gawande's *Checklist Manifesto* adds the discipline of the pause point, a moment in a procedure at which the team stops and confirms the few things that kill when forgotten; Encore's readiness review is such a pause point, and like any good checklist it is short and tested.

Encore's program, rebuilt after Vesper Hale, has five parts. Each team runs a monthly Wheel of Misfortune drawn from its own postmortems. Every quarter, an engineer who has never done one performs a manual shard failover in a staging cell, with someone who has standing behind them. New members of a rotation do two shadow weeks and one reverse-shadow week before carrying the pager alone. Incident commander candidates command two simulated on-sales before they command a real one. And in half of all drills Cue is switched off, so that the team's own judgment is kept in use rather than delegated to a fluent summary. The first time anyone performs a failover should never be the time it counts.

How do we know whether all this is working? The tempting answer is a **maturity model**, a ladder of levels against which an organization grades itself. *Accelerate* argued against such ladders in favor of capabilities that can be measured and improved, because a level suggests an arrival and production offers none. A more useful frame is the hierarchy Mikey Dickerson drew for Google's first SRE book, and which *Becoming SRE* recommends as a place to start: monitoring at the base, then incident response, postmortems, testing and release, capacity planning, development and finally product. It reads best as an order of construction: a team that cannot yet see its system should not be building elaborate release automation.

**Recap.** Operational skill is produced by rehearsal under realistic pressure and an honest debrief, and automation makes rehearsal more necessary, not less. Wheels of Misfortune, game days that measure people, shadowing and pause points keep skills alive at low cost. Maturity is better read as an order of construction than as a grade.

**Exercise 15.3.** Name the three operations your team would most need in a real incident. For each, find the last date someone on today's rotation performed it by hand. Schedule a drill for the oldest.

### 15.4 Culture — Generative Organizations and Psychological Safety

#### How information flows {#how-information-flows}

Structure and training decide what an organization *can* do under pressure; culture decides what it will actually hear. The sociologist Ron Westrum, studying safety in aviation and medicine, classified organizations by how they handle information, and set out the typology in its best-known form in 2004.

| | Pathological | Bureaucratic | Generative |
|---|---|---|---|
| Orientation | power | rules | performance |
| Messengers | shot | neglected | trained |
| Responsibilities | shirked | narrow | shared |
| Bridging between teams | discouraged | tolerated | encouraged |
| Failure leads to | scapegoating | justice | inquiry |
| Novelty | crushed | becomes a problem | implemented |

*Figure 15.3 — Westrum's typology of organizational cultures. Each column describes what happens to an inconvenient fact.*

Westrum's insight was that safety depends on information reaching the people who can act on it, in time and in a form they can use, and that culture is the main thing that speeds or blocks it. *Accelerate* later measured his typology across thousands of survey responses and found that generative culture predicts software delivery performance and organizational performance, and that culture can be moved by changing practices: teams that adopted continuous delivery and lean management became more generative as a consequence. Culture, in other words, sits near the top of Meadows's leverage points, at the level of paradigm, and yet it can be reached from the bottom, one practice at a time; DORA's more recent findings on AI adoption, which the companion volume discussed, suggest the same lesson applies to new tools.

The second strand comes from Amy Edmondson, who in 1999 defined **psychological safety** as a shared belief that the team is safe for interpersonal risk taking, and showed that teams holding that belief engaged more in learning behavior (asking for help, admitting errors, raising concerns), which in turn improved their performance. Google's later internal study of its own teams, Project Aristotle, reached a similar conclusion. Psychological safety is easily mistaken for comfort. It is closer to candor: the confidence that saying "I think the freeze is drifting" in a meeting will be met with interest, and that accountability, as Chapter 13 argued, looks forward to repair rather than back to blame.

Apollo 13 is the finest demonstration I know of generative information flow under pressure. After an oxygen tank exploded in April 1970, the crew retreated into the lunar module, whose carbon dioxide scrubbers could not last for three men and the long way home. The command module had spare lithium hydroxide canisters, but they were square, and the lunar module's sockets were round. Engineers on the ground built an adapter from materials the crew had on board (plastic bags, cardboard, hoses from the pressure suits and tape), tested it, and read the instructions up to the spacecraft step by step. An idea from people far from the front row reached the flight director, was trusted, and became a procedure in time; that is Westrum's generative column in a single episode. The analogy has limits worth saying aloud: Mission Control in the 1960s was also a place of punishing hours and rigid hierarchy, and an organization can be generative in a crisis and pathological on an ordinary Tuesday. Karl Weick and Kathleen Sutcliffe's phrase for the quality we want, **deference to expertise**, means letting the decision travel to whoever knows most, whatever their rank, on the ordinary days as well.

At Encore, Westrum's survey items now sit in the quarterly engineering survey, reported per team and never used to rank them. Readiness reviews open with the question "what are we worried about?", and the first answer is thanked before it is examined. Psychological safety also has a new object. During Vesper Hale, Jonas declined Cue's confident suggestion to restart Seat Inventory pods, in front of a busy channel, and was right to; a culture in which people feel safe contradicting a fluent machine is now as important as one in which they feel safe contradicting a senior colleague. A culture can be measured by how far bad news travels before someone softens it.

**Recap.** Westrum's typology describes culture by what happens to inconvenient information, and DORA's research ties generative culture to performance while showing that practices can change it. Psychological safety is the team-level condition for learning, closer to candor than to comfort. In an era of fluent assistants, it must include the safety to disagree with the machine.

**Exercise 15.4.** Recall the last time someone in your organization raised an unwelcome risk. Which column of Figure 15.3 describes what happened next? Write down one practice that would move it one column to the right.

### 15.5 Capstone — Operating One System End to End

#### The added dates {#the-added-dates}

Four added stadium dates for Vesper Hale go on sale at 10:00 CET on a Friday, with about 1.4 million fans expected in the waiting room across the four events. The postmortem's changes exist. The question is whether the organization can run them together, against a hard start time and a very public audience.

| When | What Encore does | From |
|---|---|---|
| T−6 weeks | On-sale-window SLOs for the four events: 99% of admitted fans finish without an error page in the first 60 minutes, beside the standing seat-map and checkout objectives; the window's error budget agreed with the organizer-facing team | Chapter 4 |
| T−5 weeks | Cold-cache load tests at 1,200 and 1,500 fans/s per event; admission held at 1,200; home regions split two events each; the pre-warm workflow now verifies cache hit ratio before the Gate opens | Chapters 6, 10 |
| T−4 weeks | Bot velocity rule retuned so that retries after server errors count as fan behavior; run in shadow mode against recorded on-sale traffic | Chapters 9, 11 |
| T−3 weeks | Two Reliability engineers embed with the On-Sale team; incident commander, communications lead, operations leads and scribe named | Sections 15.1, 12.2 |
| T−2 weeks | Calendar-aware automation verified: the node-upgrade reconciler holds drains on purchase-path pools from T−2h until the sale ends | Chapters 7, 13 |
| Tuesday before | Game day in a staging cell: cold cache, shard failover and a retry burst, with a Reliability engineer as SimSup | Chapter 9, Section 15.3 |
| Wednesday | Readiness review, a pause point; the exception register opened | Chapters 8, 13 |
| Friday 08:00 | Freeze begins; two exceptions logged, each with an approver and a reason | Chapters 8, 13 |
| Friday 10:00 | Gate opens; Cue posts the calendar, deploy history and exception register to the incident channel | Section 12.4 |
| T+1 week | Review of an on-sale that went well | Section 13.4 |

*Figure 15.4 — The added dates, end to end, with the chapter each step comes from. Read down the right-hand column and the book appears in order of use rather than order of writing.*

The game day found the weakest step. Re-admitting wrongly blocked fans with their queue positions restored, the fix applied at 10:31 during Vesper Hale, had been done by hand, and in rehearsal it took 14 minutes. It became a scripted workflow in the self-service style of Chapter 3, which Cue may propose but only a human in the channel may approve.

The day itself was gratifyingly dull. At 10:09 a Dutch issuing bank's card authentication slowed, and checkout success for Dutch fans dipped; the window's burn-rate alert fired at its slower threshold. The incident commander asked Cue for the breakdown, confirmed that the slowdown sat outside Encore at the payment service provider (PSP) boundary, chose not to act beyond a status-page note for Dutch fans, and wrote the decision into the log. Choosing not to act is also a decision, and a record that omits it misleads. About 22% of the window's error budget was spent, no exception beyond the two registered was requested, and all four dates sold out within the hour. Figure 15.5 shows the Friday itself.

{% include diagrams/fig-15-5.svg %}

*Figure 15.5 — The Friday of the added dates, with the morning before the Gate opened compressed. The red ink is the error budget, spent mostly after 10:09; the 09:40 line marks the hand-run check that the later review would find.*

#### Learning from a good day {#learning-from-a-good-day}

Encore held a review anyway, because Chapter 13 taught it that success is data too. It asked what had gone right and why, and found an adaptation nobody had designed. The pre-warm check had timed out on its first run at 09:40, and an engineer had rerun it by hand, read the cache hit ratio from a dashboard, and moved on without telling anyone. That was Safety-II in miniature, a person filling a gap the procedure did not know it had, and the review turned it into a retry with an explicit failure path. A success we do not examine teaches us only to expect another.

Read back across the day and the book's through-line becomes visible: no single control made the dates go well. Objectives told people what mattered, telemetry let them see it, capacity arithmetic and cold-cache tests kept the load honest, calendar-aware automation kept the machines from acting at the wrong moment, the freeze and its register made exceptions visible, rehearsal made the likeliest failure familiar, roles meant nobody had to improvise authority, and a review turned an ordinary success into learning. Reliability was produced, as it always is, by people and machines together.

**Recap.** The capstone is a system run end to end: SLOs, capacity, change control, automation, rehearsal, incident roles, AI assistance and review, each placed in time against a known peak. A dull day is what all the preparation was for, and a review after success finds the adaptations that made it so.

**Exercise 15.5.** Choose the next predictable peak your system faces. Build its version of Figure 15.4, with a "From" column pointing to the practices you already have. Each blank cell is your preparation plan.

### Kata: The Capstone Kata — Results Day

> **Your brief: "Quorum."** Quorum runs the online admissions platform for universities in four EU countries: 1.8 million applicants a year and 300 institutions as tenants. Load is steady except on two days. On deadline day, submissions rise 40× in the final six hours; on results day, 600,000 applicants sign in within the first hour after 08:00 to learn their offers. Quorum has 95 engineers in 12 teams, and a central operations team of six holds every pager; two of its members left last year. The applications database is one primary with a replica in the same region, and nobody has restored a full backup. An AI assistant answers applicants' questions about entry requirements, and last spring it told some applicants a deadline one day too late. Last year's results day had 52 minutes of errors after a scheduled certificate rotation restarted the authentication service at 08:05. The board's request: make results day boring.

**Deliverables:**

1. **Operating model** — the team model from Figure 15.1, an ownership map for every service and seam, on-call arithmetic per rotation, and what becomes of the central operations team.
2. **Objectives and signals** — results-day and deadline-day window SLOs, burn-rate alerts, and the traces and high-cardinality fields that would answer "which institution's applicants are failing, and since when?"
3. **Capacity and runtime plan** — arithmetic for the first hour, cold-start and cold-cache tests, scaling limits, and cost per applicant.
4. **Change and resilience plan** — a freeze with an exception register, calendar-aware automation (certificate rotation included), canary policy, and a game day with a named SimSup.
5. **Data and security plan** — a timed restore drill against stated recovery time and recovery point objectives, owned secret and certificate rotation, and data residency per country.
6. **Incident and learning plan** — staffed roles for both days, status-page templates, a CAST review of last year's certificate incident, and a scheduled review of this year's results day however it goes.
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
| Rehearsal | Will results day be the second time, not the first, that the team meets its likeliest failure? |
| Learning | Is there a plan to learn from the day if it is boring? |

#### Where you now stand

You began this book with a computer operator at a console and end it in a room full of them, human and otherwise, working one mission. Along the way you have learned to set objectives users would recognize, to see a system through its telemetry, to reason about queues and cost, to let control loops work while knowing their ironies, to ship change in small reversible steps, to design for failure and rehearse recovery, to command an incident and learn from it without blame, and finally to shape the organization that does all of this. None of it is finished, because production never is; the system you run will be different next quarter, and so will the people running it. What lasts is the habit of treating reliability as something produced every day by people and machines together, and of investing in the people as seriously as in the machines. Somewhere tonight a system is running because someone rehearsed for the night it wouldn't. Be that someone.

### References

- Matthew Skelton, Manuel Pais — [*Team Topologies*, 2nd ed.](https://teamtopologies.com/book). IT Revolution, 2025.
- Betsy Beyer, Chris Jones, Christof Leng, David Huska, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*, 2nd ed.](https://www.oreilly.com/library/view/site-reliability-engineering/9798341607675/). O'Reilly, 2026.
- David N. Blank-Edelman — [*Becoming SRE*](https://www.oreilly.com/library/view/becoming-sre/9781492090540/). O'Reilly, 2024.
- Ron Westrum — [*A Typology of Organisational Cultures*](https://doi.org/10.1136/qshc.2003.009522). Quality and Safety in Health Care, 2004.
- Amy Edmondson — [*Psychological Safety and Learning Behavior in Work Teams*](https://doi.org/10.2307/2666999). Administrative Science Quarterly, 1999.
- Nicole Forsgren, Jez Humble, Gene Kim — [*Accelerate*](https://itrevolution.com/product/accelerate/). IT Revolution, 2018.
- Camille Fournier, Ian Nowland — [*Platform Engineering*](https://www.oreilly.com/library/view/platform-engineering/9781098153601/). O'Reilly, 2024.
- David N. Blank-Edelman (ed.) — [*Seeking SRE*](https://www.oreilly.com/library/view/seeking-sre/9781491978856/). O'Reilly, 2018.
- Karl E. Weick, Kathleen M. Sutcliffe — [*Managing the Unexpected*, 3rd ed.](https://www.wiley.com/en-us/Managing+the+Unexpected%3A+Sustained+Performance+in+a+Complex+World%2C+3rd+Edition-p-9781118862414). Wiley, 2015.
- Betsy Beyer, Chris Jones, Jennifer Petoff, Niall Richard Murphy (eds.) — [*Site Reliability Engineering*](https://sre.google/sre-book/table-of-contents/). O'Reilly/Google, 2016 — free online.
- Atul Gawande — [*The Checklist Manifesto*](https://atulgawande.com/book/the-checklist-manifesto/). Metropolitan Books, 2009.
