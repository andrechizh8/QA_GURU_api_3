import os
import pytest
from utils.base_session import BaseSession
from dotenv import load_dotenv
from selene.support.shared import browser
from allure import step

load_dotenv()
browser.config.base_url = "https://demowebshop.tricentis.com/"


@pytest.fixture(scope="session")
def demoshop():
    demoshop_session = BaseSession(os.getenv("API_URL"))
    return demoshop_session


@pytest.fixture(scope="session")
def reqres():
    reqres_session = BaseSession(os.getenv("REQ_URL"))
    return reqres_session


@pytest.fixture(scope="session")
def browser_auth(demoshop):
    response = demoshop.post("login", json=

    {
        "Email": os.getenv("EMAIL"),
        "Password": os.getenv("PASSWORD")
    },
                             allow_redirects=False
                             )
    auth_cookie = response.cookies.get("NOPCOMMERCE.AUTH")

    with step("Assert status code"):
        response.status_code = 302

    browser.open("Themes/DefaultClean/Content/images/star-x-active.png")
    browser.driver.add_cookie({"name": "NOPCOMMERCE.AUTH", "value": auth_cookie})
    return browser
