<h1 align="center"> Cucumber - Gherkin </h1>

Behaviour-Driven Development (BDD) is the software development process that Cucumber was built to support.
There’s much more to BDD than just using <a href="https://cucumber.io/docs/bdd/">Cucumber.</a>

<h1 align="center"> What is BDD? </h1>
 
``BDD`` is a way for software teams to work that closes the gap between business people and technical people by:

* Encouraging collaboration across roles to build shared understanding of the problem to be solved
* Working in rapid, small iterations to increase feedback and the flow of value
* Producing system documentation that is automatically checked against the system’s behaviour

We do this by focusing collaborative work around concrete, real-world examples that illustrate how we want the system to behave. We use those examples to guide us from concept through to implementation, in a process of continuous collaboration.

<h1 align="center"> What is Gherkin? </h1>

<a href="https://cucumber.io/docs/guides/overview/#what-is-gherkin">Gherkin</a> is a set of grammar rules that makes plain text structured enough for Cucumber to understand. The scenario above is written in Gherkin.

``Gherkin`` serves multiple purposes:

* Unambiguous executable specification
* Automated testing using Cucumber
* Document how the system actually behaves

<h1 align="center"> Behave - Python </h1>

behave uses tests written in a natural language style, backed up by ``Python`` code.

First, <a href="https://pypi.org/project/behave/">install *behave*.</a>

Now make a directory called *“features/”*. In that directory create a file called *“example.feature”* containing:

<pre><blockquote>
# -- FILE: features/example.feature
Feature: Antonio Rodriguez TECH

  Scenario: Run a simple test
    Given we have behave installed
     When we implement 5 tests
     Then behave will test them for us!
</blockquote></pre>

Make a new directory called *“features/steps/”*. In that directory create a file called *“example_steps.py”* containing:

<pre><blockquote>
# -- FILE: features/steps/example_steps.py
from behave import given, when, then, step

@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement {number:d} tests')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number

@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0
</blockquote></pre>

Run behave:

<pre><blockquote>
$ behave
Feature: Cyber Guardian TECH # features/example.feature:2

  Scenario: Run a simple test          # features/example.feature:4
    Given we have behave installed     # features/steps/example_steps.py:4
    When we implement 5 tests          # features/steps/example_steps.py:8
    Then behave will test them for us! # features/steps/example_steps.py:13

1 feature passed, 0 failed, 0 skipped
1 scenario passed, 0 failed, 0 skipped
3 steps passed, 0 failed, 0 skipped, 0 undefined
</blockquote></pre>

&nbsp;
<h4 align="left">LINKs or FYI:</h4>

* https://cucumber.io/docs/cucumber/

* https://behave.readthedocs.io/en/stable/tutorial.html

* https://pypi.org/project/behave/
