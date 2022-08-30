import re


def remove_url_anchor(url):
    if "#" in url:
        result = re.findall(r'.*' + '#', url)[0][:-1]
        print(result)
        return result
    else:
        print(url)
        return url
    pass


assert remove_url_anchor("lms.ithillel.ua#about") == "lms.ithillel.ua"
assert remove_url_anchor("lms.ithillel.ua/groups/?page=1#example") == "lms.ithillel.ua/groups/?page=1"
assert remove_url_anchor("lms.ithillel.ua/groups/") == "lms.ithillel.ua/groups/"


