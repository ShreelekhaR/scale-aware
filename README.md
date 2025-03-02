# [Scale Aware Recognition in Satellite Images under Resource Constraints](https://www.cs.cornell.edu/~revankar/scale_aware)

Published as a conference paper at ICLR 2025

#### Authors: Shreelekha Revankar¹*, Cheng Perng Phoo¹, Utkarsh Mall², Bharath Hariharan¹, Kavita Bala¹
<sup>1</sup>Cornell University
<sup>2</sup>Columbia University
## Getting Started

### Setting up the Python Environment
```bash
# Clone the repository
git clone https://github.com/ShreelekhaR/scale-aware.git
cd scale-aware

# Create the conda environment from the provided environment.yml file
conda env create -f environment.yml

# OR create your own python environment
conda create -n scale_aware python=3.10

# Install PyTorch (adjust according to your CUDA version if applicable)
pip install torch torchvision

# Install the required packages
pip install -r requirements.txt
```


## Demo
coming soon
<!-- To run a quick demo of our scale-aware recognition system:

```bash
python demo.py --input_image path/to/your/satellite_image.tif --output_dir results/
```

This will process the input satellite image and save the recognition results in the specified output directory. -->

## Dataset & Training
To download our data and train the models, please refer to our [Training and Data Guide](./docs/DATA_TRAINING.md).


## Inference
<!-- To run inference on your own satellite imagery:

1. Prepare your satellite images in jpg format
2. Run the inference script:
   ```bash
   python inference.py --input_dir path/to/images/ --output_dir path/to/results/ --model path/to/pretrained_model.pth
   ```
3. The results will be saved in the output directory with the following files:
   - `predictions.json`: Contains the detected objects with their coordinates and confidence scores
   - `visualization/`: Directory containing visualized results overlaid on the original images -->


## Citation
If you find our work useful in your research, please consider citing:
```
@article{revankar2024scale,
    title={Scale-Aware Recognition in Satellite Images under Resource Constraint},
    author={Revankar, Shreelekha and Phoo, Cheng Perng and Mall, Utkarsh and Hariharan, Bharath and Bala, Kavita},
    journal={ICLR},
    year={2025}
}

```

