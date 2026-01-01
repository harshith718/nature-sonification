import serial
import numpy as np
import sounddevice as sd
import time
import threading

# ===== CONFIG =====
PORT = "COM5"        # change only if needed
BAUD = 9600
SAMPLE_RATE = 48000
sd.default.device = 7   # Windows speakers

ser = serial.Serial(PORT, BAUD, timeout=1)

# ===== SOUND BASE =====
BASE_FREQ = 261.63
current_freq = BASE_FREQ
target_freq = BASE_FREQ
phase = 0.0

# ===== STATE =====
active = False
event_count = 0
density = 0
last_time = time.time()

lock = threading.Lock()

print("Nature sonification running (auto + gated)...")

# ===== AUDIO CALLBACK =====
def audio_callback(outdata, frames, time_info, status):
    global phase, current_freq, density, active

    if not active:
        outdata[:] = np.zeros((frames, 1))
        return

    t = (np.arange(frames) + phase) / SAMPLE_RATE
    tone = np.sin(2 * np.pi * current_freq * t)
    harm = np.sin(2 * np.pi * (current_freq * 2) * t)

    # ---- AUTO SOUND SELECTION ----
    if density < 3:
        # Leaf
        out = 0.25 * tone

    elif density < 7:
        # Wood / table
        out = 0.20 * tone + 0.15 * harm

    elif density < 12:
        # Plastic cube
        pulse = np.sin(2 * np.pi * 2 * t)
        out = 0.18 * tone * pulse

    else:
        # Metal
        out = 0.15 * tone + 0.30 * harm

    outdata[:] = out.reshape(-1, 1)
    phase += frames

# ===== START AUDIO =====
stream = sd.OutputStream(
    samplerate=SAMPLE_RATE,
    channels=1,
    callback=audio_callback
)
stream.start()

# ===== SERIAL LOOP =====
try:
    while True:
        line = ser.readline().decode().strip()
        if not line:
            continue

        value = int(line)

        # ---- GATE (on/off) ----
        if value > 50:
            active = True
        else:
            active = False

        # ---- EVENT DENSITY ----
        if value > 55:
            event_count += 1

        now = time.time()
        if now - last_time > 1.0:
            density = event_count
            event_count = 0
            last_time = now

        # ---- PITCH BEND ----
        drift = np.interp(value, [40, 90], [-120, 120])
        target_freq = BASE_FREQ + drift

        with lock:
            current_freq = 0.98 * current_freq + 0.02 * target_freq

        time.sleep(0.01)

except KeyboardInterrupt:
    stream.stop()
    stream.close()
