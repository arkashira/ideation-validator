# ROADMAP.md

## Overview
An AI-powered ideation tool for indie hackers and creators to generate and validate software tool ideas. The tool leverages Axentx's shared BRAIN (pgvector) and market data to provide actionable insights, ensuring ideas solve validated paying needs without duplicating existing portfolio.

## MVP Milestone (Launch)
The Minimum Viable Product will focus on core ideation and basic validation, enabling users to input pain points or keywords and receive a list of validated software ideas with market potential.

### MVP Critical Features
- **Idea Generation Engine**: Uses SGLang for structured generation of software ideas based on user-provided inputs (e.g., target audience, pain points, technical constraints).
- **Basic Validation**: Checks against Axentx's product portfolio and open-source projects (verified via GitHub URLs) to avoid duplication, and uses market signals from datasets (e.g., `instr-resp`, `messages`) to assess real pain and willingness-to-pay.
- **User Input Interface**: A web-based interface where users can specify domain, user personas, and problem statements to generate ideas.

## Phase 1: Enhanced Validation & Portfolio Alignment (v1)
### Themes: Deep Validation & Strategic Alignment
- **Advanced Validation**: Integrate with Axentx's BRAIN to access live market data and user feedback, providing quantitative validation scores (e.g., market size, competition level, revenue potential).
- **Portfolio Avoidance**: Enhance duplication checks by cross-referencing with Axentx's existing product catalog and GitHub repositories (e.g., `iceoryx2` as a reference for IPC libraries).
- **Data Visualization**: Add interactive charts to visualize validation metrics (e.g., user demand trends, revenue forecasts, technical feasibility).

## Phase
