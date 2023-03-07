# test_package



Doc, install and writing code
-----------------------------
- Create a new github repository, check all marks:
  - [ ] gitignore,
  - [ ] license,
  - [ ] README.
- Clone the repository on your computer
- Write docstring for the function
- *Organize code as a package:* `folder/code/functions.py`, and add an `__init__.py` file, in which only the version is present.
- At the root, write a `pyproject.toml` function that will allow to install the package, and then do `pip install -e.`. This should not return errors.
- In the code folder, create a `tests` folder, a `test_linear_regression.py` file in it and write several test functions, with names starting with `test_`. Then, run `pytest` at the root file. All tests should pass.
- Check that the code is compatible with pep 8 using the command `ruff`, this can be installed using `pip install ruff`.
- Upload everything on github by first adding all new files using `git add ...`, then commiting by using `git commit -am ` (write a message here) and then `git push`. Check on github that the new code is here.

Documentation 
-------------
- At the root, create an `examples` folder. In this folder, create a function `plot_simple_example` in which you write a small example of what the linear regression code can do.
- Add some plots using matplotlib. 

## Deploying the website

- Create an empty branch `gh-pages` on you repo
```bash
git stash
git checkout --orphan gh-pages
git reset --hard
git commit --allow-empty -m "INIT gh-pages branch"
git push -u origin gh-pages
git checkout main
git stash pop
```
- In the settings, activate the the doc rendering options.

## Continuous integration
- Add a `.github/workflows` folder at the root, and write a `unittests.yml` file in it that runs continuous integration on github. This should run the `ruff` and unit tests command, everytime there is a push on the main github branch, or that somebody does a pull request

## Pull requests
- By pair, fork the github repository of one of the other student, create a new branch using `git checkout -b branch-name`, then implement regularized linear regression in the `linear_regression/linear_regression.py` file. Then, commit your changes, push the branch on github, and do a pull request on the other students' repo. 

- Check that the continuous integration tests are run, and that everything it ok. Then, merge the pull request.