# -*- coding: utf-8 -*-
__author__ = 'florije'
import time
import datetime
# from dateutil.relativedelta import relativedelta
from relativedelta import relativedelta
import os
import json


class FetchFile(object):

    def generate_file_dict(self, appkey, product_code, start_time, end_time, path='.'):

        # todo 先生成目录,其实就是先查找目录
        dir_path_list = self.__generate_dir(start_time, end_time, path)

        need_file_names = self.__generate_file_names(appkey, product_code, start_time, end_time)
        local_files = self.__get_local_files(start_time, end_time, path)
        to_download_files = [item for item in need_file_names if not item in local_files]

        res_dict = {
            'local_dirs': dir_path_list,
            'all_files': need_file_names,
            'local_files': local_files,
            'to_down_files': to_download_files
        }
        return res_dict

    def __get_local_files(self, start_time, end_time, path='.'):
        '''

        :param start_time:
        :param end_time:
        :param path:
        :return:
        '''

        short_start_time = start_time[0:6]
        short_end_time = end_time[0:6]

        month_format_str = "%Y%m"  # 这样就足够了
        start_date = datetime.datetime.strptime(short_start_time, month_format_str)
        end_date = datetime.datetime.strptime(short_end_time, month_format_str)

        month_delta = relativedelta(months=1)
        # todo 用dir name list 来生成文件夹，首先要判断文件夹是否存在，存在就跳过，也就是continue，若不存在就创建
        res_files = []
        while start_date <= end_date:
            # todo add
            dir_name = start_date.strftime(month_format_str)
            dir_path = os.path.join(path, dir_name)

            format_str = "%Y%m%d"
            for root, dir, file in os.walk(dir_path):
                for full_name in file:
                    dat_last = full_name.split('.')
                    if len(dat_last) > 1 and dat_last[-1] == 'dat':
                        str_time = full_name.split('_')[-1].split('.')[0]
                        if datetime.datetime.strptime(start_time, format_str) <= datetime.datetime.strptime(str_time, format_str) <= datetime.datetime.strptime(end_time, format_str):
                            res_files.append(full_name)
                    else:
                        continue

            start_date = start_date + month_delta

        return res_files

    def __generate_file_names(self, appkey, product_code, start_time, end_time):
        '''
        这里是生成需要的文件
        :param appkey: 变化的appkey参数
        :param start_time: 开始时间
        :param end_time: 截止时间
        :return: list[] 返回需要下载的文件的名称
        '''
        format_str = "%Y%m%d"
        start_date = datetime.datetime.strptime(start_time, format_str)
        end_date = datetime.datetime.strptime(end_time, format_str)
        res_files = []
        if start_date == end_date:
            res_files.append('PAY_%s_%s_%s.dat' % (appkey, product_code, start_time))  # todo 返回拼接的数据
            return res_files
        delta = datetime.timedelta(days=1)
        while start_date <= end_date:
            res_files.append('PAY_%s_%s_%s.dat' % (appkey, product_code, start_date.strftime(format_str)))
            start_date = start_date + delta

        return res_files

    def __generate_dir(self, start_time, end_time, path='.'):
        '''
        生成该段时间内的文件夹，若文件夹已存在，则跳过
        :param start_time: 开始时间
        :param end_time: 结束时间
        :return:
        '''
        # todo will generate mouth_list by start_time and end_times
        # todo 处理20140701为201407
        short_start_time = start_time[0:6]
        short_end_time = end_time[0:6]

        format_str = "%Y%m"  # 这样就足够了
        start_date = datetime.datetime.strptime(short_start_time, format_str)
        end_date = datetime.datetime.strptime(short_end_time, format_str)
        print start_date, end_date

        # todo generate month name list
        month_delta = relativedelta(months=1)
        # todo 用dir name list 来生成文件夹，首先要判断文件夹是否存在，存在就跳过，也就是continue，若不存在就创建
        month_list = []
        while start_date <= end_date:

            dir_name = start_date.strftime(format_str)
            dir_path = os.path.join(path, dir_name)
            if not self.__dir_exist(dir_path):
                os.mkdir(dir_path)
            month_list.append(dir_path)
            start_date = start_date + month_delta

        return month_list

    def __dir_exist(self, dir_name):
        if not dir_name:
            raise Exception('dir_name is empty!')
        return os.path.exists(dir_name) and os.path.isdir(dir_name)


if __name__ == '__main__':
    format_str = "%Y%m%d"
    str_time = time.strftime(format_str, time.localtime())
    print str_time
    date_time = datetime.datetime.strptime(str_time, format_str)
    print date_time
    date_time2 = datetime.datetime.strptime("20140705", format_str)
    delta = datetime.timedelta(days=1)
    print date_time2 + delta

    print date_time < date_time2
    # # date to str
    # datestr = time.strftime(format, time.localtime())
    # print datestr
    # # str to date
    # t = time.strptime(datestr, "%Y-%m-%d")
    # print t
    # y, m, d = t[0:3]
    # print datetime.datetime(y, m, d)


    # print FetchFile().get_local_files('20140601', '20140705', 'data')
    # print FetchFile().generate_file_names('600016', '20140701', '20140707')
    res_dict = FetchFile().generate_file_dict('600016', '1024', '20140601', '20140715', 'data')
    res_json = json.dumps(res_dict)
    print res_json

    # print FetchFile().generate_dir('20140608', '20140701', 'data')
    path = os.path.join('.', 'data', '201407')
    for p, d, f in os.walk(path):
        for item in f:
            month_path = item.split('_')[-1].split('.')[0][0:6]
            print month_path