# Note: At the beginning of each scenario the application will start in My files, with library structure:
#
# My files/
# |--- Test
# |--- Quick sheets
# |--- Folder/ (empty)
# |--- Some folder/ (empty)
# |--- Some other folder/ (empty)

Feature: Move files and folders

  This feature should test the different aspects of moving files and folders

  Scenario: Long press document to access move action
    Given the "Test" document is visible in My Files
    When the user long press the "Test" document
    And the user selects move from the drawer
    Then the user should be prompted with the move panel

  Scenario: Long press folder to access move action
    Given the "Folder" folder is visible in My Files
    When the user long press the "Folder" folder
    And the user selects move from the drawer
    Then the user should be prompted with the move panel

  Scenario: Move single file to folder
    Given the "Test" document is visible in My Files and is ready to move
    When the user moves the document to "Folder" folder
    Then the "Test" document is visible in the destination folder

  # Here we are starting with a pre condition where a folder should not be empty.
  # To fulfil this condition we have to make sure that we add a document to that folder before the start of test.
  # Once a document is added, to return to My Files screen we have to go back from the button in top menu.
  # Since the names class does not have an object for the back button I have added one.
  Scenario: Move single folder with data to another folder
    Given the folder "Folder" containing the file "Test" is ready to move
    When the user moves the non empty folder to "Some other folder"
    Then the folder "Folder" containing "Test" document is visible in the destination folder

  Scenario: Multiple documents can be moved to a different folder
    Given that more than two documents are available and selection header is displayed for "Test" document
    # The below step is required because if there are only 2 documents, then we can't move them, as the library will then
    # have no documents left.
    When the user selects multiple documents and move them to "Some folder" folder
    Then all selected documents are visible in the destination folder

  Scenario: Multiple folders can be moved to a different folder
    Given that more than two folders are available and selection header is displayed for "Folder" folder
    When the user selects multiple folders and move them to "Some folder" folder
    Then all selected folders are visible in the destination folder

  Scenario: Move file and folder to folder
    Given My files has a file and a folder to move
    When the user selects "Some other folder" and a "Test" document
    And the user confirms and move the selection
    Then the folder "Folder" and the document "Test" is visible in the destination folder

  Scenario: Move file to folder by searching for destination
    Given the "Test" document is ready to be moved
    When the user searches for "Some folder" and moves the document to that folder
    Then the "Test" document is visible in the destination folder

  Scenario: All documents can't be moved from library
    Given the selection header is displayed for "Test" document
    When the user selects all documents under My Files
    Then the user should not be allowed to move all the files

  Scenario: All folders can't be moved from library
    Given the selection header is displayed for "Folder" folder
    When the user selects all folders under My Files
    # It looks like the below step will fail as I can see the move button in drawer when all folders are selected.
    # When I select all the folders under My Files I see the Move button in drawer, but there is no folder left to move
    # these items to. In case of Documents, I do not see the move button when all documents are selected.
    Then the user should not be allowed to move all the files
