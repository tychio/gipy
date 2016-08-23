#!/usr/bin/env python

import inquirer
import os
from pprint import pprint

questions = [
    inquirer.Text(
        'commit',
        message = "Please input a comment for your commit"
    ),
]

answers = inquirer.prompt(questions)

commitComment = answers['commit']
if commitComment:
    os.system("git commit -m \"" + commitComment + "\"")
else:
    os.system("git commit -amend")