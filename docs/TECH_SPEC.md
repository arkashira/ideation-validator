# Technical Specification – ideation-validator

## 1. Overview

**Project**: `ideation-validator`  
**Purpose**: An AI‑powered ideation tool that assists indie hackers and creators in generating, refining, and validating software tool ideas.  
**Target Users**: Indie developers, product managers, early‑stage founders.  
**Core Value**: Combines generative AI with a lightweight validation workflow to surface high‑potential ideas that have demonstrated market pain and willingness‑to‑pay.

---

## 2. Architecture Overview

```
┌───────────────────────┐
│  Front‑end (React)    │
│  - Idea input form    │
│  - Idea dashboard     │
│  - Validation status  │
└─────────────┬─────────┘
              │
              ▼
┌───────────────────────┐
│  API Gateway (FastAPI)│
│  - Auth (JWT)         │
│  - Rate limiting      │
│  - Request routing    │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│  Service Layer         │
│  - IdeaService         │
│  - ValidationService   │
│  - FeedbackService     │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│  AI Inference Engine   │
│  - vLLM (LLM)          │
│  - Prompt Templates   │
│  - Post‑processing    │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│  Persistence Layer     │
│  - PostgreSQL (Ideas)  │
│  - Redis (Cache)       │
│  - S3 (Raw logs)       │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│  Monitoring & Ops      │
│  - Prometheus          │
│  - Grafana             │
│  - Loki (Logs)         │
└───────────────────────┘
```

*All services are containerized (Docker) and orchestrated via Kubernetes (EKS/EKS‑like).*

---

## 3. Components

| Component | Responsibility | Key Tech |
|-----------|----------------|----------|
| **Front‑end** | UI/UX, state management | React 18, Vite, Tailwind CSS, Zustand |
| **API Gateway** | Authentication, request routing, rate limiting | FastAPI, Starlette, JWT |
| **IdeaService** | CRUD for ideas, business logic | Python 3.11, SQLAlchemy |
| **ValidationService** | Orchestrates validation pipeline (pain, market size, pricing) | Celery + Redis |
| **FeedbackService** | Collects user feedback, stores metrics | Python, PostgreSQL |
| **AI Inference Engine** | Generates idea descriptions, validates pain, estimates TAM | vLLM (LLM), LangChain |
| **Persistence** | Stores ideas, validation results, user data | PostgreSQL 15, Redis 7 |
| **Monitoring** | Metrics, alerts | Prometheus, Grafana, Loki |
| **CI/CD** | Build, test, deploy | GitHub Actions, Helm, ArgoCD |

---

## 4. Data Model

### 4.1 Core Entities

| Table | Columns | Notes |
|-------|---------|-------|
| **users** | id (PK), email, hashed_password, created_at, updated_at | Auth via JWT |
| **ideas** | id (PK), user_id (FK), title, description, created_at, updated_at | |
| **validations** | id (PK), idea_id (FK), pain_score, market_size, pricing_feasibility, status, created_at | status: pending, in_progress, completed, failed |
| **feedback** | id (PK), idea_id (FK), user_id (FK), rating, comments, created_at | |
| **logs** | id (PK), idea_id (FK), log_type, content, created_at | Stored in S3 for long‑term retention |

### 4.2 Validation Workflow

1. **Pain Score** – LLM generates a score 0‑10 based on user description.  
2. **Market Size** – LLM estimates TAM using public data sources.  
3. **Pricing Feasibility** – LLM suggests price ranges and compares to similar tools.  
4. **Result** – Stored in `validations` table; UI shows pass/fail per metric.

---

## 5. Key APIs / Interfaces

| Endpoint | Method | Description | Request | Response |
|----------|--------|-------------|---------|----------|
| `/api/ideas/` | POST | Create new idea | `{title, description}` | `{id, title, description, created_at}` |
| `/api/ideas/{id}/` | GET | Retrieve idea | N/A | `{id, title, description, validations}` |
| `/api/ideas/{id}/validate` | POST | Trigger validation | N/A | `{validation_id, status}` |
| `/api/validations/{id}/` | GET | Get validation result | N/A | `{pain_score, market_size, pricing_feasibility, status}` |
| `/api/feedback/` | POST | Submit feedback | `{idea_id, rating, comments}` | `{id, status}` |
| `/api/auth/login` | POST | JWT login | `{email, password}` | `{access_token}` |

*All endpoints are versioned (`/api/v1/...`).*

---

## 6. Tech Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **Front‑end** | React 18, Vite, Tailwind | Rapid UI development, low bundle size |
| **API** | FastAPI | Async, automatic docs, high performance |
| **AI** | vLLM (LLM) + LangChain | Production‑grade inference, prompt orchestration |
| **Task Queue** | Celery + Redis | Background validation jobs |
| **Database** | PostgreSQL 15 | ACID, JSONB for flexible fields |
| **Cache** | Redis 7 | Session store, rate limiting |
| **Storage** | S3 (AWS) | Log archival, large payloads |
| **Observability** | Prometheus, Grafana, Loki | Metrics, dashboards, log aggregation |
| **Containerization** | Docker, Helm | Reproducible builds |
| **Orchestration** | Kubernetes (EKS) | Autoscaling, self‑healing |
| **CI/CD** | GitHub Actions, ArgoCD | GitOps workflow |

---

## 7. Dependencies

| Package | Version | Notes |
|---------|---------|-------|
| `fastapi` | ^0.110.0 | API framework |
| `uvicorn` | ^0.29.0 | ASGI server |
| `sqlalchemy` | ^2.0.30 | ORM |
| `psycopg2-binary` | ^2.9.9 | PostgreSQL driver |
| `redis` | ^5.0.0 | Redis client |
| `celery` | ^5.4.0 | Task queue |
| `langchain` | ^0.2.0 | Prompt orchestration |
| `vllm` | ^0.5.0 | LLM inference |
| `pydantic` | ^2.7.0 | Data validation |
| `python-jose` | ^3.3.0 | JWT |
| `passlib` | ^1.7.4 | Password hashing |
| `pytest` | ^8.1.0 | Testing |
| `docker` | - | Container runtime |
| `helm` | - | Kubernetes packaging |

---

## 8. Deployment

### 8.1 CI/CD Pipeline

1. **Build** – Docker image built from `Dockerfile`.  
2. **Test** – Unit tests (`pytest`), lint (`ruff`).  
3. **Push** – Image pushed to ECR.  
4. **Deploy** – Helm chart applied via ArgoCD.  
5. **Post‑deploy** – Run database migrations (`alembic`).  

### 8.2 Kubernetes Resources

| Resource | Purpose |
|----------|---------|
| `Deployment` | API server, worker, frontend |
| `Service` | ClusterIP/LoadBalancer |
| `Ingress` | TLS termination, routing |
| `StatefulSet` | PostgreSQL (high‑availability) |
| `PVC` | Persistent storage for DB |
| `ConfigMap` | Runtime config (env vars) |
| `Secret` | DB credentials, JWT secret |

### 8.3 Scaling Strategy

| Service | Scale | Trigger |
|---------|-------|---------|
| API | Horizontal | CPU > 70% or request latency > 200ms |
| Workers | Horizontal | Validation queue depth > 100 |
| DB | Vertical | CPU > 80% (scale to larger instance) |
| Cache | Horizontal | Memory usage > 80% |

### 8.4 Observability

- **Metrics**: Exported via Prometheus (`/metrics`). Key metrics: request latency, validation success rate, LLM token usage.  
- **Logs**: Structured JSON logs forwarded to Loki.  
- **Alerts**: Slack alerts for high error rates, LLM failures, DB connectivity issues.

---

## 9. Security

- **Auth**: JWT with short‑lived access tokens, refresh tokens stored in secure HTTP‑Only cookies.  
- **Rate Limiting**: Per‑user and per‑IP using Redis.  
- **Secrets**: Managed via AWS Secrets Manager, injected as Kubernetes Secrets.  
- **Data Encryption**: TLS for all traffic, AES‑256 for S3 logs.  
- **Compliance**: GDPR‑friendly design (data deletion on request).

---

## 10. Future Enhancements

1. **Multi‑LLM Support** – Switch between OpenAI, Anthropic, and open‑source models.  
2. **Real‑time Validation** – WebSocket updates for validation progress.  
3. **Marketplace Integration** – Export validated ideas to product marketplaces.  
4. **Advanced Analytics** – Heatmaps of pain scores across domains.

---

## 11. Appendix

### 11.1 Prompt Templates

```text
# Pain Score Prompt
"You are an expert product analyst. Rate the pain level of the following idea on a scale of 0-10: {description}"

# Market Size Prompt
"Estimate the TAM for the following software idea: {title}. Provide a numeric value in USD."

# Pricing Prompt
"Suggest a pricing strategy for the following tool: {title}. Consider competitor pricing and perceived value."
```

### 11.2 Database Schema (DDL)

```sql
CREATE TABLE users (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    email TEXT UNIQUE NOT NULL,
    hashed_password TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE TABLE ideas (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    user_id UUID REFERENCES users(id),
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);

CREATE TABLE validations (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    idea_id UUID REFERENCES ideas(id),
    pain_score INT,
    market_size NUMERIC,
    pricing_feasibility TEXT,
    status TEXT CHECK (status IN ('pending','in_progress','completed','failed')),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT now()
);
```

---
