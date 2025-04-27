# Kilography1024

*Not everything is broadcast. Some things are smuggled.*

Kilography1024 is a simple tool to retrieve hidden fragments embedded inside images — relics of thought, seeded into the cracks of compression and time.

With it, you can uncover small documents tucked away inside images shared from [@Kilography1024](https://X.com/Kilography1024).  
Not grand revelations — just quiet things, surviving where noise reigns.

---

## Getting Started

If you wish to walk the tunnels, follow carefully:

### 1. Install Python

Make sure you have **Python 3.8 or later** installed.  
You can download it here: [https://www.python.org/downloads/](https://www.python.org/downloads/)

On macOS and Linux, Python is often pre-installed.  
On Windows, ensure you check the box **"Add Python to PATH"** during installation.

---

### 2. Create a Virtual Environment

This keeps your Kilography tools separated from the rest of your world.

Open a terminal (or command prompt) and run:

```bash
python -m venv kilography-env
```

This will create a private little corner just for Kilography.

---

### 3. Activate the Virtual Environment

Now, step into the tunnel.

- **Windows:**

    ```bash
    kilography-env\Scripts\activate
    ```

- **macOS/Linux:**

    ```bash
    source kilography-env/bin/activate
    ```

You should now see your terminal prompt change — a quiet sign that you are inside.

---

### 4. Install Requirements

Within the virtual environment, install the necessities:

```bash
pip install -r requirements.txt
```

The tools you need will quietly gather.

---

### 5. Download a Kilography Image

Venture to [@Kilography1024](https://X.com/Kilography1024).  
Find an image that calls to you. Download it to your device.  
(Preferably keep the filename simple — **no strange spaces or symbols**.)

---

### 6. Extract the Hidden Seed

In your terminal, run:

```bash
python Kilography1024.py <path_to_image.jpg>
```

Example:

```bash
python Kilography1024.py tunneldoor.jpg
```

The script will attempt to find the embedded file within the image.  
If successful, it will create a new file alongside it — a small document, no larger than 1024 bytes.

---

## What You'll Find

Not manifestos.  
Not answers.  
Just traces — whispers folded into the noise.

A door left ajar in a place you were never meant to reach.

---

## Troubleshooting

- **"Module not found" errors?**  
  Make sure you activated your virtual environment.
  
- **No file extracted?**  
  Some images may not contain payloads.  
  (Or the path may be wrong — double-check spelling and extensions.)

- **Python errors?**  
  Ensure you're using Python 3.8 or newer.

If all else fails, sit for a moment. Listen to the silence. Try again.

---

## License

Kilography1024 is offered under a quiet license:  
use gently, respect the tunnels, and leave no loud footprints.

---

# 🌑

*"I exist. You found me."*
