from PyPDF2 import PdfMerger

merge=PdfMerger()

merge.append("Introduction & Unit 1 - MTK 26.pdf")
merge.append("Unit 2 - MTK 26.pdf")

merge.write("Merged.pdf")

merge.close()


#make sure change the file directory to cd 76-Day-76-Exercise-8

