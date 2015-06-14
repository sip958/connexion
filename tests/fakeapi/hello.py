#!/usr/bin/env python3


def post_greeting(name: str) -> dict:
    data = {'greeting': 'Hello {name}'.format(name=name)}
    return data

def get_bye(name: str) -> dict:
    return 'Goodbye {name}'.format(name=name)

def get_bye_secure(name: str) -> dict:
    return 'Goodbye {name} (Secure)'.format(name=name)