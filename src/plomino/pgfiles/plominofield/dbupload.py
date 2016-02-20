# -*- coding: utf-8 -*-
#
# File: attachment.py
#
# Copyright (c) 2009 by ['Eric BREHAULT']
#
# Zope Public License (ZPL)
#

__author__ = """Eric BREHAULT <eric.brehault@makina-corpus.com>"""
__docformat__ = 'plaintext'

# Zope
from zope.formlib import form
from zope.interface import implements
from zope import component
from zope.pagetemplate.pagetemplatefile import PageTemplateFile
from zope.schema import getFields, Choice, TextLine
from zope.schema.vocabulary import SimpleVocabulary

# CMF / Archetypes / Plone
from Products.CMFPlone.utils import normalizeString

# Plomino
from Products.CMFPlomino.fields.base import IBaseField, BaseField, BaseForm
from Products.CMFPlomino.interfaces import IPlominoField
from Products.CMFPlomino.fields.dictionaryproperty import DictionaryProperty
from ZPublisher.HTTPRequest import FileUpload


class IDbUploadField(IBaseField):
    """ Attachment field schema
    """
    widget = Choice(
            vocabulary=SimpleVocabulary.fromItems(
                [("Single file", "SINGLE"), ("Multiple files", "MULTI"), ("Download->Upload", "DOWN-UP")]),
                title=u'Type',
                description=u'Single, multiple file(s) or download->upload',
                default="MULTI",
                required=True)

    maxsize = TextLine(
            title=u'Max size',
            description=u'File max size allowed (Mb)',
            required=False)

    filetype = TextLine(
            title=u'File type',
            description=u'File type allowed (separate comma list)',
            required=False)


class DbUploadField(BaseField):
    """
    """
    implements(IDbUploadField)

    plomino_field_parameters = {'interface': IDbUploadField,
                                'label':"DB upload",
                                'index_type':"ZCTextIndex"}

    read_template = PageTemplateFile('templates/dbupload_read.pt')
    edit_template = PageTemplateFile('templates/dbupload_edit.pt')    
    
    def validate(self, submittedValue):
        """
        validate
        """
        errors = []
        return errors


    def processInput(self, submittedValue):
        """
        """
        # only called in during validation
        if not submittedValue:
            return None

        if isinstance(submittedValue, FileUpload):
            doc = self.context.REQUEST.PARENTS[0]
            import pdb;pdb.set_trace()


        #strValue = normalizeString(strValue)
        #return {strValue: 'application/unknown'}

    def getIcon(self):
        """
        """


component.provideUtility(DbUploadField, IPlominoField, 'DBUPLOAD')

for f in getFields(IDbUploadField).values():
    setattr(DbUploadField,
            f.getName(),
            DictionaryProperty(f, 'parameters'))

class SettingForm(BaseForm):
    """
    """
    form_fields = form.Fields(IDbUploadField)
