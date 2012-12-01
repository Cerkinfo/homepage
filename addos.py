from ci.os.models import OS
import os
import os.path
import datetime

memdir = "/home/_WWW/test.cerkinfo.be/ci.media/OS"

for cyear in os.listdir(memdir):
    d = os.path.join(memdir, cyear)
    if os.path.isdir(d):
        for f in  os.listdir(d):
            if f.endswith(".pdf"):
                print "%s/%s" % (d,f)
		basename = f.split('.')[0]
		tokens = basename.split('_')
		if len(tokens) == 3:
			year, num, name = tokens
		else:
			raise Exception("Cannot parse %s" % (f))	
		if cyear != year:
			raise Exception("Date in folder different than date in file %s/%s" % (cyear, f))

                os_ = OS()
                os_.comiteyear = year
                os_.title =  name
		os_.numero = num
                os_.fileobj = os.path.join('OS', cyear, f)
		print os_
		print os_.fileobj

                os_.save()

