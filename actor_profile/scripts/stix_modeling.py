#!/usr/bin/env python3
"""Shared STIX modeling decisions for canonical activity records.

The source ``activity_type`` describes what the source reported.  It is not a
STIX object type.  Keeping this decision in one place prevents generators from
silently turning every news item or single intrusion into a Campaign.
"""

from __future__ import annotations

from typing import Any


STIX_ACTIVITY_TYPES = {"campaign", "incident", "grouping"}
GROUPING_CONTEXTS = {"suspicious-activity", "malware-analysis", "unspecified"}

# These source labels do not, by themselves, establish a coherent campaign.
# ``reported-activity`` is deliberately conservative: an analyst can promote a
# specific record by setting ``stix_object_type`` explicitly after review.
DEFAULT_GROUPING_ACTIVITY_TYPES = {
    "historical-activity-cluster",
    "information-collection",
    "reported-activity",
}

# A record explicitly modeled as one intrusion is an Incident.  A multi-event
# wave can still be overridden to Campaign in the canonical record.
DEFAULT_INCIDENT_ACTIVITY_TYPES = {"intrusion"}


def default_stix_object_type(activity_type: str) -> str:
    """Return the conservative default STIX object type for an activity label."""

    if activity_type in DEFAULT_GROUPING_ACTIVITY_TYPES:
        return "grouping"
    if activity_type in DEFAULT_INCIDENT_ACTIVITY_TYPES:
        return "incident"
    return "campaign"


def activity_stix_object_type(activity: dict[str, Any]) -> str:
    """Return an explicit valid type, falling back only for legacy input."""

    explicit = activity.get("stix_object_type")
    if explicit in STIX_ACTIVITY_TYPES:
        return str(explicit)
    return default_stix_object_type(str(activity.get("activity_type", "")))


def apply_activity_modeling_defaults(activity: dict[str, Any]) -> bool:
    """Populate required modeling fields without overriding analyst decisions."""

    changed = False
    if activity.get("stix_object_type") not in STIX_ACTIVITY_TYPES:
        activity["stix_object_type"] = default_stix_object_type(
            str(activity.get("activity_type", ""))
        )
        changed = True
    if "activity_refs" not in activity:
        activity["activity_refs"] = []
        changed = True
    context = activity.get("grouping_context")
    if activity["stix_object_type"] == "grouping":
        if context not in GROUPING_CONTEXTS:
            activity["grouping_context"] = "suspicious-activity"
            changed = True
    elif context is not None:
        activity["grouping_context"] = None
        changed = True
    elif "grouping_context" not in activity:
        activity["grouping_context"] = None
        changed = True
    return changed
