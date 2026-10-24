"""
presentation_slides_data.py - Master Slide Combiner
Combines all modular slide sets (Acts 0 through 6) into a single SLIDES_DATA list.
"""

from slides_act0_act1 import ACT0_ACT1_SLIDES
from slides_act2_act3 import ACT2_ACT3_SLIDES
from slides_act4_act5 import ACT4_ACT5_SLIDES
from slides_act6 import ACT6_SLIDES

SLIDES_DATA = ACT0_ACT1_SLIDES + ACT2_ACT3_SLIDES + ACT4_ACT5_SLIDES + ACT6_SLIDES

if __name__ == "__main__":
    print(f"Total Slides Loaded: {len(SLIDES_DATA)}")
    for idx, slide in enumerate(SLIDES_DATA, 1):
        print(f"Slide {idx:02d}: [{slide.get('badge', 'INFO')}] {slide.get('title', 'Untitled')}")
