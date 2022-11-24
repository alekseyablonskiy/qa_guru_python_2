from selene.support.shared import browser
from selene import be, have


def test_positive_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI'))


def test_negative_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('olnbghuiol').press_enter()
    browser.element('p[aria-level="3"]').should(have.text('Па запыце olnbghuiol нічога не знойдзена'))

