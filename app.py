import random
import streamlit as st
# FIX: Added import for refactored game logic functions from logic_utils.py using Copilot Agent mode
from logic_utils import get_range_for_difficulty, parse_guess, check_guess, update_score


def update_score(current_score: int, outcome: str, attempt_number: int):
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

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(page_title="Glitchy Guesser", page_icon="🎮")

# ── Custom CSS: color-coded hint palette ───────────────────────────────────────
st.markdown("""
<style>
    .hint-box {
        padding: 14px 18px;
        border-radius: 10px;
        font-size: 1.1rem;
        font-weight: 600;
        margin: 10px 0;
    }
    .scorching { background-color: #7f1d1d; color: #fca5a5; border-left: 5px solid #ef4444; }
    .hot       { background-color: #78350f; color: #fcd34d; border-left: 5px solid #f59e0b; }
    .warm      { background-color: #365314; color: #bbf7d0; border-left: 5px solid #22c55e; }
    .cold      { background-color: #1e3a5f; color: #bae6fd; border-left: 5px solid #38bdf8; }
    .freezing  { background-color: #1e1b4b; color: #c7d2fe; border-left: 5px solid #818cf8; }
</style>
""", unsafe_allow_html=True)

st.title("🎮 Game Glitch Investigator")
st.caption("An AI-generated guessing game. Something is off.")

st.sidebar.header("⚙️ Settings")

difficulty = st.sidebar.selectbox(
    "Difficulty",
    ["Easy", "Normal", "Hard"],
    index=1,
)

attempt_limit_map = {
    "Easy": 6,
    "Normal": 8,
    "Hard": 5,
}
attempt_limit = attempt_limit_map[difficulty]

low, high = get_range_for_difficulty(difficulty)

st.sidebar.caption(f"Range: {low} to {high}")
st.sidebar.caption(f"Attempts allowed: {attempt_limit}")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(low, high)

if "attempts" not in st.session_state:
    # FIX: Changed attempts initialization from 1 to 0 to start game correctly
    st.session_state.attempts = 0  # FIXME: Should be 0 to start correctly

if "score" not in st.session_state:
    st.session_state.score = 0

if "status" not in st.session_state:
    st.session_state.status = "playing"

if "history" not in st.session_state:
    st.session_state.history = []  # FIXME: Now stores dicts for summary table (Challenge 4)

# ── CHALLENGE 4: Hot/Cold temperature helper ───────────────────────────────────
def get_temperature(guess: int, secret: int) -> tuple:
    """
    Return (emoji, label, css_class) based on how close the guess is.
    Core logic (check_guess) is unchanged — this is purely UI enrichment.
    """
    # FIXME: Challenge 4 addition — does not modify check_guess or logic_utils.py
    diff = abs(guess - secret)
    if diff == 0:
        return "🎯", "EXACT!", "scorching"
    elif diff <= 3:
        return "🔥🔥🔥", "Scorching!", "scorching"
    elif diff <= 8:
        return "🔥🔥", "Hot!", "hot"
    elif diff <= 15:
        return "🔆", "Warm", "warm"
    elif diff <= 25:
        return "❄️", "Cold", "cold"
    else:
        return "🧊🧊", "Freezing!", "freezing"

# ── CHALLENGE 4: Live stats bar ────────────────────────────────────────────────
# FIXME: Challenge 4 addition — four-column metric strip for at-a-glance status
col_a, col_b, col_c, col_d = st.columns(4)
col_a.metric("🎲 Attempts Left", attempt_limit - st.session_state.attempts)
col_b.metric("📋 Guesses Made", st.session_state.attempts)
col_c.metric("⭐ Score", st.session_state.score)
col_d.metric("📏 Range", f"{low}–{high}")

st.divider()

st.subheader("Make a guess")

st.info(
    f"Guess a number between {low} and {high}. "
    f"Attempts left: {attempt_limit - st.session_state.attempts}"
)

with st.expander("Developer Debug Info"):
    # FIX: Hid secret number in debug info to prevent cheating
    # FIXME: Changed from showing secret to "(hidden)" to prevent cheating
    st.write("Secret:", "(hidden)")
    st.write("Attempts:", st.session_state.attempts)
    st.write("Score:", st.session_state.score)
    st.write("Difficulty:", difficulty)
    st.write("History:", st.session_state.history)

raw_guess = st.text_input(
    "Enter your guess:",
    key=f"guess_input_{difficulty}"
)

col1, col2, col3 = st.columns(3)
with col1:
    submit = st.button("Submit Guess 🚀")
with col2:
    new_game = st.button("New Game 🔁")
with col3:
    show_hint = st.checkbox("Show hint", value=True)

if new_game:
    # FIX: Implemented proper game reset to clear all session state and generate new secret
    # FIXME: Added proper reset of all session state for new game
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(low, high)
    st.session_state.score = 0
    st.session_state.status = "playing"
    st.session_state.history = []
    st.success("New game started.")
    st.rerun()

if st.session_state.status != "playing":
    if st.session_state.status == "won":
        st.success("You already won. Start a new game to play again.")
    else:
        st.error("Game over. Start a new game to try again.")
    st.stop()

if submit:
    st.session_state.attempts += 1

    ok, guess_int, err = parse_guess(raw_guess)

    if not ok:
        st.error(f"❌ {err}")
        st.session_state.attempts -= 1  # FIXME: Don't count invalid input as an attempt
    else:
        # FIXME: Removed buggy logic that converted secret to string on even attempts using Copilot
        # FIXME: Removed buggy secret conversion to string on even attempts
        secret = st.session_state.secret

        outcome, message = check_guess(guess_int, secret)

        # CHALLENGE 4: Hot/Cold enrichment — UI only, outcome from check_guess unchanged
        # FIXME: Challenge 4 addition — get_temperature is purely cosmetic
        emoji, temp_label, css_class = get_temperature(guess_int, secret)
        direction = "—" if outcome == "Win" else ("⬆️ Go Higher" if outcome == "Too Low" else "⬇️ Go Lower")

        # FIXME: Challenge 4 — append structured dict for summary table instead of raw value
        st.session_state.history.append({
            "#": st.session_state.attempts,
            "Guess": guess_int,
            "Direction": direction,
            "🌡️ Temp": f"{emoji} {temp_label}",
            "Score Δ": None,  # filled after update_score below
        })

        # CHALLENGE 4: Color-coded hint banner replaces plain st.warning
        # FIXME: Challenge 4 — swapped st.warning(message) for styled HTML hint box
        if show_hint:
            st.markdown(
                f'<div class="hint-box {css_class}">'
                f'{emoji} &nbsp; <strong>{temp_label}</strong> &nbsp;|&nbsp; {message}'
                f'</div>',
                unsafe_allow_html=True,
            )

        new_score = update_score(
            current_score=st.session_state.score,
            outcome=outcome,
            attempt_number=st.session_state.attempts,
        )
        # FIXME: Challenge 4 — track per-turn score delta for summary table
        delta = new_score - st.session_state.score
        st.session_state.history[-1]["Score Δ"] = f"{'+' if delta >= 0 else ''}{delta}"
        st.session_state.score = new_score

        if outcome == "Win":
            st.balloons()
            st.session_state.status = "won"
            st.success(
                f"🏆 You won in **{st.session_state.attempts}** guess(es)! "
                f"The secret was **{secret}**. "
                f"Final score: {st.session_state.score}"
            )
        else:
            if st.session_state.attempts >= attempt_limit:
                st.session_state.status = "lost"
                st.error(
                    f"💀 Out of attempts! "
                    f"The secret was {st.session_state.secret}. "
                    f"Score: {st.session_state.score}"
                )

# ── CHALLENGE 4: Session summary table ────────────────────────────────────────
# FIXME: Challenge 4 addition — renders after every guess, purely display logic
if st.session_state.history:
    st.divider()
    st.subheader("📊 Guess History")
    st.table(st.session_state.history)

st.divider()
st.caption("Built by an AI that claims this code is production-ready.")