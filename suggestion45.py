"""
建议45：序列化的另一个不错的选择--JSON
"""

import datetime
import json


class DateTimeEncoder(json.JSONEncoder):  # 对JSON进行扩展
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)


d = datetime.datetime.now()
print(json.dumps(d, cls=DateTimeEncoder))
