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
    if energy > 60:
        return "kick"
    elif energy > 40:
        return "snare"
    elif energy > 20:
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

threshold = 0.35  # Define an appropriate threshold
onset_frames = np.where(onset_probs > threshold)[0]  # Frames with high probability
onset_times = onset_frames / frame_rate 

# Step 3: Extract and classify segments
y, sr = librosa.load(audio_path, sr=sr)
beat_types = []
window_size = int(0.5 * sr)  # 100ms window

onset_frames_librosa = librosa.time_to_frames(onset_times, sr=sr,hop_length=int(sr/frame_rate))

onset1=0
increment=0.5
sequence=[]
for onset in onset_times:
    # print(onset,"onset")
    if onset>onset1:
        start_sample = max(int(onset * sr) - window_size // 2, 0)
        end_sample = min(int(onset * sr) + window_size // 2, len(y))
        segment = y[start_sample:end_sample]
        
        print(start_sample/sr,end_sample/sr)
        # Classify the segment
        beat_type = classify_beat(segment)
        if beat_type=='kick':
            sequence.append('move_forward')
        elif beat_type=='snare':
            sequence.append('right')
        elif beat_type=='clap':
            sequence.append('left')
        elif beat_type=='hi-hat':
            sequence.append('move_backward')
        beat_types.append((onset, beat_type))
        onset1=onset+increment

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
