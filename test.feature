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
    Given the "Folder" folder is visible in My Files
    And the move panel is displayed for "Test" document
    When the user select the "Folder" folder
    And the user selects the move button from the move panel
    Then the "Test" document is visible in the destination folder

  # Here we are starting with a pre condition where a folder should not be empty.
  # To fulfil this condition we have to make sure that we add a document to that folder.
  # Once a document is added, to return to My Files screen we have to go back from the button in top menu.
  Scenario Outline: Move file and folder to folder
    Given the folder "Folder" contains the file "Test"
    And the move panel is displayed for "Folder" folder
    When the user select the "<Folder Name>" folder
    And the user selects the move button from the move panel
    Then the "Folder" folder is visible in the destination folder
    And the "Folder" contains "Test" document
    Examples:
      | Folder Name       |
      | Some folder       |
      | Some other folder |

  Scenario Outline: Move file to folder by searching for destination
    Given the "Test" document is visible in My Files
    And the move panel is displayed for "Test" document
    When the user clicks on the search button in the top menu
    And the user selects the "<destination folder>" from the search result
    And the user selects the move button from the move panel
    Then the "Test" document is visible in the destination folder
    Examples:
      | destination folder |
      | Some folder        |
      | Some other folder  |

  Scenario: All documents can't be moved from library
    Given the selection header is displayed for "Test" document
    When the user chooses select multiple button
    And the user selects "Quick sheets" document in My Files
    And the user selects the Done button from the top menu
    Then the user should not be allowed to move all the files
