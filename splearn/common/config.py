# -*- coding: utf-8 -*-

import threading

config = {}

config_lock = threading.Lock()

no_default = 'no_default'


class set(object):
    '''note'''

    def __init__(self, arg=None, config=config, lock=config_lock, **kwargs):
        if arg and not kwargs:
            kwargs = arg
        with lock:
            self.config = config
            self.old = {}
            for key, value in kwargs.items():
                self._assign(key.split('.'), value, config, old=self.old)

    def _assign(self, keys, value, d, old=None, path=[]):
        if len(keys) == 1:
            if old is not None:
                path_key = tuple(path + [keys[0]])
                if keys[0] in d:
                    old[path_key] = d[keys[0]]
                else:
                    old[path_key] = '--delete--'
            d[keys[0]] = value
        else:
            key = keys[0]
            if key not in d:
                d[key] = {}
                if old is not None:
                    old[tuple(path + [key])] = '--delete--'
                old = None
            else:
                raise KeyError("The key has been used")
            # recurrence
            self._assign(keys[1:], value, d[key], old, path + [key])

    def __enter__(self):
        return self.config

    def __exit__(self, exc_type, exc_val, exc_tb):
        for keys, value in self.old.items():
            if value == '--delete--':
                d = self.config
                try:
                    while len(keys) > 1:
                        d = d[keys[0]]
                        keys = keys[1:]
                    del d[keys[0]]
                except KeyError:
                    pass
            else:
                self._assign(keys, value, self.congfig)


def get(key, default=no_default, config=config):
    keys = key.split('.')
    result = config
    for k in keys:
        try:
            result = result[k]
        except (TypeError, IndexError, KeyError):
            if default is not no_default:
                return default
            else:
                raise
    return result
