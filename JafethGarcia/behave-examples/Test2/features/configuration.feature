Feature: API
  # Enter feature description here

  Scenario: # Enter scenario name here
    # Enter steps here
    Given I have connection to host http://todo.ly
    When I GET
    Then I receive status code 200