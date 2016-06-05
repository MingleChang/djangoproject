# -*- coding: UTF-8 -*-
import json

#status说明
#200：成功
#404：接口不存在
def apiJson(status=404,message=None,data=None,**kwargs):
	dic={'status':status,'message':message,'result':data}
	dic.update(kwargs)
	return json.dumps(dic)