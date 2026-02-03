# Facebook Scraper
A Python-based automation script that logs into Facebook, searches for posts containing a specific keyword, scrolls through results, and extracts post details into an Excel file. Built using Selenium for browser automation.

Features
Automates Facebook login

Searches for posts with a specified keyword

Scrolls through search results automatically

Extracts post author names and post text

Saves results into an Excel file for further analysis

Requirements
Before running the script, ensure you have the following installed:

Python 3.7+

Google Chrome browser

ChromeDriver (matching your Chrome version)

Required Python libraries:

selenium

pandas

Installation
Clone this repository

bash
Copy
Edit
git clone https://github.com/yourusername/facebook-posts-scraper.git
cd facebook-posts-scraper
Install the dependencies

bash
Copy
Edit
pip install selenium pandas
Download ChromeDriver from
https://sites.google.com/chromium.org/driver/
and place it in your system PATH or in the project directory.

Usage
Open the script file and replace the following placeholders with your Facebook credentials:

python
Copy
Edit
username.send_keys("your_email_here")
password.send_keys("your_password_here")
Optionally change the search query by editing:

python
Copy
Edit
driver.get("https://www.facebook.com/search/posts/?q=i%20need%20website")
Run the script

bash
Copy
Edit
python main.py
The extracted data will be saved as:

Copy
Edit
facebook_posts.xlsx
Notes
This script is intended for educational and research purposes only.

Scraping personal data without consent may violate Facebook’s terms of service.

Use responsibly and comply with all applicable laws and platform rules. 

