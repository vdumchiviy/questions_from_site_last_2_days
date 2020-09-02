import requests
from datetime import datetime, timedelta
import time


def main2():
    startdate = datetime.now() - timedelta(days=2)
    print(startdate)
    seconds = int(time.mktime(startdate.timetuple()))
    print(seconds)
    print(time.ctime(seconds,))


def read_page(from_date, to_date, page_number, questions):
    result = 0
    parameters = {"pagesize": 100,
                  "page": page_number,
                  "order": "desc",
                  "sort": "creation",
                  "tagged": "python",
                  "site": "stackoverflow",
                  "fromdate": int(time.mktime(from_date.timetuple())),
                  "todate": int(time.mktime(to_date.timetuple()))
                  }
    response = requests.get(
        url="https://api.stackexchange.com/2.2/search?", params=parameters)
    counter = len(questions) - 1
    if response.status_code == 200:
        if response.json()["has_more"] is True:
            result = page_number + 1
        items = response.json()["items"]
        for item in items:
            counter += 1
            questions[counter] = {"date": time.ctime(item["creation_date"]),
                                  "title": item["title"]}

    return result


def main():
    to_date = datetime.now()
    from_date = to_date - timedelta(days=2)
    questions = dict()

    page_number = 1
    while page_number != 0:
        page_number = read_page(from_date, to_date, page_number, questions)

    for key, value in questions.items():
        print(str(key+1), ":", value["date"], value["title"])


main()
