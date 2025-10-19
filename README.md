# llm-utils

`llm-utils` is a lightweight collection of helpers and examples for working with large‑language‑model (LLM) based tools and frameworks.  
The repository contains:

- **Agents** – small, reusable LLM‑powered agents that can be dropped into your own projects.
- **Examples** – minimal scripts that showcase how to use the agents.
- **Scripts** – utility scripts for interacting with LLM providers (e.g. `litellm`).

This project is ideal for developers who want a quick start with LLM tools without the overhead of a full‑blown framework.

---

## Getting Started

```bash
# Clone the repository
git clone https://github.com/<your-org>/llm-utils.git
cd llm-utils

# (Optional) Create a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt   # If a requirements file exists
# or
pip install -r examples/requirements.txt   # Example-specific deps
```

---

## Folder Structure

```
llm-utils/
├── agents/            # Reusable LLM agents
│   └── offline-wikipedia/
│       └── AGENTS.md
├── examples/          # Demo scripts
│   └── test.py
├── scripts/           # Helper scripts (e.g., for litellm)
└── README.md          # This file
```

---

## Running the Example

```bash
# From the repo root
python examples/test.py
