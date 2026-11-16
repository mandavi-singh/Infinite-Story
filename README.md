# Infinite Story – An AI-Powered Fantasy Adventure

Infinite Story is a console-based Python fantasy adventure game in which players explore an AI-generated story by making decisions. The story responds to player choices, evaluates decisions, tracks achievements, and produces a personalized ending.

## Worlds
- **Enchanted Forest** – Explore a magical forest and uncover the mystery behind its curse.
- **Lost Kingdom** – Discover hidden places and forgotten characters in a vanished kingdom.
- **Mystery Island** – Investigate the disappearance of the island's Heart gemstone.

## How to Play
1. Enter your character name.
2. Choose one of the three fantasy worlds.
3. Read the AI-generated opening scene and choose from three options.
4. Continue through six decision rounds. The story remembers earlier events and reacts to your choices.
5. Review your final scorecard, ending, decision history, and achievements.
6. Replay for another adventure.

## Features
- AI-generated opening scenes and story continuations.
- Three distinct fantasy settings.
- Three choices per decision round.
- Story context carried across rounds.
- AI-based decision evaluation, scored from 0 to 15.
- Decision categories: clue, help, strategy, risk, exploration, and other.
- Four possible ending types: Hero, Secret, Sacrifice, and Mystery.
- Achievement system and final scorecard.
- Replay option.

## Scoring
There are six decision rounds. Each decision can receive up to 15 points, for a maximum score of **90**.

## Achievements
- Adventure Finisher
- Master Explorer
- Brave Adventurer
- Clue Hunter
- Kind Heart
- Fearless Explorer

Ending-specific achievements:
- Hero – World Savior
- Secret – Truth Seeker
- Sacrifice – Ultimate Guardian
- Mystery – Mystery Keeper

## Technology
- Python
- Code in Place AI environment
- `ai.call_gpt` for AI-powered story generation and decision evaluation

## Running the Project
Run the project in the supported Code in Place environment where the `ai` module and `call_gpt` function are available.

```python
from ai import call_gpt
```

The project depends on this supported AI environment; it is not a standalone offline Python application without adapting the AI integration.

## Responsible AI and Limitations
Story text and decision feedback are AI-generated and may vary between playthroughs. Scores and categories are subjective outputs, not objective measures of a player's ability. The current version is console-based and does not include persistent save/load functionality.

## Future Improvements
- Save and resume adventures.
- Add more worlds, characters, and endings.
- Add a graphical interface and sound effects.
- Add configurable difficulty and richer inventory mechanics.

## Project Structure
```
Infinite-Story/
├── main.py
├── README.md
├── docs/
│   └── Project_Documentation.docx
└── presentation/
    └── Infinite_Story_Presentation.pptx
```

> Note: The documentation and presentation files are included alongside this README. The `main.py` shown above is the intended project entry point; add your tested source file when ready.
