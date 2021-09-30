import logging

import pandas as pd
import json
import pymysql
import simplejson


def excel_intoSql(filename):
    data = pd.read_excel(filename)
    result = data.values.tolist()
    db = pymysql.connect(user='root',
                         passwd='123456',
                         database='Nigeria',
                         host='192.168.124.105',
                         port=3306)
    cursor = db.cursor()
    try:
        for s in result:
            userId = s[0]
            appCount = s[1]
            # print(userId, appCount)
            # print(s[2])
            t = simplejson.loads(s[2], strict=False)
            appName = []
            packageName = []
            first = []
            last = []
            for i in range(len(t)):
                appName.append(t[i]['appName'])
                packageName.append(t[i]['packageName'])
                first.append(str(t[i]['firstInstallTime']))
                last.append(str(t[i]['lastUpdateTime']))
            name = ','.join(appName)
            package = ','.join(packageName)
            install = ','.join(first)
            update = ','.join(last)
            dataList = [userId, appCount, name, package, install, update]
            sql = "INSERT INTO App_list(user_id, app_count," \
                  "app_name, package_name, first_install, last_update) VALUES " \
                  "(%s, %s, %s, %s, %s, %s)"
            cursor.execute(sql, dataList)
            print('Insert success----------')
            db.commit()
    except Exception as e:
        print('Exception:{}'.format(e))
        logging.info(e)


if __name__ == '__main__':
    # excel_intoSql('applist.xlsx')
    data = pd.read_excel('applist.xlsx')
    result = data.values.tolist()
    db = pymysql.connect(user='root',
                         passwd='123456',
                         database='Nigeria',
                         host='192.168.124.105',
                         port=3306)
    cursor = db.cursor()
    package = []
    for s in result:
        list = json.loads(s[2])
        for i in range(len(list)):
            package.append(list[i]['packageName'])
    for i in package:
        sql = "INSERT INTO APP_packageName(package_name) VALUES (%s)"
        cursor.execute(sql, i)
        db.commit()

