import pyaudio
import wave

# Parameters for the recording
FORMAT = pyaudio.paInt16  # Format for audio samples
CHANNELS = 1  # Number of audio channels (1 for mono, 2 for stereo)
RATE = 44100  # Sampling rate (samples per second)
CHUNK = 1024  # Number of frames per buffer
RECORD_SECONDS = 5  # Duration of recording in seconds
OUTPUT_FILENAME = "output12.wav"  # Name of the output file

def record_audio():
    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open a stream for audio input
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Recording...")

    frames = []

    # Loop to read audio data from the stream
    for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate the PyAudio object
    audio.terminate()

    # Save the recorded data as a WAV file
    wf = wave.open(OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(audio.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

    print(f"Audio saved to {OUTPUT_FILENAME}")

def play_audio():
    # Open the WAV file
    wf = wave.open('/home/ubuntu/ros2_ws/'+OUTPUT_FILENAME, 'rb')

    # Initialize PyAudio
    audio = pyaudio.PyAudio()

    # Open a stream for audio output
    stream = audio.open(format=audio.get_format_from_width(wf.getsampwidth()),
                        channels=wf.getnchannels(),
                        rate=wf.getframerate(),
                        output=True)

    # Read and play the audio file in chunks
    print("Playing audio...")
    data = wf.readframes(CHUNK)
    while data:
        stream.write(data)
        data = wf.readframes(CHUNK)

    # Stop and close the stream
    stream.stop_stream()
    stream.close()

    # Terminate the PyAudio object
    audio.terminate()

    wf.close()
    print("Playback finished.")

def main():
    record_audio()
    play_audio()

if __name__ == "__main__":
    main()
