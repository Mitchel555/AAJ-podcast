from elevenlabs import ElevenLabs
from pprint import pprint

client = ElevenLabs(
    api_key="xxx",
)
models = client.models.get_all()

pprint(models)