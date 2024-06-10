# Python Snipping Tool (PySide6)

![snipping_tool_demo](https://github.com/sungbinlee/snipping-tool/assets/52542229/bf457fba-d073-4a80-9a37-d81f0179bd41)

This project is a Python-based snipping tool developed using PySide6 and Pillow libraries. Users can capture screenshots of any object on their screen. It is based on the implementation of [harupy/snipping-tool](https://github.com/harupy/snipping-tool) and additionally supports dual-monitor setups and handles scaling for high-resolution displays.

## Features

- Capture screenshots of any object on the screen
- Support for dual-monitor setups
- Scaling support for high-resolution displays ([High DPI Displays](https://doc.qt.io/qt-6/highdpi.html) for reference)

## How to Run

1. Clone this repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python snipping-tool.py
   ```
4. The application will start, allowing you to capture screenshots of any object on your screen.
5. Screenshots will be automatically saved with incrementing file names (e.g., `snip1.png`, `snip2.png`, etc.).
6. Press the `Q` key to exit the application.

## 블로그 글 읽어보기
- https://sungbinlee.dev/software%20engineering/snipping-tool-debugging/
