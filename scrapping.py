import vk_api
from tqdm import tqdm

from constants import DATA_DIR

vk_session = vk_api.VkApi('example@mail.ru', 'password')
vk_session.auth()

vk = vk_session.get_api()

GROUP_NAME = "https://vk.com/kalikfan"
OWNER_ID = "-179625476"

NUMBER_OF_SAMPLES = 1000  # max 5000 per day

for i in tqdm(range(1, NUMBER_OF_SAMPLES)):
    batch = vk.wall.get(owner_id=OWNER_ID, domain=GROUP_NAME, offset=i, count=1)['items']
    for j, text in enumerate(batch):
        with open(DATA_DIR / f"sample{i*100 + j}.txt", "w") as f:
            if text['text'] != "":
                f.write(text['text'])
