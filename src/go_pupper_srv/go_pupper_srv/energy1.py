import librosa
import madmom
# from madmom.madmom.features.onsets import RNNOnsetProcessor
import numpy as np
import matplotlib.pyplot as plt
import librosa.display
from pupper_interfaces.srv import GoPupper

# Lets us read arguments from the command line as needed
import sys

# Packages to let us create nodes and spin them up
import rclpy
from rclpy.node import Node
import time
import RPi.GPIO as GPIO
import sounddevice as sd
import soundfile as sf
from MangDang.mini_pupper.display import Display, BehaviorState


touchPin_Front = 6
touchPin_Left  = 3
touchPin_Right = 16
touchPin_Back  = 2

# Use GPIO number but not PIN number
GPIO.setmode(GPIO.BCM)

# Set up GPIO numbers to input
GPIO.setup(touchPin_Front, GPIO.IN)
GPIO.setup(touchPin_Left,  GPIO.IN)
GPIO.setup(touchPin_Right, GPIO.IN)
GPIO.setup(touchPin_Back,  GPIO.IN)

class MinimalClientAsync(Node):

    def __init__(self):
        super().__init__('minimal_client_async')
        #super().__init__('client_go_pupper')
        self.cli = self.create_client(GoPupper, 'pup_command')


        # "The while loop in the constructor checks if a service matching the type and name of the client 
        # is available once a second." 
        while not self.cli.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('service not available, waiting again...')

        # "Finally it creates a new request object.""
        self.req = GoPupper.Request()

    ###
    # Name: send_move_request
    # Purpose: send_move_request method, send request and spin until receive response or fail
    # Arguments:  self (reference the current class), move_command (the command we plan to send to the server)
    #####
    def send_move_request(self, move_command):
        self.req = GoPupper.Request()
        self.req.command = move_command
        print("In send_move_request, command is: %s" % self.req.command)
        self.future = self.cli.call_async(self.req)  # send the command to the server
        rclpy.spin_until_future_complete(self, self.future)
        return self.future.result()


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

def main(args=None):
    rclpy.init(args=args)
    minimal_client = MinimalClientAsync()
    audio_path = '/home/ubuntu/ros2_ws/sound/example.wav'
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
                sequence.append('move_right')
            elif beat_type=='clap':
                sequence.append('move_left')
            elif beat_type=='hi-hat':
                sequence.append('move_backward')
            beat_types.append((onset, beat_type))
            onset1=onset+increment
            
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

    # For testing - we're getting a move command string from the command line
    #cmd = sys.argv[1]
    
    # debug - comment in/our as needed
    #print("In client, got this command: %s" % cmd)

    # Call send move request (which sends cmd to server)
    # minimal_client.send_move_request(cmd)
    disp = Display()
    leftEyeLoc = "/home/ubuntu/ros2_ws/img/leftRZ.png"
    rightEyeLoc = "/home/ubuntu/ros2_ws/img/rightRZ.png"
    frontEyeLoc = "/home/ubuntu/ros2_ws/img/frontRZ.png"
    backEyeLoc = "/home/ubuntu/ros2_ws/img/backwardRZ.png"
    idleEyeLoc = "/home/ubuntu/ros2_ws/img/idleRZ.png"
    leftSound = "/home/ubuntu/ros2_ws/sound/left.wav"
    rightSound = "/home/ubuntu/ros2_ws/sound/right.wav"
    frontSound = "/home/ubuntu/ros2_ws/sound/forward.wav"
    backSound = "/home/ubuntu/ros2_ws/sound/backward.wav"
        
    print("The sequence is: ")
    print(sequence)
    for movement in sequence:
    	if movement == 'move_forward':
    	    disp.show_image(frontEyeLoc)
    	    data,rate=sf.read(frontSound)
    	    sd.play(data,rate)
    	elif movement == 'move_backward':
    	    disp.show_image(backEyeLoc)
    	    data,rate=sf.read(backSound)
    	    sd.play(data,rate)
    	elif movement == 'move_left':
    	    disp.show_image(leftEyeLoc)
    	    data,rate=sf.read(leftSound)
    	    sd.play(data,rate)
    	elif movement == 'move_right':
    	    disp.show_image(rightEyeLoc)
    	    data,rate=sf.read(rightSound)
    	    sd.play(data,rate)
    	minimal_client.send_move_request(movement)
    	print(movement)
    	time.sleep(1.0)

    # This spins up a client node, checks if it's done, throws an exception of there's an issue
    # (Probably a bit redundant with other code and can be simplified. But right now it works, so ¯\_(ツ)_/¯)
    while rclpy.ok():
        rclpy.spin_once(minimal_client)
        if minimal_client.future.done():
            try:
                response = minimal_client.future.result()
            except Exception as e:
                minimal_client.get_logger().info(
                    'Service call failed %r' % (e,))
            else:
                minimal_client.get_logger().info(
                'Result of command: %s ' %
                (response))
            break

    # Destroy node and shut down
    minimal_client.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()

