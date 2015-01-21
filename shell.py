"""
Creates shell using IPython
"""
import sys

from werkzeug import script

from rb_apps_admin.api import *

def make_shell():
    try:
        config = sys.argv[1]
    except IndexError:
        config = "settings.cfg"
    app, db = create_app()
    return dict(app=app, db=db)

if __name__ == "__main__":

    script.make_shell(make_shell, use_ipython=True)()