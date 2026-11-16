# Infinite Story – An AI-Powered Fantasy Adventure

Infinite Story is a console-based Python fantasy adventure game. Players explore an AI-generated story by making decisions; the story responds to choices, evaluates decisions, tracks achievements, and produces a personalized ending.

## Worlds
- **Enchanted Forest** — investigate a magical forest mystery and a possible curse.
- **Lost Kingdom** — discover hidden places and forgotten characters in a vanished kingdom.
- **Mystery Island** — investigate the disappearance of the Heart of the Island gemstone.

## How to Play
1. Enter a character name and choose a world.
2. Read the AI-generated opening scene and choose from three options.
3. Continue through six decision rounds. Earlier story events and choices are included as context.
4. Review the final chapter, ending, scorecard, decision history, and achievements.
5. Replay for another adventure.

## Features
- AI-generated opening scenes, choices, and story continuations.
- Three distinct fantasy settings.
- Three choices per decision round.
- Story context carried across rounds.
- AI-based decision evaluation: 0–15 points per round.
- Decision categories: clue, help, strategy, risk, exploration, and other.
- Four ending types: Hero, Secret, Sacrifice, and Mystery.
- Achievement system and final scorecard.
- Replay option.

## Scoring
There are six decision rounds. Each decision can receive up to 15 points, for a maximum score of **90**.

## Achievements
General achievements include Adventure Finisher, Master Explorer, Brave Adventurer, Clue Hunter, Kind Heart, and Fearless Explorer.

Ending-specific achievements:
- Hero — World Savior
- Secret — Truth Seeker
- Sacrifice — Ultimate Guardian
- Mystery — Mystery Keeper

## Project Documentation
- [Detailed project documentation](docs/Project_Documentation.md)
- [Presentation slide content](presentation/Presentation_Slides.md)

## Technology
- Python
- Code in Place AI environment
- `from ai import call_gpt` for AI-powered story generation and decision evaluation

## Running the Project
Run the game in the supported Code in Place environment where the `ai` module and `call_gpt` function are available.

```python
from ai import call_gpt
```

**Source-code status:** The repository was empty when inspected. The tested `main.py` source file was not present in the repository or among the available project attachments, so it has not been recreated or uploaded. Add your tested `main.py` before expecting the repository clone to run.

## Responsible AI and Limitations
Story text and decision feedback are AI-generated and may vary between playthroughs. Scores and categories are subjective outputs, not objective measures of a player's ability. The current version is console-based and does not include persistent save/load functionality or a graphical interface.

## Future Improvements
- Save and resume adventures.
- Add more worlds, characters, and endings.
- Add a graphical interface and sound effects.
- Add configurable difficulty and richer inventory mechanics.
