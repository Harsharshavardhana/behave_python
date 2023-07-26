
Feature: This feature will be used to test the login functionality of Simplilearn application
  Scenario: Validate the Login success scenario
    Given I have launched the application
    Then  I should enter the swags lab page
    Given i should enter the username
    Given i should enter the password
    Then  click login button
    Then  I should land on home page
    Given I have quit the application

