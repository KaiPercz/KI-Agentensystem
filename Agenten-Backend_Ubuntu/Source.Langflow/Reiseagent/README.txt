# Get API key from environment variable
if [ -z "$LANGFLOW_API_KEY" ]; then
    echo "Error: LANGFLOW_API_KEY environment variable not found. Please set your API key in the environment variables."
    exit 1
fi
#################################################
curl --request POST \
     --url 'http://127.0.0.1:7860/api/v1/run/69ad29e8-b561-4948-aefa-9ae6308091bc?stream=false' \
     --header 'Content-Type: application/json' \
     --header "x-api-key: $LANGFLOW_API_KEY" \
     --data '{
		           "output_type": "text",
		           "input_type": "text",
		           "input_value": "hello world!"
		         }'
#################################################

