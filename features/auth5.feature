Feature: Empty posts
  Scenario: there are no posts and a message should be shown
    Given flaskr is set up
    and we log in with "admin" and "admin"
    and we are at the index page
      Then we should see the following text: "No entries yet. Add some!"

