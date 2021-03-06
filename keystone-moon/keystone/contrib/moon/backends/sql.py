# Copyright 2015 Open Platform for NFV Project, Inc. and its contributors
# This software is distributed under the terms and conditions of the 'Apache-2.0'
# license which can be found in the file 'LICENSE' in this package distribution
# or at 'http://www.apache.org/licenses/LICENSE-2.0'.

import six
from uuid import uuid4
import copy

from keystone import config
from oslo_log import log
from keystone.common import sql
from keystone import exception
from keystone.contrib.moon.exception import *
from oslo_serialization import jsonutils
from keystone.contrib.moon import IntraExtensionDriver
from keystone.contrib.moon import TenantDriver

from sqlalchemy.orm.exc import UnmappedInstanceError
# from keystone.contrib.moon import InterExtensionDriver

CONF = config.CONF
LOG = log.getLogger(__name__)


class IntraExtension(sql.ModelBase, sql.DictBase):
    __tablename__ = 'intra_extensions'
    attributes = ['id', 'intra_extension']
    id = sql.Column(sql.String(64), primary_key=True)
    intra_extension = sql.Column(sql.JsonBlob(), nullable=True)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class Tenant(sql.ModelBase, sql.DictBase):
    __tablename__ = 'tenants'
    attributes = ['id', 'tenant']
    id = sql.Column(sql.String(64), primary_key=True, nullable=False)
    tenant = sql.Column(sql.JsonBlob(), nullable=True)

    @classmethod
    def from_dict(cls, d):
        """Override parent from_dict() method with a different implementation.
        """
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        """
        """
        return dict(six.iteritems(self))


class SubjectCategory(sql.ModelBase, sql.DictBase):
    __tablename__ = 'subject_categories'
    attributes = ['id', 'subject_category', 'intra_extension_id']
    id = sql.Column(sql.String(64), primary_key=True)
    subject_category = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class ObjectCategory(sql.ModelBase, sql.DictBase):
    __tablename__ = 'object_categories'
    attributes = ['id', 'object_category', 'intra_extension_id']
    id = sql.Column(sql.String(64), primary_key=True)
    object_category = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class ActionCategory(sql.ModelBase, sql.DictBase):
    __tablename__ = 'action_categories'
    attributes = ['id', 'action_category', 'intra_extension_id']
    id = sql.Column(sql.String(64), primary_key=True)
    action_category = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class Subject(sql.ModelBase, sql.DictBase):
    __tablename__ = 'subjects'
    attributes = ['id', 'subject', 'intra_extension_id']
    id = sql.Column(sql.String(64), primary_key=True)
    subject = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class Object(sql.ModelBase, sql.DictBase):
    __tablename__ = 'objects'
    attributes = ['id', 'object', 'intra_extension_id']
    id = sql.Column(sql.String(64), primary_key=True)
    object = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class Action(sql.ModelBase, sql.DictBase):
    __tablename__ = 'actions'
    attributes = ['id', 'action', 'intra_extension_id']
    id = sql.Column(sql.String(64), primary_key=True)
    action = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class SubjectScope(sql.ModelBase, sql.DictBase):
    __tablename__ = 'subject_scopes'
    attributes = ['id', 'subject_scope', 'intra_extension_id', 'subject_category_id']
    id = sql.Column(sql.String(64), primary_key=True)
    subject_scope = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)
    subject_category_id = sql.Column(sql.ForeignKey("subject_categories.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class ObjectScope(sql.ModelBase, sql.DictBase):
    __tablename__ = 'object_scopes'
    attributes = ['id', 'object_scope', 'intra_extension_id', 'object_category_id']
    id = sql.Column(sql.String(64), primary_key=True)
    object_scope = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)
    object_category_id = sql.Column(sql.ForeignKey("object_categories.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class ActionScope(sql.ModelBase, sql.DictBase):
    __tablename__ = 'action_scopes'
    attributes = ['id', 'action_scope', 'intra_extension_id', 'action_category']
    id = sql.Column(sql.String(64), primary_key=True)
    action_scope = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)
    action_category_id = sql.Column(sql.ForeignKey("action_categories.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class SubjectAssignment(sql.ModelBase, sql.DictBase):
    __tablename__ = 'subject_assignments'
    attributes = ['id', 'subject_assignment', 'intra_extension_id', 'subject_id', 'subject_category_id']
    id = sql.Column(sql.String(64), primary_key=True)
    subject_assignment = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)
    subject_id = sql.Column(sql.ForeignKey("subjects.id"), nullable=False)
    subject_category_id = sql.Column(sql.ForeignKey("subject_categories.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class ObjectAssignment(sql.ModelBase, sql.DictBase):
    __tablename__ = 'object_assignments'
    attributes = ['id', 'object_assignment', 'intra_extension_id', 'object_id', 'object_category_id']
    id = sql.Column(sql.String(64), primary_key=True)
    object_assignment = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)
    object_id = sql.Column(sql.ForeignKey("objects.id"), nullable=False)
    object_category_id = sql.Column(sql.ForeignKey("object_categories.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class ActionAssignment(sql.ModelBase, sql.DictBase):
    __tablename__ = 'action_assignments'
    attributes = ['id', 'action_assignment', 'intra_extension_id', 'action_id', 'action_category_id']
    id = sql.Column(sql.String(64), primary_key=True)
    action_assignment = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)
    action_id = sql.Column(sql.ForeignKey("actions.id"), nullable=False)
    action_category_id = sql.Column(sql.ForeignKey("action_categories.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class SubMetaRule(sql.ModelBase, sql.DictBase):
    __tablename__ = 'sub_meta_rules'
    attributes = ['id', 'sub_meta_rule', 'intra_extension_id']
    id = sql.Column(sql.String(64), primary_key=True)
    sub_meta_rule = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


class Rule(sql.ModelBase, sql.DictBase):
    __tablename__ = 'rules'
    attributes = ['id', 'rule', 'intra_extension_id', 'sub_meta_rule_id']
    id = sql.Column(sql.String(64), primary_key=True)
    rule = sql.Column(sql.JsonBlob(), nullable=True)
    intra_extension_id = sql.Column(sql.ForeignKey("intra_extensions.id"), nullable=False)
    sub_meta_rule_id = sql.Column(sql.ForeignKey("sub_meta_rules.id"), nullable=False)

    @classmethod
    def from_dict(cls, d):
        new_d = d.copy()
        return cls(**new_d)

    def to_dict(self):
        return dict(six.iteritems(self))


__all_objects__ = (
    SubjectScope,
    ObjectScope,
    ActionScope,
    SubjectAssignment,
    ObjectAssignment,
    ActionAssignment,
    SubMetaRule,
    SubjectCategory,
    ObjectCategory,
    ActionCategory,
    Subject,
    Object,
    Action,
    Rule,
)


class TenantConnector(TenantDriver):

    @staticmethod
    def __update_dict(base, update):
        """Update a dict only if values are not None

        :param base: dict to update
        :param update: updates for the base dict
        :return: None
        """
        for key in update:
            if type(update[key]) is not None:
                base[key] = update[key]

    def get_tenants_dict(self):
        with sql.session_for_read() as session:
            query = session.query(Tenant)
            tenants = query.all()
            return {tenant.id: tenant.tenant for tenant in tenants}

    def add_tenant_dict(self, tenant_id, tenant_dict):
        with sql.session_for_write() as session:
            new_ref = Tenant.from_dict(
                {
                    "id": tenant_id,
                    'tenant': tenant_dict
                }
            )
            session.add(new_ref)
            return {new_ref.id: new_ref.tenant}

    def del_tenant(self, tenant_id):
        with sql.session_for_write() as session:
            query = session.query(Tenant)
            query = query.filter_by(id=tenant_id)
            tenant = query.first()
            session.delete(tenant)

    def set_tenant_dict(self, tenant_id, tenant_dict):
        with sql.session_for_write() as session:
            query = session.query(Tenant)
            query = query.filter_by(id=tenant_id)
            ref = query.first()
            tenant_dict_orig = dict(ref.tenant)
            self.__update_dict(tenant_dict_orig, tenant_dict)
            setattr(ref, "tenant", tenant_dict_orig)
            return {ref.id: tenant_dict_orig}


class IntraExtensionConnector(IntraExtensionDriver):

    # IntraExtension functions

    def get_intra_extensions_dict(self):
        with sql.session_for_read() as session:
            query = session.query(IntraExtension)
            ref_list = query.all()
            return {_ref.id: _ref.intra_extension for _ref in ref_list}

    def del_intra_extension(self, intra_extension_id):
        with sql.session_for_write() as session:
            ref = session.query(IntraExtension).get(intra_extension_id)
            # Must delete all references to that IntraExtension
            for _object in __all_objects__:
                query = session.query(_object)
                query = query.filter_by(intra_extension_id=intra_extension_id)
                _refs = query.all()
                for _ref in _refs:
                    session.delete(_ref)
            # session.flush()
            session.delete(ref)

    def set_intra_extension_dict(self, intra_extension_id, intra_extension_dict):
        with sql.session_for_write() as session:
            query = session.query(IntraExtension)
            query = query.filter_by(id=intra_extension_id)
            ref = query.first()
            new_intra_extension = IntraExtension.from_dict(
                {
                    "id": intra_extension_id,
                    'intra_extension': intra_extension_dict,
                }
            )
            if not ref:
                session.add(new_intra_extension)
                ref = new_intra_extension
            else:
                for attr in IntraExtension.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_intra_extension, attr))
            # session.flush()
            return IntraExtension.to_dict(ref)

    # Getter and Setter for subject_category

    def get_subject_categories_dict(self, intra_extension_id):
        with sql.session_for_read() as session:
            query = session.query(SubjectCategory)
            query = query.filter_by(intra_extension_id=intra_extension_id)
            ref_list = query.all()
            return {_ref.id: _ref.subject_category for _ref in ref_list}

    def set_subject_category_dict(self, intra_extension_id, subject_category_id, subject_category_dict):
        with sql.session_for_write() as session:
            query = session.query(SubjectCategory)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=subject_category_id)
            ref = query.first()
            new_ref = SubjectCategory.from_dict(
                {
                    "id": subject_category_id,
                    'subject_category': subject_category_dict,
                    'intra_extension_id': intra_extension_id
                }
            )
            if not ref:
                session.add(new_ref)
                ref = new_ref
            else:
                for attr in SubjectCategory.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # # session.flush()
            return {subject_category_id: SubjectCategory.to_dict(ref)['subject_category']}

    def del_subject_category(self, intra_extension_id, subject_category_id):
        with sql.session_for_write() as session:
            query = session.query(SubjectCategory)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=subject_category_id)
            ref = query.first()
            self.del_subject_assignment(intra_extension_id, None, None, None)
            session.delete(ref)

    # Getter and Setter for object_category

    def get_object_categories_dict(self, intra_extension_id):
        with sql.session_for_read() as session:
            query = session.query(ObjectCategory)
            query = query.filter_by(intra_extension_id=intra_extension_id)
            ref_list = query.all()
            return {_ref.id: _ref.object_category for _ref in ref_list}

    def set_object_category_dict(self, intra_extension_id, object_category_id, object_category_dict):
        with sql.session_for_write() as session:
            query = session.query(ObjectCategory)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=object_category_id)
            ref = query.first()
            new_ref = ObjectCategory.from_dict(
                {
                    "id": object_category_id,
                    'object_category': object_category_dict,
                    'intra_extension_id': intra_extension_id
                }
            )
            if not ref:
                session.add(new_ref)
                ref = new_ref
            else:
                for attr in ObjectCategory.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return {object_category_id: ObjectCategory.to_dict(ref)['object_category']}

    def del_object_category(self, intra_extension_id, object_category_id):
        with sql.session_for_write() as session:
            query = session.query(ObjectCategory)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=object_category_id)
            ref = query.first()
            self.del_object_assignment(intra_extension_id, None, None, None)
            session.delete(ref)

    # Getter and Setter for action_category

    def get_action_categories_dict(self, intra_extension_id):
        with sql.session_for_read() as session:
            query = session.query(ActionCategory)
            query = query.filter_by(intra_extension_id=intra_extension_id)
            ref_list = query.all()
            return {_ref.id: _ref.action_category for _ref in ref_list}

    def set_action_category_dict(self, intra_extension_id, action_category_id, action_category_dict):
        with sql.session_for_write() as session:
            query = session.query(ActionCategory)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=action_category_id)
            ref = query.first()
            new_ref = ActionCategory.from_dict(
                {
                    "id": action_category_id,
                    'action_category': action_category_dict,
                    'intra_extension_id': intra_extension_id
                }
            )
            if not ref:
                session.add(new_ref)
                ref = new_ref
            else:
                for attr in ActionCategory.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return {action_category_id: ActionCategory.to_dict(ref)['action_category']}

    def del_action_category(self, intra_extension_id, action_category_id):
        with sql.session_for_write() as session:
            query = session.query(ActionCategory)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=action_category_id)
            ref = query.first()
            self.del_action_assignment(intra_extension_id, None, None, None)
            session.delete(ref)

    # Perimeter

    def get_subjects_dict(self, intra_extension_id):
        with sql.session_for_read() as session:
            query = session.query(Subject)
            query = query.filter_by(intra_extension_id=intra_extension_id)
            ref_list = query.all()
            return {_ref.id: _ref.subject for _ref in ref_list}

    def set_subject_dict(self, intra_extension_id, subject_id, subject_dict):
        with sql.session_for_write() as session:
            query = session.query(Subject)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=subject_id)
            ref = query.first()
            # if 'id' in subject_dict:
            #     subject_dict['id'] = subject_id
            new_ref = Subject.from_dict(
                {
                    "id": subject_id,
                    'subject': subject_dict,
                    'intra_extension_id': intra_extension_id
                }
            )
            if not ref:
                session.add(new_ref)
                ref = new_ref
            else:
                for attr in Subject.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return {subject_id: Subject.to_dict(ref)['subject']}

    def del_subject(self, intra_extension_id, subject_id):
        with sql.session_for_write() as session:
            query = session.query(Subject)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=subject_id)
            ref = query.first()
            session.delete(ref)

    def get_objects_dict(self, intra_extension_id):
        with sql.session_for_read() as session:
            query = session.query(Object)
            query = query.filter_by(intra_extension_id=intra_extension_id)
            ref_list = query.all()
            return {_ref.id: _ref.object for _ref in ref_list}

    def set_object_dict(self, intra_extension_id, object_id, object_dict):
        with sql.session_for_write() as session:
            query = session.query(Object)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=object_id)
            ref = query.first()
            new_ref = Object.from_dict(
                {
                    "id": object_id,
                    'object': object_dict,
                    'intra_extension_id': intra_extension_id
                }
            )
            if not ref:
                session.add(new_ref)
                ref = new_ref
            else:
                for attr in Object.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return {object_id: Object.to_dict(ref)['object']}

    def del_object(self, intra_extension_id, object_id):
        with sql.session_for_write() as session:
            query = session.query(Object)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=object_id)
            ref = query.first()
            session.delete(ref)

    def get_actions_dict(self, intra_extension_id):
        with sql.session_for_read() as session:
            query = session.query(Action)
            query = query.filter_by(intra_extension_id=intra_extension_id)
            ref_list = query.all()
            return {_ref.id: _ref.action for _ref in ref_list}

    def set_action_dict(self, intra_extension_id, action_id, action_dict):
        with sql.session_for_write() as session:
            query = session.query(Action)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=action_id)
            ref = query.first()
            new_ref = Action.from_dict(
                {
                    "id": action_id,
                    'action': action_dict,
                    'intra_extension_id': intra_extension_id
                }
            )
            if not ref:
                session.add(new_ref)
                ref = new_ref
            else:
                for attr in Action.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return {action_id: Action.to_dict(ref)['action']}

    def del_action(self, intra_extension_id, action_id):
        with sql.session_for_write() as session:
            query = session.query(Action)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=action_id)
            ref = query.first()
            session.delete(ref)

    # Getter and Setter for subject_scope

    def get_subject_scopes_dict(self, intra_extension_id, subject_category_id):
        with sql.session_for_read() as session:
            query = session.query(SubjectScope)
            query = query.filter_by(intra_extension_id=intra_extension_id, subject_category_id=subject_category_id)
            ref_list = query.all()
            return {_ref.id: _ref.subject_scope for _ref in ref_list}

    def set_subject_scope_dict(self, intra_extension_id, subject_category_id, subject_scope_id, subject_scope_dict):
        with sql.session_for_write() as session:
            query = session.query(SubjectScope)
            query = query.filter_by(intra_extension_id=intra_extension_id, subject_category_id=subject_category_id, id=subject_scope_id)
            ref = query.first()
            new_ref = SubjectScope.from_dict(
                {
                    "id": subject_scope_id,
                    'subject_scope': subject_scope_dict,
                    'intra_extension_id': intra_extension_id,
                    'subject_category_id': subject_category_id
                }
            )
            if not ref:
                session.add(new_ref)
                ref = new_ref
            else:
                for attr in Subject.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return {subject_scope_id: SubjectScope.to_dict(ref)['subject_scope']}

    def del_subject_scope(self, intra_extension_id, subject_category_id, subject_scope_id):
        with sql.session_for_write() as session:
            query = session.query(SubjectScope)
            if not subject_category_id or not subject_scope_id:
                query = query.filter_by(intra_extension_id=intra_extension_id)
                for ref in query.all():
                    session.delete(ref)
            else:
                query = query.filter_by(intra_extension_id=intra_extension_id, subject_category_id=subject_category_id, id=subject_scope_id)
                ref = query.first()
                session.delete(ref)

    # Getter and Setter for object_category_scope

    def get_object_scopes_dict(self, intra_extension_id, object_category_id):
        with sql.session_for_read() as session:
            query = session.query(ObjectScope)
            query = query.filter_by(intra_extension_id=intra_extension_id, object_category_id=object_category_id)
            ref_list = query.all()
            return {_ref.id: _ref.object_scope for _ref in ref_list}

    def set_object_scope_dict(self, intra_extension_id, object_category_id, object_scope_id, object_scope_dict):
        with sql.session_for_write() as session:
            query = session.query(ObjectScope)
            query = query.filter_by(intra_extension_id=intra_extension_id, object_category_id=object_category_id, id=object_scope_id)
            ref = query.first()
            new_ref = ObjectScope.from_dict(
                {
                    "id": object_scope_id,
                    'object_scope': object_scope_dict,
                    'intra_extension_id': intra_extension_id,
                    'object_category_id': object_category_id
                }
            )
            if not ref:
                session.add(new_ref)
                ref = new_ref
            else:
                for attr in Object.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return {object_scope_id: ObjectScope.to_dict(ref)['object_scope']}

    def del_object_scope(self, intra_extension_id, object_category_id, object_scope_id):
        with sql.session_for_write() as session:
            query = session.query(ObjectScope)
            if not object_category_id or not object_scope_id:
                query = query.filter_by(intra_extension_id=intra_extension_id)
                for ref in query.all():
                    session.delete(ref)
            else:
                query = query.filter_by(intra_extension_id=intra_extension_id, object_category_id=object_category_id, id=object_scope_id)
                ref = query.first()
                session.delete(ref)

    # Getter and Setter for action_scope
 
    def get_action_scopes_dict(self, intra_extension_id, action_category_id):
        with sql.session_for_read() as session:
            query = session.query(ActionScope)
            query = query.filter_by(intra_extension_id=intra_extension_id, action_category_id=action_category_id)
            ref_list = query.all()
            return {_ref.id: _ref.action_scope for _ref in ref_list}

    def set_action_scope_dict(self, intra_extension_id, action_category_id, action_scope_id, action_scope_dict):
        with sql.session_for_write() as session:
            query = session.query(ActionScope)
            query = query.filter_by(intra_extension_id=intra_extension_id, action_category_id=action_category_id, id=action_scope_id)
            ref = query.first()
            new_ref = ActionScope.from_dict(
                {
                    "id": action_scope_id,
                    'action_scope': action_scope_dict,
                    'intra_extension_id': intra_extension_id,
                    'action_category_id': action_category_id
                }
            )
            if not ref:
                session.add(new_ref)
                ref = new_ref
            else:
                for attr in Action.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return {action_scope_id: ActionScope.to_dict(ref)['action_scope']}

    def del_action_scope(self, intra_extension_id, action_category_id, action_scope_id):
        with sql.session_for_write() as session:
            query = session.query(ActionScope)
            if not action_category_id or not action_scope_id:
                query = query.filter_by(intra_extension_id=intra_extension_id)
                for ref in query.all():
                    session.delete(ref)
            else:
                query = query.filter_by(intra_extension_id=intra_extension_id, action_category_id=action_category_id, id=action_scope_id)
                ref = query.first()
                session.delete(ref)

    # Getter and Setter for subject_category_assignment

    def get_subject_assignment_list(self, intra_extension_id, subject_id, subject_category_id):
        with sql.session_for_read() as session:
            query = session.query(SubjectAssignment)
            if not subject_id or not subject_category_id or not subject_category_id:
                query = query.filter_by(intra_extension_id=intra_extension_id)
                ref = query.all()
                return ref
            else:
                query = query.filter_by(intra_extension_id=intra_extension_id, subject_id=subject_id, subject_category_id=subject_category_id)
                ref = query.first()
            if not ref:
                return list()
            return list(ref.subject_assignment)

    def set_subject_assignment_list(self, intra_extension_id, subject_id, subject_category_id, subject_assignment_list=[]):
        with sql.session_for_write() as session:
            query = session.query(SubjectAssignment)
            query = query.filter_by(intra_extension_id=intra_extension_id, subject_id=subject_id, subject_category_id=subject_category_id)
            ref = query.first()
            new_ref = SubjectAssignment.from_dict(
                {
                    "id": uuid4().hex,
                    'subject_assignment': subject_assignment_list,
                    'intra_extension_id': intra_extension_id,
                    'subject_id': subject_id,
                    'subject_category_id': subject_category_id
                }
            )
            if not ref:
                session.add(new_ref)
                ref = new_ref
            else:
                for attr in SubjectAssignment.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return subject_assignment_list

    def add_subject_assignment_list(self, intra_extension_id, subject_id, subject_category_id, subject_scope_id):
        new_subject_assignment_list = self.get_subject_assignment_list(intra_extension_id, subject_id, subject_category_id)
        if subject_scope_id not in new_subject_assignment_list:
            new_subject_assignment_list.append(subject_scope_id)
        return self.set_subject_assignment_list(intra_extension_id, subject_id, subject_category_id, new_subject_assignment_list)

    def del_subject_assignment(self, intra_extension_id, subject_id, subject_category_id, subject_scope_id):
        if not subject_id or not subject_category_id or not subject_category_id:
            with sql.session_for_write() as session:
                for ref in self.get_subject_assignment_list(intra_extension_id, None, None):
                    session.delete(ref)
                session.flush()
                return
        new_subject_assignment_list = self.get_subject_assignment_list(intra_extension_id, subject_id, subject_category_id)
        new_subject_assignment_list.remove(subject_scope_id)
        return self.set_subject_assignment_list(intra_extension_id, subject_id, subject_category_id, new_subject_assignment_list)

    # Getter and Setter for object_category_assignment

    def get_object_assignment_list(self, intra_extension_id, object_id, object_category_id):
        with sql.session_for_read() as session:
            query = session.query(ObjectAssignment)
            if not object_id or not object_category_id or not object_category_id:
                query = query.filter_by(intra_extension_id=intra_extension_id)
                ref = query.all()
                return ref
            else:
                query = query.filter_by(intra_extension_id=intra_extension_id, object_id=object_id, object_category_id=object_category_id)
                ref = query.first()
            if not ref:
                return list()
            return list(ref.object_assignment)

    def set_object_assignment_list(self, intra_extension_id, object_id, object_category_id, object_assignment_list=[]):
        with sql.session_for_write() as session:
            query = session.query(ObjectAssignment)
            query = query.filter_by(intra_extension_id=intra_extension_id, object_id=object_id, object_category_id=object_category_id)
            ref = query.first()
            new_ref = ObjectAssignment.from_dict(
                {
                    "id": uuid4().hex,
                    'object_assignment': object_assignment_list,
                    'intra_extension_id': intra_extension_id,
                    'object_id': object_id,
                    'object_category_id': object_category_id
                }
            )
            if not ref:
                session.add(new_ref)
            else:
                for attr in ObjectAssignment.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return self.get_object_assignment_list(intra_extension_id, object_id, object_category_id)

    def add_object_assignment_list(self, intra_extension_id, object_id, object_category_id, object_scope_id):
        new_object_assignment_list = self.get_object_assignment_list(intra_extension_id, object_id, object_category_id)
        if object_scope_id not in new_object_assignment_list:
            new_object_assignment_list.append(object_scope_id)
        return self.set_object_assignment_list(intra_extension_id, object_id, object_category_id, new_object_assignment_list)

    def del_object_assignment(self, intra_extension_id, object_id, object_category_id, object_scope_id):
        if not object_id or not object_category_id or not object_category_id:
            with sql.session_for_write() as session:
                for ref in self.get_object_assignment_list(intra_extension_id, None, None):
                    session.delete(ref)
                session.flush()
                return
        new_object_assignment_list = self.get_object_assignment_list(intra_extension_id, object_id, object_category_id)
        new_object_assignment_list.remove(object_scope_id)
        return self.set_object_assignment_list(intra_extension_id, object_id, object_category_id, new_object_assignment_list)

    # Getter and Setter for action_category_assignment

    def get_action_assignment_list(self, intra_extension_id, action_id, action_category_id):
        with sql.session_for_read() as session:
            query = session.query(ActionAssignment)
            if not action_id or not action_category_id or not action_category_id:
                query = query.filter_by(intra_extension_id=intra_extension_id)
                ref = query.all()
                return ref
            else:
                query = query.filter_by(intra_extension_id=intra_extension_id, action_id=action_id, action_category_id=action_category_id)
                ref = query.first()
            if not ref:
                return list()
            return list(ref.action_assignment)

    def set_action_assignment_list(self, intra_extension_id, action_id, action_category_id, action_assignment_list=[]):
        with sql.session_for_write() as session:
            query = session.query(ActionAssignment)
            query = query.filter_by(intra_extension_id=intra_extension_id, action_id=action_id, action_category_id=action_category_id)
            ref = query.first()
            new_ref = ActionAssignment.from_dict(
                {
                    "id": uuid4().hex,
                    'action_assignment': action_assignment_list,
                    'intra_extension_id': intra_extension_id,
                    'action_id': action_id,
                    'action_category_id': action_category_id
                }
            )
            if not ref:
                session.add(new_ref)
            else:
                for attr in ActionAssignment.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return self.get_action_assignment_list(intra_extension_id, action_id, action_category_id)

    def add_action_assignment_list(self, intra_extension_id, action_id, action_category_id, action_scope_id):
        new_action_assignment_list = self.get_action_assignment_list(intra_extension_id, action_id, action_category_id)
        if action_scope_id not in new_action_assignment_list:
            new_action_assignment_list.append(action_scope_id)
        return self.set_action_assignment_list(intra_extension_id, action_id, action_category_id, new_action_assignment_list)

    def del_action_assignment(self, intra_extension_id, action_id, action_category_id, action_scope_id):
        if not action_id or not action_category_id or not action_category_id:
            with sql.session_for_write() as session:
                for ref in self.get_action_assignment_list(intra_extension_id, None, None):
                    session.delete(ref)
                session.flush()
                return
        new_action_assignment_list = self.get_action_assignment_list(intra_extension_id, action_id, action_category_id)
        new_action_assignment_list.remove(action_scope_id)
        return self.set_action_assignment_list(intra_extension_id, action_id, action_category_id, new_action_assignment_list)

    # Getter and Setter for sub_meta_rule

    def get_aggregation_algorithm_id(self, intra_extension_id):
        with sql.session_for_read() as session:
            query = session.query(IntraExtension)
            query = query.filter_by(id=intra_extension_id)
            ref = query.first()
            try:
                return {"aggregation_algorithm": ref.intra_extension["aggregation_algorithm"]}
            except KeyError:
                return ""

    def set_aggregation_algorithm_id(self, intra_extension_id, aggregation_algorithm_id):
        with sql.session_for_write() as session:
            query = session.query(IntraExtension)
            query = query.filter_by(id=intra_extension_id)
            ref = query.first()
            intra_extension_dict = dict(ref.intra_extension)
            intra_extension_dict["aggregation_algorithm"] = aggregation_algorithm_id
            setattr(ref, "intra_extension", intra_extension_dict)
            # session.flush()
            return {"aggregation_algorithm": ref.intra_extension["aggregation_algorithm"]}

    def del_aggregation_algorithm(self, intra_extension_id):
        with sql.session_for_write() as session:
            query = session.query(IntraExtension)
            query = query.filter_by(id=intra_extension_id)
            ref = query.first()
            intra_extension_dict = dict(ref.intra_extension)
            intra_extension_dict["aggregation_algorithm"] = ""
            setattr(ref, "intra_extension", intra_extension_dict)
            return self.get_aggregation_algorithm_id(intra_extension_id)

    # Getter and Setter for sub_meta_rule

    def get_sub_meta_rules_dict(self, intra_extension_id):
        with sql.session_for_read() as session:
            query = session.query(SubMetaRule)
            query = query.filter_by(intra_extension_id=intra_extension_id)
            ref_list = query.all()
            return {_ref.id: _ref.sub_meta_rule for _ref in ref_list}

    def set_sub_meta_rule_dict(self, intra_extension_id, sub_meta_rule_id, sub_meta_rule_dict):
        with sql.session_for_write() as session:
            query = session.query(SubMetaRule)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=sub_meta_rule_id)
            ref = query.first()
            new_ref = SubMetaRule.from_dict(
                {
                    "id": sub_meta_rule_id,
                    'sub_meta_rule': sub_meta_rule_dict,
                    'intra_extension_id': intra_extension_id
                }
            )
            if not ref:
                session.add(new_ref)
            else:
                _sub_meta_rule_dict = dict(ref.sub_meta_rule)
                _sub_meta_rule_dict.update(sub_meta_rule_dict)
                setattr(new_ref, "sub_meta_rule", _sub_meta_rule_dict)
                for attr in SubMetaRule.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return self.get_sub_meta_rules_dict(intra_extension_id)

    def del_sub_meta_rule(self, intra_extension_id, sub_meta_rule_id):
        with sql.session_for_write() as session:
            query = session.query(SubMetaRule)
            query = query.filter_by(intra_extension_id=intra_extension_id, id=sub_meta_rule_id)
            ref = query.first()
            session.delete(ref)

    # Getter and Setter for rules

    def get_rules_dict(self, intra_extension_id, sub_meta_rule_id):
        with sql.session_for_read() as session:
            query = session.query(Rule)
            query = query.filter_by(intra_extension_id=intra_extension_id, sub_meta_rule_id=sub_meta_rule_id)
            ref_list = query.all()
            return {_ref.id: _ref.rule for _ref in ref_list}

    def set_rule_dict(self, intra_extension_id, sub_meta_rule_id, rule_id, rule_list):
        with sql.session_for_write() as session:
            query = session.query(Rule)
            query = query.filter_by(intra_extension_id=intra_extension_id, sub_meta_rule_id=sub_meta_rule_id, id=rule_id)
            ref = query.first()
            new_ref = Rule.from_dict(
                {
                    "id": rule_id,
                    'rule': rule_list,
                    'intra_extension_id': intra_extension_id,
                    'sub_meta_rule_id': sub_meta_rule_id
                }
            )
            if not ref:
                session.add(new_ref)
                ref = new_ref
            else:
                for attr in Rule.attributes:
                    if attr != 'id':
                        setattr(ref, attr, getattr(new_ref, attr))
            # session.flush()
            return {rule_id: ref.rule}

    def del_rule(self, intra_extension_id, sub_meta_rule_id, rule_id):
        with sql.session_for_write() as session:
            query = session.query(Rule)
            query = query.filter_by(intra_extension_id=intra_extension_id, sub_meta_rule_id=sub_meta_rule_id, id=rule_id)
            ref = query.first()
            session.delete(ref)


# class InterExtension(sql.ModelBase, sql.DictBase):
#     __tablename__ = 'inter_extension'
#     attributes = [
#         'id',
#         'requesting_intra_extension_id',
#         'requested_intra_extension_id',
#         'virtual_entity_uuid',
#         'genre',
#         'description',
#     ]
#     id = sql.Column(sql.String(64), primary_key=True)
#     requesting_intra_extension_id = sql.Column(sql.String(64))
#     requested_intra_extension_id = sql.Column(sql.String(64))
#     virtual_entity_uuid = sql.Column(sql.String(64))
#     genre = sql.Column(sql.String(64))
#     description = sql.Column(sql.Text())
#
#     @classmethod
#     def from_dict(cls, d):
#         """Override parent from_dict() method with a simpler implementation.
#         """
#         new_d = d.copy()
#         return cls(**new_d)
#
#     def to_dict(self):
#         """Override parent to_dict() method with a simpler implementation.
#         """
#         return dict(six.iteritems(self))
#
#
# class InterExtensionConnector(InterExtensionDriver):
#
#     def get_inter_extensions(self):
#         with sql.session_for_read() as session:
#             query = session.query(InterExtension.id)
#             interextensions = query.all()
#             return [interextension.id for interextension in interextensions]
#
#     def create_inter_extensions(self, inter_id, inter_extension):
#         with sql.session_for_read() as session:
#             ie_ref = InterExtension.from_dict(inter_extension)
#             session.add(ie_ref)
#         return InterExtension.to_dict(ie_ref)
#
#     def get_inter_extension(self, uuid):
#         with sql.session_for_read() as session:
#             query = session.query(InterExtension)
#             query = query.filter_by(id=uuid)
#             ref = query.first()
#             if not ref:
#                 raise exception.NotFound
#             return ref.to_dict()
#
#     def delete_inter_extensions(self, inter_extension_id):
#         with sql.session_for_read() as session:
#             ref = session.query(InterExtension).get(inter_extension_id)
#             session.delete(ref)

