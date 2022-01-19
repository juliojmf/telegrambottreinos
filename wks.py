import gspread

WKTS_WEEK_CELL = "G2"
WKTS_MONTH_CELL = "H2"
WKTS_YEAR_CELL = "I2"

sa = gspread.service_account(filename="") #your google account api key json file
sh = sa.open("Treinos 2022")


class Worksheet:
    def __init__(self, user_name):
        self.wks = sh.worksheet(user_name)
        self.week_wkts = self.wks.acell(WKTS_WEEK_CELL).value
        self.month_wkts = self.wks.acell(WKTS_MONTH_CELL).value
        self.year_wkts = self.wks.acell(WKTS_YEAR_CELL).value

    def addworkout(self, workout):
        self.wks.append_row(workout)
