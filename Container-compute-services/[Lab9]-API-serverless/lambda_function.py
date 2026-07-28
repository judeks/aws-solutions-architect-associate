import json
import boto3
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("Users")

# En-têtes indispensables pour éviter les blocages de sécurité CORS
CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",  # Dans un vrai projet, spécifiez l'URL de votre bucket S3
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "OPTIONS,POST,GET"
}

def lambda_handler(event, context):
    # Gestion de la requête de pré-vérification CORS (OPTIONS) si elle arrive jusqu'à Lambda
    http_method = http_method = event.get("httpMethod") or event.get("requestContext", {}).get("http", {}).get("method", "")
    
    if http_method == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": CORS_HEADERS,
            "body": json.dumps({"message": "CORS preflight OK"})
        }

    try:
        if http_method == "POST":
            body = json.loads(event.get("body", "{}"))
            
            # Validation sommaire
            if not body.get("name") or not body.get("email"):
                return {
                    "statusCode": 400,
                    "headers": CORS_HEADERS,
                    "body": json.dumps({"message": "Champs 'name' et 'email' requis"})
                }
                
            user_id = str(uuid.uuid4())  
            table.put_item(Item={
                "user_id": user_id, 
                "name": body["name"], 
                "email": body["email"]
            })
            return {
                "statusCode": 200, 
                "headers": CORS_HEADERS,
                "body": json.dumps({"message": "Utilisateur ajoute", "user_id": user_id})
            }
            
        elif http_method == "GET":
            query_params = event.get("queryStringParameters") or {}
            user_id = query_params.get("user_id")
            
            if not user_id:
                return {
                    "statusCode": 400,
                    "headers": CORS_HEADERS,
                    "body": json.dumps({"message": "Le parametre 'user_id' est requis"})
                }
                
            response = table.get_item(Key={"user_id": user_id})
            item = response.get("Item", {})
            
            if not item:
                return {
                    "statusCode": 404,
                    "headers": CORS_HEADERS,
                    "body": json.dumps({"message": "Utilisateur non trouve"})
                }
                
            return {
                "statusCode": 200, 
                "headers": CORS_HEADERS,
                "body": json.dumps(item)
            }
            
        return {
            "statusCode": 405, 
            "headers": CORS_HEADERS,
            "body": json.dumps({"message": "Methode non supportee"})
        }
        
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": CORS_HEADERS,
            "body": json.dumps({"message": "Erreur interne", "error": str(e)})
        }