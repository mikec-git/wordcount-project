from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def count(request):
  fullText = request.GET['fullText']
  wordList = fullText.split()
  wordDict = {}

  for word in wordList:
    if word in wordDict:
      wordDict[word] += 1
    else:
      wordDict[word] = 1

  sortedWords = sorted(wordDict.items(), key=operator.itemgetter(1), reverse=True)

  return render(request, 'count.html', {
    'fullText': fullText,
    'count': len(wordList),
    'sortedWords': sortedWords
  })