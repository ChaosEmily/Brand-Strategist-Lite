# Brand Strategist Lite

A human-in-the-loop brand positioning tool built on a four-layer transparent architecture. AI handles data structuring; humans handle all scoring and strategic decisions.

## Architecture

```text
JTBD (What tasks do users need to accomplish?)
  ↓ Determines evaluation dimensions
Bain 30 (How well does each brand deliver on these dimensions?)
  ↓ Produces quantitative comparison
3C Matrix (Who is strong/weak where? Where are the gaps?)
  ↓ Identifies positioning opportunities
Archetype (What personality to use when communicating this position?)
```

Each layer's input comes strictly from the previous layer's output.

## Four Layers

### Layer 1: JTBD Extraction (AI executes, human confirms)

- AI extracts verbatim quotes from interviews, categorizes into Functional / Emotional / Social Jobs
- User confirms or corrects classifications, selects top 3-5 Jobs
- Gate: ≥3 interviews required; each Job must appear in ≥2 interviews

### Layer 2: Bain 30 Selection & Human Scoring (AI suggests, human scores)

- AI suggests 8-10 relevant elements from Bain 30 based on Jobs; user confirms
- User scores importance ($W_u$ 1-10) with interview evidence
- User scores delivery ($S_c$, $S_{corp}$ 1-10) with factual evidence
- Gate: scores without evidence are marked "unverified" and excluded from computation

### Layer 3: 3C Matrix Computation (pure math, no AI)

- Gap = $S_{corp}$ - Max($S_c$) (positive = we win)
- Strength zone: $W_u$ ≥ 7 and Gap > 0
- Opportunity zone: $W_u$ ≥ 7 and Gap < 0
- Low priority: $W_u$ < 5
- Fully deterministic — same inputs always produce same outputs

### Layer 4: Positioning Options (AI assists, human decides)

- AI generates 2-3 positioning options based on strength zones
- Each option includes: supporting evidence, suggested Brand Archetype, risks and prerequisites
- User selects direction; AI then expands into communication strategy

## Getting Started

1. Add ≥3 user interviews: `/add-interview`
2. Add competitors: `/add-competitor`
3. Add your brand info: `/add-brand-info`
4. Run full workflow: `/brand-run`

## Key Differences from v1

| Aspect | v1 | v2 |
| :--- | :--- | :--- |
| Scorer | AI self-scores | Human scores with evidence |
| Traceability | No evidence links | Every score tied to source |
| Reproducibility | Non-deterministic | Layer 3 fully deterministic |
| Final output | Single conclusion | 2-3 options, human chooses |
| Archetype | AI-derived "answer" | Communication language option |
| Quality gates | None | Explicit thresholds per layer |
