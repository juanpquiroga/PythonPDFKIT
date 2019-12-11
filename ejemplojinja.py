import jinja2
import pdfkit
import base64

def get_image_file_as_base64_data():
    FILEPATH="static/tracking.png"
    with open(FILEPATH, 'rb') as image_file:
        return base64.b64encode(image_file.read())

#@profile
def pruebagen():
    css = './static/style.css'
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "name.txt"
    template = templateEnv.get_template(TEMPLATE_FILE)
    data = [ 
        {'name':'Juan', 'valor':100},
        {'name': 'Pedro', 'valor':100} 
        ]
    image1 = get_image_file_as_base64_data()
    outputText = template.render(name='Mark',data=data, image1=str(image1, "utf-8"))
    html_file = open('prueba.html', 'w')
    html_file.write(outputText)
    html_file.close()
    #pdfkit.from_file('prueba.html', 'prueba.pdf', css=css)
    
    #print("Image " + str(image1))
    pdfkit.from_string(outputText, 'prueba.pdf', css=css)

if __name__ == '__main__':
    pruebagen()