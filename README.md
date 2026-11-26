# Selenium and BDD Testing Study

Educational Python browser-test repository with Selenium helpers, Gherkin feature
files, and GitHub Actions configurations. It exercises an external application;
it is not a standalone product or an AI testing agent.

`requirements.txt` contains the original dependency pins. Feature files and step
implementations are under `features/`; additional test code is under `src/`.
The features use Behave-style steps, although the repository name mentions Cucumber.
Review and install the actual runner/browser dependencies before attempting them.

Tests depend on the original target application's availability and test data.
Do not execute them against production or personal accounts. CI configuration is
historical and is not evidence that the current suite passes.
