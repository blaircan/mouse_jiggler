# Mouse Jiggler 🐭

A simple Python script to keep your mouse moving and prevent auto-away status on Teams (or any other app).

**No installation needed!** The script auto-installs its dependency (pyautogui) on first run.

## Usage

### Basic usage (jiggles every 60 seconds):
```bash
cd ~/Documents/mouse-jiggler
python3 mouse_jiggler.py
```

### Custom interval (e.g., every 30 seconds):
```bash
python3 mouse_jiggler.py --interval 30
```

### Adjust movement distance:
```bash
python3 mouse_jiggler.py --distance 5
```

### Quiet mode (no output):
```bash
python3 mouse_jiggler.py --quiet
```

### Combine options:
```bash
python3 mouse_jiggler.py --interval 45 --distance 2
```

## Stopping the script

- **Ctrl+C**: Normal exit
- **Move mouse to top-left corner**: Emergency failsafe stop

## How it works

The script moves your mouse in a tiny square pattern (1 pixel by default) at regular intervals (60 seconds by default). The movement is subtle enough that it won't disrupt your work but sufficient to prevent auto-away status.

## Safety Features

- **FAILSAFE**: Moving the mouse to the top-left corner of your screen will immediately stop the script
- **Gentle movement**: Default 1-pixel movement is nearly invisible
- **Keyboard interrupt**: Ctrl+C for clean exit

---

*Disclaimer: Use responsibly. This tool is for preventing auto-away during legitimate work sessions.* 😉
