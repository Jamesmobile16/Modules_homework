from datetime import datetime

import worldometer

from application.salary import calculate_salary as sal

from application.db.people import  get_employees as emp

if __name__ == "__main__":
    sal()
    emp()
    print(datetime.now().date())
    print(worldometer.cigarettes_smoked_today())