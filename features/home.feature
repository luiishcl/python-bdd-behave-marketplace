Feature: Test BEES Home Web Page
  As a BEES user,
  I want to acess the page,
  So I can manager the inventory.

  # The "@" annotations are tags
  # One feature can have multiple scenarios
  # The lines immediately after the feature title are just comments

  Scenario: Access Homepage
    Given the TestBees home page is displayed
    When do login 
      """
        { 
          "email": "luishcl@outlook.com",
          "password": "1Bees-pass2"
        }
      """
    Then should present "Welcome to your storage"