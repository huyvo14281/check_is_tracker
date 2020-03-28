import dns.resolver


def dns_lookup(domain):
    list_cname = []
    query_domain: str = domain
    try:
        while True:
            cname_objs = dns.resolver.query(query_domain, 'CNAME')
            ip_addr_objs = dns.resolver.query(query_domain, 'A')

            cname_obj: dns.rdtypes.ANY.CNAME.CNAME
            ip_addr_obj: dns.rdtypes.IN.A.A

            for cname_obj in cname_objs:
                query_domain = cname_obj.to_text()

                ip_addrs: str = ''
                for ip_addr_obj in ip_addr_objs:
                    ip_addrs = ip_addrs + ip_addr_obj.to_text() + ','
                list_cname.append({'cname': cname_obj.to_text(), 'ip': ip_addrs[:-2]})

    except Exception as e:
        print('Domain: ', domain, ' stop at CNAME: ', query_domain, ' with exception:', e)

    return list_cname


if __name__ == '__main__':
    list_cname = dns_lookup('f7ds.liberation.fr')
    print(list_cname)
