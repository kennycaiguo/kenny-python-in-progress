"""
StringIO只能存储字符串，遇到从网络下载的图片视频等Bytes类型的内容就不行了，需要用到专门存储Bytes类型的BytesIO对象。

其用法和StringIO大同小异。
内存IO的应用场景之一就是和数据库打交道，如上传图片等等，尽量避免频繁操作数据库引起数据库宕机
"""
from io import BytesIO


def ByteIO_demo1():
    content = '''
     StringIO is a type of menIO
     it works just like a file
     it can write data to memory
     and it can also read data from it 
     '''
    with BytesIO() as bio:
        c = bio.write(content.encode('utf-8'))
        print('%d byte writed...' % c)
        print(bio.getvalue().decode('utf-8'))


def ByteIO_to_file():
    content = '''StringIO is a type of menIO
      it works just like a file
      it can write data to memory
      and it can also read data from it 
      '''
    with BytesIO() as bio, open('byteio.txt', 'w', encoding='utf-8') as dst:
        c = bio.write(content.encode('utf-8'))
        bio.seek(0)
        data = bio.readline()
        while data:
            dst.write(data.decode('utf-8').strip() + '\n')
            data = bio.readline()
        print("finished...")


def file_to_ByteIO(filename):
    with open(filename, 'r', encoding='utf-8') as f, BytesIO() as bio:
        data_str = f.readline()
        while data_str:
            bio.write(data_str.encode('utf-8'))
            data_str = f.readline()
        print("=====================load finished=============")
        print(bio.getvalue().decode('utf-8'))
        print("=====================end============================")


if __name__ == '__main__':
    # ByteIO_demo1()
    # ByteIO_to_file()
    file_to_ByteIO('byteio.txt')
