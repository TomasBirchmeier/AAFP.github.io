from flask import Flask, request, send_file, render_template_string
import pdfkit

app = Flask(__name__)

# Configuración de wkhtmltopdf (asegúrate de que está instalado)pip

PDFKIT_CONFIG = pdfkit.configuration(
    wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
)

@app.route('/')
def index():
    return """
    <html>
    <body>
        <h2>Generar Detalle de Sueldo</h2>
        <form id="salaryForm">
            <label for="salary">Sueldo Base:</label>
            <input type="number" id="salary" name="salary" required><br><br>

            <label for="contractType">Tipo de Contrato:</label>
            <select id="contractType" name="contractType" required>
                <option value="Indefinido">Indefinido</option>
                <option value="Plazo Fijo">Plazo Fijo</option>
            </select><br><br>

            <button type="button" onclick="sendData()">Generar PDF</button>
        </form>

        <script>
            function sendData() {
                let salary = document.getElementById("salary").value;
                let contractType = document.getElementById("contractType").value;

                if (salary === "" || contractType === "") {
                    alert("Por favor, complete todos los campos.");
                    return;
                }

                let formData = new FormData();
                formData.append("salary", salary);
                formData.append("contractType", contractType);

                fetch("/generate_pdf", {
                    method: "POST",
                    body: formData
                })
                .then(response => response.blob())
                .then(blob => {
                    let url = window.URL.createObjectURL(blob);
                    let a = document.createElement("a");
                    a.href = url;
                    a.download = "detalle_sueldo.pdf";
                    document.body.appendChild(a);
                    a.click();
                    a.remove();
                })
                .catch(error => console.error("Error:", error));
            }
        </script>
    </body>
    </html>
    """

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Obtener datos del formulario
    salary = request.form.get("salary", "No especificado")
    contract_type = request.form.get("contractType", "No especificado")

    print(f"Sueldo recibido: {salary}")
    print(f"Tipo de contrato recibido: {contract_type}")

    # Plantilla HTML para el PDF
    html_content = f"""
    <html>
    <head>
        <style>
            body {{ font-family: Arial, sans-serif; text-align: center; }}
            h1 {{ color: #333; }}
            p {{ font-size: 18px; }}
        </style>
    </head>
    <body>
        <h1>Detalle de Sueldo</h1>
        <p><strong>Sueldo Base:</strong> {salary}</p>
        <p><strong>Tipo de Contrato:</strong> {contract_type}</p>
    </body>
    </html>
    """

    # Nombre del archivo PDF
    pdf_filename = "detalle_sueldo.pdf"

    # Generar PDF desde HTML
    pdfkit.from_string(html_content, pdf_filename, configuration=PDFKIT_CONFIG)

    # Enviar PDF al usuario
    return send_file(pdf_filename, as_attachment=True, download_name=pdf_filename, mimetype="application/pdf")

if __name__ == '__main__':
    app.run(debug=True)
