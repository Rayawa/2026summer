import kagglehub

# Download latest version
path = kagglehub.dataset_download("rafi003/student-lifestyle-and-academic-performance-dataset")

print("Path to dataset files:", path)