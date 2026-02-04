# Tool-Choosing Autonomous Agent

## Overview

This project implements an autonomous agent that intelligently selects
the most suitable free and open-source tool for a given NLP task. The
agent analyzes task constraints, justifies its tool choice before
execution, and executes the task autonomously.

## Features

-   Constraint-based tool selection
-   Transparent decision logging
-   Modular and extensible design
-   Offline and open-source tools only

## How to Run

``` bash
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

## Logs

Decision logs are available in logs/decision_log.json
