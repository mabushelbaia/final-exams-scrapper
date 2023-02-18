# Final Exams Scraper

> A simple web scraper that scrapes the final exam schedule from Birzeit University [website](https://ritaj.birzeit.edu/student/final-schedule) and outputs it to an ics file.

# Usage

1. Clone the repository

```bash
git clone https://github.com/mabushelbaia/final-exams-scraper
```

2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. since the websites uses cloudflare, you need to get the html page manually and save it as `index.html` in the same directory as the script.
4. run the script

```bash
python main.py
```

5. the output will be saved as `finals.ics` in the same directory as the script.

6. import the file to your calendar app.
