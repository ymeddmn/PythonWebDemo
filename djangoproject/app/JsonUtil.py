# -*- coding:utf8 -*-
import json


def models2list(objs):
    '''''把数据库查询出来的model对象列表转换为字典列表'''
    obj_arr = []
    for o in objs:
        # 把Object对象转换成Dict
        dict = {}
        dict.update(o.__dict__)
        dict.pop("_state", None)  # 去除掉多余的字段
        obj_arr.append(dict)
    return obj_arr


def jsontobean(jsons):
    '''
    Json转数据类型
    :param jsons: 
    :return: 
    '''
    return json.loads(jsons)


def beandict2json(dicts):
    """
    字典转jsonObject
    :param dicts: 
    :return: 
    """
    if isinstance(dicts, dict):
        return json.dumps(dicts)
    else:
        return json.dumps(dicts.__dict__)


def list2json(lists):
    '''
    list转jsonArray
    :param lists: 
    :return: 
    '''
    if isinstance(lists, list):  # 判断是否是list
        return json.dumps(lists)
    else:
        return json.dumps(list(lists))


def toJson(code, body, isModel=True):
    if isModel:
        return toResultJson(code=code, body=models2list(body))
    else:
        return toResultJson(code=code, body=body)


def toResultJson(code, body, msg):
    '''
    转Json返回码对象
    :param code: 
    :param body: 
    :return: 
    '''
    return json.dumps(ResultJSON(code=code, msg=msg, body=list(body)).__dict__, ensure_ascii=False)


class ResultJSON():
    '''
    结果对象
    '''

    def __init__(self, code, msg, body):
        self.code = code
        self.body = body
        self.msg = msg
