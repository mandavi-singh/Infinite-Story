# Infinite Story – An AI-Powered Fantasy Adventure

## 1. Project Summary
Infinite Story is a console-based interactive fantasy and mystery game developed in Python. It uses generative AI to create story scenes, respond to player decisions, evaluate choices, and generate a final ending. The player participates in six decision rounds in one of three fictional worlds.

## 2. Problem and Motivation
Traditional text-based adventures often follow a fixed sequence of events. Infinite Story explores a more flexible experience in which AI-generated scenes respond to the player's decisions. The goal is to make each playthrough feel interactive and story-driven.

## 3. Project Objectives
- Create an interactive story game using Python.
- Offer multiple fantasy worlds.
- Generate story scenes and choices dynamically with AI.
- Maintain story context across decision rounds.
- Provide decision feedback, points, achievements, and multiple ending types.

## 4. Game Worlds
- **Enchanted Forest:** A magical forest mystery involving strange events and a possible curse.
- **Lost Kingdom:** A vanished kingdom with hidden places, forgotten characters, and secrets.
- **Mystery Island:** An island investigation involving the missing Heart of the Island gemstone.

## 5. User Flow
The player enters a character name and chooses a world. The AI generates an opening scene with three choices. The player selects one option in each of six rounds. The program records each decision, evaluates it, and requests a consequence scene from the AI. After round six, the AI generates a final chapter and selects an ending type. The scorecard displays the final score, decision history, feedback, and achievements. The player may replay.

## 6. AI Integration
The project uses the Code in Place AI environment through `from ai import call_gpt`. AI calls are used for three main tasks:
1. Generating story scenes and choices.
2. Evaluating a selected decision and returning points, category, and reason.
3. Generating the final chapter and ending type.

Story history is included in prompts to help preserve continuity.

## 7. Scoring and Achievements
Each decision is evaluated by the AI on a 0–15 point scale. The evaluator considers the decision in the context of the current scene and story, and returns a category such as clue, help, strategy, risk, exploration, or other, along with a short reason. The program totals the points across six rounds, giving a maximum possible score of 90.

Achievements include Adventure Finisher, Master Explorer, Brave Adventurer, Clue Hunter, Kind Heart, Fearless Explorer, and an ending-specific achievement such as World Savior, Truth Seeker, Ultimate Guardian, or Mystery Keeper.

## 8. Ending Types
The final chapter uses one of four ending types: Hero Ending, Secret Ending, Sacrifice Ending, or Mystery Ending. The AI is prompted to base the ending on the story and decisions rather than score alone.

## 9. Technologies Used
- Python
- Code in Place AI environment
- `call_gpt` for generative AI interaction

## 10. Responsible AI and Limitations
The project is intended for age-appropriate fantasy and mystery storytelling and does not require sensitive personal data. AI-generated feedback is subjective and may occasionally misinterpret a choice. The current game is console-based and does not include persistent save/load functionality or a graphical interface.

## 11. Future Scope
Potential improvements include a graphical user interface, saving and loading adventures, inventory and character attributes, richer branching storylines, additional worlds, and more consistent decision evaluation.

## 12. Demonstration Plan
1. Introduce the project and its purpose.
2. Show character entry and world selection.
3. Play through a few decisions and explain how the AI uses story history.
4. Complete the adventure to show the final ending and scorecard.
5. Conclude with the technologies, responsible AI considerations, limitations, and future improvements.

**Project language:** Python  
**AI integration:** Code in Place `call_gpt`
