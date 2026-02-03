# 🐍 Snake Game

A modern Snake game built with Python and Pygame. Control your snake through a grid to collect food while avoiding walls and yourself.

## ✨ Features

- Player-controlled gameplay with arrow keys
- Snake head rotates toward nearest food source
- Grid-based smooth movement
- Real-time score tracking
- Collision detection (walls & self)
- Custom sprite support (head, tail, food)
- Optional background image with adaptive grid colors
- Customizable window size and difficulty

## 🚀 Quick Start

### Installation
```bash
pip install pygame
```

### Run the Game
```bash
python snake.py
```

### Required Files
- `head.webp` - Snake head sprite
- `tail.webp` - Snake body sprite
- `food.webp` - Food sprite
- `BG.webp` - (Optional) Background image

## 🎮 Game Controls

| Key | Action |
|-----|--------|
| ↑ | Move Up |
| ↓ | Move Down |
| ← | Move Left |
| → | Move Right |
| R | Restart (after game over) |

## ⚙️ Configuration

Edit these settings in `snake.py`:

```python
WIDTH, HEIGHT = 1000, 700  # Screen size
CELL_SIZE = 40             # Grid cell size
FPS = 10                   # Game speed
```

**Difficulty Tips:**
- Increase `FPS` for harder gameplay
- Decrease `FPS` for easier gameplay
- Adjust screen size with `WIDTH` and `HEIGHT`

## 🎨 Customization

Replace WebP image files with your own sprites (40x40 pixels recommended). The game works without a background image using default checkerboard pattern.

## 📊 Game Mechanics

- **Head Direction**: Points toward food to help planning
- **Grid Alignment**: All sprites snap to grid positions
- **Random Spawning**: Food appears at random grid-aligned positions
- **Scoring**: +1 point per food collected

## 🐛 Troubleshooting

**Images not loading?**
- Verify all `.webp` files are in the project directory
- Check filenames are exact (case-sensitive)

**Game runs slowly?**
- Decrease `FPS` value
- Reduce window dimensions

## 📝 Project Structure

```
pamu/
├── snake.py        # Main game script
├── head.webp       # Snake head sprite
├── tail.webp       # Snake body sprite
├── food.webp       # Food sprite
├── BG.webp         # Background (optional)
└── README.md       # This file
```

## 📄 License

Open source - modify and distribute freely.

---

**Enjoy! 🎮**

