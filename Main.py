import requests
import webbrowser
from selenium import webdriver
from bs4 import BeautifulSoup


url = "https://www.fido.ca/phones"


site = requests.get(url)
chromedriver = r"C:\Users\gopal\AppData\Local\Programs\Python\Python38-32"
driver = webdriver.chrome(chromedriver)
driver.get(url)
r = requests.get(url)

session = requests.session()
session.trust_env = False
response = session.get(url)



# htmlContent = r.content

# soup = BeautifulSoup(htmlContent, 'html.parser')

# para = soup.find('dir="auto"').get_text()
# t = soup.title
# print(para)
# product count --- smartphone count (product name)
# if # product name (<p class="text-title-5 "></p>  )
    
    # if # view details click (<span class="ds-button__copy text-button text-nowrap ds-no-overflow mw-100"> VIEW DETAILS </span>)
      # TITLE    <h1 _ngcontent-bfa-rcom-ct-fido-c7="" class="mt-56" id="bfa-page-title">Samsung Galaxy Note20 Ultra 5G</h1>
      
     #FOR COLOR OPTION # <span class="dsa-selection__input d-inline-block ds-color-white" style="background: rgb(30, 33, 33);"></span>
    
     # <span class="dsa-selection__caption text-center sr-only -absolute" data-caption="Black">Black</span>
      # OR
      # <span class="dsa-selection__caption text-center sr-only -absolute" data-caption="Copper">Copper</span> 
      # 
      # FOR STORAGE 
      # <span aria-hidden="true" class="dsa-selection__label ds-no-overflow text-body mb-0 d-inline-block w-100 py-12 px-16 px-md-24"><span class="dsa-selection__input d-inline-block ds-color-white fds-icon-check"></span><span class="dsa-selection__caption text-center" data-caption="128 GB">128 GB</span><div></div></span>
      # <span class="dsa-selection__caption text-center" data-caption="128 GB">128 GB</span>
      # 
      # FOR FULL PRICE

      # <div class="ds-price__amountDollars ng-star-inserted"> 1,020 </div>

      # FOR MONTHLY PRICE 
    # <p _ngcontent-bfa-rcom-ct-fido-c7="" class="text-body mb-0 text-semi ds-color-red ng-star-inserted">$33.33/mo.<sup>±</sup></p>
    #  
    # TIME STAMP 





    
          
        # if # check storage option 

