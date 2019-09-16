# python3
import sys


def find_pattern(pattern, text):
  """
  Find all the occurrences of the pattern in the text
  and return a list of all positions in the text
  where the pattern starts in the text.
  """
  result = []
  p = pattern + '$' + text
  s = computePrefix(p)

  for i in range(len(pattern)+1, len(p)):
    if(s[i] == len(pattern)):
      result.append(i-2*len(pattern))
  # Implement this function yourself
  return result

def computePrefix(p):
  s = [0]*len(p)
  border = 0

  for i in range(1, len(p)):
    while(border > 0 and p[i] != p[border]):
      border = s[border-1]
    if p[i] == p[border]:
      border += 1
    else:
      border = 0
    s[i] = border
  return s

if __name__ == '__main__':
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

