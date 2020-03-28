import re


def convert_long_url_to_domain(long_url: str) -> str:
    url_short: list = re.findall('^https?://.*/', long_url)

    if len(url_short) > 0:
        url_short: str = url_short[0]
        domain = url_short.replace('https://', '').replace('http://', '')
        domain = domain[0:domain.index('/')]
        return domain
    else: return url_short


if __name__ == '__main__':
    url_long = 'https://0klxjejyxak3.com/pixel/purs?tmpl=70&bv=20.2.v.2'
    domain = convert_long_url_to_domain(url_long)
    print(domain)
