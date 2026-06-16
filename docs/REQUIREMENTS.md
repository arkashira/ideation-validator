# REQUIREMENTS.md

## Project Overview
**Project Name:** `ideation-validator`  
**Repository:** `arkashira/ideation-validator`  
**Purpose:** An AI‑powered ideation tool that assists indie hackers and creators in generating, validating, and prioritizing software tool ideas. The tool leverages the Axentx shared knowledge base (pgvector) and production‑grade inference engines (e.g., vLLM) to provide rapid, data‑driven idea validation.

---

## 1. Functional Requirements

| ID | Description | Priority | Acceptance Criteria |
|----|-------------|----------|---------------------|
| **FR‑1** | **Idea Generation** | Must | • Accept a natural‑language prompt (e.g., “Generate 5 software tool ideas for remote teams”). <br>• Return a list of 3–10 distinct, actionable ideas with a brief description. <br>• Each idea must include a unique value proposition and target audience. |
| **FR‑2** | **Idea Validation** | Must | • For each generated idea, compute a *validation score* (0–100) based on market signals, pain‑point data, and willingness‑to‑pay indicators from the shared BRAIN. <br>• Provide a confidence interval for the score. |
| **FR‑3** | **Prioritization** | Should | • Rank ideas by validation score, weighted by user‑specified criteria (e.g., revenue potential, technical feasibility). <br>• Allow users to adjust weights via a simple UI or API. |
| **FR‑4** | **Data Source Integration** | Must | • Pull real‑time market data from the Axentx data lake (auto, instr‑resp, messages, system‑user‑assistant). <br>• Cache results for 24 h to reduce inference load. |
| **FR‑5** | **API Exposure** | Must | • Expose a RESTful API (`/generate`, `/validate`, `/rank`) with JSON payloads. <br>• Support OAuth2 authentication. |
| **FR‑6** | **Web UI** | Should | • Provide a minimal web interface for prompt entry, result display, and weight adjustment. <br>• Responsive design for mobile and desktop. |
| **FR‑7** | **Audit Trail** | Should | • Log every request, response, and validation score to a PostgreSQL audit table. <br>• Include timestamps, user ID, and IP address. |
| **FR‑8** | **Rate Limiting** | Should | • Enforce 60 requests/min per authenticated user. |
| **FR‑9** | **Error Handling** | Must | • Return clear, actionable error messages (e.g., “Insufficient data for validation”). <br>• Log internal errors to Sentry. |
| **FR‑10** | **Extensibility** | Should | • Allow addition of new validation metrics via a plugin system. |

---

## 2. Non‑Functional Requirements

| Category | Requirement | Details |
|----------|-------------|---------|
| **Performance** | Response Time | < 2 s for API calls, < 5 s for UI rendering. |
| **Scalability** | Horizontal Scaling | Stateless API servers behind a load balancer; inference engine (vLLM) autoscaled via Kubernetes. |
| **Reliability** | Uptime | 99.9 % SLA; automated health checks and self‑healing. |
| **Security** | Data Protection | All data in transit encrypted (TLS 1.3). Sensitive fields masked in logs. |
| **Compliance** | GDPR / CCPA | User data stored with consent; ability to delete user data on request. |
| **Maintainability** | Code Quality | 90 % unit‑test coverage; linting (ESLint, Flake8). |
| **Observability** | Metrics | Prometheus metrics for request latency, error rates, cache hit ratio. |
| **Documentation** | API Docs | Auto‑generated OpenAPI spec; interactive Swagger UI. |

---

## 3. Constraints

1. **Inference Engine** – Must use the production‑grade `vLLM` model hosted in the Axentx cluster; no external LLM APIs allowed.  
2. **Data Licensing** – Only use datasets with Apache‑2.0, MIT, or CC‑BY‑4.0 licenses; no proprietary data.  
3. **Deployment** – Must run on the existing Axentx Kubernetes cluster; use Helm charts for deployment.  
4. **Budget** – No external cloud services beyond the shared Axentx infrastructure.  
5. **Time to Market** – MVP to be shipped within 8 weeks from acceptance of this spec.

---

## 4. Assumptions

- Users have an existing Axentx account and OAuth2 token.  
- The shared BRAIN (pgvector) contains up‑to‑date market signals for all target domains.  
- The inference engine can handle up to 200 concurrent requests per node.  
- The UI will be built with React and Tailwind CSS (existing company stack).  
- All regulatory requirements (GDPR, CCPA) are satisfied by the shared infrastructure.

---

## 5. Acceptance Checklist

- [ ] API endpoints `/generate`, `/validate`, `/rank` implemented and documented.  
- [ ] Web UI functional on both mobile and desktop.  
- [ ] Validation scores match benchmark data (≥ 80 % correlation with historical validated ideas).  
- [ ] Rate limiting and audit logging operational.  
- [ ] End‑to‑end tests covering 90 % of code paths.  
- [ ] Deployment Helm chart passes CI pipeline.  
- [ ] Security audit completed with no critical findings.  

---

## 6. Future Enhancements (Post‑MVP)

- **Idea Collaboration** – Real‑time multi‑user editing of idea lists.  
- **Export Formats** – CSV, PDF, and integration with project management tools.  
- **AI‑Driven Feedback Loop** – Continuous learning from user feedback to improve validation models.  

---
