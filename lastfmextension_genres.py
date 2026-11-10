"""Offline genre selection shared by the Rhythmbox extension."""


def genre_from_tags(tags, whitelist):
    """Return the first allowed tag, normalized as the plugin displays it."""
    for tag in tags:
        if tag.lower() in whitelist:
            return tag.title()
    return None
