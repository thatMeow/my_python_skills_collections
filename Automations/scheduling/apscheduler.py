from apscheduler.schedulers.background import BackgroundScheduler
scheduler = BackgroundScheduler()

def my_job():
    print ("Print upon schedule")
    
scheduler.add_job(my_job, trigger='cron', hour='*', minute='*', second='*')
scheduler.start()


# If the function has parameters, use scheduler.add_job(lambda my_job(parameter_1, parameter_2), \
#                                       trigger='cron', hour='*', minute='*', second='*')
