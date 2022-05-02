
####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
      return(len(T))
    elif (T == ""):
      return(len(S))
    else:
      if (S[0] == T[0]):
        return(MED(S[1:], T[1:]))
      else:
        return(1 + min(MED(S, T[1:]), MED(S[1:], T), MED(S[1:], T[1:])))


def fast_MED(S, T, MED={}):
  for i in range(len(T)+1):
    MED[0,i] = i
  for i in range(len(S)+1):
    MED[i,0] = i
  for row in range(1, len(S)+1):
    for col in range(1, len(T)+1):
      if S[row-1] == T[col-1]:
        MED[row, col] = MED[row-1, col-1]
      else:
        MED[row,col] = min(S[row-1], T[col-1])
  if (S == ""):
    return(len(T))
  elif (T == ""):
    return(len(S))
  else:
    if (S[0] == T[0]):
      return(fast_MED(S[1:], T[1:]))
    else:
      return(1 + min(fast_MED(S, T[1:]), fast_MED(S[1:], T), fast_MED(S[1:], T[1:])))
    # TODO -  implement memoization

def fast_align_MED(S, T, MED={}):
  for i in range(len(T)+1):
    MED[0,i] = i
  for i in range(len(S)+1):
    MED[i,0] = i
  for row in range(1, len(S)+1):
    for col in range(1, len(T)+1):
      if S[row-1] == T[col-1]:
        MED[row, col] = MED[row-1, col-1]
      else:
        MED[row,col] = min(S[row-1], T[col-1])
  if (S == "") and (T == ""):
    return("", "")
  else:
    if (S[0] == T[0]):
      aligns, alignt = fast_align_MED(S[1:], T[1:])
      return(S[0] + aligns), (T[0] + alignt)
    else:
      if min(fast_MED(S, T[1:]), fast_MED(S[1:], T), fast_MED(S[1:], T[1:])) == fast_MED(S, T[1:]):
        aligns, alignt = fast_align_MED(S, T[1:])
        return S[0] + aligns, '-' + alignt
      if min(fast_MED(S, T[1:]), fast_MED(S[1:], T), fast_MED(S[1:], T[1:])) == fast_MED(S[1:], T):
        aligns, alignt = fast_align_MED(S[1:], T)
        return '-' + aligns, T[0] + alignt
      if min(fast_MED(S, T[1:]), fast_MED(S[1:], T), fast_MED(S[1:], T[1:])) == fast_MED(S[1:], T[1:]):
        aligns, alignt = fast_align_MED(S[1:], T[1:])
        return S[0] + aligns, T[0] + alignt

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
