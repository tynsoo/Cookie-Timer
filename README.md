# Cookie Timer

Cookie Timer is a web-based countdown timer application designed to help users accurately track cookie baking times. It provides a simple and intuitive interface for setting, starting, pausing, and resetting timers, making it easier to monitor baking sessions without losing track of time.

## Features

* Real-time countdown timer that stays accurate in background tabs
* Start, pause (Stop), resume, and reset
* Timer presets: Chewy (8:00), Classic (10:00), Crispy (12:00), plus your own custom times you can save or delete
* Multiple timers: add extra trays that count down on their own, each with start, stop, reset, and remove
* Audio notification: a little 8-bit chime when a timer finishes (can be turned off)
* Browser notifications when a timer finishes (opt in with the Alerts button)
* Dark mode, which follows your system setting until you pick one
* Persistent settings: your last bake time, custom presets, sound, alerts, and theme are remembered
* Shows the countdown in the browser tab title
* Simple and responsive user interface, optimized for desktop and mobile browsers

## Technologies Used

* HTML5
* CSS3
* JavaScript

> If your project uses additional technologies such as Node.js, Express.js, or Socket.IO, add them here.

## Installation

Clone the repository:

```bash
git clone https://github.com/tynsoo/Cookie-Timer.git
```

Navigate to the project directory:

```bash
cd Cookie-Timer
```

If the project uses npm packages, install the dependencies:

```bash
npm install
```

Start the application:

```bash
npm start
```

or

```bash
node server.js
```

Open your browser and visit:

```
http://localhost:3000
```

If the project is purely frontend, simply open the `index.html` file in your browser.

## Usage

1. Open the application and click **Let's Bake**.
2. Pick a preset, or click **+ Custom** to enter your own time. **Use** applies it once and **Save preset** keeps it for next time.
3. Click **Start** to begin the countdown.
4. Click **Stop** to pause (the cookie and timer freeze), and **Start** again to resume.
5. Click **Reset** to return the timer to its initial state.
6. Baking more than one batch? Click **+ Add tray** to run extra timers at the same time.
7. Wait for the chime (and notification, if you turned on the bell).

The icons in the top corner turn sound on/off, turn browser notifications on/off (bell), and switch between dark and light mode (moon/sun).

## Project Structure

```
Cookie-Timer/
├── buttons/      pixel-art buttons (icons/ holds the generated icon buttons)
├── images/       backgrounds and cookie art
├── index.html    start screen
├── bake.html     timer screen
├── fonts/        Silkscreen pixel font (SIL Open Font License)
├── tools/        make_icons.py redraws buttons/icons/
└── README.md
```

The icon buttons copy the edges and colors of `buttons/start.png`. To change one, edit its 7×7 glyph in `tools/make_icons.py` and run `python3 tools/make_icons.py` (needs Pillow).

## Future Improvements

* Keep running timers going after a page reload
* Name extra trays

## Contributing

Contributions are welcome. To contribute:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/your-feature
```

3. Commit your changes.

```bash
git commit -m "Add your feature"
```

4. Push the branch.

```bash
git push origin feature/your-feature
```

5. Open a Pull Request.

## License

This project is licensed under the MIT License.

## Author

**Tyn Solis**

GitHub: https://github.com/tynsoo
