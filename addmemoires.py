from memoires.models import Memoire
import os
import os.path

#  mv teheux.pdf.txt teheux.pdf.txt.utf8
# iconv -o teheux.pdf.txt --t iso-8859-15 teheux.pdf.txt.utf8 
# rm teheux.pdf.txt.utf8
memdir = "/home/_WWW/test.cerkinfo.be/ci.media/memoires"

for year in os.listdir(memdir):
    d = os.path.join(memdir, year)
    if os.path.isdir(d):
        for f in  os.listdir(d):
            if f.endswith(".pdf"):
                print "%s/%s" % (d,f)
                desc = open("%s/%s.txt" % (d,f)).read()
                desc = unicode(desc, 'iso-8859-15')
                desc = desc.split('\n')
                author = desc[0]
                subject = desc[1]

                m = Memoire()
                m.author = author
                m.year = year
                m.subject = subject
                m.fileobj = os.path.join('memoires', year, f)

                m.save()

