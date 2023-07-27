
Feature: This feature will be used to test the login functionality of Simplilearn application
  Scenario: Validate the Login success scenario
    Given I have launched the application
    Then  I should enter the swags lab page
    Given i should enter the username as "standard_user"
    Given i should enter the password as "secret_sauce"
    Then  click login button
    Then  I should land on home page validate login successfully
    Given I have quit the application

  Scenario Outline: Validate the Login failure scenario
    Given I have launched the application
    Then  I should enter the swags lab page
    Given i should enter the username as "<UserName>"
    Given i should enter the password as "<Password>"
    Then  click login button
    Then  I should land on home page validate login unsuccessfully "<Error>
    Examples:
      | UserName        | Password     | Error                                                                    |
      | standard_user   | 12345        | Epic sadface: Username and password do not match any user in this service|
      | locked_out_user | secret_sauce | Epic sadface: Sorry, this user has been locked out.                      |
    Given I have quit the application
  Scenario Outline: Validate the Api
    Given I have request the GET Api link "http://localhost:3000/Database" and validate status code "200"
    Given I have request the POST Api link "http://localhost:3000/Database" and validate status code "201" and "<playload>"
    Examples:
      | playload |
      |
    {
    "postId": 1,"id": 1,"name": "id labore ex et quam laborum","email": "Eliseo@gardner.biz","body": "laudantium"} |


     enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium"
   }








