# L6 Engineering Audit — Cautious Enigma

## Executive assessment

Cautious Enigma has a credible production-shaped anomaly-detection system: reproducible Isolation Forest benchmarking, FastAPI serving, Prometheus telemetry, model-registry integrity verification, non-root containerization, Kubernetes hardening checks, CI, Trivy scanning, SPDX SBOM generation, and semantic-tag GHCR publication.

The strongest L6 narrative is not "production-ready threat detection." It is **evidence-bounded ML systems engineering for anomaly detection**. The repository has meaningful runtime and supply-chain controls, but predictive quality and operational reliability remain separate promotion gates.

## Verified strengths

- seeded synthetic benchmark generation with versioned JSON evidence;
- deterministic anomaly count checks under fixed parameters;
- bounded Pydantic API contracts and max batch size;
- optional constant-time API-key comparison;
- Prometheus request counters and latency histograms;
- model-registry artifact integrity checks before deserialization;
- non-root container runtime using UID 10001;
- health/liveness/readiness endpoints;
- Kubernetes schema and hardening assertions;
- Trivy filesystem/image scans and SPDX SBOM generation;
- semantic-tag container publication and keyless signing path.

## Critical gaps

### 1. Systems performance is not model quality

The current benchmark is valuable computational evidence, but it does not establish precision, recall, PR-AUC, false-positive rate, calibration, fairness, or threat-detection efficacy. Those claims require a labeled and versioned evaluation corpus.

### 2. Reference benchmark sample is intentionally small

The documented reference run uses only five timed iterations. That is enough for a reproducibility smoke benchmark, not enough for comparative performance claims or an SLO.

### 3. Deployment validation is primarily static/smoke based

Kubeconform and hardening assertions are useful, but they do not replace deployment into an ephemeral cluster, rollout/rollback testing, readiness transition tests, failure injection, or resource-pressure validation.

### 4. Operational SLO evidence is absent

The repository does not yet provide a repeatable load-test artifact tying p50/p95/p99, throughput, error rate, CPU, memory, concurrency and payload shape to a commit and environment.

### 5. API-key behavior is configuration-dependent

Prediction routes are protected only when `CAUTIOUS_API_KEY` is set. Documentation must not imply unconditional authentication.

### 6. Release provenance can be stronger

The supply-chain workflow already scans, emits an SPDX SBOM and signs semantic-tag images. Release evidence is stronger when source checksums, OCI source/revision/version labels, image digests and attestation output are all tied to the same tag.

## Promotion criteria — predictive quality

Before making detection-quality claims, require:

- immutable labeled dataset/manifests with provenance and license constraints;
- leakage-safe train/validation/test separation;
- versioned feature engineering;
- fixed seeds or declared repeated-evaluation design;
- baseline comparison;
- precision, recall, F1 and PR-AUC;
- confidence intervals or repeated-run uncertainty where appropriate;
- false-positive analysis by log/traffic cohort;
- pre-declared threshold-selection strategy;
- drift/OOD analysis;
- model-card update and artifact SHA-256 tied to the evaluated commit.

## Promotion criteria — runtime reliability

Before making production SLO claims, require:

- machine-readable load-test artifacts;
- p50/p95/p99 latency and throughput;
- request error rate;
- CPU and peak memory;
- concurrency and payload-shape provenance;
- graceful shutdown and readiness transition evidence;
- rollout/rollback exercise in an ephemeral Kubernetes environment;
- resource-pressure/failure-injection tests;
- documented alert thresholds and incident runbooks.

## Evidence rule

Every numerical claim should be traceable to a command, commit SHA, environment, input fixture or dataset identity, sample count and configuration. A passing workflow proves that its checks passed for a commit; it does not prove production authorization or real-world model effectiveness.
