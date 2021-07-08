from celery.decorators import task
from celery.utils.log import get_task_logger

from .updateScript import main

logger = get_task_logger(__name__)


@task(name="course_reg")
def course_reg_task(course, email, url, number):
    logger.info(f'Start tracking {course}')
    main(course, email, url, number)