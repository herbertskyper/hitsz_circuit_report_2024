# -*encoding:gbk*-
from PyPDF2 import PdfFileReader, PdfFileWriter

# 列出你想要拼接的PDF文件
pdf_files = ['pdf1.pdf','pdf2.pdf']
pdf_writer = PdfFileWriter()

for pdf_file in pdf_files:
    # 打开PDF文件
    f = open(pdf_file, 'rb')
    pdf_reader = PdfFileReader(f)
    # 将每一页添加到PdfFileWriter对象中
    if pdf_file==pdf_files[0]:
        for page_num in range(2):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)
    else:
        for page_num in range(2,pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

# 写入到一个新的PDF文件中
with open('merged.pdf', 'wb') as out:
    pdf_writer.write(out)

