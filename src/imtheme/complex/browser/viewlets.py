# -*- coding: utf-8 -*-
from plone.app.layout.viewlets import ViewletBase
from plone.app.layout.viewlets.common import SearchBoxViewlet
from Products.CMFCore.utils import getToolByName
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope.component import getMultiAdapter


class ActivitiesViewlet(ViewletBase):
    pass


class LogosViewlet(ViewletBase):

    def is_anonymous(self):
        portal_membership = getToolByName(self.context, 'portal_membership', None)
        return portal_membership.isAnonymousUser()

    def user_actions(self):
        context_state = getMultiAdapter((self.context, self.request),
                                        name=u'plone_context_state')

        actions = context_state.actions('user')
        return actions


class IMSearchBoxViewlet(SearchBoxViewlet):

    def is_anonymous(self):
        portal_membership = getToolByName(self.context, 'portal_membership', None)
        return portal_membership.isAnonymousUser()

    def user_name_home(self):

        portal_membership = getToolByName(self.context, 'portal_membership')
        # authenticated_user = portal_membership.getAuthenticatedMember().getProperty('location')
        userid = portal_membership.getAuthenticatedMember().id
        memberinfo = portal_membership.getMemberInfo(userid)

        if memberinfo:
            fullname = memberinfo.get('fullname', '')
        else:
            fullname = None
        if not fullname:
            fullname = memberinfo.get('username', '')

        homelink = "%s/useractions" % self.navigation_root_url

        return {'name': fullname, 'homelink': homelink}

    def gologin(self):
        return "%s/login" % self.navigation_root_url

    def user_name_logout(self):

        portal_membership = getToolByName(self.context, 'portal_membership')
        userid = portal_membership.getAuthenticatedMember().id
        memberinfo = portal_membership.getMemberInfo(userid)

        if memberinfo:
            fullname = memberinfo.get('fullname', '')
        else:
            fullname = None
        if not fullname:
            fullname = memberinfo.get('username', '')

        # homelink = "%s/useractions/" % self.navigation_root_url
        logoutlink = "%s/logout" % self.navigation_root_url

        return {'name': fullname, 'logoutlink': logoutlink}

