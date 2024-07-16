import subprocess
import csv
import mysql.connector
from dotenv import load_dotenv
import os
import datetime


load_dotenv()





def run_speedtest():
    result = subprocess.run(["speedtest-cli", "--csv"], capture_output=True, text=True)
    data = result.stdout.strip().split(',')
    columns = ["Server ID","Sponsor","Server Name","Timestamp","Distance","Ping","Download","Upload","Share","IP Address"]    
    output = {}
    for idx, d in enumerate(data):
        if idx == 0 :
            output[columns[idx]] = int(d)
        elif idx == 3:
            datetime_obj = datetime.datetime.fromisoformat(d[:-1])  # Remove 'Z'
            output[columns[idx]] = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        elif idx == 4 or idx == 5 or idx == 6 or idx == 7:
            output[columns[idx]] = float(d)
        else:
            output[columns[idx]] = d
    return output  # Get the first (and only) row as a dictionary

def insert_into_mysql(result):
    mydb = mysql.connector.connect(
        host=os.getenv('DBHOST'),  
        user=os.getenv('DBUSER'),
        password=os.getenv('DBPASS'),
        database=os.getenv('DBNAME')
    )

    cursor = mydb.cursor()
    
    # Exclude 'share' column since we aren't using it
    columns = ["Server ID","Sponsor","Server Name","Timestamp","Distance","Ping","Download","Upload","Share","IP Address"]
    columnss = ["Server_ID","Sponsor","Server_Name","Timestamp","Distance","Ping","Download","Upload","Share","IP_Address"]
    values = [result[col] for col in columns]  # Extract values in the correct order

    sql = "INSERT INTO bandwidth ({}) VALUES ({})".format(
        ", ".join(columnss), ", ".join(["%s"] * len(columns))  # Placeholders for values
    )
    cursor.execute(sql, values)
    mydb.commit()

    cursor.close()
    mydb.close()

if __name__ == "__main__":
    result = run_speedtest()
    insert_into_mysql(result)
