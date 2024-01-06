import random

NUM_MATRICES = 10
NUM_STRATEGIES = 16

def generate_matrix():
  # matrix generation code
  matrix = [[0] * NUM_STRATEGIES for _ in range(NUM_STRATEGIES)]

  for row in range(NUM_STRATEGIES):

    # Exclude self mutation
    targets = list(range(NUM_STRATEGIES))
    targets.remove(row)

    selected = random.sample(targets, k=4)

    for col in selected:
      matrix[row][col] = 0.25

  return matrix

def format_matrix(matrix):
  # formatting code
  formatted = ""
  for row in matrix:
    formatted += " ".join(f"{x:.4f}" for x in row) + "\n"
  return formatted

with open('all_matrices.txt', 'w') as f:

  for i in range(NUM_MATRICES):

    m = generate_matrix()
    formatted = format_matrix(m)

    f.write(formatted)

    if i < NUM_MATRICES-1:
      f.write("\n")
