# Copyright 2015 Open Platform for NFV Project, Inc. and its contributors
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the file 'LICENSE' in this package distribution
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.


import logging
import random

LOG = logging.getLogger(__name__)


def get_uuid_from_name(name, elements, **kwargs):
    LOG.error("get_uuid_from_name {} {} {}".format(name, elements, kwargs))
    for element in elements:
        if type(elements[element]) is dict and elements[element].get('name') == name:
            if kwargs:
                for args in kwargs:
                    if elements[element].get(args) != kwargs[args]:
                        LOG.error("get_uuid_from_name2 {} {} {}".format(args, elements[element].get(args), kwargs[args]))
                        return
                else:
                    return element
            else:
                return element


def get_name_from_uuid(uuid, elements, **kwargs):
    for element in elements:
        if element == uuid:
            if kwargs:
                for args in kwargs:
                    if elements[element].get(args) != kwargs[args]:
                        return
                else:
                    return elements[element].get('name')
            else:
                return elements[element].get('name')


def get_random_name():
    _list = (
        "windy",
        "vengeful",
        "precious",
        "vivacious",
        "quiet",
        "confused",
        "exultant",
        "impossible",
        "thick",
        "obsolete",
        "piquant",
        "fanatical",
        "tame",
        "perfect",
        "animated",
        "dark",
        "stimulating",
        "drunk",
        "depressed",
        "fumbling",
        "like",
        "undesirable",
        "spurious",
        "subsequent",
        "spiteful",
        "last",
        "stale",
        "hulking",
        "giddy",
        "minor",
        "careful",
        "possessive",
        "gullible",
        "fragile",
        "divergent",
        "ill-informed",
        "false",
        "jumpy",
        "damaged",
        "likeable",
        "volatile",
        "handsomely",
        "wet",
        "long-term",
        "pretty",
        "taboo",
        "normal",
        "magnificent",
        "nutty",
        "puzzling",
        "small",
        "kind",
        "devilish",
        "chubby",
        "paltry",
        "cultured",
        "old",
        "defective",
        "hanging",
        "innocent",
        "jagged",
        "economic",
        "good",
        "sulky",
        "real",
        "bent",
        "shut",
        "furry",
        "terrific",
        "hollow",
        "terrible",
        "mammoth",
        "pleasant",
        "scared",
        "obnoxious",
        "absorbing",
        "imported",
        "infamous",
        "grieving",
        "ill-fated",
        "mighty",
        "handy",
        "comfortable",
        "astonishing",
        "brown",
        "assorted",
        "wrong",
        "unsightly",
        "spooky",
        "delightful",
        "acid",
        "inconclusive",
        "mere",
        "careless",
        "historical",
        "flashy",
        "squealing",
        "quarrelsome",
        "empty",
        "long",
    )
    return random.choice(_list)
