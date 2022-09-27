#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

vector<int> longestSequence(vector<vector<int>> const &matriz, int i, int j) {
  vector<int> L;
  int n = matriz.size();

  if ((matriz[i][j] - matriz[i - 1][j] == 1) && (i > 0)) {
    L = longestSequence(matriz, i - 1, j);
  }
  if ((matriz[i][j] - matriz[i][j + 1] == 1) && (j + 1 < n)) {
    L = longestSequence(matriz, i, j + 1);
  }
  if ((matriz[i][j] - matriz[i + 1][j] == 1) && (i + 1 < n)) {
    L = longestSequence(matriz, i + 1, j);
  }
  if ((matriz[i][j] - matriz[i][j - 1] == 1) && (j > 0)) {
    L = longestSequence(matriz, i, j - 1);
  }
  L.push_back(matriz[i][j]);
  return L;
}

vector<int> longestSequence(vector<vector<int>> const &matriz) {
  vector<int> seq;
  for (int i = 0; i < matriz.size(); i++) {
    for (int j = 0; j < matriz.size(); j++) {
      vector<int> sequence = longestSequence(matriz, i, j);
      if (sequence.size() > seq.size()) {
        seq = sequence;
      }
    }
  }
  return seq;
}

void printSequence(vector<int> const &seq) {
  cout << "[";
  int n = seq.size();
  for (int i = 0; i < n; i++) {
    cout << seq[i];
    if (i < n - 1) {
      cout << ", ";
    }
  }
  cout << "]";
}

int main() {
  vector<vector<int>> matriz = {
      {10, 16, 15, 12}, {9, 8, 7, 13}, {2, 5, 6, 14}, {3, 4, 1, 11}};
  vector<int> L = longestSequence(matriz);
  printSequence(L);

  return 0;
}