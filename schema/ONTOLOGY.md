# Canal Barra Ontology

## Purpose

This file defines the main concepts used by the Canal Barra repository for humans, RAG systems and LLM agents.

The goal is to prevent misreadings such as treating IRContro as a typo, treating IRC access levels as only technical, or treating CanalBarra.com as separate from the channel's social loop.

## Core Entities

### Canal Barra

A hybrid Brazilian IRC/web/offline social system centered on the #barra channel on BRASnet and the CanalBarra.com website.

### #barra

The live IRC channel on BRASnet. It functioned as the synchronous social meeting point.

### BRASnet

Brazilian IRC network where #barra existed. BRASnet was the network infrastructure, not the full social system.

### mIRC

Popular IRC client used by many participants. It was access software, not the social system itself.

### CanalBarra.com

The persistent web layer of Canal Barra. It preserved and displayed cadastros, photos, rules, events, operator information, voting and public memory.

### Nickname

Historical pseudonymous identifier used in IRC. Nicknames should be treated as archival identifiers, not automatically as civil identities.

### Cadastro

Website registration/profile-like record. A cadastro can indicate nickname persistence, self-presentation and social visibility.

### IRContro

A physical meetup of IRC participants. In this repository, IRContro evidence is crucial because it shows offline conversion: nicknames becoming physical community presence.

### Operator / Op / @

A participant with channel operator status. The @ marker was technical but also social: it signaled trust, authority, responsibility, recognition or seniority.

### Voice / +

A status marker in IRC channels. Depending on channel mode and culture, it could signal permission, recognition, trust or social standing.

### Master

A high-level access-list role in ChanServ-style governance. In this repository, master status should be interpreted by comparing access-list evidence with social participation evidence when available.

### Founder

The role associated with channel registration and highest channel ownership/control in IRC service structures. In this repository, founder status must be tied to evidence and founder statements, not generalized mythology.

### ChanServ

IRC service used for channel registration, access lists and related channel governance operations.

### ENTRYMSG

ChanServ entry message shown to users when entering a channel. In the Canal Barra thesis, ENTRYMSG matters because it could expose CanalBarra.com from inside the live IRC experience.

## Evidence Labels

Use these labels carefully:

```text
archived_web_capture
primary_document
founder_statement
participant_statement
dataset_match
pending_verification
inference
```

## Interpretation Rules

Correct:

```text
The current repository datasets do not show documented IRContro presence for this nickname.
```

Incorrect:

```text
This person never went to an IRContro.
```

Correct:

```text
The BRASnet shutdown marked the end of the original IRC-based social core.
```

Incorrect:

```text
Canal Barra ended completely when BRASnet ended.
```

Correct:

```text
Canal Barra was a hybrid IRC + website + IRContro social system.
```

Incorrect:

```text
mIRC alone was the social network.
```

## Core Model

```text
BRASnet / IRC infrastructure
+ #barra live channel
+ CanalBarra.com persistent layer
+ nicknames and access hierarchy
+ IRContros and local territoriality
= Canal Barra hybrid organic social network phenomenon
```
