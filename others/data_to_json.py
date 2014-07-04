# -*- coding: utf-8 -*-
__author__ = 'florije'
import os
import json


class DataUtility(object):
    def dat_to_dict(self, file_name, file_path='.'):
        '''

        :param file_name:
        :param file_path:
        :return:
        '''

        res_dict = {
            'num': 0,
            'data': []
        }
        full_file_name = os.path.join(file_path, file_name)
        if not os.path.exists(full_file_name):
            return json.dumps(res_dict)

        with open(full_file_name, 'r') as file:
            for line in file:
                line_data = line.strip('\n').split('|')
                if len(line_data) == 1:
                    res_dict['num'] = int(line_data[0])
                else:
                    tmp_data = {'appkey': line_data[0], 'channel': line_data[1], 'product_code': line_data[2],
                                'order_code': line_data[3], 's_order_code': line_data[4],
                                's_merchant_code': line_data[5], 's_order_amount': line_data[6],
                                's_refund_amount': line_data[7], 's_shipment_type': line_data[8],
                                'status': line_data[9], 'paychannel': line_data[10], 'ext_account': line_data[11],
                                'usercode': line_data[12], 'settle_time': line_data[13], 'batch_no': line_data[14]}
                    res_dict['data'].append(tmp_data)
        return json.dumps(res_dict)


if __name__ == '__main__':
    print DataUtility().dat_to_dict('data.dat')

