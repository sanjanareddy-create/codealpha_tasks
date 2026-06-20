# Task Automation with Python

## Description
This project automates a repetitive task by moving JPG image files from a source folder to a destination folder using Python.

## Features
- Automatically detects JPG files
- Moves files from one folder to another
- Creates destination folder if it does not exist
- Displays success messages

## Technologies Used
- Python
- os module
- shutil module

## Project Structure

CodeAlpha_TaskAutomation/
│
├── SourceFolder/
├── DestinationFolder/
├── file_mover.py
└── README.md

## How to Run

1. Place JPG files inside SourceFolder
2. Open terminal
3. Run:

```bash
python file_mover.py
```

4. Files will be moved to DestinationFolder