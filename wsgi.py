import os, sys
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, os.path.join(ROOT_DIR,"www/lib/python2.7/site-packages"))

sys.path.append(ROOT_DIR)

sys.path.append(os.path.join(ROOT_DIR,"vmaig_blog"))

os.environ.setdefault("DJANGO_SETTINGS_MODULE",  "vmaig_blog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
