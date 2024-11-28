from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')


@when('Search for tea')
def search_product(context):
    context.driver.find_element(By.ID, 'search').send_keys('tea')
    context.driver.find_element(By.XPATH, "//button[@data-test='@web/Search/SearchButton']").click()
    sleep(5)


@then('Verify search results shown')
def verify_search_results(context):
    expected_result = 'tea'
    actual_result = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'


@when('Click on cart icon')
def search_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(5)


@then('Verify “Your cart is empty” message is shown')
def verify_cart_empty(context):
    expected_result='Your cart is empty'
    actual_result=context.driver.find_element(By.CSS_SELECTOR, "[data-test='boxEmptyMsg']").text
    assert expected_result in actual_result, f'Expected text {expected_result} not in actual {actual_result}'
    context.driver.quit()


@when('Click on sign in icon on top navigation menu')
def search_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/AccountLink']").click()
    sleep(5)


@when('Click on sign in button from right side navigation menu')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then("Verify 'Sign in' form is shown")
def verify_sign_in(context):
    expected_result = 'Create your Target account'
    actual_result = context.driver.find_element(By.CSS_SELECTOR, "#createAccount").text
    assert expected_result in actual_result, f'actual text {actual_result} not in expected result {expected_result}'
    context.driver.quit()