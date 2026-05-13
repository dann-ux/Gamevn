## screens.rpy
## UI screen definitions. All custom screens are written here.
## Ren'Py's default screens are used until replaced with final UI.

## ── MAIN MENU ─────────────────────────────────────────────────────────────────

screen main_menu():
    tag menu

    ## Background (replace with final UI asset)
    add "#1a1a1a"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 20

        text "Camp Adventure" size 48 color "#f5e6c8" xalign 0.5

        textbutton "New Game" action Start() xalign 0.5
        textbutton "Load Game" action ShowMenu("load") xalign 0.5
        textbutton "Quit" action Quit() xalign 0.5

## ── HUD / DAY DISPLAY ────────────────────────────────────────────────────────
## Shown during gameplay. Displays current day.

screen hud():
    frame:
        xalign 1.0
        yalign 0.0
        xoffset -10
        yoffset 10
        text "Day [current_day] / [max_days]" size 20 color "#f5e6c8"

## ── ADD NEW SCREENS BELOW THIS LINE ─────────────────────────────────────────
