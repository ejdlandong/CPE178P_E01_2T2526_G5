import os
import sys
import argparse
from pathlib import Path

# Ensure project root is on sys.path
script_dir = Path(__file__).resolve().parent
if str(script_dir) not in sys.path:
    sys.path.insert(0, str(script_dir))

import torch
from torch.utils.data import DataLoader, Subset
import torch.nn as nn
import torch.optim as optim
from sklearn.model_selection import train_test_split
from tqdm import tqdm

from src.dataset import ImageCSVLoader
from src.model import SimpleCNN


def train_main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-dir', default='dataset', help='Dataset root (contains images/ and labels.csv)')
    parser.add_argument('--csv', default='dataset/labels.csv', help='Labels CSV path')
    parser.add_argument('--epochs', type=int, default=5)
    parser.add_argument('--batch-size', type=int, default=16)
    parser.add_argument('--lr', type=float, default=1e-3)
    parser.add_argument('--save-path', default='model.pth')
    args = parser.parse_args(argv)

    # Resolve paths relative to the project root (script_dir)
    csv_path = Path(args.csv)
    if not csv_path.is_absolute():
        csv_path = script_dir / csv_path

    images_dir = Path(args.data_dir)
    if not images_dir.is_absolute():
        images_dir = script_dir / images_dir
    images_dir = images_dir / 'images' if images_dir.name != 'images' else images_dir

    # Fallback: if the provided CSV doesn't exist, try labels_small.csv
    if not csv_path.exists():
        fallback = script_dir / 'dataset' / 'labels_small.csv'
        if fallback.exists():
            print(f"Warning: CSV not found at {csv_path}. Using fallback {fallback} for smoke testing.")
            csv_path = fallback
        else:
            checked = [str(csv_path), str(script_dir / 'dataset' / 'labels.csv'), str(fallback)]
            raise FileNotFoundError(
                f"Labels CSV not found. Checked paths:\n  " + "\n  ".join(checked) +
                "\n\nCreate a CSV at one of these paths (format: filename,label) or pass --csv <path> to train.py."
            )

    # dataset
    dataset = ImageCSVLoader(str(csv_path), str(images_dir), require_labels=True)
    n = len(dataset)
    if n == 0:
        raise RuntimeError('Dataset appears empty (no rows in CSV)')

    indices = list(range(n))
    train_idx, val_idx = train_test_split(indices, test_size=0.2, random_state=42)

    train_ds = Subset(dataset, train_idx)
    val_ds = Subset(dataset, val_idx)

    train_loader = DataLoader(train_ds, batch_size=args.batch_size, shuffle=True)
    val_loader = DataLoader(val_ds, batch_size=args.batch_size, shuffle=False)

    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

    model = SimpleCNN(num_classes=dataset.get_num_classes())
    model.to(device)

    optimizer = optim.Adam(model.parameters(), lr=args.lr)
    criterion = nn.CrossEntropyLoss()

    for epoch in range(1, args.epochs + 1):
        model.train()
        running_loss = 0.0
        correct = 0
        total = 0
        for imgs, labels in tqdm(train_loader, desc=f'Train Epoch {epoch}'):
            imgs = imgs.to(device)
            labels = labels.to(device)
            optimizer.zero_grad()
            outputs = model(imgs)
            loss = criterion(outputs, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item() * imgs.size(0)
            _, preds = torch.max(outputs, 1)
            correct += (preds == labels).sum().item()
            total += labels.size(0)

        train_loss = running_loss / total
        train_acc = correct / total

        # validation
        model.eval()
        vloss = 0.0
        vcorrect = 0
        vtotal = 0
        with torch.no_grad():
            for imgs, labels in val_loader:
                imgs = imgs.to(device)
                labels = labels.to(device)
                outputs = model(imgs)
                loss = criterion(outputs, labels)
                vloss += loss.item() * imgs.size(0)
                _, preds = torch.max(outputs, 1)
                vcorrect += (preds == labels).sum().item()
                vtotal += labels.size(0)

        val_loss = vloss / vtotal
        val_acc = vcorrect / vtotal

        print(f'Epoch {epoch}: train_loss={train_loss:.4f} train_acc={train_acc:.4f} | val_loss={val_loss:.4f} val_acc={val_acc:.4f}')

    # save
    Path(args.save_path).parent.mkdir(parents=True, exist_ok=True)
    torch.save({'model_state_dict': model.state_dict(), 'label2idx': dataset.label2idx}, args.save_path)
    print(f'Model saved to {args.save_path}')


if __name__ == '__main__':
    train_main()
