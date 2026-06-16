# STORIES.md – ideation‑validator

## Overview
**Product**: ideation‑validator – an AI‑powered ideation tool for indie hackers and creators.  
**Goal**: Help users generate, refine, and validate software tool ideas quickly, ensuring they target a real, paying market before building.

---

## Epics & Story Backlog

| Epic | Story | Acceptance Criteria |
|------|-------|---------------------|
| **Idea Generation** | **E1‑S1** As a creator, I want to generate a list of 10 software tool ideas based on a single keyword, so that I can quickly explore possibilities. | • Input: single keyword (e.g., “budget”).<br>• Output: 10 distinct idea titles + 1‑sentence description each.<br>• Ideas must be unique and not duplicate existing portfolio items. |
| | **E1‑S2** As a creator, I want to filter generated ideas by industry, so that I can focus on my niche. | • Filter UI: industry dropdown.<br>• Result set updates in real time.<br>• No cross‑industry overlap in filtered results. |
| | **E1‑S3** As a creator, I want to rank ideas by potential market size, so that I can prioritize high‑impact concepts. | • Ranking algorithm uses public market data (e.g., TAM).<br>• Ranking displayed numerically (1‑10).<br>• Ranking is reproducible given same input. |
| **Idea Refinement** | **E2‑S1** As a creator, I want to expand an idea into a detailed PRD outline, so that I can plan development. | • PRD outline includes: problem, solution, target users, key features, MVP scope.<br>• Outline auto‑generated from selected idea. |
| | **E2‑S2** As a creator, I want to edit the PRD outline, so that I can tailor it to my vision. | • Inline editing with real‑time AI suggestions.<br>• Version history saved. |
| | **E2‑S3** As a creator, I want to generate a one‑page pitch deck from the PRD, so that I can pitch investors. | • Pitch deck includes: problem, solution, market, business model, traction, ask.<br>• Exportable to PDF. |
| **Validation** | **E3‑S1** As a creator, I want to run a quick market survey, so that I can gauge interest. | • Survey builder auto‑populates questions based on idea.<br>• Survey sent to 100 target users via email/Social.<br>• Response rate ≥ 20% triggers validation flag. |
| | **E3‑S2** As a creator, I want to analyze survey results, so that I can decide whether to proceed. | • Dashboard shows sentiment, interest score, willingness‑to‑pay.<br>• Thresholds configurable. |
| | **E3‑S3** As a creator, I want to see a “validation score” for each idea, so that I can compare ideas quickly. | • Score 0‑100 based on market size, survey interest, and TAM.<br>• Visual badge (green/yellow/red). |
| **User Management** | **E4‑S1** As a user, I want to sign up with email, so that I can access the tool. | • Email verification flow.<br>• Password strength enforcement. |
| | **E4‑S2** As a user, I want to connect my GitHub account, so that I can import my existing projects. | • OAuth flow.<br>• List of repos displayed. |
| | **E4‑S3** As a user, I want to delete my account, so that I can maintain privacy. | • Confirmation dialog.<br>• All data purged after 48h. |
| **Analytics & Reporting** | **E5‑S1** As a product owner, I want to see aggregate idea generation metrics, so that I can improve the AI model. | • Dashboard: ideas generated per day, average validation score, top industries.<br>• Export CSV. |
| | **E5‑S2** As a user, I want to export my idea list to CSV, so that I can share it offline. | • Export button available on idea list page.<br>• CSV contains title, description, validation score. |
| **Monetization** | **E6‑S1** As a creator, I want to upgrade to a paid plan, so that I get advanced analytics. | • Upgrade flow with Stripe integration.<br>• Paid features gated behind auth. |
| | **E6‑S2** As a creator, I want to see my plan status, so that I know my limits. | • Dashboard shows plan, usage, next billing date. |

---

## MVP Order (Sprint 1‑3)

1. **Sprint 1** – Idea Generation (E1‑S1, E1‑S2, E1‑S3)  
2. **Sprint 2** – Idea Refinement (E2‑S1, E2‑S2, E2‑S3)  
3. **Sprint 3** – Validation & User Management (E3‑S1, E3‑S2, E3‑S3, E4‑S1, E4‑S2, E4‑S3)  

Subsequent sprints will add Analytics, Reporting, and Monetization.

---

## Acceptance Test Checklist

| Feature | Test | Pass Criteria |
|---------|------|---------------|
| Idea Generation | Generate ideas for “budget” | 10 unique ideas returned |
| Filter by industry | Filter “finance” | Only finance ideas shown |
| Ranking | Verify ranking order | Higher TAM = lower rank number |
| PRD Outline | Generate from idea | All sections present |
| Edit PRD | Modify description | Changes saved, version history updated |
| Pitch Deck | Export PDF | PDF contains all sections |
| Survey | Send to 100 users | ≥20 responses received |
| Validation Score | View badge | Score displayed, color matches threshold |
| Sign‑up | Register email | Verification email sent, account created |
| GitHub connect | OAuth flow | Repo list displayed |
| Delete account | Confirm deletion | Data purged after 48h |
| Analytics | View dashboard | Metrics displayed, CSV export works |
| Upgrade | Stripe checkout | Payment processed, plan updated |
| Plan status | View dashboard | Correct plan and usage shown |

---

## Dependencies & Constraints

- **AI Model**: Uses vLLM for inference; must be integrated with existing `arkashira/surrogate-1-harvest` repo.  
- **Data**: Must not duplicate existing portfolio items (e.g., iceoryx2).  
- **Compliance**: All user data handled per GDPR; surveys anonymized.  
- **Performance**: Idea generation ≤ 5 s per request.  

---

## Notes for Engineering

- **Front‑end**: React + TypeScript, Material‑UI.  
- **Back‑end**: FastAPI, PostgreSQL, Redis for caching.  
- **AI Service**: Wrap vLLM inference in a microservice; expose `/generate-ideas`, `/expand-idea`.  
- **Survey**: Use Typeform API; store responses in Postgres.  
- **Payments**: Stripe Checkout, webhooks for subscription events.  

---

*End of STORIES.md*
