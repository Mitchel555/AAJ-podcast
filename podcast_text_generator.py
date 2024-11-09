# podcast_generator.py
from pydantic import BaseModel, Field
from openai import OpenAI
import json
from typing import List

class PodcastLine(BaseModel):
    role: str = Field(..., description="The role of the speaker, either 'guest' or 'moderator'")
    text: str = Field(..., description="The line spoken by the role")

class PodcastInterview(BaseModel):
    conversation: List[PodcastLine]

def generate_podcast_script() -> PodcastInterview:
    """Generate podcast script using OpenAI's structured output"""

    ########### OpenAI API key
    ########### OpenAI API key
    ########### OpenAI API key

    openai_api_key = 'xxx'

    ########### OpenAI API key
    ########### OpenAI API key
    ########### OpenAI API key

    # Initialize OpenAI client
    client = OpenAI(api_key=openai_api_key)  # Replace with your OpenAI API key
    
    try:
        completion = client.beta.chat.completions.parse(
            model="gpt-4o",
            messages=[
                {
                    "role": "system",
                    "content": "You are a podcast script generator."
                },
                {
                    "role": "user",
                    "content": """Please generate some nice smart and funny podcast between man (moderator) and woman over data in this artice which was released on allaboutjazz.com. Keep single roles text shorter. Article: Quincy Jones, a giant of popular music culture in the 20th and 21st centuries, died in Los Angeles on Sunday, November 3, He was 91.

Though he began his career in the '50s as a jazz trumpeter, Quincy Jones may be best remembered as a highly successful producer, arranger and conductor—hats he wore with increasing frequency from the '60s onwards. As a producer, Jones was at the helm of Michael Jackson's Thriller (Epic, 1982), which would sell 70 million units in Jones' lifetime. As an arranger, Jones worked his magic for Billy Eckstine, Peggy Lee, Ella Fitzgerald, Frank Sinatra and Sarah Vaughan, among others.

In 1953, aged just 20, Chicago-born Jones toured Europe with Lionel Hampton's orchestra. He then served as trumpeter and musical director for Dizzy Gillespie with whom he recorded five albums, including Dizzy Gillespie's Big Band Jazz (American recording Society, 1957). His love of big band jazz would remain undiminished. "No synthesizer, no matter how advanced, can make you feel as good as a big jazz band," Jones told Nat Hentoff in Listen To The Stories (HarperCollins,1995).

There were sideman gigs with Clifford Brown, Gigi Gryce, Art Farmer and Thad Jones before the '50s were out. In 1957 Jones released his first full-length album as leader, This Is How I Feel About Jazz (ABC-Paramount), arranging and conducting all-star large ensembles ranging from nine to fifteen players.


Over the next half century or so, Jones would shift easily between the worlds of jazz and pop music. He understood the source of all music—the links between all music. As Artistic Director of Montreux Jazz Festival in the early '90s Jones produced a number of memorable projects, including From Bebop to Hip-Hop in '91. Speaking to a private audience at the MJF in 2016 Jones said: "We were doing rap in Chicago in 1939, when I was five years old. Basically, it came from the Imbongi in South Africa thousands of years ago. You've got to know your roots," explained Jones.

An activist, Jones was one of the co-founders of the Institute for Black American Music, also co-founding the Black Arts Festival in Chicago. The Quincy Jones Workshop, which began life in the '70s, led educational projects for inner-city youth, though Jones' philanthropy extended beyond America's shores.

Education was important to Jones. Speaking with Arnaud Robert, author of 50 Summers of Music: Montreux Jazz Festival (Montreux Jazz Festival/Editions Textuel, 2016) at MJF 2016, Jones bemoaned the lack of a Minister of Culture in America. "We're trying to get a definitive curriculum in the schools because there's a very complex background to all the music and it would be nice if the kids knew what it was about, because it has as much to do with sociology as it does with culture. Whether it's gospel, blues or jazz, it all came from sociological circumstances."

Through MJF's educational programs Jones helped to launch or boost the careers of many young, aspiring musicians, mentoring among others Joey Alexander and Andreas Varady. For Jones, it was always about giving back: "When I was young Benny Carter, Clark Terry, Ray Charles and (Count) Basie—they put me on their shoulders and it's just such an honor and a privilege to put these kids on our shoulders."

It is for his music that Jones will be best remembered by millions around the world. In a long and garlanded career Jones composed and arranged for Cannonball Adderley, the Count Basie Orchestra, Herb Alpert, Louis Armstrong, Patti Austin, Tony Bennett, Ray Charles, Betty Carter, George Benson, Aretha Franklin, Milt Jackson, Little Richard, Donna Summer ... and many more.

He wrote film scores for several dozen films, among which In The Heat of the Night and In Cold Blood (both 1967), The Italian Job (1969) and The Color Purple (1985).

In 2010 Jones released Q Soul Bossa Nostra (Qwest), the final album in his name. His role was as an arranger on songs associated with him over more than half a century. The roll call of artists who lined up to pay tribute to Jones—Talib Kweli, Akon, John Legend, Snoop Dogg, LL Cool J, Mary J. Blige, Q-Tip, Wyclef Jean and Amy Winehouse—spoke volumes for his influence on popular music. Stevie Wonder arranged one track. Kamasi Washington played saxophone on another.

Recalling a State Department tour with Dizzy Gillespie to Cyprus and the former Yugoslavia in '56, Jones hailed the power of music to bring people together. For Jones, however, music was more than social glue. Much more. "Music is powerful stuff," he said. "It's like water; could you go a week without music?"""
                }
            ],
            response_format=PodcastInterview
        )
        
        return completion.choices[0].message.parsed
        
    except Exception as e:
        print(f"Error generating podcast script: {str(e)}")
        raise

def save_podcast_script(interview: PodcastInterview, filename: str = "podcast.json"):
    """Save the podcast script to a JSON file"""
    try:
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(interview.model_dump(), f, indent=2, ensure_ascii=False)
        print(f"Podcast script saved to {filename}")
    except Exception as e:
        print(f"Error saving podcast script: {str(e)}")
        raise

def main():
    try:
        # Generate podcast script
        interview = generate_podcast_script()
        
        # Print the generated conversation
        print("\nGenerated Podcast Script:")
        print("-" * 50)
        for line in interview.conversation:
            print(f"{line.role.capitalize()}: {line.text}")
        print("-" * 50)
        
        # Save to JSON file
        save_podcast_script(interview)
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()