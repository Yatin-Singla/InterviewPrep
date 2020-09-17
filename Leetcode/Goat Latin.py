class Solution:
  def latin(self, word, index, vowel):
    if word[0] not in vowel:
      word = word[1:] + word[0:1]
    return word + 'ma' + 'a' * (index + 1)
  def toGoatLatin(self, S: str) -> str:
    res = []
    vowel = set('aeiouAEIOU')
    for i, word in enumerate(S.split()):
      res.append(self.latin(word, i, vowel))
    return ' '.join(res)