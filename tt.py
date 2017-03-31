
from pages.admin_product_page import AdminProductPage
from app.tools import get,find, Wait




a = AdminProductPage()
#
a.login()
get('http://dev.restaurantsupply.com/restaura_admin/catalog/product/new/set/4/type/simple/')
Wait.invisible('//div[@class="admin__form-loading-mask"]')
# a.open_all_collapsed_settings()
#
# a.product_name.clear()
# a.product_name.send_keys('dddddddd')
#
# a.original_product_name.clear()
# a.original_product_name.send_keys('dddddddd')
#
# # a.open_price.click()
# a.price.clear()
# a.price.send_keys('155')
#
# a.internal_id_magento.send_keys('1dddddddd55')
# a.export_description.send_keys('1dddddddd55')

a.enable_all_switchers()


#a.wd.quit()