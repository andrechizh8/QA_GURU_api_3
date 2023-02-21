import os
from selene.support.shared import browser
from selene import have
import allure
from allure import step
from dotenv import load_dotenv


load_dotenv()


def test_login(browser_auth):
    browser.open("")

    with allure.step("Check successful login"):
        browser_auth.element(".account").should(have.exact_text("andrechizh.ru@yandex.ru"))


def test_add_product_to_cart(browser_auth, demoshop):
    browser.open("")

    with allure.step("Check successful add to cart"):
        demoshop.post("addproducttocart/details/45/1")
        browser.open("cart")
        browser.element("[class='product-name']").should(have.exact_text("Fiction"))


def test_delete_product_from_cart(browser_auth, demoshop):
    browser.open("")
    demoshop.post("addproducttocart/details/45/1")

    with allure.step("Check successful delete from cart"):
        browser.element("[class='ico-cart']").click()
        browser.element("[name='removefromcart']").click()
        browser.element("[name='updatecart']").click()
        browser.element("[class='order-summary-content']").should(have.exact_text("Your Shopping Cart is empty!"))


def test_add_product_to_wishlist(browser_auth, demoshop):
    browser.open("")

    with allure.step("Check successful add to wishlist"):
        demoshop.post("addproducttocart/details/53/2")
        browser.open("wishlist")
        browser.element("[class='product']").should(have.exact_text("3rd Album"))


def test_delete_product_from_wishlist(browser_auth, demoshop):
    browser.open("")
    demoshop.post("addproducttocart/details/53/2")

    with allure.step("Check successful delete from wishlist"):
        browser.element("[class='ico-wishlist']").click()
        browser.element("[name='removefromcart']").click()
        browser.element("[name='updatecart']").click()
        browser.element("[class='wishlist-content']").should(have.exact_text("The wishlist is empty!"))


def test_successful_logout(browser_auth):
    browser.open("")

    with allure.step("Check sucessful logout"):
        browser.element("[class='ico-logout'").click()
        browser.element("[class='ico-register'").should(have.exact_text("Register"))
