# Blog Builder

> AI-powered blog post generator — topic in, blog out.

A tiny Streamlit app that generates blog posts on any topic using DeepSeek's LLM. Pick a topic, a word count, and an audience, and watch the AI write in real time.

---

## How it works

```
┌──────────────┐     ┌─────────────────┐     ┌──────────────┐
│   Streamlit  │────▶│  LangChain      │────▶│  DeepSeek    │
│   Frontend   │     │  + Prompt       │     │  API (V4)    │
│   (app.py)   │◀────│  (llm.py)       │◀────│              │
└──────────────┘     └─────────────────┘     └──────────────┘
     ▲                                             │
     │  topic, words, audience                     │  DEEPSEEK_API_KEY
     │                                             │  (env variable)
     ▼                                             ▼
  ┌──────┐                                   ┌──────────┐
  │ User │                                   │  .env    │
  └──────┘                                   └──────────┘
```

That's it. Three files that matter:

| File | Does |
|------|------|
| `app.py` | Streamlit form — collects topic, word count, and audience |
| `services/llm.py` | Calls DeepSeek via LangChain, streams the response back |
| `prompts/blog_prompt.py` | Prompt template with placeholders for topic, style, and word count |

---

## Prerequisites

- **Python >= 3.14**
- **uv** (recommended) or pip
- A **DeepSeek API key** — [get one here](https://platform.deepseek.com/api_keys)

---

## Setup

```bash
# 1. Clone and enter the project
git clone <repo-url> && cd blog_builder

# 2. Install dependencies
uv sync

# 3. Set your API key as an environment variable
export DEEPSEEK_API_KEY="sk-your-key-here"

```

> **Important:** The API key is read from the `DEEPSEEK_API_KEY` environment variable. Never hardcode it.
---

## Usage

```bash
streamlit run app.py
```

Open `http://localhost:8501`, fill in the form, and hit **Generate**.

```
  ┌─────────────────────────────────┐
  │        Generate Blogs 🤖        │
  │                                 │
  │  Enter the Blog Topic           │
  │  ┌───────────────────────────┐  │
  │  │ Machine Learning in 2026  │  │
  │  └───────────────────────────┘  │
  │                                 │
  │  No of Words    Writing for     │
  │  ┌──────────┐   ┌────────────┐  │
  │  │ 800      │   │ Researchers│  │
  │  └──────────┘   └────────────┘  │
  │                                 │
  │        [ Generate ]             │
  └─────────────────────────────────┘
```

---

## Project structure

```
blog_builder/
├── app.py                  # Streamlit UI
├── main.py                 # CLI placeholder
├── services/
│   └── llm.py              # DeepSeek LLM integration
├── prompts/
│   └── blog_prompt.py      # Prompt template
├── pyproject.toml           # Dependencies & config
└── .env.example             # (you create this) DEEPSEEK_API_KEY=...
```
