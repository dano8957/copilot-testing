# Automating Testing with GitHub Copilot
## Revision 1.0 - 06/08/24

**Follow the startup instructions in the README.md file IF NOT ALREADY DONE!**

**NOTE: To copy and paste in the codespace, you may need to use keyboard commands - CTRL-C and CTRL-V.**

**Lab 1 - High level Copilot Testing Advice**

**Purpose: In this lab, we’ll start to learn about testing with Copilot at a high levele**

1. Create a new file. In the terminal, enter

   ```
   code prime.py
   ```

2. Afterwards this file should be open in a tab in the editor.

3. Start typing a function definition as below
```
def is_prime(n):
```

4. Hit return and notice the code that Copilot suggested. Hit tab to select that line. (Note that you should give Copilot a second to provide code suggestions before moving on to the next line.)
   
5. After hitting tab, Copilot will generate another part of the function. (If not, you may need to hit return.) Hit tab to accept it. Continue until you get a complete function (or Copilot stops generating additional code suggestions). One example of what code may look like is below.

![Copilot generated function](./images/ct04.png?raw=true "Copilot generated function")
   
6. Now, let's ask Copilot for some general testing advice on your project. Switch to the separate chat area, and ask it:
```
How do I add tests to my project?
```
7. Copilot will likely have generated some output with a set of instruction and some example code as shown below.
![testing suggestions for project](./images/ct05.png?raw=true "testing suggestions for project")

8. Let's also try it with a different kind of file and language. There's a large demo file of SQL statements in this project named *create-tables.sql*. Open that.
```
code create-tables.sql
```

9. Since this is a different type of file, we will specify the filename when we ask this time. Enter the following question in the chat interface.
```
How do I test the code in #file:create-tables.sql?
```

10. Copilot should again respond with some instructions and suggested examples of how to do the steps.
![testing suggestions for SQL](./images/ct06.png?raw=true "testing suggestions for sql")   


<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 2 - Using Copilot to create tests**

**Purpose: In this lab, we'll see how to have Copilot create tests for us.**

1. Let's see how to use the shortcut command */tests* to generate some tests. Still working with the same prime.py file, highlight the code and use the *CMD+I* shortcut to bring up the inline chat dialog. In the text entry box for the dialog, enter the */tests* command.

![using the shortcut command to gen tests](./images/ct07.png?raw=true "using the shortcut command to gen tests")

2. After running the command, Copilot generates some basic assert-based tests. The tests may first be shown in a pop up dialog window. You can add them into a separate file by accepting them from the resulting dialog. Or you can use the checkmark control.

![proposed tests from slash command](./images/ct08.png?raw=true "proposed tests from slash command")

3. We can also get the same results from invoking the *Generate Tests* entry from the context menu. Try that now by highlighting the code, right-clicking on it, then selecting *Copilot* and then *Generate Tests*. Go ahead and hit Tab to accept those.

![proposed tests from the menu](./images/ct09.png?raw=true "proposed tests from the menu")

4. Let's see what other suggestions Copilot can come up with for tests. Highlight the new tests and then hit **Ctrl+Enter** to see other possible completion options. 

![scrolling through alternative options](./images/ct10.png?raw=true "scrolling through alternative options") 

5. Pick a different option if you want and **Accept suggestion #**. 

![choosing an alternative suggestion](./images/ct11.png?raw=true "choosing an alternative suggestion") 

6. We can also use comments to have Copilot create tests. Let's try this with the current file. First highlight and delete the current tests that are there.
![Removing current tests](./images/ct12.png?raw=true "Removing current tests") 

7. Now, under the code, add a comment line that tell Copilot to create tests for the code above.
```
# Create tests for the codee above
```

8. Hit return (if you haven't) and Copilot will probably supply a generic testing routine, such as (you do NOT need to type this in):
```
def test_is_prime(number, expected):
    result = is_prime(number)
    assert result == expected, f"Expected {expected} but got 
{result}"
```

9. Depending on your particular comment and context, Copilot may produce a more generic testing function or a set of individual test cases. To ensure you get the latter, remove the generated code for the testing and the comment and replace it with this comment.

```
# Create a set of 10 unit tests for the code above
```

10. In this case, Copilot will usually generate a more explicit set of tests wrapped in a testing function. An example is shown next.
![test by comment](./images/ct14.png?raw=true "test by comment")    

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 3 - Generating tests through code suggestions and corrections**

**Purpose: In this lab, we'll see how to have Copilot finish tests for us using code suggestions and corrections.**

1. To get started using this approach, you need to remove the existing testing code (if any, in the prime.py file). Then start typing the start of a testing function, but just the first line.
```
def test_is_prime(number):
```

2. Leaving this as-is causes a wavy line to be added on the next line. This means there's an issue with the code.
![error in function](./images/ct15.png?raw=true "error in function") 

3. There should be an AI symbol (the two starts) showing up in the listing. Click on that and you should get an option to have Copilot fix the problem.
![option to fix error](./images/ct16.png?raw=true "option to fix error") 

4. Copilot has likely generated a simple if/else code path to print whether or not the function passed. This is not what we really need, so you can just *Discard* the suggestion. (Or if you've already accepted it, you can just select and erase that code.)
![error in function](./images/ct17.png?raw=true "error in function") 

5. To get something more direct (like specific use cases), we can add additional tokens and/or keywords to the context. Let's add an *assert* keywork and then let Copilot suggest the remaining part of the test. In the *test_is_prime* function, add an *assert* statement underneath as shown below. Then you can accept the suggestion.

![start with assert](./images/ct18.png?raw=true "start with assert")   

6. From here, you can continue with the Enter/Tab key sequences to get a set of assertion tests.

<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 4 - Validating Inputs**

**Purpose: In this lab, we'll see how to have Copilot help validate inputs in functions.**

1. Copilot can also help with other kinds of validation besides general test cases. It can also validate that inputs going into a function are valid. Highlight your *is_prime* code and enter the prompt below into the Copilot Chat interface.

```
generate asserts to ensure that the inputs to the function are valid
```

2. From here, Copilot should respond and suggest asserts, as requested, to validate the functions inputs. The response may look something like the following (again you do not have to change anything).
```
(From Copilot:)

To ensure that the function inputs are valid, we can add assertions
at the start of the function. We want to make sure that the input 
is an integer and that it is not negative. Here's how you can do it:


def is_prime(num):
    assert isinstance(num, int), "Input must be an integer"
    assert num >= 0, "Input must be a non-negative integer"

    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```
3. We can also be less specific about using asserts and ask Copilot to generate checks. Try this prompt:
```
generate checks to ensure that the inputs to the function are valid
```

4. This should allow Copilot to generate code to validate the inputs, but with a more standard coding mechanism to surface any issues. Here's what example output from that might look like.
```
To ensure that the inputs to the `is_prime` function are valid, you
can add checks at the start of the function.
 Here's how you can do it:

```python
def is_prime(num):
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")
    if num < 0:
        raise ValueError("Input must be a non-negative integer")

    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
```

In this code, the `if` statements will raise a `TypeError` if the
 input is not an integer or a `ValueError` if it's a negative 
number.
 This way, you can ensure that the inputs to the function are valid.
```

5. When you're happy with this code, you can go ahead and add them to your code using the options in the code window of the chat.


<p align="center">
**[END OF LAB]**
</p>
</br></br>

**Lab 5 - Leveraging frameworks and TDD**

**Purpose: In this lab, we'll see how to leverage Copilot with testing frameworks and how to do Test-Driven Development with it.**

1. Let's look at a TDD approach of creating the test cases with a failing test and then immplementing the code to be tested. Consider a simple example where we want to create a test class and tests for students at a university. We'll use Mockito as our testing framework. Create a pom.xml file.
```
code pom.xml
```

2. Use the inline Chat interface (bring up the dialog with CMD+I) and ask Copilot to add a mockito dependency.
```
(in dialog) add mockito dependency
```
![add mockito dependency](./images/ct19.png?raw=true "add mockito dependency")  

3. Now, let's create an appropriate test class and initial set of tests. Do this in the Copilot separate Chat interface, since we expect a significant amount of output and we may want to put it in a separate file. We'll use a prompt that tells Copilot to focus on the *pom.xml* file we just created.
```
(In the separate chat interface)
Referencing #file:pom.xml, create a StudentTest class for students enrolled at a university and add tests
```
![query to create initial tests](./images/ct20.png?raw=true "query to create initial tests")  

4. The ouptput from this prompt is likely overkill for what we want for a simple test case for a *Student* class. Let's restructure the prompt to ask for something more specific. Enter the following in chat.
```
(In the separate chat interface)
Referencing #file:pom.xml, create a StudentTest class for a student
 enrolled at a university. A student will have personal attributes
 such as a first and last name, a phone number, an address, and a
 contact email.
```
![more specific query to create tests](./images/ct21.png?raw=true "more specific query to create tests")  

5. The output from Copilot now likely looks more like what we wanted as a starting point. Click into the output, hover over the top right, and use the icon (or copy and paste) to put it in a different file. Save the file as src/test/StudentTest.java.
![save new test](./images/ct22.png?raw=true "save new test")

6. Let's now run this test and see it fail. <to do figure out how to run test and see it fail>
```
```
![run test and it fails](./images/ct23.png?raw=true "run test and it fails")

7. Folllowing the TDD methodology, I should next create the minimum code to make this test pass. We can use Copilot for that. Make sure the new test you just saved is open in the editor, and then use this prompt to create the code.
```
(in the separate Chat interface)
Referencing #editor, create a student class.
```
![output of query to create student class](./images/ct24.png?raw=true "output of query to create student class")

8. This is a good start for the code to save and run our test case against. But let's go ahead and make sure it's well-commented.
```
(in the separate Chat interface)
Referencing #editor, create a student class with verbose comments.
```
![output of query to create student class with comments](./images/ct25.png?raw=true "output of query to create student class with comments")

9. Finally, let's run the test again and it should pass. <to do - figure out how to run the test and see it pass>
```
```
![run test and see it pass](./images/ct26.png?raw=true "run test and see it pass")

<p align="center">
**[END OF LAB]**
</p>

<p align="center">
**THANKS!**
</p>
 

