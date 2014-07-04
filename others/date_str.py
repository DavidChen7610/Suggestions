# -*- coding: utf-8 -*-
__author__ = 'florije'
import time
import datetime
import os


class FetchFile(object):

    def generate_file_dict(self, appkey, start_time, end_time, path='.'):
        need_file_names = self.__generate_file_names(appkey, start_time, end_time)
        local_files = self.__get_local_files(start_time, end_time, path)
        to_download_files = [item for item in need_file_names if not item in local_files]

        res_dict = {
            'local_files': local_files,
            'all_files': need_file_names,
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
        res_files = []
        format_str = "%Y%m%d"
        for p, d, f in os.walk(path):
            for full_name in f:
                str_time = full_name.split('_')[-1].split('.')[0]
                if datetime.datetime.strptime(start_time, format_str) <= datetime.datetime.strptime(str_time,
                                                                                                    format_str) <= datetime.datetime.strptime(
                        end_time, format_str):
                    res_files.append(full_name)

        return res_files

    def __generate_file_names(self, appkey, start_time, end_time):
        '''
        这里是生成需要的文件
        :param appkey: 变化的appkey参数
        :param start_time: 开始时间
        :param end_time: 截止时间
        :return: list[] 返回需要下载的文件的名称
        '''
        start_date = datetime.datetime.strptime(start_time, format_str)
        end_date = datetime.datetime.strptime(end_time, format_str)
        res_files = []
        if start_date == end_date:
            res_files.append('PAY_%s_1024_%s.dat' % (appkey, start_time))  # todo 返回拼接的数据
            return res_files
        delta = datetime.timedelta(days=1)
        while start_date <= end_date:
            res_files.append('PAY_%s_1024_%s.dat' % (appkey, start_date.strftime(format_str)))
            start_date = start_date + delta

        return res_files


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
    print FetchFile().generate_file_dict('600016', '20140701', '20140715', 'data')