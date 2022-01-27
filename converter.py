import pdfkit


url = input('Enter URL/Link to webpage: ')
output_name = input('What would you want the name of the output file to be?: ')

pdfkit.from_url(url, f'{output_name}.pdf')
