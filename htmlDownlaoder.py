import urllib.request

def html_downloader(URL,file_name):
    try:
        url = urllib.request.urlopen(URL)
        content = url.read()
        url.close()
        html_file = open("{}.html".format(file_name),"wb")
        html_file.write(content)
        html_file.close()
        print("Your file {}.html has been created".format(file_name))
    except Exception as e:
        print(e)

html_downloader("https://www.python.org/","python_website")