import os
from pydub import AudioSegment

def convert_wav_to_mp3(wav_filename, mp3_filename):
    """
    Convert a .wav file to .mp3 format.

    Parameters:
    - wav_filename (str): The filename of the input .wav file.
    - mp3_filename (str): The filename to save the converted .mp3 file.
    """
    # Get the current working directory (where this script is located)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the full filepaths
    wav_filepath = os.path.join(current_dir, wav_filename)
    mp3_filepath = os.path.join(current_dir, mp3_filename)
    
    # Load the .wav file
    audio = AudioSegment.from_wav(wav_filepath)
    
    # Export the audio in .mp3 format
    audio.export(mp3_filepath, format="mp3")
    
    print(f"The file was converted successfully and saved to {mp3_filepath}")

# Convert 'convert.wav' to 'convert.mp3'
convert_wav_to_mp3('convert.wav', 'convert.mp3')
