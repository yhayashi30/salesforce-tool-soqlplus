from simple_salesforce import Salesforce

import configparser

# login function
def login():
    ini = configparser.ConfigParser()
    ini.read('./config.ini', 'UTF-8')
    username = ini['connect_info']['username']
    password = ini['connect_info']['password']
    organizationid = ini['connect_info']['organizationId']
    print("[username]" + username)
    return Salesforce(username=username, password=password, organizationId=organizationid)

# execQuery function
def execQuery(sf, query):
    result = sf.query(query)
    print("[totalSize]:" + str(result["totalSize"]))
    if result["totalSize"] > 0:
        return result["records"]
    else:
        return ""

# parseResult function
def parseResult(records):
    headerPrintFlg = False
    headerList = []
    recordValList = []
    for record in records:
        recordVal = ""
        for key,val in record.items():
            if key != "attributes":
                if not headerPrintFlg:
                    headerList.append(key)
                recordVal += str(val) + ','

        if not headerPrintFlg:
            headerPrintFlg = True
        recordVal = recordVal[:-1]
        recordValList.append(recordVal)

    print("[result]")
    # print header
    print(",".join(headerList))
    # print recordVal
    for recordVal in recordValList:
        print(recordVal)

if __name__ == "__main__":
    print("[start]")
    sf = login()
    query = input("[Please input query]:")
    records = execQuery(sf, query)
    parseResult(records)
    print("[end]")