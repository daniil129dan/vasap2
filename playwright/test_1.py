import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)#

    page = context.new_page()
    page.goto("http://127.0.0.1:8000/polls/")
    page.get_by_role("link", name="http://127.0.0.1:8000/api/questions/").click()
    page.goto("http://127.0.0.1:8000/api/")
    page.get_by_role("link", name="http://127.0.0.1:8000/api/choices/").click()
    page.goto("http://127.0.0.1:8000/api/")
    page.get_by_role("link", name="http://127.0.0.1:8000/api/questions/").click()
    page.goto("http://127.0.0.1:8000/")

    context.tracing.stop(path = "trace.zip")#
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
