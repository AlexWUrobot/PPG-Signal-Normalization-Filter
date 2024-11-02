import numpy as np
import matplotlib.pyplot as plt

# Constants
sampling_rate = 10  # Hz
duration = 10 * 60  # 10 minutes in seconds
time = np.arange(0, duration, 1/sampling_rate)  # Time vector

# Simulate synthetic PPG data (for example, a sine wave with noise)
frequency = 1.0  # 1 Hz (1 beat per second)
ppg_signal = 0.5 * np.sin(2 * np.pi * frequency * time) + 0.05 * np.random.normal(size=time.shape)

# Normalize function
def normalize_ppg(signal, segment_length):
    normalized_signal = np.copy(signal)
    num_segments = len(signal) // segment_length
    
    for i in range(num_segments):
        start_index = i * segment_length
        end_index = start_index + segment_length
        segment = signal[start_index:end_index]
        
        # Normalize to range [0, 1]
        min_val = np.min(segment)
        max_val = np.max(segment)
        
        if max_val - min_val != 0:  # Avoid division by zero
            normalized_signal[start_index:end_index] = (segment - min_val) / (max_val - min_val)
    
    return normalized_signal

# Normalize every 2 seconds (20 samples)
segment_length = 2 * sampling_rate  # 2 seconds in samples
normalized_ppg = normalize_ppg(ppg_signal, segment_length)

# Plotting the results
plt.figure(figsize=(12, 6))
plt.plot(time, ppg_signal, label='Original PPG Signal', alpha=0.7)
plt.plot(time, normalized_ppg, label='Normalized PPG Signal', alpha=0.7)
plt.title('PPG Signal Normalization')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()
