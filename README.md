<h1 align="center">Personal Expenses Tracker</h1>

<p align="center">
  A command-line expense tracker built with Python.<br>
  Log what you spend, browse it paginated, filter by category, and check a monthly summary.<br>
  Everything persists to a JSON file — no database, no dependencies.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.6%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python 3.6+">
  <img src="https://img.shields.io/badge/Dependencies-None-brightgreen?style=flat-square" alt="No dependencies">
  <img src="https://img.shields.io/badge/Storage-JSON-lightgrey?style=flat-square" alt="JSON storage">
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=flat-square" alt="MIT License">
</p>

<p align="center">
  <a href="#demo">Demo</a> ·
  <a href="#features">Features</a> ·
  <a href="#getting-started">Getting Started</a> ·
  <a href="#what-i-learned">What I Learned</a> ·
  <a href="#contact">Contact</a>
</p>

## Demo

<p align="center">
  <img width="565" alt="Expenses Tracker sample output" src="https://github.com/user-attachments/assets/28209df3-a0f3-4178-ad6f-44e4794aef84">
</p>

<p align="center">
  <em>Adding an expense, browsing the paginated list, and viewing the monthly summary.</em>
</p>

## Features

<table>
  <tr>
    <td width="50%" valign="top">

**Managing expenses**

- Add an expense with amount, category, description, and date
- Browse expenses in pages of 10
- Filter by category
- Delete an expense by ID

</td>
    <td width="50%" valign="top">

**Summaries**

- Total spending broken down by category
- Monthly snapshot for any month
- All data saved to a JSON file between sessions

</td>
  </tr>
</table>

## Tech Stack

| | |
|---|---|
| **Language** | ![Python](https://img.shields.io/badge/-Python%203.6%2B-3776AB?style=flat-square&logo=python&logoColor=white) |
| **Storage** | ![JSON](https://img.shields.io/badge/-JSON-000000?style=flat-square&logo=json&logoColor=white) |
| **Dependencies** | None — standard library only |

## Getting Started

**Prerequisites:** Python 3.6 or higher.

```bash
git clone https://github.com/SalmonFlight/Personal-Expenses-Tracker.git
cd Personal-Expenses-Tracker
python main.py
```

Follow the on-screen menu. Your expenses are saved to a JSON file automatically.

## What I Learned

| Area | Details |
|---|---|
| **File I/O** | Reading and writing JSON with the standard library, and handling the case where the file doesn't exist yet. |
| **Input validation** | Dates, amounts, and menu choices all need to be parsed and checked. Bad input shouldn't crash the program. |
| **Pagination** | Slicing a list into pages and walking through them without losing track of where you are. |
| **Data grouping** | Summarising a list of expenses by category and by month — the first time I used dictionaries as a grouping tool. |
| **Menu-driven design** | Keeping a program running until the user chooses to exit, and dispatching to the right function for each choice. |

### Takeaway

> **Functions first, then features.** Splitting the program into one function per action made it possible to build and test one thing at a time. When I hit a bug in the monthly summary, I knew exactly where to look.

## Future Improvements

- [ ] Edit an existing expense
- [ ] Export to CSV
- [ ] Monthly budget limits with warnings
- [ ] Charts for spending by category
- [ ] GUI version (wxPython or PyQt6)

This is a personal project, but feedback and suggestions are welcome.

## Contact

I'm actively looking for SWE roles.

<p>
  <a href="https://github.com/SalmonFlight"><img src="https://img.shields.io/badge/GitHub-SalmonFlight-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub"></a>
  <a href="https://www.linkedin.com/in/brayden-aaron-santoso/"><img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square" alt="LinkedIn"></a>
  <a href="mailto:B.AaronSantoso@gmail.com"><img src="https://img.shields.io/badge/Email-B.AaronSantoso%40gmail.com-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email: B.AaronSantoso@gmail.com"></a>
</p>

---

## License

MIT
