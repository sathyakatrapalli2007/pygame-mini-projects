# 🌧️ Rain Simulation (Pygame)

This project simulates continuous rainfall using Pygame, focusing on natural motion and variation.

The rain effect is built using a grid of raindrop sprites, where each vertical column is assigned a consistent speed. Combined with random starting positions and smooth reset logic, this creates a more realistic and non-uniform rainfall pattern.

## How it works

Raindrops are generated in a spaced grid across the screen. Instead of giving every drop the same behavior:

* each column is assigned a random speed
* all drops in that column share that speed
* vertical positions are slightly randomized to avoid visible alignment

As the simulation runs, each drop moves downward independently. When a drop exits the screen, it is repositioned above the screen at a random height, creating a seamless looping effect.

## Key concepts used

* Sprite groups for managing multiple objects
* Grid-based placement using nested loops
* Column-wise variation using a dictionary
* Continuous motion with independent object updates
* Object recycling for infinite animation
* Randomization for natural visual effects

## Running the project

```bash
python main.py
```

Press `Q` to exit.

## Sound

The simulation includes a looping rain sound effect. The file `sound/rain.wav` is loaded and played in a continuous loop using `pygame.mixer.music`. This adds an immersive audio experience to the visual rain effect.

## Notes

The goal of this project was to move beyond uniform movement and explore how small variations (speed, spacing, position) affect realism. Instead of resetting the entire scene, each raindrop is reused, allowing for a smooth and continuous animation.

## Possible improvements

* Add horizontal wind movement
* Vary drop sizes for depth perception
* Introduce intensity changes (light vs heavy rain)
* Add background effects (dark sky, lightning)

---

Part of my learning journey in Python and Pygame.


