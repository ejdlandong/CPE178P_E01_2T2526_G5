"""
Flet UI for Car Damage Classification
Provides a GUI for training and inference on the car damage dataset.
"""

import flet as ft
import threading
import os
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).resolve().parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Compatibility: some Flet versions don't expose ImageFit; fall back to string
try:
    IMAGE_FIT_CONTAIN = ft.ImageFit.CONTAIN
except Exception:
    IMAGE_FIT_CONTAIN = "contain"

from train import train_main
from predict import predict_main


class CarDamageClassifierApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Car Damage Classifier"
        self.page.window_width = 900
        self.page.window_height = 700
        self.page.theme_mode = ft.ThemeMode.LIGHT
        
        # State
        self.training_active = False
        self.predicting_active = False
        self.current_mode = "train"  # 'train' or 'predict'
        
        # Shared widgets for result display (right panel)
        # start with a placeholder container; we'll set a real Image when user selects one
        self.image_display = ft.Container(
            content=ft.Text("No image selected", size=12),
            width=400,
            height=400,
            bgcolor="#ffffff",
            padding=10,
        )

        self.predict_status = ft.Text(
            value="Select model and image to predict",
            color="blue",
            size=12,
        )

        self.prediction_result = ft.Text(
            value="Prediction: ",
            size=16,
            weight="bold",
            color="green",
        )
        
        # Build UI
        self.build_ui()
    
    def build_ui(self):
        """Build the main UI layout."""
        # Mode selector buttons
        self.train_mode_btn = ft.ElevatedButton(
            content=ft.Text("Train Mode"),
            on_click=self.on_train_mode_click,
        )
        self.predict_mode_btn = ft.ElevatedButton(
            content=ft.Text("Predict Mode"),
            on_click=self.on_predict_mode_click,
        )
        
        # Container for content
        self.content_container = ft.Container(
            expand=True,
            content=ft.Column(),
        )
        
        # Main layout
        main_layout = ft.Column(
            controls=[
                ft.Row([self.train_mode_btn, self.predict_mode_btn]),
                ft.Divider(),
                self.content_container,
            ],
            expand=True,
        )
        
        self.page.add(main_layout)
        self.show_train_mode()
    
    def on_train_mode_click(self, e):
        """Switch to train mode."""
        if self.current_mode != "train":
            self.current_mode = "train"
            self.show_train_mode()
    
    def on_predict_mode_click(self, e):
        """Switch to predict mode."""
        if self.current_mode != "predict":
            self.current_mode = "predict"
            self.show_predict_mode()
    
    def show_train_mode(self):
        """Display training UI."""
        left = self.build_train_tab()
        right = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Prediction Results", size=18, weight="bold"),
                    ft.Divider(),
                    self.image_display,
                    ft.Divider(),
                    self.predict_status,
                    self.prediction_result,
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=10,
            width=420,
        )

        self.content_container.content = ft.Row(
            controls=[left, right],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )
        self.page.update()
    
    def show_predict_mode(self):
        """Display prediction UI."""
        left = self.build_predict_tab()
        right = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Prediction Results", size=18, weight="bold"),
                    ft.Divider(),
                    self.image_display,
                    ft.Divider(),
                    self.predict_status,
                    self.prediction_result,
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=10,
            width=420,
        )

        self.content_container.content = ft.Row(
            controls=[left, right],
            alignment=ft.MainAxisAlignment.SPACE_AROUND,
        )
        self.page.update()
    
    def build_train_tab(self) -> ft.Container:
        """Build the training tab."""
        
        # Input fields
        self.data_dir_input = ft.TextField(
            label="Data Directory",
            value="dataset",
            width=350,
        )
        
        self.csv_path_input = ft.TextField(
            label="Labels CSV Path",
            value="dataset/labels.csv",
            width=350,
        )
        
        self.epochs_input = ft.TextField(
            label="Epochs",
            value="5",
            width=100,
            input_filter=ft.NumbersOnlyInputFilter(),
        )
        
        self.batch_size_input = ft.TextField(
            label="Batch Size",
            value="16",
            width=100,
            input_filter=ft.NumbersOnlyInputFilter(),
        )
        
        self.lr_input = ft.TextField(
            label="Learning Rate",
            value="0.001",
            width=100,
        )
        
        self.model_path_input = ft.TextField(
            label="Save Model As",
            value="model.pth",
            width=350,
        )
        
        # Status display
        self.train_status = ft.Text(
            value="Ready to train",
            color="blue",
            size=12,
        )
        
        self.train_log = ft.Container(
            content=ft.Column(
                controls=[],
                scroll=ft.ScrollMode.AUTO,
            ),
            bgcolor="#f0f0f0",
            border_radius=5,
            padding=10,
            height=250,
            width=750,
        )
        
        # Train button
        train_button = ft.ElevatedButton(
            content=ft.Text("Start Training"),
            on_click=self.on_train_click,
        )
        
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Training Configuration", size=18, weight="bold"),
                    ft.Divider(),
                    ft.Row([self.data_dir_input, self.csv_path_input]),
                    ft.Row([self.epochs_input, self.batch_size_input, self.lr_input]),
                    self.model_path_input,
                    ft.Row([train_button]),
                    self.train_status,
                    ft.Text("Training Log:", size=14, weight="bold"),
                    self.train_log,
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=20,
        )
    
    def build_predict_tab(self) -> ft.Container:
        """Build the prediction tab."""
        
        # Model file browsing will use native file dialog (_browse_model)
        
        self.model_path_display = ft.TextField(
            label="Model Path",
            value="model.pth",
            width=350,
            read_only=True,
        )
        
        browse_model_btn = ft.ElevatedButton(
            content=ft.Text("Browse Model"),
            on_click=lambda e: self._browse_model(),
        )
        
        # Image file browsing will use native file dialog (_browse_image)
        
        self.image_path_display = ft.TextField(
            label="Image Path",
            value="",
            width=350,
            read_only=True,
        )
        
        browse_image_btn = ft.ElevatedButton(
            content=ft.Text("Browse Image"),
            on_click=lambda e: self._browse_image(),
        )
        
        # Note: shared image and result widgets are created in __init__
        
        # Predict button
        predict_button = ft.ElevatedButton(
            content=ft.Text("Predict"),
            on_click=self.on_predict_click,
        )
        
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Model & Image Selection", size=18, weight="bold"),
                    ft.Divider(),
                    ft.Row([self.model_path_display, browse_model_btn]),
                    ft.Row([self.image_path_display, browse_image_btn]),
                    ft.Divider(),
                    ft.Row(
                        [
                            ft.Column([self.image_display]),
                            ft.Column([
                                self.predict_status,
                                predict_button,
                                ft.Divider(),
                                self.prediction_result,
                            ]),
                        ],
                        alignment=ft.MainAxisAlignment.START,
                    ),
                ],
                scroll=ft.ScrollMode.AUTO,
            ),
            padding=20,
        )
    
    def on_model_picked(self, e):
        """Handle model file selection."""
        if getattr(e, 'files', None):
            path = e.files[0].path
            self.model_path_display.value = path
            self.page.update()
    
    def on_image_picked(self, e):
        """Handle image file selection."""
        if getattr(e, 'files', None):
            image_path = e.files[0].path
            self.image_path_display.value = image_path
            try:
                img_widget = ft.Image(image_path, width=400, height=400, fit=IMAGE_FIT_CONTAIN)
                self.image_display.content = img_widget
            except Exception:
                self.image_display.content = ft.Text(f"Selected: {image_path}")

            self.predict_status.value = "Image loaded. Click 'Predict' to classify."
            self.predict_status.color = "blue"
            self.page.update()

    def _browse_model(self):
        """Open a native file dialog to select a model file and update the UI."""
        try:
            from tkinter import Tk, filedialog
            root = Tk()
            root.withdraw()
            path = filedialog.askopenfilename(filetypes=[('Model files', '*.pth'), ('All files', '*.*')])
            root.destroy()
        except Exception as ex:
            self.add_log(f"✗ Browse model failed: {ex}")
            return

        if path:
            self.model_path_display.value = path
            self.page.update()

    def _browse_image(self):
        """Open a native file dialog to select an image and update the preview/result panel."""
        try:
            from tkinter import Tk, filedialog
            root = Tk()
            root.withdraw()
            path = filedialog.askopenfilename(filetypes=[('Image files', '*.png;*.jpg;*.jpeg'), ('All files', '*.*')])
            root.destroy()
        except Exception as ex:
            self.add_log(f"✗ Browse image failed: {ex}")
            return

        if path:
            self.image_path_display.value = path
            try:
                img_widget = ft.Image(path, width=400, height=400, fit=IMAGE_FIT_CONTAIN)
                self.image_display.content = img_widget
            except Exception:
                # fallback: show path text
                self.image_display.content = ft.Text(f"Selected: {path}")

            self.predict_status.value = "Image loaded. Click 'Predict' to classify."
            self.predict_status.color = "blue"
            self.page.update()
    
    def on_train_click(self, e):
        """Handle train button click."""
        if self.training_active:
            self.train_status.value = "Training already in progress..."
            self.train_status.color = "orange"
            self.page.update()
            return
        
        self.training_active = True
        self.train_log.content.controls.clear()
        self.train_status.value = "Training started..."
        self.train_status.color = "blue"
        self.page.update()
        
        # Run training in background thread
        threading.Thread(target=self._train_thread, daemon=True).start()
    
    def _train_thread(self):
        """Training thread (runs in background)."""
        try:
            data_dir = self.data_dir_input.value or "dataset"
            csv_path = self.csv_path_input.value or "dataset/labels.csv"
            epochs = int(self.epochs_input.value or 5)
            batch_size = int(self.batch_size_input.value or 16)
            lr = float(self.lr_input.value or 0.001)
            model_path = self.model_path_input.value or "model.pth"
            
            self.add_log(f"Starting training with:")
            self.add_log(f"  Data dir: {data_dir}")
            self.add_log(f"  CSV: {csv_path}")
            self.add_log(f"  Epochs: {epochs}, Batch size: {batch_size}, LR: {lr}")
            self.add_log("")
            
            # Call train_main
            train_main([
                '--data-dir', data_dir,
                '--csv', csv_path,
                '--epochs', str(epochs),
                '--batch-size', str(batch_size),
                '--lr', str(lr),
                '--save-path', model_path,
            ])
            
            self.add_log("")
            self.add_log(f"✓ Training complete! Model saved to {model_path}")
            self.train_status.value = "Training complete!"
            self.train_status.color = "green"
            
        except Exception as ex:
            self.add_log(f"✗ Error: {str(ex)}")
            self.train_status.value = f"Error: {str(ex)}"
            self.train_status.color = "red"
        
        finally:
            self.training_active = False
            self.page.update()
    
    def on_predict_click(self, e):
        """Handle predict button click."""
        image_path = self.image_path_display.value
        model_path = self.model_path_display.value
        
        if not image_path:
            self.predict_status.value = "Please select an image"
            self.predict_status.color = "red"
            self.page.update()
            return
        
        if not model_path or not os.path.exists(model_path):
            self.predict_status.value = f"Model not found: {model_path}"
            self.predict_status.color = "red"
            self.page.update()
            return
        
        if self.predicting_active:
            self.predict_status.value = "Prediction in progress..."
            self.predict_status.color = "orange"
            self.page.update()
            return
        
        self.predicting_active = True
        self.predict_status.value = "Predicting..."
        self.predict_status.color = "blue"
        self.page.update()
        
        # Run prediction in background thread
        threading.Thread(
            target=self._predict_thread,
            args=(image_path, model_path),
            daemon=True,
        ).start()
    
    def _predict_thread(self, image_path: str, model_path: str):
        """Prediction thread (runs in background)."""
        try:
            import torch
            from PIL import Image
            from torchvision import transforms
            
            # Load model
            ckpt = torch.load(model_path, map_location='cpu')
            label2idx = ckpt.get('label2idx', {})
            idx2label = {v: k for k, v in label2idx.items()} if label2idx else {}
            
            from src.model import SimpleCNN
            num_classes = max(1, len(idx2label))
            model = SimpleCNN(num_classes=num_classes)
            model.load_state_dict(ckpt['model_state_dict'])
            model.eval()
            
            # Load and preprocess image
            img = Image.open(image_path).convert('RGB')
            transform = transforms.Compose([
                transforms.Resize((128, 128)),
                transforms.ToTensor(),
            ])
            t = transform(img).unsqueeze(0)
            
            # Predict
            with torch.no_grad():
                outs = model(t)
                _, pred = torch.max(outs, 1)
                lab = idx2label.get(int(pred.item()), str(int(pred.item())))
            
            self.prediction_result.value = f"Prediction: {lab}"
            self.prediction_result.color = "green"
            self.predict_status.value = "Prediction complete!"
            self.predict_status.color = "green"
            
        except Exception as ex:
            self.prediction_result.value = f"Error: {str(ex)}"
            self.prediction_result.color = "red"
            self.predict_status.value = f"Prediction failed"
            self.predict_status.color = "red"
        
        finally:
            self.predicting_active = False
            self.page.update()
    
    def add_log(self, message: str):
        """Add a log message to the training log."""
        log_text = ft.Text(value=message, size=11, font_family="monospace")
        self.train_log.content.controls.append(log_text)
        self.page.update()


def main(page: ft.Page):
    """Main entry point."""
    app = CarDamageClassifierApp(page)


if __name__ == '__main__':
    ft.app(target=main)
