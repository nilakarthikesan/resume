# Resume claim check: 2026-10-18

This update prioritizes LLM-agent evaluation, security controls and empirical
research engineering. It does not claim mechanistic interpretability research,
frontier-model pretraining, human-subject experiments, or publication acceptance
for the new exploratory projects.

## Selected research

- **SafeLattice:** the public [project](https://github.com/nilakarthikesan/claw-eval-safelattice)
  documents the contributor's extension and credits upstream Claw-Eval. The
  [saved live statistics](https://github.com/nilakarthikesan/claw-eval-safelattice/blob/main/analysis/safelattice_live_stats.json)
  record six models, 50 tasks and 1,222 traces. The
  [detection report](https://github.com/nilakarthikesan/claw-eval-safelattice/blob/main/analysis/safelattice_live_detection.json)
  records F1 0.8057 versus 0.1111 for binary detection, with SafeLattice precision
  0.6746 and recall 1.0. These are study-specific saved measurements, not proof of
  general safety or a newly run evaluation. The 68-trace synthetic corpus in the
  top-level README is a separate experiment; its numbers are not blended into
  the live-study claim. No acceptance or submission status is asserted.
- **Never Trust the Context:** the implemented
  [paired study design](https://github.com/nilakarthikesan/never-trust-the-context/blob/2c5fd166339b0f094a1fab1fd77518fd838b9c3d/design/paired-outcome-study.md)
  and scorer add ten original clean/perturbed scenario pairs and regression
  checks for decision corruption, grounding and required-claim coverage.
  Live-model execution remains pending. Test counts validate the software, not
  model robustness; the resume deliberately omits test-count performance claims.
- **Grasp recovery:** the existing versioned
  [pilot report](https://github.com/nilakarthikesan/grasp-recovery-under-delayed-feedback/blob/54aa4b1c6c3e7c0aba5de881ea3025954090e6a0/results/pilot_v1/report.json)
  supports 400 episodes, 88,728 branches and 94 held-out episodes. The resume
  retains the lack of completion advantage for the latency-aware selector and
  the preliminary simulation-only limitation.
- **GTSfM:** workshop credit and the visualization contribution are retained from
  the previously verified profile/resume, linked to the
  [visualization project](https://github.com/nilakarthikesan/visualization-gtsfm-paper).
  This is an ECCV 2026 SfM-DL workshop presentation, not a claim of an ECCV main
  conference paper.
- **Additional prototypes:** synthetic annotation-disagreement/time-shift and
  narrative-framing evaluation tools are published as early research
  scaffolds. They do not yet have real-model or consented human-panel results.

## Experience and education

Existing titles, organizations, dates and degrees were preserved from the
versioned resume. Industry bullets were condensed without adding new metrics.
The 100,000+ inventory records, 500+ engineers, 40% query-latency reduction,
50% reporting-processing improvement, and 8x retrieval improvement are retained
user-provided resume claims, not independently audited employer metrics.
Palantir remains explicitly a fellowship. Advisers and collaborators were not
added to the new exploratory projects as agreed coauthors.

## Build checks

The PDF is generated from JSON, with an explicit one-page bounds check, embedded
serif fonts where available, and linked project sources. Render every page and
inspect the image before publication. The saved official PDF and editable source
must be committed together by the publishing workflow.
