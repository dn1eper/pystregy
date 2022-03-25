import os, shutil
import json
from datetime import datetime, date

def todict(obj: object, classkey: str=None):
    if hasattr(obj, "__dict__"):
        data = {}
        for (k, v) in obj.__dict__.items():
            data[k] = todict(v, classkey)
        return data
    if hasattr(obj, "_asdict"):
        return dict(obj._asdict())
    elif hasattr(obj, "__iter__") and not isinstance(obj, str):
        return [todict(v, classkey) for v in obj]
    else:
        return obj

def tojson(obj: object):
    def json_serial(obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        raise TypeError ("Type %s not serializable" % type(obj))

    return json.dumps(obj, default=json_serial)

def clear_dir(dir_path: str):
    for filename in os.listdir(dir_path):
        file_path = os.path.join(dir_path, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))