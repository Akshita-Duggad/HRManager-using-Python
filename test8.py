from network_client.client import NetworkClient
from network_common.wrappers import Request,Response
client=NetworkClient()
request=Request("DesignationManager","getAll")
response=client.send(request)
