from ai import call_gpt
import re
import json


# ==================================================
# 1. WELCOME SCREEN
# ==================================================

def welcome():

    print("=" * 55)
    print("                 INFINITE STORY")
    print("          Your Choices, Your Adventure")
    print("=" * 55)

    print("\nWelcome, adventurer!")
    print("Every choice changes your destiny.")
    print("Your story is powered by AI!\n")


# ==================================================
# 2. CHARACTER SELECTION
# ==================================================

def choose_character():

    while True:

        name = input("Enter your character name: ").strip()

        if name:
            return name

        print("Please enter a valid name!")


# ==================================================
# 3. WORLD SELECTION
# ==================================================

def choose_world():

    print("\nChoose your adventure world:")
    print("1. Enchanted Forest")
    print("2. Lost Kingdom")
    print("3. Mystery Island")

    worlds = {
        "1": "Enchanted Forest",
        "2": "Lost Kingdom",
        "3": "Mystery Island"
    }

    while True:

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice in worlds:
            return worlds[choice]

        print("Invalid choice! Please select 1, 2, or 3.")


# ==================================================
# 4. AI-GENERATED OPENING SCENE
# ==================================================

def generate_opening_scene(player, world):

    prompt = f"""
    Create an exciting fantasy mystery adventure.

    Character: {player}
    World: {world}

    Write an immersive opening scene of around 100 words.

    Introduce an interesting mystery and a problem.

    End with exactly 3 numbered choices.

    Format:
    1. First choice
    2. Second choice
    3. Third choice

    Each choice should lead to a different direction.

    Keep the story age-appropriate and non-graphic.
    """

    return call_gpt(prompt)


# ==================================================
# 5. EXTRACT SELECTED CHOICE
# ==================================================

def extract_choice_text(story, choice_number):

    """Extract the actual text of a numbered choice."""

    for line in str(story).splitlines():

        match = re.match(
            r"^\s*" + str(choice_number) + r"[\.\)]\s*(.+)",
            line
        )

        if match:
            return match.group(1).strip()

    return "Option " + str(choice_number)


# ==================================================
# 6. AI-GENERATED NEXT SCENE
# ==================================================

def generate_next_scene(player, world, memory, choice_text):

    prompt = f"""
    Continue this interactive fantasy mystery adventure.

    Character: {player}
    World: {world}

    Previous story and decisions:
    {memory}

    The player's actual decision was:
    {choice_text}

    Continue the story according to this decision.

    Remember previous events and maintain consistency.

    Show the consequences of the player's decision.

    Write around 100 words.

    Introduce a new event, clue, or mystery.

    End with exactly 3 numbered choices.

    Format:
    1. First choice
    2. Second choice
    3. Third choice

    Keep the story age-appropriate and non-graphic.
    """

    return call_gpt(prompt)


# ==================================================
# 7. PLAYER CHOICE INPUT
# ==================================================

def get_player_choice():

    while True:

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice in ["1", "2", "3"]:
            return choice

        print("Invalid choice! Please enter 1, 2, or 3.")


# ==================================================
# 8. SMART AI DECISION EVALUATION
# ==================================================

def evaluate_decision(player, world, scene, choice_text, memory):

    """
    Evaluate the player's decision using AI.

    Maximum points per decision = 15.
    Six decisions = 90 maximum points.
    """

    prompt = f"""
    You are an intelligent decision evaluator
    for an AI-powered fantasy adventure game.

    PLAYER: {player}
    WORLD: {world}

    PREVIOUS STORY:
    {memory}

    CURRENT SCENE:
    {scene}

    PLAYER'S SELECTED DECISION:
    {choice_text}

    Evaluate the decision based on its actual value
    in the context of the adventure.

    IMPORTANT RULES:

    1. There are no universally correct or wrong choices.
    2. Different decisions can lead to different outcomes.
    3. Consider exploration, creativity, helpfulness,
       strategic thinking and possible consequences.
    4. Do not award points just because a decision
       sounds brave or helpful.
    5. A careful retreat can be a smart strategy.
    6. A risky decision can sometimes be valuable.
    7. Give different scores to decisions with
       meaningfully different value.
    8. Evaluate the actual selected decision,
       not an imaginary decision.

    SCORING SYSTEM:

    0-3 POINTS:
    Very weak decision with little useful progress.

    4-6 POINTS:
    Limited value, but provides some exploration
    or useful information.

    7-9 POINTS:
    Reasonable decision with moderate usefulness.

    10-12 POINTS:
    Good decision that meaningfully helps the adventure.

    13-15 POINTS:
    Excellent decision that discovers an important clue,
    solves a problem or uses outstanding strategy.

    SELECT EXACTLY ONE CATEGORY:

    clue
    help
    strategy
    risk
    exploration
    other

    CATEGORY GUIDELINES:

    clue: Discovering clues or hidden information.
    help: Helping characters or protecting others.
    strategy: Planning or solving problems intelligently.
    risk: Taking a dangerous or uncertain action.
    exploration: Discovering new places or secrets.
    other: Decisions that do not fit other categories.

    Return ONLY valid JSON in this format:

    {{
        "points": 13,
        "category": "clue",
        "reason": "You discovered an important clue that may reveal the mystery."
    }}

    Points must be an integer from 0 to 15.

    Give a short and specific reason for your score.
    Avoid giving the same score to every decision.
    """

    response = call_gpt(prompt)

    try:

        match = re.search(
            r"\{.*\}",
            str(response),
            re.DOTALL
        )

        if match:

            result = json.loads(match.group())

            points = int(result.get("points", 5))

            # Keep points between 0 and 15.
            points = max(0, min(15, points))

            category = str(
                result.get("category", "other")
            ).lower().strip()

            valid_categories = [
                "clue",
                "help",
                "strategy",
                "risk",
                "exploration",
                "other"
            ]

            if category not in valid_categories:
                category = "other"

            reason = str(
                result.get(
                    "reason",
                    "Your decision was evaluated."
                )
            )

            return {
                "points": points,
                "category": category,
                "reason": reason
            }

    except (ValueError, TypeError, json.JSONDecodeError):
        pass

    # Fallback if AI returns invalid JSON.

    return {
        "points": 5,
        "category": "other",
        "reason": "A basic score was awarded because the AI response could not be evaluated."
    }


# ==================================================
# 9. AI-GENERATED FINAL ENDING
# ==================================================

def generate_ending(player, world, memory, score):

    prompt = f"""
    You are the storyteller of an interactive fantasy
    mystery adventure.

    Character: {player}
    World: {world}

    Player's final score: {score}/90

    Complete adventure history:
    {memory}

    Analyze the player's actual decisions,
    discoveries, actions and story consequences.

    Choose the most suitable ending:

    1. HERO ENDING:
       The player saves the world.

    2. SECRET ENDING:
       The player discovers a hidden truth.

    3. SACRIFICE ENDING:
       The player makes a difficult sacrifice.

    4. MYSTERY ENDING:
       The mystery remains partly unsolved.

    Choose only one ending that fits the adventure.

    The ending must depend mainly on the story decisions,
    not simply on the player's score.

    Output format:

    ENDING TYPE: [Ending name]

    FINAL CHAPTER:

    Write a satisfying conclusion of around 150-200 words.

    Mention the consequences of the player's decisions.

    Keep the story age-appropriate and non-graphic.
    """

    return call_gpt(prompt)


# ==================================================
# 10. EXTRACT ENDING TYPE
# ==================================================

def extract_ending_type(ending):

    """Identify the ending selected by the AI."""

    text = str(ending).upper()

    match = re.search(
        r"ENDING TYPE\s*:\s*(HERO|SECRET|SACRIFICE|MYSTERY)",
        text
    )

    if match:
        return match.group(1)

    return "UNKNOWN"


# ==================================================
# 11. ACHIEVEMENT SYSTEM
# ==================================================

def calculate_achievements(
    score,
    choices,
    decision_results,
    ending_type
):

    achievements = []

    # Complete all six decisions.
    if len(choices) == 6:
        achievements.append("Adventure Finisher")

    # Select all three option numbers.
    if len(set(choices)) == 3:
        achievements.append("Master Explorer")

    # Score at least 60 points.
    if score >= 60:
        achievements.append("Brave Adventurer")

    # Discover at least two clues.
    clue_count = sum(
        1 for result in decision_results
        if result["category"] == "clue"
    )

    if clue_count >= 2:
        achievements.append("Clue Hunter")

    # Help at least two characters.
    help_count = sum(
        1 for result in decision_results
        if result["category"] == "help"
    )

    if help_count >= 2:
        achievements.append("Kind Heart")

    # Explore at least two times.
    exploration_count = sum(
        1 for result in decision_results
        if result["category"] == "exploration"
    )

    if exploration_count >= 2:
        achievements.append("Fearless Explorer")

    # Special ending-based achievements.
    ending_achievements = {
        "HERO": "World Savior",
        "SECRET": "Truth Seeker",
        "SACRIFICE": "Ultimate Guardian",
        "MYSTERY": "Mystery Keeper"
    }

    special_achievement = ending_achievements.get(ending_type)

    if special_achievement:
        achievements.append(special_achievement)

    if not achievements:
        achievements.append("New Adventurer")

    return achievements


# ==================================================
# 12. FINAL SCORECARD
# ==================================================

def show_scorecard(
    player,
    score,
    choices,
    achievements,
    decision_results,
    ending_type
):

    print("\n" + "=" * 55)
    print("              YOUR ADVENTURE SCORECARD")
    print("=" * 55)

    print("\nPlayer:", player)
    print("Total Score:", score, "/ 90")
    print("Decisions Made:", len(choices), "/ 6")

    print("Final Ending:", ending_type.title())

    print("\nYOUR DECISION BREAKDOWN:")

    for i, result in enumerate(decision_results, start=1):

        print("\nRound", i)

        print("Selected Option:", choices[i - 1])
        print("Points:", result["points"], "/ 15")
        print("Category:", result["category"].title())
        print("AI Feedback:", result["reason"])

    print("\nYOUR ACHIEVEMENTS:")

    for achievement in achievements:
        print("*", achievement)

    print("\n" + "=" * 55)


# ==================================================
# 13. MAIN ADVENTURE FUNCTION
# ==================================================

def play_adventure(player, world):

    score = 0

    choices = []

    story_memory = []

    decision_results = []

    print("\nGenerating your unique adventure...")

    story = generate_opening_scene(player, world)

    print("\n" + "=" * 55)
    print("             YOUR AI-GENERATED ADVENTURE")
    print("=" * 55)

    print("\n" + str(story))

    story_memory.append(
        "Opening Scene:\n" + str(story)
    )

    # Six decision rounds.
    for round_number in range(1, 7):

        print("\n--- Adventure Round", round_number, "---")

        choice = get_player_choice()

        # Extract the actual selected choice.
        choice_text = extract_choice_text(story, choice)

        choices.append(choice)

        # Previous story history.
        previous_memory = "\n".join(story_memory)

        print("\nAI is evaluating your decision...")

        # Evaluate decision using AI.
        result = evaluate_decision(
            player,
            world,
            story,
            choice_text,
            previous_memory
        )

        decision_results.append(result)

        # Add AI-awarded points.
        score += result["points"]

        # Save decision in story memory.
        story_memory.append(
            "Round " + str(round_number)
            + " decision: " + choice_text
        )

        # Display evaluation.
        print("\n" + "-" * 45)
        print("           DECISION EVALUATION")
        print("-" * 45)

        print("Your Decision:", choice_text)
        print("Points Earned:", result["points"], "/ 15")
        print("Category:", result["category"].title())
        print("AI Feedback:", result["reason"])
        print("Current Score:", score, "/ 90")

        print("-" * 45)

        # Generate next scene except after last round.
        if round_number < 6:

            previous_memory = "\n".join(story_memory)

            print("\nYour decision is shaping the story...")

            story = generate_next_scene(
                player,
                world,
                previous_memory,
                choice_text
            )

            story_memory.append(
                "New Scene:\n" + str(story)
            )

            print("\n" + str(story))

    # ==============================================
    # FINAL CHAPTER
    # ==============================================

    print("\n" + "=" * 55)
    print("                 THE FINAL CHAPTER")
    print("=" * 55)

    print("\nAI is analyzing your decisions...")

    complete_memory = "\n".join(story_memory)

    ending = generate_ending(
        player,
        world,
        complete_memory,
        score
    )

    print("\n" + "=" * 55)
    print("                  YOUR FINAL ENDING")
    print("=" * 55)

    print("\n" + str(ending))

    # Extract ending type.
    ending_type = extract_ending_type(ending)

    # Calculate achievements.
    achievements = calculate_achievements(
        score,
        choices,
        decision_results,
        ending_type
    )

    # Display final scorecard.
    show_scorecard(
        player,
        score,
        choices,
        achievements,
        decision_results,
        ending_type
    )

    print("\nCongratulations, " + player + "!")


# ==================================================
# 14. MAIN PROGRAM
# ==================================================

def main():

    welcome()

    while True:

        player = choose_character()

        world = choose_world()

        print("\nCharacter:", player)
        print("World:", world)

        play_adventure(player, world)

        # Replay option.
        while True:

            again = input(
                "\nWould you like another adventure? (yes/no): "
            ).strip().lower()

            if again in ["yes", "no"]:
                break

            print("Please enter yes or no.")

        if again == "no":

            print("\nThank you for playing INFINITE STORY!")

            print("Until next time, adventurer!")

            break


# ==================================================
# 15. PROGRAM ENTRY POINT
# ==================================================

if __name__ == "__main__":

    main()