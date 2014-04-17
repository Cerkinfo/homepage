from ci.fortunes.models import Fortune
fortunes = open('CI.utf8.txt').read()[3:-4].split('\n\n%\n\n')
for t in fortunes:
    f = Fortune(text=t)
    f.save()

