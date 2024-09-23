# PyScrap Tool

<p align="center">
 <img height="150" src="https://raw.githubusercontent.com/h471x/web_scraper/master/imgs/pyscrap.png"/>
</p>

<div align="center">

<p>

``pyscrap-tool`` is a Python-based web scraping utility that allows users to extract data from specified web pages. It provides options to scrape specific HTML tags and presents the data in a structured format, including the ability to save results to a CSV file.

</p>

</div>

## Features

- **Command-Line Interface (CLI)**: Easily scrape data directly from the terminal using command-line arguments.
- **Custom HTML Tag Scraping**: Specify which HTML tag to scrape from the webpage, allowing for flexible data extraction.
- **Data Output**: Print scraped data to the console and save it to a CSV file for further analysis.
- **Versioning**: Check the version of the tool using command-line options.

## Installation

### Option 1: Install from PyPI

To install `pyscrap-tool` directly from PyPI:

```bash
pip install pyscrap-tool
```

### Option 2: Build from Source

For those who prefer to build it themselves:

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone https://github.com/h471x/web_scraper.git
   cd web_scraper
   ```

2. Build the package:

   ```bash
   python setup.py sdist bdist_wheel
   ```

3. Install the package:

   ```bash
   pip install dist/*.whl
   ```

## Usage

Once the package is installed, you can use the `pyscrap` command from the terminal. The script accepts the following command-line arguments:

- **URL**:
  - `-l` or `--link`: Specify the URL of the webpage to scrape.

- **HTML Tag**:
  - `-t` or `--tag`: Specify the HTML tag to scrape (e.g., `article`, `div`).

- **Version**:
  - `-v` or `--version`: Display the version of the tool.

### Example Usage

1. **Basic Scrape**:
   ```bash
   pyscrap -l https://example.com -t article
   ```

2. **Display Version**:
   ```bash
   pyscrap -v
   ```

3. **Help Option**:
   For help with command-line options, use:
   ```bash
   pyscrap -h
   ```

## Development

To modify or extend the functionality, ensure you have the required dependencies installed. You can add new features to the CLI as needed.

## Contributing

Feel free to fork this repository, open issues, or submit pull requests with improvements or bug fixes. Your contributions help make the `PyScrap Tool` better!