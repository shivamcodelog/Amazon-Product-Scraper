# 🛒 Amazon Product Scraper

A lightweight Python web scraper that extracts product information (title, author, price, and links) from Amazon India search results using Selenium and BeautifulSoup.

## ✨ Features

- 🔍 **Multi-page scraping** - Automatically scrapes multiple pages of Amazon search results
- ⏱️ **Random delays** - Built-in random delays (1-3 seconds) to mimic human behavior
- 📊 **Flexible export** - Save scraped data in CSV or Excel format
- 🎯 **Simple configuration** - Easy-to-modify variables for product, pages, and file settings
- 🛡️ **Robust error handling** - try-except-finally blocks ensure browser always closes
- 📁 **Auto-directory creation** - Automatically creates folders using `exist_ok=True`
- 🧹 **Text cleaning** - Handles encoding issues and formats Unicode characters
- 🔄 **Dual parser approach** - Uses both BeautifulSoup and lxml for flexible data extraction

## 📋 Prerequisites

- Python 3.7 or higher
- Google Chrome browser
- ChromeDriver (matching your Chrome version)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/Amazon-Product-Scraper.git
   cd Amazon-Product-Scraper
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download ChromeDriver**
   - Visit [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads)
   - Download version matching your Chrome browser
   - Add to system PATH or place in project directory

## 📦 Dependencies

Create a `requirements.txt` file:

```txt
selenium>=4.15.0
beautifulsoup4>=4.12.0
pandas>=2.0.0
lxml>=4.9.0
openpyxl>=3.1.0
```

Install with:
```bash
pip install -r requirements.txt
```

## 🎮 Usage

### Configuration

Edit these variables at the top of the script:

```python
# Product configuration
pdt = "neuroscience"              # Product name to search
page_no = 1                       # Number of pages to scrape

# Output configuration
file_name = "neurobook_data"      # Output file name (without extension)
file_type = "excel"               # Options: "excel" or "csv"
```

### Running the Scraper

```bash
python amazon_scraper.py
```

### Expected Output

```
🌀 Preparing Page: 1/1...
file01: scraped
file02: scraped
file03: scraped
...
Pages Scraped🌀: 1
Browser closed
```

## 📁 Project Structure

```
Amazon-Product-Scraper/
│
├── amazon_scraper.py          # Main scraper script
├── requirements.txt           # Python dependencies
├── README.md                  # Documentation
│
├── data_book2/               # HTML files (auto-created)
│   ├── file01.html
│   ├── file02.html
│   └── ...
│
└── neurobook_data.xlsx       # Output data file
```

## 📊 Extracted Data Fields

| Field | Description | Example |
|-------|-------------|---------|
| **Title** | Product name/title | "Principles of Neural Science" |
| **Author** | Author or brand name | "Eric Kandel" |
| **Price** | Product price in INR | "Rs.5,249" |
| **Link** | Direct product URL | "https://www.amazon.in/..." |

### Sample Output

| Title | Author | Price | Link |
|-------|--------|-------|------|
| Principles of Neural Science | Eric Kandel | Rs.5,249 | https://amazon.in/dp/... |
| Neuroscience: Exploring the Brain | Mark Bear | Rs.3,899 | https://amazon.in/dp/... |
| Cognitive Neuroscience | Michael Gazzaniga | Rs.4,599 | https://amazon.in/dp/... |

## 🔧 Configuration Options

### Basic Settings

| Variable | Type | Description | Default |
|----------|------|-------------|---------|
| `pdt` | string | Product search query | `"neuroscience"` |
| `page_no` | integer | Number of pages to scrape | `1` |
| `file_name` | string | Output file name | `"neurobook_data"` |
| `file_type` | string | Export format: "excel" or "csv" | `"excel"` |

### Chrome Options

Uncomment to enable window maximization:
```python
options = Options()
options.add_argument("--start-maximized")  # Uncomment this line
```

## 🔍 How It Works

1. **Initialize Browser** - Opens Chrome browser with Selenium WebDriver
2. **Navigate & Wait** - Goes to Amazon search page and waits for products to load
3. **Extract HTML** - Saves each product's HTML to separate files in `data_book2/` folder
4. **Parse Data** - Uses BeautifulSoup and lxml XPath to extract title, author, price, link
5. **Clean Text** - Removes encoding issues and formats Unicode characters
6. **Export Data** - Saves to CSV or Excel file using pandas
7. **Close Browser** - Ensures browser is closed even if errors occur

## ⚙️ Technical Details

### Scraping Strategy

- Uses **WebDriverWait** with 15-second timeout for dynamic content
- Random delays between 1-3 seconds to avoid detection
- XPath selectors for precise data extraction
- Multiple fallback logic for missing elements

### Data Extraction Logic

```python
# Title extraction
title = dom.xpath("//h2/span/text()")

# Author extraction (with fallbacks)
author = soup.find("a", attrs={'class': "a-size-base a-link-normal..."})

# Price extraction (with fallbacks)
price = dom.xpath("//span[@class='a-price']/following-sibling::span[@class='a-offscreen']/text()")

# Link extraction
link = dom.xpath("//h2[contains(@class,'a-size-medium')]/parent::a/@href")
```

## 🐛 Troubleshooting

### Common Issues

**Issue**: No data scraped or empty files
- **Cause**: Amazon's HTML structure changed
- **Solution**: Update XPath selectors in the parsing section

**Issue**: ChromeDriver version mismatch error
- **Cause**: ChromeDriver doesn't match Chrome version
- **Solution**: Download correct ChromeDriver version

**Issue**: `ModuleNotFoundError`
- **Cause**: Missing dependencies
- **Solution**: Run `pip install -r requirements.txt`

**Issue**: Browser doesn't close after error
- **Cause**: Script terminated unexpectedly
- **Solution**: Script now uses try-finally to always close browser

**Issue**: "N/A" or "No text" in Author field
- **Cause**: Product doesn't have author information
- **Solution**: This is expected behavior; some products don't list authors

## ⚠️ Important Notes

### Legal & Ethical Considerations

⚖️ **Terms of Service**: Web scraping Amazon may violate their Terms of Service. This tool is provided for **educational purposes only**.

🚦 **Rate Limiting**: The scraper includes random delays (1-3 seconds) to reduce server load.

📜 **Recommended Alternative**: For commercial use, consider [Amazon Product Advertising API](https://webservices.amazon.com/paapi5/documentation/).

### Best Practices

- ✅ Use for personal research and learning
- ✅ Respect Amazon's servers with appropriate delays
- ✅ Don't scrape large amounts of data frequently
- ✅ Review Amazon's robots.txt and ToS
- ❌ Don't use for commercial purposes without permission
- ❌ Don't overload servers with rapid requests

## 🔄 Recent Improvements

- ✅ Fixed pagination loop to use variable `i` correctly
- ✅ Added random delays between requests (1-3 seconds)
- ✅ Implemented `exist_ok=True` for auto-directory creation
- ✅ Added try-except-finally for robust error handling
- ✅ Ensured browser always closes with `driver.quit()`
- ✅ Better file handling with encoding specification
- ✅ Improved text cleaning function for Unicode characters

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

## 📝 To-Do

- [ ] Add command-line arguments for configuration
- [ ] Implement logging system
- [ ] Add support for other Amazon domains (.com, .co.uk, etc.)
- [ ] Create GUI interface
- [ ] Add data visualization features
- [ ] Implement resume capability for interrupted scrapes

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Disclaimer

This web scraper is provided **for educational purposes only**. The author is not responsible for any misuse of this tool or violations of Amazon's Terms of Service. Users are solely responsible for ensuring their use complies with applicable laws and website terms.

**Always respect website policies and use official APIs for production applications.**

## 🙏 Acknowledgments

- [Selenium](https://www.selenium.dev/) - Browser automation framework
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/) - HTML/XML parsing library
- [Pandas](https://pandas.pydata.org/) - Data manipulation and analysis
- [lxml](https://lxml.de/) - XML and HTML processing

## 📧 Questions or Issues?

If you encounter any problems or have questions, please [open an issue](https://github.com/yourusername/Amazon-Product-Scraper/issues) on GitHub.

---

**Made with ❤️ for learning web scraping**

*This project is not affiliated with or endorsed by Amazon.*

