Nature Sonification

Nature Sonification is a small experimental project that explores how physical interaction with real-world objects can be converted into continuous sound. The project uses an Arduino, a piezoelectric sensor, and Python-based audio output to create sound that changes based on vibration.

The goal of this project was not to build a perfect system, but to understand what is realistically possible with minimal hardware and to learn from its limitations.

Hardware Used

The setup consists of an Arduino Uno, a piezoelectric disc sensor, a breadboard, resistors, and a laptop for running the audio software.

How It Works

When an object is touched or interacted with, the piezo sensor detects vibrations.
These vibrations are read by the Arduino as analog values and sent to the laptop through serial communication.
A Python program receives this data and generates continuous sound, which slowly changes based on the interaction.

The sound does not trigger on and off like a button. Instead, it behaves like an evolving texture that responds to movement over time.

What Worked

The system successfully generated sound in real time from physical interaction.
The connection between hardware and software was stable.
The sound evolved continuously rather than producing simple beeps.
Time-based changes in sound were clearly noticeable.

Limitations

Using a single bare piezo sensor provides limited information.
While vibrations can be detected, distinguishing between different materials is difficult with this setup.
This experiment highlighted how sensor choice and signal conditioning affect results.

How to Run

Upload the Arduino code that reads the piezo sensor.
Connect the Arduino to the laptop using USB.
Run the Python program to start sound generation.

Final Note

This project was created as a learning experiment.
It demonstrates both what is possible and what is limited when working with simple sensors.
Future improvements could include better sensors, signal buffering, or frequency-based analysis.

Project Links

A detailed explanation and reflections are available on the Notion project page.

https://www.notion.so/Nature-Sonification-2db9325d1ab1801eae36fe8f2971d58c?source=copy_link
