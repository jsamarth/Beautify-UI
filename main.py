from flask import *
import urllib2
import bs4
app = Flask(__name__)

info = {
}

soup = ""

# Return the links and the texts of the nav bar of the page
def setCarousel():
	global soup
	global info
	carouselMain = soup.find_all("div", id="homepage-slider")
	carouselChildren = carouselMain[0].contents
	info['carousel'] = [0, 1]
	print info['carousel']
	for carItem in carouselChildren:
		print str(carItem.src)
		src = str(carItem['src'])
		alt = str(carItem['alt'])

		cardict = {}
		cardict['src'] = src
		listdict['alt'] = alt
		info['carousel'].append(cardict)


# Return the links and the texts of the nav bar of the page
def setMenu():
	global soup
	global info
	listitems = soup.find_all("li", "menu-item-type-post_type", limit = 5)
	info['menu'] = []
	for listitem in listitems:
		link = str(listitem.a['href'])
		text = str(listitem.a.i.string)

		listdict = {}
		listdict['link'] = link
		listdict['text'] = text
		info['menu'].append(listdict)


# Return the title of the page
def setTitle():
	global soup
	global info
	info['title'] = str(soup.title.string)


# Return the logo of the page
def setLogo():
	global soup
	global info
	info['logo'] = str(soup.find_all("div", "logo")[0].a.img['src'])


# Return the soup
def url_to_soup(url):
    # bgp.he.net filters based on user-agent.
    f = urllib2.urlopen(url)
    global soup
    soup = bs4.BeautifulSoup(f.read(), "html.parser")





####################### Routes
@app.route('/')
def homePage():
	return render_template('index.html')


@app.route('/check', methods = ['POST', 'GET'])
def getNewLink():
	inputurl = ""
	if request.method == 'POST':
		inputurl = request.form['url']
	else:
		inputurl = request.args.get('url')

	# set the link in the info dictionary
	global info
	info['link'] = inputurl

	url_to_soup(str(inputurl))

	setTitle()
	setLogo()
	setMenu()
	setCarousel()

	return render_template("newpage.html", input=info)


if __name__ == '__main__':
	app.run()