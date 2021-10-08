# ---------- Imports --------
import pandas as pd  # for our dataframes
from tabulate import tabulate  # to print tables nicely in console
from datetime import datetime  # for our date manipulation


# ---------- Constants --------
YEAR_OF_BIRTH = 'YEAR OF BIRTH'
date_format1 = '%b  %d, %Y'
date_format2 = '%B  %d, %Y'
BIRTH_DATE = 'BIRTH DATE'


# ---------- Helper Functions --------
def print_df(df):
    print(tabulate(df, headers='keys', tablefmt='psql'))

def read_date(date):
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
    return 0


def get_lived_months(birth_date, death_date):
    return 0


def get_lived_days(birth_date, death_date):
    return 0


# ----------  Logic --------
# Pulling data from CSV into a dataframe.
filename = 'U.S. Presidents Birth and Death Information - Sheet1.csv'
df = pd.read_csv(filename, skipfooter=1, engine='python')  # We skip the last row because it contains just a reference.
pd.set_option('display.max_colwidth', None)



# Calculate new variables and append them to data.
# year_of_birth
df[YEAR_OF_BIRTH] = df[BIRTH_DATE].map(lambda x: get_year_of_birth(x))
print_df(df)

# lived_years

# lived_months

# lived_days


# Find longest 10 and shortest 10 living presidents.
