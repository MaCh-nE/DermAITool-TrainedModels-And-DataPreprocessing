import matplotlib.pyplot as plt
import numpy as np

# Models data
models = ['model700(setup1_16_70)', 'model850(setup1_16_70)', 'model850(setup2_16_70)', 'model850(setup2_16_85)', 'model850(setup2_32_85)', 'model850(setup3_16_70)']
epochs = [60, 70, 70, 85, 85, 70]
epochs = [x/100 for x in epochs]
batch_sizes = [16, 16, 16, 16, 32, 16]
batch_sizes = [x/100 for x in batch_sizes]
normalized_class_numbers = [700, 850, 850, 850, 850, 850]
normalized_class_numbers = [x/1000 for x in normalized_class_numbers]
accuracies = [0.686, 0.781, 0.85085359655438, 0.83512, 0.8555107712745667, 0.7977150678634644]

# Bar width
barWidth = 0.2

# Bar positions
r1 = np.arange(len(models))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]

# Plotting the bars
plt.figure(figsize=(14, 8))
plt.bar(r1, epochs, color='skyblue', width=barWidth, edgecolor='grey', label='Epochs/100')
plt.bar(r2, batch_sizes, color='lightgreen', width=barWidth, edgecolor='grey', label='Batch Size/1000')
plt.bar(r3, normalized_class_numbers, color='salmon', width=barWidth, edgecolor='grey', label='Class Size/100')
plt.bar(r4, accuracies, color='orange', width=barWidth, edgecolor='grey', label='Accuracy')

# Labels
plt.xticks([r + barWidth * 1.5 for r in range(len(models))], models, rotation=10)
plt.ylabel('Value', fontweight='bold')
plt.title('Model Performance Comparison', fontweight='bold')
plt.legend()

plt.tight_layout()
plt.show()


