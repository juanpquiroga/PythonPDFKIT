import pdfkit
@profile
def pruebagen():
    
    print("Inicio")
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
    }
    pdfkit.from_url('http://micropyramid.com', 'micro.pdf', options=options)
    print("Fin")

if __name__ == '__main__':
    pruebagen()