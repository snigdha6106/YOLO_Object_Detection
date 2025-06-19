from ultralytics import YOLO
import os
import glob
model = YOLO('yolov8s-seg.pt')
input_folder = '/Users/snigdhatalasila/Documents/IIITH_Online_Internship/images'
output_folder = '/Users/snigdhatalasila/Documents/IIITH_Online_Internship/results'
os.makedirs(output_folder, exist_ok=True)
image_paths = glob.glob(os.path.join(input_folder, '*.[pj][pn]g'))
for img_path in image_paths:
    print(f"Segmenting: {os.path.basename(img_path)}")
    results = model(img_path)
    results[0].save(filename=os.path.join(output_folder, os.path.basename(img_path)))
print(f"\nAll segmentations saved to: {output_folder}")
