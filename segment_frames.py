from ultralytics import YOLO
import os
import glob
model = YOLO('yolov8s-seg.pt')
input_folder = './frames'
output_folder = './segmented_frames'
os.makedirs(output_folder, exist_ok=True)
image_paths = glob.glob(os.path.join(input_folder, '*.png'))
for img_path in image_paths:
    print(f"Segmenting: {os.path.basename(img_path)}")
    results = model(img_path)
    results[0].save(filename=os.path.join(output_folder, os.path.basename(img_path)))
print(f"\nAll segmentations saved to: {output_folder}")
