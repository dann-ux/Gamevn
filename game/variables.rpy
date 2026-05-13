## variables.rpy
## All global variables, flags, and relationship values are defined here.
## This is the single source of truth for game state.

## ── PROTAGONIST ──────────────────────────────────────────────────────────────

default protagonist_name = "Alex"
default protagonist_species = "Unknown"

## ── RELATIONSHIP POINTS ──────────────────────────────────────────────────────
## One variable per character. Invisible to the player.
## Convention: rel_[character_id]
## Range: No hard cap. Narrative gates defined per character in their route.

## Placeholder characters (replace IDs when characters are named)
default rel_char1 = 0
default rel_char2 = 0
default rel_char3 = 0
default rel_char4 = 0

## ── BINARY FLAGS ─────────────────────────────────────────────────────────────
## True/False variables that permanently open or close story branches.
## Convention: flag_[description]

## Example flags (expand as narrative is written)
default flag_arrived_at_camp = False
default flag_first_day_complete = False

## ── RANDOMNESS FLAGS ─────────────────────────────────────────────────────────
## Randomness is rolled at game start and stored here.
## This ensures consistency within a single playthrough.

## Active characters this playthrough (populated on new game)
default active_characters = []

## Random event pool seed (set at new game start)
default event_seed = 0

## ── DAY TRACKING ─────────────────────────────────────────────────────────────

default current_day = 1
default max_days = 14  ## Default. Randomized at game start within design range.
