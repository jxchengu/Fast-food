from playwright.sync_api import sync_playwright # Imports the core function to run Playwright in Python

with sync_playwright() as p: # Sets up the Playwright environment and assigns it to 'p'
    broswer = p.chromium.launch(headless=False) # Launches a new, visible browser window (headless=false) does not hide the browser window
    page = broswer.new_page()  # Creates a new tab or page within the browser

      # Navigates the browser to the specified URL and waits for the page to load
    page.goto("https://www.qsrmagazine.com/story/top-50-fast-food-chains-ranked-2025/")
    
    # skip header
    rows = page.query_selector_all("table tr")[1:]

    # Loops through each row in the 'rows' list
    for row in rows:
        # Finds all the table data (<td>) cells within the current row
        cols = row.query_selector_all("td")
        # Extracts the text from each cell, removes extra whitespace, and stores it in a list
        data = [col.text_content().strip() for col in cols]
        # Prints the list of extracted data for the current row
        print(data)

    broswer.close()





























    from playwright.sync_api import sync_playwright 

with sync_playwright() as p: 
    broswer = p.chromium.launch(headless=False) 
    page = broswer.new_page()  


    page.goto("https://www.qsrmagazine.com/story/top-50-fast-food-chains-ranked-2025/")
    
    rows = page.query_selector_all("table tr")[1:]


    for row in rows:

        cols = row.query_selector_all("td")

        data = [col.text_content().strip() for col in cols]

        print(data)

    broswer.close()