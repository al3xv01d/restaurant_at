from config import browser

# full == driver.maximize_window()
window_width = 768


browser_catalog = ''
if browser == 'chrome':
    browser_catalog = 'chrome'
elif browser == 'firefox':
    browser_catalog = 'firefox'


resolution_catalog = ''
if window_width == 1024:
    resolution_catalog = 'w1024'
elif window_width == 768:
    resolution_catalog = 'w768'
elif window_width == 'full':
    resolution_catalog = 'w1920'



#************************** LINKS ***********************

index = 'https://www.restaurantsupply.com/'

simple_product = 'https://www.restaurantsupply.com/san-jamar-s46tbk-46-oz-wall-mounted-bulk-liquid-soap-dispenser-black-pearl'
product_with_related = 'https://www.restaurantsupply.com/bloomfield-8774-a'

dap_on_gesture = 'https://www.restaurantsupply.com/berkel-mb-3-8'
dap_in_cart = 'https://www.restaurantsupply.com/amana-rfs18ts-medium-duty-stainless-steel-commercial-microwave-with-push-button-controls-208-230v-1800w'
dap_before_order_confirmation = 'https://www.restaurantsupply.com/manitowoc-jc-0995'

cat_tpl_1 = 'https://www.restaurantsupply.com/best-sellers'
cat_tpl_2 = 'https://www.restaurantsupply.com/storage-and-transport'
cat_tpl_3 = ''
cat_tpl_4 = ''
cat_tpl_5 = ''
cat_tpl_6 = 'https://www.restaurantsupply.com/food-preparation'
cat_tpl_7 = 'https://www.restaurantsupply.com/everpure'
cat_tpl_8 = 'https://www.restaurantsupply.com/best-selling-fryer-baskets'
cat_tpl_9 = 'https://www.restaurantsupply.com/janitorial-supplies'
cat_tpl_10 = 'https://www.restaurantsupply.com/table-mounted-stainless-steel-shelving-units'




