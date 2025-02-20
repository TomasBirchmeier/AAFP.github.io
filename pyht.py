import pdfkit

html_content = "<h1>Test PDF</h1><p>Esto es una prueba</p>"
pdfkit.from_string(html_content, "test.pdf")
print("PDF generado correctamente.")