# Diabetes_prediction

The Diabetes Prediction project is a machine learning web application developed using Flask and Jupyter Notebook. It predicts the likelihood of diabetes based on user inputs or dataset values. The application uses the provided CSV/XLSX data files for training machine learning models and offers a simple web interface to interact with the model. The interface also includes styling for better usability. The output folder stores generated result like prediction reports.

### Features

Upload medical data to predict diabetes probability. Visualizes predictions and model performances. User-friendly interface with a custom background image and basic CSS styling. Saves outputs like prediction results into a designated folder.

### Code Structure

- **app.py**: Main Flask application file handling the backend logic.
- **templates/**: Folder containing HTML templates for the frontend.
- **static/style.css**: CSS file for styling the web application.
- **Data.csv / DATA.xlsx**: Dataset files containing medical records for model training/testing.
- **Diabetes Prediction.ipynb**: Jupyter Notebook file with data analysis, model training, and evaluation.
- **background.jpg**: Background image used in the frontend design.
- **output/**: Directory for storing output files.
- 
### Installation

**Clone the repository:**

```bash
git clone https://github.com/yourusername/diabetes-prediction
```

**Install the required packages:**

```bash
pip install Flask pandas scikit-learn matplotlib
```

**Run the application:**

```bash
python app.py
```

### Usage

**Open a web browser and go to:**

[http://localhost:5000](http://localhost:5000)

Upload data or enter user inputs to predict the likelihood of diabetes. View prediction results and model performance graphs directly in the web interface.
