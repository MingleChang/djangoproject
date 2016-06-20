# -*- coding: UTF-8 -*-
import json

CODE_SUCCESS=200
CODE_NOT_FOUND=404
CODE_SERVER_ERROR=500
CODE_PARAM_ERROR=501
CODE_DATA_ERROR=502

#status说明
#200：成功
#404：接口不存在
def apiJson(status=CODE_NOT_FOUND,message=None,data=None,**kwargs):
	dic={'status':status,'message':message,'result':data}
	dic.update(kwargs)
	return json.dumps(dic)