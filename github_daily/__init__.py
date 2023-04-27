from .from_issues import get_info_from_issue_comments
from .runner import GTDRunner

MY_STATUS_DICT_FROM_API = {
   # "番茄": {
   #     "daily_func": get_forst_daily,
   #     "url": "https://github.com/yihong0618/2023/issues/12",
   #     "unit_str": " (个)",
   # },
}

MY_STATUS_DICT_FROM_COMMENTS = {
    "周记": {"daily_func": get_info_from_issue_comments, "unit_str": " (周)"},
    "GTD": {"daily_func": get_info_from_issue_comments, "unit_str": " (个)"},
}
