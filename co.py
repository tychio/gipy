#!/usr/bin/env python

import inquirer
import os
from pprint import pprint

questions = [
    inquirer.Text(
        'commit',
        message = "Please input a comment for your commit"
    ),
    inquirer.Text(
        'prefix',
        message = "Please input a prefix for your commit"
    ),
]

answers = inquirer.prompt(questions)

commitComment = answers['commit']
prefix = answers['prefix']

if prefix: 
    prefix = "[" + prefix + "]"

if commitComment:
    os.system("git commit -m \"" + prefix + commitComment + "\"")
else:
    os.system("git commit --amend")