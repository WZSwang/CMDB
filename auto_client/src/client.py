from conf import settings
from .plugins import PluginManager
import requests
import subprocess
from concurrent.futures import ThreadPoolExecutor
class BaseClient(object):

    def __init__(self):
        self.api = settings.API

    def exec(self):
        raise NotImplementedError("必须实现exec方法")
    def post_server_info(self,server_dict):
        print(server_dict)
        response = requests.post(self.api,json=server_dict)


class AgentClient(BaseClient):

    def exec(self):
        obj = PluginManager()
        server_dict = obj.exec_plugin()




class SaltSshClient(BaseClient):



    def task(self,host):
        obj = PluginManager(host)
        server_dict = obj.exec_plugin()
        self.post_server_info(server_dict)
    def get_host_list(self):
        return ['c1.com','c2.com']


    def exec(self):
        pool = ThreadPoolExecutor(10)
        host_list = self.get_host_list()
        for host in host_list:
            pool.submit(self.task,host)







