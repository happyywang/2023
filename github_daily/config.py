# if you are not me change here
YEAR = 2023
REPO_NAME = f"happyywang/{YEAR}"

READ_LABEL_LIST = [
    "Read",
]
DRAMA_LABEL_LIST = [
    "Drama",
]
TODO_LABEL_LIST = [
    "ToDo",
]
BANGUMI_LABEL_LIST = [
    "Bangumi",
]
TIL_LABEL_LIST = [
    "TIL",
]
GRATITUDE_LABEL_LIST = [
    "Gratitude",
]
MORNING_LABEL_LIST = [
    "Morning",
]

GTD_LABEL_LIST = [
    "GTD",
]

IDEA_LABEL_LIST = [
    "Idea",
]

WEEKLY_LABEL_LIST = [
    "Weekly",
]

SQUAT_LABEL_LIST = [
    "Squat",
]

### 2023 NEW ###
TIMELINE_LABEL_LIST = [
    "Timeline",
]

GITHUB_README_COMMENTS = (
    "(<!--START_SECTION:{name}-->\n)(.*)(<!--END_SECTION:{name}-->\n)"
)

# add new label here
LABEL_DICT = {
    "TIL": {"label_list": TIL_LABEL_LIST, "comment_name": "my_til"},
    "Gratitude": {"label_list": GRATITUDE_LABEL_LIST, "comment_name": "my_gratitude"},
    "Read": {"label_list": READ_LABEL_LIST, "comment_name": "my_read"},
    "Drama": {"label_list": DRAMA_LABEL_LIST, "comment_name": "my_drama"},
    "Bangumi": {"label_list": BANGUMI_LABEL_LIST, "comment_name": "my_bangumi"},
    "ToDo": {"label_list": TODO_LABEL_LIST, "comment_name": "my_todo"},
}



##### BASE COMMENT TABLE ######
BASE_ISSUE_STAT_HEAD = "| Name | Start | Update | \n | ---- | ---- | ---- | \n"
BASE_ISSUE_STAT_TEMPLATE = "| {name} | {start} | {update} | \n"

##### BLOG COMMENT ######
BLOG_ISSUE_STAT_HEAD = (
    "| Name | Start | Update | Comments | \n | ---- | ---- | ---- | ---- |\n"
)
BLOG_ISSUE_STAT_TEMPLATE = "| {name} | {start} | {update} | {comments} | \n"


##### FOOD COMMENT TABLE ######
FOOD_ISSUE_STAT_HEAD = (
    "| Name | First_date | Last_date | Times | \n | ---- | ---- | ---- | ---- |\n"
)
FOOD_ISSUE_STAT_TEMPLATE = "| {name} | {first_date} | {last_date} | {times} |\n"


##### Month Summary ######
MONTH_SUMMARY_HEAD = "| Month | Number | \n | ---- | ---- | \n"

MONTH_SUMMARY_STAT_TEMPLATE = "| {month} | {number} |\n"

TIMEZONE = "Europe/Berlin"

##### GPT PROMPT #####
PROMPT = f"跟你对话的是一个 {YEAR - 1978} 岁的职场女性，有俩个孩子，女儿 {YEAR-2012} 岁，儿子{YEAR-2015},家庭幸福。虽然人在中年，仍有强烈的好奇心，开始尝试健康生活。\
最喜欢听播客，刷推特，读书。但有时候会感到孤独，你能作为他的朋友或助手给他回复么？因为需要记录回复，你的回复内容在 50 字以内，\
，不要带换行符号，以下为他想聊的内容： "
