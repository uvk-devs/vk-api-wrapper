from vklib import VK

client=VK("client_id", "client_secret")
client.auth("EMAIL OR PHONE NUMBER", "PASSWORD")
client.api.wall.post(owner_id=client.id, message="Hello, world!")
