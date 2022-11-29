import schedule
import time
import datetime

def Fun():
    print("Inside Fun")

def main():
    print("Inside Task Scheduler")
    schedule.every(1).minutes.do(Fun)
    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()