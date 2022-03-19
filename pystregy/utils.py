def todict(obj, classkey=None):
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