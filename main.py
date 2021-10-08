# ---------- Imports --------
import math
import pandas as pd  # for our dataframes
from tabulate import tabulate  # to print tables nicely in console
from datetime import datetime  # for our date manipulation


# ---------- Constants --------
NAN = math.nan
YEAR_OF_BIRTH = 'YEAR OF BIRTH'
date_format1 = '%b  %d, %Y'
date_format2 = '%B  %d, %Y'
BIRTH_DATE = 'BIRTH DATE'
DEATH_DATE = 'DEATH DATE'
DAYS_LIVED = 'DAYS LIVED'
YEARS_LIVED = 'YEARS LIVED'
MONTHS_LIVED = 'MONTHS LIVED'
PRESIDENT = 'PRESIDENT'

# ---------- Helper Functions --------
def print_df(df):
    print(tabulate(df, headers='keys', tablefmt='psql'))

def read_date(date):
    if isinstance(date, float) and math.isnan(date):
        return datetime.today()

    # Helps parse dates, which come in two different formats.
    # source: https://www.codegrepper.com/code-examples/python/strftime+python+multiple+formats
    for fmt in (date_format1, date_format2):
        try:
            return datetime.strptime(date, fmt)
        except ValueError:
            pass
    raise ValueError('no valid date format found')


def get_year_of_birth(birth_date):
    date = read_date(birth_date)
    return date.year

def get_lived_years(birth_date, death_date):
    bd = read_date(birth_date)
    dd = read_date(death_date)
    return (dd.year - bd.year)



def get_lived_months(birth_date, death_date):
    bd = read_date(birth_date)
    dd = read_date(death_date)
    return (dd.year - bd.year) * 12 + (dd.month - bd.month)

def get_lived_days(birth_date, death_date):
    bd = read_date(birth_date)
    dd = read_date(death_date)
    return (dd - bd).days

# ----------  Logic --------
# Pulling data from CSV into a dataframe.
filename = 'U.S. Presidents Birth and Death Information - Sheet1.csv'
df = pd.read_csv(filename, skipfooter=1, engine='python')  # We skip the last row because it contains just a reference.
pd.set_option('display.max_colwidth', None)



# Calculate new variables and append them to data.
# year_of_birth
df[YEAR_OF_BIRTH] = df[BIRTH_DATE].map(lambda x: get_year_of_birth(x))

# lived_years
df[YEARS_LIVED] = df.apply(
    lambda row:
        get_lived_years(row[BIRTH_DATE], row[DEATH_DATE])
    , axis=1)

# lived_months
df[MONTHS_LIVED] = df.apply(
    lambda row:
        get_lived_months(row[BIRTH_DATE], row[DEATH_DATE])
    , axis=1)

# lived_days
df[DAYS_LIVED] = df.apply(
    lambda row:
        get_lived_days(row[BIRTH_DATE], row[DEATH_DATE])
    , axis=1)


# Find longest 10 and shortest 10 living presidents.
livingDaysAscending = df.sort_values(by=DAYS_LIVED, ascending=False).head(10)
print('The 10 longest living presidents are: ')
print_df(livingDaysAscending[[PRESIDENT, DAYS_LIVED]])
print('')

livingDaysDescending = df.sort_values(by=DAYS_LIVED, ascending=True).head(10)
print('The 10 shortest living presidents are: ')
print_df(livingDaysDescending[[PRESIDENT, DAYS_LIVED]])
print('')
