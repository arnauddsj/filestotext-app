# Files to text App

File Processor is a Python application that combines the content of all files present in a specified folder into a single .txt document. This tool is useful for creating a consolidated view of your project's files, making it easier to feed your codebase into AI or for other analysis purposes.

## Features

- Graphical user interface for easy operation
- Recursively scans a specified directory for files
- Combines the content of all files into a single .txt document
- Allows skipping specific files and directories
- Supports various file formats including text, CSV, Excel, Word, and PDF

## Requirements

- Python 3.6+
- PyQt5
- openpyxl
- python-docx
- PyPDF2

## Installation

1. Clone this repository or download the script:
   ```
   git clone https://github.com/yourusername/file-processor.git
   cd file-processor
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required libraries:
   ```
   pip install PyQt5 openpyxl python-docx PyPDF2 pyinstaller
   ```

## Usage

Run the script using Python:

```
python file-processor-gui.py
```

The application will open with a graphical interface. From there, you can:

1. Select an input folder
2. Choose an output folder (optional)
3. Specify files and directories to ignore
4. Click "Process Files" to start the operation

## Compiling the App

To create a standalone .app file on macOS:

1. Open Terminal and navigate to the directory containing your Python script:
   ```
   cd /path/to/your/file-processor
   ```

2. Run PyInstaller with the following command:
   ```
   pyinstaller --onefile --windowed file-processor-gui.py
   ```

3. Once the process completes, you'll find your .app file in the `dist` directory.

## Configuration

The application allows you to configure the following settings through the GUI:

- Input Folder: The directory containing the files you want to combine
- Output Folder: The directory where the output .txt file will be saved (default: same as input folder)
- Ignore Files: Comma-separated list of file patterns to ignore
- Ignore Directories: Comma-separated list of directory names to ignore

## Output

The output .txt file will contain the content of all processed files, with each file's content preceded by its path:

```
PATH: /path/to/file1.txt
CONTENT:
[Content of file1.txt]

PATH: /path/to/file2.py
CONTENT:
[Content of file2.py]

...
```

## Error Handling

- If no input folder is selected, the application will display an error message.
- If no files are found in the specified directory, the application will display a message.
- Any errors encountered while processing individual files will be displayed in the application's log output.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](LICENSE).