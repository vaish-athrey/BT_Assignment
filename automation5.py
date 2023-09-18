from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.bt.com/")



# Handle Cookie Pop-up
try:
    cookie_popup = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/script[9]"))
    )
    cookie_popup.click()
except Exception as e:
    print("Cookie pop-up not found or could not be closed:", e)




# try:
#     cookie_popup = WebDriverWait(driver, 40).until(
#         EC.presence_of_element_located((By.ID, "cookieMainHeader"))
#     )
#     # Check if the cookie pop-up is displayed, and if so, click it
#     if cookie_popup.is_displayed():
#         cookie_popup.click()
# except Exception as e:
#     print("Cookie pop-up not found or could not be closed:", e)




# try:
#     # Switch to the iframe containing the cookie pop-up
#     iframe = WebDriverWait(driver, 20).until(
#         EC.presence_of_element_located((By.ID, "pop-frame06184624057374639"))
#     )
#     driver.switch_to.frame(iframe)
    
#     # Find and close the cookie pop-up
#     cookie_popup = WebDriverWait(driver, 20).until(
#         EC.element_to_be_clickable((By.ID, "cookiePolicyAnchor"))
#     )
#     cookie_popup.click()
    
#     # Switch back to the default content
#     driver.switch_to.default_content()
# except Exception as e:
#     print("Cookie pop-up not found or could not be closed:", e)


# Hover to Mobile Menu and Select Mobile Phones
mobile_menu = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/header/div[2]/div[2]/div/div[1]/div[1]/ul/li[4]"))
)
ActionChains(driver).move_to_element(mobile_menu).perform()

mobile_phones_link = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/div/header/div[2]/div[2]/div/div[1]/div[1]/ul/li[4]/ul/li/ul/li[2]"))
)
mobile_phones_link.click()



# Verify the Number of Banners
# banners = WebDriverWait(driver, 20).until(
#     EC.presence_of_all_elements_located((By.XPATH, "/html/body/div/main/div/div/div[5]"))
# )
# if len(banners) < 3:
#     print("Error: Less than 3 banners found")




# Locate the container containing banners using XPath
# banner_container = WebDriverWait(driver, 40).until(
#     EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div/div[5]"))
# )

# # Wait for banners within the container to be present using XPath
# banners = WebDriverWait(banner_container, 40).until(
#     EC.presence_of_all_elements_located((By.XPATH, "./html/body/div/main/div/div/div[5]"))
# )

# # Verify the Number of Banners within the Container
# if len(banners) < 3:
#     print("Error: Less than 3 banners found within the container")


# Locate the container containing banners using XPath
banner_container = WebDriverWait(driver, 50).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div/div[5]"))
)

# Use JavaScript to scroll to the container
driver.execute_script("arguments[0].scrollIntoView();", banner_container)

# Wait for banners within the container to be present using XPath
banners = WebDriverWait(banner_container, 200).until(
    EC.presence_of_all_elements_located((By.XPATH, "./html/body/div/main/div/div/div[5]"))
)

# Verify the Number of Banners within the Container
if len(banners) < 3:
    print("Error: Less than 3 banners found within the container")


# Scroll Down and Click View SIM Only Deals
driver.execute_script("window.scrollBy(0, 300);")
view_sim_deals_button = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div/div[5]/div[2]/div[1]/div/div/div/div[2]/div/div[3]/a"))
)
view_sim_deals_button.click()



# Validate the Title for the New Page
expected_title = "SIM Only Deals | Compare SIMO Plans & Contracts | BT Mobile"
if expected_title not in driver.title:
    print("Error: Title validation failed")



# Validate "30% off and double data" Details
# plan_details_element = WebDriverWait(driver, 40).until(
#     EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div/div[4]/div[2]/div/div[2]/div[3]"))
# )
# plan_details_text = plan_details_element.text
# expected_details = "Expected details"
# if expected_details not in plan_details_text:
#     print("Error: Details validation failed")




    
# Locate the element containing the plan details using XPath
plan_details_element = WebDriverWait(driver, 40).until(
    EC.presence_of_element_located((By.XPATH, "/html/body/div/main/div/div/div[4]/div[2]/div/div[2]/div[3][contains(text(), '30% off and double data was 125GB 250GB Essential Plan, was £27 £18.90 per month')]"))
)

# Get the text content of the element
plan_details_text = plan_details_element.text

# Expected details
expected_details = "30% off and double data was 125GB 250GB Essential Plan, was £27 £18.90 per month"

# Validate the details
if expected_details in plan_details_text:
    print("Details validation passed")
else:
    print("Error: Details validation failed")



# Close the Browser and Exit
driver.quit()

