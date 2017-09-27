import requests
import os, sys,json
from conf import settings
BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASEDIR)
os.environ["AUTO_CLIENT_SETTINGS"] = "conf.settings"
from src import plugins

from src import client
from src import script
if __name__ == '__main__':
    script.start()



    # obj = plugins.PluginManager()
    # server_dict = obj.exec_plugin()
    # a =json.dumps(server_dict)
    # requests.post(url=settings.API,data={"a":a})
    # print(a)
    # print(type(a))
    # print(server_dict)
