from pv.models import PV
import os
import os.path
import datetime

memdir = "/home/_WWW/www.cerkinfo.be/ci.media/pv"

for cyear in os.listdir(memdir):
    d = os.path.join(memdir, cyear)
    if os.path.isdir(d):
        for f in  os.listdir(d):
            if f.endswith(".pdf") or f.endswith(".rtf"):
                print "%s/%s" % (d,f)
		basename = f.split('.')[0]
		tokens = basename.split('-')
		if len(tokens) == 4:
			year, month, day, reunion_type = tokens
		else:
			year, month, day = tokens
			reunion_type = ''
			

                pv = PV()
                pv.date = datetime.date(int(year), int(month), int(day))
                pv.reunion_type =  reunion_type
		pv.year = cyear
                pv.pvfile = os.path.join('pv', cyear, f)

		if pv.date > datetime.date(2010,10,25):
			print pv
			print pv.pvfile
			print "save"
                	pv.save()

