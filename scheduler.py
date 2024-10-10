import os
import schedule
import time

def job():
    os.system('c:/Fraud_Detection/Scripts/python.exe c:/Fraud_Detection/train_log.py --data "c:/Fraud_Detection/creditcard.csv"')

# Schedule the job every 30 days
schedule.every(30).days.do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
    
