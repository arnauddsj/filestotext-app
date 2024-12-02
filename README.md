# Files to text App

Files to text App is a Python application that combines the content of all files present in a specified folder into a single .txt document. This tool is useful for creating a consolidated view of your project's files, making it easier to feed your codebase into AI or for other analysis purposes.

## Features

- Graphical user interface for easy operation
- Recursively scans a specified directory for files
- Combines the content of all files into a single .txt document
- Allows skipping specific files and directories
- Supports various file formats including text, CSV, Excel, Word, and PDF


## Requirements
* Python 3.9+ (recommended for Apple Silicon compatibility)
* PyQt5
* openpyxl
* python-docx
* PyPDF2
* requests

## Installation

1. Clone this repository or download the script:
```bash
git clone https://github.com/arnauddsj/filestotext-app.git
cd filestotext-app
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required libraries:
```bash
pip install --upgrade pip
pip install PyQt5 openpyxl python-docx PyPDF2 requests pyinstaller
```

For Apple Silicon Macs, use these commands instead:
```bash
pip install --upgrade pip
pip uninstall PyQt5 PyQt5-sip
pip install PyQt5-sip --no-binary :all:
pip install PyQt5 --no-binary PyQt5
pip install openpyxl python-docx PyPDF2 requests pyinstaller
```

## Usage
Run the script using Python:
```bash
python filestotext.py
```

The application will open with a graphical interface. From there, you can:
1. Select an input folder
2. Choose an output folder (optional)
3. Specify files and directories to ignore
4. Click "Process Files" to start the operation

## Compiling the App

### For macOS (Intel and Apple Silicon):
1. Make sure you have the required spec and entitlements files (included in the repository)
2. Open Terminal and navigate to the directory containing your Python script:
```bash
cd /path/to/your/filestotext-app
```

3. Run PyInstaller with the provided spec file:
```bash
pyinstaller --clean filestotext.spec
```

4. Once the process completes, you'll find your .app file in the `dist` directory.
5. You can move the .app file to your Applications folder:
```bash
mv dist/filestotext.app /Applications/
```

Note: When running the app for the first time, macOS might show a security warning since the app isn't from the App Store. You'll need to go to System Settings > Privacy & Security and approve the app to run.
## Configuration

The application allows you to configure the following settings through the GUI:

- Input Folder: The directory containing the files you want to combine
- Output Folder: The directory where the output .txt file will be saved (default: same as input folder)
- Ignore Files: Comma-separated list of file patterns to ignore
- Ignore Directories: Comma-separated list of directory names to ignore

## Default Ignore List

The application comes with a default list of files and directories to ignore. This list covers common patterns for JavaScript, Python, Ruby/Rails, PHP, and Go projects, as well as general development artifacts.

**Ignored Directories:** node_modules, build, dist, .git, .svn, .hg, .idea, .vscode, tmp, temp, logs, coverage, venv, env, __pycache__, .pytest_cache, .mypy_cache, vendor, .bundle, public/assets, public/packs, public/system, bin, pkg

**Ignored Files:** *.log, *.tmp, *.cache, .DS_Store, Thumbs.db, .env, .env.*, package-lock.json, *.svg, *.ico, *.lock, pnpm-lock.yaml, yarn.lock, *.pyc, *.pyo, *.egg-info, .python-version, Gemfile.lock, .ruby-version, composer.lock, go.sum

You can modify these lists in the application's GUI to suit your specific needs.

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
