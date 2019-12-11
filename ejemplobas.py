import pdfkit
@profile
def pruebagen():
    
    print("Inicio")
    pdfkit.from_url('http://micropyramid.com', 'micro.pdf')
    print("Fin")

if __name__ == '__main__':
    pruebagen()