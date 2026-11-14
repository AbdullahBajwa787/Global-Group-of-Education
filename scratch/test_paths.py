import os
import re

print("Testing video file paths...")
for path in ['assets/videos/crm_video.mp4', 'public/assets/videos/crm_video.mp4']:
    print(path, 'exists:', os.path.exists(path), 'size:', os.path.getsize(path) if os.path.exists(path) else 0)
