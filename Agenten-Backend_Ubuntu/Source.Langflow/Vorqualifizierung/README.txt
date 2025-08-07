curl --request POST \
     --url 'http://127.0.0.1:7860/api/v1/run/f5e82d96-d99b-4ac6-b4ec-c53cf58b54f3?stream=false' \
     --header 'Content-Type: application/json' \
     --header "x-api-key: $LANGFLOW_API_KEY" \
     --data '{
		           "output_type": "text",
		           "input_type": "text",
		           "input_value": "hello world!"
		         }'
--------------------------
msg.method = "POST";
msg.url = "http://127.0.0.1:7860/api/v1/webhook/f5e82d96-d99b-4ac6-b4ec-c53cf58b54f3";
--------------------------
{
  "meinedaten": "mein Urlaub. ich plane für das Frühjahr 2026 einen Campingurlaub für zwei Erwachsene und zwei große Hunde in Kroatien.",
  "session_id": "<1876295776.77424.1753965150980@email.ionos.de>"
}

#############################################################

# from langflow.field_typing import Data
from langflow.custom.custom_component.component import Component
from langflow.io import MessageTextInput, Output
from langflow.schema.data import Data


class CustomComponent(Component):
    display_name = "Custom Component"
    description = "Use as a template to create your own component."
    documentation: str = "https://docs.langflow.org/components-custom-components"
    icon = "code"
    name = "CustomComponent"

    inputs = [
        HandleInput(
            name="input_data",
            display_name="Data or DataFrame",
            input_types=["DataFrame", "Data"],
            info="Accepts either a DataFrame or a Data object.",
            required=True,
        ),
    ]

    outputs = [
        Output(display_name="Output", name="output", method="build_output"),
    ]

    def build_output(self) -> Data:
        data = Data(value=self.input_value)
        self.status = data
        return data

##############################################################

##################################################
###########  nächste Schritte ####################
##################################################
Variable wieder auslesen aus Redis Datenbank -> funktioniert
Anpassung der curl Komponente um Daten aus Redis zu holen und das Ergebnis aus dem Agenten zu versenden -> funktioniert.
##################################################
