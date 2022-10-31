import shutil
import zipfile as zf
import tarfile as tf


def shutil_demo1():
    # shutil.copyfile('test.html','test1.html')
    # shutil.copy('test.html','test2.html')
    # shutil.copy('dogcr.gif','dc.gif')
    # shutil.copy2('test.html', 'dir1/t.html')
    # 递归拷贝拷贝一个目录里面是所有文件到另外一个目录
    # shutil.copytree('dir1', 'dir2', symlinks=False, ignore=None)
    # 递归的去删除文件
    # shutil.rmtree('dir2')
    # 制作压缩文件：参数1：压缩文件名称，参数2：压缩文件类型，参数3：需要压缩的目录路径
    # shutil.make_archive('dir1_arch','zip',r'./dir1/')  # 将当前目录下面的dir1文件夹压缩为dir1_arch.zip文件保存在当前目录下面
    # 解压缩文件
    shutil.unpack_archive('dir1_arch.zip', 'dir1_arch', 'zip')


def test_zf_pack():
    z = zf.ZipFile('test.zip', 'w')  # 创建压缩文件对象
    z.write('hello.txt')
    z.write('hello1.txt')
    z.write('hello2.txt')
    z.write('dc.gif')
    z.write('t.html')
    z.close()
    print('finished...')


def test_zf_unpack():
    z = zf.ZipFile('test.zip', 'r')
    z.extractall(path='test_exat')
    z.close()


def test_tar_pack():
    t = tf.TarFile('dir_tar.tar', 'w')
    t.add('test.html')
    t.add('test1.html')
    t.add('test2.html')
    t.add('dogcr.gif')
    t.close()


def test_tar_unpack():
    t = tf.TarFile('dir_tar.tar', 'r')
    t.extractall(path='tar_file')
    t.close()


if __name__ == '__main__':
    # shutil_demo1()
    # test_zf_pack()
    # test_zf_unpack()
    # test_tar_pack()
    test_tar_unpack()
