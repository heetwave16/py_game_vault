# Py Game Vault

A personal stash of retro arcade mini-games built with Python + Pygame.

This project is focused on simple arcade mechanics like game loops, movement, collisions, score tracking, and restart flows.

---

## Games Included

### 1. Snake (`snake.py`)
Classic Snake with wrap-around movement and score tracking.

- **Controls:** Arrow keys to move
- **Restart after game over:** `R`
- **Goal:** Eat food to grow and increase score without colliding with your body.

### 2. Tetris (`tetris.py`)
Classic falling-block puzzle game with line clears, levels, and scoring.

- **Controls:**
  - `←` / `→`: Move piece
  - `↓`: Soft drop
  - `↑`: Rotate
  - `Space`: Hard drop
- **Restart after game over:** `R`
- **Goal:** Clear as many lines as possible and maximize score.

---

## How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/heetwave16/py_game_vault.git
   cd py_game_vault
   ```

2. Install dependency:

   ```bash
   pip install pygame
   ```

3. Run a game:

   ```bash
   python snake.py
   # or
   python tetris.py
   ```
