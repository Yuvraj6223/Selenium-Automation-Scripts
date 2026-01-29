# 🤖 Selenium Automation Scripts

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)

A comprehensive collection of Python Selenium WebDriver practice scripts covering essential automation topics like waits, alerts, dropdowns, file handling, authentication, browser commands, and more. Ideal for learning, revising, and demonstrating web automation skills.

## ✨ Features

- 🔍 **Element Locators**: All 8 locator strategies (ID, Name, XPath, CSS, etc.)
- ⏳ **Waits**: Implicit, Explicit, and Fluent waits with conditions
- 🚨 **Alert Handling**: Accept, dismiss, and text input in alerts
- 📋 **Dropdown Operations**: Select by value, index, and visible text
- 📁 **File Operations**: Upload and download file automation
- 🔐 **Authentication**: Basic HTTP authentication handling
- 🌐 **Browser Commands**: Navigation, screenshots, window management
- 🖱️ **Mouse Actions**: Hover, drag-and-drop, context menu
- ⌨️ **Keyboard Actions**: Key combinations, text input
- 🪟 **Window/Tab Handling**: Switch between windows and iframes
- 📸 **Screenshot Capture**: Full page and element screenshots
- 🍪 **Cookie Management**: Add, get, and delete cookies

## 🛠️ Tech Stack

- **Selenium WebDriver**: Browser automation
- **Python 3.8+**: Programming language
- **ChromeDriver**: Chrome browser driver
- **pytest**: Testing framework (optional)

## 📋 Prerequisites

- Python 3.8 or higher
- Chrome browser installed
- ChromeDriver (auto-managed with webdriver-manager)

## 🚀 Installation

1. **Clone the repository**
```bash
git clone https://github.com/Yuvraj6223/Selenium-Automation-Scripts.git
cd Selenium-Automation-Scripts
```

2. **Create a virtual environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Running Individual Scripts:

```bash
# Example: Run alert handling script
python scripts/alerts_handling.py

# Example: Run dropdown operations
python scripts/dropdown_operations.py
```

### Running All Tests (if using pytest):

```bash
pytest tests/ -v
```

## 📚 Script Categories

### 1. **Locator Strategies** (`locators.py`)
```python
# Find by ID
element = driver.find_element(By.ID, "username")

# Find by XPath
element = driver.find_element(By.XPATH, "//input[@name='email']")

# Find by CSS Selector
element = driver.find_element(By.CSS_SELECTOR, ".submit-btn")
```

### 2. **Wait Mechanisms** (`waits.py`)
```python
# Implicit Wait
driver.implicitly_wait(10)

# Explicit Wait
wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, "myElement")))

# Fluent Wait
wait = WebDriverWait(driver, 30, poll_frequency=1)
```

### 3. **Alert Handling** (`alerts.py`)
```python
# Accept alert
driver.switch_to.alert.accept()

# Dismiss alert
driver.switch_to.alert.dismiss()

# Send text to prompt
driver.switch_to.alert.send_keys("Hello")
```

### 4. **Dropdown Operations** (`dropdowns.py`)
```python
from selenium.webdriver.support.select import Select

dropdown = Select(driver.find_element(By.ID, "country"))
dropdown.select_by_visible_text("India")
dropdown.select_by_value("in")
dropdown.select_by_index(2)
```

### 5. **File Upload/Download** (`file_operations.py`)
```python
# File Upload
upload_element = driver.find_element(By.ID, "file-upload")
upload_element.send_keys("/path/to/file.txt")

# Configure download directory
chrome_options = Options()
prefs = {"download.default_directory": "/path/to/downloads"}
chrome_options.add_experimental_option("prefs", prefs)
```

### 6. **Mouse Actions** (`mouse_actions.py`)
```python
from selenium.webdriver import ActionChains

actions = ActionChains(driver)

# Hover
actions.move_to_element(element).perform()

# Drag and Drop
actions.drag_and_drop(source, target).perform()

# Right Click
actions.context_click(element).perform()
```

### 7. **Keyboard Actions** (`keyboard_actions.py`)
```python
from selenium.webdriver.common.keys import Keys

# Single key
element.send_keys(Keys.ENTER)

# Key combinations
element.send_keys(Keys.CONTROL + "a")
element.send_keys(Keys.CONTROL + "c")
```

### 8. **Window Handling** (`window_handling.py`)
```python
# Get current window handle
parent_window = driver.current_window_handle

# Switch to new window
for window in driver.window_handles:
    if window != parent_window:
        driver.switch_to.window(window)
```

### 9. **Screenshot Capture** (`screenshots.py`)
```python
# Full page screenshot
driver.save_screenshot("screenshot.png")

# Element screenshot
element.screenshot("element.png")
```

### 10. **Cookie Management** (`cookies.py`)
```python
# Add cookie
driver.add_cookie({"name": "test", "value": "cookie_value"})

# Get all cookies
cookies = driver.get_cookies()

# Delete cookie
driver.delete_cookie("test")
```

## 📁 Project Structure

```
Selenium-Automation-Scripts/
│
├── scripts/
│   ├── locators.py
│   ├── waits.py
│   ├── alerts.py
│   ├── dropdowns.py
│   ├── file_operations.py
│   ├── mouse_actions.py
│   ├── keyboard_actions.py
│   ├── window_handling.py
│   ├── screenshots.py
│   └── cookies.py
│
├── tests/              # pytest test cases
├── utils/              # Helper functions
├── requirements.txt    # Dependencies
├── LICENSE            # MIT License
└── README.md          # This file
```

## 🎓 Learning Path

**Beginner**:
1. Locators
2. Basic interactions (click, send_keys)
3. Waits

**Intermediate**:
4. Alerts and popups
5. Dropdowns
6. Window handling

**Advanced**:
7. Mouse and keyboard actions
8. File operations
9. Screenshots and cookies
10. Framework integration (pytest/unittest)

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/NewScript`)
3. Commit changes (`git commit -m 'Add authentication script'`)
4. Push to branch (`git push origin feature/NewScript`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Selenium](https://www.selenium.dev/) for web automation framework
- [Python](https://www.python.org/) community

## 📧 Contact

**Yuvraj V A** - [yuvrajva09@gmail.com](mailto:yuvrajva09@gmail.com)

Project Link: [https://github.com/Yuvraj6223/Selenium-Automation-Scripts](https://github.com/Yuvraj6223/Selenium-Automation-Scripts)

---

⭐ If you find this project helpful, please consider giving it a star!