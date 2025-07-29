import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import logging
import datetime
import io
import os

# ========== Setup Logging ==========
log_filename = f"mnist_training_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

logging.info("🟢 MNIST Training Script Started")

# ========== Load and Preprocess Data ==========
logging.info("📥 Loading MNIST dataset")
(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255.0
x_test = x_test / 255.0

x_train = x_train.reshape(-1, 28*28)
x_test = x_test.reshape(-1, 28*28)

y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)

# ========== Build the Neural Network ==========
logging.info("🧠 Building the neural network")
model = models.Sequential([
    layers.Dense(128, activation='relu', input_shape=(784,)),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Log model summary
model_summary = io.StringIO()
model.summary(print_fn=lambda x: model_summary.write(x + '\n'))
logging.info("📄 Model Summary:\n" + model_summary.getvalue())
model_summary.close()

# ========== Train the Model ==========
logging.info("🏋️ Starting training...")
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_split=0.1)
logging.info("✅ Training complete")

# ========== Evaluate the Model ==========
logging.info("📊 Evaluating model on test set")
test_loss, test_accuracy = model.evaluate(x_test, y_test)
print(f"🎯 Test accuracy: {test_accuracy:.4f}")
logging.info(f"🎯 Test accuracy: {test_accuracy:.4f}")

# ========== Inference on Few Samples ==========
logging.info("🔎 Running predictions on 5 test images")
predictions = model.predict(x_test[:5])
for i in range(5):
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"Predicted: {np.argmax(predictions[i])}, Actual: {np.argmax(y_test[i])}")
    plt.show()

# ========== Save Model ==========
keras_model_path = "my_model.keras"
model.save(keras_model_path)
model_size_kb = os.path.getsize(keras_model_path) / 1024
print(f"💾 Keras model size: {model_size_kb:.2f} KB")
logging.info(f"💾 Keras model saved as '{keras_model_path}' ({model_size_kb:.2f} KB)")

# ========== Memory Footprint ==========
total_params = np.sum([np.prod(v.shape) for v in model.trainable_weights])
float_size = 4  # Each float32 takes 4 bytes
model_memory_kb = (total_params * float_size) / 1024
print(f"🧠 Estimated memory usage for weights: {model_memory_kb:.2f} KB")
logging.info(f"🧠 Estimated memory usage for weights: {model_memory_kb:.2f} KB")

# ========== Convert to Quantized TFLite ==========
logging.info("⚙️ Converting to quantized TFLite model...")
converter = tf.lite.TFLiteConverter.from_keras_model(model)
converter.optimizations = [tf.lite.Optimize.DEFAULT]
quantized_model = converter.convert()

# Save quantized model
tflite_path = "model_quantized.tflite"
with open(tflite_path, "wb") as f:
    f.write(quantized_model)

quantized_model_size_kb = len(quantized_model) / 1024
print(f"📦 Quantized TFLite model size: {quantized_model_size_kb:.2f} KB")
logging.info(f"📦 Quantized TFLite model saved as '{tflite_path}' ({quantized_model_size_kb:.2f} KB)")

logging.info("✅ Script completed successfully.")
