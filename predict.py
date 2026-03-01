import os
import sys
import argparse
from pathlib import Path

script_dir = Path(__file__).resolve().parent
if str(script_dir) not in sys.path:
    sys.path.insert(0, str(script_dir))

import torch
from torchvision import transforms
from PIL import Image
import pandas as pd

from src.model import SimpleCNN

def predict_main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--model', default='model.pth', help='Path to saved model (.pth)')
    parser.add_argument('--data-dir', default='dataset', help='Dataset root (contains images/ and labels.csv)')
    parser.add_argument('--csv', default='dataset/labels.csv', help='CSV with filenames to predict')
    parser.add_argument('--out', default='predictions.csv', help='Output CSV with filename,pred')
    args = parser.parse_args(argv)

    ckpt = torch.load(args.model, map_location='cpu')
    label2idx = ckpt.get('label2idx', {})
    idx2label = {v: k for k, v in label2idx.items()} if label2idx else {}

    num_classes = max(1, len(idx2label))
    model = SimpleCNN(num_classes=num_classes)
    model.load_state_dict(ckpt['model_state_dict'])
    model.eval()

    images_dir = os.path.join(args.data_dir, 'images')
    df = pd.read_csv(args.csv, header=None)
    filenames = df.iloc[:, 0].astype(str).tolist()

    transform = transforms.Compose([
        transforms.Resize((128, 128)),
        transforms.ToTensor(),
    ])

    results = []
    with torch.no_grad():
        for fname in filenames:
            path = os.path.join(images_dir, fname)
            if not os.path.exists(path):
                print(f'Warning: missing {path}, skipping')
                continue
            img = Image.open(path).convert('RGB')
            t = transform(img).unsqueeze(0)
            outs = model(t)
            _, pred = torch.max(outs, 1)
            lab = idx2label.get(int(pred.item()), str(int(pred.item())))
            results.append({'filename': fname, 'prediction': lab})

    out_df = pd.DataFrame(results)
    out_df.to_csv(args.out, index=False)
    print(f'Predictions saved to {args.out}')


if __name__ == '__main__':
    predict_main()
