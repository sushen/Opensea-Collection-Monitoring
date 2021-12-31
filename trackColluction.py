import mechanicalsoup
import pandas as pd

# role="listitem"

NFT_link = "https://opensea.io/collection/ens?tab=activity"

browser = mechanicalsoup.StatefulBrowser()

browser.open(NFT_link)

listitem = browser.page.find_all("div", attrs={"class" : "Blockreact__Block-sc-1xf18x6-0 ckZjBZ"})

distribution = [value.text for value in listitem]

print(distribution)
