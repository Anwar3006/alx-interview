import re
from collections import Counter


filename = ''
def reader(filename):
    """
    function opens log files for reading
    """
    with open(filename) as f:
        log = f.read()
        return log


def count(list):
    """
    count the occurence of items in list; return a dictionary
    """
    return Counter(list)


def perform_regex(regexp):
    """
    perform regex on file
    """
    readFile = reader(filename)
    return re.findall(regexp, readFile)


def get_status_code():
    """
    get the Response size from the log file
    """
    regexp_StatusCode = r'\bHTTP/\d\.\d"\s(\d+)'
    StatusCode_list = perform_regex(regexp_StatusCode)
    result = count(StatusCode_list)

    for key in result:
        print(f"{key}: {result[key]}")


def get_response_size():
    """
    get the Response size from the log file
    """
    regexp_ResponseSize = r'\bHTTP/\d\.\d"\s\d+\s(\d+)'
    ResponseSize_list = perform_regex(regexp_ResponseSize)

    result = 0
    for item in ResponseSize_list:
        result += int(item)
        print(result)



if __name__ == "__main__":
    filename = 'apachelog.log'
    reader(filename)
    # get_response_size()

    get_status_code()
