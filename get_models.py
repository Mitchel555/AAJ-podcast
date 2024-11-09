from elevenlabs import ElevenLabs
from pprint import pprint

client = ElevenLabs(
    api_key="sk_99848a4e2760f019e60ad783be48531c932f919b231e2863",
)
models = client.models.get_all()

pprint(models)