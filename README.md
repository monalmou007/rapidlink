# RapidLink

RapidLink is a Python program that analyzes disk usage and reports on space consumption by different files and folders in Windows. It helps users understand how disk space is being utilized in a specified directory, providing a detailed breakdown of the space occupied by individual files and subdirectories.

## Features

- Analyze disk usage for a specified path.
- Report size of each file and directory in bytes.
- Recursively explore subdirectories to provide detailed space consumption reports.

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the `rapidlink.py` file.
2. Ensure you have Python 3 installed on your system.

## Usage

Open your command line or terminal and navigate to the directory where `rapidlink.py` is located. Run the script using Python and specify the path you want to analyze as follows:

```bash
python rapidlink.py <path>
```

Replace `<path>` with the directory path you wish to analyze. For example:

```bash
python rapidlink.py C:\Users\YourUsername\Documents
```

## Example Output

```plaintext
Disk usage for directory: C:\Users\YourUsername\Documents
Directory: C:\Users\YourUsername\Documents\Project - Size: 204800 bytes
File: C:\Users\YourUsername\Documents\Report.docx - Size: 102400 bytes
File: C:\Users\YourUsername\Documents\Presentation.pptx - Size: 51200 bytes
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.