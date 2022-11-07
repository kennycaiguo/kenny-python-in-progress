import gevent  # 是协程的第三方模块，需要单独安装
import requests, time

start = time.time()


def f(url):
    print('get: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s' % (len(data), url))


def main():
    gevent.joinall([
        gevent.spawn(f, 'https://www.python.org'),
        gevent.spawn(f, 'https://www.yahoo.com'),
        gevent.spawn(f, 'https://www.baidu.com'),
        gevent.spawn(f, 'https://www.sina.com.cn'),
        gevent.spawn(f, 'https://huaban.com/'),
    ])
    print("time consumed:", time.time() - start)


if __name__ == '__main__':
    main()
