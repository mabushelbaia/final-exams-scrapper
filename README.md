# Final Exams Scraper

> A simple web scraper that scrapes the final exam schedule from Birzeit University [website](https://ritaj.birzeit.edu/student/final-schedule) and outputs it to an ics file.

# Usage

1. Clone the repository

```bash
git clone https://github.com/mabushelbaia/final-exams-scraper.git
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

# Console Output
The script will also output the scraped data to the console in a tabular format.
```bash
                   Date           Time    Course                Course Title                             Rooms
0   Thursday 16/02/2023  08:00 - 10:30  ENCS4110  COMPUTER DESIGN LABORATORY                Masri304, Masri306
1     Monday 20/02/2023  11:00 - 13:30   COMP333            DATABASE SYSTEMS                  Aggad225, KNH625
2  Wednesday 22/02/2023  14:00 - 16:30  ENEE3309       COMMUNICATION SYSTEMS  Masri109, S.Abdulhadi380, SCI240
3   Thursday 23/02/2023  14:00 - 16:30  ENCS3320           COMPUTER NETWORKS        A.Shaheen152, A.Shaheen162
4   Saturday 25/02/2023  08:00 - 10:30  ENCS3340     ARTIFICIAL INTELLIGENCE     Al-Juraysi002, S.Abdulhadi380
5     Sunday 26/02/2023  11:00 - 13:30  ENCS3390           OPERATING SYSTEMS               KNH625, Masrouji014
6    Tuesday 28/02/2023  11:00 - 13:30  ENCS4370       COMPUTER ARCHITECTURE          A.Shaheen150, ALSADIK102
```
