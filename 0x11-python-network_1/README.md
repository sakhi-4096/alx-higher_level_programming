# Python - Network #1
Refers to the use of the Python programming language for tasks related to computer networking.

![Networking](https://imgs.xkcd.com/comics/python.png)

## Description
Python networking refers to the use of Python programming language to work with various networking tasks, including sending and receiving data over the internet, communicating with web services, making HTTP requests, and more. Two commonly used libraries for networking in Python are **'urllib'** and **'requests'**.

## Features
 * **Socket Programming:** Python's built-in socket library allows you to create and manage network sockets for various protocols like TCP and UDP. You can use sockets to implement network clients and servers, enabling communication over a network.
 * **HTTP Requests:** Python provides libraries like requests that simplify making HTTP requests to web servers. These libraries are commonly used to fetch web pages, interact with REST APIs, and perform web scraping.
 * **Network Protocol Implementation:** Python allows you to implement custom network protocols and applications. You can create servers and clients for specific protocols, handle data transmission, and define communication rules.
 * **Network Scanning and Analysis:** Python is used for network scanning and analysis, including tasks like port scanning, network monitoring, packet capture, and network device configuration.
 * **Network Security:** Python is often used for tasks related to network security, such as penetration testing, vulnerability scanning, and security analysis.
 * **Network Automation:** Python is a popular choice for automating network-related tasks, such as configuring network devices (e.g., routers and switches), managing network resources, and provisioning network services.
 * **File Transfer:** Python can be used for transferring files between systems using protocols like FTP, SFTP (SSH File Transfer Protocol), and SCP (Secure Copy Protocol).
 * **Web Servers:** Python can be used to create web servers using frameworks like Flask and Django, allowing you to build dynamic web applications and RESTful APIs.
 * **Network Monitoring:** Python is used for network monitoring and alerting by collecting and analyzing network performance data.
 * **IoT (Internet of Things):** Python is commonly used for IoT devices and applications, where network connectivity and communication play a crucial role in connecting devices to the internet.

## Usage
```py
# urlib
import urllib.request

response = urllib.request.urlopen('https://sakhile.tech')
html = response.read()
print(html)

# requests
import requests

response = requests.get('https://sakhile.tech')
if response.status_code == 200:
    print(response.text)

```
## Credits
 * [HTTP (HyperText Transfer Protocol)](https://www3.ntu.edu.sg/home/ehchua/programming/webprogramming/HTTP_Basics.html)
 * [Using HTTP cookies](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies)
 * [HOWTO Fetch Internet Resources Using urllib Package](https://docs.python.org/3/howto/urllib2.html)
 * [Quickstart with Requests package](https://requests.readthedocs.io/en/latest/)
 * [Requests package](https://pypi.org/project/requests/)

## Contact
 * [Sakhile Ndlazi](https://www.twitter.com/sakhilelindah)
