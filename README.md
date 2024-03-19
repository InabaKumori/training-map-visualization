# Training mAP Visualization

This repository contains a Python script for generating a line chart that visualizes the training mean Average Precision (mAP) values over 30 epochs, demonstrating improvements in model performance. The visualization focuses on epochs 5 through 29, where significant changes in mAP values are observed.

## Usage

To use this script, you will need Python installed on your system along with the Matplotlib library. You can install Matplotlib using pip:

```sh
pip install matplotlib
```

After installing the necessary library, you can run the script to generate the visualization:

```sh
python training_map_visualization.py
```

This will display a line chart showing the training mAP values after improvements, with epochs on the x-axis and mAP percentage on the y-axis.

## Script

The script `training_map_visualization.py` is structured as follows:

```python
import matplotlib.pyplot as plt

# Training mAP values (after improvements) from epoch 5 to 29
epochs = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
mAP_values = [
    68.318, 68.974, 69.770, 70.632, 70.912, 71.861, 72.583, 72.790,
    72.969, 72.873, 73.696, 73.965, 74.063, 74.830, 75.139, 74.834,
    75.081, 75.654, 75.990, 76.113, 76.362, 76.794, 76.414, 76.934, 76.497
]

plt.figure(figsize=(12, 8))
plt.plot(epochs, mAP_values, marker='o', linestyle='-', color='blue', label='Training mAP (After Improvement)')
plt.title('Training mAP Over Epochs (After Improvement)')
plt.xlabel('Epoch')
plt.ylabel('mAP (%)')
plt.xticks(ticks=[-1] + list(range(0, 31, 2)), labels=[''] + [str(x) for x in range(0, 31, 2)])
plt.yticks(range(0, 101, 10))
plt.grid(True)
plt.tight_layout()
plt.show()
```

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries, you can reach out through my GitHub profile: [@inabakumori](https://github.com/inabakumori).
