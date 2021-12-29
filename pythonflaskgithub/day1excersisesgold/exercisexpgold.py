from flask import Flask
from datetime import datetime, date
from flask import render_template_string, render_template
app = Flask(__name__)


@app.route("/main")
def main(date1 = None,time = None):
    time_now = date.today()
    now = datetime.now()
    string_current_hour = now.strftime("%H")
    current_hour = int(string_current_hour)
    if 8 <= current_hour <= 13:
        return render_template('timepage.html',date1 = time_now, time = 'Good morning')
    elif 14 <= current_hour <= 17:
        return render_template('timepage.html', date1 =time_now, time='Good afternoon')
    elif 18 <= current_hour <= 21:
        return render_template('timepage.html', date1 =time_now, time='Good evening')
    else:
        return render_template('timepage.html', date1=time_now, time='Good night')

@app.route("/main/date")
def main_time(today_date = None, count_days = None):
    today_date = datetime.now()
    new_year_date = datetime(year = 2022, month = 1,day = 1, hour = 0, minute = 0, second= 0)
    final_time = new_year_date - today_date
    return render_template('countdown.html',today_date = today_date, count_days = final_time)

@app.route("/main/birthday")
def birthday(birthdate_time = None, minutes_passed = None):
    birthdate = datetime(year = 1993, month = 4,day = 22, hour = 6, minute = 13, second= 0)
    today_date = datetime.today()
    final_time = today_date - birthdate
    final_seconds = final_time.total_seconds()
    final_minutes = final_seconds // 60
    return render_template('birthday.html', birthdate_time = birthdate, minutes_passed = final_minutes)
if __name__ == "__main__":
    app.run(debug=True,port=5000)