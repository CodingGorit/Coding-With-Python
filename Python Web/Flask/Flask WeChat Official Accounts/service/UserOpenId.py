#!/usr/bin/python
# -*- coding: utf-8 --
#@File: UserOpenId.py
#@author: Gorit
#@contact: gorit@qq.com
#@time: 2020/3/4 15:13
from service.WxService import send_event

ls = [
        "oWDLWw-xp8otjsgA6uxdRAmI_ZjE",
        "oWDLWw9lrivntCVTPgIPkB8Vs0wc",
        "oWDLWw7g5vS2-g5ISmnSO3QDKCcs",
        "oWDLWw6vlo5tsb8s8EcuAAs8Mo30",
        "oWDLWwy8_7qcpgJB2HHT4HlYjPP8",
        "oWDLWw26XPjOgMN5lpYsE-9yu2Ds",
        "oWDLWw1MrMK3dYP1lT78CVy-71x8"
]

for i in ls:
        send_event(i)