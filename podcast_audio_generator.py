# podcast_audio_generator.py
from pydantic import BaseModel, Field
import requests
import json
from typing import List

class PodcastLine(BaseModel):
    role: str = Field(..., description="The role of the speaker, either 'guest' or 'moderator'")
    text: str = Field(..., description="The line spoken by the role")

class PodcastInterview(BaseModel):
    conversation: List[PodcastLine]

# Map roles to voice IDs
voice_ids = {
    'guest': 'Xb7hH8MSUJpSbSDYk0k2',       # Replace with correct voice ID for 'guest'
    'moderator': 'pqHfZKP75CvOlQylNhV4'    # Replace with correct voice ID for 'moderator'
}

########### ElevenLabs API key
########### ElevenLabs API key
########### ElevenLabs API key

elevenlabs_api_key = 'xxx'

########### ElevenLabs API key
########### ElevenLabs API key
########### ElevenLabs API key

def load_podcast_script(filename: str = "podcast.json") -> PodcastInterview:
    """Load the podcast script from a JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return PodcastInterview.model_validate(data)
    except Exception as e:
        print(f"Error loading podcast script: {str(e)}")
        raise

def generate_audio(interview: PodcastInterview):
    """Generate audio files for each line in the podcast"""
    for idx, line in enumerate(interview.conversation):
        role = line.role.lower()
        text = line.text
        voice_id = voice_ids.get(role)
        
        if voice_id is None:
            print(f"No voice ID found for role '{role}'. Skipping line.")
            continue
        
        # Get previous_text and next_text for context
        previous_text = interview.conversation[idx - 1].text if idx > 0 else ""
        next_text = interview.conversation[idx + 1].text if idx < len(interview.conversation) - 1 else ""
        
        # Prepare the ElevenLabs API request
        url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
        
        payload = {
            "text": text,
            "model_id": "eleven_turbo_v2_5",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5,
                "style": 0.5,
                "use_speaker_boost": True
            },
            "seed": 123,
            "previous_text": previous_text,
            "next_text": next_text,
            "apply_text_normalization": "auto"
        }
        
        headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": elevenlabs_api_key
        }
        
        response = requests.post(url, json=payload, headers=headers)
        
        if response.status_code == 200:
            filename = f"line_{idx+1}_{role}.mp3"
            with open(filename, 'wb') as f:
                f.write(response.content)
            print(f"Saved audio for line {idx+1} ({role}) to {filename}")
        else:
            print(f"Error generating audio for line {idx+1} ({role}): {response.status_code}")
            print(response.text)

def main():
    try:
        # Load the podcast script
        print("Loading podcast script...")
        interview = load_podcast_script()
        
        # Print the loaded conversation
        print("\nLoaded Podcast Script:")
        print("-" * 50)
        for line in interview.conversation:
            print(f"{line.role.capitalize()}: {line.text}")
        print("-" * 50)
        
        # Generate audio files
        print("\nGenerating audio files...")
        generate_audio(interview)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()