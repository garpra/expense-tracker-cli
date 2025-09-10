# Expense Tracker CLI

A simple CLI tool to keep a track of your daily expenses from terminal itself. Build and run around the concept of providing as little friction, speed and utility for day to day operations without the entity of GUI apps.

## Tech Stack

| Technology | Purpose                       |
| ---------- | ----------------------------- |
| Python     | Main programming language     |
| SQLite     | File-based DB                 |
| Typer      | Modern CLI framework          |
| Rich       | Terminal formatting & styling |

## Key Features

- Quickly add expenses
- Categorize transactions
- View expense history
- Persistent local storage with SQLite

## Getting Started

### Prerequisites

Make sure you have installed:

- Python 3.10 or newer
- pip

### Installation

**1. Clone repository**

```bash
git clone https://github.com/username/expense-tracker-cli.git
cd expense-tracker-cli
```

**2. Create virtual environment (recommended)**

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
# or
.venv\Scripts\activate     # Windows
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

## Usage

### Add expense

```bash
python main.py add
```

### List all expenses

```bash
python main.py list
```

### Summary all expense

```bash
python main.py summary
```
