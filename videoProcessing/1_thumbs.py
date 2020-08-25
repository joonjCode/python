from conf import SAMPLE_INPUTS, SAMPLE_OUTPUTS
from moviepy.editor import *
from PIL import Image

source_path = os.path.join(SAMPLE_INPUTS, 'sample.mp4')
thumbnail_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails')
thumbnail_per_dir = os.path.join(SAMPLE_OUTPUTS, 'thumbnails-per-frame')
os.makedirs(thumbnail_dir, exist_ok= True)
os.makedirs(thumbnail_per_dir, exist_ok= True)

clip = VideoFileClip(source_path)
# print(clip.reader.fps)
# print(clip.reader.nframes)


duration = clip.duration
max_duration = int(duration)+1
for i in range(0, max_duration):
    # print(frame)
    new_img_filepath = os.path.join(thumbnail_dir, f'{i}.jpg')
    print(f'frame at {i} seconds')
    frame = clip.get_frame(i)
    new_img = Image.fromarray(frame)
    new_img.save(new_img_filepath)

fps = clip.reader.fps
nframes = clip.reader.nframes
seconds = nframes / (fps* 1.0)

# per Frame 
for i, frame in enumerate(clip.iter_frames()):
    if i% fps ==0:
        current_ms = int((i/fps)*1000)
        new_img_filepath = os.path.join(thumbnail_per_dir, f'{i}.jpg')
        # print(f'frame at {i} seconds')
        new_img = Image.fromarray(frame)
        new_img.save(new_img_filepath)

