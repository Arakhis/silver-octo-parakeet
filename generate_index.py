from horo import gen_prom, times, advices, promises
from datetime import datetime as dt

def generate_page(head, body, footer):
	page = ("<html>" + head + body + footer + "</html>")
	return page

def generate_body(paragraphs):
	body = ("<h2>Еще один гороскоп</h2>")
	i = 0
	while i < len(paragraphs):
		body += ("<p>" + paragraphs[i] + "</p>")
		i = i + 1
	return "<body>" + body + "</body>"

def generate_head(title, fst_header):
	head = ("<meta charset='utf-8'>" + "<h1>{1}</h1>" + "<title>{0}</title>").format(title, fst_header)
	return "<head>" + head + "</head>"

def generate_number(amount):
	number = ("")
	am = 0
	while am < amount:
		number += generate_body(paragraphs)
		am = am + 1
	return "<body>" + number + "</body>"

footer = "<footer><a href='/about.html'>О чем все это?</a></footer>"
paragraphs = gen_prom
head = (generate_head("Гороскоп для всех", "Гороскоп на " + str(dt.now().date())))
body = (generate_number(3))
fp = open("index.html", "w")
print(generate_page(head, body, footer), file=fp)
fp.close()

def generate_about(heada, bodya, footera):
	about = "<html>{0}{1}{2}</html>".format(heada, bodya, footera)
	return about

def generate_lists(sp_name, sp_items):
	lst = "sp_name" + "<ul>"
	f = 0
	while f < len(sp_items):
		lst += "<li>" + sp_items[f] + "</li>"
		f = f + 1
	return body + "</ul>"

sp1 = generate_lists("<li>Times</li>", times)
sp2 = generate_lists("<li>Advices</li>", advices)
sp3 = generate_lists("<li>Promises</li>", promises)

def generate_genlist(spi1, spi2, spi3):
	genlist = "<ol>{0}{1}{2}</ol>".format(spi1,spi2,spi3)
	return "<body>" + genlist + "</body>"

abody = generate_genlist(sp1, sp2, sp3)
ahead = "<title>{tit}</title><img src='/zodiac.jpeg' height='100' width='100'>".format(tit='О чем все это?')
afooter = "<a href='/index.html'>Вернуться на главную</a>"
ap = open("about.html", "w")
print(generate_about(ahead, abody, afooter), file=ap)
ap.close()


