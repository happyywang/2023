from .cli import main
from .from_issues import get_info_from_issue_comments
from .runner import GTDRunner

MY_STATUS_DICT_FROM_COMMENTS = {
    "周记": {"daily_func": get_info_from_issue_comments, "unit_str": " (周)"},
    "GTD": {"daily_func": get_info_from_issue_comments, "unit_str": " (个)"},
}
