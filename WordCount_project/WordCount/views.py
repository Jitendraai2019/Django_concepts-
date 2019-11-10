
from django.shortcuts import render
import operator
def homepage(request):
    return render(request,'home.html')

def aboutPage(request):
    return render(request,'about_page.html')

def count(request):
    # to get the content of fulltext textarea. fulltext is name of textarea in the home.html
    full_text=request.GET['fulltext']
    #print(fulltext)                      # This full text print in the terminal
    word_list = full_text.split()

    word_dict = {}
    for word in word_list:
        if word in word_dict:
            # increase dictionary values
            word_dict[word] += 1
        else:
            # add to the dictionary.
            word_dict[word] = 1

    sorted_words=sorted(word_dict.items(),key=operator.itemgetter(1),reverse=True)

    return render(request,'count.html',{'fulltext':full_text,'count':len(word_list),'sorted_dictionary':sorted_words})
