from . import global_settings
import os
import importlib


class Settings(object):
    """
    获取默认和自定义的配置信息
    """
    def __init__(self):

        for item in dir(global_settings):
            if item.isupper():
                k = item
                v = getattr(global_settings, item)
                setattr(self, k, v)
        setting_path = os.environ.get('AUTO_CLIENT_SETTINGS')
        mode_settings = importlib.import_module(setting_path)
        for item in dir(mode_settings):
            if item.isupper():
                k = item
                v = getattr(mode_settings, k)
                setattr(self, k, v)


settings = Settings()
