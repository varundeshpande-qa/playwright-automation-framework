from playwright.sync_api import Page, expect


def test_saucedemo_checkout_flow(page: Page):
    page.goto("https://www.saucedemo.com/")

    # 1. Login
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

    # 2. Add to cart and go to checkout
    page.locator("[data-test='add-to-cart-sauce-labs-fleece-jacket']").click()
    page.locator("[data-test='shopping-cart-link']").click()
    page.locator("[data-test='checkout']").click()

    # 3. Fill the form
    page.locator("[data-test='firstName']").fill("John")
    page.locator("[data-test='lastName']").fill("Price")
    page.locator("[data-test='postalCode']").fill("110110")

    # 4. Finish the order
    page.locator("[data-test='continue']").click()
    page.locator("[data-test='finish']").click()
    expect(page.locator("[data-test='complete-header']")).to_have_text("Thank you for your order!")
    page.locator("[data-test='back-to-products']").click()