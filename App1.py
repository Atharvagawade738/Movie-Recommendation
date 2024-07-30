import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv("https://raw.githubusercontent.com/rashida048/Some-NLP-Projects/master/movie_dataset.csv")

# Define functions for different actions
def display_genre_distribution():
    plt.figure(figsize=(12, 8))
    genres = data['genres'].str.split(' ').explode().value_counts()
    sns.barplot(x=genres.values, y=genres.index, palette='viridis')
    plt.title('Distribution of Movie Genres')
    plt.xlabel('Number of Movies')
    plt.ylabel('Genre')
    plt.show()

def display_correlation_heatmap():
    plt.figure(figsize=(14, 10))
    numeric_data = data.select_dtypes(include='number')
    correlation_matrix = numeric_data.corr()
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=.5)
    plt.title('Correlation Heatmap')
    plt.show()

def display_summary_statistics():
    summary_stats = data.describe()
    print(summary_stats)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Data Science Project GUI")
        self.setGeometry(100, 100, 600, 400)

        # Create buttons
        self.button_genre_distribution = QPushButton("Genre Distribution")
        self.button_correlation_heatmap = QPushButton("Correlation Heatmap")
        self.button_summary_statistics = QPushButton("Summary Statistics")

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.button_genre_distribution)
        layout.addWidget(self.button_correlation_heatmap)
        layout.addWidget(self.button_summary_statistics)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        # Connect buttons to functions
        self.button_genre_distribution.clicked.connect(display_genre_distribution)
        self.button_correlation_heatmap.clicked.connect(display_correlation_heatmap)
        self.button_summary_statistics.clicked.connect(display_summary_statistics)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())