# multi_agent_automation_system_python
# Multi Agent Automation System (Python)

A multi-agent automation system for content generation, A/B testing, and optimization.

---

# Features

*  Multi-Agent Collaboration
*  Task Queue (Batch 100 tasks)
*  A/B Testing System
*  Viral Content Learning
*  Prompt Optimization

---

# Architecture

```text
Task Queue → Scheduler → Agents → Analysis → Optimization
```

---

# Quick Start

```bash
git clone https://github.com/Ccstyg1100/multi_agent_automation_system_python.git
cd multi_agent_automation_system_python

pip install -r requirements.txt
python main.py
```

---

# Example Output

```text
完成任务: 1
完成任务: 2
新爆款策略！score=95
完成任务: 3
```

---

# Dashboard

```bash
uvicorn dashboard.app:app --reload
```

Open in browser:

http://127.0.0.1:8000

---

# Project Structure

```text
agents/        # AI agents
core/          # scheduler & queue
data/          # storage
dashboard/     # web UI
main.py        # entry point
```

---

# Future Work

* Integrate OpenAI / Claude
* Auto-generate short video scripts
* Connect video generation tools
* Multi-account publishing

---

