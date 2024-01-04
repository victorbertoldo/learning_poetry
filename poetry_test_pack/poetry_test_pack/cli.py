from httpx import get


def cli():
    print(
        get(
            'http://httpbin.org/get?arg=Poetry test'
        ).json()['args']['arg']
    )