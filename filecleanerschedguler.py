import schedule
import time
import filecleaner  
def job():
    filecleaner.run()  

schedule.every().day.at("07:30:00").do(job)

print("File cleaner script running. Press Ctrl+C to exit.")
while True:
    schedule.run_pending()
    time.sleep(1)
