def url_extract(raw_url):
    return "https:"+ str(str(raw_url).split(":")[2].split("->")[0]).strip('\"').replace('\"', "")