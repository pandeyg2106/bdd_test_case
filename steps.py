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
from xmlrpc.client import boolean

from behave import Given, When, Then

import names
import test

from library_helper import find_visible_document
from library_helper import find_visible_folder
from library_helper import find_search_result


#### Given statements (preconditions) ####

## This step verifies that a document is visible under My Files
@Given('the "{document_name}" document is visible in My Files')
def step(context, document_name):
    test.verify(find_visible_document(document_name) != None)

## This step verifies that a folder is visible under My Files
@Given('the "{folder_name}" folder is visible in My Files')
def step(context, folder_name):
    test.verify(find_visible_folder(folder_name))


@Given('the selection header is displayed for "{document_name}" document')
def step(context, document_name):
    longMouseClick(find_visible_document(document_name))
    waitForObject(names.header_select_multiple)
    waitForObject(names.header_close)


@Given('the folder "{folder_name}" contains the file "{document_name}"')
def step_impl(context, folder_name, document_name):
    longMouseClick(find_visible_document(document_name))
    mouseClick(waitForObject(names.drawer_move))
    mouseClick(find_visible_folder(folder_name))
    mouseClick(waitForObject(names.movePanel_move))
    mouseClick(waitForObject(names.topMenu_back))


@Given('the move panel is displayed for "{folder_name}" folder')
def step_impl(context, folder_name):
    longMouseClick(find_visible_folder(folder_name))
    mouseClick(waitForObject(names.drawer_move))
    waitForObject(names.movePanel_label)
    waitForObject(names.movePanel_cancel_move)
    waitForObject(names.movePanel_move)
    test.verify(find_visible_folder(folder_name) == None)


@Given('the move panel is displayed for "{document_name}" document')
def step_impl(context, document_name):
    longMouseClick(find_visible_document(document_name))
    mouseClick(waitForObject(names.drawer_move))
    waitForObject(names.movePanel_label)
    waitForObject(names.movePanel_cancel_move)
    waitForObject(names.movePanel_move)


#### When statements (exercising behaviour) ####

@When('the user long press the "{document_name}" document')
def step(context, document_name):
    try:
        longMouseClick(find_visible_document(document_name))
        pass
    except:
        raise ValueError("Document doesn't exist under Library")

@When('the user long press the "{folder_name}" folder')
def step(context, folder_name):
    try:
        longMouseClick(find_visible_folder(folder_name))
        pass
    except:
        raise ValueError("Folder doesn't exist under Library")

### This step selects the move from the drawer ###
@When("the user selects move from the drawer")
def step(context):
    mouseClick(waitForObject(names.drawer_move))


### This step selects the move button from the move panel ###
@When("the user selects the move button from the move panel")
def step(context):
    mouseClick(waitForObject(names.movePanel_move))


@When("the user chooses select multiple button")
def step(context):
    mouseClick(waitForObject(names.header_select_multiple))


@When('the user clicks on the search button in the top menu')
def step(context):
    mouseClick(waitForObject(names.topMenu_search))


@When("the user selects the {} from the search result")
def step(context, folder_name):
    mouseClick(waitForObject(find_search_result(folder_name)))


@When('the user selects "{document_name}" document in My Files')
def step(context, document_name):
    try:
        mouseClick(find_visible_document(document_name))
    except:
        raise ValueError("Only one document exists in the library")


@When('the user selects the Done button from the top menu')
def step(context):
    mouseClisk(waitForObject(names.header_confirm_selection))


@When('the user select the {} folder')
def step_impl(context, folder_name):
    if find_visible_folder(folder_name) != None:
        mouseClick(waitForObject(find_visible_folder(folder_name)))
    else:
        raise ValueError("Folder doesn't exist under Library")


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
    object.exists(names.drawer_move) == false
