from django.urls import re_path

from . import views

urlpatterns = [
    re_path("^user/?$", views.createUser, name="createUser"),
    re_path("^dmusers/?$", views.getDMUsers, name="getDMUsers"),
    re_path("^group/?$", views.createGroup, name="createGroup"),
    re_path("^group/(?P<game>\\d+)/?$", views.getGroupByGame, name="getGroupByGame"),
    re_path("^group/(?P<languages>\\w+)/?$", views.getGroupByLanguage, name="getGroupByLanguage"),
    re_path("^groupnodm/?$", views.getGroupWithoutDM, name="getGroupWithoutDM"),
    re_path("^game/?$", views.createGame, name="createGame"),
    re_path("^game/(?P<game_id>\\d+)/id/?$", views.getGameByID, name="getGameByID"),
    re_path("^denyApplication/(?P<application_id>\\d+)/?$", views.denyApplication, name="denyApplication"),
    re_path("^acceptApplication/(?P<application_id>\\d+)/?$", views.acceptApplication, name="acceptApplication"),
    re_path("^kickPlayer/?$", views.kickPlayer, name="kickPlayer"),
    re_path("^invitePlayer/?$", views.invitePlayer, name="invitePlayer"),
    re_path("^applyToGroup/?$", views.applyToGroup, name="applyToGroup"),
    re_path("^cancelApplication/?$", views.cancelApplication, name="cancelApplication"),
    re_path("^getGroupSessions/(?P<group_id>\\d+)/?$", views.getGroupSessions, name="getGroupSessions"),
    re_path("^addGroupTags/?$", views.addGroupTags, name="addGroupTags"),
    re_path("^removeGroupTags/?$", views.removeGroupTags, name="removeGroupTags"),
    re_path("^addPlayerPreference/?$", views.addPlayerPreference, name="addPlayerPreference"),
    re_path("^removePlayerPreference/?$", views.removePlayerPreference, name="removePlayerPreference"),
    re_path("^users/?$", views.getAllUsers, name="getAllUsers"),
    re_path("^groups/?$", views.getAllGroups, name="getAllGroups"),
    re_path("^games/?$", views.getAllGames, name="getAllGames"),
    re_path("^groups/filter_open/?$", views.getOpenGroups, name="getOpenGroups"),
    re_path("^groups/filter_tags/?$", views.getGroupsWithTags, name="getGroupsWithTags"),
    re_path("^groups/exclude_tags/?$", views.getGroupsWithoutTags, name="getGroupsWithoutTags"),
    re_path("^user/(?P<user_id>\\d+)/schedule/?$", views.getUserSchedule, name="getUserSchedule"),
    re_path("^application/(?P<app_id>\\d+)/chat/?$", views.getAppChat, name="getAppChat"),
    re_path("^user/(?P<user_id>\\d+)/id/?$", views.getUserByID, name="getUserByID"),
    re_path("^user/(?P<user_id>\\d+)/update/?$", views.updateUser, name="updateUser"),
    re_path("^group/(?P<group_id>\\d+)/update/?$", views.updateGroup, name="updateGroup"),
    re_path("^user/(?P<user_id>\\d+)/groups/?$", views.getUserGroups, name="getUserGroups"),
    re_path("^group/(?P<group_id>\\d+)/owner/?$", views.getGroupOwner, name="getGroupOwner"),
    re_path("^user/(?P<user_id>\\d+)/preferences/?$", views.getPlayerPreferences, name="getPlayerPreferences"),
    re_path("^group/(?P<group_id>\\d+)/tags/?$", views.getGroupTags, name="getGroupTags"),
    re_path("^user/(?P<user_id>\\d+)/sessions/?$", views.getUserSessions, name="getUserSessions"),
    re_path("^user/(?P<user_id>\\d+)/ownedGroups/?$", views.getOwnedGroups, name="getOwnedGroups"),
    re_path("^group/(?P<group_id>\\d+)/delete/?$", views.deleteGroup, name="deleteGroup"),
    re_path("^group/(?P<group_id>\\d+)/setOwner/?$", views.setGroupOwner, name="setGroupOwner"),
    re_path("^group/(?P<group_id>\\d+)/setNickname/?$", views.setGroupUserNickname, name="setGroupUserNickname"),
    re_path("^user/(?P<user_id>\\d+)/applications/?$", views.getUserApplications, name="getUserApplications"),
    re_path("^group/(?P<group_id>\\d+)/applications/?$", views.getGroupApplications, name="getGroupApplications"),
    re_path("^tags/?$", views.getAllTags, name="getAllTags"),
    re_path("^tag/create/?$", views.createTag, name="createTag"),
    re_path("^group/(?P<group_id>\\d+)/chat/?$", views.getGroupChat, name="getGroupChat"),
    re_path("^group/(?P<group_id>\\d+)/applications/?$", views.getGroupApps, name="getGroupApps"),
    re_path("^group/(?P<group_id>\\d+)/players/?$", views.getGroupPlayers, name="getGroupPlayers"),
    re_path("^group/(?P<group_id>\\d+)/id/?$", views.getGroupByID, name="getGroupByID"),
    re_path("^group/(?P<group_name>\\w+)/name/?$", views.getGroupByName, name="getGroupByName"),
    re_path("^group/by/description/?$", views.getGroupByDescription, name="getGroupByDescription"),
    re_path("^users/(?P<tag_id>\\d+)/preference/?$", views.getUsersByPreference, name="getUsersByPreference"),
    re_path("^users/(?P<tag_id>\\d+)/avoidance/?$", views.getUsersByAvoidance, name="getUsersByAvoidance"),
    re_path("^chat/(?P<chat_id>\\d+)/?$", views.getChatMessages, name="getChatMessages"),
    re_path("^chatmessage/create/?$", views.createChatMessage, name="createChatMessage"),
    re_path("^chatmessage/(?P<chatmessage_id>\\d+)/edit/?$", views.editChatMessage, name="editChatMessage"),
    re_path("^chatmessage/(?P<chatmessage_id>\\d+)/delete/?$", views.deleteChatMessage, name="deleteChatMessage"),
    re_path("^schedule/create/?$", views.createSchedule, name="createSchedule"),
    re_path("^schedule/(?P<sched_id>\\d+)/edit/?$", views.editSchedule, name="editSchedule"),
    re_path("^schedule/(?P<sched_id>\\d+)/delete/?$", views.deleteSchedule, name="deleteSchedule"),
    re_path("^group/(?P<group_id>\\d+)/dm/(?P<user_id>\\d+)/?$", views.changeDM, name="changeDM"),
    re_path("^group/(?P<group_id>\\d+)/owner/(?P<user_id>\\d+)/?$", views.changeOwner, name="changeOwner"),
    re_path("^user/(?P<user_id>\\d+)/tags/looking/?$", views.getUserTagsLooking, name="getUserTagsLooking"),
    re_path("^user/(?P<user_id>\\d+)/tags/avoiding/?$", views.getUserTagsAvoiding, name="getUserTagsAvoiding"),
    re_path("^application/(?P<app_id>\\d+)/id/?$", views.getAppById, name="getAppById")
]
