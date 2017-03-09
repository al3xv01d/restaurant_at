from config import browser, base_url

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

index = base_url + '/'

simple_product = base_url + '/san-jamar-s46tbk-46-oz-wall-mounted-bulk-liquid-soap-dispenser-black-pearl'
product_with_related = base_url + '/bloomfield-8774-a'

dap_on_gesture = base_url + '/berkel-mb-3-8'
dap_in_cart = base_url + '/amana-rfs18ts-medium-duty-stainless-steel-commercial-microwave-with-push-button-controls-208-230v-1800w'
dap_before_order_confirmation = base_url + '/manitowoc-jc-0995'

cat_tpl_1 = base_url + '/best-sellers'
cat_tpl_2 = base_url + '/storage-and-transport'
cat_tpl_3 = ''
cat_tpl_4 = ''
cat_tpl_5 = ''
cat_tpl_6 = base_url + '/food-preparation'
cat_tpl_7 = base_url + '/everpure'
cat_tpl_8 = base_url + '/best-selling-fryer-baskets'
cat_tpl_9 = base_url + '/janitorial-supplies'
cat_tpl_10 = base_url + '/table-mounted-stainless-steel-shelving-units'



