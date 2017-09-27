import subprocess
import importlib
from lib.config import settings
import traceback
import paramiko


class PluginManager(object):
    """
    三种模式选择
    """

    def __init__(self, hostname=None):
        self.hostname = hostname
        self.plugin_items = settings.PLUGIN_ITEMS
        self.mode = settings.MODE
        self.test = settings.TEST
        if self.mode == "SSH":
            self.ssh_user = settings.SSH_USER
            self.ssh_post = settings.SSH_POST
            self.ssh_pwd = settings.SSH_PWD

    def exec_plugin(self):
        server_info = {}
        for k, v in self.plugin_items.items():
            info = {"status": True, "data": None, "msg": None}
            try:
                module_path, cls_name = v.rsplit(".", maxsplit=1)
                # print(module_path,cls_name)
                module_list = importlib.import_module(module_path)
                cls = getattr(module_list, cls_name)

                if hasattr(cls, "initial"):
                    obj = cls.initial()
                else:
                    obj = cls()
                ret = obj.process(self.exec_cmd, self.test)
                info['data'] = ret
            except Exception as e:

                info['status'] = False
                info['msg'] = traceback.format_exc()
            server_info[k] = info
        return server_info

    def exec_cmd(self, cmd):
        if self.mode == "AGENT":

            result = subprocess.getoutput(cmd)
        elif self.mode == "SSH":

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(hostname=self.hostname,
                        port=self.ssh_post,
                        username=self.ssh_user,
                        password=self.ssh_pwd
                        )
            stdin, stdout, stderr = ssh.exec_command(cmd)
            result = stdout.read()
            ssh.close()
        elif self.mode == "SALT":
            result = subprocess.getoutput("salt '%s' cmd.run '%s'" % (self.hostname, cmd))
        else:
            raise Exception("模式选择错误：只能选择一下模式：AGENT,SSH,SALT")
        return result
