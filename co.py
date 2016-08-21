#!/usr/bin/env python

import inquirer
from pprint import pprint

questions = [
    inquirer.Text(
        "commit",
        message = "Please input a comment for your commit"
    ),
]

answers = inquirer.prompt(questions)

pprint(answers)