class NotificationType(object):
    """
    Constants regarding the different types of notification we can send to a device
    See https://docs.google.com/document/d/1SV-hNCtgAn2hSMZaC973UdLHCFXCNpvq_RKq0UoY4yg/edit#
    """

    # DO NOT CHANGE THESE CONSTANTS
    UPCOMING_MATCH = 0
    MATCH_SCORE = 1
    LEVEL_STARTING = 2
    ALLIANCE_SELECTION = 3
    AWARDS = 4
    MEDIA_POSTED = 5
    DISTRICT_POINTS_UPDATED = 6
    SCHEDULE_POSTED = 7
    FINAL_RESULTS = 8

    # These aren't notifications, but used for upstream API calls
    UPDATE_FAVORITES = 100
    UPDATE_SUBSCIPTION = 101

    type_names = {
        UPCOMING_MATCH: "upcoming_match",
        MATCH_SCORE: "match_score",
        LEVEL_STARTING: "starting_comp_level",
        ALLIANCE_SELECTION: "alliance_selection",
        AWARDS: "awards_posted",
        MEDIA_POSTED: "media_posted",
        DISTRICT_POINTS_UPDATED: "district_points_updated",
        SCHEDULE_POSTED: "schedule_posted",
        FINAL_RESULTS: "final_results",

        UPDATE_FAVORITES: "update_favorites",
        UPDATE_SUBSCIPTION: "update_subscriptions",
    }

    types = {
        "upcoming_match": UPCOMING_MATCH,
        "match_score": MATCH_SCORE,
        "starting_comp_level": LEVEL_STARTING,
        "alliance_selection": ALLIANCE_SELECTION,
        "awards_posted": AWARDS,
        "media_posted": MEDIA_POSTED,
        "district_points_updated": DISTRICT_POINTS_UPDATED,
        "schedule_posted": SCHEDULE_POSTED,
        "final_results": FINAL_RESULTS,

        "update_favorites": UPDATE_FAVORITES,
        "update_subscriptions": UPDATE_SUBSCIPTION
    }