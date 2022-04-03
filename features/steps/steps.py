# A quick introduction to implementing scripts for BDD tests:
#
# This file contains snippets of script code to be executed as the .feature
# file is processed.
#
# The decorators Given/When/Then/Step can be used to associate a script snippet
# with a pattern which is matched against the steps being executed. Optional
# table/multi-line string arguments of the step are passed via a mandatory
# 'context' parameter:
#
#   @When("the user enters the text")
#   def step(context):
#      <code here>
#
# The pattern is a plain string without the leading keyword, but a couple of
# placeholders including |any|, |word| and |integer| are supported which can be
# used to extract arbitrary, alphanumeric and integer values resp. from the
# pattern; the extracted values are passed as additional arguments:
#
#   @Then("the user gets |integer| different names")
#   def step(context, numNames):
#      <code here>

from behave import Given, When, Then

from resources import names
import test
from resources.library_helper import find_visible_document
from resources.library_helper import find_visible_folder
from resources.library_helper import find_search_result
from resources.library_helper import find_all_visible_documents
from resources.library_helper import find_all_visible_folders
from resources.library_helper import is_document_selected
from resources.library_helper import is_folder_selected
from resources.library_helper import find_all_selected_documents
from resources.library_helper import find_all_selected_folders

### These are the global variables whose values are updated by the functions in library_helper.py
SELECTED_DOCUMENTS = []
SELECTED_FOLDERS = []
ALL_VISIBLE_DOCUMENTS = []
ALL_VISIBLE_FOLDERS = []

#### Given statements (preconditions) ####

## This step verifies a pre-condition where a specific document is visible under My Files
@Given('the "{document_name}" document is visible in My Files')
def step(context, document_name):
    test.verify(find_visible_document(document_name) != None)


## This step verifies the pre-condition where a specific folder is visible under My Files
@Given('the "{folder_name}" folder is visible in My Files')
def step(context, folder_name):
    test.verify(find_visible_folder(folder_name))


## This step verifies the pre-condition where a selection header with options is displayed when a document is long pressed.
@Given('the selection header is displayed for "{document_name}" document')
def step(context, document_name):
    longMouseClick(find_visible_document(document_name))
    waitForObject(names.header_select_multiple)
    waitForObject(names.header_close)


## This step verifies the pre-condition where a selection header with options is displayed when a folder is long pressed.
@Given('the selection header is displayed for "{folder_name}" folder')
def step(context, folder_name):
    longMouseClick(find_visible_folder(folder_name))
    waitForObject(names.header_select_multiple)
    waitForObject(names.header_close)


## This step verifies the pre-condition where a specific folder contains a soecific document.
@Given('the folder "{folder_name}" contains the file "{document_name}"')
def step_impl(context, folder_name, document_name):
    longMouseClick(find_visible_document(document_name))
    mouseClick(waitForObject(names.drawer_move))
    mouseClick(find_visible_folder(folder_name))
    mouseClick(waitForObject(names.movePanel_move))
    mouseClick(waitForObject(names.topMenu_back))


## This step verifies the pre-condition where the move panel with all objects is displayed when a folder is long pressed.
@Given('the move panel is displayed for "{folder_name}" folder')
def step_impl(context, folder_name):
    longMouseClick(find_visible_folder(folder_name))
    mouseClick(waitForObject(names.drawer_move))
    waitForObject(names.movePanel_label)
    waitForObject(names.movePanel_cancel_move)
    waitForObject(names.movePanel_move)
    test.verify(find_visible_folder(folder_name) == None)


## This step verifies the pre-condition where the move panel with all objects is displayed when a document is long pressed.
@Given('the move panel is displayed for "{document_name}" document')
def step_impl(context, document_name):
    longMouseClick(find_visible_document(document_name))
    mouseClick(waitForObject(names.drawer_move))
    waitForObject(names.movePanel_label)
    waitForObject(names.movePanel_cancel_move)
    waitForObject(names.movePanel_move)

## This step verifies the pre-condition where the total number of documents under My Files are more than 2. This is
## required because if the documents <= 2, then the system should not allow the Move.
@Given("the total number of documents are more than 2")
def step_impl(context):
    find_all_visible_documents()
    if len(ALL_VISIBLE_DOCUMENTS) < 3:
        ALL_VISIBLE_DOCUMENTS.clear()
        raise ValueError("Multiple documents can't be moved as there are only 2 documents.")
    else:
        ALL_VISIBLE_DOCUMENTS.clear()
        pass

## This step verifies the pre-condition where the total number of folders under My Files are more than 2. This is
## required because if the documents <= 2, then the system should not allow the Move.
@Given("the total number of folders are more than 2")
def step_impl(context):
    find_all_visible_folders()
    if len(ALL_VISIBLE_FOLDERS) < 3:
        ALL_VISIBLE_DOCUMENTS.clear()
        raise ValueError("Multiple folders can't be moved as there are only 2 folders.")
    else:
        ALL_VISIBLE_FOLDERS.clear()
        pass

## This step verifies the pre-condition that My Files has a document and a folder to move at the same time.
@Given("My files has a file and a folder to move")
def step_impl(context):
    ## Here we will use the methods find_all_visible_folders() and find_all_visible_documents() to assert if we have
    ## data to start the test
    find_all_visible_documents() # returns a list ALL_VISIBLE_DOCUMENTS
    find_all_visible_folders()   # returns a list ALL_VISIBLE_FOLDERS
    if(len(ALL_VISIBLE_DOCUMENTS) > 0 & len(ALL_VISIBLE_FOLDERS) > 0):
        pass


#### When statements (exercising behaviour) ####

## In this step  a user long press a specific document, and raises an exception if the specified document doesn't exists.
@When('the user long press the "{document_name}" document')
def step(context, document_name):
    try:
        longMouseClick(find_visible_document(document_name))
        pass
    except:
        raise ValueError("Document doesn't exist under Library")


## In this step  a user long press a specific folder, and raises an exception if the specified folder doesn't exists.
@When('the user long press the "{folder_name}" folder')
def step(context, folder_name):
    try:
        longMouseClick(find_visible_folder(folder_name))
        pass
    except:
        raise ValueError("Folder doesn't exist under Library")


## In this step the user selects the move button from the drawer, which opens the move panel for the document or folder.
@When("the user selects move from the drawer")
def step(context):
    mouseClick(waitForObject(names.drawer_move))


## In this step the user selects the move button from the move panel which moves the document or folder.
@When("the user selects the move button from the move panel")
def step(context):
    mouseClick(waitForObject(names.movePanel_move))


## In this step the user selects the multiple select button from the top menu when a document/folder is long pressed.
@When("the user chooses select multiple button")
def step(context):
    mouseClick(waitForObject(names.header_select_multiple))


@When('the user clicks on the search button in the top menu')
def step(context):
    mouseClick(waitForObject(names.topMenu_search))


@When("the user selects the {} from the search result")
def step(context, folder_name):
    mouseClick(waitForObject(find_search_result(folder_name)))


## This step will select all the visible not selected documents under My Files
@When('the user selects all documents under My Files')
def step(context):
    list = find_all_visible_documents()
    for i in list:
        if not is_document_selected(i):
            mouseClick(waitForObject(find_visible_document(i)))


@When("the user selects all folders under My Files")
def step_impl(context):
    list = find_all_visible_folders()
    for i in list:
        if not is_folder_selected(i)
        mouseClick(waitForObject(find_visible_folder(i)))

### This step confirms the selection of documents/folders. After this step the move panel will be visible.
@When('the user selects the Done button from the top menu')
def step(context):
    mouseClisk(waitForObject(names.header_confirm_selection))

### In this step the user selects the destination folder where move operation will be performed.
@When('the user selects the "{folder_name}" folder')
def step_impl(context, folder_name):
    if find_visible_folder(folder_name) != None:
        mouseClick(waitForObject(find_visible_folder(folder_name)))
    else:
        raise ValueError("Folder" +folder_name+ " doesn't exist under Library")

@When('the user select the "{document_name}" document')
def step_impl(context, document_name):
    if find_visible_document(document_name) != None:
        mouseClick(waitForObject(find_visible_folder(folder_name)))
    else:
        raise ValueError("Document" +document_name+ " doesn't exist under Library")


@When("the user selects one more document under My Files")
def step_impl(context):
    SELECTED_DOCUMENTS.clear() # Clearing the list in start so that there are no previous data.
    find_all_visible_documents() # result saved in the global list ALL_VISIBLE_DOCUMENTS
    count = 0
    for i in ALL_VISIBLE_DOCUMENTS:
        if not is_document_selected(i): # If there is any document not already selected, then we will select it. This is
        # done to ensure we don't do a mouse click on already selected document, as that will de-select it.
            mouseClick(waitForObject(find_visible_document(i)))
            find_all_selected_documents() #This method will store the names of all the selected documents in a global
            count +=1                     # list calledSELECTED_DOCUMENTS, which will be used to verify if only these
            if count > 0:                 # selected documents are moved.
                ALL_VISIBLE_DOCUMENTS.clear() #Clearing the list of all visible documents so that it doesn't affect other tests.
                break

@When("the user selects one more folder under My Files")
def step_impl(context):
    SELECTED_FOLDERS.clear()
    find_all_visible_folders()  # result saved in the global list ALL_VISIBLE_FOLDERS
    count = 0
    for i in ALL_VISIBLE_FOLDERS:
        if not is_folder_selected()_selected(i):
            mouseClick(waitForObject(find_visible_folder(i)))
            find_all_selected_folders()  # This method will store the names of all the selected documents in a global
            count += 1  # list called SELECTED_FOLDERS
            if count > 0:
                ALL_VISIBLE_FOLDERS.clear()
                break

#### Then statements (verifying outcome) ####

### This step verifies that user can view the move panel ###
@Then("the user should be prompted with the move panel")
def step(context):
    waitForObject(names.movePanel_label)
    waitForObject(names.movePanel_cancel_move)
    waitForObject(names.movePanel_move)


@Then('the "{Folder}" folder is visible in the destination folder')
def step_impl(context, Folder):
    test.verify(find_visible_folder(Folder) != None)


@Then('the "{Folder}" contains "{Test}" document')
def step_impl(context, Folder, Test):
    mouseClick(find_visible_folder(Folder))
    test.verify(find_visible_document(Test) != None)


@Then('the "{document_name}" document is visible in the destination folder')
def step_impl(context, document_name):
    test.verify(find_visible_document(document_name) != None)


@Then('the user should not be allowed to move all the files')
def step_impl(context):
    waitForObject(names.drawer_copy)
    waitForObject(names.drawer_favorite)
    waitForObject(names.drawer_send)


### This step will verify that all the selected documents are moved to the destination folder
@Then("all selected documents are visible in the destination folder")
def step_impl(context):
    for i in SELECTED_DOCUMENTS:  # We are iterating through the list of selected documents, and verifying all those are
        # present in the destination folder.
        test.verify(find_visible_document(i)) # This step will verify that all the selected documents are moved in the
                                              # destination folder.

### This step will verify that all the selected folders are moved to the destination folder
@Then("all selected folders are visible in the destination folder")
def step_impl(context):
    for i in SELECTED_FOLDERS:  # We are iterating through the list of selected folders, and verifying all those are
        # present in the destination folder.
        test.verify(find_visible_folder(i)) # This step will verify that all the selected documents are copied in the
                                              # destination folder.


