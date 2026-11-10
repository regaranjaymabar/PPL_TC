from selenium.webdriver.support import expected_conditions as EC

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


class TestInventory:
    """Kasus uji alur inventori dan keranjang belanja."""

    def test_tc_inv_01_add_backpack_to_cart(self, driver):
        """Memastikan badge keranjang bertambah setelah Backpack ditambahkan."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.add_backpack_to_cart()

        assert inventory_page.get_cart_badge_count() == "1"

    def test_tc_inv_02_sort_name_z_to_a(self, driver):
        """Memastikan produk terurut berdasarkan nama dari Z ke A."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.select_sort_option("za")
        inventory_page.wait.until(
            EC.text_to_be_present_in_element(
                InventoryPage.FIRST_PRODUCT_NAME,
                "Test.allTheThings() T-Shirt (Red)",
            )
        )

        assert inventory_page.get_first_product_name() == "Test.allTheThings() T-Shirt (Red)"

    def test_tc_inv_03_sort_price_low_to_high(self, driver):
        """Memastikan produk terurut berdasarkan harga dari rendah ke tinggi."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.select_sort_option("lohi")
        inventory_page.wait.until(
            EC.text_to_be_present_in_element(
                InventoryPage.FIRST_PRODUCT_NAME,
                "Sauce Labs Onesie",
            )
        )

        assert inventory_page.get_first_product_name() == "Sauce Labs Onesie"

    def test_tc_inv_04_verify_dashboard_loaded(self, driver):
        """Memastikan logo dan kontainer produk inventori berhasil dimuat."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)

        assert login_page.is_dashboard_displayed() is True
        assert inventory_page.get_first_product_name() == "Sauce Labs Backpack"

    def test_tc_inv_05_logout_from_inventory(self, driver):
        """Memastikan logout mengembalikan pengguna ke halaman login."""
        login_page = LoginPage(driver)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory_page = InventoryPage(driver)
        inventory_page.logout()

        login_page.wait.until(EC.url_to_be(LoginPage.URL))
        assert login_page.get_current_url() == LoginPage.URL
        assert login_page.find_element(LoginPage.LOGIN_BUTTON).is_displayed()
