import re

def is_tracker(domain:str,
               block_domain: str):
    result = re.findall('.*({})$'.format(block_domain + '.'), domain)

    if len(result) == 0:
        return False

    return True


if __name__ == '__main__':
    string = 'track.adformnet.akadns.net'
    block_domain = 'techsolutions.com.tw'
    result = is_tracker(domain=string,
                        block_domain=block_domain)
    print(result)