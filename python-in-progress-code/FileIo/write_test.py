# 以字符形式写
def write_demo_str_w():
    file = open("test.txt", 'w', encoding='utf-8')
    len = file.write('人生苦短，好好爱你的女人，多多...')
    print(len)
    file.close()

def write_demo_str_a():  # 追加
    file = open("test.txt", 'a', encoding='utf-8')
    len = file.write('人生苦短，好好爱你的女人，多多...\n')
    print(len)
    file.close()

# 以二进制方式写,str右encode方法，byte右decode方法不要搞错了
def write_demo_str_wb():
    file = open("testb.txt", 'wb')
    content = '人生苦短，好好爱你的女人，多多...\n'.encode('utf-8')  # 字符串以二进制写入，必须先编码，否则文件里面是乱码
    len = file.write(content)
    print(len)
    file.close()

def write_demo_str_ab():
    file = open("testb.txt", 'ab')
    content = '人生苦短，好好爱你的女人，多多...爱爱\n'.encode('utf-8')  # 字符串以二进制写入，必须先编码，否则文件里面是乱码
    len = file.write(content)
    print(len)
    file.close()

if __name__ == '__main__':
    # write_demo_str_w()
    # write_demo_str_a()
    # write_demo_str_wb()
    write_demo_str_ab()
