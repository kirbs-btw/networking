import os
import threading
from queue import Queue
import time
import subprocess

queue = Queue()
open_domain = []


f = open('words.txt')
domain_list = []
for i in f:
    domain_list.append(i[0:-1].lower())

print(len(domain_list))

def pingDomain(domain):
    command = "nslookup {}.com".format(domain)
    command_output = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    return command_output


def fill_queue(domain_list):
    for i in domain_list:
        queue.put(i)

def worker():
    while not queue.empty():
        domain = queue.get()
        command_output = pingDomain(domain)
        print(command_output)
        if 'Non-existent domain' in str(command_output):
            print(f"Domain {domain}.com is not in use")
            open_domain.append(domain)
        else:
            print(f"Domain {domain}.com is already used")

fill_queue(domain_list)

thread_list = []

if __name__ == '__main__':

    for t in range(10):
        thread = threading.Thread(target=worker)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print(open_domain)