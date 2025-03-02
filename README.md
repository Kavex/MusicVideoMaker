![image](https://github.com/user-attachments/assets/2d9d49be-b0c9-4253-a48e-b1c66582a03e)

# Music Video Maker

Music Video Maker is a simple Python GUI application that uses FFmpeg to convert an image and an audio file (MP3/WAV) into an MP4 video. The generated video displays the image for the duration of the audio track.

Download: https://github.com/Kavex/MusicVideoMaker/releases/

## Features

- **User-friendly GUI:** Built using Tkinter, the application provides a straightforward interface to select the required files.
- **Flexible Input:** Supports common image formats (JPG, JPEG, PNG) and audio formats (MP3, WAV).
- **FFmpeg Integration:** Uses FFmpeg to create a video that loops a still image with the audio track, encoding with H.264 and AAC.
- **Real-time Console Output:** Displays FFmpeg conversion progress in a scrollable text area.
- **Error Handling:** Informs the user if an error occurs during conversion.

## Prerequisites

- **Python 3.x:** Ensure you have Python installed.
- **FFmpeg:** The application relies on FFmpeg. Make sure it is installed and added to your system's PATH.
- **Tkinter:** Typically bundled with Python on most platforms.
