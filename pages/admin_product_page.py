from pages.admin_base_page import AdminBasePage
from app.tools import find


class AdminProductPage(AdminBasePage):

    switcher_lo = '//div[@class="admin__actions-switch"]'
    collapsed_setting_lo = '//div[@class="fieldset-wrapper admin__collapsible-block-wrapper"]'

    product_name_lo = '//input[@name="product[name]"]'

    sku_lo = '//input[@name="product[sku]"]'
    original_product_name_lo = '//input[@name="product[orig_name]"]'

    price_lo = '//input[@name="product[price]"]'

    internal_id_magento_lo = '//input[@name="product[internal_id_magento]"]'

    export_description_lo = '//textarea[@name="product[export_description]"]'
    # --------------------------------  ACTIONS ------------------------------------------------------------------

    def open_all_collapsed_settings(self):

        all_collapsed_settings = self.wd.find_elements_by_xpath(self.collapsed_setting_lo)

        for setting in all_collapsed_settings:
            setting.click()

    def enable_all_switchers(self):

        all_awitchers = self.wd.find_elements_by_xpath(self.switcher_lo)

        for switcher in all_awitchers:
            switcher.click()


    # -------------------------------- ELEMENTS -------------------------------------
    @property
    def product_name(self):
        return find(self.product_name_lo)

    @property
    def sku(self):
        return find(self.sku_lo)

    @property
    def original_product_name(self):
        return find(self.original_product_name_lo)

    @property
    def price(self):
        return find(self.price_lo)

    @property
    def internal_id_magento(self):
        return find(self.internal_id_magento_lo)

    @property
    def export_description(self):
        return find(self.export_description_lo)
