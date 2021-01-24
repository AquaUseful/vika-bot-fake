import json
import os
try:
    from app import config
except ImportError:
    pass


class User:
    def __init__(self, user_dict):
        self.id = user_dict["id"]
        self.first_name = user_dict["first_name"]
        self.last_name = user_dict["last_name"]
        self.username = user_dict["username"]
        self.bot = user_dict["bot"]


async def get_data_dir_path():
    try:
        data_dir_path = config.DATA_DIR_PATH
    except NameError:
        data_dir_path = os.environ["DATA_DIR_PATH"]
    return data_dir_path


async def get_chats_from_file():
    data_dir_path = await get_data_dir_path()
    chats_json_path = os.path.join(data_dir_path, "chats.json")
    with open(chats_json_path, "r") as f:
        chats_data = json.load(f)
    return chats_data


async def get_users_from_file():
    data_dir_path = await get_data_dir_path()
    users_json_path = os.path.join(data_dir_path, "users.json")
    with open(users_json_path, "r") as f:
        users_data = json.load(f)
    return users_data


async def get_users_info(*user_ids):
    users = await get_users_from_file()
    selected_users = filter(lambda user: user["id"] in user_ids, users)
    users_obj = tuple(User(user_dict) for user_dict in selected_users)
    return users_obj


async def get_chat_by_token(token):
    chats_data = await get_chats_from_file()
    for chat in chats_data:
        if chat["token"] == token:
            return chat


async def get_chat_id_by_token(token):
    chat = await get_chat_by_token(token)
    return chat["id"]


async def verify_token(token):
    chat = await get_chat_by_token(token)
    return (chat is not None)


async def get_last_photo(id):
    data_dir_path = await get_data_dir_path()
    pic_path = os.path.join(data_dir_path, "pics", str(id) + ".png")
    with open(pic_path, "rb") as pic:
        return pic.read()


async def get_chat_info(chat_id):
    chats_data = await get_chats_from_file()
    for chat in chats_data:
        if chat["id"] == chat_id:
            return chat


async def get_chat_members(chat_id):
    chat = await get_chat_info(chat_id)
    users = await get_users_info(*chat["members_ids"])
    return users
