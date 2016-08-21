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

os.system("git commit -m \"" + answers['commit'] + "\"")