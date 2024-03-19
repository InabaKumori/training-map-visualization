import matplotlib.pyplot as plt

# Training mAP values (after improvements) from epoch 5 to 29
epochs = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
mAP_values = [
    68.318, 68.974, 69.770, 70.632, 70.912, 71.861, 72.583, 72.790,
    72.969, 72.873, 73.696, 73.965, 74.063, 74.830, 75.139, 74.834,
    75.081, 75.654, 75.990, 76.113, 76.362, 76.794, 76.414, 76.934, 76.497
]

# Setting up the plot
plt.figure(figsize=(12, 8))
plt.plot(epochs, mAP_values, marker='o', linestyle='-', color='blue', label='Training mAP (After Improvement)')

# Title and labels
plt.title('Training mAP Over Epochs (After Improvement)')
plt.xlabel('Epoch')
plt.ylabel('mAP (%)')

# Setting the range and labels for the x-axis and y-axis
# Adjusted x-axis ticks and labels
plt.xticks(ticks=[-1] + list(range(0, 31, 2)), labels=[''] + [str(x) for x in range(0, 31, 2)])

plt.yticks(range(0, 101, 10))

# Adding grid for better readability
plt.grid(True)

# Adjusting layout for better visibility of labels
plt.tight_layout()

# Show the plot
plt.show()

