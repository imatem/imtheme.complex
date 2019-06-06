from plone.app.layout.viewlets import ViewletBase
from Products.CMFCore.utils import getToolByName
from plone.app.layout.viewlets.common import SearchBoxViewlet


class ActivitiesViewlet(ViewletBase):
    pass


class LogosViewlet(ViewletBase):
    pass


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

