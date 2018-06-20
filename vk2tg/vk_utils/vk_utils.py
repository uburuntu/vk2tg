from vk2tg.vk_utils.vk_post import VkPost


class VkUtils:
    def __init__(self, vk_api):
        self.vk = vk_api

    def post_from_url(self, url):
        post_id = url.split('wall')[-1]
        post = self.vk.wall.getById(posts=post_id, extended=True)
        return post

    @staticmethod
    def parse_post(post):
        return VkPost(post).html()
