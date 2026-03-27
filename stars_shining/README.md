# ✨ Star Shining Animation (Pygame)

This project creates a simple star field animation using Pygame, where stars appear to “shine” by alternating between two layered grids over time.

Instead of modifying individual stars, the effect is achieved by switching between two pre-built sprite groups (`Star` and `StarShine`) at fixed intervals. This creates a clean blinking/shimmering illusion without complex calculations.

## How it works

A full-screen grid of stars is created twice:

* one normal layer (`stars`)
* one brighter/alternate layer (`starshine`)

A timer runs inside the game loop. Every few frames, it toggles which layer is displayed:

* when `whatshine = False` → normal stars are shown
* when `whatshine = True` → shining stars are shown

This alternating pattern gives the impression that stars are flickering or glowing.

## Key concepts used

* Sprite groups in Pygame
* Grid-based object placement using nested loops
* Basic animation using a timer
* Layer switching for visual effects
* Game loop structure and rendering control
* Playing soothing music on loop using the pygame.mixer module

## Running the project

```bash
python main.py
```

Press `ESC` to exit.

## Notes

This approach focuses on simplicity — instead of animating each star individually, it uses layer switching to simulate motion and variation. It’s a good introduction to building visual effects using minimal logic.

## Possible improvements

* Add random flicker timing instead of fixed intervals
* Introduce different star sizes for depth
* Combine with movement for a parallax effect
* Gradually fade between layers instead of switching instantly

---

Part of my learning journey in Python and Pygame.
