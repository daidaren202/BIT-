#coding:utf-8
import requests
from lxml import etree
import time
import json
import ctypes
i = 1
while i:
	i+=1
	#i-=1
	#print '\a'
	time.sleep(1)
	url = 'http://jwms.bit.edu.cn/jsxsd/xsxkkc/xsxkGgxxkxk?kcxx=&skls=&skxq=&skjc=&sfym=true&sfct=true&szjylb=&kcxz=06&kcgs=2'
		   #http://jwms.bit.edu.cn/jsxsd/xsxkkc/xsxkGgxxkxk?kcxx=&skls=&skxq=&skjc=&sfym=false&sfct=true&szjylb=&kcxz=06&kcgs=2
	headers = {
		'Cookie':'JSESSIONID=jwms1~B644EBA395B3A78269DC02D2B7CE7E48',
		'Connection': 'keep-alive',
		'Host': 'jwms.bit.edu.cn',
		'Origin': 'http://jwms.bit.edu.cn',
		'Referer': 'http://jwms.bit.edu.cn/jsxsd/xsxkkc/comeInGgxxkxk',
		'X-Requested-With': 'XMLHttpRequest'
		#'User-Agent':' Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
	}

	params = {
		#'kcxx': '',
		#'skls': '',
		#'skxq': '',
		#'skjc': '',
		'sfym': 'false',
		'sfct': 'true',
		'szjylb': '',
		'kcxz': 06,
		'kcgs': 2,
	}
	data = {
		'sEcho': 1,
		'iColumns': 14,
		#'sColumns': '',
		'iDisplayStart': 0,
		'iDisplayLength': 15,
		'mDataProp_0': 'kch',
		'mDataProp_1': 'kcmc',
		'mDataProp_2': 'bhbm',
		'mDataProp_3': 'kcsxmc',
		'mDataProp_4': 'kcgsmc',
		'mDataProp_5': 'szkcflmc',
		'mDataProp_6': 'xf',
		'mDataProp_7': 'skls',
		'mDataProp_8': 'sksj',
		'mDataProp_9': 'skdd',
		'mDataProp_10': 'xkrs',
		'mDataProp_11': 'syrs',
		'mDataProp_12': 'ctsm',
		'mDataProp_13': 'czOper',
	}
	try:
		r = requests.post(url, headers=headers, data=data)
		content = r.content
		dic = json.loads(content)
		iTotalRecords = dic['iTotalRecords']

		if iTotalRecords > 0:
			print u'\n\n\n有课啦！！！\n\n\n'
			ctypes.windll.user32.MessageBoxA(0,u"有课啦！！！".encode('gb2312'),u' 提示'.encode('gb2312'),0)

		else:
			if i%60 == 0:
				print 'No',
			pass
	except:
		print 'failed	',