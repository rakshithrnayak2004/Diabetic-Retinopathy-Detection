import matplotlib.pyplot as plt

# Data for accuracy
labels = ['Training Accuracy', 'Validation Accuracy']
values = [96, 90]

# Create bar chart
plt.figure(figsize=(6, 4))
plt.bar(labels, values, color=['blue', 'green'])
plt.ylim(80, 100)  # Set y-axis limits for better visualization
plt.ylabel('Accuracy (%)')
plt.title('Training vs Validation Accuracy')

# Save the graph inside static/images
output_path = "static/images/accuracy.png"
plt.savefig(output_path)
plt.show()

print(f"Accuracy graph saved at: {output_path}")
