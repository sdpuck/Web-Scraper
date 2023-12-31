# Scrape

#### Video Demo: https://www.youtube.com/watch?v=jnbf2vACohA


#### Description:
# Python-based Web Scraper for Cybersecurity Applications

## Overview

This project introduces a Python-based web scraper designed for extracting words from websites and compiling them into a list based on their frequency. Ideal for cybersecurity applications, this tool excels in creating customized password lists for penetration testing and Red Team exercises.

## Features

- Web Scraping**: Efficiently extracts words from specified web pages.
- Frequency Analysis: Compiles words into a list prioritizing their frequency of occurrence.
- Length Filtering: Filters words based on specified length criteria, ensuring data relevancy.
- Character Substitution**: Includes functionality to substitute certain letters with special characters, a practice common in creating strong passwords.
- Customized Password Lists: Generates lists suitable for testing password strength in various cybersecurity scenarios.

## Ideal Use Case

This tool is particularly valuable for cybersecurity professionals and enthusiasts. It aids in conducting penetration tests and Red Team exercises by providing realistic password lists that mimic user-generated passwords. Such lists are crucial for testing the robustness of security systems against common password attacks.

## Technical Details

Language: Written in Python
-Libraries: Utilizes libraries such as BeautifulSoup for web scraping and Tabulate for presenting data in an organized format.
- Customization: Users can customize the length of the words to be scraped and the letters to be substituted, allowing for flexibility according to the test requirements.

## Installation and Usage

1. Installation: Clone this repository and install the required libraries using `pip install -r requirements.txt`.
2. Configuration: Configure the script by setting the desired URL, word length, and character substitution rules.
3. Execution: Run the script from the command line to generate a password list.

## Disclaimer

This tool is developed for educational and ethical testing purposes only. Users must ensure they have the right to scrape the targeted website and should use the tool responsibly.
