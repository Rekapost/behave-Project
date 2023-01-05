Feature: orangeHRM Logo
   Scenario: Logo Presence on orangeHRM page
     Given Launch Chrome browser
     When open orangeHRM page
     Then verify that the logo present on page
     And close browser
