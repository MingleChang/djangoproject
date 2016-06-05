# -*- coding: UTF-8 -*-
import json


def apiJson(status=404,message=None,data=None,**kwargs):
	dic={'status':status,'message':message,'result':data}
	dic.update(kwargs)
	return json.dumps(dic)