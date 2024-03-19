Feature:(REST-API) Get from mock rest api a json response

Scenario: Fetch from a mock rest api a json response
    Given the mock url
    When we consume the endpoint
    Then json response is retrieved with right data and 200 as status code