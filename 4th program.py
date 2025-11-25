import numpy as np

# Simulate 10 days of walking (steps and time taken in minutes)
# Assume these are realistic values based on watch data before it stopped
np.random.seed(0)  # for reproducibility
steps = np.random.randint(4800, 5200, size=10)  # ~5000 steps per day
time_minutes = np.random.randint(35, 45, size=10)  # ~40 minutes per walk

# Display the data
for day, (s, t) in enumerate(zip(steps, time_minutes), 1):
    print(f"Day {day}: {s} steps in {t} minutes")

# Calculate average steps per minute
steps_per_minute = steps / time_minutes
avg_spm = np.mean(steps_per_minute)

print(f"\nAverage steps per minute over 10 days: {avg_spm:.2f}")

# Calculate how many minutes needed to walk 2000 steps
steps_needed = 2000
estimated_time = steps_needed / avg_spm

print(f"\nYou need to walk ~{estimated_time:.2f} minutes to complete 2000 steps.")

