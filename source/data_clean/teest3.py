import datetime
def extract_week_number(raw_date):
    year = '2018'#raw_date[:4]
    month = '02'#raw_date[5:7]
    day = '01'#raw_date[8:]
    dt = datetime.date(int(year), int(month), int(day))
    wk = dt.isocalendar()[1]
    print wk

extract_week_number('2018 04 06')