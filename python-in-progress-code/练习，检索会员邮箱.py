# 分割一个字符串获取邮箱地址，将每一个邮箱地址分割位用户名和域名两个部分，再把这些数据放到一个字典在，key是域名，value是用户列表，即相同域名的用户放
# 在同一个列表中

def get_members(info: str):
    # 分割出邮箱地址
    mailaddrs = info.split(',')
    # print(mailaddrs)
    member = {}
    g_list = []
    o_list = []
    q_list = []
    for m in mailaddrs:
        mail = m.split('@')
        user = mail[0]
        domain = mail[1]
        if domain == 'gmail.com':
            g_list.append(user)
            member[domain] = g_list
        elif domain == 'outlook.com':
            o_list.append(user)
            member[domain] = o_list
        else:
            q_list.append(user)
            member[domain] = q_list
    # print(member)
    return member


def get_domains(info: str):
    domain_list = []
    mailaddrs = info.split(',')
    for m in mailaddrs:
        mail = m.split('@')
        domain_list.append(mail[1])
    domain_list = list(set(domain_list))
    # print(domain_list)
    return domain_list


def get_members2(info):
    mail_addr = info.split(',')
    member = {}
    for m in mail_addr:
        mail = m.split('@')
        user = mail[0]
        domain = mail[1]
        u = member.get(domain, [])  # 刚开始字典是空的，没有数据,注意这里的意思，如果字典有值就返回该值，如果没有就返回[],
        if len(u) == 0:  # 长度==0 说明没有这个key，需要添加这个key
            u.append(user)
            member[domain] = u
        else:  # 有key，直接将用户添加到key对应列表
            u.append(user)

    return member


if __name__ == '__main__':
    msg = 'may@qq.com,kenny123@gmail.com,jack@outlook.com,majack@qq.com,w123@gmail.com,bili123@outlook.com,sexy123@qq.com'
    # data = get_members(msg)
    # print(data)
    # print(get_domains(msg))
    print(get_members2(msg))
