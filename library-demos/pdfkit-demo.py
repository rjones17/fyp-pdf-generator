import pdfkit

options = {
    'page-size': 'Letter',
    'margin-top': '2.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'encoding': "UTF-8",
    'custom-header': [
        ('Accept-Encoding', 'gzip')
    ],
    'no-outline': None,
    'quiet': ''
}

html_string = """
    <html>
      <head>
      </head>
      <body>
      Hello World!
      </body>
      </html>
    """

config = pdfkit.configuration(
    wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')

pdfkit.from_url('http://google.com', 'example-pdfkit.pdf',
                configuration=config)

data = pdfkit.from_url('http://google.com', False, configuration=config)

with open("example-pdfkit-fromdata.pdf", "wb") as f:
    f.write(data)

pdfkit.from_string(html_string, 'example-pdfkit-fromstring.pdf',
                   configuration=config)

pdfkit.from_string(html_string, 'example-pdfkit-fromstring_with_options.pdf',
                   configuration=config, options=options)
