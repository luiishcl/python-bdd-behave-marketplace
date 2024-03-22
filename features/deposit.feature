Feature: Register on Deposit 
  As a BEES user,
  I want to access deposit
  So I can manager the deposit register

  Scenario: Register a Deposit
    Given stay on "Deposits" session
    When create a new deposit
        """
            {
                "name": "Deposit_A",
                "address": "Rua Orlando Viana",
                "city": "Campinas",
                "state": "Sao Paulo",
                "zipcode": "13044900"
            }
        """
    Then should present in the list of Deposits