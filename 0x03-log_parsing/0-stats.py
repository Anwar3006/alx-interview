import re
from collections import Counter
# open log file for reading.,


def reader(filename):
    """
    function opens log files for reading
    """
    with open(filename) as f:
        log = f.read()

        regexp_IP = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
        regexp_StatusCode = r'\bHTTP/\d\.\d"\s(\d+)'
        regexp_ResponseSize = r'\bHTTP/\d\.\d"\s\d+\s(\d+)'

        IP_list = re.findall(regexp_IP, log)
        StatusCode_list = re.findall(regexp_StatusCode, log)
        ResponseSize_list = re.findall(regexp_ResponseSize, log)

        print(IP_list)
        print(StatusCode_list)
        print(ResponseSize_list)
    
def count(ip_list):
    """
    count the occurence of ip addresses
    """
    return Counter(ip_list)


if __name__ == "__main__":
    reader('accesslog.log')
    