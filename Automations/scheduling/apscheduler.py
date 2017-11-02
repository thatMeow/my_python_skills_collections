from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()

def my_job():
    print ("Print upon schedule")
    
scheduler.add_job(my_job, trigger='cron', hour='*', minute='*', second='*')
scheduler.start()
