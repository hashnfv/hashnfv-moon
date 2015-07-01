# Copyright 2015 Open Platform for NFV Project, Inc. and its contributors
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the file 'LICENSE' in this package distribution
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

import logging

from cliff.lister import Lister
from cliff.command import Command


class SubjectCategoriesList(Lister):
    """List all Intra_Extensions."""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(SubjectCategoriesList, self).get_parser(prog_name)
        parser.add_argument(
            '--intraextension',
            metavar='<intraextension-uuid>',
            help='IntraExtension UUID',
        )
        return parser

    def take_action(self, parsed_args):
        if not parsed_args.intraextension:
            parsed_args.intraextension = self.app.intraextension
        data = self.app.get_url("/v3/OS-MOON/intra_extensions/{}/subject_categories".format(parsed_args.intraextension),
                                authtoken=True)
        if "subject_categories" not in data:
            raise Exception("Error in command {}: {}".format("SubjectCategoriesList", data))
        return (
            ("subject_categories",),
            ((_uuid, ) for _uuid in data["subject_categories"])
        )


class SubjectCategoriesAdd(Command):
    """List all Intra_Extensions."""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(SubjectCategoriesAdd, self).get_parser(prog_name)
        parser.add_argument(
            'subject_category',
            metavar='<subject_category-uuid>',
            help='Subject UUID',
        )
        parser.add_argument(
            '--intraextension',
            metavar='<intraextension-uuid>',
            help='IntraExtension UUID',
        )
        return parser

    def take_action(self, parsed_args):
        if not parsed_args.intraextension:
            parsed_args.intraextension = self.app.intraextension
        data = self.app.get_url("/v3/OS-MOON/intra_extensions/{}/subject_categories".format(parsed_args.intraextension),
                                post_data={"subject_category_id": parsed_args.subject_category},
                                authtoken=True)
        if "subject_categories" not in data:
            raise Exception("Error in command {}".format(data))
        return (
            ("subject_categories",),
            ((_uuid, ) for _uuid in data["subject_categories"])
        )


class SubjectCategoriesDelete(Command):
    """List all Intra_Extensions."""

    log = logging.getLogger(__name__)

    def get_parser(self, prog_name):
        parser = super(SubjectCategoriesDelete, self).get_parser(prog_name)
        parser.add_argument(
            'subject_category',
            metavar='<subject_category-uuid>',
            help='Subject UUID',
        )
        parser.add_argument(
            '--intraextension',
            metavar='<intraextension-uuid>',
            help='IntraExtension UUID',
        )
        return parser

    def take_action(self, parsed_args):
        if not parsed_args.intraextension:
            parsed_args.intraextension = self.app.intraextension
        self.app.get_url("/v3/OS-MOON/intra_extensions/{}/subject_categories/{}".format(
            parsed_args.intraextension,
            parsed_args.subject_category
        ),
            method="DELETE",
            authtoken=True)