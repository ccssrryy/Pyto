"""
Save values on disk

This module makes possible to save values on disk. Values are shared between the Today Widget and the main app.
Values are stored in a JSON dictionary, so it's not possible to save every type of data.
"""

try:
    from rubicon.objc.api import ObjCClass, NSString
    import json

    NSUserDefaults = ObjCClass("NSUserDefaults")
    userDefaults = NSUserDefaults.alloc().initWithSuiteName("group.pyto")

    if userDefaults.valueForKey("userKeys") is None:
        userDefaults.setValue("{}", forKey="userKeys")
except (NameError, ValueError):
    pass


def __dictionary__():
    return json.loads(str(userDefaults.valueForKey("userKeys")))


def get(key: str):
    """
    Returns the value stored with the given key.

    :param key: The key identifying the value.
    """

    return __dictionary__()[key]


def delete(key: str):
    """
    Deletes the value stored with the given key.

    :param key: The key identifying the value to delete.
    """

    dictionary = __dictionary__()
    del dictionary[key]
    _json = NSString.alloc().initWithUTF8String(json.dumps(dictionary).encode("utf-8"))
    userDefaults.setValue(_json, forKey="userKeys")
    _json.release()


def set(value, key: str):
    """
    Adds the given value to the database with the given key.

    :param value: A JSON compatible value.
    :param key: The key identifying the value.
    """

    dictionary = __dictionary__()
    dictionary[key] = value
    _json = NSString.alloc().initWithUTF8String(json.dumps(dictionary).encode("utf-8"))
    userDefaults.setValue(_json, forKey="userKeys")
    _json.release()
