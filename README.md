A look at a behavior driven test case!
===

We are in the process of defining and automating the user acceptance criterias for the Move file/folder functionality on the mobile client. It is a functionality that our users need and we have to make sure that it works according to our specification.

You can download the official reMarkable companion application on your phone (go into App Store or Play Store dependent on wether you have an IOS or Android phone). When asked to fill in a One Time Code use the following cridentials:

Username: qa.interview.remarkable@gmail.com

Password: SAND6tish7chis_spum

When the client is connected, you'll see the file structure that you need in order to solve this task. You can use this to better understand how the Move functionality is working. Feel free to experiment as much as you want with the Move functionality.

Your task
---

Your task is to complete the three empty scenarios in test.feature and supply corresponding step implementations in steps.py. The spesific file structure that should be used when solving this task is desribed in test.feature. An object map with items relevant to the Move functionality is given in names.py (you shouldn't have to edit anything there). Some support functions are given in library_helper.py. We encourage you to think of other relevant scenarios to test as well. These do not have to be implemented, but if you have time for it you are of course allowed to implement those as well.

When implementing the steps you'll probably need the Squish APIs:
https://doc.froglogic.com/squish/latest/rgs-squish.html
https://doc.froglogic.com/squish/latest/rgs-qtconvenience.html

If you're unfamiliar with BDD frameworks and how to write Gherkin steps in a feature file, we recommend having a look at: https://automationpanda.com/2017/01/30/bdd-101-writing-good-gherkin/ We're not expecting your solution to follow all these guidelines, but we are going to look for two things in particular: 1. One scenario covers one behavior and 2. Respecting the integrity of the step type.
Unfortunately you can't run the actual tests on your system. So the syntactic correctness of the Python step implementation isn't that important, but we are going to evaluate whether the Python code is readable and sensible.

As you work on implementing this feature try to think of other scenarios that we might have forgotten to include and that we should test in order to ensure that Move works as expected.
