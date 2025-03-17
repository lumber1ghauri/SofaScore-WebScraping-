Ping Pong Match Scraper
This repository contains two Python scripts designed to scrape ping pong match data from SofaScore, specifically targeting the Czech Liga Pro league. The project was developed as part of a task assigned by a client to automate the collection of match data and export it to an Excel file.

Background
The task came from a client request:

"Hey Ukasha Zahid! I would like to have an Excel file containing the data of the ping pong matches of each day for example of the Czech Liga Pro league from the site www.sofascore.com/it/ping-pong (or whatever you want). If the data import is automatic better otherwise I can do it manually every day at the same time. In Excel I need these columns: Player 1, Player 2, Final result, Set 1 result, Set 2 result, Set 3 result, Set 4 result (optional), Set 5 result (optional). Can you give me a quote?"

To address this, I built a two-step solution: one script to fetch the raw HTML data and another to parse it into the required format. Below are the details of each script.

Files
1. fetch_sofascore.py
Purpose: Fetches the raw HTML content from the SofaScore ping pong page and saves it to a file.

Functionality:

Uses Selenium to load the dynamic page https://www.sofascore.com/it/ping-pong.
Waits for JavaScript content to render (10 seconds).
Saves the full page source to sofascore_pingpong.html.
Runs in headless mode to avoid opening a browser window.
Usage:

bash

Collapse

Wrap

Copy
python fetch_sofascore.py
Output: Creates sofascore_pingpong.html in the current directory.

2. parse_html.py
Purpose: Parses the HTML file to extract Czech Liga Pro match data and saves it to an Excel file.

Functionality:

Reads sofascore_pingpong.html using BeautifulSoup.
Extracts match details for Czech Liga Pro, including:
Player 1
Player 2
Final result (e.g., "3-2")
Set 1-5 results (currently placeholders; see Limitations).
Saves the data to ping_pong_matches.xlsx using pandas.
Note: Set scores require fetching individual match pages, which is partially implemented but needs refinement (see Limitations).
Usage:

bash

Collapse

Wrap

Copy
python parse_html.py
Output: Creates ping_pong_matches.xlsx with the extracted data.

Setup
Install Dependencies:
bash

Collapse

Wrap

Copy
pip install selenium webdriver-manager beautifulsoup4 pandas openpyxl
Run Scripts:
First, run fetch_html.py to get the HTML.
Then, run parse_matches.py to process it into Excel.
Limitations
Set Scores: The current sofascore_pingpong.html only contains final scores (e.g., "3-2"). Individual set scores (e.g., "11-9") are on match-specific pages (e.g., /it/table-tennis/match/...). The parse_matches.py script attempts to fetch these but needs accurate selectors for set scores, which I couldn’t fully test without a match page sample.
Automation: The scripts are manual for now. For daily automation, a scheduler (e.g., schedule library or cron) could be added.
Future Improvements
Refine set score extraction by fetching and parsing individual match pages with precise selectors.
Add a scheduler for automatic daily runs.
Handle potential anti-scraping measures from SofaScore (e.g., captchas).
Acknowledgments
Built with help from Grok (xAI) for debugging and optimization.
Designed to meet the client’s request for structured ping pong data.
