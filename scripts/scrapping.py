import vk_api
from tqdm import tqdm

from constants import DATA_DIR

vk_session = vk_api.VkApi("example@mail.ru", "****")
vk_session.auth()

vk = vk_session.get_api()

GROUP_NAME = "https://vk.com/jumoreski"
OWNER_ID = "-92876084"

NUMBER_OF_SAMPLES = 50  # max 5000 per day

with open(DATA_DIR / f"new_dataset.txt", "w") as f:
    for i in tqdm(range(NUMBER_OF_SAMPLES)):
        batch = vk.wall.get(
            owner_id=OWNER_ID, domain=GROUP_NAME, offset=i * 100, count=100
        )["items"]
        for j, text in enumerate(batch):
            if text["text"] != "":
                f.write(text["text"])
