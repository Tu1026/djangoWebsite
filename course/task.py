from celery.utils.log import get_task_logger
from djangoWebsite.celery import app
from .updateScript import main
#from celery.contrib import rdb
logger = get_task_logger(__name__)


@app.task()
def course_reg_task(course, email, url, number):
    logger.info(f'Start tracking {course}')
    ### using telnet to debug celery
    # rdb.set_trace()
    main(course, email, url, number)
    
@app.task()
def test(a , b):
    print(a+b)