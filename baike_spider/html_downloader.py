import urllib

class HtmlDownloader(object):

    def download(self,url):
        if url is None:
            return None

        response=urllib.request.urlopen(url)

        if response.getCode()!=200:
            return None

        return response.read()