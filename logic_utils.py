#FIX: Refactored logic into logic_utils.py using Copilot Agent mode

def get_range_for_difficulty(difficulty: str):
    """Return the inclusive low/high range for a given difficulty level.

    This mirrors the mapping originally hard‑coded in the Streamlit UI so that
    both the frontend and the tests rely on the same source of truth.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50
    # fallback default
    return 1, 100


def parse_guess(raw: str):
    """
    Convert a raw text input into an integer guess.

    Returns a tuple (ok, guess_int, error_message) much like Streamlit's
    validation helpers. Empty inputs or non‑numeric values are rejected.
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        # allow floats by casting through float first
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare the numeric *guess* to *secret* and return
    ``(outcome, message)``.

    The UI sometimes passes the secret as a string (an intentional game
    glitch), so we coerce it to an integer if possible.  The outcome strings
    exactly match those used in the app.
    """
    try:
        secret_value = int(secret)
    except Exception:
        # fall back to whatever was passed; comparisons may raise
        secret_value = secret

    if guess == secret_value:
        return "Win", "🎉 Correct!"
    
    #FIX: Used Claude AI to figure out how to debug progress to find a problem in guess check functionality
    if guess < secret_value:
        return "Too Low", "📈 Go HIGHER!"
    return "Too High", "📉 Go LOWER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Calculate new score given the outcome of a guess attempt.

    This replicates the scoring logic that was previously embedded in the
    Streamlit script so it can be tested independently.
    """
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
