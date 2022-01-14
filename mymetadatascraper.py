"""
Author: Christopher Duncan
Build Date: 01/06/2022
This project is a metadata scraper that I built with the guidance of a few youtube resources. After watching these
videos I ensured that I modified my own code and did not directly copy syntax unless it was needed to use the
functionality.

This was a very fun project and gave me more insight into the usages and inner workings of metadata as a whole.

The videos I used for reference are below:
https://www.youtube.com/watch?v=mgl5ZLwjZyg - From a PDF
https://www.youtube.com/watch?v=KBJ2i7IqDY8 - From a site
https://www.youtube.com/watch?v=UmPe07a3bWs - From a PDF

In simple terms metadata is data that describes other data. Ex. Googling for boating sites. Those sites have info
that the Google appliance utilizes to match a description of a site with the query.

We will have to utilize the PyPDF2 module to extract the data.
I found a sample pdf online to test with this tool.
"""

import PyPDF2 as PyPD


"""The code below will open the pdf file in the first half and allow us to read it in the second with the rb string.
Were going to also access the PyPD module here and get a predefined function that will allows to read (PdfFileReader). 
We can also file write and file merge if we wanted to use those functions. 
"""
MyPDFfile = open("sample-pdf-file.pdf","rb")
pdfread = PyPD.PdfFileReader(MyPDFfile)

"""1.Now if we wanted to extract a single page of the PDF we can do so with the getPage function. An example
of that is below. 2.The first page is always 0 just like when we do an array or list. Test the code here. You 
can modify the page number as well. 3. There are other details we can find such as if the file is encrypted, document
 general info, and number of pages and or decrypt the file."""
a = pdfread.getPage(0)
print(a.extractText())
print(pdfread.getIsEncrypted())
print(pdfread.getDocumentInfo())
print(pdfread.getNumPages())

"""This section shows how we can extract the entire PDF by utilizing a while loop.
This while loop will keep going until the i variable is greater than the number of pages in the document."""
i = 0
while i < pdfread.getNumPages():
    pageinfo = pdfread.getPage(i)
    print(pageinfo.extractText())
    i = i + 1

