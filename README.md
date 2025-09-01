# 21 Python Projects 🐍

This repository is a collection of 21 beginner-to-intermediate Python projects, covering games, utilities, and automation scripts. Each project is standalone and demonstrates different aspects of Python programming—from console-based logic games to GUI apps and API integrations.

## Table of Contents
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Running Projects](#running-projects)
- [Key Dependencies](#key-dependencies)
- [Highlights](#highlights)
- [Future Improvements](#future-improvements)
- [License](#license)

## Project Structure
The repository is organized as follows:

```
mrastatine-21_python_proj/
├── req.txt                        # Required dependencies
├── 4_color_match/                 # Mastermind-style color guessing game
├── Aim_trainer/                   # Reflex-based aim trainer using Pygame
├── Alarm_clock/                   # Alarm clock with sound notifications
├── Automated_file_backup/         # Scheduled folder backup utility
├── Backup/                        # Backup destination folder
├── Choose_your_own_adventure/     # Text-based adventure game
├── Currency_converter/            # Currency conversion using an API
├── Madlibs_generator/             # Fill-in-the-blanks story generator
├── NBA_stats/                     # Fetch NBA stats & live scoreboard
├── Number_guesser/                # Random number guessing game
├── Password_generator/            # Random strong password generator
├── Password_Manager/              # Encrypted password manager
├── Path_finder/                   # BFS maze pathfinding visualizer
├── PIG/                           # Dice game "Pig"
├── Quiz_game/                     # Computer basics quiz
├── Rock_paper_scissor/            # Classic rock-paper-scissors game
├── Scripting/                     # File/game compilation automation scripts
├── Slot_machine/                  # Command-line slot machine game
├── Timed_math_challenge/          # Speed math challenge game
├── Turtle_race/                   # Turtle graphics racing game
├── WPM_test/                      # Words-per-minute typing test
└── YT_downloader/                 # YouTube video downloader
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/21-python-projects.git
   cd 21-python-projects
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python -m venv venv
   # On Linux/Mac
   source venv/bin/activate
   # On Windows
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r req.txt
   ```

## Running Projects

Each project is self-contained. Navigate into a project folder and run its script:

```bash
cd Aim_trainer
python train.py
```

**Note:** Some projects (like `Currency_converter`, `NBA_stats`, and `YT_downloader`) require an internet connection or API access.

## Key Dependencies

The following are the main dependencies used across the projects:

- **pygame**: For games and visualization (e.g., Aim Trainer, Turtle Race)
- **cryptography**: For Password Manager encryption
- **requests**: For API requests (e.g., NBA stats, currency conversion)
- **pytube**: For YouTube video downloads
- **schedule**: For automated backups
- **playsound**: For alarm clock sound

*(Full list available in `req.txt`)*

## Highlights

### Games 🎮
- Rock-Paper-Scissors
- Pig Dice Game
- Slot Machine
- Quiz
- Turtle Race
- Typing Test

### Utilities 🛠️
- File Backup
- Password Manager
- Alarm Clock
- YouTube Downloader

### API-based Apps 🌐
- NBA Stats Tracker
- Currency Converter

### Logic/Visuals 🔍
- Maze Pathfinding (BFS)
- Madlibs Generator

## Future Improvements

- Add GUI support for more projects
- Refactor repeated input validation into reusable utilities
- Improve error handling and testing coverage

## License

This project is open-source under the MIT License.
