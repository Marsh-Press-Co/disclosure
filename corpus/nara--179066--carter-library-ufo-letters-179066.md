---
id: "nara--179066--carter-library-ufo-letters-179066"
title: "Carter Library UFO letters - 179066"
source: NARA-RG615
source_url: "https://www.archives.gov/research/topics/uaps"
agency: "White House (Carter)"
record_type: "archival-record"
incident_date: ""
incident_location: ""
pages: 1
naid: ""
provenance: "NARA RG 615; scanned pages vision-transcribed with gemini-3-flash-preview - not verbatim OCR, verify quotes against source"
---

# Carter Library UFO letters - 179066

## Page 1

```

In []:
```python
import PIL.Image
import PIL.ImageDraw

# Load the image to get its dimensions
img = PIL.Image.open('input_file_0.png')
width, height = img.size

# Define the bounding box for the contact sheet and the text areas
# The contact sheet is the main part of the image
# The text is at the bottom
# I'll define the contact sheet as one large image area and then the text elements

# Bounding boxes in [ymin, xmin, ymax, xmax] format, normalized to 1000
# Contact sheet area: roughly from top to where the label starts
# Label area: the white strip with text
# Date: bottom left
# Number: bottom right of label
# Stamp: bottom right

objs = [
    {'box_2d': [0, 0, 810, 1000], 'label': 'contact sheet'},
    {'box_2d': [825, 215, 925, 670], 'label': 'typed label'},
    {'box_2d': [900, 90, 940, 210], 'label': 'handwritten date'},
    {'box_2d': [895, 680, 930, 750], 'label': 'typed number'},
    {'box_2d': [875, 765, 930, 905], 'label': 'stamp'}
]

# No need to actually draw, just preparing for the final output format.
```

*Image: A contact sheet of Kodak Safety Film 5063 containing 18 black and white photographic frames. The frames show several men in suits in an office setting, gathered around a table with a large sack and a pile of letters.*

Frank Moore receives 9000 letters
concerning UFO incidents in con-
junction with Nat. Enquirer artecl

*Handwritten: 4 - 26 - 78*

5 3 7 6

*Stamp: "SHADDIX"*
