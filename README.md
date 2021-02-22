# temp_match_cv
Template Matching  - A method for searching and finding the location of a template image in a larger image.

## Goal
To find objects in an image using Template Matching.

## Concept behind working
We require two components for template matching.

a. Source image (s): The image in which we expect to find a match to the template image.

b. Template image (t): The patch image which will be compared to the template image.

We slide the template my moving it one pixel at a time from left to right, up and down. For each location of t over s, you store the metric in result matrix.

The image as a result of sliding the template over the source image will result into a bright point. The brightest point is the point detected by the
