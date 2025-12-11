# Atmospheric Rivers & NSR Besetting Risks: Monte Carlo Simulator

This repo hosts a Python-based Monte Carlo model estimating atmospheric river (AR)-induced entrapment (besetting) risks for Northern Sea Route (NSR) transits, based on 2024–2025 ERA5 reanalysis data. Simulates 10K voyages to output probabilities, costs, and distributions—key for ice-class ship insurance (H&M/P&I) modeling.

## Why This Matters
ARs drive 60–80% of Arctic melt but spawn fog traps (15–20% beset odds by 2040). Mean cost: $1.75M/transit. See full analysis: [Atmospheric Rivers NSR Report](https://docs.google.com/document/d/e/2PACX-1vStGVcin9Ql2ff1ob3Z9hEcT2AXHmtU1zy6dThDFqA036sicfQJbt8qWuTEHcgm4eTQZ6oUMYShazQg/pub).

## Quick Start
1. Clone: `git clone https://github.com/anirbanmarine/atmospheric_rivers.git`
2. Install: `pip install numpy pandas matplotlib`
3. Run: `python nsr_monte_carlo.py`
4. Outputs: Console summary + `besetting_cost_hist.png` (tail-risk distro).

## Key Params (Edit & Rerun)
- `ar_prob = 0.3`: Baseline AR frequency (triples by 2040).
- `salvage_cost = 10_000_000`: $10M/incident.
- Add sensitivity: e.g., `ar_prob = 0.4` for 20% beset scenario.

## Sample Output
| Metric              | Value          |
|---------------------|----------------|
| Beset Prob          | 14.6%         |
| Mean Cost/Transit   | $1,750,800    |
| 95% CI High         | $12,000,000   |

## License
MIT—fork away for your AR models.

Questions? @anirbanmarine on X or email [marine.anirban@gmail.com].
