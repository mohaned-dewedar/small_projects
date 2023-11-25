from playwright.sync_api import sync_playwright
import time
import pandas as pd
def run(playwright):
    browser = playwright.chromium.launch(headless=False)  # Set headless=False to see the browser
    page = browser.new_page()

    # Navigate to the Forbes Middle East Top 100 Arab Celebrities page
    page.goto('https://www.forbesmiddleeast.com/list/the-top-100-arab-celebrities')

    # Keep clicking the 'Load More' button until it no longer exists
    while True:
        # Check if the 'Load More' button is present
        time.sleep(2)
        load_more_button = page.locator('text=Load More')
        if load_more_button.is_visible():
            # Click the 'Load More' button
            load_more_button.click()
            # Wait for the network to be idle after clicking
            page.wait_for_load_state('networkidle')
        else:
            # Break out of the loop if the button is no longer present
            break

    # Extracting the data into lists
    names = page.locator("td:nth-child(3)").all_text_contents()
    professions = page.locator("td:nth-child(4)").all_text_contents()
    countries = page.locator("td:nth-child(5)").all_text_contents()
    followings = page.locator("td:nth-child(6)").all_text_contents()
    print(f"Names: {len(names)}, Professions: {len(professions)}, Countries: {len(countries)}, Followings: {len(followings)}")

    # Close the browser
    browser.close()

    # Creating a pandas DataFrame
    data = {
        'Name': names,
        'Profession': professions,
        'Country': countries,
        'Following': followings
    }
    df = pd.DataFrame(data)

    # Close the browser
    input("Press Enter to close the browser")  # This will keep the browser open until you press Enter
    browser.close()
    return df

with sync_playwright() as playwright:
   dataframe = run(playwright) 

dataframe.to_csv("celebrities.csv", index=False)
