#!/usr/bin/python
# R-Finder ( File & Open Directory finder ) - R&D ICWR

import random, requests
from argparse import ArgumentParser
from multiprocessing.pool import ThreadPool

class finder:

    def useragent(self):

        arr = ["Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.0.12) Gecko/2009070611 Firefox/3.0.12 (.NET CLR 3.5.30729)", "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3", "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; ja-jp) AppleWebKit/533.16 (KHTML, like Gecko) Version/5.0 Safari/533.16", "Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0", "Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.1 (KHTML, like Gecko) Chrome/6.0.427.0 Safari/534.1"]
        return arr[random.randint(0, len(arr)-1)]

    def check(self, path):

        try:

            x = requests.get(url="{}/{}".format(self.args.target, path), headers={ "User-Agent": self.useragent() }, timeout=5)
        
            if x.status_code == 200:

                self.result += "[+] {}/{}\n".format(self.args.target, path)

        except:

            pass

    def __init__(self):

        print("[*] R-Finder Running")
        self.result = ""
        parser = ArgumentParser()
        parser.add_argument("-x", "--target", required=True)
        parser.add_argument("-w", "--wordlist", required=True)
        parser.add_argument("-t", "--thread", required=True, type=int)
        self.args = parser.parse_args()
        print("[*] Finding...\n")
        ThreadPool(self.args.thread).map(self.check, open(self.args.wordlist).read().splitlines())
        print("[*] Result:\n")

        if self.result != '':

            print(self.result)

        else:

            print("[-] No result")

finder() if __name__ == "__main__" else exit()
