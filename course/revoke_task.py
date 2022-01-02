from djangoWebsite.celery import app
import sys
if __main__ == "__main__":
    app.control.revoke(sys.argv[0],terminate=True, signal='SIGKILL')