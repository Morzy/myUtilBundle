# Video Thumbnail Comparator

This script compares the thumbnails of videos to determine their similarity. It uses `ffmpeg` to extract thumbnails and the Python Imaging Library (PIL) to calculate image similarity.

## Features

- Extracts thumbnails from videos using `ffmpeg`.
- Compares two images for similarity using Root Mean Square (RMS) difference.
- Supports batch comparison of videos in two directories.
- Outputs whether videos have similar thumbnails based on a configurable threshold.

## Requirements

- Python 3.x
- `ffmpeg` installed and available in the system's PATH.
- Python libraries:
  - `Pillow`

Install the required Python libraries using:
```bash
pip install Pillow
```

## Usage

### Compare Two Videos

To compare the thumbnails of two videos:
1. Modify the `video1` and `video2` paths in the `are_thumbnails_similar` function.
2. Run the script.

### Compare Videos in Two Directories

To compare videos in two directories:
1. Set the paths for `video_directory1` and `video_directory2` in the `__main__` section.
2. Run the script:
   ```bash
   python video_thumbnail_comparator.py
   ```

The script will print whether similar thumbnails are found.

## Configuration

- **Thumbnail Timestamp**: Change the `timestamp` parameter in the `extract_thumbnail` function to extract thumbnails at a different time.
- **Similarity Threshold**: Adjust the `threshold` parameter in the `are_thumbnails_similar` or `are_thumbnails_similar_in_directory` functions. Default is `0.9`.

## Example

```bash
python video_thumbnail_comparator.py
```

Output:
```
Similar thumbnails found: video1.mp4 and video2.mp4
The videos have similar thumbnails.
```

## License

This script is provided as-is without any warranty. Use it at your own risk.