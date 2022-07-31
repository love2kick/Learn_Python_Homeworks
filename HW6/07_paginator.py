class Pagination:
    pages=[]
    page_count=int
    item_count=int

    def __init__(self, text, symbols=0):
        prevpageend=0
        self.item_count=len(text)
        for i in range(0,len(text)):
            if i % symbols == 0 and i!=0:
                if prevpageend==0:
                    self.pages.append(text[prevpageend:i])
                    prevpageend=i
                else:
                    self.pages.append(text[prevpageend:i])
                    prevpageend=i
            elif i==len(text)-1:
                    self.pages.append(text[prevpageend:len(text)])
                    prevpageend=i
        self.page_count=len(self.pages)

    def count_items_on_page(self, pagenum):
        items=0
        try:
            for i in self.pages[pagenum]:
                items+=1
            if items>1:
                print(f"There are {items} chars on page {pagenum}.")
            else:
                print(f"There is {items} char on page {pagenum}.")
        except:
            print(f"Invalid index. Page {pagenum} is missing.")

    def display_page(self,page):
        print(self.pages[page])

    def find_page(self, word):
        searchlist=[]
        concat=""
        for i,j in zip(self.pages, range(len(self.pages))):
            if word in i:
                searchlist.append(j)
        if len(searchlist)==0:
            for i,j in zip(self.pages, range(len(self.pages))):
                if j>0:
                    concat=self.pages[j-1]+i
                    if word in concat:
                        searchlist.append(j-1)
                        searchlist.append(j)
            try:
                if len(searchlist)==0:
                    raise Exception()
            except:
                print(f"Exception: \"{word}\" is missing on the pages.")
            else:
                print(f"{word} found on pages {searchlist}.")
        else:
            print(f"{word} found on pages {searchlist}.")

pages = Pagination('Your beautiful text', 5)
print(pages.page_count)
print(pages.item_count)
pages.count_items_on_page(0)
pages.count_items_on_page(3)
pages.count_items_on_page(4)
pages.find_page('Your')
pages.find_page('e')
pages.find_page('beautiful')
pages.find_page('great')
pages.display_page(0)