import pickle
from scipy import spatial
pkl_path = "img_facenet.pkl"

with open(pkl_path, 'rb') as f:
    data = pickle.load(f)
A = data['Anthony_Hopkins_0001.jpg']
B = data['Anthony_Hopkins_0002.jpg']
print(spatial.distance.euclidean(A, B))