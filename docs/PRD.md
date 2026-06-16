# Product Requirements Document  
**Project:** ideation‑validator  
**Repo:** `arkashira/ideation-validator`  
**Author:** Senior Product & Engineering Lead  
**Date:** 2026‑06‑16  

---

## 1. Executive Summary  

`ideation-validator` is an AI‑powered ideation platform that assists indie hackers, solo founders, and creators in generating software‑tool ideas and validating them against real market signals before any code is written. The tool leverages Axentx’s shared knowledge base (pgVector), large‑scale training data, and production inference engines (vLLM) to surface high‑probability, revenue‑validated concepts that fit the company’s portfolio strategy.

---

## 2. Problem Statement  

- **Idea Silo & Validation Gap** – Indie hackers often generate ideas in isolation and lack a systematic way to test market demand before investing time and money.  
- **High Failure Rate** – 70 %+ of early‑stage software ideas fail due to lack of validated pain points or willingness‑to‑pay.  
- **Duplication Risk** – Without a central validation engine, teams risk re‑inventing ideas already shipped by the company or the broader ecosystem.  

---

## 3. Target Users  

| Persona | Role | Pain Points | How Ideation‑Validator Helps |
|---------|------|-------------|------------------------------|
| **Indie Hacker** | Solo founder, early‑stage startup | Limited time, uncertain market fit | Rapid idea generation + instant market signal scoring |
| **Creator / Influencer** | Content creator, product evangelist | Need fresh, monetizable tool ideas | Curated idea list aligned with audience interests |
| **Product Manager (Axentx)** | Internal PM | Need validated concepts for roadmap | Quick validation pipeline that feeds into the company’s shared BRAIN |
| **Early‑Stage VC / Angel** | Investor | Identifying high‑potential startups | Pre‑validated idea briefs for due‑diligence |

---

## 4. Goals & Objectives  

| Goal | Success Metric | Target |
|------|----------------|--------|
| **Generate high‑quality ideas** | Average idea relevance score (0‑1) | ≥ 0.75 |
| **Validate market demand** | % of ideas with ≥ 1 validated signal | ≥ 60 % |
| **Prevent duplication** | % of ideas flagged as duplicates of existing portfolio | 0 % |
| **Speed** | Time from prompt to validated idea list | ≤ 30 s |
| **User satisfaction** | NPS | ≥ 70 |

---

## 5. Key Features (Prioritized)  

| # | Feature | Description | Acceptance Criteria |
|---|---------|-------------|---------------------|
| **1** | **Prompt‑Driven Idea Generation** | Users enter a brief prompt (e.g., “tool for remote teams”) and receive a ranked list of 5–10 ideas. | • List contains ≥ 5 ideas <br>• Each idea has a title, short description, and relevance score |
| **2** | **Market Signal Validation Engine** | AI model cross‑checks ideas against live market signals (search volume, forum discussions, existing product gaps). | • Each idea is annotated with 3+ validation signals <br>• Signals are sourced from at least 2 distinct data streams |
| **3** | **Duplication Checker** | System queries the shared BRAIN to detect overlap with existing Axentx products. | • Duplicate ideas are flagged with similarity score <br>• No duplicate passes the “validated” gate |
| **4** | **Portfolio Alignment Score** | Calculates how well an idea fits the company’s current portfolio gaps. | • Score ≥ 0.5 triggers “high fit” badge |
| **5** | **Export & Collaboration** | Users can export ideas to CSV/JSON and share via link or Slack webhook. | • Export contains all metadata <br>• Share link is secure (token‑based) |
| **6** | **Feedback Loop** | Users can rate validation accuracy; data feeds back to improve the model. | • Feedback stored in pgVector <br>• Model retraining scheduled weekly |
| **7** | **Rate Limiting & Quotas** | Protects inference engine and enforces fair usage. | • 100 requests/day per user <br>• Exceeding quota shows friendly message |
| **8** | **Admin Dashboard** | Monitor usage, model performance, and data quality. | • Real‑time metrics dashboard <br>• Alert on anomalous validation scores |

---

## 6. Success Metrics  

| Metric | Definition | Target |
|--------|------------|--------|
| **Idea Relevance** | Mean relevance score across all generated ideas | ≥ 0.75 |
| **Validation Rate** | % of ideas with ≥ 1 validated market signal | ≥ 60 % |
| **Duplication Rate** | % of ideas flagged as duplicates | 0 % |
| **Time to Insight** | Avg. time from prompt to final validated list | ≤ 30 s |
| **User NPS** | Net Promoter Score from post‑use survey | ≥ 70 |
| **Model Accuracy** | Precision/recall of validation signals | ≥ 0.8 |

---

## 7. Scope  

| Item | In‑Scope | Out‑of‑Scope |
|------|----------|--------------|
| **AI Model** | vLLM inference engine, fine‑tuned on `instr-resp` + `messages` datasets | Training new large‑scale models from scratch |
| **Data Sources** | Search volume APIs, community forums, existing Axentx product list | Proprietary third‑party data not in public domain |
| **User Interface** | Minimal web UI + API endpoints | Native mobile apps |
| **Deployment** | Dockerized microservice on AWS ECS + RDS (pgVector) | On‑prem or hybrid deployments |
| **Security** | OAuth2, token‑based sharing, GDPR compliance | Enterprise SSO integration |
| **Analytics** | Basic usage dashboards | Advanced BI integration (e.g., Looker) |

---

## 8. Dependencies  

- **Shared BRAIN** – pgVector instance with product portfolio and market signal embeddings.  
- **Inference Engine** – vLLM deployed on GPU cluster.  
- **Data Pipelines** – Weekly ingestion of search volume & forum data.  
- **Auth Service** – OAuth2 provider for user accounts.  

---

## 9. Timeline (High‑Level)  

| Phase | Duration | Milestones |
|-------|----------|------------|
| **Discovery & Design** | 2 weeks | User stories, wireframes, data schema |
| **Core Development** | 6 weeks | Prompt API, validation engine, duplication checker |
| **Beta Release** | 4 weeks | Internal testing, feedback loop |
| **Public Launch** | 2 weeks | Documentation, marketing, onboarding |
| **Post‑Launch Iteration** | Ongoing | Model retraining, feature enhancements |

---

## 10. Risks & Mitigations  

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Model Drift** | Validation accuracy falls | Weekly retraining, monitor drift metrics |
| **Data Privacy** | Sensitive user data exposure | Encrypt at rest, GDPR audit |
| **Duplicate Detection Failure** | Re‑launch of existing product | Strict similarity threshold, manual review |
| **API Rate Limits** | Service slowdown | Implement graceful back‑off, caching |

---

## 11. Acceptance Criteria  

1. **Functional** – All listed features meet acceptance criteria.  
2. **Performance** – End‑to‑end latency ≤ 30 s for 95 % of requests.  
3. **Quality** – Validation accuracy ≥ 0.8 on held‑out test set.  
4. **Compliance** – GDPR & data‑privacy audit passed.  
5. **Documentation** – API docs, user guide, and internal runbook complete.  

---

## 12. Appendix  

- **Data Licenses** – All training data complies with Apache‑2.0, MIT, etc.  
- **Model Card** – Version, training data, evaluation metrics.  
- **Runbook** – Deployment, scaling, and rollback procedures (see `docs/runbook.md`).  

---
