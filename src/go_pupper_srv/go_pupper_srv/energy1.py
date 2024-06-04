import librosa
import madmom
# from madmom.madmom.features.onsets import RNNOnsetProcessor
import numpy as np
import matplotlib.pyplot as plt
import librosa.display

# Simulated function to classify beat types
def classify_beat(segment):
    # Placeholder for real classification logic
    energy = np.sum(segment ** 2)
    print(energy)
    if energy > 7.5:
        return "kick"
    elif energy > 4.5:
        return "snare"
    elif energy > 2:
        return "clap"
    else:
        return "hi-hat"

# Load the audio file
audio_path = 'file_example_WAV_1MG.wav'
y, sr = librosa.load(audio_path,sr=22050)
frame_rate=100

# Use madmom's RNNOnsetProcessor to detect onsets
proc = madmom.features.onsets.RNNOnsetProcessor()
# proc = RNNOnsetProcessor()
onset_probs = proc(audio_path)


sr = 22050  # Sample rate of your audio
frame_rate = 100  # Frames per second used by RNNOnsetProcessor

# Step 2: Convert frame indices to onset times
# onset_frames = np.arange(len(onset_probs))  # Frame indices
# onset_times = onset_frames / frame_rate  # Convert frame indices to time in seconds
threshold = 0.35  # Define an appropriate threshold
onset_frames = np.where(onset_probs > threshold)[0]  # Frames with high probability
onset_times = onset_frames / frame_rate 

# Step 3: Extract and classify segments
y, sr = librosa.load(audio_path, sr=sr)
beat_types = []
window_size = int(0.05 * sr)  # 50ms window

onset_frames_librosa = librosa.time_to_frames(onset_times, sr=sr,hop_length=int(sr/frame_rate))

for onset in onset_times:
    start_sample = max(int(onset * sr) - window_size // 2, 0)
    end_sample = min(int(onset * sr) + window_size // 2, len(y))
    segment = y[start_sample:end_sample]
    
    print(start_sample,end_sample)
    # Classify the segment
    beat_type = classify_beat(segment)
    beat_types.append((onset, beat_type))

# for frame in onset_frames_librosa:
#     # Calculate the start and end time of the segment
#     start_time = librosa.frames_to_time(frame, sr=sr, hop_length=int(sr/frame_rate))
#     end_time = onset_times[frame + 1] if frame + 1 < len(onset_times) else len(y) / sr

#     # Calculate the duration of the sound following the onset
#     duration = end_time - start_time

#     # Adjust window size based on duration
#     window_size = int(duration * sr)  # Use the duration to set window size

#     # Extract the segment from the audio
#     start_sample = max(frame * int(sr / frame_rate) - window_size // 2, 0)
#     end_sample = min(frame * int(sr / frame_rate) + window_size // 2, len(y))
#     segment = y[start_sample:end_sample]

#     # Classify the segment (assuming classify_beat is defined elsewhere)
#     beat_type = classify_beat(segment)
#     print((librosa.frames_to_time(frame, sr=sr, hop_length=int(sr/frame_rate))))
#     beat_types.append((librosa.frames_to_time(frame, sr=sr, hop_length=int(sr/frame_rate)), beat_type))
    
# Print detected onsets and classified beats
# print('Detected onsets and classified beats:')
# for onset, beat_type in beat_types:
#     print(f'Time: {onset:.2f}s, Type: {beat_type}')

# Plot waveform and onsets with classified beat types
plt.figure(figsize=(14, 5))
librosa.display.waveshow(y, sr=sr, alpha=0.6)
for onset, beat_type in beat_types:
    color = {'kick': 'r', 'snare': 'g', 'clap': 'y', 'hi-hat': 'b'}.get(beat_type, 'k')
    plt.vlines(onset, -1, 1, color=color, linestyle='--', label=beat_type)
plt.xlabel('Time (s)')
plt.title('Waveform and Detected Onsets with Beat Types')
# plt.legend(['kick', 'snare', 'clap', 'hi-hat'])
legend_labels = ['Kick', 'Snare', 'Clap', 'Hi-hat']
legend_handles = [plt.Line2D([0], [0], color=color, linewidth=3, linestyle='--', label=label) for color, label in zip(['r', 'g', 'y', 'b'], legend_labels)]
plt.legend(handles=legend_handles, labels=legend_labels)
plt.show()



