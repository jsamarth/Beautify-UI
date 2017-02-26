import urllib2
import bs4

link = "http://www.mashawigrill.com/"

# Return the soup
def url_to_soup(url):
    # bgp.he.net filters based on user-agent.
    f = urllib2.urlopen(link)
    soup = bs4.BeautifulSoup(f.read(), "html.parser")
    return soup

# soup = url_to_soup(link)



#
# 
# 
# 
# 
# 
# 
# 
# 
# title
# div = []
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 


