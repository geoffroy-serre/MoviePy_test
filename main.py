from moviepy.editor import *
from moviepy.config import change_settings
from spaceentity import SpaceEntity

change_settings({"IMAGEMAGICK_BINARY": r"imagemagick\\convert.exe"})

space_entities = [
    SpaceEntity("Terre", 6371, 15),
    SpaceEntity("Venus", 6051, 462),
    SpaceEntity("Mars", 3300, 63),
    SpaceEntity("Galaxy", 50000000, 0)
]

videos_name = ['galaxy', 'mars', 'terre', 'venus']
clips = []
for entity in space_entities:
    video_file_clips = VideoFileClip(f"assets/{entity.name}.mp4").subclip(0, 5)
    name = TextClip(entity.name, fontsize=80, color='white').set_position((0.1, 0.5), relative=True
                                                                          ).set_duration(
        5),

    composite = CompositeVideoClip([video_file_clips, name])

    clips.append(composite)

# assembler les vidéos
final_clip = concatenate_videoclips(clips)

# rendu
final_clip.write_videofile("final_render.mp4", codec='libx264')
