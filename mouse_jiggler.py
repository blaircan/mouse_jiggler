#!/usr/bin/env python3
"""
Mouse Jiggler - Keeps your mouse moving to prevent auto-away status

Usage:
    python3 mouse_jiggler.py [--interval SECONDS] [--distance PIXELS]

This script automatically manages its own virtual environment - just run it!
"""

import sys
import os
import subprocess
from pathlib import Path

# Get the directory where this script lives
SCRIPT_DIR = Path(__file__).parent.absolute()
VENV_DIR = SCRIPT_DIR / ".venv"
VENV_PYTHON = VENV_DIR / "bin" / "python3"

# Check if we're running inside the venv
if not hasattr(sys, 'real_prefix') and not (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    # We're NOT in a venv - need to set one up and re-run ourselves
    
    # Create venv if it doesn't exist
    if not VENV_DIR.exists():
        print("🔧 First-time setup: Creating environment...")
        subprocess.check_call([sys.executable, "-m", "venv", str(VENV_DIR)])
        print("✅ Environment created!")
    
    # Install pyautogui if needed
    try:
        subprocess.check_call(
            [str(VENV_PYTHON), "-c", "import pyautogui"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
    except subprocess.CalledProcessError:
        print("📦 Installing dependencies...")
        subprocess.check_call([
            str(VENV_PYTHON), "-m", "pip", "install", "-q",
            "pyautogui",
            "--index-url", "https://pypi.ci.artifacts.walmart.com/artifactory/api/pypi/external-pypi/simple",
            "--trusted-host", "pypi.ci.artifacts.walmart.com"
        ])
        print("✅ Dependencies installed!\n")
    
    # Re-run this script with the venv Python
    os.execv(str(VENV_PYTHON), [str(VENV_PYTHON), __file__] + sys.argv[1:])

# If we get here, we're running in the venv - proceed with actual logic
import time
import argparse
from datetime import datetime
import pyautogui

# Fail-safe: move mouse to corner to stop
pyautogui.FAILSAFE = True


def jiggle_mouse(interval: int = 60, distance: int = 1, verbose: bool = True):
    """
    Jiggles the mouse at regular intervals.
    
    Args:
        interval: Seconds between jiggles (default: 60)
        distance: Pixels to move (default: 1 for subtle movement)
        verbose: Print status messages (default: True)
    """
    if verbose:
        print(f"🐭 Mouse Jiggler started!")
        print(f"   Interval: {interval} seconds")
        print(f"   Distance: {distance} pixels")
        print(f"   Move mouse to top-left corner to stop (FAILSAFE)")
        print(f"   Press Ctrl+C to exit\n")
    
    try:
        while True:
            # Get current position
            x, y = pyautogui.position()
            
            # Move mouse in a tiny square pattern
            pyautogui.moveRel(distance, 0, duration=0.1)
            pyautogui.moveRel(0, distance, duration=0.1)
            pyautogui.moveRel(-distance, 0, duration=0.1)
            pyautogui.moveRel(0, -distance, duration=0.1)
            
            if verbose:
                timestamp = datetime.now().strftime("%H:%M:%S")
                print(f"[{timestamp}] Jiggled at position ({x}, {y})")
            
            # Wait for the specified interval
            time.sleep(interval)
            
    except KeyboardInterrupt:
        if verbose:
            print("\n👋 Mouse Jiggler stopped. Stay productive!")
        sys.exit(0)
    except pyautogui.FailSafeException:
        if verbose:
            print("\n🛑 FAILSAFE triggered! Mouse moved to corner.")
        sys.exit(0)


def main():
    parser = argparse.ArgumentParser(
        description="Keep your mouse moving to prevent auto-away status"
    )
    parser.add_argument(
        "-i", "--interval",
        type=int,
        default=60,
        help="Seconds between jiggles (default: 60)"
    )
    parser.add_argument(
        "-d", "--distance",
        type=int,
        default=1,
        help="Pixels to move (default: 1 for subtle movement)"
    )
    parser.add_argument(
        "-q", "--quiet",
        action="store_true",
        help="Suppress output messages"
    )
    
    args = parser.parse_args()
    
    jiggle_mouse(
        interval=args.interval,
        distance=args.distance,
        verbose=not args.quiet
    )


if __name__ == "__main__":
    main()
