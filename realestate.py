import pandas
from time import sleep
from DrissionPage import ChromiumPage
page = ChromiumPage()


daataInside = []
def save_csv(data):
    daataInside.append(data)
    df=pandas.DataFrame(daataInside,columns=["AgentName","AgentPhone","Address","SoldDate","Price","Property_url"])
    df.to_csv('realestate.csv',index=False)


def childLinks():
    childLink = []
    page.get('https://www.realestate.com.au/sold/in-northern+queensland+-+region,+qld/list-1?source=refinement')
    # while True:
    links = page.eles('xpath://h2//a[@class="details-link residential-card__details-link"]')
    for post in links:
        childLink.append(post.attrs['href'])
        # try:stoper = page.ele('xpath://nav[@aria-label="Pagination Navigation"]//a[@title="Go to Next Page"]').click()
        # except:stoper = ''
        # sleep(2)
        # if stoper == '':
        #     break
    return childLink


def scrapStart():
    for childUrl in childLinks():
        page.get(f'https://www.realestate.com.au{childUrl}')
        sleep(1)
        agentName = page.ele('xpath://div[@class="agent-info__contact-info"]//a').text.strip()
        agentPhone = page.ele('xpath://div[@class="agent-info__contact-info"]//div[@class="phone"]/a').attrs['href'].replace('tel:','')
        address = page.ele('xpath://div[@class="sidebar-traffic-driver__detail-info"]').text.strip()
        soldDate = page.ele('xpath://div[@class="property-info__middle-content"]//span[contains(text(),"Sold")]').text.strip()
        price = page.ele('xpath://div[@class="property-info__middle-content"]//span[@class="property-price property-info__price"]').text.strip()
        Property_url = page.url
        row = [agentName,agentPhone,address,soldDate,price,Property_url]
        print(row)
        save_csv(row)
scrapStart()