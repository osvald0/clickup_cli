from typing import TypedDict, List, Optional, Dict, Union


class ClickupConfig(TypedDict):
    CLICKUP_API_TOKE: str
    CLICKUP_TEAM_ID: str
    CLICKUP_USER_ID: str


class TaskStatus(TypedDict):
    status: str
    id: str
    color: str
    type: str
    orderindex: int


class User(TypedDict):
    id: int
    username: str
    color: str
    initials: str
    email: str
    profilePicture: Optional[str]


class Tag(TypedDict):
    name: str
    tag_fg: str
    tag_bg: str
    creator: int


class CustomFieldOption(TypedDict):
    id: str
    name: str
    color: Optional[str]
    orderindex: int


class CustomFieldTypeConfig(TypedDict):
    default: int
    placeholder: Optional[str]
    options: List[CustomFieldOption]


class CustomField(TypedDict):
    id: str
    name: str
    type: str
    type_config: Dict[
        str, Union[CustomFieldTypeConfig, Dict[str, Union[bool, int, str]]]
    ]
    date_created: str
    hide_from_guests: bool
    required: bool


class Task(TypedDict):
    id: str
    custom_id: Optional[str]
    custom_item_id: int
    name: str
    text_content: str
    description: str
    status: TaskStatus
    orderindex: str
    date_created: str
    date_updated: str
    date_closed: Optional[str]
    date_done: Optional[str]
    archived: bool
    creator: User
    assignees: List[User]
    group_assignees: List[User]
    watchers: List[User]
    checklists: List[Dict]
    tags: List[Tag]
    parent: Optional[str]
    top_level_parent: Optional[str]
    priority: Optional[str]
    due_date: Optional[str]
    start_date: Optional[str]
    points: Optional[str]
    time_estimate: Optional[int]
    time_spent: Optional[int]
    custom_fields: List[CustomField]
    dependencies: List[Dict]
    linked_tasks: List[Dict]
    locations: List[Dict]
    team_id: str
    url: str
    permission_level: str
    list: Dict[str, Union[str, bool]]
    project: Dict[str, Union[str, bool]]
    folder: Dict[str, Union[str, bool]]
    space: Dict[str, str]
